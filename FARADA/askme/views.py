from django.shortcuts import render
import openai , os
from dotenv import load_dotenv
#from google.cloud import translate_v2 as translate


load_dotenv()

api_key = os.getenv("open_ai" , None)
#os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r"myservicesaccount-46cd4407d2d2.json"

#translate_client = translate.Client()
 
def farada (request):
    farada_response = None 
    #target = 'fa'

    if api_key is not None and request.method == "POST" :
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt =user_input #translate here
        print(prompt)
        response = openai.Completion.create (
            engine = 'text-davinci-003', #the gpt-4 currntly is not available for me so i use this engin
            prompt = prompt , 
            max_tokens= 256 , 
            temperature = 0.5  
        )
        print (response)
        farada_response = response["choices"][0]["text"] #translate here
    return render(request ,'main.html' , {"response" : farada_response})