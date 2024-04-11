
from api import*
import os
from unicodedata import name
from flask import Flask 
from flask import request,send_from_directory,url_for,send_file
import tik1
import instadown
import datetime
import requests
import download_youtube
#import firebase_admin
from text2image import text2image

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
                  

#@app.route('/sms', methods=['POST'])
#def bot():
 # incoming_msg = request.values.get('Body', '').lower()
 # resp = MessagingResponse()
 # msg = resp.message()
 # print('a')
  #if 'tiktok' in incoming_msg:
   #try:
  #  msg.body('ها قد وصل الفيديو الان 🤞🏻')
   # print('done')
   # a=tik.download(incoming_msg) 
   # print(a)
    #
   # b=msg.media(a)
   #except :
   # return print('finish')
  #return str(resp)


@app.route('/')
def hello():
    
   return "hello Boyaf3"

@app.route("/uploads/<path:name>")
def download_file(name):
   print(name)
   return send_file(os.getcwd()+'/'+name)
  

tpo='''

▒▒┌──┐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┌─┐┌───┐
▒▒│┌┐│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│┌┘│┌─┐│
▒▒│└┘└┐┌──┐┌┐▒┌┐┌──┐┌┘└┐└┘┌┘│
▒▒│┌─┐││┌┐│││▒│││┌┐│└┐┌┘┌┐└┐│
▒▒│└─┘││└┘││└─┘││┌┐│▒││▒│└─┘│
▒▒└───┘└──┘└─┐┌┘└┘└┘▒└┘▒└───┘
▒▒▒▒▒▒▒▒▒▒▒┌─┘│▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒└──┘▒▒▒████████▒▒▒
▒▒┌┐▒▒▒▒▒▒▒▒▒▒┌┐▒█████████▌▒▒
▒▒││▒▒▒▒▒▒▒▒▒▒││▒███▒▀▀▒███▒▒
▒▒│└─┬──┬─┬──┐││▒███▒▒▒▒███▒▒
▒▒│┌┐││─┤┌┤│─┤└┘▒████▒▄████▒▒
▒▒│││││─┤│││─┤┌┐▒▒████████▒▒▒
▒▒└┘└┴──┴┘└──┘└┘▒▒▒▀████▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐██▌▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
'''

@app.route('/sms', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    media=request.values.get("MediaUrl0")
    print(media)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    date=datetime.datetime.now()
    if date.strftime("%H") == 12:
         list_file=os.listdir(os.getcwd()+'/')
         for mp4 in list_file:
           if mp4.endswith('.mp4'):
            os.remove(os.path.join(os.getcwd()+'/', mp4))
    print(incoming_msg)

    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////insta downloader api enjoy with boyaf3
    if 'instagram' in incoming_msg:
       a= instadown.insta(link=incoming_msg)
       msg.media(a)
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////// tiktk downloader api enjoy with Boyaf3

    if 'tiktok' in incoming_msg:
        a=tik1.result(url=incoming_msg)
        msg.media(a)
        #msg.body('🤞🏻ها هو الفيديو مع تحيات بويافع')
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////youtube downloader enjoy with Boyaf3

    if 'youtu' in incoming_msg:
        a=download_youtube.youtube(url='{}'.format(incoming_msg))
        print(a)
        #msg.body('ها قد وصل الفيديو الان 🤞🏻')
        msg.media('https://whatsbot57568.herokuapp.com/uploads/'+a)
        responded = True
        print('done')
       #msg.body(' 🤖: هناك خلل ما في الرابط المرسل الي يرجى التأكد من الرابط🔴 وفي حين استمرار هذه المشكلة يرجى التواصل معنا عبر الايميل الاتي'+'📞(boyaf3bot@gmail.com)')
        #msg.body(' 📞(boyaf3bot@gmail.com)ه🤖: هناك خلل ما في الرابط المرسل الي يرجى التأكد من الرابط🔴 وفي حين استمرار هذه المشكلة يرجى التواصل معنا عبر الايميل الاتي')
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////if code  not supported url or word
    if "boyaf3" in incoming_msg:
     msg.body(tpo)
    else:
        if incoming_msg.endswith("mp3"):
            responded = True
        elif incoming_msg.endswith("mp4"):
             responded = True
        else:    
         if "java" or "python" or "html" in incoming_msg:
          text=incoming_msg
          a=texttocode(input=text)
          responded = True
          msg.body(a)
    '''if "text2image" in incoming_msg:
        responded = True
        text=incoming_msg.replace("text2image","")
        result=text2image(text=text)
        msg.media(result)'''
        

    if not responded:
        msg.body('عذرا🔴  سوف يتم تحديث البوت قريبا هذا فقط بوت تجريبي مع تحيات بويافع🤞🏻')
        
    return str(resp),200
     
	

 
 

 #msg.media('https://example.com/path/image.jpg')


if __name__ == '__main__':
    app.run()

 







