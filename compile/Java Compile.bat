@echo off
echo.
echo Compile the Java Program
echo.
echo       — Made by : Wang Zijia
echo.
echo.
echo Please Input name of program which you want:
set /p name=">>> "
echo.
javac %name%.java
echo The %name% has already compiled
echo.
echo Thanks for using
pause>nul
