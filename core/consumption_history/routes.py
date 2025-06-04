from application import app
from fastapi import Header
import core.consumption_history.controller as ctrl
from core.consumption_history.dto.consumption_history_dto import ConsumptionHistoryDTO


@app.post("/histories")
def store(data: ConsumptionHistoryDTO, x_user_id: int = Header(...)):
    return ctrl.store(data=data, user_id=x_user_id)


@app.get("/histories/consumed")
def consumed(x_user_id: int = Header(...)):
    return ctrl.consumed(user_id=x_user_id)


@app.get("/histories/history")
def consumed(x_user_id: int = Header(...)):
    return ctrl.history(user_id=x_user_id)
