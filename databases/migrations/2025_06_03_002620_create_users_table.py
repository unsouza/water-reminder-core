"""CreateUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")
            table.string("name")
            table.decimal("weight")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
