import os
import csv
from django.core.management.base import BaseCommand, CommandError
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
			reader = csv.reader (f, delimiter=',',quotechar="\"")
			first = True
			for row in reader:
				if first:
					first = False
					continue
				try:
					obj = Squirrel()
					obj.Latitude = float(row[1])
					obj.Longitude = float(row[0])
					obj.Unique_Squirrel_ID = row[2]
					obj.Shift = row[4]
					date = row[5][4:] + '-' + row[5][:2] + '-' + row[5][2:4]
					obj.Date = date
					obj.Age = row[7]
					obj.Primary_Fur_Color = row[8]
					obj.Location = row[12]
					obj.Specific_Location = row[14]
					obj.Running = (row[15] == 'true')
					obj.Chasing = (row[16] == 'true')
					obj.Climbing = (row[17] == 'true')
					obj.Eating = (row[18] == 'true')
					obj.Foraging = (row[19] == 'true')
					obj.Other_Activities = row[20]
					obj.Kuks = (row[21] == 'true')
					obj.Quaas = (row[22] == 'true')
					obj.Moans = (row[23] == 'true')
					obj.Tail_flags = (row[24] == 'true')
					obj.Tail_twitches = (row[25] == 'true')
					obj.Approaches = (row[26] == 'true')
					obj.Indifferent = (row[21] == 'true')
					obj.Runs_from = (row[27] == 'true')
					obj.save ()
				except Exception as e:
					raise CommandError(e)
		self.stdout.write(self.style.SUCCESS('Successfully read file "%s"' % path))