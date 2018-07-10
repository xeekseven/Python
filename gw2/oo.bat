@echo off

@echo 100 > oo.txt
for /l %%i in (1,1,3) do (
 
 python oo.py < oo2.txt
 ping -n 2 127.0.0.1>nul
)

set /p opone=<oo.txt
if %opone% == 101 exit

::ping -n 1800 127.0.0.1>nul

@echo 200 > oo.txt
for /l %%i in (1,1,6) do (

 python oo.py < oo2.txt
 ping -n 6 127.0.0.1>nul
)

set /p optwo=<oo.txt
if %optwo% == 201 exit

::ping -n 2700 127.0.0.1>nul
@echo 300 > oo.txt
for /l %%i in (1,1,6) do (
 
 python oo.py < oo2.txt
 ping -n 6 127.0.0.1>nul
)
@echo 100>oo.txt