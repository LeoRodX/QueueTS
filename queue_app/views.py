from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import QueueTab
import socket


gong_was = 0
invited_was = 0


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            today_reg = date.today()
            wu = QueueTab.objects.latest('id')
            wz = int(wu.ticket)
            wd = wu.data_reg
            # Проверка соответствует ли номер талона интервалу от 1 до 9.
            if (1 > wz) or (wz > 98) or (wd < today_reg):
                wc = 0
            else:
                wc = wz
            wa = wc + 1
            QueueTab.objects.create(ticket=wa)
            return redirect('queue_app:ticket')
    else:
        form = RegistrationForm(initial={'ticket': 11})
    return render(request, 'queue_app/registration.html', {'form': form})


def pages(request):
    return render(request, 'queue_app/pages.html')


def probe(request):
    return render(request, 'queue_app/probe.html')


def screen(request):
    global gong_was
    today_screen = date.today()
    gong = 0
    list_for_screen = QueueTab.objects.filter(serviced__isnull=True, data_reg=today_screen)[:7]
    list_for_screen_count = QueueTab.objects.filter(serviced__isnull=True, data_reg=today_screen)[:7].count()
    invited_on_screen_count = QueueTab.objects.filter(invited__isnull=False, serviced__isnull=True,
                                                      data_reg=today_screen).count()

    opacity_on_screen = 170 + ((list_for_screen_count - 1) * 102)

    if invited_on_screen_count > 0:
        invited_on_screen = 'Пройдите'
        invited_on_screen2 = 'на прием'
    else:
        invited_on_screen = ''
        invited_on_screen2 = ''

    # Cделаем чтобы гонг звучал при вызове только один раз

    if invited_on_screen_count == 0:
        gong_was = 0

    if invited_on_screen_count > 0 and gong_was == 1:
        gong = 0

    if invited_on_screen_count > 0 and gong_was == 0:
        gong_was = 1
        gong = 1

    return render(request, 'queue_app/screen.html', {'list_for_screen': list_for_screen,
                                                     'invited_on_screen': invited_on_screen,
                                                     'invited_on_screen2': invited_on_screen2,
                                                     'gong': gong,
                                                     'opacity_on_screen': opacity_on_screen})


def ticket(request):
    posts = QueueTab.objects.latest('id')
    return render(request, 'queue_app/ticket.html', {'posts': posts})


def about(request):
    return render(request, 'queue_app/about.html')


def operator(request):
    global invited_was
    date_today = date.today()
    dt_today = datetime.today()
    if 'button_invited' in request.POST:
        button_invited_count = QueueTab.objects.filter(invited__isnull=True,
                                                       serviced__isnull=True, data_reg=date_today).count()
        if button_invited_count > 0 and invited_was == 0:
            button_invited_pk = QueueTab.objects.filter(invited__isnull=True,
                                                        serviced__isnull=True, data_reg=date_today).first().pk
            QueueTab.objects.filter(pk=button_invited_pk).update(invited=dt_today)
            invited_was = 1
        return redirect('queue_app:operator')
    elif 'button_serviced' in request.POST:
        button_serviced_count = QueueTab.objects.filter(invited__isnull=False,
                                                        serviced__isnull=True, data_reg=date_today).count()
        if button_serviced_count > 0: # and invited_was == 1:
            button_serviced_pk = QueueTab.objects.filter(invited__isnull=False,
                                                         serviced__isnull=True, data_reg=date_today).first().pk
            QueueTab.objects.filter(pk=button_serviced_pk).update(serviced=dt_today)
            invited_was = 0
        return redirect('queue_app:operator')
    else:
        form = RegistrationForm()

        total_tickets = QueueTab.objects.filter(invited__isnull=True, serviced__isnull=True,
                                                data_reg=date_today).count()

        invited_count = QueueTab.objects.filter(invited__isnull=False, serviced__isnull=True,
                                                data_reg=date_today).count()
        if invited_count > 0:
            invited_ticket = QueueTab.objects.filter(invited__isnull=False, serviced__isnull=True,
                                                     data_reg=date_today).first().ticket
        else:
            invited_ticket = ' - '

        if total_tickets == 0:
            total_tickets = '0'

        return render(request, 'queue_app/operator.html', {'form': form,
                                                           'invited_ticket': invited_ticket,
                                                           'total_tickets': total_tickets})
