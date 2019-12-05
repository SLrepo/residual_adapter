# read numpy file 
import numpy as np
import matplotlib.pyplot as plt
data = np.load('res/ho_pretrain.npy')
num_epoch = 20
epoch = range(0, num_epoch)
data_train_loss = data[0, 0:num_epoch, 0]
data_test_loss = data[2, 0:num_epoch, 0]
plt.plot(epoch, data_train_loss, 'r--', epoch, data_test_loss, 'bs')
plt.xlabel('Epoch')
plt.ylabel('Loss Function')
plt.gca().legend(('Training', 'Testing'))
plt.show()
data_train_acc = data[1, 0:num_epoch, 0]
data_test_acc = data[3, 0:num_epoch, 0]
plt.plot(epoch, data_train_acc, 'r--', epoch, data_test_acc, 'bs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.gca().legend(('Training', 'Testing'))
plt.show()
# print(data[0])