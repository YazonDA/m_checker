# Section 3
'''
Args:
	Mote (object)
Answer:
	#1. Mote (object)
			with removing wrong DPs (sample period > period between neighbor DPs)
	#2. Dict{number_of_chain: start/end date_of_chain_of_correct_Dps}
'''
import logging
import datetime


def todo(_mote):
	logging.info(f'Section 3: It`s started.')

	dp_numbers = sorted(_mote.DP.keys())
	dp_date = {}
	
	for i in dp_numbers:
		param_numbers = _mote.DP[i].keys()
		for j in param_numbers:
			param =_mote.DP[i][j]
			if param['port_number'] == 1:
				zzz = datetime.datetime.fromtimestamp(param['data_timestamp'])
				break
		dp_date[i] = zzz

	logging.info(f'dp_date of Mote is {dp_date}')
