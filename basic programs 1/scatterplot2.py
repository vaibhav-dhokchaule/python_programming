# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:22:18 2021

@author: HP
"""

import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0,1.0,1000)
y = numpy.random.normal(10.0,2.0,1000)
plt.scatter(x,y)
plt.show()