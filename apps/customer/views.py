from django.views.generic import ListView, CreateView
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm


# Create your views here.

class CustomerListView(ListView):
    template_name = 'customer/customer_list.html'
    model = Customer
    queryset = Customer.objects.all()


class CustomerCreateView(CreateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')
