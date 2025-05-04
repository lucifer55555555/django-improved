from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid username or password'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class HomeView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        books = Book.objects.all()
        cart = request.session.get('cart', {})
        return render(request, 'store/home.html', {'books': books, 'cart': cart})

class AddCart(View):
    def post(self, request):
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 0))

        if quantity <= 0:
            return redirect('home') 

        cart = request.session.get('cart', {})

        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        return redirect('home')


class RemoveCart(LoginRequiredMixin, View):
    login_url = 'login'
    def post(self, request):
        item_id = request.POST.get('item_id')
        cart = request.session.get('cart', {})
        if item_id in cart:
            del cart[item_id]
        request.session['cart'] = cart
        return redirect('home')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = Book.objects.filter(id__in=cart.keys())
        cart_items = []

        for book in books:
            quantity = cart.get(str(book.id), 0)
            cart_items.append({
                'book': book,
                'quantity': quantity
            })

        return render(request, 'store/cart.html', {'cart_items': cart_items})

