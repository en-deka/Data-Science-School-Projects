#Assignment Information

print('Data 51100- Spring 2021\nAllison F*****\nProgramming Assignment #3\n')

import numpy as np

#read in features of training data and testing data;
#create arrays for values and names data sets
testing_name = np.loadtxt('nn-testing-data.csv', delimiter =',', usecols = (4), dtype = 'str')

testing_num = np.loadtxt('nn-testing-data.csv', delimiter = ',', usecols = (0,1,2,3))

training_name = np.loadtxt('nn-training-data.csv', delimiter =',', usecols = (4), dtype = 'str')

training_num = np.loadtxt('nn-training-data.csv', delimiter = ',', usecols = (0,1,2,3))

#determine index of NN for each data point in test data
nn_index = np.sqrt(((testing_num[:,np.newaxis] - training_num[np.newaxis,:])**2).sum(2)).argmin(1)

#create array for predicted training names
predicted = np.array((training_name[nn_index]))

#calculate accuracy of predicted classificattion
accuracy = np.sum(testing_name == predicted) / len(testing_name) * 100

#print formatted output
print('#, True, Predicted')

for x in range(len(predicted)):
    print('%d,%s,%s' % (x + 1, testing_name[x], predicted[x]))
    
print('Accuracy: %.2f%%' % (accuracy))