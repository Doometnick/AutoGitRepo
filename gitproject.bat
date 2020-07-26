@echo off
Call :createproject %~1
EXIT /B %ERRORLEVEL%

:createproject
SET BASE_FOLDER="C:\Users\brand\Documents\MyProjects\"
SET PROJECT_NAME=%BASE_FOLDER%%~1
SET GIT_CONNECT_SCRIPT="C:/BAT/github_connect.py"
SET GITHUB_USER_DOMAIN="https://github.com/Doometnick/"
SET PYTHON_EXE="C:\Users\brand\Miniconda3\python.exe"

IF EXIST %PROJECT_NAME% (
	echo Folder already exists.
) ELSE (

cd /d BASE_FOLDER
md %~1
cd %~1
git init .
git commit -m "initial commit"
%PYTHON_EXE% %GIT_CONNECT_SCRIPT% %~1
git remote add origin %GITHUB_USER_DOMAIN%%~1.git
git remote -v
echo.>>"README.md"
git add "README.md"
git commit -m "Added readme"
git push --set-upstream origin master
git push origin master

)

EXIT /B 0
