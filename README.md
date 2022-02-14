# VAKSH-DOC (DETECTION OF CANCER)
Vaksh(वक्ष्ः) Is sanskrit Name of Breast.  
Breast Cancer Detection App Using Microsoft Azure and ML. <br>
<br>

## Setup Environment and Run App Locally  

### *Note: Make sure, you have Python 3 installed. (preferebly 3.9)*  

In Windows Powershell:
```
> python -m venv venv
> Set-ExecutionPolicy Unrestricted -Scope Process
> venv\scripts\activate
```
`Set-ExecutionPolicy` command will give unrestricted aceess to current process, so it will let you run activate script.   

Or In Linux/Mac:
```
$ python3 -m venv venv
$ . venv/bin/activate
```
3. Now, install requirements with this command:
```
pip install -r requirements.txt
```
4. Now run the application using below command:
```
flask run
```
After running, You can access this app on http://127.0.0.1:5000