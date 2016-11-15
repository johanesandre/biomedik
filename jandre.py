import pywt,numpy as np,os
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
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)

#open Z file
openfileS=open(os.path.join(active_file_dir,"Zresult.txt"),"r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
composite_list_S=np.split(dataS,100)
get_all_data.append(composite_list_S)
# ^ end of input data



for x in range(len(get_all_data)):
    for y in range(len(get_all_data[x])) :
        # jandre kodemu startnya dari sini saja
        #if len(get_all_data[x][y])== int(4097):
         #   counter+=1
         
    
#print counter    