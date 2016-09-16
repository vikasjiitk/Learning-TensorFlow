import tensorflow as tf 

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', 'data/', 'Directory for storing data')

mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

#hyperparameters
learning_rate = 0.001 
training_iterations = 200000 
batch_size = 200
display_step = 10

#network parameters
input_size = 784
no_classes = 10
dropout = 0.5
