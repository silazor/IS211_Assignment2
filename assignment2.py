
# Import modules for features not supported by base python install

import urllib.request
import csv
import codecs
import datetime
import logging
import argparse
import sys

def downloadDATA(url):
    '''
    Create the downloadDATA function

    Use urllib.request ( urllib2 really ) to instantiate the
    csvstream variable

    use csv.reader to read from the csvstream and put it in the variable
    csv_data
    turn it into a list with list()
    return data
    '''
    print(url)
    #raise Exception('spam', 'eggs')
    csvstream = urllib.request.urlopen(url)
    csv_data = csv.reader(codecs.iterdecode(csvstream, 'utf-8'))
    data = list(csv_data)
    return data

def processData(url_data):
    '''
    Create the processData function that takes in the csv_data
    from downloadDATA

    Loop through the array and access the values
    0 - ID
    1 - name
    2 - date
    Validate the date using dateTime
    '''
    counter = 0
    valid_data = {}
    assignment2 = get_logger()
    for data in url_data:
        counter += 1
        #print(data[2])
        # The csv files first line is a header file, we need to skip it
        if data[2] == 'birthday':
            continue
        try:
            new_datetime = datetime.datetime.strptime(data[2], '%d/%m/%Y')
            valid_data[counter] = (data[1], new_datetime)
        except ValueError:
            assignment2.error('Error processing line %s for ID %s', counter, data[0])
            #print(ValueError("Incorrect data format, should be DD/MM/YYYYY"))
    return valid_data

def get_logger():
    logging.basicConfig(filename='errors.log', level=logging.ERROR)
        #format = 'Error processing line %(linenum)s for ID %(id)d')
    logger=logging.getLogger(__name__)
    return logger

def displayPerson(id, personData):
    int_id=int(id)
    if int_id in personData:
        print(f'Person {int_id} is {personData[int_id][0]} with a birthday of {personData[int_id][1].strftime("%Y-%m-%d")}')
    else:
        print("No user found with that id")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    url = args.url

    try:
        csv_data = downloadDATA(url)
    except Exception as e:
        sys.exit(f"Innappropriate Error Message {e}")
    personData = processData(csv_data)
    id = input("Enter ID to lookup ")
    #TODO:  Validate id ( it can't be 0 or negative)
    if int(id) > 0:
        displayPerson(id, personData)
    else:
        sys.exit()

if __name__ == "__main__":
    while True:
        main()
