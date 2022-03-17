# Django-Discord 
Discord Bot controllable from django website with oauth2   
[Demo (Takes 30 sec to start)](https://hazzahsbot.herokuapp.com/) 

## **Bot Features:**
1.  **Basic**
  	* Ping - Ping Bot
2.  **Fun**
  	* Cat - Return Random Cat Picture
  	* Dog - Return Random Dog Picture
  	* Comeback {TargetUser} - Return Random Comeback
  	* Inspire - Return Inspirational Qoute
3.  **Uncategorised**
  	* New Member Welcome Message

## Setup:
1. Create [Discord Bot](https://discord.com/developers/docs/intro) Application
1. Within OAuth2 tab add redirect url eg. https://hazzahsbot.herokuapp.com/oauth2/login/redirect 
1. Fork repo
1. Create [Heroku App](https://www.heroku.com/)
1. In settings tab add the following config vars:
	* DISABLE_COLLECTSTATIC = 1
	* DiscordBotToken = (Discord Bot Token)
	* SECRET_KEY = (Random Security key for django)
	* CLIENT_ID = discord bot client id
	* CLIENT_SECRET = discord bot client secret
	* DOMAIN = Domain to use eg. hazzahsbot.herokuapp.com
1. In deploy tab select connect to github and select repo
1. At bottom of deploy tab select Deploy Branch
1. In top right heroku click more > run console then 'python manage.py migrate'
1. At bottom of deploy tab select Deploy Branch
1. In the resource tab of heroku, switch on 'worker python bot.py'
  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)