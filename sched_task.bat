echo off && setlocal
schtasks /create /sc once /ri 1 /tn kaboom /tr main_source.bat /st %time:~0,5% /f