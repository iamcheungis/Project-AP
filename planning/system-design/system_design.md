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

flowchart TD
    A[Start: Call generate_shopping_list] --> B[Initialize empty dict: shopping_list]
    B --> C[Initialize total_plan_cost = 0.0]
    C --> D[Loop through each Recipe in recipes list]
    
    D --> E{More Recipes?}
    E -- Yes --> F[Select next Recipe]
    F --> G[Add Recipe.cost to total_plan_cost]
    G --> H[Loop through Recipe.ingredients]
    
    H --> I{More Ingredients?}
    I -- Yes --> J[Get ingredient name and price]
    J --> K{Is ingredient in shopping_list?}
    
    K -- Yes --> L[Add price to existing ingredient total]
    K -- No --> M[Insert new ingredient into shopping_list]
    
    L --> H
    M --> H
    
    I -- No --> D
    
    E -- No --> N{Is total_plan_cost <= target_budget?}
    N -- Yes --> O[Flag: Within Budget]
    N -- No --> P[Flag: Over Budget]
    
    O --> Q[Return summary dictionary]
    P --> Q
    Q --> R[End]
