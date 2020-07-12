from flask import Flask, request, render_template, send_from_directory
from model import Person, PersonCollection, validateCSV, parseCSVToPerson, parseCSVToList
from werkzeug.utils import secure_filename
import os
import sys

# The line below is for make the standalone using pyinstaler
# references: https://github.com/ciscomonkey/flask-pyinstaller
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    template_folder = os.path.join(os.getcwd(), 'templates')
    static_folder = os.path.join(os.getcwd(), 'static')
    app = Flask(__name__)

ALLOWED_EXTENSIONS = ['csv']
persons = PersonCollection()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if (request.method == 'GET'):
        return render_template('add.html')
    else:
        message = "Cannot process data. Try again."
        try:
            f = request.files['file']
            if (allowed_file(secure_filename(f.filename)) and validateCSV(f)):
                newPersons = parseCSVToPerson(f, persons)
                for newPerson in newPersons:
                    persons.addPerson(newPerson)
                message = "Data added successfully."
        except:
            pass
        return render_template('add.html', message=message)
        
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'GET'):
        personsList = persons.asList()
        return render_template('delete.html',persons=personsList, courses=persons.getCourses(), available=len(personsList))
    else:
        checkbox = request.form.getlist('checked')
        for checked in checkbox:
            persons.deleteCourseToPerson(checked)
            persons.deletePersonById(checked)
        personsList = persons.asList()
        return render_template('delete.html',persons=personsList, courses=persons.getCourses(), available=len(personsList))
        
@app.route('/show', methods=['GET', 'POST'])
def show():
    if (request.method == 'GET'):
        personsList = persons.asList()
        return render_template('show.html', persons=personsList, courses=persons.getCourses(), available=len(personsList))
    else:
        selectedIdList = list()
        try:
            f = request.files['file']
            if (allowed_file(secure_filename(f.filename)) and validateCSV(f)):
                selectedIdList = parseCSVToList(f)
        except:
            pass
        personsList = persons.asListWithSelectedId(selectedIdList)
        selectColumn = request.form.getlist('selectColumn')
        if (len(selectColumn) == 0):
            selectColumn = persons.getCourses()
        return render_template('show.html', persons=personsList, courses=selectColumn, available=len(personsList))
    
@app.route('/download/<filename>')
def download(filename):
    directory = app.static_folder
    filename += '.csv'
    filename = secure_filename(filename)
    return send_from_directory(directory=directory, filename=filename)

# run main app
if __name__ == '__main__':
    try:
        while True:
            port = input('Input the port number and click Enter, leave it blank to use the default (5000): ')
            if (port == ''):
                port = 5000
                break
            try:
                port = int(port)
                break 
            except ValueError:
                print('Invalid port! Try again')
        app.run(host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        exit()
