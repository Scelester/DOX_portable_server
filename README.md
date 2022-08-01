## DAOX_portable_server

portable server you can carry on your usb/pendrive [based on xampp].

# How to run 
  * Extract zip file in you pendrive on toplevel e.g. D:/,E:/,.. etc.
  * Run runme.bat  to start the server.
  * It will show you your local IP address where your server will be hosted.
  * This will start apache server. You should see "apache is starting" message.
  * Don't close the CMD window or the Apache server will stop running.


# More info
Only works for windows machine for now.
The server uses Django framework which is located inside hung_collection folder. 
This Django framework runs on the apache web server located inside xampp folder.
mod-wsgi python framework is used for connecting apache and django (wsgi.py).
sometimes the server will fail to load the website that means the apache server
Is not running properly. So you have to close the runme.bat window and start again.


# Creating your own application.
Go inside the hung_application folder i.e. django-folder, then go inside temp_app to
change or add html files. Or you can create your new own apps inside hung_application folder 
yourself. 
