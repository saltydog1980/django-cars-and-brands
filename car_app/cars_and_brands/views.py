from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Brand, CarModel, Option, ModelOptions



# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def brands(request):
    data = {'brand_list': Brand.objects.all().values()}
    return render(request, 'pages/brands.html', data)

def brand_new(request):
    if request.method == 'POST':
        car_brand_name = request.POST['car_brand_name']
        car_brand_country = request.POST['car_brand_country']
        car_brand_date = request.POST['car_brand_date']
        new_car = Brand(name=car_brand_name, origin_country=car_brand_country, establishment_date= car_brand_date)
        new_car.save()
        return JsonResponse({'status': "Brand added successfully!"})
    return render(request, 'pages/brand_new.html')


def brand(request, brand_id):
    data = {'brand': Brand.objects.get(id=brand_id)}
    return render(request, 'pages/brand_detail.html', data)


def brand_update(request, brand_id):
    if request.method == 'POST':
        car_brand_name = request.POST['car_brand_name']
        car_brand_country = request.POST['car_brand_country']
        car_brand_date = request.POST['car_brand_date']
        #grabbing the brand by id then re-assigning the  values
        update_car = Brand.objects.get(id=brand_id)
        update_car.name = car_brand_name
        update_car.origin_country = car_brand_country
        update_car.establishment_date = car_brand_date
        #saving the item
        update_car.save()
        return JsonResponse({'status': "Brand updated successfully!"})

    
    data = {'brand': Brand.objects.get(id=brand_id)}
    return render(request, 'pages/brand_edit.html', data)


def cars(request, brand_id):
    model_list = CarModel.objects.filter(brand=brand_id).values
    data = {"brand_id": brand_id, "model_list": model_list}
    return render(request, 'pages/models.html', data)


def car_new(request, brand_id):
    if request.method == "POST":
        brand = Brand.objects.get(id=brand_id)
        car_model_name = request.POST['car_model_name']
        car_model_country = request.POST['car_model_country']
        car_model_date = request.POST['car_model_date']
        car_model_price = request.POST['car_model_price']
        car_model_options = request.POST['car_model_options'].split(",")
        new_model = CarModel.objects.create(brand=brand, name=car_model_name, assembled_country=car_model_country, release_date=car_model_date, base_price=car_model_price)

        for option in car_model_options:
            ModelOptions.objects.create(model=new_model, option=Option.objects.get(id=option))
        return JsonResponse({'status': "Model added successfully!"})

    data = {'brand_id': brand_id, 'options': Option.objects.all().values()}
    return render(request, 'pages/car_new.html', data)


def car(request, brand_id, model_id):
    car = CarModel.objects.get(id=model_id)
    options = car.options.all().values()
    sticker_price = car.base_price
    for option in options:
        sticker_price += option['price']
    
    data = {"model": car, "brand_id":brand_id, "options": options,"sticker_price": sticker_price}
    return render(request, 'pages/model_detail.html', data)


def car_update(request, brand_id, model_id):
    if request.method == "POST":
        brand = Brand.objects.get(id=brand_id)
        car_model_name = request.POST['car_model_name']
        car_model_country = request.POST['car_model_country']
        car_model_date = request.POST['car_model_date']
        car_model_price = request.POST['car_model_price']
        car_model_options = request.POST['car_model_options'].split(",")
        #grabbing the brand by id then re-assigning the  values
        update_car = CarModel.objects.get(id=model_id)
        update_car.brand = brand
        update_car.name = car_model_name
        update_car.assembled_country = car_model_country
        update_car.release_date = car_model_date
        update_car.base_price = car_model_price
        #saving the item
        update_car.save()
        for option in car_model_options:
            ModelOptions.objects.create(model=update_car, option=Option.objects.get(id=option))

        return JsonResponse({'status': "Model updated successfully!"})
    

    data = {'brand_id': brand_id, 'options': Option.objects.all().values(), 'model': CarModel.objects.get(id=model_id)}
    return render(request, 'pages/car_edit.html', data)

#view to delete the car
def delete(request, model_id):
    car = CarModel.objects.get(id=model_id)
    car.delete()
    return redirect('cars_and_brands:home')
