# Langchainを使ってOpenAIのチャットモデルを呼び出すサンプルコード
#　一様今の所は以下のリンクを読めばできる
# https://docs.langchain.com/oss/python/integrations/chat/openai
from langchain_openai import ChatOpenAI
import config


llm = ChatOpenAI(api_key=config.OPENAI_API_KEY,model="gpt-4o-mini")

messages = [
    (
        "system",
        "あなたは優秀なPythonの専門家です。",
    ),
    ("human", "Pythonとは何ですか？"),
]
ai_msg = llm.invoke(messages)
print(ai_msg)