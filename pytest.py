import numpy as np

a_list = ['this', 'is', 'awesome!']


def print_a_list(a_list):
    for item in a_list:
        print(item)

print_a_list(a_list)

a_list.append('Teste')

print(a_list)

data = np.random.randn(100, 100)
print(data)
