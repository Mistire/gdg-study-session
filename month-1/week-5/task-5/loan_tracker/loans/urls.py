from django.urls import path
from .views import LoanListView, LoanUpdateView, LoanCreateView, LoanDeleteView
app_name = 'loans'

urlpatterns = [
  path('', LoanListView.as_view(), name='loan-list'),
  path('add/', LoanCreateView.as_view(), name='loan-add'),
  path('<int:pk>/edit/', LoanUpdateView.as_view(), name='loan-edit'),
  path('<int:pk>/delete/', LoanDeleteView.as_view(), name='loan-delete')
]

