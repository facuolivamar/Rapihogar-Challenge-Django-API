from rapihogar.models import Pedido, Tecnico
from django.db.models import Sum

class TecnicoService:
    def __init__(self, tecnico = Tecnico):
        self.pedidos = Pedido.objects.filter(technician = tecnico)
        self.hours_worked = self.pedidos.aggregate(HOURS_WORKED = Sum('hours_worked'))['HOURS_WORKED'] or 0

    def calc_total_paid(self):
        hours_worked = self.calc_hours_worked()
        if hours_worked >= 0 and hours_worked <= 14:
            total = hours_worked * 200 - (hours_worked * 200 * 0.15)
        elif hours_worked >= 15 and hours_worked <= 28:
            total = hours_worked * 250 - (hours_worked * 250 * 0.16)
        elif hours_worked >= 29 and hours_worked <= 47:
            total = hours_worked * 300 - (hours_worked * 300 * 0.17)
        else:
            total = hours_worked * 350 - (hours_worked * 350 * 0.18)
        
        return total

    def calc_pedidos_count(self):
        return self.pedidos.count()

    def calc_hours_worked(self):
        return self.hours_worked
