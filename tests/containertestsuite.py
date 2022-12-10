#!/usr/bin/env python3
"""
executes container test suite
"""
import argparse
import sys
sys.path.append('../')
import setup,run,apptest,destroy

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--container', '-c', help='container image name', required=True)
    parser.add_argument('--testname', '-t', help='Enter one of the testname setup|run|destroy|all', required=True)

    try:
        args = parser.parse_args()
        container = args.container
        testname  = args.testname
    except:
        parser.print_usage()
        sys.exit(0)

    