import pywt,numpy as np
np.set_printoptions(threshold=np.nan)

openfileS=open("C:\\Users\\freddy\\Downloads\\Compressed\\S\\Sresult.txt","r")
tempdataS=openfileS.read()
temp1dataS=tempdataS.split("\n")
#become list in data.
temp2dataS= map(int, temp1dataS)
#become numpy array.
dataS=np.asarray(temp2dataS)
#split data every 4097 data
get_S_wavelet=[]
composite_list_S=np.split(dataS,100)
for x in range(len(composite_list_S)):
    
    '''
    ca,cd1,cd2,cd,cd3,cd4 = pywt.wavdec(composite_list_S[x],"db1",level=4)
    temp=[]
    temp.append(ca)
    temp.append(cd)
    get_S_wavelet.append(temp)
    #print len(temp)
    #sisanya kita tinggal ngepush semua datanya yang kita dapatkan dari wavelet yang ada.
print len(get_S_wavelet[1])
'''