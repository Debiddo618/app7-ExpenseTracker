from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.contrib import messages
from django.db.models import Sum
import datetime


# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    expenses = Expense.objects.all()
    total = expenses.aggregate(Sum('amount'))

    # Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    year_data = Expense.objects.filter(date__gt=last_year)
    year_total = year_data.aggregate(Sum('amount'))

    # Logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    month_data = Expense.objects.filter(date__gt=last_month)
    month_total = year_data.aggregate(Sum('amount'))

    # Logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    week_data = Expense.objects.filter(date__gt=last_week)
    week_total = week_data.aggregate(Sum('amount'))

    daily_total = Expense.objects.filter().values(
        'date').order_by('date').annotate(sum=Sum('amount'))

    categorical_total = Expense.objects.filter().values(
        'category').order_by('category').annotate(sum=Sum('amount'))

    expense_form = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form': expense_form, "expenses": expenses, "total": total,
                                                "year_total": year_total, "month_total": month_total, "week_total": week_total, "daily_total": daily_total, "categorical_total": categorical_total})


def edit(request, id):
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    return render(request, "myapp/edit.html", {'expense_form': expense_form})


def delete(request, id):
    Expense.objects.filter(id=id).delete()
    messages.success(request, "Expense deleted successfully")
    return redirect('index')
