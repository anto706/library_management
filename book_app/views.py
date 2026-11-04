from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class Goodmorningview(View):
    def get(self,request):
        data={
            "message":"Good Morning"
        }
        return JsonResponse(data)
    
class Libraryview(View):
    def get(self,request):
        data={
            "Library": "Central Library",
            "contact":"987654321",
            "owner":"Renjith",
            "Location": "Idukki",
            "Status": "Open"

        }
        return JsonResponse(data)

class Bookview(View):
    def get(self,request):
        data={
                "Book_Name": "Django for Beginners",
                "Author": "William S. Vincent",
                "Price": 650,
                "Description":"fhrfrf rfbjrg5 fgnkfredihnfdmsfhd",
                "published_year":2000

        }
        return JsonResponse(data)

class StudentView(View):
    def get(self,request):
        data={
             "Name": "Anu",
             "Course": "Python Django",
             "Batch": "June 2026",
             "Institution":"Luminar Technolab",
             "joining_year":2026,
             "joining_month":"May",
             "Location":"Kochi",
            "Mobile":8976543210,
            "DOB":"20/08/2000"

        }
        return JsonResponse(data)
    
class BooksView(View):
    def get(self,request):
        data={
        "Books": [
        "Python",
        "Django",
        "Java",
        "React",
        "MySQL"
    ]

        }
        return JsonResponse(data)
    
class EmployeeView(View):
    def get(self,request):
        data={
            "id":"1",
            "name":"anto",
            "place":"kakkanad",
            "designation":"developer",
            "contact":"123123",
            "experience":"0",
            "qualification":"0"

        }
        return JsonResponse(data)