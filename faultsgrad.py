import tensorflow as tf
import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize) #For expanding the output display in terminal/console

a=np.ndarray([])
b=np.ndarray([])

x_ = tf.placeholder(tf.float32, shape=[20384,21], name = 'x-input')
y_ = tf.placeholder(tf.float32, shape=[20384,4], name = 'y-input')
x_test = tf.placeholder(tf.float32, shape=[4619,21], name = 'xtest-input')
y_test = tf.placeholder(tf.float32, shape=[4619,1], name = 'xtest-output')

#Theta1,Theta2,Theta3 are the weights for different layers
Theta1 = tf.Variable(tf.random_uniform([21,15], -1, 1), name = "Theta1")
Theta2 = tf.Variable(tf.random_uniform([15,15], -1, 1), name = "Theta2")
Theta3 = tf.Variable(tf.random_uniform([15,4], -1, 1), name = "Theta3")

Bias1 = tf.Variable(tf.zeros([15]), name = "Bias1") #Bias for input layer
Bias2 = tf.Variable(tf.zeros([15]), name = "Bias2") #Bias for hidden layer 1
Bias3 = tf.Variable(tf.zeros([4]), name = "Bias3")  #Bias for hidden layer 2

A2 = tf.sigmoid(tf.matmul(x_, Theta1) + Bias1) #Layer 2(Hidden layer 1)
A3 = tf.sigmoid(tf.matmul(A2, Theta2) + Bias2) #Layer 3(Hidden layer 2)
A4 = tf.sigmoid(tf.matmul(A3, Theta3) + Bias3) #Layer 4(Output layer)

cost = tf.reduce_mean(( (y_ * tf.log(A4)) + 
		((1 - y_) * tf.log(1.0 - A4)) ) * -1) #Cost function used

optimizer = tf.train.GradientDescentOptimizer(0.06).minimize(cost)

input_X = pd.read_excel(r'C:\Users\nikhi\OneDrive\Documents\data_normalizedfinal.xlsx',sheet_name='train_hs_norm') #Importing training data input 
input_Y = pd.read_excel(r'C:\Users\nikhi\OneDrive\Documents\data_normalizedfinal.xlsx',sheet_name='trainoutfinal') #Importing training data output
test_input = pd.read_excel(r'C:\Users\nikhi\OneDrive\Documents\data_normalizedfinal.xlsx',sheet_name='test_hs_norm') #Importing testing data input 
test_out = pd.read_excel(r'C:\Users\nikhi\OneDrive\Documents\data_normalizedfinal.xlsx',sheet_name='testoutfinal').to_numpy().flatten() #Importing testing data output for calc accuracy 
print(test_out.shape)

init = tf.global_variables_initializer()
sess = tf.Session()

writer = tf.summary.FileWriter("./logs/xor_logs", sess.graph)
i=0

sess.run(init)

for i in range(10000):
	sess.run(optimizer, feed_dict={x_: input_X, y_: input_Y})
	if i % 1000 == 0:
		print('Epoch ', i)
		print('cost ', sess.run(cost, feed_dict={x_: input_X, y_: input_Y}))

#~~~~~~~~~~~Testing~~~~~~~~~~~#
test_A2 = tf.sigmoid(tf.matmul(x_test, Theta1) + Bias1)
test_A3 = tf.sigmoid(tf.matmul(test_A2, Theta2) + Bias2)
test_A4 = tf.sigmoid(tf.matmul(test_A3, Theta3) + Bias3)
#print('res',np.argmax(sess.run(test_A4, feed_dict={x_test: test_input}),axis=1))
#~~~~Calculating accuracy~~~~#
diff=np.subtract((np.argmax(sess.run(test_A4, feed_dict={x_test: test_input}),axis=1)),test_out)
print(diff)
#print(test_out)
nonz=np.count_nonzero(diff)
acc=100-nonz*100/(diff.size)
print(acc)
#~~~~~Loading the test output data in excel~~~~~~#
#ex=pd.DataFrame(np.argmax(sess.run(test_A4, feed_dict={x_test: test_input}),axis=1))
#ex.to_excel('comp.xlsx',index=False)

