

# Virtual Music Studio
### Created by Ilana Rose Mercer

*Virtual Music Studio* is an organizational web app for private music teachers that allows them to keep track of all their students in one space. 


![](static/img/readme-media/chart-gif.gif)

### Stack
Front-end: JavaScript (AJAX, JSON), CSS, HTML </br>
Back-end: Python, Flask, Jinja, SQLAlchemy, PostgreSQL </br>
Libraries/APIs: Chart.js, Twilio SMS API

## Setup/Installation

#### Requirements
* Python 3.8.3
* PostgreSQL

#### Clone this repository
```bash
git clone https://github.com/violatido/Virtual_Music_Studio.git
```
#### Create a virtual environment
``` bash
virtualenv env
```
#### Activate the virtual environment 
``` bash
source env/bin/activate 
```
#### Install the requirements 
```bash
pip3 install -r requirements.txt
```


## Usage

### If using the Twilio SMS API feature:
1. After installation, visit the [Twilio SMS API docs](https://www.twilio.com/docs/sms/api) to set up your account 
2. Create a file called secrets.sh
3. In secrets.sh, set an export variable for your Account SID, Auth Token, and Twilio phone number (these items will be needed in the "send_message" function declared in line 366 of server.py)
4. Run in the command line: source secrets.sh

![GitHub Logo](/static/img/secrets-readme-img.png)


## About the developer ...
Ilana Rose Mercer is a software engineer finishing her fellowship at Hackbright Academy. Her previous career as a performing classical musician and private music teacher inspired this project, designing this web app with her past experiences in mind. 

Feel free to connect with Ilana here on Github and on [LinkedIn](https://www.linkedin.com/in/i-mercer/)