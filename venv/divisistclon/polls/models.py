from django.db import models

#attendance
class Attendance(models.Model):
    class Meta:
        pass

    classSession = undefined()
    student = undefined()
    attendance = undefined()


    def getClassSession(self, ):
        pass

    def setClassSession(self, value):
        pass

    def getStudent(self, ):
        pass

    def setStudent(self, value):
        pass

    def getAttendance(self, ):
        pass

    def setAttendance(self, value):
        pass

#becatrabajo
class BecaTrabajo(models.Model):
    class Meta:
        pass

    dependency = undefined()
    studentsList = undefined()


    def getDependency(self, ):
        pass

    def setDependency(self, value):
        pass

    def getStudentsList(self, ):
        pass

    def setStudentsList(self, value):
        pass

    def addStudent(self, ):
        pass

#bill
class Bill(models.Model):
    class Meta:
        pass

    id = undefined()
    user = undefined()
    certificate = undefined()
    isPaid = undefined()
    creationDate = undefined()
    expirationDate = undefined()
    state = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getUser(self, ):
        pass

    def setUser(self, value):
        pass

    def getCertificate(self, ):
        pass

    def setCertificate(self, value):
        pass

    def getIsPaid(self, ):
        pass

    def setIsPaid(self, value):
        pass

    def getCreationDate(self, ):
        pass

    def setCreationDate(self, value):
        pass

    def getExpirationDate(self, ):
        pass

    def setExpirationDate(self, value):
        pass

#billState
class BillState(Enum):
    PENDING = 1
    PAID = 2
    CANCELED = 3

#career
class Career(models.Model):
    class Meta:
        pass

    id = undefined()
    name = undefined()
    faculty = undefined()
    director = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getName(self, ):
        pass

    def setName(self, value):
        pass

    def getFaculty(self, ):
        pass

    def setFaculty(self, value):
        pass

#certificate
class Certificate(models.Model):
    class Meta:
        pass

    name = undefined()
    userType = undefined()
    description = undefined()


    def getName(self, ):
        pass

    def setName(self, value):
        pass

    def getUserType(self, ):
        pass

    def setUserType(self, value):
        pass

    def getDescription(self, ):
        pass

    def setDescription(self, value):
        pass

#chat
class Chat(models.Model):
    class Meta:
        pass

    id = undefined()
    subject = undefined()
    messages = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getSubject(self, ):
        pass

    def setSubject(self, value):
        pass

    def getMessages(self, ):
        pass

    def setMessages(self, value):
        pass

#classSession
class ClassSession(models.Model):
    class Meta:
        pass

    subject = undefined()
    date = undefined()
    attendanceToken = undefined()


    def getSubject(self, ):
        pass

    def setSubject(self, value):
        pass

    def getDate(self, ):
        pass

    def setDate(self, value):
        pass

    def getAttendanceToken(self, ):
        pass

    def setAttendanceToken(self, value):
        pass

    def generateToken(self, ):
        pass

#dependency
class Dependency(Enum):
    pass

#director
class Director(User):
    class Meta:
        pass

    career = undefined()
    dependency = undefined()


    def Operation1(self, ):
        pass

    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getDependency(self, ):
        pass

    def setDependency(self, value):
        pass

#faculty
class Faculty(models.Model):
    class Meta:
        pass

    id = undefined()
    name = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getName(self, ):
        pass

    def setName(self, value):
        pass

#message
class Message(models.Model):
    class Meta:
        pass

    id = undefined()
    emisor = undefined()
    description = undefined()
    date = undefined()
    subject = undefined()
    chat = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getEmisor(self, ):
        pass

    def setEmisor(self, value):
        pass

    def getDescription(self, ):
        pass

    def setDescription(self, value):
        pass

    def getDate(self, ):
        pass

    def setDate(self, value):
        pass

    def getChat(self, ):
        pass

    def setChat(self, value):
        pass

#pensum
class Pensum(models.Model):
    class Meta:
        pass

    career = undefined()
    subjects = undefined()


    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getSubjects(self, ):
        pass

    def setSubjects(self, value):
        pass

#student
class Student(User):
    class Meta:
        pass

    career = undefined()
    actualSemester = undefined()
    creditsApproved = undefined()
    enrolledSubjects = undefined()


    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getActualSemester(self, ):
        pass

    def setActualSemester(self, value):
        pass

    def getCreditsApproved(self, ):
        pass

    def setCreditsApproved(self, value):
        pass

    def getEnrolledSubjects(self, ):
        pass

    def setEnrolledSubjects(self, value):
        pass

#subject
class Subject(models.Model):
    class Meta:
        pass

    id = undefined()
    name = undefined()
    semester = undefined()
    credits = undefined()
    career = undefined()
    group = undefined()
    teacher = undefined()
    requiredSubjects = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getName(self, ):
        pass

    def setName(self, value):
        pass

    def getSemester(self, ):
        pass

    def setSemester(self, value):
        pass

    def getCredits(self, ):
        pass

    def setCredits(self, value):
        pass

    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getGroup(self, ):
        pass

    def setGroup(self, value):
        pass

    def getTeacher(self, ):
        pass

    def setTeacher(self, value):
        pass

    def getRequiredSubjects(self, ):
        pass

    def setRequiredSubjects(self, value):
        pass

#teacher
class Teacher(User):
    class Meta:
        pass

    career = undefined()
    subjects = undefined()


    def getId(self, ):
        pass

    def setId(self, value):
        pass

    def getCareer(self, ):
        pass

    def setCareer(self, value):
        pass

    def getSubjects(self, ):
        pass

    def setSubjects(self, value):
        pass

    def setNote(self, subject, student, note):
        pass

#user
class User(models.Model):
    class Meta:
        pass

    id = undefined()
    document = undefined()
    documentType = undefined()
    name = undefined()
    lastname = undefined()
    personalEmail = undefined()
    institutionalEmail = undefined()
    institutionalEmailPassword = undefined()
    birthday = undefined()
    phone = undefined()
    recoveryToken = undefined()

    def login(self, ):
        pass

    def generateRecoveryToken(self, ):
        pass

    def getName(self, ):
        pass

    def setName(self, value):
        pass

    def getLastname(self, ):
        pass

    def setLastname(self, value):
        pass

    def getPersonalEmail(self, ):
        pass

    def setPersonalEmail(self, value):
        pass

    def getInstitutionalEmail(self, ):
        pass

    def setInstitutionalEmail(self, value):
        pass

    def getInstitutionalEmailPassword(self, ):
        pass

    def setInstitutionalEmailPassword(self, value):
        pass

    def getBirthday(self, ):
        pass

    def setBirthday(self, value):
        pass

    def getPhoneNumbers(self, ):
        pass

    def setPhoneNumbers(self, value):
        pass

    def getRecoveryToken(self, ):
        pass

    def setRecoveryToken(self, ):
        pass

    def login(self, ):
        pass

    def recoverPassword(self, ):
        pass

#userType
class UserType(Enum):
    STUDENT = 1
    TEACHER = 2
    DIRECTOR = 3
