#pre release material
##task1
1.1
To set up a structure based on the structure of the data with elementary components and composite components for the program to handle.
1.2
star:repetition
circle:to choose one
1.3
While 
>CALL ReadSalary()
>>IF Salary>50:
>>>THEN
>>>>IF Salary>=90
>>>>>Then
>>>>>>Role-Project Manager
              
>>>>>Else
>>>>>>Role-Lead Developer
       
>>>ENDIF

>>ELSE
>>>Role-Manager

>ENDIF

ENDWHILE
1.4
see the image in the same folder
1.5
While 
>CALL ReadSalary()
>>IF Salary>50:
>>>THEN
>>>>IF Salary>90
>>>>>THEN
>>>>>>Role<-Project Manager
              
>>>>>Else
>>>>>>IF Salary>=70
>>>>>>>THEN 
>>>>>>>>Role<-Consultant

>>>>>>>ELSE
>>>>>>>>Role<-lead developer

>>>>>>ENDIF    

>>>>>ENDIF   

>>>ENDIF

>>ELSE
>>>Role-Manager

>ENDIF

ENDWHILE

1.6
def Role(s):
>if s<50:
>>return (“manager”)

>if s>=90:>>return (“Project Manager”)    
>if s<70:>>return (“Consultant”)    
>else:>>return (“Lead Developer”)

