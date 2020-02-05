import os
import sys
import math
try:
    import cv2
except:
    os.system("pip3 install opencv-python --user")
try:
    import numpy as np
except:
    os.system("pip3 install numpy --user")

import argparse

try:
    import skimage.metrics
except:
    os.system("pip3 install scikit-image --user")

try:
    import scipy
    from scipy import stats
except:
    os.system("pip3 install scipy --user")

class Sumando():
    def __init__(self):
        print("Hola, esto es el constructor ")       
    def calcularMSE(self,original,cuantificada):
        x = cv2.imread(original, -1)
        y = cv2.imread(cuantificada, -1)
        MSE = skimage.metrics.mean_squared_error(x, y)
        return MSE
    def GetPesos(self,cuantificador, q):
        total = os.stat("/tmp/"+str(q)+"/"+str(cuantificador)+"/").st_size
        return total
    def GetMSE(self,cuantificador,imagen,q=8):
        cuantizada = "/tmp/"+str(q)+"/"+cuantificador+"/inversas/"+"{:03d}".format(imagen)+".png"
        original = "/tmp/"+str(q)+"/original/"+"{:03d}".format(imagen)+".png"
        x = cv2.imread(original, -1)
        y = cv2.imread(cuantizada, -1)
        MSE = skimage.metrics.mean_squared_error(x, y)
        return MSE
    def AddSizes(path = "/tmp/", N = 5):
        tamanoTotal = 0.0
        tamanoTotalNuevo = 0.0 
        for i in range(N):            
            path_archivo_normal = os.path.join(path,"{:03d}".format(i)+".png")
            path_archivo_reducido = os.path.join(path,"LL{:03d}".format(i)+".png")
            tamanoTotalNuevo += os.stat(path_archivo_reducido).st_size
            path_archivo_reducido = os.path.join(path,"LH{:03d}".format(i)+".png")
            tamanoTotalNuevo += os.stat(path_archivo_reducido).st_size
            path_archivo_reducido = os.path.join(path,"HL{:03d}".format(i)+".png")
            tamanoTotalNuevo += os.stat(path_archivo_reducido).st_size
            path_archivo_reducido = os.path.join(path,"HH{:03d}".format(i)+".png")
            tamanoTotal += os.stat(path_archivo_normal).st_size
            tamanoTotalNuevo += os.stat(path_archivo_reducido).st_size
        print("Original " + str(tamanoTotal))
        print("Nuevo " + str(tamanoTotalNuevo))
        print("Ratio de compresion " + "{0:.5f}".format(tamanoTotal/tamanoTotalNuevo))
        """
    if __name__ =="__main__":
            if len(sys.argv) < 2:
                AddSizes()
            elif len(sys.argv) == 2:
                AddSizes(N=int(sys.argv[1]))            
            else:
                AddSizes(sys.argv[1],int(sys.argv[2]))
                """
