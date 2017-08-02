import os
import glob
import sys
import numpy as np
import scipy
import scipy.io.wavfile
from scikits.talkbox.features import mfcc

from utilities import GENRE_DIR, CHART_DIR, GENRE_LIST

def write_ceps(ceps, fn):
    """
    MFCC to separate files for speeding up the process.
    """
    base_fn, ext = os.path.splitext(fn)
    data_fn = base_fn + ".ceps"
    np.save(data_fn, ceps)
    print "Written ", data_fn


def create_ceps(fn):
    """
        Creating the MFCC features.
    """    
    sample_rate, X = scipy.io.wavfile.read(fn)
    X[X==0]=1
    ceps, mspec, spec = mfcc(X)
    write_ceps(ceps, fn)


def read_ceps(genre_list, base_dir=GENRE_DIR):
    """
        Reading the MFCC features and returning them in a numpy array.
    """
    X = []
    y = []
    for label, genre in enumerate(genre_list):
        for fn in glob.glob(os.path.join(base_dir, genre, "*.ceps.npy")):
            ceps = np.load(fn)
            num_ceps = len(ceps)
            X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
            y.append(label)
    return np.array(X), np.array(y)


def create_ceps_test(fn):
    """
        Creating the MFCC features from the test files, saving them to disk and returning the saved file name.
    """
    sample_rate, X = scipy.io.wavfile.read(fn)
    X[X==0]=1
    np.nan_to_num(X)
    ceps, mspec, spec = mfcc(X)
    base_fn, ext = os.path.splitext(fn)
    data_fn = base_fn + ".ceps"
    np.save(data_fn, ceps)
    print "Written ", data_fn
    return data_fn


def read_ceps_test(test_file):
    """
        Reading the MFCC features from test file and returning them in a numpy array.
    """
    X = []
    y = []
    ceps = np.load(test_file)
    num_ceps = len(ceps)
    X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
    return np.array(X), np.array(y)


if __name__ == "__main__":
    import timeit
    start = timeit.default_timer()
    for subdir, dirs, files in os.walk(GENRE_DIR):
        traverse = list(set(dirs).intersection( set(GENRE_LIST) ))
        break
    print "Working with these genres --> ", traverse
    print "Starting ceps generation"     
    for subdir, dirs, files in os.walk(GENRE_DIR):
        for file in files:
            path = subdir+'/'+file
            if path.endswith("wav"):
                tmp = subdir[subdir.rfind('/',0)+1:]
                if tmp in traverse:
                    create_ceps(path)
                    
    stop = timeit.default_timer()
    print "Total ceps generation and feature writing time (s) = ", (stop - start) 








#^^^()()^^^










