import argparse
import json
import os
import requests
import sys
import random
from datetime import datetime
from pprint import pprint
from lib import headers, iot_list


class SherlockSight:
    def __init__(self, args):
        if args.auth:
            if os.path.exists('.apikey.auth'):
                exit("Active authentication detected. If you want to re-authenticate with another api key, delete/edit the current .apikey.auth file")
            else:
                with open('.apikey.auth', 'w') as file:
                    self.api_key = args.auth
                    file.write(self.api_key)
                    file.close()
                exit("api key is Successfully saved to the .apikey.auth file")
        else:
            with open('.apikey.auth', 'r') as file:
                self.api_key = file.readline().strip()

        self.api = 'https://api.criminalip.io'
        self.headers = {
            "x-api-key": self.api_key,
            "User-Agent": random.choice(headers.user_agents)
        }

        if args.ip:
            self.uri = '{}/v1/ip/data'.format(self.api)

            if args.full == 'Y' or args.full == 'y':
                f_option = 'true'
            elif args.full == 'N' or args.full == 'n':
                f_option = 'false'
            else:
                f_option = 'false'

            self.params = {
                "ip": args.ip,
                "full": f_option,
            }
            self.query_ip()
        elif args.query:
            self.uri = '{}/v1/banner/search'.format(self.api)

            self.offset = args.start if args.start else 0
            self.params = {
                "query": args.query,
                "offset": self.offset,
            }
            self.query_search()

        if args.list:
            self.iot_list()

        if args.read:
            self.read_file(args.read)

    def query_ip(self):
        response = requests.get(url=self.uri, params=self.params, headers=self.headers)
        response = response.json()
        pprint(response)

        if response['status'] == 200:
            if args.output:
                self.output(response)
            else:
                self_created_path = "log/{}_{}".format(datetime.now().strftime('%Y%m%d_%H%M%S'), args.ip)
                self.output(response, self_created_path)
        else:
            exit("'{}' is not found in Criminal IP".format(args.ip))

    def query_search(self):
        response = requests.get(url=self.uri, params=self.params, headers=self.headers)
        response = response.json()
        pprint(response)

        if response['status'] == 200:
            if args.output:
                self.output(response)
            else:
                self_created_path = "log/{}_{}".format(datetime.now().strftime('%Y%m%d_%H%M%S'), args.query.replace(" ", "_"))
                self.output(response, self_created_path)
        else:
            exit("'{}' is not found in Criminal IP".format(args.query))

    def iot_list(self):
        print("=== IoT query list ===")

        iot_query_list = []
        for i, d in enumerate(iot_list.iot_search_query):
            print("{} : {}".format(i+1, d))
            iot_query_list.append(d)

        selected_number = int(input("If you want to query right now, input the number : "))
        offset = input("Input the offset (criminal_ip returns data by 100) : ")

        try:
            offset = int(offset)
        except ValueError:
            offset = 0

        if selected_number == 1:
            cip_query = iot_list.iot_search_query[iot_query_list[0]]
        elif selected_number == 2:
            cip_query = iot_list.iot_search_query[iot_query_list[1]]
        elif selected_number == 3:
            cip_query = iot_list.iot_search_query[iot_query_list[2]]
        elif selected_number == 4:
            cip_query = iot_list.iot_search_query[iot_query_list[3]]
        elif selected_number == 5:
            cip_query = iot_list.iot_search_query[iot_query_list[4]]
        else:
            exit("Select one of the list. Thank you")

        print("copy and paste below query :\n")
        print("./cip -Q {} -S {}".format(cip_query, offset))
        print("")

    def output(self, result, self_created_path=None):
        if self_created_path:
            file_path = self_created_path
        else:
            file_path = "log/{}_{}".format(datetime.now().strftime('%Y%m%d_%H%M%S'), args.output)

        with open(file_path, "a") as file:
            file.write("{}".format(json.dumps(result)))
            file.close()

    def read_file(self, file):
        with open("log/{}".format(args.read), "r") as file:
            for r in file:
                pprint(json.loads(r))


parser = argparse.ArgumentParser(description='SherlockSight - by Aidennnn33')
parser.add_argument('-A', '--auth', help='api authentication with a valid criminalip.io api key', metavar='<api_key>')
parser.add_argument('-I', '--ip', help='return information of a target IP', metavar='<ip>')
parser.add_argument('-Q', '--query', help='text search query', metavar='<query>')
parser.add_argument('-F', '--full', help='return full(Y) or short information(N) of a target IP', metavar='<Y/N>')
parser.add_argument('-O', '--output', help='write output to a file', metavar='<path/to/file>')
parser.add_argument('-S', '--start', help='start number for search query', metavar='<start_number>')
parser.add_argument('-L', '--list', help='return IoT search query', metavar='<Y>')
parser.add_argument('-R', '--read', help='read file and pretty print the information', metavar='<path/to/file>')
parser.add_argument('-v', '--verbose', help='enable verbosity', action='store_true')

args = parser.parse_args()

