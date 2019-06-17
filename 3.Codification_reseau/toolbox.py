# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os, os.path
from datetime import datetime, date
import pickle


def format_list_strings(string):
	res= list([])
	for s in string.split(","):
		aux= s.strip(" \n")
		if aux!='':
			aux= aux+"_E" if aux[-1].isupper() else aux + "_O"
			res.append(aux)
	return tuple(res)

def get_int(s):
	return (int(s) if s!="" else -1)

def get_float(s):
	if s=='':
		return -1
	else:
		return float(s)

def get_mean(series):
	positive_series= series.loc[series>=0]
	return positive_series.mean() if positive_series.shape[0]>0 else -1

def get_min(series):
	positive_series= series.loc[series>=0]
	return positive_series.min() if positive_series.shape[0]>0 else -1


def format_time(heure):
	return (datetime.strptime(heure,"%H:%M")).time()
