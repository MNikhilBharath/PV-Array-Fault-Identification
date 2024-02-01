import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import pandas as pd
import numpy as np
import clr
import sys

np.set_printoptions(threshold=sys.maxsize);
x_ = tf.placeholder(tf.float32, shape=[13832,21], name = 'x-input')
y_ = tf.placeholder(tf.float32, shape=[13832,3], name = 'y-input')
x_test = tf.placeholder(tf.float32, shape=[2945,21], name = 'xtest-input')
y_test = tf.placeholder(tf.float32, shape=[2945,1], name = 'xtest-output')

Theta1 = tf.Variable(tf.random_uniform([21,15], -1, 1), name = "Theta1")
Theta2 = tf.Variable(tf.random_uniform([15,15], -1, 1), name = "Theta2")
Theta3 = tf.Variable(tf.random_uniform([15,3], -1, 1), name = "Theta3")

Bias1 = tf.Variable(tf.zeros([15]), name = "Bias1")
Bias2 = tf.Variable(tf.zeros([15]), name = "Bias2")
Bias3 = tf.Variable(tf.zeros([3]), name = "Bias3")

A2 = tf.sigmoid(tf.matmul(x_, Theta1) + Bias1)
A3 = tf.sigmoid(tf.matmul(A2, Theta2) + Bias2)
A4 = tf.sigmoid(tf.matmul(A3, Theta3) + Bias3)

cost = tf.reduce_mean(( (y_ * tf.log(A4)) +
		((1 - y_) * tf.log(1.0 - A4)) ) * -1)

gs=tf.train.create_global_step()
optimizer = tf.train.AdamOptimizer(learning_rate=clr.cyclic_learning_rate(global_step=gs, mode='triangular2')).minimize(cost)

input_X = pd.read_excel(r'C:\Users\dwije\Downloads\data_normalized.xlsx',sheet_name='upinput_norm')
input_Y = pd.read_excel(r'C:\Users\dwije\Downloads\data_normalized.xlsx',sheet_name='upout')#Loading the output of size mx1
test_input = pd.read_excel(r'C:\Users\dwije\Downloads\data_normalized.xlsx',sheet_name='test_norm')
test_out = pd.read_excel(r'C:\Users\dwije\Downloads\data_normalized.xlsx',sheet_name='testout2').to_numpy().flatten()
print(test_out.shape)

init = tf.global_variables_initializer()
sess = tf.Session()

writer = tf.summary.FileWriter("./logs/xor_logs", sess.graph)

sess.run(init)

for i in range(2000):
	sess.run(optimizer, feed_dict={x_: input_X, y_: input_Y})
	if i % 1000 == 0:
		print('Epoch ', i)
		print('cost ', sess.run(cost, feed_dict={x_: input_X, y_: input_Y}))

test_A2 = tf.sigmoid(tf.matmul(x_test, Theta1) + Bias1)
test_A3 = tf.sigmoid(tf.matmul(test_A2, Theta2) + Bias2)
test_A4 = tf.sigmoid(tf.matmul(test_A3, Theta3) + Bias3)
diff=np.subtract((np.argmax(sess.run(test_A4, feed_dict={x_test: test_input}),axis=1)),test_out)
print(diff)
nonz=np.count_nonzero(diff)
acc=100-nonz*100/(diff.size)
print(acc)
