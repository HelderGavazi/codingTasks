:: hyperiondev - Software Engineering Fundamentals
:: Task 2 - Getting Started with Your Bootcamp - Practical Task 1 - "ifExample.bat"
:: Author: Helder P - HP24010013265
:: Date: 12/03/2024


@echo off
"C:\Users\helde\AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\helde\OneDrive\Documents\Software Dev\SessionWorkSpace\ifExample.bat"

rem Checking if the folder 'new_folder' exists
if exist new_folder (
    rem Creating a new folder called 'if_folder'
    mkdir if_folder
) else (
    rem Otherwise create a new folder called 'new-projects'
    mkdir new-projects
)

rem Checking if the folder 'if_folder' exists
if exist if_folder (
    rem Creating a new folder called 'hyperionDev'
    mkdir hyperionDev
) else (
    rem Creating a new folder called 'new-projects' if 'if_folder' does not exist
    mkdir new-projects
)

rem Navigating back to the parent directory
cd ..
