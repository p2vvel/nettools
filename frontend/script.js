window.addEventListener("load", event => {

    let tcp_ports_area = document.querySelector("#tcp_ports");
    let udp_ports_area = document.querySelector("#udp_ports");

    function clear_tables(info = `<tr><td colspan="2">Choose a host to see its ports</td></tr>`) {
        tcp_ports_area.innerHTML = info;
        udp_ports_area.innerHTML = info;
    }

    // load data from backend, display graph of hosts
    function load_data() {
        fetch("http://127.0.0.1:8000/fake_data/")
            .then(response => response.json())
            .then(data => {
                clear_tables()

                var hosts_data = data;
                let hosts = Object.keys(data["hosts"])

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
                        let udp_ports = hosts_data["hosts"][chosen_host]["udp"];
                        let tcp_ports = hosts_data["hosts"][chosen_host]["tcp"];
                        let tcp_table = Object.keys(tcp_ports).map(k => `<tr><td>${k}</td><td>${tcp_ports[k]}</td></tr>`).join("");
                        if (!tcp_table)
                            tcp_table = `<tr><td colspan="2">No open TCP ports</td></tr>`;
                        let udp_table = Object.keys(udp_ports).map(k => `<tr><td>${k}</td><td>${udp_ports[k]}</td></tr>`).join("");
                        if (!udp_table)
                            udp_table = `<tr><td colspan="2">No open UDP ports</td></tr>`;
                        tcp_ports_area.innerHTML = tcp_table;
                        udp_ports_area.innerHTML = udp_table;
                    }
                    catch (err) {
                        clear_tables()
                        console.log(err);
                    }  // nothing to do, clicked on empty space
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