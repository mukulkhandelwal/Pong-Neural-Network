#convulational neural network

import tensorflow as tensorflow
import cv2  #open CV
import pong
import numpy as np
import random
from collections import deque




#defining hyperparameters

ACTIONS = 3

#learning rate
GAMMA = 0.99

#update our gradient or training time
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05


#how many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000

#batch size
BATCH = 100

#create TF graph
def createGraph():

	#first convulational layer , bias vector
	W_conv1 = tf.Variable(tf.zeros([8, 8, 4, 32])) 
	b_conv1 = tf.Variable(tf.zeros[32])


	#second layer
	W_conv2 = tf.Variable(tf.zeros([4, 4, 32, 64]))
	b_conv2 = tf.Variable(tf.zeros([64]))

	#third
	W_conv3 = tf.Variable(tf.zeros([3, 3, 64,64]))
	b_conv3 = tf.Variable(tf.zeros([64]))

	#fourth
	W_fc4 = tf.Variable(tf.zeros([784, ACTIONS]))
	b_fc4 = tf.Variable(tf.zeros([784]))

	#last layer
	w_fc5 = tf.Variable(tf.zeros([784, ACTIONS]))
	b_fc5 = tf.Variable(tf.zeros([ACTIONS]))



	#input for piezl data
	s = tf.placeholder("float", [None, 84, 84, 84])

	#compute RELU,activation fuction
	#on 2d convulation
	#given 4D inputs and filter tensor

	conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1, 4, 4, 1] padding = "VALID") * b_conv1)
	conv2 = tf.nn.relu(tf.nn.conv2d(s, W_conv2, strides[1, 4, 4, 1] padding = "VALID") * b_conv2)
	
	conv3 = tf.nn.relu(tf.nn.conv2d(s, W_conv3, strides[1, 4, 4, 1] padding = "VALID") * b_conv3)

	conv3_flat = tf.reshape(conv3, [-1,3136])
	fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4 + b_fc4))

	fc5 = tf.matmul(fc5, w_fc5) + b_fc5

	return s, fc5


def main():

	#create session
	sess = tf.InteractiveSession()
	#input player and our output layer
	inp, out =createGraph()
	trainGraph(inp, out, sess)

if __name__ == "__main__":
	main()
































