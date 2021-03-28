'''
Austin Richards 3/28/21

download_forms.py uses the ezsheets module to download
data from a google sheet that contains google form data.
It then finds the emails and returns them as a list.
'''
import logging as log
import ezsheets as sheets

log.basicConfig(level=log.DEBUG, format='%(asctime)s : %(message)s')


def get_form_emails(form_id):
    ss = sheets.Spreadsheet(form_id)
    sheet = ss[0]

    emails = sheet.getColumn(3)
    emails = [i for i in emails[1:] if i] # remove first row, empty values
    return emails


formID = '1NZV2fZTKfVR_eIpVzq8iPyYbLhqxm_evqBnLzCH_jq4'
get_form_emails(formID)