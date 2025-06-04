from app.ConsumptionHistory import ConsumptionHistory
from core.consumption_history.dto.consumption_history_dto import ConsumptionHistoryDTO


class RegisterConsumptionHistory:
    def execute(self, payload: ConsumptionHistoryDTO, user_id: int) -> ConsumptionHistory:
        consumption_history = ConsumptionHistory().create({
            "ml": payload.ml,
            "user_id": user_id
        })

        return consumption_history
