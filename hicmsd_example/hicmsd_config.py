
from hicmsd.hicmsdnet import msdmodel_l30_4last as msdmodel

msdmodel = msdmodel
lowdata_dir = '../data_process_example/data/train_low.npz'
highdata_dir = '../data_process_example/data/train_high.npz'
lowtest_dir = '../data_process_example/data/test_low.npz'
hightest_dir = '../data_process_example/data/test_high.npz'
modelsave_dir = './model/'
trained_model_dir = './model/pytorch_hg19_model_200'
log_dir = './log/log.txt'
use_gpu = 1
epochs = 200
batch_size = 128
learning_rate = 0.0005
num_layers = 30
growth_rate = 1
kernel_size = 3
size_diff = 13
dilation_mod = 10
down_sample_ratio = 16
max_value = None
device_ids = [0]
subImage_size = 80
step = 35
input_resolution = 10000


