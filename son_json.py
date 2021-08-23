# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:18:34 2021

@author: Admin
"""

import json

x=10


x_json =json.dumps(x)

m= True
m_json = json.dumps(m)



sonlar = (34,54,98,678)
sonlar_json = json.dumps(sonlar)


# pythondan JSON ga o'tish dumps() funksiyasi orqali
#jsondan PYTHON ga o'tish loads() funksiyasi orqali

json.loads(m_json) 



bemor ={
        "ism" : "Alijon Valiyev",
        "yosh":30,
        "oila":True,
        "farzandlar":("Ahmad","Bonu"),
        "alergiya":None,
        "dorilar":[
            {"nomi":"analgin","miqdori":0.5},
            {"nomi":"panadol","miqdori":1.2}
            ]
        }

bemor_json=json.dumps(bemor,indent=4)
print(bemor_json)
# jsonga o'tkazish
with open('bemor.json','w') as f:
    json.dump(bemor,f)
    
#pythonga o'tkazish
# with open('bemor.json','w') as f:
#     json.dump(bemor,f)
    
bemor2=json.loads(bemor_json)


