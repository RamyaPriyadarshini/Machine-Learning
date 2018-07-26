from sklearn import tree

height = [[160],[180],[164],[179],[175],[155],[153],[181]]
gender = ['f','m','f','m','m','f','f','m']

tr = tree.DecisionTreeClassifier()
tr = tr.fit(height,gender)

x = int(input("Enter your height :- "))

prediction = tr.predict(x)

if prediction == ['f']:
	print("Female")
else:
	print("Male")