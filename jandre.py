import pywt,numpy as np,os

import waveletdecompose as dc
#import coba1file as coba
#import cobafileturun as cobalagi
#import pyegg as buatentropy
#import approximateEn as apEn
np.set_printoptions(threshold=np.nan)

active_file_dir=os.path.dirname(__file__)
get_all_data=[]
get_all_wavelet=[] # -> untuk menyimpan semua hasil waveletnya dari 5 file besar tersebut.

np.set_printoptions(threshold=np.nan)
active_file_dir=os.path.dirname(__file__)
get_all_data=[]
get_all_wavelet=[] # -> untuk menyimpan semua hasil waveletnya dari 5 file besar tersebut.

#open file F
openfileS=open(os.path.join(active_file_dir,"Fresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
#become list in data.
temp2dataS= map(int, temp1dataS)


#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data


#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open N data
openfileS=open(os.path.join(active_file_dir,"Nresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")


#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)


#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)

#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#get O data
openfileS=open(os.path.join(active_file_dir,"Oresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")


#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)


#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open S file
openfileS=open(os.path.join(active_file_dir,"Sresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")


#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)


#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open Z file
openfileS=open(os.path.join(active_file_dir,"Zresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")


#become list in data.
temp2dataS= map(int, temp1dataS)


#become list in data.
temp2dataS= map(int, temp1dataS)

#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)
# ^ end of input data

temp_wavelet1=[]
for x in range(len(get_all_data)):
    for y in range(len(get_all_data[x])) :
        # jandre kodemu startnya dari sini saja
        if len(get_all_data[x][y])== int(4097):
        	#get_all_wavelet.append(dc.waveletTransform(get_all_data[x][y]))
        	temp_wavelet1.append(dc.waveletTransform(get_all_data[x][y]))
    get_all_wavelet.append(temp_wavelet1)
    temp_wavelet1=[]         

#print (get_all_wavelet[0][0])
temp_extrasi1=[]
temp_wavelet1=[]# for getting temporary array for fiture extraction
hasil_extrasi_fitur=[] #getting all result in feature extraction
for x in range(len(get_all_wavelet)):
    for y in range(len(get_all_wavelet[x])):
        temp_extrasi1.append(dc.energi(get_all_wavelet[x][y]))
        temp_extrasi1.append(np.std(get_all_wavelet[x][y])) # stdmu salah cak ji. aku langsung ambil ae iki.
        temp_extrasi1.append(dc.maximum(get_all_wavelet[x][y]))
        temp_extrasi1.append(dc.mininum(get_all_wavelet[x][y]))
        #temp_extrasi1.append() diisi dengan aproximate entropy
        temp_wavelet1.append(temp_extrasi1)
        temp_extrasi1=[]
    hasil_extrasi_fitur.append(temp_wavelet1)
    temp_wavelet1=[]
    
# hasil seluruh extrasi fitur ada di hasil_extrasi_fitur dengan data berukuran 3D

'''
print len(hasil_extrasi_fitur)
if len(hasil_extrasi_fitur) >int(0):
    print len(hasil_extrasi_fitur[0])
    print hasil_extrasi_fitur[0][0][0]
    print hasil_extrasi_fitur[0][0][1]
    print hasil_extrasi_fitur[0][0][2]
    print hasil_extrasi_fitur[0][0][3]
   # print hasil_extrasi_fitur[0][0][4]
'''
# ini buat nyimpan kelas SVM nya aku asumsikan bahwa kelasnya banyaknya 5
svm_class_all=[1,2,3,4,5]
svm_every_file=[]
temp_for_class_svm=[]
for x in range(len(svm_class_all)):
    for y in range(len(get_all_wavelet[x])):
        temp_for_class_svm.append(svm_class_all[x])
    svm_every_file.append(temp_for_class_svm)
    temp_for_class_svm=[]

#print (svm_every_file[0])

#saiki kate lapo?????
