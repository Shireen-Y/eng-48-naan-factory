from naan_factory_functions import *
# Tests go here (for separation of concerns)


# Make test for make_dough
print("testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# When I pass in cement and water, or anything else.. I should ge: 'Not dough'
print("testing make_dough with 'water' and 'cement'. Expected --> 'Not dough'")
print(make_dough('water', 'cement') == 'Not dough')
print('got:', make_dough('water', 'cement'))

print("testing make_dough with 'egg' and 'flour'. Expected --> 'Not dough'")
print(make_dough('egg', 'flour') == 'Not dough')
print('got:', make_dough('egg', 'flour'))


# Make test for bake_dough
# Then with the dough, we should be able to put it in the oven and get out a naan :)
print("testing bake_dough with 'dough'. Expected --> 'naan'")
print(bake_dough('dough') == 'naan')
print("When calling bake_dough('dough'), got:", bake_dough('dough'))

# When bake_dough is passed something than 'dough', it should output: 'Not naan'
print("testing bake_dough with 'chicken'. Expected --> 'Not naan'")
print(bake_dough('chicken') == 'Not naan')
print("When calling bake_dough('chicken'), got:", bake_dough('chicken'))

print("testing bake_dough with 'bricks'. Expected --> 'Not naan'")
print(bake_dough('bricks') == 'Not naan')
print("When calling bake_dough('bricks'), got:", bake_dough('bricks'))