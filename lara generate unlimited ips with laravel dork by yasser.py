import requests as req
import re
import json
import os

pages = 500



def pause():
    k = input("")

def start():
    file = input("Give me keywords file: ")
    if not file:
        start()
    else:
        print("Preparing...")
        if os.path.isfile(file):
            with open(file) as f:
                keywords = f.readlines()
                if not keywords:
                    print("File is empty!!!")
                    start()
                else:
                    dump(keywords)
        else:
            print("File not found!!")
            start()
            

def dump(keywords):
    for key in keywords:
        print(key+" -> getting data... ");
        for page in range(pages):
            link = "https://leakix.net/search?scope=leak&q="+key+"&page="+str(page)
            heads = {"api-key":"ezmeralda97", 'Accept':'application/json'}
            t = req.get(link, headers=heads).text

            try:
                datas = json.loads(t)
            except ValueError as err:
                break;
            else:
                for data in datas:
                    if(data['ip']!=''):
                        print(data['ip'])
                        with open("ips.txt", "a") as put:
                            put.write(data['ip']+"\n")

        print(key+" -> DONE! ");
        
    put.close()
    print("\n----> TASK IS COMPLETE! <----")
    
    

start()
pause()
