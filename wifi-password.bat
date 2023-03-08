:: SachaDee 2020

@for /f "skip=2 delims=: tokens=2" %%a in ('netsh wlan show profiles') do @for /f "tokens=2 delims=:" %%b in ('netsh wlan show profile name^=%%a key^=clear ^| findstr "Cont"') do @echo %%a =^> %%b

pause
