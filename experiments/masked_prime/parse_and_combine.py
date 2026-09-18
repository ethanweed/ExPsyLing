"""
parse_and_combine.py

Uses the helpers in data_wrangling.py to collect, parse, and combine the
per-participant data exported from JATOS into a single tidy dataframe.

Steps:
    1. collect_data_files() walks the JATOS Results Archive folder, renames
       each participant's data.txt to "<participant_id>_<component_num>.txt",
       and moves everything into a "raw_data" subfolder.
    2. Each renamed file is parsed with parse_labjs_data() (falling back to
       parse_jatos_data() if it isn't lab.js-formatted), tagged with its
       participant_id and component_num, and concatenated into one dataframe.
    3. The combined dataframe is saved to combined_data.csv in DATA_DIR.

Usage:
    python parse_and_combine.py
"""

import re
from pathlib import Path

import pandas as pd

import data_wrangling as dw

DATA_DIR = Path(__file__).parent / "/Users/ethan/Desktop/test"


def main():
    raw_data_dir = DATA_DIR / "raw_data"

    # Rename/move data.txt files into DATA_DIR/raw_data (skip if already done)
    if not raw_data_dir.exists():
        dw.collect_data_files(str(DATA_DIR))

    combined_frames = []

    for data_file in sorted(raw_data_dir.glob("*.txt")):
        match = re.match(r"(\d+)_(\d+)\.txt", data_file.name)
        if not match:
            print(f"Skipping unrecognized file name: {data_file.name}")
            continue
        participant_id, component_num = match.groups()

        df = dw.parse_labjs_data(str(data_file))
        if df is None:
            df = dw.parse_jatos_data(str(data_file))

        df.insert(0, "participant_id", participant_id)
        df.insert(1, "component_num", int(component_num))

        combined_frames.append(df)

    combined_df = pd.concat(combined_frames, ignore_index=True)

    output_path = DATA_DIR / "combined_data.csv"
    combined_df.to_csv(output_path, index=False)
    print(f"\nSaved combined data ({len(combined_df)} rows) to {output_path}")


if __name__ == "__main__":
    main()
