// names of protocols
var udp_names = {7: 'echo', 9: 'discard', 13: 'daytime', 19: 'chargen', 21: 'fsp', 37: 'time', 49: 'tacacs', 53: 'domain', 67: 'bootps', 68: 'bootpc', 69: 'tftp', 88: 'kerberos', 111: 'sunrpc', 123: 'ntp', 137: 'netbios-ns', 138: 'netbios-dgm', 161: 'snmp', 162: 'snmp-trap', 163: 'cmip-man', 164: 'cmip-agent', 177: 'xdmcp', 213: 'ipx', 319: 'ptp-event', 320: 'ptp-general', 369: 'rpc2portmap', 370: 'codaauth2', 371: 'clearcase', 389: 'ldap', 427: 'svrloc', 443: 'https', 464: 'kpasswd', 500: 'isakmp', 512: 'biff', 513: 'who', 514: 'syslog', 517: 'talk', 518: 'ntalk', 520: 'route', 538: 'gdomap', 546: 'dhcpv6-client', 547: 'dhcpv6-server', 554: 'rtsp', 623: 'asf-rmcp', 636: 'ldaps', 646: 'ldp', 655: 'tinc', 750: 'kerberos4', 751: 'kerberos-master', 752: 'passwd-server', 779: 'moira-ureg', 853: 'domain-s', 1194: 'openvpn', 1210: 'predict', 1434: 'ms-sql-m', 1645: 'datametrics', 1646: 'sa-msg-port', 1701: 'l2f', 1812: 'radius', 1813: 'radius-acct', 2049: 'nfs', 2086: 'gnunet', 2101: 'rtcm-sc104', 2102: 'zephyr-srv', 2103: 'zephyr-clt', 2104: 'zephyr-hm', 2430: 'venus', 2431: 'venus-se', 2432: 'codasrv', 2433: 'codasrv-se', 2583: 'mon', 3130: 'icpv2', 3205: 'isns', 3493: 'nut', 4500: 'ipsec-nat-t', 4569: 'iax', 5060: 'sip', 5061: 'sip-tls', 5353: 'mdns', 5555: 'rplay', 6346: 'gnutella-svc', 6347: 'gnutella-rtr', 6696: 'babel', 7000: 'afs3-fileserver', 7001: 'afs3-callback', 7002: 'afs3-prserver', 7003: 'afs3-vlserver', 7004: 'afs3-kaserver', 7005: 'afs3-volser', 7007: 'afs3-bos', 7008: 'afs3-update', 7009: 'afs3-rmtsys', 17001: 'sgi-cmsd', 17002: 'sgi-crsd', 17003: 'sgi-gcd', 27374: 'asp'};
var tcp_names = {1: 'tcpmux', 7: 'echo', 9: 'discard', 11: 'systat', 13: 'daytime', 15: 'netstat', 17: 'qotd', 19: 'chargen', 20: 'ftp-data', 21: 'ftp', 22: 'ssh', 23: 'telnet', 25: 'smtp', 37: 'time', 43: 'whois', 49: 'tacacs', 53: 'domain', 70: 'gopher', 79: 'finger', 80: 'http', 88: 'kerberos', 102: 'iso-tsap', 104: 'acr-nema', 106: 'poppassd', 110: 'pop3', 111: 'sunrpc', 113: 'auth', 119: 'nntp', 135: 'epmap', 139: 'netbios-ssn', 143: 'imap2', 161: 'snmp', 162: 'snmp-trap', 163: 'cmip-man', 164: 'cmip-agent', 174: 'mailq', 179: 'bgp', 199: 'smux', 209: 'qmtp', 210: 'z3950', 345: 'pawserv', 346: 'zserv', 369: 'rpc2portmap', 370: 'codaauth2', 389: 'ldap', 427: 'svrloc', 443: 'https', 444: 'snpp', 445: 'microsoft-ds', 464: 'kpasswd', 465: 'submissions', 487: 'saft', 512: 'exec', 513: 'login', 514: 'shell', 515: 'printer', 538: 'gdomap', 540: 'uucp', 543: 'klogin', 544: 'kshell', 548: 'afpovertcp', 554: 'rtsp', 563: 'nntps', 587: 'submission', 607: 'nqs', 628: 'qmqp', 631: 'ipp', 636: 'ldaps', 646: 'ldp', 655: 'tinc', 706: 'silc', 749: 'kerberos-adm', 750: 'kerberos4', 751: 'kerberos-master', 754: 'krb-prop', 775: 'moira-db', 777: 'moira-update', 783: 'spamd', 853: 'domain-s', 871: 'supfilesrv', 873: 'rsync', 989: 'ftps-data', 990: 'ftps', 992: 'telnets', 993: 'imaps', 995: 'pop3s', 1080: 'socks', 1093: 'proofd', 1094: 'rootd', 1099: 'rmiregistry', 1127: 'supfiledbg', 1178: 'skkserv', 1194: 'openvpn', 1236: 'rmtcfg', 1313: 'xtel', 1314: 'xtelw', 1352: 'lotusnote', 1433: 'ms-sql-s', 1524: 'ingreslock', 1645: 'datametrics', 1646: 'sa-msg-port', 1649: 'kermit', 1677: 'groupwise', 1812: 'radius', 1813: 'radius-acct', 2000: 'cisco-sccp', 2049: 'nfs', 2086: 'gnunet', 2101: 'rtcm-sc104', 2119: 'gsigatekeeper', 2121: 'iprop', 2135: 'gris', 2401: 'cvspserver', 2430: 'venus', 2431: 'venus-se', 2432: 'codasrv', 2433: 'codasrv-se', 2583: 'mon', 2600: 'zebrasrv', 2601: 'zebra', 2602: 'ripd', 2603: 'ripngd', 2604: 'ospfd', 2605: 'bgpd', 2606: 'ospf6d', 2607: 'ospfapi', 2608: 'isisd', 2628: 'dict', 2792: 'f5-globalsite', 2811: 'gsiftp', 2947: 'gpsd', 3050: 'gds-db', 3205: 'isns', 3260: 'iscsi-target', 3306: 'mysql', 3389: 'ms-wbt-server', 3493: 'nut', 3632: 'distcc', 3689: 'daap', 3690: 'svn', 4031: 'suucp', 4094: 'sysrqd', 4190: 'sieve', 4353: 'f5-iquery', 4369: 'epmd', 4373: 'remctl', 4460: 'ntske', 4557: 'fax', 4559: 'hylafax', 4691: 'mtn', 4899: 'radmin-port', 4949: 'munin', 5060: 'sip', 5061: 'sip-tls', 5222: 'xmpp-client', 5269: 'xmpp-server', 5308: 'cfengine', 5432: 'postgresql', 5556: 'freeciv', 5666: 'nrpe', 5667: 'nsca', 5671: 'amqps', 5672: 'amqp', 5680: 'canna', 6000: 'x11', 6001: 'x11-1', 6002: 'x11-2', 6003: 'x11-3', 6004: 'x11-4', 6005: 'x11-5', 6006: 'x11-6', 6007: 'x11-7', 6346: 'gnutella-svc', 6347: 'gnutella-rtr', 6379: 'redis', 6444: 'sge-qmaster', 6445: 'sge-execd', 6446: 'mysql-proxy', 6514: 'syslog-tls', 6566: 'sane-port', 6667: 'ircd', 6697: 'ircs-u', 7000: 'bbs', 7100: 'font-service', 8021: 'zope-ftp', 8080: 'http-alt', 8081: 'tproxy', 8088: 'omniorb', 8140: 'puppet', 8990: 'clc-build-daemon', 9098: 'xinetd', 9101: 'bacula-dir', 9102: 'bacula-fd', 9103: 'bacula-sd', 9418: 'git', 9667: 'xmms2', 9673: 'zope', 10000: 'webmin', 10050: 'zabbix-agent', 10051: 'zabbix-trapper', 10080: 'amanda', 10081: 'kamanda', 10082: 'amandaidx', 10083: 'amidxtape', 10809: 'nbd', 11112: 'dicom', 11371: 'hkp', 17004: 'sgi-cad', 17500: 'db-lsp', 22125: 'dcap', 22128: 'gsidcap', 22273: 'wnn6', 24554: 'binkp', 27374: 'asp', 30865: 'csync2', 57000: 'dircproxy', 60177: 'tfido', 60179: 'fido'};


