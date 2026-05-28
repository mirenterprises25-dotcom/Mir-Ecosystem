import EnterpriseLayout from '@/components/layout/EnterpriseLayout';

export default function OperationsDashboard() {
  return (
    <EnterpriseLayout>
      <div className="max-w-7xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-gray-800/60 pb-6">
          <div>
            <div className="flex items-center gap-3">
              <div className="h-3 w-3 rounded-full bg-indigo-400 animate-pulse"></div>
              <h2 className="text-3xl font-bold text-white tracking-tight">Agent 2: Operations & BI</h2>
            </div>
            <p className="mt-2 text-sm text-gray-400">
              Real-time trend analysis, pricing strategies, and inventory forecasting.
            </p>
          </div>
        </div>

        {/* Insights Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-gradient-to-br from-indigo-900/40 to-[#141720]/80 rounded-2xl border border-indigo-500/30 p-6 relative overflow-hidden">
             <div className="absolute top-0 right-0 p-4 opacity-20">
               <svg xmlns="http://www.w3.org/2000/svg" className="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>
             </div>
             <h3 className="text-indigo-300 font-semibold mb-1">Viral Trend Detected</h3>
             <p className="text-2xl font-bold text-white mb-2">Leather Jackets</p>
             <p className="text-sm text-indigo-200/70">Demand up 300% across social channels. Agent recommends +5% price increase.</p>
             <button className="mt-4 text-xs font-semibold text-white bg-indigo-500 px-3 py-1.5 rounded hover:bg-indigo-600 transition-colors">Apply Pricing Strategy</button>
          </div>
          
          <div className="bg-[#141720]/80 rounded-2xl border border-gray-800/60 p-6">
             <h3 className="text-gray-400 font-semibold mb-1">Inventory Alert</h3>
             <p className="text-2xl font-bold text-white mb-2">Stock Low</p>
             <p className="text-sm text-gray-500">Only 45 Leather Jackets remaining. Expected to stock out in 48 hours at current velocity.</p>
          </div>

          <div className="bg-[#141720]/80 rounded-2xl border border-gray-800/60 p-6">
             <h3 className="text-gray-400 font-semibold mb-1">Competitor Analysis</h3>
             <p className="text-2xl font-bold text-white mb-2">Stable</p>
             <p className="text-sm text-gray-500">Zara dropped prices by 2%, but overall market positioning remains optimal.</p>
          </div>
        </div>

        {/* Data Table Placeholder */}
        <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 overflow-hidden">
          <div className="px-6 py-4 border-b border-gray-800/60 flex justify-between items-center">
            <h3 className="text-sm font-semibold text-gray-200">Product Line Forecast</h3>
            <span className="text-xs text-gray-500">Updated: 10 mins ago</span>
          </div>
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-gray-800/60 text-xs uppercase text-gray-500 bg-gray-900/30">
                <th className="px-6 py-3 font-medium">Product</th>
                <th className="px-6 py-3 font-medium">Current Stock</th>
                <th className="px-6 py-3 font-medium">Velocity (30d)</th>
                <th className="px-6 py-3 font-medium">AI Recommendation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-800/60">
              <tr className="hover:bg-gray-800/30">
                <td className="px-6 py-4 text-sm text-gray-200">Leather Jackets</td>
                <td className="px-6 py-4 text-sm text-red-400 font-medium">45</td>
                <td className="px-6 py-4 text-sm text-gray-400">High (+300%)</td>
                <td className="px-6 py-4 text-sm text-indigo-400">Restock Urgently, +5% Price</td>
              </tr>
              <tr className="hover:bg-gray-800/30">
                <td className="px-6 py-4 text-sm text-gray-200">Tracksuits</td>
                <td className="px-6 py-4 text-sm text-emerald-400 font-medium">500</td>
                <td className="px-6 py-4 text-sm text-gray-400">Stable</td>
                <td className="px-6 py-4 text-sm text-gray-500">Hold Position</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </EnterpriseLayout>
  );
}
