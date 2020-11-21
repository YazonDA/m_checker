import configparser


def config(_config):
	parser = configparser.ConfigParser()
	parser.read(_config)
	return parser

