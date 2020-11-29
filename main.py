import sys
import m_checker.section_00 as section_00
import m_checker.section_01 as section_01
import m_checker.section_02 as section_02
import m_checker.section_03 as section_03
import logging

def main():
	line_format = "[%(asctime)s] %(levelname)s: %(message)s"
	logging.basicConfig(filename="m_checker.log",
						format=line_format,
						level=logging.INFO)

	tst_mote = section_00.todo('settings.ini')
	
	logging.info('')
	logging.info(f'Test for Mote {tst_mote.DevEUI[-6:]} is starting!')
	
	logging.info(f'Section 0: Mote-object is created!')
	
	section_01.todo(tst_mote)
	logging.info(f'Section 1: Mote have {len(tst_mote.DP)} some DPs.')
	
	section_02.todo(tst_mote)
	logging.info(f'Section 2: Mote have {len(tst_mote.DP)} DPs where each DP is equal to sample.')

	section_03.todo(tst_mote)
	logging.info(f'Section 3: Mote have {len(tst_mote.DP)} DPs .')

	logging.shutdown()
	return 0


if __name__ == '__main__':
	sys.exit(main())

