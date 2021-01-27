import psycopg2

conn = psycopg.connect("dbname='lora_network_eu' user='lorawan' host='localhost' password='Meter2015'")
cur - conn.cursor()
cur.execute('SELECT to_hex(eui), to_hex(appeui) FROM motes WHERE to_hex(eui)="16c00000108873";')
ans = cur.fetchall()

print(ans)