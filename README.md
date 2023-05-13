# langchain-test

首先，有太多库都是建立在openai基础上了，如果要把它们都重写成requests就太费力了。所以，我们还是要用openai库，因此要在其中加入proxy支持。
方法也很简单，打开 api_requestor.py 文件，搜索session.request，有多处，但是只有一处是写着明文参数的，就在那里加入proxies参数。
此外大概也有通过requests，使用python代码进行全局设置的办法，不过可能考虑很多因素，所以就算了。

