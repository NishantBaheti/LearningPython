import time
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
#loading iris data


iris=load_iris()

#print flowers name

#dir(iris)

fl_names=iris.target_names

#print features of iris

fl_features= iris.feature_names

#loading flower features data

fl_feature_data=iris.data


print (fl_feature_data)

iris.target

setosa=iris.target[0:50]

train_setosa= setosa[0:49]

test_setosa= setosa[-1]

train_setosa.size

plt.xlabel("SETOSA")
plt.ylabel("VERSICOLOR")
plt.title("IRIS FLOWER")

x1=fl_feature_data[0:50]
y1=fl_feature_data[50:100]
z1=fl_feature_data[100:150]


plt.scatter(x1,y1,label="setosa",marker="o")
plt.scatter(x1,z1,label="versicolor",marker="^")
plt.scatter(y1,z1,label="verginica",marker="*")



plt.legend()
plt.show()

