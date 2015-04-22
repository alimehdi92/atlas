from mongoengine import *

class Course(Document):
	cid = StringField(unique=True)
	name = StringField(required=True)

class Professor(Document):
	pid = StringField(unique=True)
	pname = StringField(required=True)
	rating = FloatField()

class TaughtBy(Document):
	course = ReferenceField(Course)
	pname = ReferenceField(Professor)

class User(Document):
	username = StringField(unique=True, required=True)
	password = StringField(required=True)

class Document(Document):
	fname = StringField(required=True)
	md5 = StringField(required=True, unique=True)
	upload_date = DateTimeField(required=True)
	upload_user = ReferenceField(User, required=True)
	binary = BinaryField(required=True)
