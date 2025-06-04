from core.user.use_cases.create_user import CreateUser
from core.user.use_cases.find_user import FindUser
from core.user.dto.user_dto import UserDTO


def store(data) -> str:
    use_case = CreateUser()

    payload = UserDTO(name=data.name, weight=data.weight)

    user = use_case.execute(payload=payload)
    return user.serialize()


def find(user_id: int):
    use_case = FindUser()

    return use_case.execute(user_id=user_id)
