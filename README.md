# AI Research Crew

A multi-agent research system built with **CrewAI** and **LangChain**. Three specialized AI agents collaborate to research any topic, analyze findings, and produce a professional report.

## How it works

```
User Input (topic)
       │
       ▼
┌─────────────────┐
│  Researcher     │  ← Searches the web, gathers facts and sources
│  (Agent 1)      │
└────────┬────────┘
         │ findings
         ▼
┌─────────────────┐
│  Analyst        │  ← Identifies trends, risks, opportunities
│  (Agent 2)      │
└────────┬────────┘
         │ analysis
         ▼
┌─────────────────┐
│  Writer         │  ← Produces structured Markdown report
│  (Agent 3)      │
└────────┬────────┘
         │
         ▼
   Final Report (saved to /reports)
```

Each agent has a specialized role, backstory, and toolset. They communicate through a sequential process where each agent builds on the previous one's output.

## Agents

| Agent | Role | Tools |
|-------|------|-------|
| Researcher | Senior Research Analyst | Web search (SerperDev) |
| Analyst | Data Analyst & Synthesizer | LLM reasoning |
| Writer | Technical Report Writer | LLM generation |

## Stack

| Layer | Technology |
|-------|-----------|
| Multi-Agent Framework | CrewAI |
| LLM Orchestration | LangChain |
| Language Model | OpenAI GPT-3.5-turbo |
| Search Tool | SerperDev API |

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Add your OPENAI_API_KEY and SERPER_API_KEY
```

### 3. Run a research

```bash
# Research a specific topic
python crew.py "LLM agents in enterprise automation 2025"

# Or edit crew.py and run directly
python crew.py
```

The final report is saved to the `reports/` directory in Markdown format.

## Example Output

Running `python crew.py "AI adoption in supply chain 2025"` produces a report with:

- Executive Summary
- Key Findings (with sources)
- Trend Analysis
- Risks and Opportunities
- Actionable Recommendations
- Conclusion

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `SERPER_API_KEY` | SerperDev API key for web search (free tier available at serper.dev) |
