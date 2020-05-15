from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EntradaForm, SaidaForm
from django.core.paginator import Paginator
from .models import Toner, Departamento, Entrada, Saida
from django.utils import timezone
from django.db.models import F, Sum, Count, Max
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your views here.
def home(request):

    lista_stock = Entrada.objects.all().order_by('-id')[:5]
    paginator = Paginator(lista_stock, 5)
    page = request.GET.get('page')
    lista_stock = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
        lista_stock = Entrada.objects.filter(descricao__referencia__icontains=busca)

    context = {
        'lista_stock': lista_stock,

    }
    return render(request, 'index.html', context)


def botao_ver_tudo(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10, 800, 'mldmfmpdmflmd')
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Termo_de_Entrega_LTI.pdf')
    #return redirect('listagem')


def botao_relatorio(request):

    return redirect('relatorio')


def entrada_toner(request):

    context = {
        'form': EntradaForm
    }
    return render(request, 'entrada.html', context)


def botao_add_toner(request):

    addform = EntradaForm(request.POST)

    if addform.is_valid():
        addform.save()
        messages.add_message(request, messages.SUCCESS, 'O toner foi adicionado com sucesso!')
    return redirect('index')


def botao_cancelar_toner(request):

    return render(request, 'index,html')


def form_saida_toner(request):
    context = {
        'form': SaidaForm,
    }
    return render(request, 'saida.html', context)


def botao_add_saida(request):

    addform = SaidaForm(request.POST)
    if addform.is_valid():
        addform.save()
    return redirect('index')


#def botao_cancelar_toner(request):

#    return render(request, 'index,html')


def listagem_tudo(request):

    toner_list = Entrada.objects.all()
    paginator = Paginator(toner_list, 1)
    page = request.GET.get('page')
    toners = paginator.get_page(page)
    busca = request.GET.get('search')
    if busca:
        toners = Entrada.objects.filter(descricao__referencia__icontains=busca)

    return render(request, 'listagem.html', {'toners': toners})




