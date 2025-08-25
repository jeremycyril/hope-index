# 🌍 Hope Index

**Tagline:** Making optimism searchable.  
**One-liner:** A structured dataset and framework for tracking positive, AI-driven breakthroughs that improve human life and the planet.  

---

## Overview

The **Hope Index** is a structured dataset and framework for tracking positive, AI-driven breakthroughs that improve human life and the planet.  

It was created as a practical experiment in designing content systems for **dual audiences**:  
- **Humans** who want clear, inspiring information.  
- **AI agents** that need structured data they can parse and retrieve.  

The dataset is stored as CSV/JSON, aligned with a schema that allows both people and machines to filter, analyze, and learn from it.

---

## Schema (v0.2)

Each row in the Hope Index represents a single development, tagged and scored for credibility, speed, scale, and impact.  

| Field | Type | Example | Notes |
|-------|------|---------|-------|
| `id` | string | `HI-WF-0001` | Unique identifier |
| `date_logged` | date | `2025-08-24` | When added |
| `date_event` | date | `2025-07-31` | When event occurred |
| `domain` | enum | `Climate`, `Health`, `Accessibility`, `Energy`, `Space`, etc. | Category |
| `paradigm` | enum | `Breakthrough`, `Deployment`, `Policy`, `Collaboration`, `Funding`, `Research` | Development type |
| `scale` | text | `Local`, `National`, `Global`, `Planetary` | Converted to `scale_score` |
| `time_horizon` | text | `Immediate`, `1-5y`, `10+y` | Converted to `speed_score` |
| `geography` | string | `Texas, USA` | Location |
| `title` | string | Short headline |
| `summary` | string | 1–2 sentence description |
| `impact_metric` | string | `$59.8M program budget` | Narrative metric |
| `impact_score` | int | `3` | Numeric score (3/5/7/9/10) |
| `speed_score` | int | `6` | From `time_horizon` |
| `scale_score` | int | `6` | From `scale` |
| `credibility_score` | int | `1–5` | Source reliability |
| `hope_score` | int (0–10) | `4` | Composite optimism score |
| `sources` | url(s) | `https://www.darpa.mil/...` | At least one source |
| `tags` | string | `wildfire,autonomy,DARPA` | Keywords |
| `verification_status` | enum | `claimed`, `pilot`, `deployed`, `scaled`, `verified` | Stage |
| `verified_sources_count` | int | `2` | Count of independent sources |
| `update_status` | enum | `announced`, `pilot`, `deployed`, `scaled` | Deployment lifecycle |
| `organization_type` | enum | `government`, `startup`, `enterprise`, `NGO`, `academic`, `international` | Who’s behind it |
| `funding_status` | enum | `public`, `grant`, `seed`, `series`, `revenue` | Funding stage |
| `uncertainty_level` | enum | `low`, `medium`, `high` | Confidence level |
| `hype_risk` | int (1–5) | `3` | Degree of hype vs. substance |
| `related_entries` | string | `HI-WF-0002` | Links to connected entries |

---

## Hope Score Formula

Hope Score is derived from four sub-scores:

hope_score = ROUND(
  0.3*scale_score +
  0.3*impact_score +
  0.2*speed_score +
  0.2*credibility_norm
)

Where:
	•	scale_score: Local=3, National=6, Global=9, Planetary=10
	•	impact_score: 3/5/7/9/10, based on improvement magnitude/systemic shift
	•	speed_score: Immediate=10, 1-5y=6, 10+y=3
	•	credibility_norm: credibility_score × 2, +1 if verified_sources_count ≥2 (capped at 10)

Example (DARPA Wildfire Testbed)
	•	scale_score = 3 (National)
	•	impact_score = 3
	•	speed_score = 6 (1-5y horizon)
	•	credibility_score = 5 → credibility_norm = 10
	•	hope_score = 4

⸻

Implementation Notes
	•	The repo includes both manual scoring fields (impact_score, scale_score, etc.) and a calculated hope_score.
	•	In Numbers/Excel/Sheets, the calculation uses:
=ROUND(0.3*N2 + 0.3*L2 + 0.2*M2 + 0.2*MIN(O2*2 + IF(T2>=2,1,0),10),0)

Where:
	•	L = impact_score
	•	M = speed_score
	•	N = scale_score
	•	O = credibility_score
	•	T = verified_sources_count
	•	Some categories (e.g., pure economic damage reports) are tracked but not scored, since they don’t represent a forward-looking breakthrough.

⸻

Wildfire Vertical (Worked Example)

To demonstrate the schema in practice, the repo includes hope_index_wildfire_full.csv.

This sub-dataset captures AI-driven wildfire detection, prevention, and response systems — DARPA helicopters, Google FireSat, ECMWF ML forecasts, Indigenous AI fire management, etc.

It acts as a calibration domain for the broader Hope Index.

Status
	•	✅ Schema v0.2 defined
	•	✅ Wildfire vertical populated (10+ entries)
	•	⏳ Expanding to additional domains (Health, Accessibility, Energy, Space)

⸻

Contributing

Want to add hope? Fork the repo and submit pull requests with:
	•	New entries (aligned to schema v0.2)
	•	Verification improvements (sources, lifecycle updates)
	•	Scoring calibration proposals

## Scoring Calibration Anchors

To keep the Hope Score consistent across domains, the repo includes a set of calibration anchors.  
These are reference examples that define what a **3, 5, 7, and 9** should look like in practice.

| Score | Anchor Example | Why |
|-------|----------------|-----|
| **3** | **DARPA Wildfire Testbed** — $59.8M pilot program, autonomous helicopters (National scale, medium certainty) | Early-stage, national-only, pilot not yet deployed |
| **5** | **ECMWF Wildfire Forecasting** — ML extends prediction to 10 days (Global, deployed, moderate impact) | Clear improvement, already deployed, credible global org |
| **7** | **Pano AI Coverage** — Startup system deployed across 30M acres, 100K fires detected (National scale, proven deployment) | Significant real-world scale and adoption, though not global |
| **9** | **Google FireSat** — 5x5m global detection satellites, validated with live images (Global scale, high funding, deployed) | Systemic global infrastructure with measurable results |
| **10** | Reserved for **systemic shifts** (e.g., universal vaccines, grid-scale climate breakthroughs, AI-driven accessibility transformation) | Transformational, planetary-level change |

**Notes:**
- **Scale, impact, speed, credibility** all matter — but the anchors prevent grade inflation.  
- **10** is deliberately rare. It should be a generational breakthrough.  
- **Economic reports** (e.g., wildfire costs) are not scored, but provide important context.  
- This calibration will evolve as more domains (Health, Accessibility, Energy, Space) are added.  
