# Section 0
'''
Args:
	config.ini path/name
Answer:
	Mote (object)
'''

import configparser


def todo(_config):
	config_ini = config(_config)
	ts_ini = config(config_ini['TS']['ts'])
	return Mote(config_ini, ts_ini)

class Mote():
	def __init__(self, _config, _ts):
		self.DevEUI = _config['API']['dev']
		self.AppEUI = _config['API']['app']
		self.hosts = _config['API']['url']
		self.ports = list(map(int, (_config['API']['port']).split()))
		self.ts = _ts['TS']
		self.DP = {}
		self.format_dp = list(map(int, (_config['DP']['parameter'].split())))


def config(something_ini):
	parser = configparser.ConfigParser()
	parser.read(something_ini)

	return parser

