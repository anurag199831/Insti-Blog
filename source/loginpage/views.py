from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData
# Create your views here.

def submitcategory(request):
    """
    This function submits category of a user to database 

    Args:
        request

    Returns:
        index.html: HTML page 
        
    """
    print('hello2')
    catg= Category.objects.all()
    selected=''
    for i in catg:
        temp=request.GET.get(i.name,'no value')
        if temp != 'no value':
            selected=selected+','+i.name
    curremail=request.user.email
    temp=UserData.objects.filter(uemail=curremail).exists()
    # UserData.objects.update_or_create(uemail=curremail,ucategory=selected)
    if temp:
        temp2 = UserData.objects.get(uemail=request.user.email)
        temp2.ucategory=selected
        temp2.save()
    else :
        UserData.objects.create(uemail=curremail,ucategory=selected)
    catg= Category.objects.all()
    blog= Blog.objects.all()
    temp2 = UserData.objects.get(uemail=request.user.email)
    print(temp2.ucategory)
    ucat=temp2.ucategory.split(",")[1:]
    blog2=[]
    ucat=temp2.ucategory.split(",")[1:]
    print('here')
    for i in blog:
        print('here2')
        temp=i.category.split(",")[1:]
        print(temp,ucat)
        if set(temp)&set(ucat):
            blog2.append(i.title)
            print('here3')
    params={'cat':catg,'blog':blog,'blog2':blog2,'ucat':ucat}
    return render(request,'index.html',params)
    # params={'cat':catg,'blog':blog,'ucat':ucat}
    # return render(request,'index.html',params)
    

def editcat(request):
    """
    This function edit user category 

    Args:
        request

    Returns:
        selectcat.html: HTML page 
        
    """
    print('hello')
    catg= Category.objects.all()
    blog= Blog.objects.all()
    params={'cat':catg,'blog':blog}
    return render(request,'selectcat.html',params)

def index(request):
    """
    This function redirects to homepage after logging in

    Args:
        request

    Returns:
        index.html: HTML page 
        
    """
    curremail=request.user.email
    temp=UserData.objects.filter(uemail=curremail).exists()
    
    if temp:

        # catg= Category.objects.all()
        # blog= Blog.objects.all()
        # temp2 = UserData.objects.get(uemail=request.user.email)
        # print(temp2.ucategory)
        # ucat=temp2.ucategory.split(",")[1:]
        # params={'cat':catg,'blog':blog,'ucat':ucat}
        # return render(request,'index.html',params)

        catg = Category.objects.all()
        blog = Blog.objects.all()
        temp2 = UserData.objects.get(uemail=request.user.email)
        print(temp2.ucategory)
        blog2=[]
        ucat=temp2.ucategory.split(",")[1:]
        print('here')
        for i in blog:
            print('here2')
            temp=i.category.split(",")[1:]
            print(temp,ucat)
            if set(temp)&set(ucat):
                blog2.append(i.title)
                print('here3')
        params={'cat':catg,'blog':blog,'blog2':blog2,'ucat':ucat}
        return render(request,'index.html',params)
    else:
        catg= Category.objects.all()
        blog= Blog.objects.all()
        params={'cat':catg,'blog':blog}
        return render(request,'selectcat.html',params)