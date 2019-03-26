# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:16:27 2019

@author: Ahmed
"""

from PIL import Image
import numpy as np
#import cv2

img = Image.open('face.png').convert('L')
img = np.asarray(img)
print(img)
row,col=np.shape(img)
#image=Image.fromarray(np.abs(np.fft.fftshift(np.fft.fft2(img))))
print(np.fft.fft2(img))
#image.show()
pd=(img+1)*250+1
#print(pd)

T1=(img+1)*120+100

T2=(img/3+50)
print(T1)
#image=Image.fromarray(T2)
#image.show()
##x=complex(1,2)
print(T2)
## modifing to a vector
x=np.array([[0.0],[0.0],[1.0]])
spin=img.tolist()
for i in range(row):
    for j in range  (col):
        spin[i][j]=pd[i,j]*x
        #spin[i][j]=img[i,j]*x
        #spin[i][j]=x    
spin=np.array(spin)
#print(spin)
## rotation around y axis
filpAngle=np.radians(90)
TE=10
TR=1000
yRotMat=np.array([[np.cos(filpAngle), 0, np.sin(filpAngle)], [0, 1, 0],[-np.sin(filpAngle), 0, np.cos(filpAngle)]])
#
yRotMat2=np.array([[np.cos(-filpAngle), 0, np.sin(-filpAngle)], [0, 1, 0],[-np.sin(-filpAngle), 0, np.cos(-filpAngle)]])
kspace=np.zeros([row,col], dtype=np.complexfloating)

#def decay(te,t1,t2,spin):
#    decay = np.array([[np.exp(-te/t2), 0 , 0],[0 ,np.exp(-te/t2), 0],[0, 0, np.exp(-te/t1)]])
#    return np.matmul(decay,spin)+np.array([[0],[0],[1-np.exp(-te/t1)]])
#
#def zRot(theta):
#    return np.array([[np.cos(theta),-np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
#
thx=np.zeros([row,col])
thy=np.zeros([row,col])
for kRow in range(row):
    #Rf
    #print(kRow)
    for i in range(row):
        for j in range  (col):
            spin[i][j]=np.matmul(yRotMat, spin[i][j])
#        print(kRow,spin)

#    #decay
#
    for i in range(row):
        for j in range  (col):
            spin[i][j][0]=spin[i][j][0]*np.exp(-TE/T2[i][j])
            spin[i][j][1]=spin[i][j][1]*np.exp(-TE/T2[i][j])
#            print(spin[i][j])
#            print(i,' ', j)
#            print('------------------------')
#    #column   
#    #print(spin[0][0])
    for kcol in range(col):
#        print(kRow,' ',kcol)
#        print(kcol)
        stepi=2*np.pi/(row)*(kRow)
        stepj=2*np.pi/(row)*(kcol)
        
#        print('X',thx)
#        print('Y',thy)
        for i in range(row):
            for j in range  (col):
                theta=stepi*i + stepj*j
#                thx[i][j]=np.degrees(stepi*i)
#                thy[i][j]=np.degrees(stepj*j)
                
#                thetai=stepi*j 
#                thetaj=stepj*i
                
                kspace[kRow][kcol]+=(np.sqrt(np.square(spin[i][j][0])+np.square(spin[i][j][1]))*np.exp(complex(0,-theta)))
#                print('thetai= ',thetai,' ','thetaj = ', thetaj)
#                print('------------------------')
#                rot=np.matmul(zRot(thetaj),zRot(thetai))
#                spin[i][j]=np.matmul(rot,spin[i][j])
#                kspace[kRow][kcol]+=complex(spin[i][j][0],spin[i][j][1])
#               
                
#                print(i,' ', j)
#                #print(kspace[kRow][kcol])
#                print(kspace)
#                print('------------------------')
#               # print((np.sqrt(np.square(spin[i][j][0])+np.square(spin[i][j][1])))*np.exp(complex(0,theta)))
#                #spin[i][j]=np.matmul(yRotMat, spin[i][j])
#    #print('Done---------------------------')
#        print(th)
##    prin90t(spin)
#    img=np.fft.ifft2(kspace)
#    img=np.abs(img)
#    image=Image.fromarray(img)
#    image.show()
            
    for i in range(row):
        for j in range  (col):
            spin[i][j][2] *=(1-np.exp(-TR/T1[i][j]))
            spin[i][j]=np.matmul(yRotMat2, spin[i][j])
            spin[i][j][0]=0
            spin[i][j][1]=0
            
#
##for i in range(row):
##    kspace[i]=np.fft.fft(kspace[i])
##for i in range(row):
##    kspace[i,0:row]=np.fft.fft( kspace[i,0:row])     
#
img=(kspace)
print(np.round(img))
##img=np.abs(img)
#
##image=Image.fromarray(img)
##image.show()
img=(np.fft.ifft2(kspace))
img=np.round(np.abs(img))
image=Image.fromarray(img)
image.show()
print(img)

#print(img)
##print(img)