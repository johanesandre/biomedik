import numpy as np
import pywt
import math

def waveletTransform(nilai):
	cA, cD1, cD2,cD3,cD4,cD5,cD6,cD7,cD8 = pywt.wavedec(nilai, "db4", level = 8)
	return cA

def energi(nilai):
    MN = len(nilai)
    [abs(x) for x in nilai]
    jumlah = sum(nilai)
    E = jumlah/MN
    #print('The energy is {}.'.format(E))
    return E

def standardeviasi(nilai):
	np.std(nilai)
	return nilai

def maximum(nilai):
	nilaimaximum= np.amax(nilai)
	return nilaimaximum

def mininum(nilai):
	nilaimininum= np.amin(nilai)
	return nilaimininum



'''
def waveletTransform(lagu):
	cA, cD = pywt.dwt(lagu, 'bior2.8')

	return cD
	#cd itu highpass,ca lowpass
'''



def crossCorrelation(fullLagu, potonganLagu):
	hasilCross = np.correlate(fullLagu, potonganLagu)

	return hasilCross

def magnitude(crossCorrelation):
	magnitude = np.sqrt(crossCorrelation.dot(crossCorrelation))

	return magnitude


