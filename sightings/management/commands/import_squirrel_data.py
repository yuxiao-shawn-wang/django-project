import os
import csv
from django.core.management.base import BaseCommand, CommandError
from distutils.util import strtobool
from sightings.models import Squirrel

class Command(BaseCommand):
	help = 'Import data from a csv file'
	def add_arguments(self, parser):
		parser.add_argument('file', type=str, help='Path to csv file')

	def handle(self, *args, **kwargs):
		path = kwargs['file']
		
		if not os.path.exists(path):
			raise CommandError("%s does not exist." % path)

		with open (path, 'r') as f:
			reader = csv.DictReader (f)
			data = list(reader)
			for item in data:
				try:
					obj = Squirrel()
					obj.Latitude = float(item['Y'])
					obj.Longitude = float(item['X'])
					obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
					obj.Shift = item['Shift']
					date = item['Date'][4:] + '-' + item['Date'][:2] + '-' + item['Date'][2:4]
					obj.Date = date
					obj.Age = item['Age']
					obj.Primary_Fur_Color = item['Primary Fur Color']
					obj.Location = item['Location']
					obj.Specific_Location = item['Specific Location']
					obj.Running = (item['Running'] == 'true') or (item['Running'] == 'True')
					obj.Chasing = (item['Chasing'] == 'true') or (item['Chasing'] == 'True')
					obj.Climbing = (item['Climbing'] == 'true') or (item['Climbing'] == 'True')
					obj.Eating = (item['Eating'] == 'true') or (item['Eating'] == 'True')
					obj.Foraging = (item['Foraging'] == 'true') or (item['Foraging'] == 'True')
					obj.Other_Activities = item['Other Activities']
					obj.Kuks = (item['Kuks'] == 'true') or (item['Kuks'] == 'True')
					obj.Quaas = (item['Quaas'] == 'true') or (item['Quaas'] == 'True')
					obj.Moans = (item['Moans'] == 'true') or (item['Moans'] == 'True')
					obj.Tail_flags = (item['Tail flags'] == 'true') or (item['Tail flags'] == 'True')
					obj.Tail_twitches = (item['Tail twitches'] == 'true') or (item['Tail twitches'] == 'True')
					obj.Approaches = (item['Approaches'] == 'true') or (item['Approaches'] == 'True')
					obj.Indifferent = (item['Indifferent'] == 'true') or (item['Indifferent'] == 'True')
					obj.Runs_from = (item['Runs from'] == 'true') or (item['Runs from'] == 'True')
					obj.save ()
				except Exception as e:
					raise CommandError(e)
		self.stdout.write(self.style.SUCCESS('Successfully read file "%s"' % path))