
import logging
import logging.handlers


class MyLogs(logging.Logger):
    def __init__(self, class_name, filename="../logdir/mylog.log", mode='a'):
        super(MyLogs, self).__init__(self)
        # 日志文件名
        self.filename = filename
        self.class_name = class_name
        self.mode = mode

        logging.getLogger("{}.{}".format(self.__class__.__qualname__, class_name))
        logging.basicConfig(filemode='w')

        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 2)
        # fh = logging.handlers.RotatingFileHandler(self.filename, mode=self.mode, maxBytes=0, backupCount=10)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.INFO)
        fh_formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(fh_formatter)
        fh.set_name(self.class_name)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        date_format = "%m/%d/%Y %H:%M:%S %p"
        ch_formatter = logging.Formatter(datefmt=date_format, fmt=log_format)
        ch.setFormatter(ch_formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)


class t1:
    def __init__(self):
        pass

    def get(self):
        log = MyLogs("t1")
        log.error("value is {}".format(222))
        return 10

class t2:
    def __init__(self):
        pass
    def cal(self):
        logger = MyLogs("t2")
        logger.error("another value is {}".format(322))
        return 10


if __name__ == "__main__":
    my = t1()
    print(my.get())

    my2 = t2()
    print(my2.cal())