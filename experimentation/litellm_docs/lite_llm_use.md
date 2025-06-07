Let me outline the steps needed to use LiteLLM with DeepEval for evaluation. I'll check how other models are set up and used in the codebase.


Search files...
Let me outline the steps needed to use LiteLLM with DeepEval for evaluation:

1. **Installation**:
```bash
pip install deepeval litellm
```

2. **Model Registration**:
First, we need to register the LiteLLM model in DeepEval's model registry. Add this to `models/__init__.py`:
```python
from deepeval.models.llms import (
    GPTModel,
    AzureOpenAIModel,
    LocalModel,
    OllamaModel,
    AnthropicModel,
    GeminiModel,
    AmazonBedrockModel,
    LiteLLMModel,  # Add this line
)
```

3. **Usage in Metrics**:
You can use the LiteLLM model in any metric that accepts a model parameter. Here are some examples:

```python
from deepeval.models import LiteLLMModel
from deepeval.metrics import GEval, AnswerRelevancyMetric, ContextualRelevancyMetric

# Initialize the model
model = LiteLLMModel(
    model="gpt-3.5-turbo",  # or any other model supported by LiteLLM
    api_key="your-api-key",  # optional, can be set via environment variable
    api_base="your-api-base",  # optional, for custom endpoints
    temperature=0
)

# Use with GEval metric
g_eval = GEval(
    name="my-evaluation",
    evaluation_params=[...],
    model=model,
    threshold=0.5
)

# Use with Answer Relevancy metric
answer_relevancy = AnswerRelevancyMetric(
    model=model,
    threshold=0.5
)

# Use with Contextual Relevancy metric
contextual_relevancy = ContextualRelevancyMetric(
    model=model,
    threshold=0.5
)
```

4. **Environment Variables**:
You can set up environment variables for API keys:
```bash
export LITELLM_API_KEY="your-api-key"
export LITELLM_API_BASE="your-api-base"  # optional
```

5. **Using with Different Providers**:
LiteLLM supports multiple providers. Here are some examples:

```python
# OpenAI
model = LiteLLMModel(model="gpt-3.5-turbo")

# Anthropic
model = LiteLLMModel(model="claude-3-opus")

# Google
model = LiteLLMModel(model="gemini-pro")

# Mistral
model = LiteLLMModel(model="mistral-large")

# Custom endpoint
model = LiteLLMModel(
    model="custom-model",
    api_base="https://your-custom-endpoint.com"
)
```

6. **Using in Benchmarks**:
You can also use the model in benchmarks:

```python
from deepeval.benchmarks import SQuAD, EquityMedQA

# SQuAD benchmark
squad = SQuAD(
    evaluation_model=model,
    verbose_mode=True
)

# Equity Med QA benchmark
equity_med_qa = EquityMedQA(
    model=model
)
```

7. **Async Support**:
The model supports both synchronous and asynchronous operations:

```python
# Sync
result = metric.measure(test_case)

# Async
result = await metric.a_measure(test_case)
```

8. **Schema Validation**:
The model supports schema validation for structured outputs:

```python
from pydantic import BaseModel

class MySchema(BaseModel):
    score: float
    reason: str

result, cost = model.generate(prompt, schema=MySchema)
```

9. **Cost Tracking**:
The model automatically tracks costs for each generation:

```python
result, cost = model.generate(prompt)
print(f"Generation cost: ${cost:.6f}")
```

10. **Error Handling**:
The model includes retry logic and proper error handling:

```python
try:
    result = metric.measure(test_case)
except Exception as e:
    print(f"Error during evaluation: {e}")
```

The implementation is designed to work seamlessly with all DeepEval metrics and benchmarks, providing a unified interface for any LLM provider supported by LiteLLM. Would you like me to explain any of these aspects in more detail?
