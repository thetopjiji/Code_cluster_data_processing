import os
import sys
import shutil
import getopt

##delete and rebuild the output
shutil.rmtree('output')
os.mkdir('output')
##delete and rebuild the error
shutil.rmtree('error')  
os.mkdir('error')
##delete EDGF

shutil.rmtree('instances')  
os.mkdir('instances')


def copyFiles(src,dest):
	src_files = os.listdir(src)
	for file_name in src_files:
    		full_file_name = os.path.join(src, file_name)
    		if (os.path.isfile(full_file_name)):
        		shutil.copy(full_file_name, dest)


fhfn=file("fn.txt",'w')
for f in os.listdir("original_ins"):
	print>>fhfn,'%s'%(f)
copyFiles("original_ins","instances")

dict_cpu={0:'',1:'#SBATCH --partition=amd-opteron-4184',2:'#SBATCH --partition=amd-opteron-6134', 3:'#SBATCH --partition=intel-E5-2695',4:'#SBATCH --partition=intel-E5-2670'}

# 0:19, 1:5, 2:5, 3:2, 4:7


dict1 =	{'A-randomA1.rmf':866968, 'A-randomA2.rmf':6522206, 'A-randomA3.rmf':14194583, 'A-randomA4.rmf':1717176, 'A-randomG4.rmf':140211,
'B-bintree10.rmf':3696, 'B-hc10.rmf':523776, "B-mesh33x33.rmf":31729, 
'C-3elt.rmf':357329, 'C-airfoil1.rmf':272931, 'C-whitaker3.rmf':1143645,
'D-c1y.rmf':62230,'D-c2y.rmf':78757,'D-c3y.rmf':123145,'D-c4y.rmf':114936,'D-c5y.rmf':96850,
'gd95c.rmf':506, 'gd96a.rmf':95242, 'gd96b.rmf':1416, 'gd96c.rmf':519, 'gd96d.rmf':2391}

def main(argv):
	time=""
	memory=""
	cpu=0
	lim=0
	try:
		opts, args = getopt.getopt(argv,"l:t:m:c:h",["time=","memory=","cpu=","limi="])
	except getopt.GetoptError:
		print 'name.py -t time -m memory -c cpu'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'name.py -t time -m memory -c cpu'
			sys.exit()
		elif opt in ("-t", "--time"):
			time = arg
		elif opt in ("-m", "--memory"):
			memory = arg
		elif opt in ("-c", "--cpu"):
			cpu = int(arg)
		elif opt in ("-l", "--limi"):
			lim = int(arg)

	cppname='exe_cpp/LS_minLA.cpp exe_cpp/MLA_addfun.cpp exe_cpp/MLA_search.cpp exe_cpp/McAllistar_ini.cpp exe_cpp/SDX.cpp'
	exename='MLA_1'
#	cmd1='srun g++ %s -O3 -lm -Wall -o %s'%(cppname,exename)
	cmd1='srun --partition=intel-E5-2670 g++ %s -O3 -lm -Wall -o %s'%(cppname,exename)
	os.system(cmd1)

	instancedir='instances'
	filesubmit="mem1_minla.sh"

	ll=0
	for fn in os.listdir(instancedir): 
		ll = ll+1
	print ll

	prefix="""#!/bin/bash
#SBATCH -N 1
#SBATCH --mem-per-cpu=%s
#SBATCH --time=%s
#SBATCH --array=0-%d
#SBATCH -o output/%%A-%%a.out
#SBATCH -e error/%%A-%%a.err
#SBATCH --mail-type=end,fail
#SBATCH --mail-user=rjtkxj@gmail.com
%s
	"""%(memory,time,ll*lim-1,dict_cpu[cpu])

	start_fix="""
case $SLURM_ARRAY_TASK_ID in
"""

	finish_fix="""
esac
"""
	surfix="""
srun MLA_1 $ARGS
"""


	fhandle=file(filesubmit,'w')
	print>>fhandle,prefix
	print>>fhandle,start_fix
	count=0
	for f in os.listdir(instancedir):
		for i in range(lim):
			print>>fhandle,'	%d) ARGS="-i %s --seed %d -rep %d -alb %d -L1 %d -L2 %d -L3 %d -p %d";;'%(count, instancedir+'/'+f, i*10, i, 0, 100, 20, 30,20)
			count=count+1
	print count

	print>>fhandle,finish_fix
	print>>fhandle,surfix

	fhandle.close()

	os.popen("chmod u+x %s"%filesubmit)

if __name__ == "__main__":
	main(sys.argv[1:])
