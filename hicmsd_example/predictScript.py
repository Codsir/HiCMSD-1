

import sys

sys.path.append('/home/tiger/HiC/HiCMSD/')

from hicmsd.hicmsdnet import runMsdnet as rmsd
import hicmsd_config as config


input_dir = '/media/tiger/Biao/biodata/Generate_data_20181102/down_gm12878/MAP30_npy/'
outputdir = '/media/tiger/Biao/biodata/down_16/GM12878_nomin/hicmsd'
chrlist = [str(i) for i in range(18,23)]
#chrlist.append('X')

for chrN in chrlist:
	inputfile = input_dir + str(chrN) + '_10kb.matrix.npy'
	rmsd.runMsdnet(inputfile, outputfile, chrN, config)
