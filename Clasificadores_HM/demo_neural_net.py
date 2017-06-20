from sklearn.neural_network import MLPClassifier

# Multi-layer Perceptron classifier.
# This model optimizes the log-loss function using LBFGS or stochastic gradient descent.

clf = MLPClassifier(alpha=1)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)

prediction = clf.predict([[168, 70, 40]])
proba = clf.predict_proba([[168, 70, 40]])

print(prediction)
print(proba)