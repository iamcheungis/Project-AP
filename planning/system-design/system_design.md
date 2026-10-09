# System Design & Object Architecture

## Class Diagram

This diagram basically models the relationship between the "Recipe" class and the "MealPlan" class.

```mermaid
classDiagram
    class Recipe {
        +str name
        +float cost
        +int servings
        +dict ingredients
        +__init__(name: str, cost: float, servings: int)
        +add_ingredient(name: str, price: float) Void
        +get_cost_per_serving() float
        +get_summary() str
    }

    class MealPlan {
        +str plan_name
        +list recipes
        +float target_budget
        +__init__(plan_name: str, target_budget: float)
        +add_recipe(recipe: Recipe) Void
        +calculate_total_cost() float
        +is_within_budget() bool
        +generate_shopping_list() dict
    }

    MealPlan "1" o-- "*" Recipe : contains
