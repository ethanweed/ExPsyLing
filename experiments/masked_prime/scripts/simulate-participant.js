#!/usr/bin/env node
// Simulated participant for the masked-priming lab.js/JATOS study at
// 
//
// Structure and timing below is taken directly from the study's own
// script.js. Every
// non-target screen auto-advances on a fixed lab.js timeout, so the
// script never needs to read canvas content -- it just waits the known
// durations and sends the known keys in the known order/counts.
 
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const STUDY_URL = 'https://broca.cc.au.dk/publix/u3DICCeaNAk';

const PRACTICE_TRIALS = 4;
const MAIN_TRIALS_PER_SEQUENCE = 60;
const NUM_MAIN_SEQUENCES = 2; // Short + Long, order is randomized by the study itself

function parseArgs(argv) {
  // rtMin must stay above the real pre-target screen chain duration
  // (fixation 539ms + mask1 32ms + prime 32ms + mask2 32ms [+ DELAY 80ms
  // for Long trials] = 635-715ms) -- otherwise the response keypress can
  // land on mask2/prime instead of target. Those screens also have an
  // unfiltered "any key" listener, so an early press gets silently
  // consumed there instead of answering the trial, desyncing the whole
  // run. rtMax must stay under 2000ms (Short trials' target timeout).
  const opts = { runs: 1, headed: false, rtMin: 800, rtMax: 1600 };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--runs') opts.runs = parseInt(argv[++i], 10);
    else if (a === '--headed') opts.headed = true;
    else if (a === '--rt-min') opts.rtMin = parseInt(argv[++i], 10);
    else if (a === '--rt-max') opts.rtMax = parseInt(argv[++i], 10);
    else if (a === '--help') {
      console.log(`Usage: node simulate-participant.js [--runs N] [--headed] [--rt-min ms] [--rt-max ms]`);
      process.exit(0);
    }
  }
  return opts;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomResponseKey() {
  return Math.random() < 0.5 ? 'm' : 'n';
}

// Wait a simulated "reaction time", then send a target response key.
// Default window [800,1600]ms sits safely above the ~635-715ms
// pre-target screen chain and below the 2000ms Short-trial cap.
async function respondToTrial(page, opts) {
  await sleep(randInt(opts.rtMin, opts.rtMax));
  await page.keyboard.press(randomResponseKey());
}

async function runOnce(browser, runIndex, opts, outDir) {
  const start = Date.now();
  const context = await browser.newContext();
  const page = await context.newPage();
  const log = (msg) => console.log(`[run ${runIndex}] ${msg}`);

  try {
    log(`navigating to ${STUDY_URL}`);
    await page.goto(STUDY_URL, { waitUntil: 'networkidle', timeout: 60000 });

    // Welcome0-3: 4 screens x 500ms, no response needed, plus initial
    // JATOS/lab.js boot time.
    log('waiting through welcome screens');
    await sleep(3000);

    // Instructions1, Instructions1a, Instructions2, Instructions3,
    // Instructions4: any key. Instructions5: Space specifically
    // ("press SPACE to start the practice round"). Space satisfies both.
    log('advancing through instructions');
    for (let i = 0; i < 6; i++) {
      await page.keyboard.press('Space');
      await sleep(250);
    }

    // Practice loop: 4 trials, target has no timeout (waits for response).
    log(`running ${PRACTICE_TRIALS} practice trials`);
    for (let i = 0; i < PRACTICE_TRIALS; i++) {
      await respondToTrial(page, opts);
    }

    // "Practice complete" screen: any key.
    await sleep(250);
    await page.keyboard.press('Space');
    await sleep(250);

    // Experiment Sequence: Short + Long sub-sequences, order randomized
    // by the study. From the script's perspective both look the same:
    // MAIN_TRIALS_PER_SEQUENCE trials each, then a Break screen (Space).
    // The Long sequence has an extra 80ms non-interactive DELAY screen
    // per trial, which the fixed ~750ms response wait already covers.
    for (let seq = 0; seq < NUM_MAIN_SEQUENCES; seq++) {
      log(`running main sequence ${seq + 1}/${NUM_MAIN_SEQUENCES} (${MAIN_TRIALS_PER_SEQUENCE} trials)`);
      for (let i = 0; i < MAIN_TRIALS_PER_SEQUENCE; i++) {
        await respondToTrial(page, opts);
      }
      log(`sequence ${seq + 1} done, pressing Space at Break screen`);
      await sleep(300);
      await page.keyboard.press('Space');
      await sleep(300);
    }

    // Second Break press above ends the study (epilogue submits data via
    // jatos.submitResultData). Give it a moment to settle and record
    // final state.
    await sleep(2000);
    const finalUrl = page.url();
    const finalTitle = await page.title().catch(() => '(unknown)');
    log(`finished. final URL: ${finalUrl} | title: ${finalTitle}`);

    const shotPath = path.join(outDir, `run-${runIndex}-final.png`);
    await page.screenshot({ path: shotPath }).catch(() => {});

    await context.close();
    return { runIndex, success: true, durationMs: Date.now() - start, finalUrl, finalTitle };
  } catch (err) {
    log(`ERROR: ${err.message}`);
    const shotPath = path.join(outDir, `run-${runIndex}-error.png`);
    await page.screenshot({ path: shotPath }).catch(() => {});
    await context.close();
    return { runIndex, success: false, durationMs: Date.now() - start, error: err.message };
  }
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  const stamp = new Date().toISOString().replace(/[:.]/g, '-');
  const outDir = path.join(__dirname, 'runs', stamp);
  fs.mkdirSync(outDir, { recursive: true });

  console.log(`Starting ${opts.runs} run(s), headed=${opts.headed}, rt=[${opts.rtMin},${opts.rtMax}]ms`);
  console.log(`Screenshots/logs -> ${outDir}`);

  const browser = await chromium.launch({ headless: !opts.headed });
  const results = [];
  for (let i = 1; i <= opts.runs; i++) {
    results.push(await runOnce(browser, i, opts, outDir));
  }
  await browser.close();

  console.log('\n=== Summary ===');
  for (const r of results) {
    const secs = (r.durationMs / 1000).toFixed(1);
    if (r.success) {
      console.log(`run ${r.runIndex}: OK in ${secs}s`);
    } else {
      console.log(`run ${r.runIndex}: FAILED after ${secs}s -- ${r.error}`);
    }
  }
  const failures = results.filter((r) => !r.success).length;
  process.exit(failures > 0 ? 1 : 0);
}

main();
