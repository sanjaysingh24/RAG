import os 
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
load_dotenv()

class AgentConfig:
    def __init__(self):
        self.huggingFace_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        self.llm = self._init_llm()
    def _init_llm(self):
        return HuggingFaceEndpoint(
            repo_id="Qwen/Qwen2.5-7B-Instruct",
            task="text-generation",
            max_new_tokens=2048,
            huggingfacehub_api_token=self.huggingFace_api_key
        )