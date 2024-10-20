@echo off
:menu
echo ================================
echo Please choose an option:
echo ================================
echo 1. Run 'py manigen.py init'
echo 2. Run 'py manigen.py template'
echo 3. Exit
echo ================================
set /p choice=Enter your choice (1, 2, or 3): 

if "%choice%"=="1" goto init
if "%choice%"=="2" goto template
if "%choice%"=="3" goto end
echo Invalid option. Please try again.
goto menu

:init
echo Running 'py manigen.py init'...
py manigen.py init
goto menu

:template
echo Running 'py manigen.py template'...
py manigen.py template
goto menu

:end
echo Exiting...
exit