#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
 
  """
  use nested for loops to compare the recipe and ingredient keys
  add total variable to count how many batchs can be made
  """ 
  batches = 0
  for key, value in recipe.items():
      print(key, value)
  for key, value in ingredients.items():
      print(key, value)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))