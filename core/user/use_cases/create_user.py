from app.User import User
from core.user.dto.user_dto import UserDTO


class CreateUser:
    def execute(self, payload: UserDTO) -> User:
        user = User().create({
            "name": payload.name,
            "weight": payload.weight
        })

        return user.serialize()
