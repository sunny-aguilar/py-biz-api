#!/usr/bin/env python3
import reports
import datetime
import sys
import os


def get_paragraph_body():
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
    # create body paragraph
    data = ''
    for name, weight in zip(item_name, item_weight):
        data += '<br/><br/>name: ' + name + "<br/>weight: " + str(weight)

    return data

def get_title():
    # get date
    date_data = datetime.datetime.now()
    date_str = date_data.strftime('%b %d, %Y')
    # append date to report title
    report_title = 'Processed Update on ' + date_str
    return date_str


def main():
    # genereate a report by calling generate_report function
    attachment = '/tmp/processed.pdf'
    title = get_title
    paragraph = get_paragraph_body()
    reports.generate_report(attachment, title, paragraph)


if __name__ == "__main__":
    main()