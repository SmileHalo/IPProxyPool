from Spiders import webPageSpider
#from ValidateServer import server
#import Utils.valitador
import threading
from os import system
from Utils import valitador
def start():
    #webPageSpider.start_crawl()
    #from Spiders import proxySpiderLuncher
    #proxySpiderLuncher.start_crawl_process()
    valitador.start_vali_process()
    
    #system('python ValidateServer\server.py')
    #threads=[]
    #thread=threading.Thread(target=server.start_server())
    #threads.append(thread)
    #for t in threads:
    #    t.setDaemon(True)
    #    t.start()  
    # Utils.valitador.validate()
    #webPageSpider.start_crawl()
   # proxySpiderLuncher.start_crawl_process()
    