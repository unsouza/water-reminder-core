from application import app
from fastapi import Header
import core.user.controller as ctrl
from core.user.dto.user_dto import UserDTO


@app.post("/users")
def store(data: UserDTO):
    return ctrl.store(data=data)


@app.get("/users/me")
def find(x_user_id: int = Header(...)):
    return ctrl.find(user_id=x_user_id)
