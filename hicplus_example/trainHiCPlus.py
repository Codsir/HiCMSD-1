import sys

sys.path.append('/home/tiger/HiC/HiCMSD/')
#sys.path.append('/home/tiger/Documents/hic_codes/hicplusplus/')

#import msdnet.trainMsdnet as msdtrain
from hicmsd.hicplus import trainhicplus as tmsd
import hicplus_config as config

#from msdnet
#import msdnet



tmsd.trainhicplus(config)

