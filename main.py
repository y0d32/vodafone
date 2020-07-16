#from data_structures.datacenter import Datacenter
import pandas
import urllib.request
import json
import time


URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"

def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    iterations = 0

    try:

        with urllib.request.urlopen(URL) as url:
            data = json.loads(url.read().decode())
            #print(data)
            #save data if required for audit
            # with open('dc.json', 'w') as json_file:
            #     json.dump(data, json_file)
            return data

    except Exception as e:
        while iterations < max_retries:
            with urllib.request.urlopen(URL) as url:
                data = json.loads(url.read().decode())
                #print(data)
                #save the data if required
                with open('dc.json', 'w') as json_file:
                    json.dump(data, json_file)
                return data
                if data:
                    break

            time.sleep(delay_between_retries)
            iterations += 1

def show_indices(obj, indices):
    for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
        if isinstance(v, (dict, list)):
            yield from show_indices(v, indices + [k])
        else:
            yield indices + [k], v



def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    # for keys, v in show_indices(data, []):
    #     print(keys, v)

    for  k, v in data.items():
        print("Here is a DataCenter: " + k)
        print("Here is what the datacenter contains: " + str(v))
        for x, i in v.items():
            print("Here is a Cluster: " + x)
            print("Here is  what the cluster contains: " + str(i))

if __name__ == '__main__':
    main()
