#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import reports
import datetime
import sys
import os


# generate report
def generate_report():
    # directory of description files
    directory = './supplier-data/descriptions/'
    files = os.listdir(directory)

    item_name = []
    item_weight = []

    # open each text file
    for file in files:
        with open(directory+file, 'r+') as current_file:
            desc = 0
            for line in current_file:
                # add fields to item dictionary
                if desc == 0:
                    item_name.append(line.strip())

                elif desc == 1:
                    # convert weight string to integer
                    item_weight.append(int(line[0:4].strip()))

                # go to next item in file
                desc += 1

    # print lists
    # print(f'{item_name}\n{item_weight}')

    # report name
    report_name = 'processed.pdf'

    # report object
    report = SimpleDocTemplate(report_name)

    # get styles
    styles = getSampleStyleSheet()

    # get date
    date_data = datetime.datetime.now()
    date_str = date_data.strftime('%b %d, %Y')
    # print(date_str)

    # add report title
    title = 'Processed Update on ' + date_str
    report_title = Paragraph(title, styles['h1'])

    # create body paragraph
    data = ''
    for name, weight in zip(item_name, item_weight):
        data += '<br/><br/>name: ' + name + "<br/><br/>" + str(weight)
        print(f'Data: {name}  {weight}')
    paragraph = Paragraph(data, styles["BodyText"])


    # generate report
    report.build([report_title, paragraph])




def main():
    # genereate a report by calling generate_report function
    generate_report()


if __name__ == "__main__":
    main()