#!/bin/sh
# walltime : maximum wall clock time (hh:mm:ss)
#PBS -l walltime=99:00:00
#
# join stdout and stderr
#PBS -j oe
#
# spool output immediately
#PBS -k oe
#PBS -q gpu
#PBS -l nodes=1:ppn=1
#PBS -l mem=8GB
#
# export all my environment variables to the job
#PBS -V
#
# job name (default = name of script file)
#PBS -N myjob
#
# specify email for notifications
#PBS -M kyleabeauchamp@gmail.com
#
# mail settings (one or more characters)
# n: do not send mail
# a: send mail if job is aborted
# b: send mail when job begins execution
# e: send mail when job terminates
#PBS -m n
#
# filename for standard output (default = <job_name>.o<job_id>)
# at end of job, it is in directory from which qsub was executed
# remove extra ## from the line below if you want to name your own file
##PBS -o myoutput

# Change to working directory used for job submission
cd $PBS_O_WORKDIR

# start spark workers
ConvertDataToHDF.py -s system.pdb -i ../longtraj_symlinks_PROJ8900/ -S fah -a AtomIndices.dat  -t 10
