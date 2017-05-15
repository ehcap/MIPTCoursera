import numpy as np
from sklearn import  metrics, tree, datasets

def write_answer(filename, result):
    with open(filename, "w") as fout:
        fout.write(str(result))

def L_vector(y, predict):
    return -( predict - y)


def gbm_predict(X):
    return [sum([coeff * algo.predict([x])[0] for algo, coeff in
                 zip(base_algorithms_list, coefficients_list)]) for x in X]

boston = datasets.load_boston()
X=boston.data
y=boston.target
n = len(boston.data)
#split dataset to train and test (75/25)
X_train = np.array(X[:int(0.75*n)])
X_test = np.array(X[int(0.75*n):])
y_train = np.array(y[:int(0.75*n)])
y_test = np.array(y[int(0.75*n):])

base_algorithms_list = []
coefficients_list = []
tt = tree.DecisionTreeRegressor(max_depth=5, random_state=42)
ystart = np.zeros(len(y_train))
tt.fit(X_train, y_train)
base_algorithms_list.append(tt)

for i in range(1, 51):
    tt = tree.DecisionTreeRegressor(max_depth=5, random_state=42)
    tt.fit(X_train, L_vector(y_train, gbm_predict(X_train)))
    print "Step %i, MSE - %f" % (i, metrics.mean_squared_error(y_train, gbm_predict(X_train)))
    base_algorithms_list.append(tt)
    #coefficients_list.append(0.9 / (1.0 + i))
    coefficients_list.append(0.9)

import math

mean = metrics.mean_squared_error(y_test, gbm_predict(X_test))

mean = mean **0.5
print "RMSE for test - %f" % (mean)

write_answer("answ3.txt",mean)

