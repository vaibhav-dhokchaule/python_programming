# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:05:23 2021

@author: HP
"""

import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0,1.0,100000)
plt.hist(x,100)
plt.show()