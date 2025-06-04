from app.User import User
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


class FindUser:
    def execute(self, user_id: int) -> User:
        print(user_id)
        user = User.find(user_id)

        if not user:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=f"Usuário com ID {user_id} não encontrado."
            )

        return user.serialize()
