class Recipe:
    def __init__(self, name: str, cost: float, servings: int = 1):
        """Initializes a recipe with a name, estimated cost, serving size"""
        self.name = name
        self.cost = cost
        self.servings = servings

    def get_cost_per_serving(self) -> float:
        """This gives the calculated cost per serving"""
        if self.servings <= 0:
            return 0.0
        return self.cost / self.servings

    def get_summary(self) -> str:
        """This gives a formatted summary string of the recipe details"""
        return (f"Recipe: {self.name} | Total Cost: ${self.cost:.2f} | "
                f"Servings: {self.servings} | Cost/Serving: ${self.get_cost_per_serving():.2f}")

    def update_cost(self, new_cost: float) -> None:
        """This updates the total cost of the recipe"""
        if new_cost >= 0:
            self.cost = new_cost

    def scale_servings(self, new_servings: int) -> None:
        """Changes the serving count and updates object state"""
        if new_servings > 0:
            self.servings = new_servings
