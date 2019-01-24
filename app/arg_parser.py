import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Find Words")
    parser.add_argument('-w')
    parser.add_argument('-l', type=int, default=4)
    parser.add_argument('-a', action='store_true')
    return parser.parse_args()
