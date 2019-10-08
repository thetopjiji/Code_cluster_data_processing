#!/sur/bin/python
#generate the file of syntexe

import os
import math
import cmath
import sys
import getopt
import shutil 

def usage():
	print """'-p'+number of rotation degrees 
for exemple: -p 30"""


num_file=50
##The dictionary of the best
dict1 =	{'path20.rnd':1,'path25.rnd':1,'path30.rnd':1,
	 'path35.rnd':1,'path40.rnd':1,'path100.rnd':1,
      	 'path125.rnd':1,'path150.rnd':1,'path175.rnd':1,
	 'path200.rnd':1,'path300.rnd':1,'path475.rnd':1,
	 'path650.rnd':1,'path825.rnd':1,'path1000.rnd':1,
	 'cycle20.rnd':1,'cycle25.rnd':1,'cycle30.rnd':1,
	 'cycle35.rnd':1,'cycle40.rnd':1,'cycle100.rnd':1,
	 'cycle125.rnd':1,'cycle150.rnd':1,'cycle175.rnd':1,
	 'cycle200.rnd':1,'cycle300.rnd':1,'cycle475.rnd':1,
	 'cycle650.rnd':1,'cycle825.rnd':1,'cycle1000.rnd':1,
	 'mesh2D5x4.rnd':4,'mesh2D5x5.rnd':5,'mesh2D5x6.rnd':5,
	 'mesh2D5x7.rnd':5,'mesh2D5x8.rnd':5,'mesh2D10x10.rnd':10,
	 'mesh2D5x25.rnd':5,'mesh2D10x15.rnd':10,'mesh2D7x25.rnd':7,
	 'mesh2D8x25.rnd':8,'mesh2D15x20.rnd':15,'mesh2D19x25.rnd':19,
	 'mesh2D25x26.rnd':19,'mesh2D28x30.rnd':28,'mesh2D20x50.rnd':20,
	 'mesh3D4x4x4.rnd':14,'mesh3D5x5x5.rnd':21,'mesh3D6x6x6.rnd':30,
	 'mesh3D7x7x7.rnd':40,'mesh3D8x8x8.rnd':52,'mesh3D9x9x9.rnd':65,
	 'mesh3D10x10x10.rnd':80,'mesh3D11x11x11.rnd':96,'mesh3D12x12x12.rnd':114,'mesh3D13x13x13.rnd':133,
	 'tree2x4.rnd':4,'tree3x3.rnd':7,'tree10x2.rnd':28,
	 'tree3x4.rnd':15,'tree5x3.rnd':26,'tree13x2.rnd':46,
	 'tree2x7.rnd':19,'tree17x2.rnd':77,'tree21x2.rnd':116,
	 'tree25x2.rnd':163,'tree5x4.rnd':98,'tree2x9.rnd':57,
	 'caterpillar3.rnd':3,'caterpillar4.rnd':3,'caterpillar5.rnd':4,
	 'caterpillar6.rnd':5,'caterpillar7.rnd':6,'caterpillar13.rnd':10,
	 'caterpillar14.rnd':11,'caterpillar16.rnd':13,'caterpillar17.rnd':14,
	 'caterpillar19.rnd':15,'caterpillar23.rnd':19,'caterpillar29.rnd':24,
	 'caterpillar35.rnd':29,'caterpillar39.rnd':33,'caterpillar44.rnd':37,
	 'hypercube11.rnd':526,'hypercube12.rnd':988,'hypercube13.rnd':1912,
	 'can_24.mtx.rnd':5,'jgl009.mtx.rnd':4,'jgl011.mtx.rnd':5,'rgg010.mtx.rnd':5,
	 'A-pores_1.mtx.rnd':7,'B-ibm32.mtx.rnd':9,'C-bcspwr01.mtx.rnd':4,
	 'D-bcsstk01.mtx.rnd':12,'E-bcspwr02.mtx.rnd':7,'F-curtis54.mtx.rnd':8,
	 'G-will57.mtx.rnd':6,'H-impcol_b.mtx.rnd':17,'I-ash85.mtx.rnd':9,
	 'J-nos4.mtx.rnd':10,'K-dwt__234.mtx.rnd':12,'L-bcspwr03.mtx.rnd':11,
	 'M-bcsstk06.mtx.rnd':49,'N-bcsstk07.mtx.rnd':50,'O-impcol_d.mtx.rnd':38,
	 'P-can__445.mtx.rnd':47,'Q-494_bus.mtx.rnd':46,'R-dwt__503.mtx.rnd':44,
	 'S-sherman4.mtx.rnd':29,'T-dwt__592.mtx.rnd':30,'U-662_bus.mtx.rnd':52,
	 'V-nos6.mtx.rnd':22,'W-685_bus.mtx.rnd':36,'X-can__715.mtx.rnd':60}

