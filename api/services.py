from rapihogar.models import Pedido, Tecnico
from django.db.models import Sum

class TecnicoService:
    def __init__(self, tecnico = Tecnico):
        self.id = tecnico.id
        self.full_name = tecnico.full_name
        self.pedidos = Pedido.objects.filter(technician = tecnico)
        self.hours_worked = self.pedidos.aggregate(HOURS_WORKED = Sum('hours_worked'))['HOURS_WORKED'] or 0
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

