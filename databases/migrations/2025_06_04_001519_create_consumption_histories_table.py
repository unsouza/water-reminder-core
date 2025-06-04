"""CreateConsumptionHistoriesTable Migration."""

from masoniteorm.migrations import Migration


class CreateConsumptionHistoriesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("consumption_histories") as table:
            table.increments("id")
            table.integer("ml")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("consumption_histories")
