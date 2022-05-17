# coding=utf-8

# imports
import os
import csv
import time
import datetime

import pickle
import numpy as np
import pandas as pd

from tqdm import tqdm
from google import colab
import ipywidgets as widgets

from IPython.core.display import clear_output
import matplotlib.pyplot as plt

class DeepLearningRealTimeTrainMonitoring():
  # 
  def __init__(self, endpoint, separator=';', reload_time=10, preview_size=450):
    # class constants
    self.ENDPOINT = endpoint
    self.HISTORY_FILE = endpoint + 'history.csv'
    self.GENERATED = endpoint + 'generated/'
    self.SEPARATOR = separator
    self.PREVIEW_SIZE = preview_size

    # class variables
    self.reload_time = reload_time

    # create interface
    self.interface = self.get_interface()

  def get_interface(self):
    w = widgets.FloatLogSlider(
        value=10,
        base=10,
        min=-10, # max exponent of base
        max=10, # min exponent of base
        step=0.2, # exponent step
        description='Log Slider'
    )
    return w

# s = DeepLearningRealTimeMonitoring(endpoint='')
# display(s.interface)
