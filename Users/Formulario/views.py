from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Formulario.models import Usuarios


def formulario(request):
	return render(request,'Fromulario.html')

def gracias(request):
	return render(request, 'vistaformulario.html')

def send(request):
	errors = []
	if request.method == 'POST':
		b = request.POST['codigo']
		a = request.POST['nombre']
		c = request.POST['edad']
		d = request.POST['pass']
		e = request.POST['correo']
		#f = request.POST['pw']

		busq = Usuarios.objects.filter(nombre_icontains=a)
		busq2 = Usuarios.objects.filter(codigo_icontains=b)

		if not request.POST.get('codigo', ''):
			errors.append('Por favor introduce el codigo.')

		if not request.POST.get('nombre', ''):
			errors.append('Por favor introduce un Nombre.')

		if not request.POST.get('edad', ''):
			errors.append('Por favor introduce la edad.')

		if not request.POST.get('pass', ''):
			errors.append('Por favor introduce una contrasena.')

		if request.POST.get('correo') and '@' not in request.POST['correo']:
			errors.append('Por favor introduce una direccion de emailvalida.')
		
		if not request.POST.get('wp', ''):
			errors.append('Por favor introduce una Pagina web.')

		##if busq = a:
		##	errors.append('Este nombre de Usuario ya existe')

		##if busq2 = b:
		##	errors.append('Este nombre de Usuario ya existe')

		if 	not errors:
			p1 = Usuarios(nombre = a, codigo = b, edad = c, contrasena = d, correo = e )
			p1.save()
			return HttpResponseRedirect('/send/gracias')
			
	return render(request, 'Fromulario.html', {'errors': errors})