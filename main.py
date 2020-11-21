import sys
import m_checker.modules as do_it


def main():
	_config = do_it.config('settings.ini')
	_ts = do_it.config('/home/yda/Documents/ts.ini')
	tst_mote = do_it.Mote(_config, _ts)

	#print(tst_mote.format_dp)

	return 0


if __name__ == '__main__':
	sys.exit(main())

