from server import Server
from device import Device
import mylog
import json
import numpy as np
import os
import shutil
import User,Node,Broker
currentPath = os.path.abspath()
parentDir = os.path.abspath(os.path.dirname(currentPath)+os.path.sep+".")
class Env:

    def Init(self):#初始化数据
        """
        初始化用户，节点，broker信息
        :return:
        """
        for user in self.users:
            user.init()
        for node in self.nodes:
            node.init()
        for broker in self.brokers:
            broker.init()

    def InitEnv(self):# 重置当前环境
        """
        重置当前用户，节点，broker信息
        :return:
        """
        for user in self.users:
            user.InitUser()
        for node in self.nodes:
            node.InitNode()
        for broker in self.brokers:
            broker.InitBroker()

    def UpdateEnv(self):# 更新环境
        """
        更新当前用户，节点，broker信息
        :return:
        """
        self.logger.info('EnvUpdate start')
        for user in self.users:
            user.UpdateUser()
        for node in self.nodes:
            node.UpdateNode()
        for broker in self.brokers:
            broker.UpdateBroker()
        self.logger.info('EnvUpdate finish')

    def GetEnv(self):# 获取当前环境
        """
        返回当前节点，用户，broker的信息
        :return:
        """
        state = []
        # 添加节点信息
        for node in self.nodes:
            state.append(node.env)
            state.append(node.nodeid)
            state.append(node.ask)
            state.append(node.cap)
            state.append(node.cost)
            state.append(node.cucap)
            state.append(node.mu)
            state.append(node.pt)
            state.append(node.ut)
        # 添加用户信息
        for user in self.users:
            state.append(user.env)
            state.append(user.userid)
            state.append(user.usertype)
            state.append(user.alpha)
        # 添加broker信息
        for broker in self.brokers:
            state.append(broker.env)
            state.append(broker.time)
            state.append(broker.current)
            state.append(broker.bidcouple)
            state.append(broker.property)
        return np.array(state)

    def GetTask(self):# 获取任务
        """
        获得当前用户的任务需求
        :return:
        """
        state = []
        for user in self.users:
            state.append(user.task)
        return np.array(state)

    def CalTask(self):# 计算任务价值 V(Lq)
        """
        Lq = a^2/[b(b-a)]
        a:用户任务到达速率
        b:服务计算速率
        """
        state = []
        for user in self.users:
            Lqs = []
            for node in self.nodes:
                Lq = math.pow(user.alpha)/(node.mu*(node.mu-user.alpha))
                Lqs.append(Lq)
            state.append(Lqs)
        return np.array(state)

    def GetBidPrice(self, task):# 获取出价
        """
        获得当前用户的出价信息
        :param task:
        :return:
        """
        state = []
        for user in self.users:
            state.append(user.Setupbid())
        return np.array(state)

    def GetAucResult(self):# 获取拍卖结果
        """
        获得当前拍卖结果
        :return:
        """
        return broker.bidcouple

    def GetReward(self, result):# 获取奖励
        """
        获得总的拍卖奖励
        """
        return self.broker.CalReward()