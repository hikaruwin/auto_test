"""
读取配置。这里配置文件用的yaml，也可用其他如xml，ini等，需在file_reader中添加相应的方法进行处理
"""

import os

from utils.file_reader import YamlReader


# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


class Config:

    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过’---‘分节的。用YamlReader读取返回的事一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        :param element: yaml文件中一行的键
        :param index: list下标
        :return: 返回对应list下标键的值
        """
        return self.config[index].get(element)
