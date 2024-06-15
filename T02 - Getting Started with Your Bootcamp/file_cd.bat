:: hyperiondev - Software Engineering Fundamentals
:: Task 2 - Getting Started with Your Bootcamp - Practical Task 1 - "file_cd.bat"
:: Author: Helder P - HP24010013265
:: Date: 12/03/2024


rem Disables the command echoing feature so that commands are not displayed in the console as they are executed.
@echo off
"C:\Users\helde\AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\helde\OneDrive\Documents\Software Dev\SessionWorkSpace\file_cd.bat"


rem The next few lines will create three new folders.
mkdir folder1
mkdir folder2
mkdir folder3

rem Navigating into one of the folders and creating three new folders inside it
cd folder1
mkdir subfolder1
mkdir subfolder2
mkdir subfolder3

rem Removing two folders and all its contents (/s flag) without asking for confirmation (/q flag)
rmdir /s /q subfolder2
rmdir /s /q subfolder3

rem Navigating back to the parent directory
cd ..