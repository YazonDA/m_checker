import sys
import m_checker.modules as my_
import configparser

def main():
	_config = my_.config('settings.ini')
	_ts

	print(_config['API']['dev'])

	return 0


if __name__ == '__main__':
	sys.exit(main())

