var nodes = [
    { id: 1, label: 'Node 1' },
    { id: 2, label: 'Node 2' },
    { id: 3, label: 'Node 3' },
    { id: 4, label: 'Node 4' },
    { id: 5, label: 'Node 5' },
    { id: 6, label: 'Node 6' }
];

var edges = [
    { source: 1, target: 2 },
    { source: 1, target: 3 },
    { source: 2, target: 3 },
    { source: 2, target: 3 },
    { source: 1, target: 3 },
    { source: 3, target: 4 },
    { source: 4, target: 5 }
];


var svg = d3.select('#network-graph')
    .append('svg')
    .attr('width', '100%')
    .attr('height', '100%');

var simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(edges))
    .force('charge', d3.forceManyBody())
    .force('center', d3.forceCenter(svg.node().parentElement.clientWidth / 2, svg.node().parentElement.clientHeight / 2));

var link = svg.selectAll('.link')
    .data(edges)
    .enter()
    .append('line')
    .attr('class', 'link');

var node = svg.selectAll('.node')
    .data(nodes)
    .enter()
    .append('circle')
    .attr('class', 'node')
    .attr('r', 10)
    .attr('fill', 'steelblue');

simulation.on('tick', function() {
    link.attr('x1', function(d) { return d.source.x; })
        .attr('y1', function(d) { return d.source.y; })
        .attr('x2', function(d) { return d.target.x; })
        .attr('y2', function(d) { return d.target.y; })
        .attr('stroke', 'red');

    node.attr('cx', function(d) { return d.x; })
        .attr('cy', function(d) { return d.y; });
});