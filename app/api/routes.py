from fastapi import APIRouter

from app.api.schemas import PlannerRequest
from app.services.planner import MealPlanner, PlannerSession

router = APIRouter()

planner = MealPlanner()


@router.post("/recommend")
def recommend(req: PlannerRequest):

    session = PlannerSession()

    planner.update(session, req.members)
    planner.update(session, req.ingredients)
    planner.update(session, req.preference)

    return {
        "result": planner.next(session)
    }