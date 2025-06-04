from datetime import datetime, time
from masoniteorm.query import QueryBuilder

from app.ConsumptionHistory import ConsumptionHistory


class GetDailyConsumed:
    def execute(self, user_id: int):
        now = datetime.now()
        start = datetime.combine(now.date(), time.min)
        end = datetime.combine(now.date(), time.max)

        total = (
            ConsumptionHistory()
            .where("user_id", user_id)
            .where("created_at", ">=", start)
            .where("created_at", "<=", end)
            .sum("ml")
            .first()
            .serialize()
        )

        return {"total_consumed": total.get('ml')}
