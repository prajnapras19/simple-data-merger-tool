# Simple Data Merger Tool
This simple tool is useful if you want to merge data which satisfy:
* Separated in some files, and have same unique identifier across the files
* Data ordering is different in every files, but you want to order it with that unique identifier
* Not have a good system to automate this process

This is an updated version from my [old project](https://github.com/prajnapras19/simple-score-merger-tool)<br>

### Case Example
You are a teacher and you need to compile all the scoresheets of the final year student<br>
Every year the class is shuffled, which means there exists a student assigned to the new class in the new year that different from the class he was assigned to in the previous year<br>
But, you need to order the scores by the last updated namelist<br>

### How to use it
Follow one of the steps you prefer below<br>
##### Use the standalone
Go to the standalone directory (windows-standalone for windows user and linux-standalone for linux user) and download the executable file<br>
You just need to click the app and input the port number<br>
After that, open the browser and access ```localhost:<PORT_NUMBER>```, where ```<PORT_NUMBER>``` is the port that you input when you run the app<br>
The standalone version is generated using [pyInstaller](https://pypi.org/project/PyInstaller/)<br>
##### Use python
Download or clone the repository to your machine<br>
Open your terminal / command prompt and go to the directory of the repository<br>
If you have python3.x installed, you need to install the required module(s)<br>
```
pip install -r requirements.txt
```
Then, run the app<br>
```
python app.py
```
After that, open the browser and access ```localhost:<PORT_NUMBER>```, where ```<PORT_NUMBER>``` is the port that you input when you run the controller<br>
