import EnterpriseLayout from '@/components/layout/EnterpriseLayout';

export default function Home() {
  return (
    <EnterpriseLayout>
      <div className="max-w-7xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-3xl font-bold text-white tracking-tight">Executive Dashboard</h2>
            <p className="mt-2 text-sm text-gray-400">
              Live cognitive overview of MIR Enterprises operations and compliance.
            </p>
          </div>
        </div>

        {/* Key Metrics Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Agent 1 Metric */}
          <div className="bg-[#0a0a0a]/80 backdrop-blur-xl rounded-2xl border border-red-900/30 p-6 relative overflow-hidden group hover:border-red-500/40 transition-colors">
            <div className="absolute top-0 right-0 w-32 h-32 bg-red-600/5 rounded-bl-full transition-transform group-hover:scale-110"></div>
            <h3 className="text-sm font-medium text-gray-400 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-red-500"></span>
              Agent 1: Legal Compliance
            </h3>
            <div className="mt-4 flex items-end gap-3">
              <span className="text-4xl font-bold text-white">99.8%</span>
            </div>
            <p className="mt-2 text-sm text-red-400">All subsidiaries tax-compliant</p>
          </div>
          
          {/* Agent 2 Metric */}
          <div className="bg-[#0a0a0a]/80 backdrop-blur-xl rounded-2xl border border-red-900/30 p-6 relative overflow-hidden group hover:border-red-500/40 transition-colors">
            <div className="absolute top-0 right-0 w-32 h-32 bg-red-500/5 rounded-bl-full transition-transform group-hover:scale-110"></div>
            <h3 className="text-sm font-medium text-gray-400 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-red-400"></span>
              Agent 2: Market Sentiment
            </h3>
            <div className="mt-4 flex items-end gap-3">
              <span className="text-4xl font-bold text-white">+24%</span>
            </div>
            <p className="mt-2 text-sm text-red-300">Apparel line trending positively</p>
          </div>
          
          {/* Agent 3 Metric */}
          <div className="bg-[#0a0a0a]/80 backdrop-blur-xl rounded-2xl border border-red-900/30 p-6 relative overflow-hidden group hover:border-red-500/40 transition-colors">
            <div className="absolute top-0 right-0 w-32 h-32 bg-red-800/10 rounded-bl-full transition-transform group-hover:scale-110"></div>
            <h3 className="text-sm font-medium text-gray-400 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-red-600"></span>
              Agent 3: Orchestrator Load
            </h3>
            <div className="mt-4 flex items-end gap-3">
              <span className="text-4xl font-bold text-white">12</span>
              <span className="text-sm text-gray-500 font-medium mb-1">Active</span>
            </div>
            <p className="mt-2 text-sm text-gray-400">12 async workflows executing</p>
          </div>
        </div>

        {/* Two Column Layout for deeper insights */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          {/* Recent Cognitive Actions */}
          <div className="bg-[#0a0a0a]/80 backdrop-blur-xl rounded-2xl border border-red-900/30 overflow-hidden flex flex-col">
            <div className="px-6 py-5 border-b border-red-900/30">
              <h3 className="text-lg font-semibold text-white">Recent Cognitive Actions</h3>
            </div>
            <div className="flex-1 p-0 overflow-y-auto max-h-[400px]">
              <div className="divide-y divide-red-900/20">
                <div className="px-6 py-4 hover:bg-red-900/10 transition-colors cursor-default">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-red-600/20 text-red-500 flex items-center justify-center font-bold border border-red-600/30">A3</div>
                      <div>
                        <p className="text-sm font-medium text-gray-200">Synthesized Executive Report</p>
                        <p className="text-xs text-gray-500 mt-0.5">Topic: Launch of Q4 Leather Collection</p>
                      </div>
                    </div>
                    <span className="text-xs font-medium text-gray-500 bg-gray-900 border border-gray-800 px-2 py-1 rounded-md">2 mins ago</span>
                  </div>
                </div>
                
                <div className="px-6 py-4 hover:bg-red-900/10 transition-colors cursor-default">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-red-800/20 text-red-400 flex items-center justify-center font-bold border border-red-800/30">A1</div>
                      <div>
                        <p className="text-sm font-medium text-gray-200">BOE Compliance Scan</p>
                        <p className="text-xs text-gray-500 mt-0.5">No changes to IVA logic detected</p>
                      </div>
                    </div>
                    <span className="text-xs font-medium text-gray-500 bg-gray-800 px-2 py-1 rounded-md">1 hour ago</span>
                  </div>
                </div>
                
                <div className="px-6 py-4 hover:bg-gray-800/30 transition-colors cursor-default">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold border border-purple-500/30">A2</div>
                      <div>
                        <p className="text-sm font-medium text-gray-200">Competitor Pricing Adjusted</p>
                        <p className="text-xs text-gray-500 mt-0.5">Noted 5% drop in Zara leather jackets</p>
                      </div>
                    </div>
                    <span className="text-xs font-medium text-gray-500 bg-gray-800 px-2 py-1 rounded-md">3 hours ago</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* External Chart Integration Container (PowerBI / Recharts) */}
          <div className="bg-[#0a0a0a]/80 backdrop-blur-xl rounded-2xl border border-red-900/30 p-6 flex flex-col">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-white">Financial Forecast</h3>
              <span className="text-xs border border-red-500 text-red-400 px-2 py-1 rounded bg-red-900/20">PowerBI / Recharts Ready</span>
            </div>
            
            <div className="flex-1 rounded-xl bg-black border border-gray-800 flex items-center justify-center relative overflow-hidden min-h-[300px]">
              
              {/* This div represents where a <iframe src="powerbi..."> or <ResponsiveContainer> from Recharts would go */}
              <div className="w-full h-full absolute inset-0 flex flex-col items-center justify-center text-center p-6">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-gray-700 mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <p className="text-gray-500 font-medium text-sm">
                  Connect external reporting engines here.<br/>
                  <span className="text-xs text-gray-600 mt-2 block">Compatible with PowerBI Embedded, Looker, or native React charting libraries like Recharts / Chart.js.</span>
                </p>
              </div>

              {/* Decorative Red Chart bars for the placeholder */}
              <div className="absolute bottom-0 left-0 w-full h-full flex items-end px-12 pb-8 gap-4 opacity-20 pointer-events-none">
                <div className="w-1/6 bg-red-600/40 h-24 rounded-t-md"></div>
                <div className="w-1/6 bg-red-600/60 h-32 rounded-t-md"></div>
                <div className="w-1/6 bg-red-600/80 h-48 rounded-t-md"></div>
                <div className="w-1/6 bg-red-500 h-64 rounded-t-md relative">
                   <div className="absolute -top-3 w-full flex justify-center">
                     <span className="w-2 h-2 rounded-full bg-white shadow-[0_0_10px_white]"></span>
                   </div>
                </div>
                <div className="w-1/6 bg-red-700/40 h-56 rounded-t-md border border-dashed border-red-500/50"></div>
              </div>

            </div>
          </div>
          
        </div>
      </div>
    </EnterpriseLayout>
  );
}
