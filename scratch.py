# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:12:43 2017

@author: Baiyu
"""
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, csv

with open(r'E:\Software\Winpy\WinPython-64bit-3.6.1.0Qt5\notebooks\thesis.csv', 'r') as f:
    cont = csv.reader(f)
    tmp = [x for x in cont]
tmp.pop(0)
data = np.array(tmp, dtype=np.float)
data=10*np.log10(data)
x = np.linspace(5000,75000,15)/1000000

plt.plot(x, data[:,0], label='UTA', marker='D')
plt.plot(x, data[:,1], label='Normal', marker='>')
plt.plot(x, data[:,2], label='Static', marker='*')
plt.legend()
plt.grid()
plt.xlabel(u'User density $\lambda$')
plt.ylabel('Transmitting power per sector (dbm)')
plt.show()
