from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer
from rest_framework import viewsets
from pizza.serializers import ToppingSerializer, OrderSerializer, \
    CrustSerializer, SizeSerializer, SidesSerializer, SideNumberSerializer
from pizza.models import Order, Topping, Crust, Size, Sides, SideNumber

User = get_user_model()

class UserCreateAPIView(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()



class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user).order_by('-order_time')

    def create(self, request, *args, **kwargs):
        a = super().create(request, *args, **kwargs)
        print(a.data)
        order = Order.objects.get(id=a.data['id'])

        toppings = order.toppings.all()
        print('number of toppings ', order.toppings.count())
        total = 0
        for i in toppings:
            total += i.topping_price
            print('toppings total', total)

        calculate_price = order.crust.crust_price + order.size.size_price + total

        order.order_total = calculate_price
        order.save()
        print(order.crust.crust_price)
        print(order.size.size_price)
        print(order.order_total)
        return a



# User = get_user_model()

class UserCreateAPIView(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

# User = get_user_model()

class ToppingViewSet(viewsets.ModelViewSet):

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class CrustViewSet(viewsets.ModelViewSet):

    queryset = Crust.objects.all()
    serializer_class = CrustSerializer

class SizeViewSet(viewsets.ModelViewSet):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SidesViewSet(viewsets.ModelViewSet):

    queryset = Sides.objects.all()
    serializer_class = SidesSerializer

class SideNumberViewSet(viewsets.ModelViewSet):

    queryset = SideNumber.objects.all()
    serializer_class = SideNumberSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user =self.request.user
        return Order.objects.filter(user=user)



