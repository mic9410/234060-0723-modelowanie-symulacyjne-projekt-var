import pandas as pd
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime

def garch(data):
    a = DataReader('JPM', 'yahoo', datetime(2006, 6, 1), datetime(2016, 6, 1))
    print(a)

  