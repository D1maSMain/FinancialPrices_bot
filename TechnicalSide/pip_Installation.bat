@echo off
python -m pip install --upgrade pip
set libraries[0]=aiogram
set libraries[1]=asyncio
set libraries[2]=regex
set libraries[3]=email
set libraries[4]=smtplib
set libraries[5]=bs4
set libraries[6]=os
set libraries[7]=requests
set libraries[8]=matplotlib
set libraries[9]=mpl_finance
set libraries[10]=pandas
set libraries[11]=fake-useragent
set libraries[12]=wheel
set lib = null


FOR %%i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) do (
	call pip install %%libraries[%%i]%%
)
	
nhcolor 0a Ready
PAUSE