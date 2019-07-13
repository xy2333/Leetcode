import numpy as np
import tensorflow as tf

W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
linear_model = W * x + b


loss = tf.reduce_sum(tf.square(linear_model-y))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

curr_W, curr_b, curr_loss = sess.run([W,b,loss],{x:[1,2,3,4],y:[0,-1,-2,-3]})
print('curr_W: %s curr_b: %s curr_loss: %s' % (curr_W,curr_b,curr_loss))