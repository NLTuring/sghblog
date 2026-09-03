@echo off
chcp 65001 >nul 2>&1
title SchoolHall 博客

set "PYTHON=D:\utils\Python\python.exe"
if not exist "%PYTHON%" (
    echo [错误] 找不到 Python: %PYTHON%
    echo 请修改本文件中的 PYTHON 路径。
    pause
    exit /b 1
)

echo ========================================
echo    SchoolHall 博客 - 开发服务器
echo ========================================
echo 地址: http://127.0.0.1:8000
echo 按 Ctrl+C 停止
echo.

start "" cmd /c "timeout /t 1500 /nobreak >nul & start http://127.0.0.1:8000"

"%PYTHON%" manage.py runserver

pause
