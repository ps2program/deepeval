I'll help you add CLI support for setting up LiteLLM models. Let's first check how the Ollama CLI command is implemented and then create a similar command for LiteLLM.


Search files...
Let me check the key handler to understand how to add new key values for LiteLLM.


Search files...
Based on the codebase analysis, I'll create a CLI command for setting up LiteLLM models. First, let's add the necessary key values to the `KeyValues` enum in `key_handler.py`:



Now, let's add the CLI command for setting up LiteLLM models in `cli/main.py`:



Now, let's update the `metrics/utils.py` file to add support for checking if LiteLLM should be used:



Now users can set up LiteLLM models in two ways:

1. **Using Code**:
```python
from deepeval.models import LiteLLMModel

# Initialize the model
model = LiteLLMModel(
    model="gpt-3.5-turbo",  # or any other model supported by LiteLLM
    api_key="your-api-key",  # optional, can be set via environment variable
    api_base="your-api-base",  # optional, for custom endpoints
    temperature=0
)
```

2. **Using CLI**:
```bash
# Set up a LiteLLM model
deepeval set-litellm gpt-3.5-turbo --api-key="your-api-key" --api-base="your-api-base"

# Remove LiteLLM configuration
deepeval unset-litellm
```

The CLI commands will:
1. Store the model configuration in the key file
2. Set the appropriate flags to use LiteLLM
3. Disable other model providers (Azure OpenAI, Local Model, Gemini)
4. Provide clear feedback messages

The implementation follows the same pattern as other model integrations in the codebase, ensuring consistency and ease of use. Would you like me to make any adjustments to the implementation?
