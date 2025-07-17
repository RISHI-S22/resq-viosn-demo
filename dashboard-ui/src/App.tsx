import React, { useState } from 'react';
import { 
  Menu, 
  X, 
  Activity, 
  Camera, 
  Shield, 
  MapPin, 
  Clock, 
  AlertTriangle,
  Eye,
  FileText,
  Settings,
  ChevronRight,
  Phone,
  Building2
} from 'lucide-react';

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const sidebarItems = [
    { icon: Activity, label: 'Dashboard', active: true },
    { icon: Eye, label: 'Live Feed' },
    { icon: FileText, label: 'Reports' },
    { icon: Building2, label: 'Nearby Hospitals' },
    { icon: Shield, label: 'Nearby Police Stations' },
    { icon: Settings, label: 'Settings' },
  ];

  const summaryCards = [
    {
      title: 'Total Detections Today',
      value: '12',
      icon: AlertTriangle,
      color: 'text-orange-400',
      bgColor: 'bg-orange-400/10',
    },
    {
      title: 'Active Cameras',
      value: '24',
      icon: Camera,
      color: 'text-blue-400',
      bgColor: 'bg-blue-400/10',
    },
    {
      title: 'System Health',
      value: '98%',
      icon: Shield,
      color: 'text-green-400',
      bgColor: 'bg-green-400/10',
    },
  ];

  const policeStations = [
    { name: 'Central Police Station', distance: '0.8 km' },
    { name: 'Traffic Police HQ', distance: '1.2 km' },
    { name: 'Emergency Response Unit', distance: '2.1 km' },
    { name: 'Metro Police Station', distance: '2.8 km' },
  ];

  const hospitals = [
    { name: 'City General Hospital', distance: '1.1 km' },
    { name: 'Emergency Medical Center', distance: '1.5 km' },
    { name: 'Trauma Care Unit', distance: '2.3 km' },
    { name: 'Regional Medical Center', distance: '3.2 km' },
  ];

  const detectionLogs = [
    {
      videoName: 'CAM_001_Highway_A1',
      detectionTime: '2025-01-02 14:35:22',
      status: 'Success',
      statusColor: 'bg-green-500',
    },
    {
      videoName: 'CAM_005_Junction_B2',
      detectionTime: '2025-01-02 13:28:15',
      status: 'Pending',
      statusColor: 'bg-yellow-500',
    },
    {
      videoName: 'CAM_003_Main_Street',
      detectionTime: '2025-01-02 12:45:33',
      status: 'Success',
      statusColor: 'bg-green-500',
    },
    {
      videoName: 'CAM_008_Bridge_C4',
      detectionTime: '2025-01-02 11:22:18',
      status: 'Alert',
      statusColor: 'bg-red-500',
    },
    {
      videoName: 'CAM_002_Downtown',
      detectionTime: '2025-01-02 10:55:42',
      status: 'Success',
      statusColor: 'bg-green-500',
    },
  ];

  const StatusBadge = ({ status, color }: { status: string; color: string }) => (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium text-white ${color}`}>
      {status}
    </span>
  );

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Top Navigation */}
      <nav className="bg-gray-800 border-b border-gray-700 px-4 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <button
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="lg:hidden text-gray-300 hover:text-white"
            >
              <Menu className="h-6 w-6" />
            </button>
            <div className="flex items-center space-x-2">
              <div className="bg-blue-600 p-2 rounded-lg">
                <AlertTriangle className="h-6 w-6 text-white" />
              </div>
              <h1 className="text-xl font-bold">ResQ Vision</h1>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <div className="h-2 w-2 bg-green-400 rounded-full"></div>
            <span className="text-sm text-gray-300">System Online</span>
          </div>
        </div>
      </nav>

      <div className="flex">
        {/* Sidebar */}
        <div className={`${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} lg:translate-x-0 fixed lg:static inset-y-0 left-0 z-50 w-64 bg-gray-800 transition-transform duration-300 ease-in-out`}>
          <div className="flex items-center justify-between p-4 lg:hidden">
            <span className="text-lg font-semibold">Menu</span>
            <button
              onClick={() => setSidebarOpen(false)}
              className="text-gray-300 hover:text-white"
            >
              <X className="h-6 w-6" />
            </button>
          </div>
          <nav className="mt-8 px-4">
            <ul className="space-y-2">
              {sidebarItems.map((item, index) => (
                <li key={index}>
                  <a
                    href="#"
                    className={`flex items-center space-x-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                      item.active
                        ? 'bg-blue-600 text-white'
                        : 'text-gray-300 hover:bg-gray-700 hover:text-white'
                    }`}
                  >
                    <item.icon className="h-5 w-5" />
                    <span>{item.label}</span>
                    {item.active && <ChevronRight className="h-4 w-4 ml-auto" />}
                  </a>
                </li>
              ))}
            </ul>
          </nav>
        </div>

        {/* Main Content */}
        <div className="flex-1 lg:ml-0">
          <div className="p-6">
            {/* Summary Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              {summaryCards.map((card, index) => (
                <div key={index} className="bg-gray-800 rounded-xl p-6 border border-gray-700 hover:border-gray-600 transition-colors">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm text-gray-400 mb-1">{card.title}</p>
                      <p className="text-2xl font-bold">{card.value}</p>
                    </div>
                    <div className={`${card.bgColor} p-3 rounded-lg`}>
                      <card.icon className={`h-6 w-6 ${card.color}`} />
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Main Dashboard Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
              {/* Live Video Preview */}
              <div className="bg-gray-800 rounded-xl p-6 border border-gray-700 lg:col-span-2">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-lg font-semibold">Live Video Preview</h2>
                  <div className="flex items-center space-x-2">
                    <div className="h-2 w-2 bg-red-400 rounded-full animate-pulse"></div>
                    <span className="text-sm text-gray-400">Live</span>
                  </div>
                </div>
                <div className="bg-gray-900 rounded-lg p-8 border border-gray-700 aspect-video flex items-center justify-center">
                  <div className="text-center">
                    <Camera className="h-16 w-16 text-gray-600 mx-auto mb-4" />
                    <p className="text-gray-400">No active accident detection</p>
                    <p className="text-sm text-gray-500 mt-2">Monitoring 24 cameras across the city</p>
                  </div>
                </div>
              </div>

              {/* Police Stations */}
              <div className="bg-gray-800 rounded-xl p-6 border border-gray-700">
                <div className="flex items-center space-x-2 mb-4">
                  <Shield className="h-5 w-5 text-blue-400" />
                  <h2 className="text-lg font-semibold">Nearby Police Stations</h2>
                </div>
                <div className="space-y-3">
                  {policeStations.map((station, index) => (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors">
                      <div className="flex items-center space-x-3">
                        <div className="bg-blue-600 p-2 rounded-lg">
                          <Shield className="h-4 w-4 text-white" />
                        </div>
                        <span className="text-sm font-medium">{station.name}</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <MapPin className="h-4 w-4 text-gray-400" />
                        <span className="text-sm text-gray-400">{station.distance}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Hospitals */}
              <div className="bg-gray-800 rounded-xl p-6 border border-gray-700">
                <div className="flex items-center space-x-2 mb-4">
                  <Building2 className="h-5 w-5 text-green-400" />
                  <h2 className="text-lg font-semibold">Nearby Hospitals</h2>
                </div>
                <div className="space-y-3">
                  {hospitals.map((hospital, index) => (
                    <div key={index} className="flex items-center justify-between p-3 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors">
                      <div className="flex items-center space-x-3">
                        <div className="bg-green-600 p-2 rounded-lg">
                          <Building2 className="h-4 w-4 text-white" />
                        </div>
                        <span className="text-sm font-medium">{hospital.name}</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <MapPin className="h-4 w-4 text-gray-400" />
                        <span className="text-sm text-gray-400">{hospital.distance}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Recent Detection Logs */}
            <div className="bg-gray-800 rounded-xl p-6 border border-gray-700">
              <div className="flex items-center space-x-2 mb-4">
                <Clock className="h-5 w-5 text-yellow-400" />
                <h2 className="text-lg font-semibold">Recent Detection Logs</h2>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b border-gray-700">
                      <th className="text-left py-3 px-4 text-sm font-medium text-gray-400">Video Name</th>
                      <th className="text-left py-3 px-4 text-sm font-medium text-gray-400">Detection Time</th>
                      <th className="text-left py-3 px-4 text-sm font-medium text-gray-400">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {detectionLogs.map((log, index) => (
                      <tr key={index} className="border-b border-gray-700 hover:bg-gray-700/50 transition-colors">
                        <td className="py-3 px-4 text-sm font-medium">{log.videoName}</td>
                        <td className="py-3 px-4 text-sm text-gray-400">{log.detectionTime}</td>
                        <td className="py-3 px-4">
                          <StatusBadge status={log.status} color={log.statusColor} />
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          {/* Footer */}
          <footer className="bg-gray-800 border-t border-gray-700 py-4 px-6">
            <div className="text-center text-sm text-gray-400">
              © 2025 ResQ Vision – All rights reserved
            </div>
          </footer>
        </div>
      </div>

      {/* Mobile sidebar overlay */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}
    </div>
  );
}

export default App;