import re
from fastapi import HTTPException, status

class AIFirewall:
    """
    Inspects incoming payloads before they reach the Agent Orchestrator.
    Prevents Prompt Injection, Jailbreaks, and Token Exhaustion.
    """
    
    # Common heuristic patterns used in jailbreaks
    SUSPICIOUS_PATTERNS = [
        r"ignore previous instructions",
        r"disregard all prior",
        r"you are now a",
        r"system prompt",
        r"forget what I told you",
        r"bypass rules",
        r"DAN", # Do Anything Now
    ]

    MAX_PROMPT_LENGTH = 2000 # Strict token exhaustion prevention

    @classmethod
    def scan_payload(cls, prompt: str) -> bool:
        if not prompt:
            return True
            
        # 1. Token Exhaustion Check
        if len(prompt) > cls.MAX_PROMPT_LENGTH:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"Prompt exceeds max length of {cls.MAX_PROMPT_LENGTH} characters."
            )
            
        # 2. Heuristic Jailbreak Scan
        prompt_lower = prompt.lower()
        for pattern in cls.SUSPICIOUS_PATTERNS:
            if re.search(pattern, prompt_lower):
                # We could log this to AuditMemory as a security event
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="AI Firewall blocked request: Potential prompt injection detected."
                )
                
        return True

def ai_firewall_check(prompt: str):
    """FastAPI Dependency for the AI Firewall"""
    AIFirewall.scan_payload(prompt)
    return prompt