def relatorio(request):
    total_toners = Entrada.objects.filter(descricao__descricao = 'Toner').count()
    total_toners_saidas = Saida.objects.filter(quantidade_saida=1).order_by('-data_saida')[:30].count()
    ultimo_departamento = Saida.objects.all().order_by('-data_saida')[:1]
    data_ultima_saida = Saida.objects.filter(descricao__descricao='Toner').dates('data_saida', 'day', order='DESC')[:1]


    # data_ultima_saida = Entrada.objects.filte
    # r(data__quarter=1).latest()
    # data_ultima_saida = Entrada.objects.order_by('-data').latest()

    # data_ultima_saida = Entrada.objects.filter(data=None)

    total_referencia_126A = Entrada.objects.filter(descricao__referencia='126A').count()
    b_126A = Entrada.objects.filter(descricao__referencia='126A', descricao__cor='Black').count()
    c_126A = Entrada.objects.filter(descricao__referencia='126A', descricao__cor='Cyan').count()
    y_126A = Entrada.objects.filter(descricao__referencia='126A', descricao__cor='Yellow').count()
    m_126A = Entrada.objects.filter(descricao__referencia='126A', descricao__cor='Magenta').count()

    total_referencia_131A = Entrada.objects.filter(descricao__referencia='131A').count()
    b_131A = Entrada.objects.filter(descricao__referencia='131A', descricao__cor='Black').count()
    c_131A = Entrada.objects.filter(descricao__referencia='131A', descricao__cor='Cyan').count()
    y_131A = Entrada.objects.filter(descricao__referencia='131A', descricao__cor='Yellow').count()
    m_131A = Entrada.objects.filter(descricao__referencia='131A', descricao__cor='Magenta').count()

    total_referencia_128A = Entrada.objects.filter(descricao__referencia='128A').count()
    b_128A = Entrada.objects.filter(descricao__referencia='128A', descricao__cor='Black').count()
    c_128A = Entrada.objects.filter(descricao__referencia='128A', descricao__cor='Cyan').count()
    y_128A = Entrada.objects.filter(descricao__referencia='128A', descricao__cor='Yellow').count()
    m_128A = Entrada.objects.filter(descricao__referencia='128A', descricao__cor='Magenta').count()

    total_referencia_410A = Entrada.objects.filter(descricao__referencia='410A').count()
    b_410A = Entrada.objects.filter(descricao__referencia='410A', descricao__cor='Black').count()
    c_410A = Entrada.objects.filter(descricao__referencia='410A', descricao__cor='Cyan').count()
    y_410A = Entrada.objects.filter(descricao__referencia='410A', descricao__cor='Yellow').count()
    m_410A = Entrada.objects.filter(descricao__referencia='410A', descricao__cor='Magenta').count()

    total_referencia_415A = Entrada.objects.filter(descricao__referencia='415A').count()
    b_415A = Entrada.objects.filter(descricao__referencia='415A', descricao__cor='Black').count()
    c_415A = Entrada.objects.filter(descricao__referencia='415A', descricao__cor='Cyan').count()
    y_415A = Entrada.objects.filter(descricao__referencia='415A', descricao__cor='Yellow').count()
    m_415A = Entrada.objects.filter(descricao__referencia='415A', descricao__cor='Magenta').count()

    total_referencia_53A = Entrada.objects.filter(descricao__referencia='53A').count()
    b_53A = Entrada.objects.filter(descricao__referencia='53A', descricao__cor='Black').count()
    c_53A = Entrada.objects.filter(descricao__referencia='53A', descricao__cor='Cyan').count()
    y_53A = Entrada.objects.filter(descricao__referencia='53A', descricao__cor='Yellow').count()
    m_53A = Entrada.objects.filter(descricao__referencia='53A', descricao__cor='Magenta').count()

    total_referencia_80A = Entrada.objects.filter(descricao__referencia='80A').count()
    b_80A = Entrada.objects.filter(descricao__referencia='80A', descricao__cor='Black').count()
    c_80A = Entrada.objects.filter(descricao__referencia='80A', descricao__cor='Cyan').count()
    y_80A = Entrada.objects.filter(descricao__referencia='80A', descricao__cor='Yellow').count()
    m_80A = Entrada.objects.filter(descricao__referencia='80A', descricao__cor='Magenta').count()

    total_referencia_17A = Entrada.objects.filter(descricao__referencia='17A').count()
    b_17A = Entrada.objects.filter(descricao__referencia='17A', descricao__cor='Black').count()
    c_17A = Entrada.objects.filter(descricao__referencia='17A', descricao__cor='Cyan').count()
    y_17A = Entrada.objects.filter(descricao__referencia='17A', descricao__cor='Yellow').count()
    m_17A = Entrada.objects.filter(descricao__referencia='17A', descricao__cor='Magenta').count()

    total_referencia_305A = Entrada.objects.filter(descricao__referencia='305A').count()
    b_305A = Entrada.objects.filter(descricao__referencia='305A', descricao__cor='Black').count()
    c_305A = Entrada.objects.filter(descricao__referencia='305A', descricao__cor='Cyan').count()
    y_305A = Entrada.objects.filter(descricao__referencia='305A', descricao__cor='Yellow').count()
    m_305A = Entrada.objects.filter(descricao__referencia='305A', descricao__cor='Magenta').count()

    total_referencia_CEXV38 = Entrada.objects.filter(descricao__referencia='CEXV38').count()
    b_CEXV38 = Entrada.objects.filter(descricao__referencia='CEXV38', descricao__cor='Black').count()
    c_CEXV38 = Entrada.objects.filter(descricao__referencia='CEXV38', descricao__cor='Cyan').count()
    y_CEXV38 = Entrada.objects.filter(descricao__referencia='CEXV38', descricao__cor='Yellow').count()
    m_CEXV38 = Entrada.objects.filter(descricao__referencia='CEXV38', descricao__cor='Magenta').count()

    total_referencia_GPR16 = Entrada.objects.filter(descricao__referencia='GPR16').count()
    b_GPR16 = Entrada.objects.filter(descricao__referencia='GPR16', descricao__cor='Black').count()
    c_GPR16 = Entrada.objects.filter(descricao__referencia='GPR16', descricao__cor='Cyan').count()
    y_GPR16 = Entrada.objects.filter(descricao__referencia='GPR16', descricao__cor='Yellow').count()
    m_GPR16 = Entrada.objects.filter(descricao__referencia='GPR16', descricao__cor='Magenta').count()

    context = {
        'total_toners': total_toners,
        'total_toners_saidas': total_toners_saidas,
        'ultimo_departamento': ultimo_departamento,
        'data_ultima_saida': data_ultima_saida,
        'total_referencia_126A': total_referencia_126A,
        'b_126A': b_126A,
        'c_126A': c_126A,
        'y_126A': y_126A,
        'm_126A': m_126A,
        'total_referencia_128A': total_referencia_128A,
        'b_128A': b_128A,
        'c_128A': c_128A,
        'y_128A': y_128A,
        'm_128A': m_128A,
        'total_referencia_131A': total_referencia_131A,
        'b_131A': b_131A,
        'c_131A': c_131A,
        'y_131A': y_131A,
        'm_131A': m_131A,
        'total_referencia_410A': total_referencia_410A,
        'b_410A': b_410A,
        'c_410A': c_410A,
        'y_410A': y_410A,
        'm_410A': m_410A,
        'total_referencia_415A': total_referencia_415A,
        'b_415A': b_415A,
        'c_415A': c_415A,
        'y_415A': y_415A,
        'm_415A': m_415A,
        'total_referencia_53A': total_referencia_53A,
        'b_53A': b_53A,
        'c_53A': c_53A,
        'y_53A': y_53A,
        'm_53A': m_53A,
        'total_referencia_80A': total_referencia_80A,
        'b_80A': b_80A,
        'c_80A': c_80A,
        'y_80A': y_80A,
        'm_80A': m_80A,
        'total_referencia_17A': total_referencia_17A,
        'b_17A': b_17A,
        'c_17A': c_17A,
        'y_17A': y_17A,
        'm_17A': m_17A,
        'total_referencia_305A': total_referencia_305A,
        'b_305A': b_305A,
        'c_305A': c_305A,
        'y_305A': y_305A,
        'm_305A': m_305A,
        'total_referencia_CEXV38': total_referencia_CEXV38,
        'b_CEXV38': b_CEXV38,
        'c_CEXV38': c_CEXV38,
        'y_CEXV38': y_CEXV38,
        'm_CEXV38': m_CEXV38,
        'total_referencia_GPR16': total_referencia_GPR16,
        'b_GPR16': b_GPR16,
        'c_GPR16': c_GPR16,
        'y_GPR16': y_GPR16,
        'm_GPR16': m_GPR16,
    }
    return render(request, 'relatorio.html', context)




def saida_toner(request):

    return render(request, 'saida.html')

