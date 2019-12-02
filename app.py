import argparse
from src import *

def get_parser():
    parser = argparse.ArgumentParser(description='wallet-care')
    parser.add_argument('-e', '--expense', help='expense microservice', action='store_true')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    arguments = vars(parser.parse_args())

    controller.config.service_start(arguments)
    controller.config.app.run(port=5002)