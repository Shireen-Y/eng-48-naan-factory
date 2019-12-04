# Basis of a test
# You'll be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # And testing for these

# Make test for make_dough
print("testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
def make_dough(arg1, arg2):
    pass

def bake_dough(arg1):
    pass

print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# Make test for bake_dough
# Then with the dough, we should be able to put it in the oven and get out a naan :)
print("testing bake_dough with 'dough'. Expected --> 'naan'")
print(bake_dough('dough') == 'naan')
print('got:', bake_dough('dough'))

