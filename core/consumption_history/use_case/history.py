from app.ConsumptionHistory import ConsumptionHistory


class GetConsumptionHistory:
    def execute(self, user_id: int):
        history = (
            ConsumptionHistory.select_raw(
                "DATE(created_at) as date, SUM(ml) as total_ml"
            )
            .where("user_id", user_id)
            .group_by_raw("DATE(created_at)")
            .order_by("date", "desc")
            .get()
            .serialize()
        )

        return [
            {"date": record["date"], "total_ml": record["total_ml"]}
            for record in history
        ]
