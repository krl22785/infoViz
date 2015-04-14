import csv

def inputParse(file):
	f = open(file)	
	reader = csv.reader(f)
	headers = reader.next() 

	summary = {} 

	pat_index = headers.index('DESYNPUF_ID')
	claim_index = headers.index('CLM_PMT_AMT')

	diag1_index = headers.index('ICD9_DGNS_CD_1')
	diag2_index = headers.index('ICD9_DGNS_CD_2')
	diag3_index = headers.index('ICD9_DGNS_CD_3')
	diag4_index = headers.index('ICD9_DGNS_CD_4')
	diag5_index = headers.index('ICD9_DGNS_CD_5')
	diag6_index = headers.index('ICD9_DGNS_CD_6')
	diag7_index = headers.index('ICD9_DGNS_CD_7')
	diag8_index = headers.index('ICD9_DGNS_CD_8')
	diag9_index = headers.index('ICD9_DGNS_CD_9')
	diag10_index = headers.index('ICD9_DGNS_CD_10')

	all_chronic = [diag1_index, diag2_index, diag3_index, diag4_index, diag5_index, diag6_index, diag7_index, diag8_index, diag9_index, diag10_index]
	 
	for visit in reader:
		index = 0 

		while index < 9:
			if visit[all_chronic[index]] == '':
				pass
			else:
				# print visit[pat_index], visit[all_chronic[index]], visit[claim_index]
				visit_diag = visit[all_chronic[index]]
				if visit_diag not in summary: 
					summary[visit_diag] = {} 
					summary[visit_diag][]
			index += 1 
			
		#print visit[patient], visit[claim


if __name__=='__main__':
	f = "DE1_0_2008_to_2010_Inpatient_Claims_Sample_1.csv" 
	inputParse(f)

	

