from django.shortcuts import render, redirect
import datetime
from webpages.forms import ExternalData
from .forms import ExternalDataPdfForm
from .utils import process_pdf, replace_newlines_with_br


def list_pdfs(request):
    all_external_data = ExternalData.objects.all().filter(data_type='pdf')

    for data in all_external_data:
        data.content = data.content[:500]

    context = {
        'all_external_data': all_external_data
    }

    return render(request, 'list-pdf.html', context)


def view_pdf(request):
    ed_pdf = get_object_or_404(ExternalData, id=id)
    context = {
        'external_data': replace_newlines_with_br(ed_pdf)
    }
    return render(request, 'view-pdf.html', context)


def save_pdf(request):
    if request.method == 'POST':
        ed_pdf_form = ExternalDataPdfForm(request.POST, request.FILES)
        if ed_pdf_form.is_valid():
            text = process_pdf(request.FILES['pdf'])
            ed_pdf = ExternalData(
                content=text.decode('utf-8'),
                url=None,
                added_on=datetime.datetime.now(datetime.timezone.utc),
                data_type='pdf'
            )
            ed_pdf.save()
            return redirect('list_pdfs')
    else:
        ed_pdf_form = ExternalDataPdfForm()
        context = {
            'ed_pdf_form': ed_pdf_form
        }
        return render(request, 'new-pdf.html', context)
