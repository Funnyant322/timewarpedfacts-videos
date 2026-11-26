import sys,os
data=open(sys.argv[1],'rb').read(); out=sys.argv[2]; pre=sys.argv[3]; os.makedirs(out,exist_ok=True); p=0; n=0
while p<len(data):
    nl=data.index(b'\n',p); hdr=data[p:nl].decode().split(); L=int(hdr[1]); open(f'{out}/{pre}{n}.jpg','wb').write(data[nl+1:nl+1+L]); p=nl+1+L; n+=1
print(n)
