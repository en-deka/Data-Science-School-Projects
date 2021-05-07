#Assignment Information
print("Data 51100- Spring 2021\nAllison Fischer\nProgramming Assignment #3\n")
import numpy as np
#read in features of training data
xtrain_arr = np.loadtxt(r"nn-training-data.csv",
                        delimiter = ",",usecols = (0,1,2,3))
#read in classification of training data
ytrain_arr = np.loadtxt(r"nn-training-data.csv",
                        delimiter = ",",usecols = (4), dtype = "str")
#read in features of test data
xtest_arr = np.loadtxt(r"nn-testing-data.csv",
                        delimiter = ",",usecols = (0,1,2,3))
#read in classification of test data
ytest_arr = np.loadtxt(r"nn-testing-data.csv",
                       delimiter = ",",usecols = (4), dtype = "str")
#determine index of NN for each data point in test set
nn_index = np.sqrt(((xtest_arr[:,np.newaxis] - xtrain_arr[np.newaxis,:])**2).sum(2)).argmin(1)

# Creating arrays for values and names of the testing data set
testing_name = np.loadtxt("nn-testing-data.csv", delimiter =',', usecols = (4), dtype = 'str')

testing_num = np.loadtxt("nn-testing-data.csv", delimiter = ',', usecols = (0,1,2,3))

training_name = np.loadtxt("nn-training-data.csv", delimiter =',', usecols = (4), dtype = 'str')

training_num = np.loadtxt("nn-training-data.csv", delimiter = ',', usecols = (0,1,2,3))

# Creating array containing the predicted training names for each test example
predicted = np.array((training_name[nn_index]))

# calculating the accuracy of the predicted classification

accuracy = np.sum(testing_name == predicted) / len(testing_name) * 100

print('#, True, Predicted')

for x in range(len(predicted)):
    print("%d,%s,%s" % (x + 1, testing_name[x], predicted[x]))

print('Accuracy: %.2f%%' % (accuracy))