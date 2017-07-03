#encoding:UTF-8

from keras import backend as K

# 定义CTC损失函数
def custom_loss(y_true, y_pred):
    return y_pred

def ctc_lambda_func(args):
    y_pred, labels, input_length, label_length = args
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(labels, y_pred, input_length, label_length) 