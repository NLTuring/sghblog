@echo off
chcp 65001 >nul 2>&1
title 初始化博客数据

set "PYTHON=D:\utils\Python\python.exe"
if not exist "%PYTHON%" (
    echo [错误] 找不到 Python: %PYTHON%
    pause
    exit /b 1
)

echo.
echo 正在初始化博客数据...
echo.

"%PYTHON%" manage.py init_sample_data

echo.
pause
