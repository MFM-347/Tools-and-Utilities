@echo off
set /p directory="Enter the directory path: "
set /p base_name="Enter the base name: "

python ren.py "%directory%" "%base_name%"