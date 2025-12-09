from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
# StrOutputParsers
# 出力が文字列だけになって、不要な文字がなくなる
# https://reference.langchain.com/python/langchain_core/#langchain_core.output_parsers
from langchain_core.output_parsers import StrOutputParser
import config

llm = ChatOpenAI(api_key=config.OPENAI_API_KEY,model="gpt-4o-mini")

# プロンプトテンプレート
template = "あなたは優秀なPythonの専門家です。次の質問に答えてください。{question}"
prompt = PromptTemplate(input_variables=["question"],template=template)

# 質問を埋め込んでプロンプトを作成する
filled_prompt = prompt.format(question="Pythonとは何ですか？")

response = llm.invoke(filled_prompt)

# 応答を文字列として解析
output_parser = StrOutputParser()
parsed_response = output_parser.invoke(response)

print(parsed_response)