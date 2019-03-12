
# it3038c-scripts

## LAB 7 Example

This is a Python script which uses a plugin called numpy.First,Lets create a Virtual ENV called scripts.
   
   virtualenv /venv/numpy
   source /venv/scripts/activate
   pip install numpy
   
You can type python and then type 
   >>> import numpy as np
   >>> numarray =np.arange(20).reshape(4,5)
   >>> numarray
   
This will display the array based on above variable numarray.

You can run sereval commands to show the size,shape,the type of elements in the array. 

   numarray.size
   numarray.shape
   numarray.dtype.name
   
   
   

## Project 1

### Script Name
 project1LogFiles.ps1
 
## About

The script is a powershell script,used for getting system error log files from the event log.
The error logs are then saved into a txt file on the computer "C:\" drive and sent as an attachment through email.

## Documentation
1. Download the Project 1 file.
2. Open the Powershell ISE as Administrator
3. Open the project 1 file in the Powershell ISE.
4. Change the receivers email address.
5. Save the script.
6. Click on the run button.
7. Enter email and password. 
8. The email receiver should get an attachement with the system error logfiles.

## Links
[Project 1](https://github.uc.edu/patelm7/it3038c-scripts/blob/master/powershell/Project1LogFiles.ps1)


