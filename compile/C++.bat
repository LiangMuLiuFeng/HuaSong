@echo off
echo.
echo Run the C++ Program
echo.
echo       — Made by : Wang Zijia
echo.
echo.
echo Please Input name of program which you want:
set /p name=">>> "
cls
g++ %name%.cpp
pause>nul
