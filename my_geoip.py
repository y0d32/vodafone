#!/usr/bin/python3


import sys
import json
import re
import csv
import argparse

# Handle Python 2 and 3 compatibility for urllib
try:
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen

def getData(filenames, sortByCount):
  """
  The given file is scraped for IPv4 addresses, and the addresses are used
  with the GeoIP location provider to obtain location data in JSON format.
  The JSON data is then parsed and appended to the 'results' list.
  """

  addresses = []
  filteredAddresses = []
  results = []

  for filename in filenames:
    try:
      f = open(filename, 'r')
    except IOError:
      print ('Could not find the specified file:', filename)
      sys.exit(1)

    # Parse file for valid IPv4 addresses via RegEx
    addresses += re.findall(r'(\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b)',f.read())
    f.close()

  # Count number of occurrences for each IP address
  addressCounts = {i:addresses.count(i) for i in addresses}

  # Remove duplicates from list
  addresses = set(addresses)

  # Filter list to eliminate bogon addresses, the loopback network, link local addresses, and RFC 1918 ranges; add results to new list
  for address in addresses:
    if not (re.match(r'^0.\d{1,3}.\d{1,3}.\d{1,3}$|^127.\d{1,3}.\d{1,3}.\d{1,3}$|^169.254.\d{1,3}.\d{1,3}$|^10.\d{1,3}.\d{1,3}.\d{1,3}$|^172.(1[6-9]|2[0-9]|3[0-1]).[0-9]{1,3}.[0-9]{1,3}$|^192.168.\d{1,3}.\d{1,3}$', address)):
      filteredAddresses.append(address)

  # Iterate through new list and obtain GeoIP information from ipinfo.io
  for filteredAddress in filteredAddresses:
    formattedData = ''
    # Build query URL from found addresses
    url = ('https://ipinfo.io/' + filteredAddress + '/json')

    try:
      rawData = urlopen(url).read()
      rawData = json.loads(rawData.decode('utf-8'))
    except:
      print ('Error parsing address:', filteredAddress)
      sys.exit(1)

    keys = ['ip','hostname','country','region','city','postal','loc','org']

    for key in keys:
      try:
        # If the key exists but is null, set its value to 'N/A'
        if (rawData[key] == ""):
          rawData[key] = 'N/A'

        # If the key is loc, add a trailing comma to the end of the value
        if (key == 'loc'):
          formattedData += rawData[key] + ','
        # If the key is anything else, strip the commas from the value, then add a trailing comma to the end of the value
        else:
          formattedData += rawData[key].replace(',','') + ','

      except:
        # If the loc key is missing, add 'N/A,N/A' and a trailing comma
        if (key == 'loc'):
          formattedData += 'N/A,N/A,'
        # If any other key is missing, add 'N/A' and a trailing comma
        else:
          formattedData += 'N/A,'

    # Get number of occurrences for IP address and add to results
    addressCount = addressCounts[filteredAddress]
    formattedData += str(addressCount)

    # Add final formatted data string to list
    results.append(formattedData)

  if (sortByCount == 1):
    # Sort addresses by count (descending)
    results  = sorted(results, key=lambda x: int(x.split(',')[9]), reverse=True)

  # Add column headers
  results.insert(0,'IP Address,Hostname,Country,Region,City,Postal Code,Latitude,Longitude,ASN,Count')

  return results

def printData(results):
  # The Python 2 csv module does not support Unicode, so ignore anything that isn't ASCII text
  #resultsNoUnicode = [result.encode('ascii','ignore') for result in results]

  rows = list(csv.reader(results))
  widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

  for row in rows:
    print(' | '.join(cell.ljust(width) for cell, width in zip(row, widths)))

def writeData(results,outfile):
  try:
    f = open(outfile, 'w')
  except IOError:
    print ('Could not write the specified file:', outfile)
    sys.exit(1)

  for result in results:
    # While Unicode characters will not be displayed via stdout, they will be written to the file
    f.write(result + '\n')

  f.close()

def main():
  parser = argparse.ArgumentParser(description='A GeoIP lookup utility utilizing ipinfo.io services.', usage='my_geoip.py filename(s) [-w outfile] [-s]', add_help=False)
  parser.add_argument('filenames', nargs="*")
  parser.add_argument('-w', '--write', help='Write output to CSV file instead of stdout', required=False)
  parser.add_argument('-s', '--sort-by-count', action='store_true', help='Sort addresses by count (descending)', required=False)
  parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
  args = vars(parser.parse_args())

  # Make sure at least one filename was provided
  if not (args['filenames']):
    parser.print_usage()
    parser.exit()

  filenames = args['filenames']
  writeToFile = 0
  sortByCount = 0

  if (args['write']):
    writeToFile = 1
    outfile = args['write']

  if (args['sort_by_count']):
    sortByCount = 1

  output = getData(filenames,sortByCount)

  if (writeToFile == 1):
    writeData(output,outfile)

  else:
    printData(output)


if __name__ == '__main__':
  main()
