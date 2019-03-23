import numpy as np
from generation import *
import matplotlib.pyplot as plt

t1_val = t1_mat[511][511]
t2_val = t2_mat[511][511]
theta = 90
t = 5
spin_vector = np.array([[0],[0],[1]])

def rotation_y(spin_vector,theta):
    theta = np.radians(theta)
    rotation_mat = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
    return  np.matmul(rotation_mat , spin_vector )


def decay_recovery(rotated_mat,t,t1,t2):
     return  np.matmul(np.array([[np.exp(-t/t2),0,0],[0,np.exp(-t/t2),0],[0,0,np.exp(t/t1)]]) ,rotated_mat) + np.array([[0],[0],[1-np.exp(-t/t1)]])


rotated= rotation_y(spin_vector,90)
final = decay_recovery(rotated,t,t1_val,t2_val)
print(final)
