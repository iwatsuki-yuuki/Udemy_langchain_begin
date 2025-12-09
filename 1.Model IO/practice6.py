from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
import config

# 現在はwith_structured_outputを使うと構造化データを抽出できる（今回はやってない）
# JsonOutputParsers
# JsonOutputParserを使って、応答を解析する

model = ChatOpenAI(api_key=config.OPENAI_API_KEY, model="gpt-4o-mini")

class Translatedaword(BaseModel):
    english: str = Field(..., description="英語")
    french: str = Field(..., description="フランス語")
    chinese: str = Field(..., description="中国語")

query = "こんにちは"

parser = JsonOutputParser(pydantic_object=Translatedaword)

prompt = PromptTemplate(
    template = "指定した言語に翻訳\n{format_instructions}\n質問: {query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},

)
query_prompt = prompt.invoke({"query": query})
output = model.invoke(query_prompt)
result = parser.invoke(output)
print(result)
