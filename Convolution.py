'''
@bbai
Email:243979648@qq.com
Github:https://github.com/FeiWard/TensorFlow_learning
'''
import numpy as np
import random
def convolution(x,filter_size,stride,padding):
    '''
    :param x: input data this could image or other data
    :param filter_size: your filter to use for convolution
    :param stride: how much step the filter moves
    :param padding: padding with the data
    :return: output the convolution result
    :param x_pad:after padding the data is x_pad
    :param x_map: which region to convolution
    '''
    x_pad = np.zeros((len(x) + 2 * padding, len(x[0]) + 2 * padding))
    filter_w, filter_h = filter_size
    filter = np.zeros((filter_h, filter_w))
    x_map=np.zeros((filter_h,filter_w))

    #Calculate the output shape
    out_h=int((len(x)+2*padding-filter_h)/stride)
    out_w=int((len(x[0])+2*padding-filter_w)/stride)
    out=np.zeros((out_h,out_w))

    #padding the image
    if padding!=0:
        for i in range(0,len(x)+2*padding-1):
            for j in range(0,len(x[0])+2*padding-1):
                if(i<padding or j<padding or i>len(x) or j>len(x[0])):
                    x_pad[i][j]=0
                else:
                    x_pad[i][j]=x[i-padding][j-padding]
    else:
        # x_pad=np.zeros((len(x),len(x[0])))
        for i in range(0, len(x)-1):
            for j in range(0, len(x[0])-1):
                x_pad[i][j] = x[i][j]

    #Get a random filter in range(1,2)
    for i in range(0,filter_h):
        for j in range(0,filter_w):
            filter[i][j]=random.randrange(1,2)
    #The course of convolution
    for i in range(0,len(x_pad)-filter_h):
        for j in range(0,len(x_pad[0])-filter_w):
            for m in range(0,filter_h):
                for n in range(0,filter_w):
                    x_map[m][n]=x_pad[i+m][j+n]
                    n+=1
                m+=1
            out[i][j]=sum(sum(np.multiply(filter,x_map)))
            j+=stride
        i+=stride
    return out

def pooling(input,filter_size,stride,padding,is_max_polling=True):
    '''

    :param input: input data could be image or other data
    :param filter_size: the pool filter size
    :param stride: the pooling stride
    :param padding: paddinf with the data
    :param is_max_polling: choose use max_pooling or mean_pooling default:max_pooling
    :return:the results of pooling of the data
    '''
    hang,lie=filter_size
    out=np.zeros((int(len(input)/hang),int(len(input[0])/lie)))
    input_pad=np.zeros((len(input)+2*padding,len(input[0])+2*padding))
    x_map=np.zeros((hang,lie))
    # padding the image
    if padding != 0:
        for i in range(0, len(input) + 2 * padding - 1):
            for j in range(0, len(input[0]) + 2 * padding - 1):
                if (i < padding or j < padding or i > len(input) or j > len(input[0])):
                    input_pad[i][j] = 0
                else:
                    input_pad[i][j] = input[i - padding][j - padding]
    else:
        # x_pad=np.zeros((len(x),len(x[0])))
        for i in range(0, len(input) - 1):
            for j in range(0, len(input[0]) - 1):
                input_pad[i][j] = input[i][j]

    if is_max_polling:
        for i in range(0, int(len(input)/hang)):
            for j in range(0, int(len(input_pad[0])/lie)):
                for m in range(0, hang):
                    for n in range(0, lie):
                        x_map[m][n] = input_pad[i + m][j + n]
                        n += 1
                    m += 1
                out[i][j] = np.amax(x_map)
                j+= stride
            i+= stride
    else:
        for i in range(0, len(input_pad) - hang):
            for j in range(0, len(input_pad[0]) - lie):
                for m in range(0, hang):
                    for n in range(0, lie):
                        x_map[m][n] = input_pad[i + m][j + n]
                        n += 1
                    m += 1
                out[i][j] = np.mean(x_map)
                j+= stride
            i+= stride
    return out

def batch_normalization(input,alpha,beta,gamma):
    mean=np.mean(input)
    var=np.var(input)
    input_norm=(input-mean)/(np.sqrt(var)+alpha)
    out=gamma*input_norm+beta
    return out

a_matrix=[[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8],[4,5,6,7,8,9]]
b_matrix=convolution(a_matrix,[2,2],1,1)
c_matrix=pooling(a_matrix,[2,2],2,0,is_max_polling=True)
d_matrix=batch_normalization(a_matrix,0.1,0.1,0.1)
print('**********************************')
print('convolution')
print(b_matrix)
print('**********************************')
print('pooling')
print(c_matrix)
print('**********************************')
print('Batch normalization')
print(d_matrix)
