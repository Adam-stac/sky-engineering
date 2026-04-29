const container = document.getElementById('org-chart-container');
const data = JSON.parse(container.dataset.chart);

const width = container.offsetWidth;
const nodeWidth = 180;
const nodeHeight = 70;
const margin = { top: 40, right: 20, bottom: 40, left: 20 };

const tree = d3.tree().nodeSize([nodeWidth + 20, nodeHeight + 40]);
const root = d3.hierarchy(data);
tree(root);

const svg = d3.select('#org-chart-container')
    .append('svg')
    .attr('width', width)
    .attr('height', 600)
    .style('overflow', 'auto');

const g = svg.append('g')
    .attr('transform', `translate(${width / 2}, ${margin.top})`);

g.selectAll('.link')
    .data(root.links())
    .enter()
    .append('path')
    .attr('class', 'link')
    .attr('fill', 'none')
    .attr('stroke', '#e2e8f0')
    .attr('stroke-width', 1.5)
    .attr('d', d3.linkVertical()
        .x(d => d.x)
        .y(d => d.y)
    );

const node = g.selectAll('.node')
    .data(root.descendants())
    .enter()
    .append('g')
    .attr('class', 'node')
    .attr('transform', d => `translate(${d.x}, ${d.y})`);

node.append('rect')
    .attr('x', -nodeWidth / 2)
    .attr('y', -nodeHeight / 2)
    .attr('width', nodeWidth)
    .attr('height', nodeHeight)
    .attr('rx', 8)
    .attr('fill', d => {
        if (d.data.type === 'root') return '#0f172a';
        if (d.data.type === 'department') return '#1e293b';
        if (d.data.status === 'active') return '#ffffff';
        if (d.data.status === 'restructuring') return '#fffbeb';
        return '#f8fafc';
    })
    .attr('stroke', d => {
        if (d.data.type === 'root' || d.data.type === 'department') return 'none';
        if (d.data.status === 'active') return '#e2e8f0';
        if (d.data.status === 'restructuring') return '#fcd34d';
        return '#e2e8f0';
    })
    .attr('stroke-width', 1);

node.append('text')
    .attr('text-anchor', 'middle')
    .attr('y', d => d.data.type === 'root' || d.data.type === 'department' ? -8 : -12)
    .attr('fill', d => d.data.type === 'root' || d.data.type === 'department' ? '#ffffff' : '#0f172a')
    .attr('font-size', '12px')
    .attr('font-weight', '500')
    .attr('font-family', '-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif')
    .text(d => d.data.name.length > 20 ? d.data.name.substring(0, 20) + '...' : d.data.name);

node.append('text')
    .attr('text-anchor', 'middle')
    .attr('y', d => d.data.type === 'root' || d.data.type === 'department' ? 10 : 6)
    .attr('fill', d => d.data.type === 'root' || d.data.type === 'department' ? 'rgba(255,255,255,0.6)' : '#64748b')
    .attr('font-size', '10px')
    .attr('font-family', '-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif')
    .text(d => {
        if (d.data.type === 'root') return 'Organisation';
        if (d.data.type === 'department') return d.data.leader;
        return d.data.manager;
    });

node.filter(d => d.data.type === 'team')
    .append('text')
    .attr('text-anchor', 'middle')
    .attr('y', 22)
    .attr('fill', d => d.data.status === 'active' ? '#15803d' : '#854d0e')
    .attr('font-size', '10px')
    .attr('font-family', '-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif')
    .text(d => d.data.status.charAt(0).toUpperCase() + d.data.status.slice(1));

const zoom = d3.zoom()
    .scaleExtent([0.5, 2])
    .on('zoom', (event) => {
        g.attr('transform', event.transform);
    });

svg.call(zoom);
svg.call(zoom.transform, d3.zoomIdentity.translate(width / 2, margin.top));