import { Home, TrendingUp, Users, BarChart2, Settings, ChartPie, Cog } from 'lucide-react'
import { NavLink } from 'react-router-dom'
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

const sidebarItems = [
  {
    icon: Home,
    label: "Dashboard",
    path: "/",
  },
  {
    icon: TrendingUp,
    label: "Trend Analysis",
    path: "/trend-analysis",
  },
  {
    icon: Users,
    label: "Network Analysis",
    path: "/network-analysis",
  },
  {
    icon: BarChart2,
    label: "Sentiment Analysis",
    path: "/sentiment-analysis",
  },
  {
    icon: ChartPie,
    label: "Engagement Patterns",
    path: "/engagement-patterns",
  },
  {
    icon: Cog,
    label: "Settings",
    path: "/settings",
  },
]

export function Sidebar() {
  return (
    <div className="flex flex-col w-64 bg-white border-r">
      <div className="flex items-center justify-center h-16 border-b">
        <span className="text-2xl font-semibold">Sosialityca</span>
      </div>
      <nav className="flex-1 overflow-y-auto">
        <ul className="p-2 space-y-2">
          {sidebarItems.map((item, index) => (
            <li key={index}>
              <NavLink
                to={item.path}
                className={({ isActive }) =>
                  cn(
                    "flex items-center w-full p-2 rounded-lg text-sm font-medium transition-colors",
                    isActive
                      ? "bg-gray-100 text-gray-900"
                      : "text-gray-500 hover:text-gray-900 hover:bg-gray-50"
                  )
                }
              >
                <item.icon className="mr-2 h-4 w-4" />
                {item.label}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  )
}

