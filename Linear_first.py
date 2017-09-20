'''
@bbai
Email:243979648@qq.com
Github:https://github.com/FeiWard/TensorFlow_learning
'''
#%%
'''
A simple linera function 
x:input data
y:label
w:weightes
'''
import random
w=0.5
x=[i for i in range(1,100)]
y=[2*i+random.randint(1,10)/10 for i in range(1,100)]

for i in range(1,1000):
    ind=random.randint(0,98)
    y_=w*x[ind]
    loss=y[ind]-y_
    w=w+loss/x[ind]

x_test=4
y_test=w*x_test
print(y_test)
