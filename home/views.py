from django.shortcuts import render
from django.views import View
from .models import *


class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['contacts'] = ContactInfo.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['products'] = Product.objects.all()

        return render(request, 'index.html', self.views)

class CategoryView(BaseView):
    def get(self, request, slug):
        self.views
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_product'] = Product.objects.filter(category_id = cat_id)
        return render(request, 'category.html', self.views)

class BrandView(BaseView):
    def get(self, request, slug):
        self.views
        b_id = Brand.objects.get(slug = slug).id
        self.views['brand_product'] = Product.objects.filter(brand_id = cat_id)
        return render(request, 'brand.html', self.views)