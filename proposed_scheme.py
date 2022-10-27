#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import bplib as bp
import numpy as np
import random
import hashlib
import time
import petlib
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

G = bp.bp.BpGroup()

def authorized():
    Z_p = G.order()
    k_u = Z_p.random()
    sk_u = Z_p.random()
    
    return k_u, sk_u

def buildIndex(word_list,k_u, sk_u):
    delta_list = []
    c_list = []
    
    g2 = G.gen2()
    for word in word_list:
        Z_p = G.order()
        r_i = Z_p.random()
        tmp = word + str(sk_u)
        
        g1 = G.hashG1(tmp.encode('utf-8'))
        g_2 = g2.mul(r_i)
        
        k = k_u ** 2
        gt = G.pair(g1.mul(k), g_2)
        c = g2.mul(k_u*r_i)

        delta_list.append(gt)
        c_list.append(c)
        
    return delta_list, c_list

def Trapdoor(k_u, word_list):
    result = []

    for word in word_list:
        tmp = word + str(sk_u)
        g1 = G.hashG1(tmp.encode('utf-8'))
        
        t_i = g1.mul(k_u)
        result.append(t_i)
        
    return result

def Search(delta_lst, c_lst, t):
    cv = 0
    iterlen = 0
    if(len(c_lst) <= len(t)):
        iterlen = len(c_lst)
    else :
        iterlen = len(t)
    for i in range(iterlen):
        gt = G.pair(t[i], c_lst[i])
        if gt == delta_lst[i]:
            cv += 1
    if cv == len(t):
        return True
    else:
        return None
    

