from sklearn.naive_bayes import GaussianNB

clf = GaussianNB([[0.1 0.9]]) # (priors=None)

# Gaussian Naive Bayes (GaussianNB)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)

prediction = clf.predict([[100, 55, 37]])
proba = clf.predict_proba([[100, 55, 37]])

print(prediction)
print(proba)