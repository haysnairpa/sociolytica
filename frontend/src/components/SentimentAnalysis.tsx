import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const data = [
  { name: 'Product A', positive: 4000, neutral: 2400, negative: 2400 },
  { name: 'Product B', positive: 3000, neutral: 1398, negative: 2210 },
  { name: 'Product C', positive: 2000, neutral: 9800, negative: 2290 },
  { name: 'Product D', positive: 2780, neutral: 3908, negative: 2000 },
  { name: 'Product E', positive: 1890, neutral: 4800, negative: 2181 },
]

export function SentimentAnalysis() {
  return (
    <div className="p-6 space-y-6">
      <h2 className="text-3xl font-bold">Sentiment Analysis</h2>
      <Card>
        <CardHeader>
          <CardTitle>Product Sentiment Overview</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="positive" fill="#82ca9d" />
              <Bar dataKey="neutral" fill="#8884d8" />
              <Bar dataKey="negative" fill="#ffc658" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  )
}

