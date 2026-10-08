# Recipe & Grocery Budgeter

## Pathway
AP

## User
Budget conscious students and home cooks who want to organize weekly meals and track grocery spending efficiently and not waste both time and money.

## Problem
Manual meal planning often leads to wasted food, forgotten ingredients, and unexpected grocery expenses due to a lack of organization.

## Features
1. **Recipe Manager:** Store and organize recipes along with their required ingredients and estimated costs.
2. **Weekly Planner:** Build a custom meal plan by selecting saved recipes for the week.
3. **Automated Shopping List:** Generate a consolidated grocery list that combines ingredients and calculates total expected costs.

## Technical Question
How can I use object oriented programming and data structures to cross reference multiple recipes, eliminate duplicate ingredients, and calculate cumulative totals?

## Proof of Concept

This program bascially demonstrates user input handling, basic arithmetic calculation, and some conditional decision making to evaluate recipe costs against a target limit. It also proves that the project can accept dynamic pricing data, process expenditure, and also give budget feedback to the user. This logic basically will serve as the building block for future functions and data structures.

## Class Proof of Concept: Recipe

- **What the class represents:** The Recipe class basically models individual recipes, including properties such as recipe name, estimated total cost, and serving count.
- **Why it belongs in the project:** Representing recipes as distinct objects allows the application to store, modify, and also calculate pricing for more than 1 meal independently before putting them into a weekly meal plan.
- **What the test proves:** The driver script shows object creation, updating cost and scaling servings, and accurate calculation of data (cost per serving).
