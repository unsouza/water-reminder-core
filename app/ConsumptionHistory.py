"""ConsumptionHistory Model"""

from masoniteorm.models import Model


class ConsumptionHistory(Model):
    """ConsumptionHistory Model"""

    __fillable__ = ["ml", "user_id"]
    pass
