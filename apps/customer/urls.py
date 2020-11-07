from django.urls import path
from .views import CustomerListView, CustomerCreateView

app_name = 'customer'
urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer-list'),
    path('', CustomerCreateView.as_view(), name='customer-create')
]
