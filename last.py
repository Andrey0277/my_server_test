import socket
from _io import open
import os

def get_size(file_name):
    st= os.stat(file_name)
    return st.st_size




def get_ansver(par,file_name):
    siz=get_size(file_name)
    
    if "html"==par:
        return "HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: text/html\r\ncharset=utf-8\r\nConnection: close\r\nContent-Length:" +str(siz)   +"\r\n\r\n"
    elif "css"==par:
        return "HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type:text/css\r\ncharset=utf-8\r\nConnection: close\r\nContent-Length:" +str(siz)   +"\r\n\r\n"
    
    
    elif par=="jpeg"or "jpg"==par:
      
        return"HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length:" +str(siz)   +"\r\n\r\n"
    elif par=="gif":
         return "HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: image/gif\r\nConnection: close\r\nContent-Length:" +str(siz)   +"\r\n\r\n"
    elif par=="mp3":
         return "HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: audio/mpeg\r\nConnection: close\r\nContent-Length:" +str(siz)   +"\r\n\r\n"
    elif par=="MOV":
         return "HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: video/quicktime \r\nConnection: close\r\nContent-Length:" +str(siz)+"\r\n\r\n"
 
 
def write_kili_byte(f,siz,soket):
    print(siz)
	
    for i in range(siz//100000):
        soket.sendall(f.read(100000))

    if (siz%100000!=0):
        soket.sendall(f.read(100000))
    
        



 
 
    

def  get_content(soc):
    data=soc.recv(1024)
    
    file_name=str.split(data.decode('utf-8'))[1][1:]
   
    print(data.decode('utf-8'))
    print(file_name)
    if file_name=="":
        file_name="info.html"
  
    rec= get_ansver(str.split(file_name,".")[1],file_name)    
    siz=get_size(file_name)
    print(rec)
    file=open(file_name,"rb")
    
    soc.sendall(bytes(rec,'utf-8'))
   
    write_kili_byte(file, siz, soc)
   
    
 
    
    
def get_404(soc):
    rec="""HTTP/1.1 200 OK\r\nServer: Apache\r\nContent-Type: text/html\r\ncharset=utf-8\r\nConnection: close\r\n\r\n"""                 
    soc.sendall(bytes(rec,'utf-8'))
    soc.sendall(bytes("<h1>error:404<h1>",'utf-8')) 
      

    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))
s.listen(1)

while True:
    soc,conect= s.accept()
    
   
    try:
        get_content(soc)
    except:
        get_404(soc)
    soc.close()

