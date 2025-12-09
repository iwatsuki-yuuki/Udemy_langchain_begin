from langchain_openai import ChatOpenAI
#ChatPromptTemplate
# https://reference.langchain.com/python/langchain_core/prompts/#langchain_core.prompts.chat.ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
import config

llm = ChatOpenAI(api_key=config.OPENAI_API_KEY,model="gpt-4o-mini")
template = ChatPromptTemplate(
    [
        ("system", "あなたは優秀はpythonの専門家です。"),
        ("human", "{user_input}"),
    ]
)

prompt_value = template.invoke(
    {
        "user_input": "Pythonとは何ですか？",
    }
)

response = llm.invoke(prompt_value)

print(response)