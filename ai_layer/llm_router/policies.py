from enum import Enum
from typing import List, Dict

class TaskComplexity(Enum):
    LOW = "low"         # Basic formatting, extraction, simple chat
    MEDIUM = "medium"   # Summarization, simple reasoning
    HIGH = "high"       # Complex legal analysis, financial forecasting, orchestration

class RoutingPolicy:
    """
    Determines which model to use based on task complexity and current load.
    """
    
    # Model tiers defined by provider/model-name format required by LiteLLM
    TIER_1_MODELS = ["openai/gpt-4o", "anthropic/claude-3-5-sonnet-20240620"]
    TIER_2_MODELS = ["openai/gpt-3.5-turbo", "anthropic/claude-3-haiku-20240307"]
    TIER_3_MODELS = ["ollama/llama3"] # Local models

    @classmethod
    def get_preferred_model(cls, complexity: TaskComplexity) -> str:
        """Returns the primary model for a given complexity level."""
        if complexity == TaskComplexity.HIGH:
            return cls.TIER_1_MODELS[0]
        elif complexity == TaskComplexity.MEDIUM:
            return cls.TIER_2_MODELS[0]
        else:
            return cls.TIER_3_MODELS[0]

    @classmethod
    def get_fallback_chain(cls, complexity: TaskComplexity) -> List[str]:
        """Returns the fallback chain if the preferred model fails."""
        if complexity == TaskComplexity.HIGH:
            return cls.TIER_1_MODELS[1:] + cls.TIER_2_MODELS
        elif complexity == TaskComplexity.MEDIUM:
            return cls.TIER_2_MODELS[1:] + cls.TIER_1_MODELS
        else:
            return cls.TIER_2_MODELS # Fallback to cheap cloud if local fails
