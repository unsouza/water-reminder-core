from app.User import User


class FindUser:
    def execute(self, user_id: int) -> User:
        print(user_id)
        user = User.find(user_id).serialize()
        print(user)

        if not user:
            raise Exception(f"Usuário com ID {user_id} não encontrado.")

        return user
