from langchain_community.document_loaders import PyPDFLoader
import os

# 外部データを読み込んでdocumentsに格納
# カレントディレクトリをスクリプトの場所に変更
main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

loader = PyPDFLoader("LangChain株式会社IR資料.pdf")
documents = loader.load()
print(documents)