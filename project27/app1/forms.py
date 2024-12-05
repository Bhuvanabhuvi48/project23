from django import forms
class StudentForm(forms.Form):
    rollno=forms.IntegerField(label='StudentRollNo')
    name=forms.CharField(label='SudentName',max_length=20)
    course=forms.CharField(label='Course',max_length=20)
    fee=forms.IntegerField(label='StudentFee')