from crewai import Agent
from config import MODEL_NAME

# ---------------------
# Define Agents
# ---------------------
researcher = Agent(
    role="Researcher",
    goal="Research information based on user input",
    backstory="An AI researcher who gathers insights from trusted sources.",
    llm=f"gemini/{MODEL_NAME}",
    verbose=True,
)

summarizer = Agent(
    role="Summarizer",
    goal="Summarize researched content",
    backstory="An expert at summarizing information clearly and concisely.",
    llm=f"gemini/{MODEL_NAME}",
    verbose=True,
)

# ✅ Re-export pipeline function so accidental imports still work
try:
    from pipeline import run_ai_pipeline
except ImportError:
    run_ai_pipeline = None
