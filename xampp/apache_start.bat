@echo off
cd /D %~dp0
echo Please close this command only for Shutdown
echo Apache 2 is starting ...

apache\bin\httpd.exe

if errorlevel 255 goto finish
if errorlevel 1 goto error
goto finish

:error
echo.
echo Apache could not be started
pause

:finish
