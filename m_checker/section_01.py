# Section 1
'''
Args:
	Mote (object)
Answer:
	Mote (object)
		with filling DP as dict
'''

import requests
import csv


def todo(_mote):
	tmp_dp_list = get_dp(_mote)
	
	#Classes.write_csv(tmp_dp_list, 'tmp_dp_list.csv')

	for _dp in tmp_dp_list:
		params = _mote.DP.setdefault(_dp['link_id'],{})
		params[_dp['param_id']] = {'port_number': _dp['port_number'], 'data_timestamp': _dp['data_timestamp'], 'value': _dp['value']}


def get_dp(_mote):
	answer = []
	for port_number in _mote.ports:
		dev_url = f'https://{_mote.hosts}/v1/applications/{_mote.AppEUI}/devices/{_mote.DevEUI}/ports/{port_number}/packets'

		params = {'DEV_EUI': _mote.DevEUI, 'PORT_NUMBER': port_number}
		params.update(get_token(_mote).json())

		answer_server = requests.get(dev_url, params=params)
		answer += answer_server.json()['data']
	return answer

def get_token(_mote):
	_url = f'https://{_mote.hosts}/v1/authenticate'
	_data = {'login': _mote.ts['log'], 'password': _mote.ts['pass']}
	_session = requests.Session()
	return _session.post(_url, data=_data)

def write_csv(inp_table, file_name):
	target_table = []
	target_table.append(list(inp_table[0].keys()))
	
	for one_dict in inp_table:
			new_row = []
			for column_caption in target_table[0]:
				new_row.append(one_dict[column_caption])
			target_table.append(new_row)

	with open(file_name, 'w') as csv_file:
		writer = csv.writer(csv_file, dialect = 'excel')
		for i in target_table:
			writer.writerow(i)