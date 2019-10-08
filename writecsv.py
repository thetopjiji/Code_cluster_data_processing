import csv
import os
import sys

os.chdir('summary')
os.system('rm R0.csv')
os.system('rm R1.csv')
os.system('rm R2.csv')
os.system('rm R3.csv')

infile0="Result_0.txt"
outfile0="R0.csv"
infile1="Result_1.txt"
outfile1="R1.csv"
infile2="Result_2.txt"
outfile2="R2.csv"
infile3="Result_3.txt"
outfile3="R3.csv"

def writecsv(infile,outfile):
	csvfile=file(outfile,'wb')
	writer=csv.writer(csvfile)
	fi=open(infile,'r')
	data = fi.readlines()
	for line in data:
		str_line= line.split()
		max_num=len(str_line)
		writer.writerow(str_line)  
	csvfile.close()	
	fi.close()

writecsv(infile2,outfile2)

os.chdir('..')
os.chdir('summary_new')
writecsv(infile2,outfile2)


