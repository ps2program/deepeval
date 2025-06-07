import pytest
from deepeval.models.llms.litellm_model import LiteLLMModel
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# Initialize the model with LMStudio configuration
model = LiteLLMModel(
    # model="lm_studio/Meta-Llama-3.1-8B-Instruct-GGUF",  # LMStudio uses OpenAI-compatible API
    model="lm_studio/Meta-Llama-3.1-8B-Instruct-GGUF",
    api_key="lm-studio",
    api_base="http://localhost:1234/v1",
    temperature=0,
)

# Test basic generation
prompt = "What is the capital of France?"
response, cost = model.generate(prompt)

# Basic assertions
assert response is not None
assert isinstance(response, str)
assert len(response) > 0
assert cost >= 0

# Test with schema validation
from pydantic import BaseModel

class ResponseSchema(BaseModel):
    answer: str
    confidence: float

prompt = "What is the capital of France? Respond in JSON format with 'answer' and 'confidence' fields."
response, cost = model.generate(prompt, schema=ResponseSchema)

# Schema validation assertions
# assert isinstance(response, ResponseSchema)
# assert hasattr(response, 'answer')
# assert hasattr(response, 'confidence')
# assert isinstance(response.confidence, float)
# assert 0 <= response.confidence <= 1

# Test with AnswerRelevancyMetric
metric = AnswerRelevancyMetric(model=model)
test_case = LLMTestCase(
    input="What is the capital of France?",
    actual_output="Paris is the capital of France.",
    context=["France is a country in Europe. Its capital city is Paris."]
)
score = metric.measure(test_case)

# Metric assertions
assert isinstance(score, float)
assert 0 <= score <= 1
