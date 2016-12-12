
# https://github.com/blackyboy/RedHat-Centos-Common-Stuffs/blob/master/Step-by-Step-how-to-setup-a-DNS-Server-in-RHEL-6.2-6.4-6.5-Using-Bind.md
# https://github.com/blackyboy/RedHat-Centos-Common-Stuffs/tree/master/DNS_server_setup_RHEL6



# Primary DNS Server (or) Master DNS Server:
yum install bind*


# Create a log directory:
mkdir /var/log/named
chown named:named /var/log/named

  
  



# Configuration of name server:
# /etc/named.conf 
#----------------------------------------------------------------------------------------------------------
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//

options {
        listen-on port 53 { 127.0.0.1; };
        listen-on-v6 port 53 { ::1; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        allow-query     { localhost; };
        recursion yes;

        dnssec-enable yes;
        dnssec-validation yes;

        /* Path to ISC DLV key */
        bindkeys-file "/etc/named.iscdlv.key";

        managed-keys-directory "/var/named/dynamic";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
        type hint;
        file "named.ca";
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";






































