#!/bin/bash

EUI=$1
echo 'NC'
psql postgresql://lorawan:ves2018@127.0.0.1:/controller_00 << EOF
	SELECT to_hex(eui), to_hex(appeui) FROM motes WHERE to_hex(eui)='$1';
EOF
echo 'NS 1703'
psql postgresql://lorawan:ves2018@127.0.0.1:/network_00 << EOF
	SELECT to_hex(eui), to_hex(appeui), to_hex(networkaddress), networksessionkey, downmsgseqno, upmsgseqno, to_hex(gatewayeui) FROM motes WHERE to_hex(eui)='$1';
EOF
echo 'NS 1705'
psql postgresql://lorawan:ves2018@127.0.0.1:/network_01 << EOF
	SELECT to_hex(eui), to_hex(appeui), to_hex(networkaddress), fintkey, sintkey, networksessionkey, downmsgseqno, upmsgseqno, to_hex(gatewayeui) FROM motes WHERE to_hex(eui)='$1';
	SELECT * FROM mote_context WHERE to_hex(eui)='$1';
EOF
echo 'AS 4000'
psql postgresql://lorawan:ves2018@127.0.0.1:/application_00 << EOF
	SELECT to_hex(eui), to_hex(appeui), appkey FROM joinmotes WHERE to_hex(eui)='$1';
	SELECT to_hex(eui), to_hex(appeui), sessionkey, to_hex(networkaddress) FROM activemotes WHERE to_hex(eui)='$1';
EOF
echo 'AS 4001'
psql postgresql://lorawan:ves2018@127.0.0.1:/application_01 << EOF
	SELECT to_hex(eui), to_hex(appeui), nwkkey, appkey FROM joinmotes WHERE to_hex(eui)='$1';
	SELECT to_hex(eui), to_hex(appeui), sessionkey, to_hex(networkaddress) FROM activemotes WHERE to_hex(eui)='$1';
	SELECT to_hex(mote), nonce FROM nonces WHERE to_hex(mote)='$1';
EOF
echo 'CS 5005'
psql postgresql://lorawan:ves2018@127.0.0.1:/customer_00 << EOF
	SELECT to_hex(eui), to_hex(appeui), lastrxframe, accid, mote_descriptors_id FROM motes WHERE to_hex(eui)='$1';
	SELECT * FROM mote_data_descriptors WHERE to_hex(mote_id)='$1' ORDER BY param_code;
EOF
echo 'CS 5004'
psql postgresql://lorawan:ves2018@127.0.0.1:/customer_01 << EOF
	SELECT to_hex(eui), to_hex(appeui), lastrxframe, accid, mote_descriptors_id FROM motes WHERE to_hex(eui)='$1';
	SELECT * FROM mote_data_descriptors WHERE to_hex(mote_id)='$1' ORDER BY param_code;
EOF
echo 'CS 5006'
psql postgresql://lorawan:ves2018@127.0.0.1:/adeunis << EOF
	SELECT to_hex(eui), to_hex(appeui), lastrxframe FROM motes WHERE to_hex(eui)='$1';
