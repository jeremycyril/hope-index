# 🌍 Hope Index

**Making optimism searchable.**  

---

## Overview

The **Hope Index** is a structured dataset and framework for tracking positive, AI-driven breakthroughs that improve human life and the planet.  

It was created as a practical experiment in designing content systems for **dual audiences**:  
- **Humans** who want clear, inspiring information.  
- **AI agents** that need structured data they can parse and retrieve.  

The dataset is aligned with a schema that allows both people and machines to filter, analyze, and learn from it.

The dataset exists in two layers:
- Human Layer: CSV/Airtable views with filters like “This Week’s Wins” or “Top Hope Signals,” designed for newsletters, dashboards, and quick communication.
- AI Layer: A JSON schema that lets large language models and agents query the same information programmatically, returning structured results.

This dual-audience design makes the Hope Index more than a dataset. It’s a blueprint for future content systems, where information must be equally legible to people and machines.

Use Cases
- Curating uplifting AI breakthroughs for the AI Saves The Universe newsletter.
- Building portfolio case studies on AI-human content strategy.
- Prototyping the Optimism API, where optimism becomes searchable and retrievable by query.
- Inspiring other researchers, writers, and designers to structure positive narratives with the same rigor usually applied to risks.

The Hope Index is an MVP (minimum viable product) but its structure is infinitely extensible. The vision: a living database of optimism, continuously updated and consumable by both humans and AI systems.

⸻


---

## Schema (v0.2)

Each entry in the Hope Index represents a single positive development.  
The schema includes validation, lifecycle, and credibility tracking fields:

| Field | Type | Example | Notes |
|-------|------|---------|-------|
| `id` | string | `HI-2025-0001` | Unique identifier |
| `date_logged` | date | `2025-08-24` | When added to dataset |
| `date_event` | date | `2025-07-31` | When event occurred |
| `domain` | enum | `Climate`, `Health`, `Accessibility`, `Energy`, `Space`, etc. | Top-level category |
| `paradigm` | enum | `Breakthrough`, `Deployment`, `Policy`, `Collaboration`, `Funding`, `Tooling` | Type of development |
| `scale` | enum | `Local`, `National`, `Global`, `Planetary` | Geographic or systemic reach |
| `time_horizon` | enum | `Immediate`, `1-5y`, `10+y` | Time to impact |
| `geography` | string | `California, USA` | Location |
| `title` | string | Short headline |
| `summary` | string | 1–2 sentence description |
| `impact_metric` | string | `Median detection time reduced from 14m to 4m` | Tangible metric |
| `credibility_score` | int (1–5) | `4` | Source reliability |
| `hope_score` | int (1–10) | `7` | Composite optimism score (see below) |
| `sources` | string | URL(s) | At least one credible source |
| `tags` | string | `wildfire, satellite, detection` | Comma-delimited keywords |
| `verification_status` | enum | `claimed`, `pilot`, `deployed`, `scaled`, `policy` | Lifecycle stage |
| `verified_sources_count` | int | `2` | How many independent sources |
| `update_status` | enum | `announced`, `pilot`, `deployed`, `scaled`, `retired` | Deployment lifecycle |
| `organization_type` | enum | `academic`, `startup`, `enterprise`, `government`, `NGO`, `international` | Who’s behind it |
| `funding_status` | enum | `research`, `seed`, `series`, `grant`, `public`, `revenue` | Stage of funding |
| `uncertainty_level` | enum | `low`, `medium`, `high` | Maturity / risk |
| `hype_risk` | int (1–5) | `3` | Level of hype vs evidence |
| `related_entries` | string | `HI-2025-0002;HI-2025-0005` | IDs of connected items |

---

## Scoring

### **Hope Score Formula**
```text
hope_score = round(
  0.3*scale_score +
  0.3*impact_score +
  0.2*speed_score +
  0.2*credibility_norm
)
