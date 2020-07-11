#encoding=utf-8
import numpy as np

def check_shape_and_type(y_true, y_pred):
    y_true_shape = np.shape(y_true)
    y_pred_shape = np.shape(y_pred)

    if y_true_shape != y_pred_shape:
        raise ValueError('y_true shape is not equal to y_pred')
    return y_true_shape

def accuracy(y_true, y_pred):
    #检查y_true和y_pred的形状和类型是否一致
    shape = check_shape_and_type(y_true, y_pred)
    #数量为0
    if shape[0] == 0:
         return 0
    true_cnt = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            true_cnt += 1
    return true_cnt * 1.0 / shape[0]

if __name__ == '__main__':
    y_true = [0, 0, 0, 1]
    y_pred = [0, 1, 1, 0]

    acc = accuracy(y_true, y_pred)
    print(acc)

