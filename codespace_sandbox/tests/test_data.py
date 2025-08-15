import pytest
from openai import OpenAI


def test_openai():
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5",
        input="return the string 'OK' if you are working"
    )
    if response.output_text == "OK":
        return True
    else:
        return False