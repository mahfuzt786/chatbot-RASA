from flask import Flask
from flask import render_template,jsonify,request
import requests
from application_config import *
from response import *
import random
from flask_mysqldb import MySQL
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb
import subprocess
import sys
 
app = Flask(__name__)

mysql = MySQLdb.connect(host="localhost",  # your host 
                    user="alegra6_syed",       # username
                    passwd="smdBAlg%94z",     # password
                    db="alegra6_hdms")   # name of the database

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = "alegra6_syed"
# app.config['MYSQL_DATABASE_PASSWORD'] = 'smdBAlg%94z'
# #app.config['MYSQL_DATABASE_USER'] = 'root'
# #app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'alegra6_hdms'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# mysql = MySQL(app)

class ServiceMonitor(object):

    def __init__(self, service):
        self.service = service

    def is_active(self):
        """Return True if service is running"""
        cmd = '/bin/systemctl status %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        #print(str(proc.communicate()[0].decode("utf-8")).split('\n'))
        # stdout_list = proc.communicate()[0].split('\n')
        stdout_list = str(proc.communicate()[0].decode("utf-8")).split('\n')
        for line in stdout_list:
            if 'Active:' in line:
                if '(running)' in line:
                    return True
        return False

    def start(self):
        cmd = '/bin/systemctl start %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        proc.communicate()

        return True

    def stop(self):
        cmd = '/bin/systemctl stop %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        proc.communicate()

        return True

    def restart(self):
        cmd = '/bin/systemctl restart %s.service' % self.service
        proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
        proc.communicate()

        return True


@app.route('/')
def home_page():
    stat            = ServiceMonitor('chatflask') #subprocess.call('systemctl status chatflask', shell=True)
    statApiHttp     = ServiceMonitor('chatflaskApi') # os.system('sudo systemctl status chatflaskApi.service')
    statApiHttps    = ServiceMonitor('chatflaskApiSSL') # os.system('systemctl status chatflaskApiSSL.service > /dev/null')

    if stat.is_active():
        status = 0
    else :
        status = 768

    if statApiHttp.is_active():
        statusHttp = 0
    else :
        statusHttp = 768

    if statApiHttps.is_active():
        statusHttps = 0
    else :
        statusHttps = 768

    
    return render_template('home.html', status=status, statusHttp=statusHttp, statusHttps=statusHttps)

@app.route('/stopService',methods=["POST"])
def stopService():
    user_service    = request.form["service"]
    toStop          = ServiceMonitor(user_service)

    toStop.stop()
    
    return jsonify({"status":"success","response":'stop'})

@app.route('/startService',methods=["POST"])
def startService():
    user_service    = request.form["service"]
    toStart         = ServiceMonitor(user_service)

    toStart.start()
    
    return jsonify({"status":"success","response":'start'}) 

@app.route('/reStartService',methods=["POST"])
def reStartService():
    user_service    = request.form["service"]
    toStart         = ServiceMonitor(user_service)

    toStart.restart()
    
    return jsonify({"status":"success","response":'restart'})

get_random_response = lambda intent:random.choice(response[intent])

def get_response(intent, params=None, user_email=None, phone_number=None):
    if user_email == None or user_email == "":
        if intent == "user_email":
            if params != None and len(params) > 0:
                for p in params:
                    if p == "email_format" and params[p] != "":
                        user_email=params[p]
            if user_email == None or user_email == "":
                return_response = get_random_response("required_email")
            elif user_email !="" and phone_number == "":
                return_response = get_random_response("email_without_phone_number")
            else:
                return_response = get_random_response("email_received")
        else:
            return_response = get_random_response("required_email")
    elif phone_number == None or phone_number == "":
        if intent == "user_phone_number":
            if params != None and len(params) > 0:
                for p in params:
                    if p == "phone_number" and params[p] != "":
                        phone_number=params[p]
            if phone_number != "":
                return_response = get_random_response("phone_number_received")
            else:
                return_response = get_random_response("required_phone_number")
        else:
            return_response = get_random_response("required_phone_number")
    elif intent == "greet" or intent == "affirm" or intent == "goodbye" or intent == "fallback" or intent == "bot_name" or intent == "bot_age" or intent == "bot_status" or intent == "need_help" or intent == "your_designation" or intent == "online_status" or intent == "about_company" or intent == "company_address" or intent == "skills" or intent == "company_owner" or intent == "employee_strength" or intent == "hire_resource" or intent == "how_to_contact" or intent == "our_services" or intent == "company_business" or intent == "job_vacancies" or intent == "service_charges" or intent == "user_phone_number" or intent == "user_email" or intent == "user_annoyed" or intent == "company_name" or intent == "bot_surrender" or intent == "working_days_and_hours" or intent == "our_expertise" or intent == "platform" or intent == "development" or intent == "linux_os" or intent == "cloud_server" or intent == "microsoft_tech" or intent == "framework" or intent == "javascript" or intent == "php_framework" or intent == "python_framework" or intent == "databases" or intent == "consultancy" or intent == "full_consultancy" or intent == "deployment" or intent == "dev_platform" or intent == "version_control" or intent == "version_control_type" or intent == "used_tools" or intent == "agile_dev" or intent == "support_control" or intent == "ui_ux" or intent == "ui_ux_designer" or intent == "ui_design" or intent == "mobile_app" or intent == "custom_software" or intent == "third_party" or intent == "api_dev" or intent == "code_quality" or intent == "code_check" or intent == "linkedin" or intent == "twitter" or intent == "facebook" or intent == "train_learn" or intent == "memory_bot" or intent == "gender" or intent == "live_server" or intent == "creator" or intent == "emotions" or intent == "smile" or intent == "laugh_cry" or intent == "laugh" or intent == "angry_sad" or intent == "feel_sad" or intent == "get_angry" or intent == "happy" or intent == "introvert" or intent == "arrogant" or intent == "strong" or intent == "weak" or intent == "play" or intent == "play_me" or intent == "entertain" or intent == "sing" or intent == "appointment":
        return_response = get_random_response(intent)
    elif intent == "specific_office_address":
        office_location=""
        if params != None and len(params) > 0:
            for p in params:
                if p == "office_location" and params[p] != "":
                    office_location=params[p]
        if office_location != "":
            office_location = office_location.lower()
            if office_location == "germany" or office_location == "berlin":
                 return_response = get_random_response("company_address")
            elif office_location == "uk" or office_location == "bath" or office_location == "united kingdom":
                return_response = get_random_response("company_address")
            elif office_location == "india" or office_location == "guwahati":
                return_response = get_random_response("company_address")
            else:
                return_response = "Sorry! we don't have any office in your provide location"
        else:
            return_response = "I am sorry! I don't have this specific information"           
    else:
        return_response = "Sorry! I am just a bot, I am not able to answer this I need to talk to my developer to make me understand this. I will be pleased if I can help you with anything else that you want to know"
    return return_response, user_email, phone_number

