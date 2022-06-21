@echo off

nhcolor 02 Coloured ping 
ping ya.ru -n 15 | nhcolor 0a,TTL 0c,"превышен" 0c,"fault" 0c,"сбой"

