#-*- codeing = utf-8 -*-
#@Time : 2023-03-31 15:57
#@Author : Sophie
#@File : User.py
#@Software: PyCharm

class User(object):
    def __init__(self,userid,usertype,alpha,task,env):
        """
        :param userid: 用户id
        :param usertype: 用户类型 0 1 2 个人 家庭 企业
        :param alpha: 用户任务生成速率
        :param task: 用户任务：任务类型（0 C 1 G 2 A）+任务处理时间+任务价值+竞标价格
        :param env: 当前环境
        """
        self.userid = userid
        self.usertype=usertype
        self.alpha = alpha
        self.task = task
        self.env = env

    #重置用户信息
    def InitUser(self):
        return

    #更新用户信息
    def UpdateUser(self):
        return
    """
    生成任务信息
    """
    def SetupTask(self):
        return

    """
    记录任务提交记录
    """
    def RecordTask(self):
        return

    "获得拍卖结果"
    def RecordAuction(self):
        return
