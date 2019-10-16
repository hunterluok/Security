import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from zipfile import ZipFile


font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}


def get_list(data, step=1000):
    a = data.shape[0]
    k = int(a / step)
    d = []
    for i in range(k):
        temp = np.repeat(i, step)
        d.extend(temp)
    d = pd.DataFrame(d, columns=['class'])
    data = data[['A', 'B', 'C', 'CVT']]
    data = pd.concat([data, d], axis=1)
    data = data[['A', 'B', 'C', 'CVT']].groupby(data['class']).mean().reset_index()
    return data


def plot_myfit(data, name='xx'):
    plt.figure(figsize=(16, 9))
    plt.plot(data['A'])
    plt.plot(data['B'])
    plt.plot(data['C'])
    plt.plot(data['CVT'])

    plt.legend(['A', 'B', 'C', 'CVT'])
    plt.xlabel("data points", font1)
    plt.ylabel("value", font1)
    plt.title("data distribute", font1)

    # m = data.shape[0]
    # plt.plot(np.arange(m), np.repeat(0, m))
    plt.savefig("{}.jpg".format(name))
    #plt.savefig("/Users/zy0019/Desktop/mydianchang/{}.jpg".format(name))


def plot_pict(da):
    name = da.split('.')[0]
    myzip = ZipFile(da)
    csv_data = name + '.csv'
    open_data = myzip.open(csv_data)
    mydata  = pd.read_csv(open_data, skiprows=4) # columns=['A','B', 'C', 'CVT'])
    mydata = get_list(mydata)
    plot_myfit(mydata, name=name)
    open_data.close()
    myzip.close()
    return None


if __name__ == "__main__":
    lists = os.listdir('./')
    for da in lists:
        if da.endswith('zip'):
            plot_pict(da)
