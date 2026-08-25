#!/usr/bin/env python3
"""Convert nested outline (.bike / OPML-like XML) into animated HTML disclosures."""

# usage: python3 outline2html_v2.py "input.bike" output.html --title "Page Title" --theme soft


import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

URL_RE = re.compile(r'(https?://[^\s<>"]+)')
EMAIL_RE = re.compile(r'([\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[a-zA-Z]{2,})')


def linkify(text):
    """Turn bare URLs and email addresses in plain text into clickable links."""
    if not text:
        return text
    text = URL_RE.sub(
        lambda m: (
            f'<a href="{m.group(1)}" data-tip="{m.group(1)}" '
            f'target="_blank" rel="noopener noreferrer">{m.group(1)}</a>'
        ),
        text,
    )
    text = EMAIL_RE.sub(
        lambda m: f'<a href="mailto:{m.group(1)}" data-tip="{m.group(1)}">{m.group(1)}</a>',
        text,
    )
    return text

THEMES = {
    "plain": {
        "bg": "#ffffff",
        "text": "#222222",
        "leaf": "#333333",
        "hover": "#f0f0f0",
        "radius": "4px",
        "border": "transparent",
    },
    "soft": {
        "bg": "#faf7f2",
        "text": "#3a3530",
        "leaf": "#6b6259",
        "hover": "#efe8dd",
        "radius": "10px",
        "border": "#e5ddd0",
    },
    "dark": {
        "bg": "#1e1e1e",
        "text": "#e8e8e8",
        "leaf": "#a8a8a8",
        "hover": "#2a2a2a",
        "radius": "8px",
        "border": "#333333",
    },
}

CSS = """
__THEME_VARS__

body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0 auto;
  padding: 3rem 2.5rem;
  max-width: 900px;
  font-size: 1.4rem;
  line-height: 1.6;
  background-color: var(--bg);
  color: var(--text);
}

details {
  margin-left: 1.6rem;
  margin-top: 0.4rem;
}

summary {
  cursor: pointer;
  padding: 6px 8px;
  border-radius: var(--radius);
  list-style: none;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-weight: 600;
  transition: background-color 150ms ease;
}

summary::-webkit-details-marker {
  display: none;
}

summary::before {
  content: "\\25B6";
  display: inline-block;
  flex-shrink: 0;
  font-size: 0.75em;
  transition: transform 250ms ease-out;
}

details[open] > summary::before {
  transform: rotate(90deg);
}

summary:hover {
  background-color: var(--hover);
}

details > .content {
  overflow: hidden;
  border-left: 2px solid var(--border);
  margin-left: 0.5rem;
  padding-left: 0.6rem;
}

.leaf {
  margin-left: 1.6rem;
  padding: 6px 8px;
  margin-top: 0.3rem;
  max-width: 65ch;
  color: var(--leaf);
}

h1 {
  font-size: 2.75rem;
  margin-bottom: 1rem;
}

a[href] {
  position: relative;
  color: inherit;
  text-decoration-color: var(--border);
}

a[href]:not([data-tip])::after {
  content: attr(href);
}

a[href]::after {
  content: attr(data-tip);
  position: absolute;
  left: 100%;
  top: 50%;
  margin-left: 0.5em;
  background: var(--text);
  color: var(--bg);
  padding: 0.3em 0.6em;
  border-radius: 6px;
  font-size: 0.65em;
  font-weight: 400;
  white-space: nowrap;
  opacity: 0;
  transform: translateY(-50%) translateX(-4px);
  pointer-events: none;
  transition: opacity 150ms ease, transform 150ms ease;
  z-index: 10;
}

a[href]:hover::after {
  opacity: 1;
  transform: translateY(-50%) translateX(0);
}
"""

