from crewai import Task, Crew
from agents import researcher, summarizer

def run_ai_pipeline(user_prompt: str):
    """Run CrewAI pipeline with a custom user topic."""

    task1 = Task(
        description=f"Research about: {user_prompt}. Provide 3 key bullet points.",
        agent=researcher,
        expected_output="A list of 3 bullet points with insights about the topic.",
    )

    task2 = Task(
        description=f"Summarize the research on {user_prompt} into a short paragraph.",
        agent=summarizer,
        expected_output="A concise 4-5 sentence paragraph summarizing the findings.",
    )

    crew = Crew(
        agents=[researcher, summarizer],
        tasks=[task1, task2],
        verbose=True,
    )

    return crew.kickoff()
