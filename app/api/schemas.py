from pydantic import BaseModel


class PlannerRequest(BaseModel):
    members: list[str]
    ingredients: list[str]
    preference: str = "auto"