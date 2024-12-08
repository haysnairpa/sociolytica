import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar } from 'recharts'

const dummyData = [
  { time: '00:00', engagement: 120 },
  { time: '04:00', engagement: 80 },
  { time: '08:00', engagement: 250 },
  { time: '12:00', engagement: 320 },
  { time: '16:00', engagement: 450 },
  { time: '20:00', engagement: 380 },
]

const contentTypeData = [
  { type: 'Images', engagement: 450 },
  { type: 'Videos', engagement: 380 },
  { type: 'Text', engagement: 250 },
  { type: 'Links', engagement: 180 },
]

export default function EngagementPatterns() {
  return (
    <div className="p-6 space-y-6">
      <h2 className="text-3xl font-bold tracking-tight">Engagement Pattern Analysis</h2>
      
      {/* Best Time to Post */}
      <Card>
        <CardHeader>
          <CardTitle>Best Time to Post</CardTitle>
          <CardDescription>Engagement levels throughout the day</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={dummyData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="time" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line 
                  type="monotone" 
                  dataKey="engagement" 
                  stroke="#8884d8" 
                  activeDot={{ r: 8 }} 
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      {/* Content Type Performance */}
      <Card>
        <CardHeader>
          <CardTitle>Content Type Performance</CardTitle>
          <CardDescription>Engagement rates by content type</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={contentTypeData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="type" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="engagement" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      {/* Engagement Metrics Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Average Likes</CardTitle>
            <CardDescription>Per post in last 30 days</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">245</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Average Comments</CardTitle>
            <CardDescription>Per post in last 30 days</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">32</p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Engagement Rate</CardTitle>
            <CardDescription>Average interaction rate</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-3xl font-bold">4.8%</p>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
