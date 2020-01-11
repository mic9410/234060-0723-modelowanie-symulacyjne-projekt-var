import numpy as np
import pandas as pd
import os
from data_manipulation import garch

data_files = os.listdir('data')

for file_name in data_files:
    rare_data = pd.read_csv('data/' + file_name)
    calculated_garch = garch(rare_data)