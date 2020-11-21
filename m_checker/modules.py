import configparser


def config(config_ini):
	parser = configparser.ConfigParser()
	parser.read(config_ini)
	return parser

