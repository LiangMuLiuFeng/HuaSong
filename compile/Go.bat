@echo off
echo.
echo Run the go program
echo.
echo       — Made by : Wang Zijia
echo.
echo.
echo Please Input the name of program which you want:
set /p name=">>> "
cls
go run %name%.go
pause>nul
