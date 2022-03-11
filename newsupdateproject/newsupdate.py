#news update

import requests
def NewsFromBBC():
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=tpo&apikey=6721c46e385a4a6cb4d4516999eb0e0"
    open_bbc_page=requests.get(main_url).json()
    article=open_bbc_page ["article"]
    
    result=[]

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i+1,results[i])

    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.Speak(results)
if __name__ == "__main__":


       NewsFromBBC()
