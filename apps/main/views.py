from django.shortcuts import render

#home View
def home(request):
    return render(request, 'main/home.html')

#About View
def about(request):
    return render(request, 'main/about.html')

#Terms and conditions view
def terms(request):
    return render(request, 'main/terms.html')

#contact Us View
def contact(request):
    return render(request, 'main/contact.html')

#Privacy View
# def privacy(request):
#     return render(request, 'main/privacy.html')

#Currency Converter View

#faq view

