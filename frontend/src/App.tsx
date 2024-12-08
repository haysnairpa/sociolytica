import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import { Layout } from "./components/Layout"
import { Dashboard } from "./components/Dashboard"
import { TrendAnalysis } from "./components/TrendAnalysis"
import { NetworkAnalysis } from "./components/NetworkAnalysis"
import { SentimentAnalysis } from "./components/SentimentAnalysis"
import { Settings } from "./components/Settings"
import EngagementPatterns from '@/components/EngagementPatterns'

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/trend-analysis" element={<TrendAnalysis />} />
          <Route path="/network-analysis" element={<NetworkAnalysis />} />
          <Route path="/sentiment-analysis" element={<SentimentAnalysis />} />
          <Route path="/engagement-patterns" element={<EngagementPatterns />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Layout>
    </Router>
  )
}

export default App
