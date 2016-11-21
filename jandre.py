import pywt,numpy as np,os
<<<<<<< HEAD
import waveletdecompose as dc
import coba1file as coba
#import cobafileturun as cobalagi
#import pyegg as buatentropy
#import approximateEn as apEn
np.set_printoptions(threshold=np.nan)

active_file_dir=os.path.dirname(__file__)
get_all_data=[]
get_all_wavelet=[] # -> untuk menyimpan semua hasil waveletnya dari 5 file besar tersebut.

=======
np.set_printoptions(threshold=np.nan)
active_file_dir=os.path.dirname(__file__)
get_all_data=[]
get_all_wavelet=[] # -> untuk menyimpan semua hasil waveletnya dari 5 file besar tersebut.
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
#open file F
openfileS=open(os.path.join(active_file_dir,"Fresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
#become list in data.
temp2dataS= map(int, temp1dataS)
<<<<<<< HEAD

#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data

=======
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open N data
openfileS=open(os.path.join(active_file_dir,"Nresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
<<<<<<< HEAD

#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)

=======
#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#get O data
openfileS=open(os.path.join(active_file_dir,"Oresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
<<<<<<< HEAD

#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)

=======
#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open S file
openfileS=open(os.path.join(active_file_dir,"Sresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
<<<<<<< HEAD

#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)

=======
#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open Z file
openfileS=open(os.path.join(active_file_dir,"Zresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
<<<<<<< HEAD

#become list in data.
temp2dataS= map(int, temp1dataS)

=======
#become list in data.
temp2dataS= map(int, temp1dataS)
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)
# ^ end of input data


<<<<<<< HEAD
'''
cobawavelet= dc.waveletTransform(coba.eeg)
print cobawavelet
nilaimax=np.amax(cobawavelet)
print nilaimax

cobaentropy = dc.ap_entropy(cobawavelet)

#cobaentropy

#hasilcobalagi= dc.waveletTransform(cobalagi.eeg)
#print hasilcobalagi
'''

=======
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374

for x in range(len(get_all_data)):
    for y in range(len(get_all_data[x])) :
        # jandre kodemu startnya dari sini saja
<<<<<<< HEAD
        if len(get_all_data[x][y])== int(4097):
        	get_all_wavelet.append(dc.waveletTransform(get_all_data[x][y]))
         
    
#print counter    

print get_all_wavelet
=======
        #if len(get_all_data[x][y])== int(4097):
         #   counter+=1
         
    
#print counter    
>>>>>>> d2481780c9e52f24896c133d0b7610d6cde17374