JS = """
class Accordion {
  constructor(el) {
    this.el = el;
    this.summary = el.querySelector(':scope > summary');
    this.content = el.querySelector(':scope > .content');
    this.animation = null;
    this.isClosing = false;
    this.isExpanding = false;
    if (this.summary && this.content) {
      this.summary.addEventListener('click', (e) => this.onClick(e));
    }
  }
  onClick(e) {
    e.preventDefault();
    this.el.style.overflow = 'hidden';
    if (this.isClosing || !this.el.open) {
      this.open();
    } else if (this.isExpanding || this.el.open) {
      this.shrink();
    }
  }
  shrink() {
    this.isClosing = true;
    const startHeight = `${this.el.offsetHeight}px`;
    const endHeight = `${this.summary.offsetHeight}px`;
    if (this.animation) this.animation.cancel();
    this.animation = this.el.animate(
      { height: [startHeight, endHeight] },
      { duration: 250, easing: 'ease-out' }
    );
    this.animation.onfinish = () => this.onAnimationFinish(false);
    this.animation.oncancel = () => { this.isClosing = false; };
  }
  open() {
    this.el.style.height = `${this.el.offsetHeight}px`;
    this.el.open = true;
    window.requestAnimationFrame(() => this.expand());
  }
  expand() {
    this.isExpanding = true;
    const startHeight = `${this.el.offsetHeight}px`;
    const endHeight = `${this.summary.offsetHeight + this.content.offsetHeight}px`;
    if (this.animation) this.animation.cancel();
    this.animation = this.el.animate(
      { height: [startHeight, endHeight] },
      { duration: 250, easing: 'ease-out' }
    );
    this.animation.onfinish = () => this.onAnimationFinish(true);
    this.animation.oncancel = () => { this.isExpanding = false; };
  }
  onAnimationFinish(open) {
    this.el.open = open;
    this.animation = null;
    this.isClosing = false;
    this.isExpanding = false;
    this.el.style.height = this.el.style.overflow = '';
  }
}
document.querySelectorAll('details').forEach((el) => new Accordion(el));
"""


def inner_xml(el):
    """Serialize inner content (text + child tags), auto-linking bare URLs/emails."""
    parts = [linkify(html.escape(el.text or ""))]
    for child in el:
        parts.append(ET.tostring(child, encoding="unicode"))
        parts.append(linkify(html.escape(child.tail or "")))
    return "".join(parts).strip()


def parse_li(li):
    p = li.find("p")
    text = inner_xml(p) if p is not None else ""
    children = []
    ul = li.find("ul")
    if ul is not None:
        for child_li in ul.findall("li"):
            children.append(parse_li(child_li))
    return {"text": text, "children": children}


def render_node(node, is_top, indent=0):
    pad = "  " * indent
    if node["children"]:
        summary_text = f'<strong>{node["text"]}</strong>' if is_top else node["text"]
        inner = "".join(
            render_node(c, False, indent + 2) for c in node["children"]
        )
        return (
            f'{pad}<details>\n'
            f'{pad}  <summary>{summary_text}</summary>\n'
            f'{pad}  <div class="content">\n'
            f'{inner}'
            f'{pad}  </div>\n'
            f'{pad}</details>\n'
        )
    else:
        return f'{pad}<div class="leaf">{node["text"]}</div>\n'


def convert(input_path, title, theme="soft"):
    tree = ET.parse(input_path)
    root_ul = tree.getroot().find("body").find("ul")
    top_items = [parse_li(li) for li in root_ul.findall("li")]

    body = "".join(render_node(item, True) for item in top_items)

    colors = THEMES[theme]
    root_vars = ":root {\n" + "".join(
        f"  --{name}: {value};\n" for name, value in colors.items()
    ) + "}"
    css = CSS.replace("__THEME_VARS__", root_vars)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>{css}</style>
</head>
<body>

<h1>{title}</h1>

{body}
<script>{JS}</script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to outline file (.bike / XML)")
    parser.add_argument("output", help="Path to write output HTML")
    parser.add_argument("--title", help="Page title (default: input filename)")
    parser.add_argument(
        "--theme",
        choices=sorted(THEMES.keys()),
        default="soft",
        help="Color theme (default: soft)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    title = args.title or input_path.stem

    html = convert(input_path, title, args.theme)
    Path(args.output).write_text(html, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
