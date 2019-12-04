# Basis of a test
# You'll be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # And testing for these


def make_dough(arg1, arg2):
    if arg1 != 'water' and arg2 != 'water':
        return 'Not dough'
    elif arg1 != 'flour' and arg2 != 'flour':
        return 'Not dough'
    elif 'water' in [arg1, arg2] and 'flour' in [arg1, arg2]:
        return 'dough'

def bake_dough(arg1):
    if arg1 != 'dough':
        return 'Not naan'
    elif arg1 == 'dough':
        return 'naan'

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