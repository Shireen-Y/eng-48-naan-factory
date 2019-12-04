

def hello():
    return 'hello'


print(hello())

# Basis of a test
# You'll be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # And testing for these

# Make test for make_dough
# To make dough it will take in 'water' and flour to make the dough
print(make_dough('water', 'flour') == 'dough')




# Make test for bake_dough
# Then with the dough, we should be able to put it in the oven and get out a naan :)
print(bake_dough('dough') == 'naan')

