import EnterpriseLayout from '@/components/layout/EnterpriseLayout';

export default function FinancialDashboard() {
  return (
    <EnterpriseLayout>
      <div className="max-w-7xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-gray-800/60 pb-6">
          <div>
            <div className="flex items-center gap-3">
              <div className="h-3 w-3 rounded-full bg-emerald-400 animate-pulse"></div>
              <h2 className="text-3xl font-bold text-white tracking-tight">Agent 1: Legal & Financial</h2>
            </div>
            <p className="mt-2 text-sm text-gray-400">
              Monitoring BOE compliance, IVA tiers, and Impuesto de Sociedades liabilities.
            </p>
          </div>
          <button className="bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-4 py-2 rounded-md text-sm font-medium hover:bg-emerald-500/20 transition-colors">
            Run Manual Scan
          </button>
        </div>

        {/* Top Widgets */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-5">
            <h4 className="text-gray-400 text-xs font-semibold uppercase tracking-wider mb-2">IVA Liability (Q1)</h4>
            <div className="text-2xl font-bold text-white">€45,200</div>
            <div className="mt-1 flex items-center text-xs text-emerald-400">
              <span>Modelo 303 Projected</span>
            </div>
          </div>
          <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-5">
            <h4 className="text-gray-400 text-xs font-semibold uppercase tracking-wider mb-2">Corporate Tax (S.L.)</h4>
            <div className="text-2xl font-bold text-white">25.0%</div>
            <div className="mt-1 flex items-center text-xs text-gray-500">
              <span>Standard Tier</span>
            </div>
          </div>
          <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-5 border-l-2 border-l-red-500">
            <h4 className="text-gray-400 text-xs font-semibold uppercase tracking-wider mb-2">BOE Alerts</h4>
            <div className="text-2xl font-bold text-white">1</div>
            <div className="mt-1 flex items-center text-xs text-red-400">
              <span>Requires Attention</span>
            </div>
          </div>
          <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-5">
            <h4 className="text-gray-400 text-xs font-semibold uppercase tracking-wider mb-2">Agent Confidence</h4>
            <div className="text-2xl font-bold text-white">96%</div>
            <div className="mt-1 flex items-center text-xs text-indigo-400">
              <span>Based on 530 data points</span>
            </div>
          </div>
        </div>

        {/* Detailed Insights */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* BOE Feed */}
          <div className="col-span-2 bg-[#141720]/80 rounded-xl border border-gray-800/60 overflow-hidden">
            <div className="px-6 py-4 border-b border-gray-800/60 bg-gray-900/30">
              <h3 className="text-sm font-semibold text-gray-200">Live Legal Intelligence Feed (BOE)</h3>
            </div>
            <div className="p-0">
              <div className="divide-y divide-gray-800/60">
                <div className="px-6 py-5">
                  <div className="flex justify-between items-start">
                    <div>
                      <span className="inline-flex items-center rounded-md bg-red-400/10 px-2 py-1 text-xs font-medium text-red-400 ring-1 ring-inset ring-red-400/20 mb-2">Tax Reform Alert</span>
                      <h4 className="text-base font-medium text-white">Proposed changes to IVA brackets</h4>
                      <p className="mt-1 text-sm text-gray-400 max-w-xl">
                        AI analysis detects a proposed bill to increase the general IVA rate to 23%. This would decrease net margins on MIR Clothing by an estimated 1.8% if prices are not adjusted.
                      </p>
                    </div>
                    <button className="text-xs text-indigo-400 font-medium hover:text-indigo-300">View Draft Report</button>
                  </div>
                </div>
                
                <div className="px-6 py-5">
                  <div className="flex justify-between items-start">
                    <div>
                      <span className="inline-flex items-center rounded-md bg-emerald-400/10 px-2 py-1 text-xs font-medium text-emerald-400 ring-1 ring-inset ring-emerald-400/20 mb-2">Routine Compliance</span>
                      <h4 className="text-base font-medium text-white">Modelo 130 Generation Complete</h4>
                      <p className="mt-1 text-sm text-gray-400 max-w-xl">
                        Agent 1 has successfully compiled the draft for Q1 Modelo 130 (Autónomos associated with MIR Consulting). Pending human review before submission.
                      </p>
                    </div>
                    <button className="text-xs text-indigo-400 font-medium hover:text-indigo-300">Review Draft</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Tax Breakdown Chart Stub */}
          <div className="bg-[#141720]/80 rounded-xl border border-gray-800/60 p-6">
            <h3 className="text-sm font-semibold text-gray-200 mb-6">Tax Allocation Overview</h3>
            <div className="flex justify-center items-center h-48">
              {/* CSS Circle Chart */}
              <div className="relative w-40 h-40 rounded-full border-[16px] border-emerald-500/20 border-t-emerald-500 border-r-indigo-500 border-b-emerald-500/20 border-l-emerald-500/20 animate-[spin_10s_linear_infinite]">
                 <div className="absolute inset-0 m-auto w-24 h-24 bg-[#141720] rounded-full flex items-center justify-center animate-[spin_10s_linear_infinite_reverse]">
                   <span className="text-sm text-gray-400 font-semibold">Q1</span>
                 </div>
              </div>
            </div>
            <div className="mt-6 space-y-3">
              <div className="flex justify-between items-center text-sm">
                <span className="text-gray-400 flex items-center gap-2"><div className="w-2 h-2 rounded-full bg-emerald-500"></div> IVA</span>
                <span className="text-white font-medium">65%</span>
              </div>
              <div className="flex justify-between items-center text-sm">
                <span className="text-gray-400 flex items-center gap-2"><div className="w-2 h-2 rounded-full bg-indigo-500"></div> IRPF</span>
                <span className="text-white font-medium">35%</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </EnterpriseLayout>
  );
}
