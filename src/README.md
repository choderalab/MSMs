Src Kinase
====

FAH Core17 Project 8900

Instructions
------------

1.  Rsync data from FAH server to cluster: 171.64.65.69:/home/server.171.64.65.69/server2/data/SVR42734182/PROJ8900/ to sd.cbio.mskcc.org:/cbio/jclab/projects/fah/fah-data/PROJ8900
2.  Extract data from bzip2 files using code/fahprocessing/extract_xtc.py.  Note that you must manually edit this script to input various parameters.
3.  Make a directory of symlinks that ignores trajectories that are too short using using code/fahprocessing/make_symlinks.py 
Note: MSMBuilder's ConvertDataToHDF.py also handles this, but requires actually *reading* the trajectories to determine their length.  This makes the current MSMB approach way too slow for our dataset.  See issue 326 on msmbuilder GitHub.
4.  Submit code/fahprocessing/convert.sh to the queue, which will build the msmbuilder project using ConvertDataToHDF.py
5.  Cluster using protocol to be determined by KAB