##The dictionary of Tabu
dict2 =	{'path20.rnd':1,'path25.rnd':1,'path30.rnd':1,
	 'path35.rnd':1,'path40.rnd':1,'path100.rnd':1,
      	 'path125.rnd':1,'path150.rnd':1,'path175.rnd':1,
	 'path200.rnd':1,'path300.rnd':1,'path475.rnd':1,
	 'path650.rnd':3,'path825.rnd':4,'path1000.rnd':8,
	 'cycle20.rnd':1,'cycle25.rnd':1,'cycle30.rnd':1,
	 'cycle35.rnd':1,'cycle40.rnd':1,'cycle100.rnd':1,
	 'cycle125.rnd':1,'cycle150.rnd':1,'cycle175.rnd':1,
	 'cycle200.rnd':1,'cycle300.rnd':1,'cycle475.rnd':3,
	 'cycle650.rnd':4,'cycle825.rnd':7,'cycle1000.rnd':8,
	 'mesh2D5x4.rnd':4,'mesh2D5x5.rnd':5,'mesh2D5x6.rnd':5,
	 'mesh2D5x7.rnd':5,'mesh2D5x8.rnd':5,'mesh2D10x10.rnd':10,
	 'mesh2D5x25.rnd':5,'mesh2D10x15.rnd':11,'mesh2D7x25.rnd':7,
	 'mesh2D8x25.rnd':8,'mesh2D15x20.rnd':16,'mesh2D19x25.rnd':20,
	 'mesh2D25x26.rnd':26,'mesh2D28x30.rnd':29,'mesh2D20x50.rnd':22,
	 'mesh3D4x4x4.rnd':14,'mesh3D5x5x5.rnd':21,'mesh3D6x6x6.rnd':30,
	 'mesh3D7x7x7.rnd':40,'mesh3D8x8x8.rnd':52,'mesh3D9x9x9.rnd':65,
	 'mesh3D10x10x10.rnd':80,'mesh3D11x11x11.rnd':108,'mesh3D12x12x12.rnd':433,'mesh3D13x13x13.rnd':551,
	 'tree2x4.rnd':4,'tree3x3.rnd':7,'tree10x2.rnd':28,
	 'tree3x4.rnd':15,'tree5x3.rnd':26,'tree13x2.rnd':46,
	 'tree2x7.rnd':19,'tree17x2.rnd':77,'tree21x2.rnd':116,
	 'tree25x2.rnd':163,'tree5x4.rnd':98,'tree2x9.rnd':57,
	 'caterpillar3.rnd':3,'caterpillar4.rnd':3,'caterpillar5.rnd':4,
	 'caterpillar6.rnd':5,'caterpillar7.rnd':6,'caterpillar13.rnd':10,
	 'caterpillar14.rnd':11,'caterpillar16.rnd':13,'caterpillar17.rnd':14,
	 'caterpillar19.rnd':15,'caterpillar23.rnd':19,'caterpillar29.rnd':24,
	 'caterpillar35.rnd':29,'caterpillar39.rnd':33,'caterpillar44.rnd':37,
	 'hypercube11.rnd':548,'hypercube12.rnd':1224,'hypercube13.rnd':2810,
	 'can_24.mtx.rnd':5,'jgl009.mtx.rnd':4,'jgl011.mtx.rnd':5,'rgg010.mtx.rnd':5,
	 'A-pores_1.mtx.rnd':7,'B-ibm32.mtx.rnd':9,'C-bcspwr01.mtx.rnd':4,
	 'D-bcsstk01.mtx.rnd':12,'E-bcspwr02.mtx.rnd':7,'F-curtis54.mtx.rnd':8,
	 'G-will57.mtx.rnd':6,'H-impcol_b.mtx.rnd':17,'I-ash85.mtx.rnd':9,
	 'J-nos4.mtx.rnd':10,'K-dwt__234.mtx.rnd':11,'L-bcspwr03.mtx.rnd':10,
	 'M-bcsstk06.mtx.rnd':45,'N-bcsstk07.mtx.rnd':45,'O-impcol_d.mtx.rnd':35,
	 'P-can__445.mtx.rnd':46,'Q-494_bus.mtx.rnd':30,'R-dwt__503.mtx.rnd':41,
	 'S-sherman4.mtx.rnd':27,'T-dwt__592.mtx.rnd':29,'U-662_bus.mtx.rnd':55,
	 'V-nos6.mtx.rnd':17,'W-685_bus.mtx.rnd':33,'X-can__715.mtx.rnd':60}

def copyFiles(src,dest):
	src_files = os.listdir(src)
	for file_name in src_files:
    		full_file_name = os.path.join(src, file_name)
    		if (os.path.isfile(full_file_name)):
        		shutil.copy(full_file_name, dest)

def w_mat_file(str_met,name_instance):

	strF="F"
	strA="A"
	for i in range(num_file):
		cbmp=5000
		strN="%s"%i
		filename=name_instance+str_met+strF+strN
		infile=open(filename,'r')
		datas = infile.readlines()
		for line in datas:
			str_line= line.split()  
			line_float=map(float,str_line)
			if (line_float[1]<cbmp):
				cbmp=line_float[1]
				#t=line_float[2]	
		ofx.write("{0:<10.4f}\n".format(cbmp))	
		infile.close()	

