@echo on &setlocal
tasklist /v /fi "STATUS eq running" /fi "imagename ne cmd.exe" /fi "imagename ne conhost.exe" /fo list | find "PID:">tmp.txt
