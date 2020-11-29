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

	# take List of DP`s id
	dp_id = sorted(_mote.DP.keys())
	dp_date = {}
	
	# create dict of pare -- id_dp / date
	for i in dp_id:
		param_numbers = _mote.DP[i].keys()
		for j in param_numbers:
			param =_mote.DP[i][j]
			if param['port_number'] == 1:
				dp_date[i] = datetime.datetime.fromtimestamp(param['data_timestamp'])
				# NEED
				# only DATE, remove TIME
				break

	logging.info(f'dp_date of Mote is {dp_date}')

	# HERE !!!!!!
	# NEED
	# to remove DP with date like 2020-01-01 from mote.DP

	dp_chain = {}
	j = 1

	# THEN
	#change dp_id[1] to dp_id[0]
	dp_chain.setdefault(j,[dp_id[1]])

	# THEN
	# change (1, len(dp_id) - 2) to (len(dp_id) - 1)
	for index_id in range(1, len(dp_id) - 2):
		logging.info(f'index_id == {index_id}  from {len(dp_id)}')
		logging.info(f'second date is {dp_date[dp_id[index_id + 1]]}')
		logging.info(f'first date is {dp_date[dp_id[index_id]]}')
		day_delta = dp_date[dp_id[index_id + 1]] - dp_date[dp_id[index_id]]
		logging.info(f'day_delta == {day_delta} & day_delta.days == {day_delta.days}')
		if day_delta.days == 1:
			logging.info('add dp_id to dp_chain[j]')
			dp_chain[j].append(dp_date[dp_id[index_id + 1]])
		elif day_delta.days < 1:
			logging.info('remove dp_id from _mote.DP')
			_mote.DP.pop(dp_id[index_id + 1])
		else:
			logging.info('dp_chain.setdefault(++j,[dp_id[i + 1]])')
			j += 1
			dp_chain.setdefault(j,[dp_id[i + 1]])

	return dp_chain