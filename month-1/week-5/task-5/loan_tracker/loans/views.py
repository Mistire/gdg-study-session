from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from loans.models import Loan
from django.db.models import Q

# Create your views here.
class LoanListView(ListView):
  model = Loan
  template_name = 'loans/loans_list.html'
  context_object_name = 'loans'

  def get_queryset(self):
    queryset = super().get_queryset()
    query = self.request.GET.get('q', '')

    if query:
      queryset = queryset.filter(Q(name__icontains=query))
    return queryset


class LoanCreateView(CreateView):
  model = Loan
  template_name = 'loans/loans_form.html'
  fields = ['name', 'amount', 'date', 'reason']
  success_url = reverse_lazy('loans:loan-list')


class LoanUpdateView(UpdateView):
  model = Loan
  template_name = 'loans/loans_form.html'
  fields = ['name', 'amount', 'date', 'reason']
  success_url = reverse_lazy('loans:loan-list')

class LoanDeleteView(DeleteView):
  model = Loan
  template_name = 'loans/loans_confirm_delete.html'
  success_url = reverse_lazy('loans:loan-list')