#!/usr/bin/env python3
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Author:       Sandro Aguilar
# Date:         May 12, 2020
# Project:      C
#
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import sys
import os


# generate report
def generate_report(attachment, title, paragraph):
    # report object
    report = SimpleDocTemplate(attachment)

    # get styles
    styles = getSampleStyleSheet()

    # add report title
    title = Paragraph(title, styles['h1'])

    # add body paragraph
    paragraph = Paragraph(paragraph, styles["BodyText"])

    # generate report
    report.build([title, paragraph])