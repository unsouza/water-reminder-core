from core.consumption_history.use_case.register_consumption_history import (
    RegisterConsumptionHistory,
)
from core.consumption_history.use_case.get_daily_consumed import GetDailyConsumed
from core.consumption_history.use_case.history import GetConsumptionHistory
from core.consumption_history.dto.consumption_history_dto import ConsumptionHistoryDTO


def store(data, user_id) -> str:
    use_case = RegisterConsumptionHistory()

    payload = ConsumptionHistoryDTO(ml=data.ml)

    water = use_case.execute(payload=payload, user_id=user_id)
    return water.serialize()


def consumed(user_id):
    use_case = GetDailyConsumed()
    return use_case.execute(user_id=user_id)


def history(user_id):
    use_case = GetConsumptionHistory()
    return use_case.execute(user_id=user_id)
