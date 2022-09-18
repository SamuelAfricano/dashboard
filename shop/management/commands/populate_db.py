import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from shop.models import Item, Purchase

class Command(BaseCommand):
	help='Dados aleatórios para preencher a Base de Dados'

	def add_arguments(self, parser):
		parser.add_argument("--montante", type=int, help="Número de dados.")

	def handle(self, *args, **options):
		names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Africano']
		surname = ['Samuel', 'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles']
		items = [
			Item.objects.get_or_create(name='CD',price=6.5),
			Item.objects.get_or_create(name='DVD',price=5),
			Item.objects.get_or_create(name='Disco de venil',price=50),
			Item.objects.get_or_create(name='Disk Man', price=4),
			Item.objects.get_or_create(name='Roteador',price=6.5),
			Item.objects.get_or_create(name='Disco de drake',price=230),
			Item.objects.get_or_create(name='SUblime disk',price=6.55),
			Item.objects.get_or_create(name='Podcast',price=65),
			Item.objects.get_or_create(name='Mask off',price=6.5),
		]
		motante = options['montante'] if options['montante'] else 500
		for i in range(0, motante):
			dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
			purchase = Purchase.objects.create(
				customer_full_name=random.choice(names) +' '+random.choice(surname),
				item=random.choice(items)[0],
				payment_method=random.choice(Purchase.PAYMENT_METHODS)[0],
				successful=True if random.randint(1, 2) == 1 else False			
			)
			purchase.time = dt
			purchase.save()

		self.stdout.write(self.style.SUCCESS('Base de dados carregada com sucesso!!'))