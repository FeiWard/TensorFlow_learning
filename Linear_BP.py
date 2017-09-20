'''
@bbai
Email:243979648@qq.com
Github:https://github.com/FeiWard/TensorFlow_learning
'''
import numpy as np
import random

def xavier_random_function(shape,dtype=np.float32):
    w,h=shape
    weightes=np.zeros((w,h))
    low=-(np.sqrt(6/(w+h)))
    high=(np.sqrt(6/(w+h)))
    for i in range(0,w):
        for j in range(0,h):
            weightes[i][j]=random.uniform(low,high)
    return weightes

weights=xavier_random_function(shape=[4,1],dtype=np.float32)
shape=[1]
bias=np.zeros(shape)
# print(bias)
x_data=[[1,0.8,10,1],[2,0.7,9,2],[3,0.6,8,3],[4,0.8,7,3],[1,0.7,6,2],[2,0.6,5,1],
        [4,0.2,10,3],[1,0.1,9,2],[4,1,6,6],[2,0.2,4,3],[3,0.6,3,2],[4,0.9,2,1],
        [4,0.5,9,3],[3,0.4,4,5],[2,0.3,5,7],[2,0.5,6,8],[4,0.2,4,6],[1,0.6,5,4],[3,0.5,4,6],[4,0.3,9,8]]
y_data=[10,9,10,11,8,9,8,6,5,6,7,6,8,3,8,5,4,9,9,8]

y_predict=np.zeros((20))
loss=0
while(loss>0.001):
    for i in range(0,len(x_data)):
        # y_predict[0]=x_data[0]*weights+bias
        y_predict[i]=(np.dot(x_data[i],weights)+bias)
        loss=loss+y_data[i]-y_predict[i]
        loss=loss/len(x_data)
        print(loss/weights)
        weights=weights+loss/weights
        bias=bias+loss/bias

x_data_test=[[1,0.8,10,1]]
y_predict_test=np.dot(x_data_test,weights)+bias
print(y_predict_test)

