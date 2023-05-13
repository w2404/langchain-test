import os
import config
os.environ['OPENAI_API_KEY']=config.key

#读取bilibili视频
#from langchain.document_loaders.bilibili import BiliBiliLoader
#loader = BiliBiliLoader(
#    ["https://www.bilibili.com/video/BV1xt411o7Xu/"]
#)
#loader.load()

from langchain.document_loaders import TextLoader
loader = TextLoader('./3.txt') #../state_of_the_union.txt')

#生成index
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])


query = "描述下这篇文档的内容"
s1=index.query(query)
print(s1)
s2=index.query_with_sources(query)
print(s2)
