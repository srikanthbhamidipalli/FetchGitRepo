#render is to render a html document to show the generated result.
from django.shortcuts import render
#To work with Webpages requests is needed
import requests
def fetch(request):#request is the first parameter required when we are visiting any web page.
    user={}#To store the fetched repositories of a Git-user. 
    username=''#To store the nicknme of a Git user.
    if 'username' in request.GET:#checking for username in get method.
        username=request.GET['username']#Loading the value from TextField.
        #TO get the repositories using github api.
        url='https://api.github.com/users/{}/repos'.format(username)
        #To get a github webpage. 
        response=requests.get(url)
        #To get the response data in json format.
        user=response.json()
        #Sending the results to home page.
    return render(request,'home.html',{'user':user,'username':username})