from langchain_openai import ChatOpenAI
import config

#max tokensやtemperatureなどのパラメータを指定することも可能
# temperatureは応答のランダム性を制御するパラメータで、値が低いほど応答は決定的になり高いほど多様性が増す。
# デフォルトは0.7
llm = ChatOpenAI(api_key=config.OPENAI_API_KEY,model="gpt-4o-mini",temperature=0.5)

messages = [
    (
        "system",
        "あなたは優秀なPythonの専門家です。",
    ),
    ("human", "Pythonとは何ですか？"),
]
ai_msg = llm.invoke(messages)
print(ai_msg)