import nimpy as np
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.minist import load_minist

(x_train,t_train),(x_test,t_test) = \
load_mnist(flatten=True,normalize=False)

train_size = x_train.shape[0]
batch_size=10
batch_mask=np.random.choice(train_size,batch_size)　　#訓練データからランダムに抽出
x_batch=x_train[batch_mask]
t_batch=t_train[batch_mask]

np.random.choice(60000,10)


