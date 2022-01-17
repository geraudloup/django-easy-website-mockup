from django.shortcuts import render

# Create your views here.

# def your_name_of_view(request):
#   context = {'your_data_to_inject_in_template': '...'}
#   return render(request, 'your_template.html', context)

def homepage(request):
  context = {}
  return render(request, 'homepage.html', context)

def demo_bootstrap(request):
  context = {}
  return render(request, 'demo-bootstrap.html', context)
