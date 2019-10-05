import json
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views import generic
from django.shortcuts import render


from ..models import Product, Order


class IndexView(generic.View):

    def get(self, request, *args, **kwargs):
        context = {
            'products': Product.objects.filter(avaliabled=True),
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        response_data = {'nice':1}
        
        order = Order.objects.create(
	    name=request.POST['name'],
	    email=request.POST['email'],
	    phone=request.POST['phone'],
        )
        for i in request.POST.getlist('product[]'):
	    order.products.add(Product.objects.get(id=int(i)))

        order.save()
	try:
            products_orders = order.products.all()
            message = """
                Новый заказ на сайте!\n\n
                Имя пользователя: {0}\n
                Телефон: {1}\n
                Email: {2}\n\n
                Отмеченные товары: \n
                {3}\n\n
                Итого: {4}
            """.format(order.name, order.phone, order.email, '\n'.join(['(id: {0}) {1} - {2}'.format(i.id, i.title, i.price if i.price else '-') for i in products_orders]), sum([i.price for i in products_orders if i.price]))
            from django.conf import settings
            from django.core.mail import send_mail

            send_mail(
                'Новый заказ на сайте.',
                message,
                settings.EMAIL_HOST_USER,
                [settings.MAIL_FOR_ALERT,],
            )
        except:
            pass
        return HttpResponse(json.dumps(response_data), content_type="application/json")
