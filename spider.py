# -*- coding: utf-8 -*-  
import urllib  
import re  
import time  
import os  
  
#显示下载进度  
def schedule(a,b,c):  

print ('%02d%%'%(100.0 * count * block_size/ total_size);
#urllib.urlretrieve("http://sports.sina.com.cn/", reporthook= report_hook)



def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()  
    return html  
  
  
def downloadImg(html):  
    reg = r'src="(.+?\.jpg)" pic_ext'  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre, html)  
    #定义文件夹的名字  
    t = time.localtime(time.time())  
    foldername = str(t.__getattribute__("tm_year"))+"-"+str(t.__getattribute__("tm_mon"))+"-"+str(t.__getattribute__("tm_mday"))  
    picpath = 'C:\\DownloadS\\%s' % (foldername) #下载到的本地目录  
      
    if not os.path.exists(picpath):   #路径不存在时创建一个  
        os.makedirs(picpath)     
    x = 0  
    for imgurl in imglist:  
        target = picpath+'\\%s.jpg' % x  
        print 'Downloading image to location: ' + target + '\nurl=' + imgurl  
        image = urllib.urlretrieve(imgurl, target, schedule)  
        x += 1  
    return image;  
  
      
	  
      
if __name__ == '__main__':  
    print '''''            ************************************* 
            **      Welcome to use Spider      ** 
            **     Created on  2014-05-13      ** 
            **       @author: cruise           ** 
            *************************************'''  
      
    html = getHtml("http://tieba.baidu.com/p/2460150866")  
  
    downloadImg(html)  
    print "Download has finished."  