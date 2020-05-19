#!/usr/bin/env python3
import shutil
import psutil
import sched
import time
import os
import sys
import socket
import emails


starttime=time.time()
while True:
    print("tick")
    # report an error if CPU usage is over 80%
    usage = psutil.cpu_percent()
    if usage > 5:
        print(usage, '% CPU usage')
        # send email

    # report an error if available disk space is lower than 20%
    disk_usage = psutil.disk_usage('./')
    free_disk_space = 100 - disk_usage[3]
    if free_disk_space < 20:
        print(free_disk_space, '%')
        # send email

    # report an error if available memory is less than 500MB
    memory = psutil.virtual_memory()
    mem_avail = memory[1]/1024
    mem_avail = mem_avail/1024
    print(mem_avail, 'MB free disk space')
    if mem_avail < 500:
        print(mem_avail, 'MB')

    # report an error if the host name 'localhost' cannot be resolved to '127.0.0.1'
    s = socket.gethostbyname(socket.gethostname())
    print(s)
    if s is not '127.0.0.1':
        print('Unresolved localhost')
        # send email


    time.sleep(2.0 - ((time.time() - starttime) % 2.0))



def main():
    sender = 'automation@example.com'
    recipient = 'student-01-fb6b4f12e8ed@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'Please check your system and resolve the issue as soon as possible.'
    attachment_path = '/tmp/processed.pdf'
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)

if __name__ == "__main__":
    main()