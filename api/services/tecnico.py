from rapihogar.models import Pedido, Tecnico
from django.db.models import Sum


class TecnicoService:
    def __init__(self, tecnico=Tecnico):
        self.id = tecnico.id
        self.full_name = tecnico.full_name
        self.pedidos = Pedido.objects.filter(technician=tecnico)
        self.hours_worked = self.pedidos.aggregate(
            HOURS_WORKED=Sum('hours_worked')
        )['HOURS_WORKED'] or 0
        self.total_paid = self.calc_total_paid()
        self.pedidos_count = self.pedidos.count()

    def calc_total_paid(self):
        hours_worked = self.get_hours_worked()
        if hours_worked >= 0 and hours_worked <= 14:
            total = hours_worked * 200 - (hours_worked * 200 * 0.15)
        elif hours_worked >= 15 and hours_worked <= 28:
            total = hours_worked * 250 - (hours_worked * 250 * 0.16)
        elif hours_worked >= 29 and hours_worked <= 47:
            total = hours_worked * 300 - (hours_worked * 300 * 0.17)
        else:
            total = hours_worked * 350 - (hours_worked * 350 * 0.18)

        return total

    def get_total_paid(self):
        return self.total_paid

    def get_pedidos_count(self):
        return self.pedidos_count

    def get_hours_worked(self):
        return self.hours_worked


class ReportService:
    def __init__(self, queryset):
        self.tecnicos = [TecnicoService(tecnico) for tecnico in queryset]
        self.total_paid = sum(
            [tecnico.get_total_paid() for tecnico in self.tecnicos]
        )
        self.average_paid = self.total_paid / len(self.tecnicos)
        self.tecnicos_below_average = [
            tecnico for tecnico in self.tecnicos
            if tecnico.get_total_paid() < self.average_paid
        ]
        self.technician_with_lowest_paid = min(
            self.tecnicos, key=lambda tecnico: tecnico.get_total_paid()
        )
        self.technician_with_highest_paid = max(
            self.tecnicos, key=lambda tecnico: tecnico.get_total_paid()
        )

    def get_average_paid(self):
        return self.average_paid

    def get_technicians_below_average(self):
        return self.tecnicos_below_average

    def get_technician_with_lowest_paid(self):
        return self.technician_with_lowest_paid

    def get_technician_with_highest_paid(self):
        return self.technician_with_highest_paid
