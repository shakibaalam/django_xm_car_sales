from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from .models import CarModel, BrandModel, CommentModel
from users.forms import CommentForm
from django.utils.decorators import method_decorator


class CarListView(ListView):
    model = CarModel
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug:
            return CarModel.objects.filter(brand__slug=brand_slug)
        return CarModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.all()
        context['current_brand'] = self.kwargs.get('brand_slug', '')
        return context


@method_decorator(login_required, name='dispatch')
class CarDetailView(View):

    def get(self, request, *args, **kwargs):
        car = get_object_or_404(CarModel, pk=kwargs['pk'])
        comment_form = CommentForm()
        return render(request, 'cars/car_detail.html', {
            'car': car,
            'comment_form': comment_form,
        })

    def post(self, request, *args, **kwargs):
        car = get_object_or_404(CarModel, pk=kwargs['pk'])
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect(reverse('car_detail', kwargs={'pk': car.pk}))
        return render(request, 'cars/car_detail.html', {
            'car': car,
            'comment_form': comment_form,
        })
