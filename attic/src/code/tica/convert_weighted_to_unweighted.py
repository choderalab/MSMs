import msmbuilder as msmb
import tables
import shutil

n_pairs_list = [100, 500, 1000, 2000, 4000]

for n_pairs in n_pairs_list:
    in_filename = "./tICAData%d-weighted.h5" % n_pairs
    out_filename = "./tICAData%d-unweighted.h5" % n_pairs
    shutil.copy(in_filename, out_filename)    
    f = tables.File(in_filename, 'a')  # Fix later
    f.root.timescale_weighted[0] = True
    f.close()
