from typing import List, Dict, Any, Optional
from ai_layer.llm_router.policies import RoutingPolicy, TaskComplexity
from ai_layer.llm_router.fallbacks import execute_with_fallbacks
from ai_layer.core.config import settings

# Apply keys to litellm environment
import os
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
os.environ["ANTHROPIC_API_KEY"] = settings.ANTHROPIC_API_KEY

class LLMRouter:
    """
    The central abstraction layer for all LLM calls in the MIR-Ecosystem.
    Agents do not call OpenAI or Anthropic directly; they use this router.
    """

    @staticmethod
    async def generate(
        messages: List[Dict[str, str]], 
        complexity: TaskComplexity = TaskComplexity.MEDIUM,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """
        Generates a response using the appropriate model based on task complexity.
        """
        
        primary_model = RoutingPolicy.get_preferred_model(complexity)
        fallback_models = RoutingPolicy.get_fallback_chain(complexity)

        response = await execute_with_fallbacks(
            messages=messages,
            primary_model=primary_model,
            fallback_models=fallback_models,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # litellm normalizes response objects to look like OpenAI's format
        if response and response.choices:
            return response.choices[0].message.content
        return ""
