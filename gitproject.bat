@echo off
Call :createproject %~1
EXIT /B %ERRORLEVEL%

:createproject
SET foldername="C:\Users\brand\Documents\MyProjects\%~1"

IF EXIST %foldername% (
	echo Folder already exists.
) ELSE (

cd /d "C:\Users\brand\Documents\MyProjects"
md %~1
cd %~1
git init .
git commit -m "initial commit"
C:\Users\brand\Miniconda3\python.exe "C:/BAT/github_connect.py" %~1
git remote add origin https://github.com/Doometnick/%~1.git
git remote -v
echo.>"README.md"
git add "README.md"
git commit -m "Added readme"
git push --set-upstream origin master
git push origin master

)

EXIT /B 0
