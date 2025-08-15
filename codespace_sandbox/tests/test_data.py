import pytest
from openai import OpenAI

def test_openai():
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5-nano",
        input="return the string 'OK' if you are working"
    )
    assert response.output_text == "OK"