# Simple Data Merger Tool
This simple tool is useful if you want to merge data which satisfy:
* Separated in some files, and have same unique identifier across the files
* Data ordering is different in every files, but you want to order it with that unique identifier
* Not have a good system to automate this process

This is an updated version from my [old project](https://github.com/prajnapras19/simple-score-merger-tool)

### Case Example
You are a teacher and you need to compile all the scoresheets of the final year student
Every year the class is shuffled, which means there exists a student assigned to the new class in the new year that different from the class he was assigned to in the previous year
But, you need to order the scores by the last updated namelist

### How to use it
Follow one of the steps you prefer below
##### Use the standalone
Go to the standalone directory (windows-standalone for windows user and linux-standalone for linux user) and download the executable file
You just need to click the app and input the port number
After that, open the browser and access ```localhost:<PORT_NUMBER>```, where ```<PORT_NUMBER>``` is the port that you input when you run the controller
The standalone version is generated using [pyInstaller](https://pypi.org/project/PyInstaller/)
##### Use python
Download or clone the repository to your machine 
Open your terminal / command prompt and go to the directory of the repository
If you have python3.x installed, you need to install the required module(s)
```
pip install -r requirements.txt
```
Then, run the app
```
python app.py
```
After that, open the browser and access ```localhost:<PORT_NUMBER>```, where ```<PORT_NUMBER>``` is the port that you input when you run the controller

