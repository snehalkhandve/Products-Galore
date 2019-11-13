from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product # to import all the Product code 
from django.utils import timezone

# Create your views here.

def home(request):
	products = Product.objects # get all the available products from database
	return render(request, 'products/home.html', {'products':products})

# django is just sooooo amazing that with mere single statement below it will 1st check if user is logged in 
# and allow access to create page else redirect it to login page
@login_required(login_url="/accounts/signup")
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['icon'] and request.POST['image'] :
			product = Product() # create a new product object for owner who wanna create a product
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://') :
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']
			product.icon = request.POST['icon']
			product.image = request.POST['image']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save() # to save the product
			return redirect('/products/'+ str(product.id))
		else:
			return render(request , 'products/create.html', {'error':'All the fields should be filled'})
	else:
		return render(request, 'products/create.html')


'''
	So whenever u r adding images in create.html page 1st create an images folder inside producthunt-project
	and add images there then choose images from these images folder only
'''

def  detail(request , product_id):
	product = get_object_or_404(Product, pk = product_id)
	return render(request, 'products/detail.html', {'product': product})

@login_required(login_url="/accounts/signup")  # u can upvote only when logged in
def  upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk = product_id)
		product.votes_total += 1
		product.save() 		# save this to database
		return redirect('/products/'+ str(product.id))