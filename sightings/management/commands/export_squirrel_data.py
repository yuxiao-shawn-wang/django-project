from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv
class Command(BaseCommand):
	help = 'Export data to a csv file'
	def add_arguments(self, parser):
		parser.add_argument('path', type=str, help='Path to csv file')

	def handle(self, *args, **kwargs):
		file_path = kwargs['path']
		field_list = [x.name for x in Squirrel._meta.fields]
		field_name = ['Y','X','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color',
		'Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging',
		'Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches',
		'Indifferent','Runs from']
		with open (file_path, 'w') as f:
			try:
				writer = csv.writer(f)
				writer.writerow(field_name)
				for obj in Squirrel.objects.all():
					data = [str(getattr(obj, field)) for field in field_list]
					data[4] = ''.join(data[4].split('-'))
					data[4] = data[4][4:]+data[4][:4]
					writer.writerow(data)
			except Exception as e:
				raise CommandError(e)
		self.stdout.write(self.style.SUCCESS('Successfully write file "%s"' % file_path))