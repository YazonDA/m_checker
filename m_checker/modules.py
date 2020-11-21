import configparser


class Mote():
	def __init__(self, _config, _ts):
		self.DevEUI = _config['API']['dev']
		self.AppEUI = _config['API']['app']
		self.hosts = _config['API']['url']
		self.ports = list(map(int, (_config['API']['port']).split()))
		self.ts = _ts['TS']
		self.DP = {}
		self.format_dp = list(map(int, (_config['DP']['parameter'].split())))


def config(config_ini):
	parser = configparser.ConfigParser()
	parser.read(config_ini)

	print(parser)
	return parser

