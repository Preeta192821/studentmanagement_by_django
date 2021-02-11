from django.db import models

# Create your models here.
class Admin(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=300)
	email=models.CharField(max_length=300)
	password=models.CharField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()



class Staffs(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=300)
	email=models.CharField(max_length=300)
	password=models.CharField(max_length=300)
	address=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()



class Courses(models.Model):
	id=models.AutoField(primary_key=True)
	course_name=models.CharField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()
	
    



class Subjects(models.Model):
	id=models.AutoField(primary_key=True)
	subject_name=models.CharField(max_length=300)
	course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
	staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()




class Students(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=300)
	email=models.CharField(max_length=300)
	password=models.CharField(max_length=300)
	gender=models.CharField(max_length=300)
	profile_pic=models.FileField()
	address=models.TextField()
	course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
	id = models.AutoField(primary_key=True)
	subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
	attendance_date=models.DateTimeField(auto_now_add=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class AttendanceReport(models.Model):
	id = models.AutoField(primary_key=True)
	subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
	attendance_date=models.DateTimeField(auto_now_add=True)
	status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class LeaveReportStudent(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
	leave_date=models.CharField(max_length=300)
	leave_message=models.CharField(max_length=300)
	leave_status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class LeaveReportStaffs(models.Model):
	id=models.AutoField(primary_key=True)
	staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
	leave_date=models.CharField(max_length=300)
	leave_message=models.CharField(max_length=300)
	leave_status=models.BooleanField(default=False)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class FeedbackStudent(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=300)
	feedback_reply=models.CharField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class FeedbackStaffs(models.Model):
	id=models.AutoField(primary_key=True)
	staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=300)
	feedback_reply=models.CharField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

class NotificationStudent(models.Model):
	id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
	message=models.TextField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class NotificationStaffs(models.Model):
	id=models.AutoField(primary_key=True)
	staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
	message=models.TextField(max_length=300)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()

from django.contrib.auth.models import User
import hashlib
import uuid
# Create your models here.
def hash_password(password):
	salt = uuid.uuid4().hex
	return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password,user_password):
	password,salt = hashed_password.split(':')
	return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# Create your models here.

class user(models.Model):
	username = models.CharField(max_length=20)
	email_id = models.CharField(max_length=50,unique=True,primary_key=True)
	password = models.CharField(max_length=512)

	def __str__(self):
		return (self.username)

	@classmethod
	def checkUserExists(cls,email_id):
		s = cls.objects.filter(email_id=email_id)
		if s:
			return 1
		else:
			return 0

	@classmethod
	def registerUser(cls,username,email_id,password):
		try:
			if cls.checkUserExists(email_id):
				return -1
			else:
				#password = hash_password(password)
				u = cls(username=username,email_id=email_id,password=password)
				u.save()
				return u
		except Exception as e:
			return e

	@classmethod
	def loginUser(cls,email_id,password):
		s = cls.objects.filter(email_id=email_id)
		if s:
			if s[0].password==password:

				return s[0]
			else:
				return -1
		else:
			return -1
























































































































	

































































