def mailChat(user_email, data):
    # me == my email address
    # you == recipient's email address
    me = "jay3000bc@outlook.in"
    you = user_email

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Chat Transcript"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = data
    html = data

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.live.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('jay3000bc@outlook.in', 'cactus57')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

@app.route('/chat',methods=["POST"])
def chat():
    try:
        response = requests.get("http://alegralabs.com:5000/parse", params={"q":request.form["text"]})
        # response = requests.get("http://127.0.0.1:5000/parse", params={"q":request.form["text"]})
        response = response.json()
        if response["intent"]["confidence"] >= 0.6: #earlier 0.89
            intent = response["intent"]["name"]
        else:
            intent = "fallback"
        entities = response["entities"]
        # Initialize params dictionary
        params = {}
        # Fill the dictionary with entities
        for ent in entities:
            params[ent["entity"]] = str(ent["value"])

        user_email=request.form["usr_email"]
        phone_number=request.form["usr_phone_number"]
        response_text, user_email, phone_number=get_response(intent,params,user_email,phone_number)
        
        dbInsert = '<span style="font-size:1.7em;">[</span> <span style="color: red; font-size:1.4em;">user</span>: '+ request.form["text"] +'<br/> <span style="color: red; font-size:1.4em;">bot</span>: ' +response_text+ '<span style="font-size:1.7em;">]</span> <br/><br/>'

        cur = mysql.cursor()
        cur.execute("SELECT email, phone_number FROM alegra6_hdms.chatbots WHERE email LIKE %s AND phone_number LIKE %s", (user_email, phone_number))
        data = cur.fetchall()
        
        if len(data) is 0 :
            cur.execute("INSERT INTO alegra6_hdms.chatbots(email, chats, phone_number) VALUES (%s, %s, %s)", (user_email, dbInsert, phone_number))
        else :
            cur.execute("UPDATE alegra6_hdms.chatbots SET chats = CONCAT(chats, %s) WHERE email LIKE %s AND phone_number LIKE %s", (dbInsert, user_email, phone_number))
        mysql.commit()
        cur.close()

        return jsonify({"status":"success","response":response_text,"user_email":user_email,"phone_number":phone_number})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response": "Sorry! I am just a bot, my application server may be down, can't help you at the moment! I am heartly sorry for the inconvenience :(","user_email":"","phone_number":""})


@app.route('/mail',methods=["POST"])
def mail():
    try:
        user_email=request.form["usr_email"]
        phone_number=request.form["usr_phone_number"]

        cur = mysql.cursor()
        cur.execute("SELECT chats FROM alegra6_hdms.chatbots WHERE email LIKE %s AND phone_number LIKE %s", (user_email, phone_number))
        data = cur.fetchall()
        #data = cur.fetchone()
 
        if len(data) is 0 :
            response_text = 'There is no data to mail'
        else :
            response_text = 'Mailed Successfully'
            for row in data:
                for rows in row:
                    rows = str(rows.decode("utf-8"))
                    #mail the chat
                    mailChat(user_email, rows)

            #print(data)

        mysql.commit()
        cur.close()

        return jsonify({"status":"success","response":response_text,"user_email":user_email,"phone_number":phone_number})
    except Exception as e:
        print(e)
        return jsonify({"status":"fail","response": "Sorry! my application server may be down, can't mail at the moment! :(","user_email":"","phone_number":""})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8891, host='0.0.0.0')
