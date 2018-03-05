
from flask import *
import time
app = Flask(__name__)
@app.route('/')
def Process():
    return '''
<html>
<head>
</head>
<body>
<h1>Welcome to Raymond’s super mega flask website</h1>
<p> I power ai and more</p>

</body>
</html>
'''

new_message=""
'''
@app.route('/AI',methods=['GET','POST'])
def ai():
    if request.method=='GET':return '<form><input type="text"></input><button type="submit">GET</button></form>'

    return myai.rec(request.form['msg'])
'''
chat='''
Welcome to chat alpha
'''


@app.route("/new")
def newssa():
    global new_message
    return new_message

css='''<style>
    body{
    border-style:groove;
    border-color:orange;
    background-color:black;
     margin: 0;
  padding: 5px;
    }
    p{
    color:white;

  list-style: none;

  font: 0.8em  Consolas, 'Courier New', 'Comic sans';
  line-height: 1.6em;

  -webkit-border-bottom-right-radius: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -moz-border-radius-bottomright: 3px;
  -moz-border-radius-bottomleft: 3px;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
    }

    </style>'''
@app.route("/get")
def get1():
    global chat,css
    out=css
    for x in chat.splitlines():
        out=out+x+"<br>"
    return '<meta http-equiv="cache-control" content="no-cache" /><meta http-equiv="expires" content="0" /><meta http-equiv="pragma" content="no-cache" /><p>'+out+"</p>"+'''

    <script>
    var cache;
    cache="";
    function reload(text){
    if(cache!=text){
    cache=text
    var para = document.createElement("p");
    var node = document.createTextNode(text);
    para.appendChild(node);
    document.body.appendChild(para);
    }
    }
    function Get(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}
function call(){
Get('/new',reload)

}
setInterval(call, 2000);

    </script>
    '''
temp='''
<style>
iframe{
width:100%;
height:90%;
}
input{
background-color: yellow;
width:90%;
height:10%;
font-size:40;
}
button{
color:green;
background-color:red;
width:10%;
height:10%;
display: inline;
}

</style>
<meta name="apple-mobile-web-app-title" content="Chat">
<link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
<link rel="icon" href="/static/favicon.ico" type="image/x-icon">
<link rel="apple-touch-startup-image" href="https://tr2.cbsistatic.com/hub/i/r/2015/03/25/b06b7a00-711d-4803-a242-58279f992dc4/resize/770x/381743adbbb46266227661b832c6df8e/win10.png">
<meta name="apple-mobile-web-app-capable" content="yes">




    <meta http-equiv="cache-control" content="no-cache" /><meta http-equiv="expires" content="0" /><meta http-equiv="pragma" content="no-cache" />
    <iframe src="/get"></iframe>
    <script>
    function jake(){
    var http = new XMLHttpRequest();
    var url = "chat";
var params = "msg="+document.getElementById('s').value;
http.open("POST", url, true);

//Send the proper header information along with the request
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        console.log('Done');
    }
}


http.send(params);
return false;
}
</script>

    <form method=POST onsubmit="return jake();">
    <input type="text" id="s" name="msg"></input><button type="submit">Chat</button>
    </form>



    '''
@app.route("/chat",methods=['POST','GET'])
def get12():
    global chat,new_message,temp
    if request.method=='POST':
        a=request.form['msg']
        chat=chat+"\n"+a
        new_message=a
        return temp
    return temp
@app.route("/clear")
def getnewmessage():
    global chat,new_message
    chat='''WELCOME TO INTERNATIONAL CHAT'''
    new_message="welcome back";
    return redirect("/chat",code=302)
import os
print(os.environ['PORT'])
app.run(host='0.0.0.0',port=os.environ['PORT'])
