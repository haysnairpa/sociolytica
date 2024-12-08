import { useEffect, useRef } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import * as d3 from 'd3'

const data = {
  nodes: [
    { id: 1, name: "User 1" },
    { id: 2, name: "User 2" },
    { id: 3, name: "User 3" },
    { id: 4, name: "User 4" },
    { id: 5, name: "User 5" },
  ],
  links: [
    { source: 1, target: 2 },
    { source: 1, target: 3 },
    { source: 2, target: 4 },
    { source: 3, target: 5 },
    { source: 4, target: 5 },
  ]
}

export function NetworkAnalysis() {
  const d3Container = useRef(null)

  useEffect(() => {
    if (d3Container.current) {
      const svg = d3.select(d3Container.current)
      
      const width = 600
      const height = 400

      const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id))
        .force("charge", d3.forceManyBody().strength(-50))
        .force("center", d3.forceCenter(width / 2, height / 2))

      const link = svg.append("g")
        .selectAll("line")
        .data(data.links)
        .join("line")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)

      const node = svg.append("g")
        .selectAll("circle")
        .data(data.nodes)
        .join("circle")
        .attr("r", 5)
        .attr("fill", "#69b3a2")

      node.append("title")
        .text(d => d.name)

      simulation.on("tick", () => {
        link
          .attr("x1", d => d.source.x)
          .attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x)
          .attr("y2", d => d.target.y)

        node
          .attr("cx", d => d.x)
          .attr("cy", d => d.y)
      })
    }
  }, [])

  return (
    <div className="p-6 space-y-6">
      <h2 className="text-3xl font-bold">Network Analysis</h2>
      <Card>
        <CardHeader>
          <CardTitle>User Network Visualization</CardTitle>
        </CardHeader>
        <CardContent>
          <svg ref={d3Container} width={600} height={400} />
        </CardContent>
      </Card>
    </div>
  )
}

