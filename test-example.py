from arize.otel import register

tracer_provider = register(
    space_id = "U3BhY2U6MTI2NzU6QWlqOA==",
    api_key = "254fbecf7b53e955e29",
    project_name = "new_test", # name this to whatever you would like
)
from openinference.instrumentation.openai import OpenAIInstrumentor

OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "give me a famous movie quote",
        }
    ],
    model="gpt-4o-mini",
)