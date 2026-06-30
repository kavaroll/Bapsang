from openai import OpenAI

from app.config import VLLM_URL


class LLM:

    def __init__(self):

        self.client = OpenAI(
            api_key="EMPTY",
            base_url=f"{VLLM_URL}/v1",
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model="Qwen",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content