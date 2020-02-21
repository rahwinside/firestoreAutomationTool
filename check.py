import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:\\Users\\Administrator\\Downloads\\bookbrokers.json')
firebase_admin.initialize_app(cred)
print('auth OK!')

sem1=[u'Communicative English',u'Mathematics',u'Physics',u'Chemistry',u'Python Programming',u'Engineering Graphics']
sem2=[u'Technical English',u'Engineering Mathematics II',u'Physics II',u'Basic Electrical,Electronics and Measurement Engineering',u'Information Technology Essentials',u'Programming in C']
sem3=[u'Discrete Mathematics',u'Digital Principles and System Design',u'Data Structures',u'Object Oriented Programming',u'Analog and DigitalCommunication']
sem4=[u'Probability and Statistics',u'Computer Architecture',u'Database Management Systems',u'Design and Analysis of Algorithms',u'Operating Systems',u'Environmental Science and Engineering']
sem5=[u'Algebra and Number Theory',u'Computer Networks',u'Microprocessors and Microcontrollers',u'Web Technology',u'Software Engineering']
sem6=[u'Computational Intelligence',u'Object Oriented Analysis and Design',u'Mobile Communication',u'Big Data Analytics',u'Computer Graphics and Multimedia']
sem7=[u'Principles of Management',u'Cryptography and Network Security',u'Cloud Computing']
sem8=[u'Project Manual']

sem = [sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8]

db = firestore.client()

for i in range(0,8):
    for x in sem[i]:
        doc_ref = db.collection(u'books').document(u'mech').collection(str(i+1)).document(x).collection(u'collection').document(u'init')
        doc_ref.set({
            u'first': u'INIT'
        })
