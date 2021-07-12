import argparse
import pandas as pd
import numpy as np
import os
import sys
from matplotlib import pyplot as plt

PRECLEARANCE_STATES = ["Alabama", "Alaska", "Arizona", "Georgia", "Louisiana", "Mississippi", "South Carolina", "Texas", "Virginia"]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_path', default='data_digits_8_vs_9_noisy')
    parser.add_argument('--n_rows', type=int, default=3)
    parser.add_argument('--n_cols', type=int, default=3)
    parser.add_argument('--example_ids_to_show', type=str, default='0,1,2,3,4,5,6,7,8')
    args = parser.parse_args()
