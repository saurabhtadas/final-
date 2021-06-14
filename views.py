from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Menu
from .models import Cuisines
from .models import Cart

# Create your views here.
def index(request):
	return render(request, 'index.html')

def dish(request):
	menuData = Menu.objects.all()
	return render(request, 'menu.html', {'menu': menuData}) 

def menucard(request, menuType, menu):
	menuData = Menu.objects.get(menu=menu)
	data = Cuisines.objects.filter(menuType=menuType, dish_type_id=menuData)
	return render(request, 'dish.html', {'menuType': menuType, 'menu': menu, 'cuisines': data}) 

def cartData(request):
	# get the data from the form
	if request.method == 'POST':
		username = request.POST.get('username')
		dish_id = request.POST.get('dish_id')
		menu = request.POST.get('menu')
		menuType = request.POST.get('menuType')
		dish_name = request.POST.get('dish_name')
		cost = request.POST.get('cost')
		quantity = request.POST.get('quantity')
		menuData = Menu.objects.filter(menu = menu).values('id')
		data = Cuisines.objects.all().filter(menuType = menuType, dish_type_id = menuData)

		# save data to the table cart
		Cart.objects.create(
			menuType = menuType, 
			dish_name = dish_name, 
			unit_price = cost, 
			cost = cost, 
			quantity = quantity, 
			username = username, 
			dish_type_id = menuData
		)
		return HttpResponse('Added to cart!')
	else:
		return HttpResponse('Invalid request!')

def cart(request):
	if request.user.is_authenticated:
		cartData = Cart.objects.filter(username=request.user.email).values()

		# To calculate the total cost
		totalamount = Cart.objects.filter(username=request.user.email).values_list('cost', flat=True)
		a = list(totalamount)
		total = 0
		for i in range(0,len(a)):
			total = total + a[i]
		return render(request, 'cart.html', {'dish': cartData, 'totalamount': total})
	else:
		return render('index.html')

def cartRemove(request):
	if request.method == 'POST':
		cartid = request.POST['id']
		Cart.objects.filter(id=cartid).delete()
		return HttpResponse('')
	else:
		return render('index.html')

def cartAdd(request):
	if request.method == 'POST':
		cartid = request.POST['id']
		quantity = request.POST['qty']
		quantity = int(quantity) + 1
		cost = int(request.POST['unit_price']) * quantity
		data = Cart.objects.filter(id=cartid).update(quantity=quantity, cost=cost)
		return HttpResponse('')
	else:
		return render('index.html')


def order(request):
	return render(request, 'book.html')

def place_order(request):
	if request.method == 'POST':
		table_no = request.POST['tableno']
		contact_no = request.POST['contact_no']
		data = Cart.objects.filter(username=request.user.email).update(table_no=table_no, contact_no=contact_no)
		return HttpResponse('<script type="text/javascript">alert("Order Placed!"); location.href="/";</script>')
	else:
		return HttpResponseRedirect('/');