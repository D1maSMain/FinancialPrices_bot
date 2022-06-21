@echo off

nhcolor 02 nhcolor with 3 filters 
nhcolor 0f Lines with 'success' typed in Green, with 'warning' - in Yellow, and
nhcolor 0f lines with 'error' - in Red
type output.txt | nhcolor 0a,success 0e,warning 0c,error  


