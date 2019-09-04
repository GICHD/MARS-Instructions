How to submit a bug using email
---- 
To submit a new bug, the users can email directly to the **MARS JIRA** system. __The JIRA__ will create a task and you can track it the new task and others using the JIRA dashboard with your access. Once JIRA received an email it create the task, and it will notify you by email that there is a new task created as well a link.  

This action will trigger a message to notify the MARS development project manager who will allocate resources to the new-created task.

In JIRA we can track the status of the new-created task as well all the planned/ongoing development, the bugs and any other issues. To prevent confusion, we ask all the team to follow those best practices when submitting bugs the email. 

The email address is [mars.support@jira.itransition.com][1]

Each email will contain a subject and body. 

## - The Subject:
  The email subject is translated into the header of the new issue. Make it short, clear and up to the point. Avoid the use of long text in the header.
	```
	Subject Example: Cannot synchronise report in Android
	```

## - The Body:
  This is the part of the email that you can describe in details the issue. Make sure you have the following in your body as well with the description : 

  - __Environment__ (Operating System, Browser ...):
	* Device: What type of hardware are you using? What is the specific model?
	* OS: Which version number of the OS has displayed the issue?
	* Testing App Version: Which version number of the application are you testing? Writing “latest version” or “MARS Download Version ” won’t cut it, since some bugs are version specific — make sure your testers include this information.
	* Connection type (if applicable): If the application you’re testing is reliant on Internet connectivity, are you on WiFi, Ethernet, or cellular data? What is the speed of the connection?
	* Reproducibility Rate: How many times have you been able to reproduce the error, using the exact steps you’ve taken to activate the bug? It’s also useful to report how many times I have reproduced the bug vs. the number of attempts it’s taken to reproduce the issue, in case it’s an intermittent occurrence.
  - __Steps to reproduce__: We number our steps from the beginning to the end so developers can follow through by repeating the same process. We prefer to keep step numbers relatively whittled down by using the “\>” symbol.
	  \#\#### For example:
		```
		  1. Go to Users > Profile (this would take a user to a new screen)
		  2. Tap on Profile Name > Delete User
		```
  * __Expected Result__: What is the expected outcome of your action.
  * __Actual Result__: The result of the bug that you encounter.
  * __Visual Proof__ (screen-shots, videos, text): You can attach pictures, files and videos to your email. 
	  
---- 

* Remove any auto signature in the email your name is just enough. 
* JIRA will setup emails with a priority **Major**. If you need to change login to JIRA.
* JIRA will classifies the type of the issue as **Support Case**.
* Keep it simple by avoiding complicated terms or difficult to understand for non-native English speakers.

[1]:	mailto:mars.support@jira.itransition.com