import BBT_dac as dac
import BBT_dp as dp
import time
import matplotlib.pyplot as plt

# Create a sample binary tree
#     1
#    / \
#   2   3
#  / \
# 4   5
root = dac.TreeNode(1)
root.left = dac.TreeNode(2)
root.right = dac.TreeNode(3)
root.left.left = dac.TreeNode(4)
root.left.right = dac.TreeNode(5)


def check_by_dac(root):
    # Verfica si el árbol esta balanceado
    if dac.is_balanced(root):
        print("The binary tree is balanced.")
    else:
        print("The binary tree is not balanced.")


def check_by_dp(root):
    # Verificacion para programacion dinamica
    if dp.is_balanced(root):
        print("The binary tree is balanced.")
    else:
        print("The binary tree is not balanced.")


def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


times = 50
dac_times = []
dp_times = []

for size in range(times):
    dac_time = measure_time(check_by_dac, root)
    dp_time = measure_time(check_by_dp, root)
    dac_times.append(dac_time)
    dp_times.append(dp_time)

plt.plot(range(times), dac_times, label='Divide and Conquer')
plt.plot(range(times), dp_times, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Execution time (s)')
plt.title('DaC vs DP')
plt.legend()
plt.show()
