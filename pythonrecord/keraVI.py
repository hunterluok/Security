脚本 api.py 中有两处需要更改：
第一处：
开始导入包时：
需要将 from gevent.wsgi import WSGIServer
改为：from gevent.pywsgi import WSGIServer

第二处：
encode 方法定义中iteritems 改成 items

git clone http://www.github.com/fchollet/hualos

from keras import callbacks
remote = callbacks.RemoteMonitor(root='http://localhost:9000')
model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, validation_data=(X_test, Y_test), callbacks=[remote])
