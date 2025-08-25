#!/usr/bin/env python3
"""
export.py — Convert Hope Index CSV into JSON with schema + metadata

Usage:
    python export.py hope_index_wildfire_full_v0.4.csv hope_index_wildfire_full_v0.4.json
"""

import sys
import json
import pandas as pd
from datetime import datetime

# Which fields to coerce into integers
NUM_FIELDS = {
    "impact_score", "speed_score", "scale_score",
    "credibility_score", "hope_score",
    "verified_sources_count", "hype_risk"
}

def coerce_types(record):
    for k in NUM_FIELDS:
        if k in record:
            v = str(record[k]).strip()
            if v == "" or v.lower() == "nan":
                record[k] = None
            else:
                try:
                    record[k] = int(float(v))
                except Exception:
                    record[k] = v  # leave as-is if can't coerce
    return record

def main(csv_path, json_path):
    df = pd.read_csv(csv_path, dtype=str).fillna("")
    records = [coerce_types(rec) for rec in df.to_dict(orient="records")]

    output = {
        "schema_version": "0.2",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "record_count": len(records),
        "records": records,
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ Exported {len(records)} records to {json_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export.py input.csv output.json")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