def readfile(name_file,method):
	list_cbmp=[]
	list_t=[]
	str1="F"
	for i in range(num_file):
		cbmp=5000
		t=0.0
		str3="%s"%(i)
		filename=name_file+str1+str3
		infile=open(filename,'r')
		data = infile.readlines()
		for line in data:
			str_line= line.split() 
			line_float=float(str_line[1])
			if (line_float<cbmp):
				cbmp=float(str_line[1])
				t=float(str_line[2])
		infile.close()		
		list_cbmp.append(cbmp)
		list_t.append(t)
		
	return (list_cbmp,list_t)

def search_best(list_in):
	best=5000
	for i in range(num_file):
		if (list_in[i]<best):
			best=list_in[i]
	return best

def num_best(list_in,b):
	co=0;
	for i in range(num_file):
		if (list_in[i]==b):
			co=co+1
	return co;

def cal_avg_time(list_in,list_in2,b):
	sum_up=0.0
	cou=0
	for i in range(num_file):
		if(list_in[i]==b):
			sum_up=list_in2[i]+sum_up
			cou=cou+1
	avg=sum_up/cou
	return avg

def cal_avg(list_in):
	sum_up=0.0
	for i in range(num_file):
		sum_up=list_in[i]+sum_up
	avg=sum_up/num_file
	return avg

def cal_dev(list_in,avg):
	dev=0.0
	temp_sum=0.0
	for i in range(num_file):
		temp_sum=math.pow(list_in[i]-avg,2)+temp_sum
	dev=cmath.sqrt(temp_sum/num_file)
	return dev
		
def cal_RR(list_in,avg):
	RR=0.0
	temp_sum=0.0
	for i in range(num_file):
		temp_sum=math.pow((list_in[i]-avg)/avg,2)+temp_sum
	RR=cmath.sqrt(temp_sum/num_file)
	return RR
def verify_avancer(old,new):
	return (old-new)

def sor_all(list_in,list_in2,num_allresult):
	wopen=open(num_allresult,'a')
	for i in range(num_file):
		wopen.write("{0:<10.4f} {1:^10.4f} \n".format(list_in[i],list_in2[i]))
	wopen.close()

try:
	opt,args=getopt.getopt(sys.argv[1:],'p:')
	for name,deg in opt:
		if name in ('-p'):
			print deg
except getopt.GetoptError:
	usage()
	sys.exit(2)

outfile0="Result_0.txt"
outfile1="Result_1.txt"
outfile2="Result_2.txt"
outfile3="Result_3.txt"
outfilex="Result_all.txt"
infile="../fn.txt"
linked="_"
linename=""
rootdir="../instances/"
naf=""
str_met0="0"
str_met1="2"
str_met2="2"
str_met3="3"
num_instance=1
"""
##regenerate the folder Input_mat
shutil.rmtree('Input_mat')  
os.mkdir('Input_mat')

os.chdir('Input_mat')
##
"""
"""
##generate the file in the matlab
with open(infile) as fo:
	dataf=fo.read().rstrip().splitlines()
	for ff in dataf:
		file_in_mat0="inputStatTest-%d-0.in"%num_instance
		file_in_mat1="inputStatTest-%d-1.in"%num_instance
		file_in_mat2="inputStatTest-%d-2.in"%num_instance
		file_in_mat3="inputStatTest-%d-3.in"%num_instance

		naf=rootdir+ff

		ofx=open(file_in_mat0,'w')
		w_mat_file(str_met0,naf)
		ofx.close()

		ofx=open(file_in_mat1,'w')
		w_mat_file(str_met0,naf)
		ofx.close()

		ofx=open(file_in_mat2,'w')
		w_mat_file(str_met2,naf)
		ofx.close()
		
		ofx=open(file_in_mat3,'w')
		w_mat_file(str_met3,naf)
		ofx.close()
		num_instance=num_instance+1
		print num_instance
"""

##change the dir of folder


shutil.rmtree('summary_new')  
os.mkdir('summary_new')

os.chdir('summary_new')


of=open(outfile2,'w')
with open(infile) as seo:
	data=seo.read().rstrip().splitlines()
	for f in data:
			lc=[]
			lt=[]
			naf=rootdir+f
			(lc,lt)=readfile(naf,str_met1)
			cbmp_best=search_best(lc)
			num_b=num_best(lc,cbmp_best)
			cbmp_avg=cal_avg(lc)
			time_avg=cal_avg_time(lc,lt,cbmp_best)
			cbmp_dev=cal_dev(lc,cbmp_avg)
			cbmp_RR=cal_RR(lc,dict1[f])
			flag=verify_avancer(dict2[f],cbmp_best)
			sor_all(lc,lt,outfilex)
			linename=f+linked+"2"
			#of.write("%s %f %f %f \n"%(linename,cbmp_best,cbmp_avg,time_avg))
			of.write("{0:<30} {1:^10.4f} {2:^10.4f} {3:^10.4f} {4:^10.4f} {5:^10.4f} {6:^10} {7:^10}\n".format(linename,cbmp_best,cbmp_avg,time_avg,cbmp_dev.real,cbmp_RR.real,flag,num_b))
of.close()
