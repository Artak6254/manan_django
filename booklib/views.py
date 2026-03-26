from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse,HttpResponse
from .models import Book, Category,SelectedBook


def home(request):
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories': categories
    })



def category_books(request,category_id=None):
    categories = Category.objects.all()

    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    return render(request, 'category_books.html', {
        'books': books,
        'categories': categories
    })


def contact(request):
    return render(request, 'contact.html')    

def login_page(request):
    return render(request, 'login.html')    



def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form}) 


def forgetPass(request):
    form = RegisterForm()
    return render(request, 'forgetPass.html',{'form': form})

def user_account(request):
    if not request.user.is_authenticated:
        return redirect("login")

    selected_books = SelectedBook.objects.filter(user=request.user).select_related("book")

    return render(request, "useraccount.html", {
        "selected_books": selected_books
    })

@require_POST
def toggle_book(request):
    book_id = request.POST.get("book_id")
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)

    exists = SelectedBook.objects.filter(user=user, book=book).exists()

    if exists:
        return JsonResponse({
            "status": "exists",
            "message": "Դուք արդեն ընտրել եք այս գիրքը"
        })

  
    SelectedBook.objects.create(user=user, book=book)

    return JsonResponse({
        "status": "added",
        "message": "Գիրքը ավելացվեց"
    })



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Գրանցումը հաջողությամբ կատարվեց։")
            return redirect("login_page")  # կամ "home"
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        users = User.objects.filter(email=email)
        if not users.exists():
            messages.error(request, "Էլ․ հասցե կամ գաղտնաբառ սխալ է։")
            return redirect("login")
        
        user_obj = users.first()
        
        user = authenticate(username=user_obj.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_account")
        else:
            messages.error(request, "Էլ․ հասցե կամ գաղտնաբառ սխալ է։")
            return redirect("login")

    return render(request, "login.html")



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
Անուն: {name}
Email: {email}

Հաղորդագրություն:
{message}
"""

        send_mail(
            subject="Նոր հաղորդագրություն",
            message=full_message,
            from_email="poghos877@gmail.com",
            recipient_list=[email],
        )

        return render(request, "sendcontact.html")

    return render(request, "contact.html")


