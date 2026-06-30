from enum import Enum
from pathlib import Path

from app.services.llm import LLM
from app.services.retriever import Retriever


class PlannerState(str, Enum):
    MEMBERS = "members"
    INGREDIENTS = "ingredients"
    PREFERENCE = "preference"
    RECOMMEND = "recommend"


class PlannerSession:

    def __init__(self):
        self.members = []
        self.ingredients = []
        self.preference = "auto"
        self.state = PlannerState.MEMBERS


class MealPlanner:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM()

        self.prompt = Path(
            "app/prompts/meal_planner.txt"
        ).read_text()

    def next(self, session):

        if session.state == PlannerState.MEMBERS:
            return {
                "type": "members",
                "question": "누가 식사하시나요?"
            }

        if session.state == PlannerState.INGREDIENTS:
            return {
                "type": "ingredients",
                "question": "집에 있는 재료는 무엇인가요?"
            }

        if session.state == PlannerState.PREFERENCE:
            return {
                "type": "preference",
                "question": "어떤 요리를 원하시나요? (자동도 가능합니다)"
            }

        return self.recommend(session)

    def update(self, session, answer):

        if session.state == PlannerState.MEMBERS:
            session.members = answer
            session.state = PlannerState.INGREDIENTS

        elif session.state == PlannerState.INGREDIENTS:
            session.ingredients = answer
            session.state = PlannerState.PREFERENCE

        elif session.state == PlannerState.PREFERENCE:
            session.preference = answer
            session.state = PlannerState.RECOMMEND

    def recommend(self, session):

        query = f"""
        가족: {', '.join(session.members)}
        재료: {', '.join(session.ingredients)}
        선호: {session.preference}
        """

        recipes = self.retriever.search(query)

        prompt = self.prompt.format(
            profile=query,
            recipes="\n".join(recipes),
        )

        return self.llm.generate(prompt)