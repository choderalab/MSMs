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
6.  BuildMSM and extract strongly connected component.  Build a new project that includes ONLY the trajectory chunks that are strongly connected.  This step of protocol is not present in most MSM pipelines but may be useful for achieving accurate clusterings of datasets built from homology model simulations, some of which are possibly garbage.  Preliminary script to do this is goodtrim.py
7.  Recluster final trimmed dataset.



TICA
----

1.  python generate_atom_pairs.py
2.  tICA_train.py -d 1 atompairs -a AtomPairs.dat
3.  Cluster.py -p ProjectInfo.yaml -o TICA tica -f tICAData.h5 -n 7 kcenters -k 100


Cluster.py -p ProjectInfo.yaml -o TICA tica -f tICAData.h5 -n 7 kcenters -k 200
BuildMSM.py -l 1 -a TICA/Assignments.h5 -o TICA/
PCCA.py -a TICA/Assignments.Fixed.h5 -n 6 -t TICA/tProb.mtx  -o TICA6 -A PCCA+
BuildMSM.py -l 1 -a TICA6/MacroAssignments.h5 -o TICA6/
SaveStructures.py -a TICA6/Assignments.Fixed.h5 -c 4 -s -1 -o TICA6/PDBs
