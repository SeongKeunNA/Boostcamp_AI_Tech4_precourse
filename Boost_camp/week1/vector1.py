import numpy as np


def l1_norm(x):
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm


def l2_norm(x):
    x_norm = x * x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm


v1 = np.array([1, 3])
v2 = np.array([[1, 2], [3, 4]])


print(l1_norm(v1), l2_norm(v1))
print(l1_norm(v2), l2_norm(v2))


v3 = np.array([[3, 4], [-1, -2]])
v4 = np.array([3, -1])


def angle(x, y):
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y))
    print('cos(theta)):', v)
    theta = np.arccos(v)
    return theta


print(angle(v2, v3))
print(angle(v3, v4))

x = np.array([0, 1])
y = np.array([0, 2])
print(angle(x, y))

x = np.array([1, -1, 1, -1])
y = np.array([4, -4, 4, -4])
print(angle(x, y))

