from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

print(np.linalg.inv(X))

print(X @ np.linalg.inv(X))

Y = np.array([[0, 1],
              [1, -1],
              [-2, 1]])

print(np.linalg.pinv(Y))

print(np.linalg.pinv(Y) @ Y)

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([4, 8, 9])
x_test = [[1, 2]]
# Scikit Learn을 활용한 회귀분석
model = LinearRegression()
model.fit(X, y)
y_test = model.predict(x_test)
y_test2 = model.predict([[3, 4]])
y_test3 = model.predict([[5, 6]])
print(y_test)
print(y_test2)
print(y_test3)

# Moore-Penrose 역행렬

X_ = np.array([np.append(x, [1]) for x in X])
beta = np.linalg.pinv(X_) @ y
y_test = np.append(x_test, [1]) @ beta
y_test2 = np.append([3, 4], [1]) @ beta
y_test3 = np.append([5, 6], [1]) @ beta
print(y_test)
print(y_test2)
print(y_test3)
