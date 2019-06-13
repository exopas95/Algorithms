# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:21:53 2019

@author: cross
"""

import utility
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data
def bin_search_tree_insert(root,node):
    if root is None:
        root=node
    else:
        if(root.data > node.data):
            if(root.l_child is None):
                root.l_child = node
            else:
                bin_search_tree_insert(root.l_child, node)
        else:
            if(root.r_child == None):
                root.r_child = node
            else:
                bin_search_tree_insert(root.r_child, node)
        
#def bin_search_t:
#    tree_delete(root,node):
    
    
r = Node(7)
bin_search_tree_insert(r,Node(9))
bin_search_tree_insert(r,Node(1))
bin_search_tree_insert(r,Node(3))
bin_search_tree_insert(r,Node(12))

utility.print_inOrder(r)
print()
utility.print_preOrder(r)
