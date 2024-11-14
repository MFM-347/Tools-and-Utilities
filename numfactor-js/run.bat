@echo off
set /p num="Enter a Number to Factorize: "

python ren.py 
node numFactorizer.js "%num%"