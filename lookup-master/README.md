# Lookup master

## Installation

1.  Clone or download the repository
```PS
git clone https://github.com/eldoniis/Toolsuite4Emails
```
2. Run the setup script on powershell
```PS
.\setup.ps1
```
Linux
```sh
.\setup.sh
```
## PS
If you are on Windows probably may see a similar error like the following:
```PS
.\xyxy.py : File C:\Users\xxxx\yyyyy\xyxy.py cannot be loaded because running scripts is
disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
```
For fixing it just run the following command on PowerShell.
```PS
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
This will allow script execution for the current session, meaning that everytime you close the terminal must run again the command if want to execute again the tool.

## Usage
Run on command line
```PS
python main.py
```
Open browser on: http://127.0.0.1:5000/