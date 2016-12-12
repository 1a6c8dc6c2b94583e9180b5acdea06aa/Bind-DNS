#
include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";

# Limiting access to local networks only
acl "clients" {
        127.0.0.0/8;
        10.8.8.0/24;
};

options {
	listen-on port 53 { any; };
	listen-on-v6 { none; };
	directory 	"/var/named";
	dump-file 	"/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";

	# Maximum number of simultaneous client TCP connections to accept
	tcp-clients 50;

	# Disable built-in server information zones
	version none;
	hostname none;
	server-id none;

	# Attempt to do all the work required to answer the query
	recursion yes;
	recursive-clients 100;
        allow-recursion { clients; };
        allow-query { clients; };
	# Only LAN users are allowed to receive zone transfers from the server
        allow-transfer { clients; };

	auth-nxdomain no;
        notify no;
	dnssec-enable yes;
	dnssec-validation auto;
	dnssec-lookaside auto;

	# Path to ISC DLV key
	bindkeys-file "/etc/named.iscdlv.key";
	managed-keys-directory "/var/named/dynamic";
};

# Specifications of what to log, and where the log messages are sent
logging {
        channel "common_log" {
                file "/var/log/named/named.log" versions 10 size 5m;
		severity error;
                print-category yes;
                print-severity yes;
                print-time yes;
        };
        category default { "common_log"; };
        category general { "common_log"; };
        category queries { "common_log"; };
	category client { "common_log"; };
	category security { "common_log"; };
	category query-errors { "common_log"; };
	category lame-servers { null; };
};

# Internal zone definitions
zone "hl.local" {
        type master;
        file "/etc/named/db.hl.local";
        allow-update { none; };
};

zone "8.8.10.in-addr.arpa" {
        type master;
        file "/etc/named/db.8.8.10";
        allow-update { none; };
};
