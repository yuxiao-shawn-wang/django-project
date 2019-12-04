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
		with open (file_path, 'w') as f:
			try:
				writer = csv.writer(f)
				writer.writerow(field_list)
				for obj in Squirrel.objects.all():
					data = [getattr(obj, field) for field in field_list]
					writer.writerow(data)
			except Exception as e:
				raise CommandError(e)
		self.stdout.write(self.style.SUCCESS('Successfully write file "%s"' % file_path))