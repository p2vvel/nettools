window.addEventListener("load", event => {

    // load data from backend, display graph of hosts
    function load_data() {
        fetch("http://127.0.0.1:8000/fake_data/")
            .then(response => response.json())
            .then(data => {
                // let hosts = data.get("hosts").map()
                let hosts = new Array();
                for (let k in data["hosts"])
                    hosts.push(k);
                let nodes = new vis.DataSet(hosts.map((h, i) => { return { id: i + 1, label: h } }));

                var edges = [];
                for (let i = 2; i <= hosts.length; i++)
                    edges.push({ from: i, to: 1 });
                edges = new vis.DataSet(edges);

                var container = document.getElementById("mynetwork");
                var data = {
                    nodes: nodes,
                    // edges: edges,
                };
                var options = {};
                var network = new vis.Network(container, data, options);

                // event handling when clicking on nodes
                network.on('click', function (properties) {
                    var ids = properties.nodes;
                    try {
                        var clickedNodes = nodes.get(ids);
                        console.log('clicked nodes:', clickedNodes[0].label, clickedNodes[0]);
                    }
                    catch (err) {}  // nothing to do, clicked on empty space
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