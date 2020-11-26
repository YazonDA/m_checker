# Section 2
'''
Args:
	Mote (object)
Answer:
	Mote (object)
		with removing wrong DPs (!= format_dp)
'''
import logging


def todo(_mote):
	dp_numbers = sorted(_mote.DP.keys())
	#print(dp_numbers)
	
	for i in dp_numbers:
		param_numbers = sorted(_mote.DP[i].keys())
		
		if param_numbers != _mote.format_dp:
			_mote.DP.pop(i)
