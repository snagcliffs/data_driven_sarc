import numpy as np
# import itertools
# import operator
# import sys
import os
import pandas as pd

def LoadData(datapath, verbose = False):

	sarc_list = {}
	count = 0

	for dirpath, dirnames, filenames in os.walk(datapath):
	    for file in filenames:
	        	        
	        if 'data.json' in file:
	            
	            count = count+1
	            
	            # get meta info
	            path = os.path.join(datapath, file.split('.')[0]+'.meta.json')
	            meta = pd.read_json(path)
	            description = [float(j) for j in meta['actin_permissiveness_args'][0][1:-1].split(',')]    
	            period = description[0]
	            phase = description[1]
	            span = description[2]
	            half_life = description[4]
	            
	            # read in data
	            path = os.path.join(datapath, file)
	            if (period, phase, span, half_life) in sarc_list:
	                sarc_list[(period, phase, span, half_life)].append(pd.read_json(path))
	            else: sarc_list[(period, phase, span, half_life)] = [pd.read_json(path)]
	                
	            if count % 1000 == 0 and verbose: print(count)

	return sarc_list

def MovingAve(x, m):
    n = len(x)
    xs = np.zeros(n-2*m)
    for j in range(n-2*m):
        xs[j] = np.mean(x[j:j+2*m])
    return xs