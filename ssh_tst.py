import paramiko
import configparser


def config(something_ini):
	parser = configparser.ConfigParser()
	parser.read(something_ini)

	return parser


tmp_ini = '/home/yda/Documents/ssh/smartiko'
tmp_command0 = 'psql postgresql://lorawan:Meter2015@127.0.0.1:/lora_controller SELECT to_hex(eui), to_hex(appeui) FROM motes WHERE to_hex(eui)="16c00000108873";'
tmp_command1 = 'psql postgresql://lorawan:Meter2015@127.0.0.1:/lora_controller'
tmp_command2 = 'SELECT to_hex(eui), to_hex(appeui) FROM motes WHERE to_hex(eui)="16c00000108873";'
tmp_config = config(tmp_ini)

hostname = tmp_config['server']['host']
password = tmp_config['server']['password']
username = tmp_config['server']['username']
port = tmp_config['server']['port']

#print(hostname, password, username, port)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, password=password, username=username, port=port)
#stdin, stdout, stderr = ssh.exec_command('ls')
#stdin, stdout, stderr = ssh.exec_command(tmp_command1)
stdin, stdout, stderr = ssh.exec_command(tmp_command0)
#data = stdout.read() + stderr.read()
print(f'stdout -- {stdout.read()}')
print(f'stderr -- {stderr.read()}')

ssh.close()
