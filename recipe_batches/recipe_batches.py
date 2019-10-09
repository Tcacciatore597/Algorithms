#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #find what ingredients are needed for the recipe
  batches = 0
  # for a in recipe:
  #   for b in ingredients:
  #     if a == b:
  #       while ingredients[b]/recipe[a] >= 1:
  #         ingredients[b] - recipe[a]
  #         batches += 1
  #       else:
  #         print("no more batches can be made")
  # return batches
  # enough = True
  # while enough:
  #   for a in recipe.keys():
  #     if a in ingredients:
  #       #compare ingredient value to recipe value
  #       x = ingredients[a]/recipe[a]
  #       if x >=1:
  #         ingredients[a] - recipe[a]
  #       else:
  #         enough = False
  #   if enough == True:
  #     batches += 1
  # #how much of each ingredient for the recipe
  # #how many whole batches can we make with the given ingredients?
  # return batches
  rec = recipe.keys()
  ing = ingredients.keys()
  common = set(rec).intersection(set(ing))
  for key in common:
    if ingredients[key] > recipe[key]:
      div = ingredients[key]/recipe[key]
      #find lowest div out of all the keys being compared.
      #batches = lowest div rounded down.
  

  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 51, 'flour': 11}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))