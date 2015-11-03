from config import slack_token, db, output_file
from getslackdata import getslackdata
from geochart import GeoChart
import os


def main():

	if os.path.isfile("../config.py"):
		print "config.py not found"
		exit(1)

	# Store slack data to local SQLITE db
	getslackdata(slack_token, db)

	# Make output file with GeoChart
	map = GeoChart(db, output_file)
	map.makeChart()

	print "Done"

if __name__ == '__main__':
	main()