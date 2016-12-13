import pywt,numpy as np,os
from pyeeg  import ap_entropy 
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
        temp_extrasi1.append(ap_entropy(get_all_wavelet[x][y],len(get_all_wavelet[x][y])/5,temp_extrasi1[1]*float(0.2)))# diisi dengan aproximate entropy
        #param 1 itu datanya param ke dua itu panjangnya data yang ingin d potong , param ke tiga itu similarity. param ke dua dan ketiga diisi dengan mencoba coba
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
    print hasil_extrasi_fitur[0][0][4]
'''
training_array=[]
testing_array=[]
temp=[]
temp1=[]
for x in range(len(get_all_wavelet)):
	for y in range(len(get_all_wavelet[x])):
		if y < len(get_all_wavelet[x])-10:
		    training_array.append(hasil_extrasi_fitur[x][y])
		else :
		    testing_array.append(hasil_extrasi_fitur[x][y])
	#training_array.append(temp)
	#testing_array.append(temp1)
	#temp=[]
	#temp1=[]

#print training_array

# ini pembagiannya untuk setiap array traning ada 90 data dan setiap array testing ada 10 data. panjang dari array training dan testing adalah 5

# ini buat nyimpan kelas SVM nya aku asumsikan bahwa kelasnya banyaknya 5

#Nama --> Set
#1 --> F-->D
#2---> N-->C
#3---> O-->B
#4-->  S-->F
#5-->  Z-->A

#Normal--> O & Z (B Dan A )
#Epilepsi tidak aktif --> F & N(C Dan D)
#Epilepsi Aktif -->  S  
svm_class_all=[2,2,1,3,1]
svm_every_file=[]
temp_for_class_svm=[]
for x in range(len(svm_class_all)): #5
    for y in range(len(get_all_wavelet[x])-10): #100
        svm_every_file.append(svm_class_all[x])
    #svm_every_file.append(temp_for_class_svm)
    #temp_for_class_svm=[]
#print svm_every_file[0][0]
from sklearn.svm import SVC

X1= np.array(training_array)
print len(X1)
y1=np.array(svm_every_file)
print len(y1)
clf = SVC()    
clf.fit(X1,y1)

#hasil=[]
for x in range(len(testing_array)):
    print (clf.predict(testing_array[x]))
#print hasil




#print (svm_every_file[0])

#saiki kate lapo?????

