from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import os
# Create your views here.
HLS_url="http://127.0.0.1:80/static/video/live.m3u8"
@csrf_exempt
def index(request):

    return render(request,'index.html')

def files(request):
    filepaths=os.listdir('/home/pi/Desktop/static/')
    #filepaths.remove('System Volume Information')
    data={'files':filepaths}
    return render(request,'download_page.html',data)

def download(request):  
    """                                                                           
    Send a file through Django without loading the whole file into                
    memory at once. The FileWrapper will turn the file object into an             
    iterator for chunks of 8KB.                                                   
    """   
    filepath=request.GET.get('filepath') 
    filepath_='/home/pi/Desktop/static/'+filepath
    filename_=filepath.split('.')[0]
    filetype_='.'+filepath.split('.')[1]
    #下载文件  
    def readFile(fn, buf_size=262144):#大文件下载，设定缓存大小  
        f = open(fn, "rb")  
        while True:#循环读取  
            c = f.read(buf_size)  
            if c:  
                yield c  
            else:  
                break  
        f.close()  
    response = HttpResponse(readFile(filepath_), content_type='APPLICATION/OCTET-STREAM') #设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开  
    
    response['Content-Disposition'] = 'attachment; filename='+filename_+filetype_#设定传输给客户端的文件名称  
    
    response['Content-Length'] = os.path.getsize(filepath_)#传输给客户端的文件大小  
    
    return response  