window.addEventListener("load", event => {

    let tcp_ports_area = document.querySelector("#tcp_ports");
    let udp_ports_area = document.querySelector("#udp_ports");
    let new_hostname = document.querySelector("#new_hostname");
    let current_hostname = document.querySelector("#current_hostname");

    function clear_tables(info = `<tr><td colspan="2">Choose a host to see its ports</td></tr>`) {
        tcp_ports_area.innerHTML = info;
        udp_ports_area.innerHTML = info;
    }

    // load data from backend, display graph of hosts
    function load_data() {
        fetch("http://127.0.0.1:8080/hosts/")
            .then(response => response.json())
            .then(data => {
                clear_tables()

                let hosts = data.map((host, index) => host["name"]);
                let ports_array = data.map(host => {
                    return {
                        "udp": host["ports"].filter(port => port["proto"] === true).map(port => port["number_of_port"]),
                        "tcp": host["ports"].filter(port => port["proto"] === false).map(port => port["number_of_port"]),
                    }
                })
                let hosts_data = {};
                for (let i = 0; i < hosts.length; i++)
                    hosts_data[data[i]["name"]] = ports_array[i];


                // create graph
                let nodes = new vis.DataSet(hosts.map((h, i) => { return { id: i + 1, label: h } }));
                var container = document.getElementById("mynetwork");
                var network = new vis.Network(container, { nodes: nodes }, {});


                // event handling when clicking on nodes
                network.on('click', function (properties) {
                    var ids = properties.nodes;
                    clear_tables("")
                    try {
                        var clickedNodes = nodes.get(ids);
                        let chosen_host = clickedNodes[0].label;
                        new_hostname.value = chosen_host;
                        current_hostname.value = chosen_host;
                        let udp_ports = hosts_data[chosen_host]["udp"];
                        let tcp_ports = hosts_data[chosen_host]["tcp"];
                        let tcp_table = tcp_ports.map((port, i) => `<tr><td>${port}</td><td>${tcp_names[port] || "-"}</td></tr>`).join("");
                        if (!tcp_table)
                            tcp_table = `<tr><td colspan="2">No open TCP ports</td></tr>`;
                        let udp_table = udp_ports.map((port, i) => `<tr><td>${port}</td><td>${udp_names[port]  || "-"}</td></tr>`).join("");
                        if (!udp_table)
                            udp_table = `<tr><td colspan="2">No open UDP ports</td></tr>`;
                        tcp_ports_area.innerHTML = tcp_table;
                        udp_ports_area.innerHTML = udp_table;

                    }
                    catch (err) {
                        console.log(err)
                        clear_tables()
                    }
                });
            }).catch(error => {
                console.log(error);
            });
    }

    // add event to refresh button
    let refresh_button = document.querySelector("#refresh_button");
    refresh_button.addEventListener("click", load_data);

    load_data();    // initialize graph on load
});