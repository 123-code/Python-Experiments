import numpy as np
import math
import random
class Tree():
    def __init__(self,node):
        self.node = node

    
class Node():
    def __init__(self ):
        self.children = []
        self.ucb_value = 0
        self.wins = 0
        self.visits = 0
        self.parent = None

    def add_child(self,new_node:Node)->None:
        new_node.parent = self
        # agregar direccion
        self.children.append(new_node)

    def get_parent(self):
        return self.parent
 
    def calculate_ucb(self,c:int,node:Node)->int:
        
        #UCB = Q(s, a) + c * sqrt(ln(N(s)) / N(s, a))
        Q = (self.wins/self.visits)/2
        UCB = Q + c * math.sqrt(math.log(self.get_parent().visits)/self.visits)
        return UCB

    def select(self)->int:
        best_ucb = -np.inf
        best_child = None
        for x in self.children:
            if x.ucb_value > best_ucb:
                best_ucb = x.ucb_value
                best_child = x

        return best_ucb

    def simulation(self,node):
        while len(node.children ) != 0:
            node = random.choice(node.children)
        return node.ucb_value   
             
        

    def expand(self)->Node:
        node  = Node()
        self.add_child(node)
        return node

    def backpropagate(self,node:Node,result:int):
        while node:
            node.visit_counts += 1
            node.wins += result
            node = node.parent


node = Node() 
n_iterations = 10

for x in range(n_iterations):
    root = node
    new_node = root.expand()
    new_node .simulation(new_node)
    new_node .backpropagate()
    
 
 
