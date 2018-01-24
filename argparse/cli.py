#!/usr/bin/python

import argparse

parser=argparse.ArgumentParser(description='Argument parsing test. Process some integers.')
parser.add_argument('integers',metavar='N',type=int,nargs='+',help='an integer for the accumulator')

parser.add_argument('-s','--sum',dest='sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args=parser.parse_args()

print(args.sum(args.integers))