import sqlite3
import re
from chart_stub import html_source

class GeoChart(object):
	def __init__(self, database, outputfile="GeoChart.html"):
		self._db = sqlite3.connect(database)
		self._cursor =  self._db.cursor()
		self._file = outputfile
		self.locations = {}
		self.total = 0
		self.source = ""

	def makeChart(self):
		self._process_data()
		self._gen_html()

		with open(self._file, "w") as f:
			f.write(self.source)

		print "Checkout %s file to see the GeoChart"%self._file

	def _process_data(self):
		try:
			self._cursor.execute("""SELECT timezone,count(*) FROM timezones group by timezone""")
			self.rawdata = self._cursor.fetchall()

			for row in self.rawdata:
				# it column has valid data
				if row[0]:

					#Obtain proper city name #HACKY
					splitname = row[0].split('/')[-1]
					city = re.sub('_',' ',splitname)

					self.locations[ city ] = row[1]
					self.total +=  row[1]

		except Exception as e:
			print "DB read error for ", row,", type ,", type(e)


	def _gen_html(self):

		self._stub = ""
		for location,count in self.locations.items():
			percent = str(float(count*100)/self.total)[:3]
			self._row = ",\n['{0}',{1},{2}]".format(location, percent, count)
			self._stub += self._row

		self.source = html_source.format( self._stub )

if __name__ == '__main__':
	pass