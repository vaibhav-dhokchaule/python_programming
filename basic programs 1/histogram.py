# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:56:16 2021

@author: HP
"""

import numpy 
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0,5.0,250)
plt.hist(x,5)
plt.show()