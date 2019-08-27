from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

import torch
import torch.nn.functional as F
import torch.optim as optim

import numpy as np


class MyLineModel(torch.nn.Module):
    def __init__(self):
        super(MyLineModel, self).__init__()
        self.linear1 = torch.nn.Linear(32, 16)
        # self.linear2 = torch.nn.Linear(48, 24)
        self.linear3 = torch.nn.Linear(16, 1)

    def forward(self, x):
        output1 = self.linear1(x)
        output1 = F.relu(output1)
        # output1 = self.linear2(output1)
        # output1 = F.tanh(output1)
        output1 = self.linear3(output1)
        return output1


def get_data(x_train, y_train, batch_size=56):
    m, n = x_train.shape
    np.random.shuffle(np.arange(m))
    iters = int( m / batch_size) + 1
    for i in np.arange(iters):
        temp_x = x_train[i * batch_size : (i+1) * batch_size]
        temp_y = y_train[i * batch_size : (i+1) * batch_size]
        yield temp_x, temp_y

def train(model, device, optimizer, epoch, x_train, y_train, batch_size=56):
    model.train()
    for batch_idx, (data, target) in enumerate(get_data(x_train, y_train, batch_size)):
        data = torch.tensor(data, dtype=torch.float32)
        target = torch.tensor(target, dtype=torch.float32)
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.mse_loss(output, target)
        loss.backward()
        optimizer.step()
       # if batch_idx % 20 == 0:
            # error = mean_squared_error(target.numpy(), output.numpy())
            # print('epoch {}: mean squared_error: {:.6f}'.format(epoch, error))



def absolute_percent_error(y_test,  y_predict):
    err = np.abs((y_predict - y_test) / (y_test + 000.1))
    return err


def test(model, device, x_eval, y_eval):
    y_eval = torch.tensor(y_eval, dtype=torch.float32)
    x_eval = torch.tensor(x_eval, dtype=torch.float32)
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        data, target = x_eval.to(device), y_eval.to(device)
        output = model(data)
        temp_y = y_eval.numpy()
        temp_output = output.numpy().reshape(-1)
        error = np.mean(absolute_percent_error(temp_y, temp_output))
        #print(temp_y.shape, temp_output.shape) #.reshape((294, ))
        mse = mean_squared_error(temp_y, temp_output)
        print('mean_squared_error: {:.4f}, mse is {}'.format(error, mse))
    return temp_y, temp_output



x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")
x_eval = np.load("x_eval.npy")
y_eval = np.load("y_eval.npy")

device = torch.device("cpu")
model = MyLineModel().to(device)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
for epoch in range(1, 20):
    train(model, device, optimizer, epoch, x_train, y_train, batch_size=56)
    y, pred = test(model, device, x_eval, y_eval)
torch.save(model.state_dict(),"hjh_mlp_1.pt")




def line_mode(x_train, y_train, x_test, y_test):
    m22 = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
    result = m22.fit(x_train, y_train)
    pred = m22.predict(x_eval)
    print("mylinemodel interst {} ".format(np.mean(absolute_percent_error(y_eval, pred))))
    print("mylinemodel mse is {}".format(mean_squared_error(y_eval, pred)))