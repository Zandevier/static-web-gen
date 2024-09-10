from flask import Flask,request
from langchain.chat_models import ChatOpenAI
from dotenv import  load_dotenv
import os

from langchain.schema import (
    HumanMessage,
    SystemMessage
)
load_dotenv()

app = Flask(__name__)
OPEN_API_KEY =  os.getenv('SECRET_KEY')

post_response = ''
@app.route('/uploadimage',methods=['GET','POST'])
def uploadimage():
    data = ["jknd","akjsjd"]
    return data
    # return(request.files['imageUpload'])
    # image_path = "./images/" + imagefile.filename;
    # imagefile.save(image_path)
    
    # Code or function for the uploadimage from the machine learning model
@app.route('/uploaddescription',methods=['POST'])
def uploaddescription(): 
    global post_response
    user_input = request.json.get('description','')
    response = "msg from server " + user_input
    post_response = str(user_input)
    return response

@app.route('/uploaddescription',methods=['GET'])
def uploadDescription_display():
    global post_response
    chat = ChatOpenAI(openai_api_key=OPEN_API_KEY)
    # user_input = request.args.get('input', '')
    message = [
        SystemMessage(content = 'write the html code for the following'),
        HumanMessage(content=post_response)
        ]
    output = chat(message)
    text_message = output.content
    return text_message


if __name__ == '__main__':
    app.run(debug=True)