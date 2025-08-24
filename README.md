# hope-index
Making optimism searchable.


The Hope Index is a structured dataset and framework for tracking positive, AI-driven breakthroughs that improve human life and the planet. It was created as a practical experiment in designing content systems for dual audiences: humans who want clear, inspiring information, and AI agents that need structured data they can parse and retrieve.

Most conversations about AI focus on risk and hype. The Hope Index flips the script. It provides a consistent, transparent way to capture “hope signals” — real deployments, policy changes, scientific advances, and collaborations where AI is being applied to health, climate, accessibility, energy, and beyond. Each entry is tagged and scored across multiple dimensions:
	•	Domain (e.g., Climate, Health, Accessibility, Energy, Space)
	•	Paradigm (Breakthrough, Deployment, Policy, Collaboration, Tooling)
	•	Scale (Local, National, Global, Planetary)
	•	Time Horizon (Immediate, 1–5 years, 10+ years)
	•	Impact Metric (e.g., % improvement, beneficiaries reached, policy scope)
	•	Credibility Score (1–5, based on source quality)
	•	Hope Score (1–10, composite of scale, impact, speed, and credibility)

The dataset exists in two layers:
	•	Human Layer: CSV/Airtable views with filters like “This Week’s Wins” or “Top Hope Signals,” designed for newsletters, dashboards, and quick communication.
	•	AI Layer: A JSON schema that lets large language models and agents query the same information programmatically, returning structured results.

This dual-audience design makes the Hope Index more than a dataset. It’s a blueprint for future content systems, where information must be equally legible to people and machines.

Use Cases
	•	Curating uplifting AI breakthroughs for the AI Saves The Universe newsletter.
	•	Building portfolio case studies on AI-human content strategy.
	•	Prototyping the Optimism API, where optimism becomes searchable and retrievable by query.
	•	Inspiring other researchers, writers, and designers to structure positive narratives with the same rigor usually applied to risks.

The Hope Index is an MVP (minimum viable product) but its structure is infinitely extensible. The vision: a living database of optimism, continuously updated and consumable by both humans and AI systems.

## Wildfire Vertical (Worked Example)

To demonstrate the Hope Index schema in practice, this repository includes a **wildfire-specific dataset**:  
[`hope_index_wildfire_full.csv`](./hope_index_wildfire_full.csv)

This file captures a full “vertical” view of AI-driven wildfire detection, prevention, and response systems.  
It includes entries from government, corporate, academic, and community sources — each normalized to the Hope Index v0.2 schema.

### Why Wildfire?
Wildfire response is a prime case study: it spans satellites, indigenous knowledge, machine learning forecasts, insurance economics, and military/utility applications. By running a single domain through the Hope Index pipeline, we can demonstrate:

- **Source validation:** Government reports (U.S. Congress, NASA, DARPA), corporate programs (Google FireSat, Pano AI), NGOs (NAILSMA), and insurance/economic assessments.  
- **Lifecycle tracking:** Items move from *announced* → *pilot* → *deployed* → *scaled*.  
- **Negative space:** Some entries include uncertainty (`uncertainty_level`) or hype risk (`hype_risk`) to show limitations.  
- **Relationships:** Linked entries (e.g., Google FireSat R&D → Earth Fire Alliance validation).

### Example Entries
- **DARPA Testbed (HI-WF-0001):** $59.8M autonomy program for helicopters fighting wildfires in Texas (pilot, medium certainty).  
- **Google FireSat (HI-WF-0002):** Satellite constellation with 5x5m detection resolution (deployed, low hype risk).  
- **Healthy Country AI (HI-WF-0009):** Indigenous-led fire management initiative in Australia with CSIRO ($2.6M grant, pilot).  
- **U.S. Congress Report (HI-WF-0004):** Annual wildfire costs estimated at $394–893B (policy/economic anchor, verified).  

### Usage
This wildfire dataset acts as a **calibration domain** for the larger Hope Index. It demonstrates how diverse, messy information can be structured for both **human dashboards** and **AI-readable JSON/API outputs.**
