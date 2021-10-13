# importing libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# importing data
data = pd.read_csv('data.csv')

# Calculating the coefficients of friction
data['mass'] /= 1000
data['mass'] += 0.0276
radius = 0.03
cable_radius = 0.0009
g = 9.81
gear_ratio = 5.9
mu_no_groove = (1/np.pi)*np.log(((radius+cable_radius)*data['mass']*g)/((radius+cable_radius)*data['mass']*g - gear_ratio*data['no_groove']))
print(mu_no_groove)
mu_simple_groove = (1/np.pi)*np.log((radius*data['mass']*g)/(radius*data['mass']*g - gear_ratio*data['simple_groove']))
print(mu_simple_groove)
lambda_simple = mu_simple_groove/mu_no_groove
print(lambda_simple)
mu_complexe_groove = (1/np.pi)*np.log((radius*data['mass']*g)/(radius*data['mass']*g - gear_ratio*data['complexe_groove']))
lambda_complexe = mu_complexe_groove/mu_no_groove
mu_big_groove = (1/np.pi)*np.log(((radius-0.0018)*data['mass']*g)/((radius-0.0018)*data['mass']*g - gear_ratio*data['big_groove']))
lambda_big = mu_big_groove/mu_no_groove

# Changing the figure font parameters
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer modern roman"]})

# Creating the figure
fig, ax1 = plt.subplots()

color = 'black'
ax1.set_xlabel('mass [kg]')
ax1.set_ylabel('$\mu_k$', color = color)
plt1 = ax1.plot(data['mass'], mu_no_groove, color =color)
plt2 = ax1.plot(data['mass'], mu_simple_groove, color=color, linestyle='--')

ax2 = ax1.twinx()

color = 'blue'
ax2.set_ylabel('$\eta$', color=color)  # we already handled the x-label with ax1
plt3 = ax2.plot(data['mass'], lambda_simple, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.grid(True)
all_plt = plt1+plt2+plt3
ax1.legend(all_plt,['$\mu_{k1}$:no groove', '$\mu_{k2}$:simple groove', '$\eta = \mu_{k2}/\mu_{k1}$'])
plt.show()
# plt.plot(data['mass'],data['simple_groove'])
# plt.plot(data['mass'],data['complexe_groove'])
# plt.plot(data['mass'],data['big_groove'])
# plt.grid(True)
# plt.xlabel('mass (g)')
# plt.ylabel('Torque (Nm)')
# plt.legend(['no groove', 'simple groove','complex groove',
# 'big groove'])
# plt.show()