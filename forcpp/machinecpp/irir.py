# load irir target 

from sklearn.datasets import load_iris

label = load_iris()['target']

with open("label.txt", 'w') as f:
	for ele in label:
		key = str(ele) + '\n'
		f.write(str(key))
