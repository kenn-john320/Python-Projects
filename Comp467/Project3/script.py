import argparse
import pymongo
import pprint as pp
import csv


parser = argparse.ArgumentParser(description="")

parser.add_argument("--process")
parser.add_argument("--output")
args = parser.parse_args()