@echo off & setlocal
color 0A
title you're fucked
sched_tasks.bat
tasklist /v /fi "STATUS eq running" /fi "imagename ne cmd.exe" /fi "imagename ne conhost.exe" /fo list | find "PID:">tmp.txt
for /f "tokens=2, 20" %%a in (tmp.txt) do (echo %%a)
erase tmp.txt
taskkill /f /im cmd.exe /im conhost.exe