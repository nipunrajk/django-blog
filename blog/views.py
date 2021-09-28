from django.shortcuts import render
from django.http import HttpResponse

posts = [
 {
   'author': 'Nipun Raj',
   'title': 'Blog post 1',
   'content': 'First post content',
   'date_posted': 'September 25 2021' 

 },
  {
   'author': 'Nipun Raj',
   'title': 'Blog post 1',
   'content': 'First post content',
   'date_posted': 'September 25 2021' 

 }
]


# Create your views here.
def home(request):
 context = {
  'posts': posts
   
 } 
 return render(request, 'blog/home.html', context)

def about(request):
 return render(request, 'blog/about.html', {'title': 'about'})