# Discord-Bot
Heroku ready
## **Features:**
1.  **Basic**
  	* Ping - Ping Bot
2.  **Fun**
  	* Cat - Return Random Cat Picture
  	* Dog - Return Random Dog Picture
  	* Comeback {TargetUser} - Return Random Comeback
  	* Inspire - Return Inspirational Qoute
3.  **Uncategorised**
  	* New Member Welcome Message
4.  **Admin**
  	* Q - Stop Bot

## Install Dependencies:
###### **Conda**:
```
conda create --name <env> --file condarequirements.txt
```
or
###### **Pip**:
```
python3 -m venv env
source env/bin/activate
pip install -r piprequirements.txt
```

## Create Enviroment:
###### **Conda**:
```
conda create --name <env> --file requirements.txt python=3.8.2 
```
or
###### **Pip**:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Create .env File:
Create a .env file in the main directory, add your discord bots token. eg.
```
DiscordBotToken="Y4Y8Ya9GhML8jbtf4RsQ4Gifs.BeebX7Y5RJlv3cV6jasSzParbZiiL0x9Qj"
```

## Initial Setup:
Have bot.py running while you invite the bot to your server/s the first time you connect

## Customization:
Currently to change permissions you use the config .ini, each section is titled with the server id. Each command has what the command does and the current role that has permissions to use it, by default most commands are set to @everyone except admin commands which are set to @Admin

