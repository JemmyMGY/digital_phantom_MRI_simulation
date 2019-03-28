# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:28:29 2019

@author: Ahmed
"""
import numpy as np
def flip (TE,TR,T1,T2,pd,filpAngle):
    ## initializie
    pd = np.asarray(pd)
    T1 = np.asarray(T1)
    T2 = np.asarray(T2)
    filpAngle=np.radians(filpAngle)
    row,col=np.shape(pd)
    kspace=np.zeros([row,col], dtype=np.complexfloating)
    #rotation around y axis
    yRotMat=np.array([[np.cos(filpAngle), 0, np.sin(filpAngle)], [0, 1, 0],[-np.sin(filpAngle), 0, np.cos(filpAngle)]])
    # re rotation
    yRotMat2=np.array([[np.cos(-filpAngle), 0, np.sin(-filpAngle)], [0, 1, 0],[-np.sin(-filpAngle), 0, np.cos(-filpAngle)]])
    ## modifing to a vector
    x=np.array([[0.0],[0.0],[1.0]])
    spin=pd.tolist()
    for i in range(row):
        for j in range  (col):
            spin[i][j]=pd[i,j]*x 
    spin=np.array(spin)
    # start kspace
    for kRow in range(row):
        #Rf
        for i in range(row):
            for j in range  (col):
                spin[i][j]=np.matmul(yRotMat, spin[i][j])
#    #decay
        for i in range(row):
            for j in range  (col):
                spin[i][j][0]=spin[i][j][0]*np.exp(-TE/T2[i][j])
                spin[i][j][1]=spin[i][j][1]*np.exp(-TE/T2[i][j])
        # gradiant and read data
        for kcol in range(col):
            stepi=2*np.pi/(row)*(kRow)
            stepj=2*np.pi/(row)*(kcol)
        
            for i in range(row):
                for j in range  (col):
                    theta=stepi*i + stepj*j
                    kspace[kRow][kcol]+=(np.sqrt(np.square(spin[i][j][0])+np.square(spin[i][j][1]))*np.exp(complex(0,-theta)))
        # spoilar   
        for i in range(row):
            for j in range  (col):
                spin[i][j]=np.matmul(yRotMat2, spin[i][j])
                spin[i][j][0]=0
                spin[i][j][1]=0
                spin[i][j][2] *=(1-np.exp(-TR/T1[i][j]))
        # take iamge back
    img=(np.fft.ifft2(kspace))
    img=np.round(np.abs(img))
    return img
    
    