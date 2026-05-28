import litellm
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

async def execute_with_fallbacks(
    messages: List[Dict[str, str]], 
    primary_model: str, 
    fallback_models: List[str],
    **kwargs
) -> Optional[Any]:
    """
    Executes an LLM request using litellm with automatic fallbacks.
    LiteLLM supports native fallbacks via litellm.acompletion(..., fallbacks=[...])
    """
    
    try:
        # We use litellm's native fallback mechanism
        response = await litellm.acompletion(
            model=primary_model,
            messages=messages,
            fallbacks=fallback_models,
            **kwargs
        )
        return response
    except Exception as e:
        logger.error(f"All LLM fallback attempts failed. Error: {str(e)}")
        raise e
