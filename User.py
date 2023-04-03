#-*- codeing = utf-8 -*-
#@Time : 2023-03-31 15:57
#@Author : Sophie
#@File : User.py
#@Software: PyCharm

import logging
import numpy as np

class User(object):
    def __init__(self,userid,usertype,env):
        #用户处在的环境
        self.env = env
        #用户id
        self.userid = userid
        #用户类型
        self.usertype = usertype
        #用户生成任务速率
        self.alpha = 0
        #每个time spot用户生成的任务
        self.tasks = {}
        #任务处理结果
        self.finished = True

    #初始化用户信息
    def InitUser(self):
        self.finished = True
        #生成用户类型
        np.random.seed(1)
        self.usertype = np.random.randint(0,3,dtype="l")
        return

    #更新用户信息
    def UpdateUser(self):
        return

    #生成新任务
    def SetupTask(self):
        """
        任务=任务类型+任务处理时间+任务价值+竞标价格
        :return:
        """
        #任务类型
        np.random.seed(1)
        self.usertype = np.random.randint(0,3,dtype="l")
        task={}
        task["userid"] = self.userid
        task["tasktype"] = np.random.randint(0,3,dtype="l")


    """
    记录任务提交记录
    """
    def RecordTask(self):
        return

    "获得拍卖结果"
    def RecordAuction(self):
        return
