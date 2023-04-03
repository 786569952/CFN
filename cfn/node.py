# -*- coding:utf-8 -*-
"""
the computing node
"""
# Authors: Ben

from typing import *
import uuid

class Node:

    def __init__(self, cap: dict, mu: float, cost: float, ) -> None:
        """
        """
        self.id = str(uuid.uuid4())
        self.cap = cap
        self.mu = mu
        self.cost = cost
        ...
    

if __name__ == '__main__':
    node = Node()
    pass