class Person:
    def __init__(self, personId):
        self.personId = personId
        self.scores = dict()
    
    def getPersonId(self):
        return self.personId
        
    def setPersonId(self, personId):
        self.personId = personId
        
    def getScores(self, course):
        try:
            return self.scores[course]
        except KeyError:
            return '-'
    
    def setScores(self, course, score):
        self.scores[course] = score

    def __str__(self):
        return self.personId
    
class PersonCollection:
    def __init__(self):
        self.persons = list()
        self.courses = set()
        self.courseToPerson = dict()
        
    def addPerson(self, person):
        self.persons.append(person)
    
    def getPersonById(self, personId):
        for person in self.persons:
            if (person.getPersonId() == personId):
                return person
        return False
    
    def deletePersonById(self, personId):
        self.persons.remove(self.getPersonById(personId))
    
    def addCourses(self, course):
        self.courses.add(course)
    
    def getCourses(self):
        return self.courses
    
    def addCourseToPerson(self, course, person):
        try:
            tmp = self.courseToPerson[course]
        except KeyError:
            self.courseToPerson[course] = set()
        self.courseToPerson[course].add(person)
    
    def deleteCourseToPerson(self, personId):
        person = self.getPersonById(personId)
        for course in self.courses.copy():
            self.courseToPerson[course].discard(person)
            if (len(self.courseToPerson[course]) == 0):
                self.courseToPerson.pop(course)
                self.courses.discard(course)
                
    def asList(self):
        return self.persons
        
    def asListWithSelectedId(self, selectedId=[]):
        tmp = list()
        for personId in selectedId:
            person = self.getPersonById(personId)
            if (person):
                tmp.append(person)
        return tmp
    
    def __str__(self):
        return ', '.join(persons)
        
def validateCSV(f):
    csv = f
    csv.seek(0)
    length = 0
    cnt = 0
    for row in csv:
        cnt += 1
        row = row.decode("utf-8")
        tmp = len(row.strip('\n').strip('\r').split(','))
        if (cnt == 1):
            length = tmp
        else:
            if (length != tmp):
                return False
    return ((cnt > 0) and (length > 0))
    
def parseCSVToPerson(f, personCollection):
    csv = f
    csv.seek(0)
    persons = list()
    header = list()
    cnt = 0
    length = 0
    for row in csv:
        cnt += 1
        row = row.decode("utf-8")
        line = row.strip('\n').strip('\r').split(',')
        if (cnt == 1):
            header = line
            length = len(line)
            for course in header[1:]:
                personCollection.addCourses(course)
        else:
            personId = line[0]
            newPerson = personCollection.getPersonById(personId)
            if not(newPerson):
                newPerson = Person(personId)
                persons.append(newPerson)
            for i in range(1, length):
                newPerson.setScores(header[i], line[i])
                personCollection.addCourseToPerson(header[i], newPerson)
    return persons

def parseCSVToList(f):
    csv = f
    csv.seek(0)
    tmp = list()
    for row in csv:
        row = row.decode("utf-8")
        tmp.append(row.strip('\n').strip('\r'))
    return tmp
