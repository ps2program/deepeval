I'll help you create a documentation page for the LiteLLM integration, following a similar structure to the Ollama documentation. Here's the content:

```markdown
# LiteLLM Integration

DeepEval allows you to use any model supported by LiteLLM to run evals, either through the CLI or directly in Python.

## Prerequisites

Before getting started, make sure you have LiteLLM installed:
```bash
pip install litellm
```

## Command Line

To configure your LiteLLM model through the CLI, run the following command. Replace `gpt-3.5-turbo` with any LiteLLM-supported model of your choice:

```bash
deepeval set-litellm gpt-3.5-turbo
```

You can also specify additional parameters:

```bash
# With API key
deepeval set-litellm gpt-3.5-turbo --api-key="your-api-key"

# With custom API base
deepeval set-litellm gpt-3.5-turbo --api-base="https://your-custom-endpoint.com"

# With both API key and custom base
deepeval set-litellm gpt-3.5-turbo \
    --api-key="your-api-key" \
    --api-base="https://your-custom-endpoint.com"
```

> **Note**: The CLI command above sets LiteLLM as the default provider for all metrics, unless overridden in Python code. To use a different default model provider, you must first unset LiteLLM:

```bash
deepeval unset-litellm
```

## Python

Alternatively, you can specify your model directly in code using `LiteLLMModel` from DeepEval's model collection:

```python
from deepeval.models import LiteLLMModel
from deepeval.metrics import AnswerRelevancyMetric

model = LiteLLMModel(
    model="gpt-3.5-turbo",  # or any other model supported by LiteLLM
    api_key="your-api-key",  # optional, can be set via environment variable
    api_base="your-api-base",  # optional, for custom endpoints
    temperature=0
)

answer_relevancy = AnswerRelevancyMetric(model=model)
```

### Parameters

The `LiteLLMModel` class accepts the following parameters:

- `model` (required): A string specifying the name of the LiteLLM model to use
- `api_key` (optional): A string specifying the API key for the model
- `api_base` (optional): A string specifying the base URL for the model API
- `temperature` (optional): A float specifying the model temperature. Defaults to 0

## Supported Models

LiteLLM supports a wide range of models from various providers. Here are some examples:

### OpenAI Models
- gpt-3.5-turbo
- gpt-4
- gpt-4-turbo-preview

### Anthropic Models
- claude-3-opus
- claude-3-sonnet
- claude-3-haiku

### Google Models
- gemini-pro
- gemini-ultra

### Mistral Models
- mistral-small
- mistral-medium
- mistral-large

### Custom Models
You can also use any custom model by specifying the appropriate API base and model name.

> **Note**: For a complete list of supported models and their capabilities, refer to the [LiteLLM documentation](https://docs.litellm.ai/docs/providers).

## Environment Variables

You can also configure LiteLLM using environment variables:

```bash
# OpenAI
export OPENAI_API_KEY="your-api-key"

# Anthropic
export ANTHROPIC_API_KEY="your-api-key"

# Google
export GOOGLE_API_KEY="your-api-key"

# Custom endpoint
export LITELLM_API_BASE="https://your-custom-endpoint.com"
```

## Examples

### Basic Usage
```python
from deepeval.models import LiteLLMModel
from deepeval.metrics import AnswerRelevancyMetric

model = LiteLLMModel(model="gpt-3.5-turbo")
metric = AnswerRelevancyMetric(model=model)
```

### Using Custom Endpoint
```python
model = LiteLLMModel(
    model="custom-model",
    api_base="https://your-custom-endpoint.com",
    api_key="your-api-key"
)
```

### Using Different Providers
```python
# Anthropic
model = LiteLLMModel(model="claude-3-opus")

# Google
model = LiteLLMModel(model="gemini-pro")

# Mistral
model = LiteLLMModel(model="mistral-large")
```

### Using with Schema Validation
```python
from pydantic import BaseModel

class ResponseSchema(BaseModel):
    score: float
    reason: str

model = LiteLLMModel(model="gpt-3.5-turbo")
response, cost = model.generate(
    "Rate this answer: 'The capital of France is Paris'",
    schema=ResponseSchema
)
```

## Best Practices

1. **API Key Security**: Store your API keys in environment variables rather than hardcoding them in your scripts.

2. **Model Selection**: Choose the appropriate model based on your needs:
   - For simple tasks: Use smaller models like `gpt-3.5-turbo`
   - For complex reasoning: Use larger models like `gpt-4` or `claude-3-opus`
   - For cost-sensitive applications: Use models like `mistral-small` or `claude-3-haiku`

3. **Error Handling**: Implement proper error handling for API rate limits and connection issues.

4. **Cost Management**: Monitor your usage and costs, especially when using larger models.

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure your API key is valid and has sufficient permissions
   - Check if the API key is properly set in environment variables

2. **Connection Issues**
   - Verify your internet connection
   - Check if the API endpoint is accessible
   - Ensure your firewall isn't blocking the connection

3. **Model Availability**
   - Confirm the model is available in your region
   - Check if you have access to the model with your API key

### Getting Help

If you encounter any issues:
1. Check the [LiteLLM documentation](https://docs.litellm.ai/)
2. Visit the [DeepEval GitHub repository](https://github.com/confident-ai/deepeval)
3. Join the [DeepEval Discord community](https://discord.gg/confident-ai)
```

This documentation provides a comprehensive guide for using the LiteLLM integration in DeepEval, covering both CLI and Python usage, supported models, best practices, and troubleshooting. Would you like me to make any adjustments to the content?
