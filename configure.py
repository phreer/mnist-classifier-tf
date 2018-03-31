TRAIN_IMGS_FILENAME = "../train_imgs_array.np"
TRAIN_LABELS_FILENAME = "../train_labels_onehot.np"
TEST_IMGS_FILENAME = "../test_imgs_array.np"
TEST_LABELS_FILENAME = "../test_labels_onehot.np"
LOG_DIR = "log/"
SAVE_DIR = "save/"
BATCH_SIZE = 32
LEARNING_RATE_INIT = 1e-3
WIDTH = 28
HEIGHT = 28
CHANNELS = 1
PADDING = 2
CLASS_NUM = 10
IS_TRAINING = True
KEEP_PROB = 0.5 if IS_TRAINING else 1
TRAIN_NUMS = 60000
TRAIN_KP = 0.5
BOOST_M = 3 # train 3 models to boost