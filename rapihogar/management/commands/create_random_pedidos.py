import random
from django.core.management.base import BaseCommand
from rapihogar.models import Pedido, User, Scheme, Tecnico


class Command(BaseCommand):
    help = 'Create n random objects for YourModel'

    def add_arguments(self, parser):
        parser.add_argument(
            'n',
            type=int,
            help='Number of random Pedidos to create'
            )

    def handle(self, *args, **kwargs):
        n = kwargs['n']
        if n >= 1 and n <= 100:
            tecnico_count = Tecnico.objects.count()
            cliente_count = User.objects.count()
            scheme_count = Scheme.objects.count()

            # Check that data exists
            if not tecnico_count or not cliente_count or not scheme_count:
                self.stdout.write(
                    self.style.ERROR(f'There are not enough objects created in the databse.')
                    )
                return

            for _ in range(n):
                Pedido.objects.create(
                    type_request=random.choice([0, 1]),
                    scheme=random.choice(Scheme.objects.all()),
                    client=random.choice(User.objects.all()),
                    technician=random.choice(Tecnico.objects.all()),
                    hours_worked=random.randint(1, 10),
                )

            self.stdout.write(
                self.style.SUCCESS(f'Successfully created {n} random objects')
                )
        else:
            self.stdout.write(
                self.style.HTTP_BAD_REQUEST(f'n argument must be between 1 and 100. {n} was provided.')
                )
