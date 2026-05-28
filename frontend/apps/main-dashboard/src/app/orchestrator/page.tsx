import EnterpriseLayout from '@/components/layout/EnterpriseLayout';

export default function OrchestratorDashboard() {
  return (
    <EnterpriseLayout>
      <div className="max-w-7xl mx-auto space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-gray-800/60 pb-6">
          <div>
            <div className="flex items-center gap-3">
              <div className="h-3 w-3 rounded-full bg-purple-500 animate-pulse"></div>
              <h2 className="text-3xl font-bold text-white tracking-tight">Agent 3: Cognitive Governor</h2>
            </div>
            <p className="mt-2 text-sm text-gray-400">
              System-wide orchestration, task delegation, and LLM telemetry.
            </p>
          </div>
        </div>

        {/* Telemetry Metrics */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
           <div className="bg-[#141720]/80 p-4 border border-gray-800/60 rounded-xl">
             <div className="text-xs text-gray-500 uppercase tracking-wide">LLM Router</div>
             <div className="text-xl font-bold text-white mt-1">LiteLLM <span className="text-xs font-normal text-emerald-400 ml-2">Active</span></div>
           </div>
           <div className="bg-[#141720]/80 p-4 border border-gray-800/60 rounded-xl">
             <div className="text-xs text-gray-500 uppercase tracking-wide">Token Usage (24h)</div>
             <div className="text-xl font-bold text-purple-400 mt-1">142.5k <span className="text-xs font-normal text-gray-600">~ $0.42</span></div>
           </div>
           <div className="bg-[#141720]/80 p-4 border border-gray-800/60 rounded-xl">
             <div className="text-xs text-gray-500 uppercase tracking-wide">Avg Latency</div>
             <div className="text-xl font-bold text-white mt-1">1.2s</div>
           </div>
           <div className="bg-[#141720]/80 p-4 border border-gray-800/60 rounded-xl border-b-2 border-b-red-500">
             <div className="text-xs text-gray-500 uppercase tracking-wide">Fallbacks Triggered</div>
             <div className="text-xl font-bold text-white mt-1">3 <span className="text-xs font-normal text-gray-500 ml-1">OpenAI timeouts</span></div>
           </div>
        </div>

        {/* Live RabbitMQ Event Stream */}
        <div className="bg-[#141720] rounded-xl border border-gray-800 flex flex-col h-[500px]">
          <div className="px-4 py-3 border-b border-gray-800 flex items-center justify-between bg-[#11131a] rounded-t-xl">
            <h3 className="text-sm font-semibold text-gray-300 font-mono">Terminal :: RabbitMQ Event Stream</h3>
            <span className="flex h-2 w-2 relative">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
            </span>
          </div>
          <div className="flex-1 p-4 overflow-y-auto font-mono text-sm space-y-2 custom-scrollbar">
            <div className="text-gray-500">[11:24:01.000] <span className="text-blue-400">INFO</span> : Gateway emitted TaskRequested: "Analyze Leather Jackets Launch"</div>
            <div className="text-gray-400">[11:24:01.050] <span className="text-purple-400">ORCH</span> : Task ingested. Routing logic applied.</div>
            <div className="text-gray-500">[11:24:01.100] <span className="text-gray-600">AMQP</span> : Published AgentSubTaskEvent to queue: agent1_queue</div>
            <div className="text-gray-500">[11:24:01.102] <span className="text-gray-600">AMQP</span> : Published AgentSubTaskEvent to queue: agent2_queue</div>
            <div className="text-gray-400">[11:24:02.400] <span className="text-emerald-400">AGT1</span> : AgentResponseEvent received. Status: success</div>
            <div className="text-gray-400">[11:24:03.100] <span className="text-indigo-400">AGT2</span> : AgentResponseEvent received. Status: success</div>
            <div className="text-gray-300">[11:24:03.150] <span className="text-purple-400">ORCH</span> : All subtasks complete. Synthesizing via openai/gpt-4o...</div>
            <div className="text-white font-semibold">[11:24:05.800] <span className="text-emerald-500">DONE</span> : WorkflowCompletedEvent emitted. Trace ID: a8c2-49f2...</div>
          </div>
        </div>

      </div>
    </EnterpriseLayout>
  );
}
