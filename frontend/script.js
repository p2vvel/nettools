window.addEventListener("load", event => {

    function load_data(){
        fetch("http://127.0.0.1:8000/fake_data/")
        .then(response => response.json())
        .then(data => {
            let hosts = new Array();
            for (let k in data["hosts"])
                hosts.push(k);
            let nodes = new vis.DataSet(hosts.map((h, i) => { return {id: i+1, label: h} }));
            
            // let edges = new vis.DataSet(hosts.map())
            // let vortex_data = [];
            var edges = [];
            for (let i = 2; i <= hosts.length; i++)
                edges.push({from: i, to: 1});
            edges = new vis.DataSet(edges);
                
            var container = document.getElementById("mynetwork");
            var data = {
                nodes: nodes,
                edges: edges,
            };
            var options = {};
            var network = new vis.Network(container, data, options);
            
            // console.log(hosts);
        }).catch(error => {
            console.log(error);
        });

    }

    let refresh_button = document.querySelector("#refresh_button");
    refresh_button.addEventListener("click", load_data);
    // first initialization
    load_data();
});