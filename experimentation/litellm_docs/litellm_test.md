Yes, we should add tests for the LiteLLM implementation to ensure it works correctly and maintains compatibility with other models. Let me check how other models are tested.


Search files...
Let me check the test directory structure.


Ran tool
I see that there are specific test files for each model implementation, like `test_gemini_model.py` and `test_bedrock.py`. Let's create a similar test file for LiteLLM. I'll create `test_litellm_model.py`:



I've created a comprehensive test file for the LiteLLM model implementation. The tests cover:

1. **Model Initialization**:
   - Testing with different model types (OpenAI, Anthropic)
   - Testing with custom endpoints
   - Testing parameter validation (temperature)

2. **Text Generation**:
   - Basic text generation
   - Generation with schema validation
   - Async generation
   - Raw response generation
   - Sample generation

3. **Cost Calculation**:
   - Testing cost calculation for different types of generations
   - Verifying cost is always a non-negative float

4. **Integration with Metrics**:
   - Testing the model with GEval metric
   - Testing with test cases

5. **Error Handling**:
   - Testing invalid parameters
   - Testing response validation

The tests follow the same pattern as other model tests in the codebase (like `test_gemini_model.py` and `test_bedrock.py`).

To run these tests, users can use:
```bash
# Run all tests
pytest

# Run only LiteLLM tests
pytest tests/test_litellm_model.py

# Run with verbose output
pytest -v tests/test_litellm_model.py
```

Would you like me to add any additional test cases or make any adjustments to the existing ones?
