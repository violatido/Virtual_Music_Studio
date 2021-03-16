

# **Virtual Music Studio**
### Created by Ilana Rose Mercer

*Virtual Music Studio* is an organizational web app for private music teachers that allows them to keep track of all their students in one space. 

[*Demo Video*](https://www.youtube.com/watch?v=l1CXHxR0d8k)


## **Stack**
**Front-end**: JavaScript (AJAX, JSON), CSS, HTML </br>
**Back-end**: Python, Flask, Jinja, SQLAlchemy, PostgreSQL </br>
**Libraries/APIs**: Chart.js, Moment.js, Twilio SMS API


## **Features**


* Using Charts.js, students can log their practice sessions and view three different charts that analyze their practice data in terms of frequency and length of session. 

![](static/img/readme-media/charts-giphy.gif)

* The Twilio SMS API allows teachers to quickly send important updates and reminders straight to a student's phone without sharing their own personal contact information. 

![](static/img/readme-media/twilio-giphy.gif)

## **Setup/Installation**

#### **Clone this repository**
```bash
git clone https://github.com/violatido/Virtual_Music_Studio.git
```
#### **Create a virtual environment**
``` bash
virtualenv env
```
#### **Activate the virtual environment**
``` bash
source env/bin/activate 
```
#### **Install the requirements**
```bash
pip3 install -r requirements.txt
```


## **Usage**

### **If using the Twilio SMS API feature:**
1. After installation, visit the [Twilio SMS API docs](https://www.twilio.com/docs/sms/api) to set up your account 
2. Create a file called secrets.sh
3. In secrets.sh, set an export variable for your Account SID, Auth Token, and Twilio phone number. These items will be needed in the "send_message" function declared in line 365 of [server.py](https://github.com/violatido/Virtual_Music_Studio/blob/69b6be5885f11f3f7f6e6eec5cda15a789e6785e/server.py#L365)
```bash 
export ACCOUNT_SID = ''
export AUTH_TOKEN = ''
export TWILIO_PHONE = ''
```
4. Run in the terminal: source secrets.sh


## **About the developer ...**
Ilana Rose Mercer is a software engineer finishing her fellowship at Hackbright Academy. Before she learned how to code and became passionate about growing my career in tech, Ilana worked as a professional classical musician and private music teacher. This project is very personal to her because it is a beautiful joining of her past and present careers, and a product that she would have used daily during my private music teaching years. 

Feel free to connect with Ilana here on Github and on [LinkedIn](https://www.linkedin.com/in/i-mercer/)

![VMS logo](static/img/Light-logo-cutout.png)