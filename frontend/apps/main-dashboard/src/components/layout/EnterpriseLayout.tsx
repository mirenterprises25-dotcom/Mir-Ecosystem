import React from 'react';
import Link from 'next/link';

export default function EnterpriseLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen bg-[#0f1117] text-gray-100 font-sans selection:bg-indigo-500 selection:text-white">
      {/* Sidebar */}
      <aside className="w-64 bg-[#0a0a0a] border-r border-red-900/30 flex flex-col transition-all duration-300">
        <div className="h-16 flex items-center justify-center border-b border-red-900/30">
          <Link href="/" className="text-xl font-bold tracking-wider bg-gradient-to-r from-red-600 to-red-400 bg-clip-text text-transparent">
            MIR <span className="font-light text-gray-400">ECOSYSTEM</span>
          </Link>
        </div>
        
        <nav className="flex-1 p-4 space-y-2 mt-4">
          <Link href="/" className="block px-4 py-2.5 bg-red-600/10 text-red-400 hover:bg-red-600/20 hover:text-red-300 rounded-lg text-sm font-medium transition-all duration-200 border border-red-500/20 shadow-[0_0_15px_rgba(220,38,38,0.15)]">
            Executive Overview
          </Link>
          <Link href="/financial" className="block px-4 py-2.5 text-gray-400 hover:text-gray-100 hover:bg-red-900/20 rounded-lg text-sm font-medium transition-all duration-200 border border-transparent hover:border-red-900/50">
            Agent 1: Legal & Financial
          </Link>
          <Link href="/operations" className="block px-4 py-2.5 text-gray-400 hover:text-gray-100 hover:bg-red-900/20 rounded-lg text-sm font-medium transition-all duration-200 border border-transparent hover:border-red-900/50">
            Agent 2: Operations & BI
          </Link>
          <Link href="/orchestrator" className="block px-4 py-2.5 text-gray-400 hover:text-gray-100 hover:bg-red-900/20 rounded-lg text-sm font-medium transition-all duration-200 border border-transparent hover:border-red-900/50">
            Agent 3: Orchestrator Log
          </Link>
          
          <div className="pt-6 mt-6 border-t border-red-900/30">
            <h4 className="px-4 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Tools</h4>
            <Link href="/simulation" className="block px-4 py-2.5 text-gray-300 hover:text-white bg-red-900/10 hover:bg-red-900/30 rounded-lg text-sm font-medium transition-all duration-200 border border-red-500/20">
              Simulation Sandbox
            </Link>
          </div>
        </nav>
        
        {/* User Profile */}
        <div className="p-4 border-t border-red-900/30 bg-[#050505]">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-red-600 to-red-900 flex items-center justify-center text-sm font-bold shadow-lg shadow-red-600/30">
              M
            </div>
            <div className="text-sm">
              <p className="font-medium text-gray-200">MIR Enterprises</p>
              <p className="text-xs text-red-500">Super Admin</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden relative bg-black">
        {/* Glow effects in background */}
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-red-900/10 rounded-full blur-[100px] pointer-events-none"></div>
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-red-800/5 rounded-full blur-[100px] pointer-events-none"></div>

        {/* Top Navbar */}
        <header className="h-16 bg-black/80 backdrop-blur-md border-b border-red-900/30 flex items-center justify-between px-8 z-10 sticky top-0">
          <div className="flex items-center gap-2">
            <div className="h-2 w-2 rounded-full bg-red-500 animate-pulse"></div>
            <span className="text-xs font-medium text-gray-400 tracking-wide">SYSTEM: <span className="text-red-500">NOMINAL</span></span>
          </div>
          <div className="flex items-center gap-4">
            <button className="relative text-gray-400 hover:text-red-500 transition-colors">
              <span className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full border-2 border-[#0f1117]"></span>
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
            </button>
          </div>
        </header>

        {/* Dynamic Content */}
        <div className="flex-1 overflow-auto p-8 z-10 custom-scrollbar">
          {children}
        </div>
      </main>
    </div>
  );
}
