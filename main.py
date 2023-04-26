import time
import matplotlib.pyplot as plt
import numpy as np
import BBT_dac as dac
import BBT_dp as dp
import random

# generate a random binary tree


def generate_random_binary_tree(size):
    if size == 0:
        return None
    val = random.randint(0, 1000)
    root = Node(val)
    root.left = generate_random_binary_tree(size//2)
    root.right = generate_random_binary_tree(size//2)
    return root


class Node:
    # Crea nodo con el valor pasado por parametro
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_by_dac(root):
    # Verfica si el árbol esta balanceado
    if dac.is_balanced(root):
        return "The binary tree is balanced."
    else:
        return "The binary tree is not balanced."


def check_by_dp(root):
    # Verificacion para programacion dinamica
    if dp.is_balanced(root):
        return "The binary tree is balanced."
    else:
        return "The binary tree is not balanced."


def measure_time(func, *args):
    start = time.time()
    for i in range(100):
        func(*args)
    end = time.time()
    return (end - start) / 100


sizes = [10, 100, 1000, 10000, 20000]
dac_times = []
dp_times = []

for size in sizes:
    root = generate_random_binary_tree(size)
    dac_time = measure_time(check_by_dac, root)
    dp_time = measure_time(check_by_dp, root)
    dac_times.append(dac_time)
    dp_times.append(dp_time)

plt.plot(sizes, dac_times, label='Divide and Conquer')
plt.plot(sizes, dp_times, label='Dynamic Programming')
plt.xscale('log')
plt.yscale('logit')
plt.ylim(10**-6, 1)
plt.xlabel('Input Size (log scale)')
plt.ylabel('Execution time (s) (logit scale)')
plt.title('DaC vs DP')
plt.legend()
plt.show()
