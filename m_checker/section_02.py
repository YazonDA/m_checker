# Section 2
'''
Args:
	Mote (object)
Answer:
	Mote (object)
		with removing wrong DPs (!= format_dp)
'''

def todo(_mote):
	dp_numbers = sorted(_mote.DP.keys())
	#print(dp_numbers)
	
	for i in dp_numbers:
		param_numbers = sorted(_mote.DP[i].keys())
		#print(f'for DP#{i} have the params {param_numbers}')

		if param_numbers != _mote.format_dp:
			#print(f'it`s wrong and this DP will be removed!')
			_mote.DP.pop(i)

	#dp_numbers = sorted(_mote.DP.keys())
	#print(dp_numbers)

	return bool(len(_mote.DP))
