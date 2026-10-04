# from pgmpy.models import DiscreteBayesianNetwork

# model = DiscreteBayesianNetwork([
#     ('Burglary', 'Alarm'),
#     ('Earthquake', 'Alarm'),
#     ('Alarm', 'JohnCalls'),
#     ('Alarm', 'MaryCalls')
# ])

# print("Nodes in the Bayesian Network:")
# print(model.nodes())

# print("\nEdges in the Bayesian Network:")
# print(model.edges())
























from pgmpy.models import DiscreteBayesianNetwork


data = DiscreteBayesianNetwork([
    
    ('prince','one'),
    ('anuj','two'),
    ('sumit','one'),
    ('rehan','one'),
])

print("node data of my data")
print(data.nodes())

print("edge of data")
print(data.edges())