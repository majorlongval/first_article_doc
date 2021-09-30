# importing libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# importing data
data = pd.read_csv('data.csv')

# Calculating the coefficient of friction
data['mass'] /= 1000
data['mass'] += 0.0276
mu_no_groove = (1/np.pi)*np.log((5.7*data['no_groove']+2*(0.03+0.0009)*9.81*data['mass'])/\
                                (-5.7*data['no_groove']+2*(0.03+0.0009)*9.81*data['mass']))
print(mu_no_groove)
#creating  initial plot
# fig1 = plt.figure()
# plt.plot(data['mass'],data['no_groove'])
# plt.plot(data['mass'],data['simple_groove'])
# plt.plot(data['mass'],data['complexe_groove'])
# plt.plot(data['mass'],data['big_groove'])
# plt.grid(True)
# plt.xlabel('mass (g)')
# plt.ylabel('Torque (Nm)')
# plt.legend(['no groove', 'simple groove','complex groove',
# 'big groove'])
# plt.show()