# Python3.7.3
"""Multilayer perceptron problem example. 
A big thank you to https://builtin.com/data-science/deep-learning-python for the example."""

import numpy as np

print("Enter two values for input layers")

print('a = ')
a = int(input())

print('b = ')
b = int(input())

input_data = np.array([a, b])

weights = {
    'node_0': np.array([1, 1]),
    'node_1': np.array([-1, 1]),
    'output_node': np.array([2, -1])
}

node_0_value = (input_data * weights['node_0']).sum()
# a * 1 + b * 1 = 5
print('node 0_hidden: {}'.format(node_0_value))

node_1_value = (input_data * weights['node_1']).sum()
# a * -1 + b * 1 = 1
print('node_1_hidden: {}'.format(node_1_value))

hidden_layer_values = np.array([node_0_value, node_1_value])

output_layer = (hidden_layer_values * weights['output_node']).sum()

print("output layer : {}".format(output_layer))

