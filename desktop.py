#Ayushi Patel
#Desktop Notifications

#The module notification is being imported from plyer.
from plyer import notification
 
 
title = 'Daily Reminders To Keep you on Track!!' #title of the notification

message= 'STUDY FOR MIDTERMS' + '\nDont forget to take care of yourself !!' + '\nDo More of what makes you HAPPY :)' #the body of the notification

#Telling the input what they need to print and what matters.
notification.notify(title= title, 
                    message= message, 
                    app_icon= None, 
                    timeout= 50, 
                    toast= False)