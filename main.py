import sys
import m_checker.section_00 as section_00
import m_checker.section_01 as section_01

def main():
	tst_mote = section_00.todo('settings.ini')
	
	print(f'Test for Mote {tst_mote.DevEUI[-6:]} is starting!\n')
	
	print(f'Section 0:\n\tMote-object is created!\n')
	
	answer_01 = section_01.todo(tst_mote)
	print(f'Section 1:\n\tMote - have some DPs. Is it True ?\n\t{answer_01}\n')
	
	return 0


if __name__ == '__main__':
	sys.exit(main())

