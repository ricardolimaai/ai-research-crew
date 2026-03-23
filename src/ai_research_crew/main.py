#!/usr/bin/env python
import sys
import warnings
from ai_research_crew.crew import AiResearchCrew

warnings.filterwarnings('ignore')


def run():
    """Run the crew."""
    inputs = {
        'topic': 'AI agents in enterprise automation 2025'
    }
    AiResearchCrew().crew().kickoff(inputs=inputs)


def train():
    """Train the crew for a given number of iterations."""
    inputs = {
        'topic': 'AI agents in enterprise automation 2025'
    }
    try:
        AiResearchCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """Replay the crew execution from a specific task."""
    try:
        AiResearchCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """Test the crew execution and returns the results."""
    inputs = {
        'topic': 'AI agents in enterprise automation 2025'
    }
    try:
        AiResearchCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
