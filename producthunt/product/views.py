from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone   
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def home(request):
    products = Product.objects
    return render(request, 'product/home.html',{'products':products})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url']:
            try: 
                fm = request.FILES['image']
            except MultiValueDictKeyError:
                return render(request, 'product/create.html',{'error_message':'All fields are required.'})
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.pub_date = timezone.datetime.now()
            product.image = request.FILES['image']
            product.user = request.user
            product.save()
            return redirect('/product/' +str(product.id))
        else:
            return render(request, 'product/create.html',{'error_message':'All fields are required.'})
    else:
        return render(request, 'product/create.html')

def detail(request,p_id):
    product = get_object_or_404(Product,pk = p_id)
    return render(request,'product/detail.html',{'product': product})  

@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes += 1
        product.save()
        return redirect('/product/' + str(product.id))      