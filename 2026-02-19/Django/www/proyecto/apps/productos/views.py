from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
 
def productos_views(request):
    doc_externo = open("proyecto/templates/template.html")

    #mensaje = "Estas en la pantalla Productos"
    mensaje = "PRODUCTOS"
    planti = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"parrafo":mensaje})
    
    documento = planti.render(ctx)
    
    return render(request, "productos.html", {"parrafo":mensaje})
    # return HttpResponse(documento)
