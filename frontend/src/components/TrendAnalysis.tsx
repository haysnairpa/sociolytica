import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const data = [
  { name: 'Jan', hashtag1: 4000, hashtag2: 2400, hashtag3: 2400 },
  { name: 'Feb', hashtag1: 3000, hashtag2: 1398, hashtag3: 2210 },
  { name: 'Mar', hashtag1: 2000, hashtag2: 9800, hashtag3: 2290 },
  { name: 'Apr', hashtag1: 2780, hashtag2: 3908, hashtag3: 2000 },
  { name: 'May', hashtag1: 1890, hashtag2: 4800, hashtag3: 2181 },
  { name: 'Jun', hashtag1: 2390, hashtag2: 3800, hashtag3: 2500 },
  { name: 'Jul', hashtag1: 3490, hashtag2: 4300, hashtag3: 2100 },
]

export function TrendAnalysis() {
  return (
    <div className="p-6 space-y-6">
      <h2 className="text-3xl font-bold">Trend Analysis</h2>
      <Card>
        <CardHeader>
          <CardTitle>Top Hashtags Over Time</CardTitle>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="hashtag1" stroke="#8884d8" activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="hashtag2" stroke="#82ca9d" />
              <Line type="monotone" dataKey="hashtag3" stroke="#ffc658" />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  )
}

