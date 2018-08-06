from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Course

# Create your views here.
@login_required
def main(request):
	course_list = Course.objects.filter(professor = request.user) #Busca por todos os cursos ministrados pelo professor logado
	context = { 'course_list': course_list} #Prepara a informação para a página
	return render(request, 'home/main.html', context)