from django.test import TestCase

# Create your tests here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

        ultimas_datas = Entrada.objects.filter(descricao__referencia=busca)



def update(request, id):
   emp = Employee.objects.get(pk = id)
   #you can do this for as many fields as you like
   #here I asume you had a form with input like <input type="text" name="name"/>
   #so it's basically like that for all form fields
   emp.name = request.POST.get('name')
   emp.save()
   return HttpResponse('updated')

def delete(request, id):
   emp = Employee.objects.get(pk = id)
   emp.delete()
   return HttpResponse('deleted')