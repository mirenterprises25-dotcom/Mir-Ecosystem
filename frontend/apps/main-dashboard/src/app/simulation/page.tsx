import EnterpriseLayout from '@/components/layout/EnterpriseLayout';

export default function SimulationDashboard() {
  return (
    <EnterpriseLayout>
      <div className="max-w-7xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-gray-800/60 pb-6">
          <div>
            <div className="flex items-center gap-3">
              <div className="h-3 w-3 rounded-full bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]"></div>
              <h2 className="text-3xl font-bold text-white tracking-tight">Simulation Sandbox</h2>
            </div>
            <p className="mt-2 text-sm text-gray-400">
              Run safely isolated "What-If" scenarios against the cognitive ecosystem.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Controls Panel */}
          <div className="col-span-1 space-y-6">
            
            <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-6">
              <h3 className="text-lg font-semibold text-white mb-4">Macro: Tax Reform</h3>
              <p className="text-sm text-gray-400 mb-6">Simulate changes to Spanish IVA or Corporate Tax rates to calculate margin impacts.</p>
              
              <div className="space-y-4">
                <div>
                  <label className="block text-xs font-medium text-gray-400 mb-1">Target Tax</label>
                  <select className="w-full bg-[#0f1117] border border-gray-700 rounded-md py-2 px-3 text-white text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500">
                    <option>IVA (Impuesto sobre el Valor Añadido)</option>
                    <option>Impuesto de Sociedades (S.L.)</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-medium text-gray-400 mb-1">New General Rate (%)</label>
                  <input type="number" defaultValue={23.0} className="w-full bg-[#0f1117] border border-gray-700 rounded-md py-2 px-3 text-white text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" />
                </div>
                <div>
                  <label className="block text-xs font-medium text-gray-400 mb-1">Effective Date</label>
                  <input type="date" defaultValue="2026-07-01" className="w-full bg-[#0f1117] border border-gray-700 rounded-md py-2 px-3 text-white text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500" />
                </div>
                <button className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2 rounded-md transition-colors shadow-lg shadow-indigo-500/20 mt-2">
                  Run Macro Simulation
                </button>
              </div>
            </div>
            
            <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-6">
              <h3 className="text-lg font-semibold text-white mb-4">Micro: Demand Shock</h3>
              <p className="text-sm text-gray-400 mb-6">Simulate sudden viral trends or supply chain failures.</p>
              <button className="w-full bg-gray-800 hover:bg-gray-700 text-white font-medium py-2 rounded-md transition-colors border border-gray-700">
                Configure Micro Scenario
              </button>
            </div>

          </div>

          {/* Results Panel */}
          <div className="col-span-2 bg-[#141720]/80 rounded-xl border border-indigo-500/20 overflow-hidden flex flex-col relative">
            <div className="absolute top-0 right-0 p-4">
               <span className="inline-flex items-center rounded-md bg-amber-400/10 px-2 py-1 text-xs font-medium text-amber-400 ring-1 ring-inset ring-amber-400/20">Sandbox Environment Active</span>
            </div>
            
            <div className="px-6 py-5 border-b border-gray-800/60">
              <h3 className="text-lg font-semibold text-white">Simulation Results</h3>
              <p className="text-sm text-gray-500">Awaiting execution...</p>
            </div>
            
            <div className="flex-1 p-8 flex flex-col items-center justify-center opacity-50">
               <svg xmlns="http://www.w3.org/2000/svg" className="h-16 w-16 text-gray-600 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
               </svg>
               <p className="text-gray-400 text-center max-w-md">
                 Configure a scenario on the left to inject simulated variables into the Agent's Short-Term Memory.
               </p>
            </div>
          </div>

        </div>
      </div>
    </EnterpriseLayout>
  );
}
