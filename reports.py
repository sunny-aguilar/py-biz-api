#!/usr/bin/env python3
import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import sys
import os


# generate report
def generate_report():
    # directory of description files
    directory = './supplier-data/descriptions/'
    files = os.listdir(directory)

    item_name = ''
    item_weight = 0

    # open each text file
    for file in files:
        with open(directory+file, 'r+') as current_file:
            desc = 0
            for line in current_file:
                # add fields to item dictionary
                if desc == 0:
                    item_name = line.strip()

                elif desc == 1:
                    # convert weight string to integer
                    item_weight = int(line[0:4].strip())

                # go to next item in file
                desc += 1


    # report name
    report_name = 'processed.pdf'

    # report object
    report = SimpleDocTemplate(report_name)

    # get styles
    styles = getSampleStyleSheet()

    # get date
    date_data = datetime.datetime.now()
    date_str = date_data.strftime('%b %d, %Y')
    print(date_str)

    # add report title
    report_title = Paragraph('Processed Update on ', date_str, styles['h1'])


def main(argv):
    # genereate a report by calling generate_report function
    generate_report()


if __name__ == "__main__":
    main(sys.argv)