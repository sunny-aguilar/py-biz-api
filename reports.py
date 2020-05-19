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