
---
title: 'Jina 3.7.0 发布，云原生神经搜索框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3883'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3883'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Jina 是一个神经搜索框架，它使任何人都可以在几分钟内</span>在云上构建可扩展且可持续的神经搜索系统<span style="color:#333333">。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Jina 3.7.0 正式发布，本期主要更新如下：</p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>浮动执行器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以在 Flow 中添加浮动执行器。这种在 Flow 中添加 Executor 的方式可用于正在构建的服务，响应不需要的异步后台任务。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<div style="text-align:start"> 
 <pre><code>f = Flow().add().add(needs=['gateway'],floating=True)</code></pre> 
</div> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4967" target="_blank">#4967 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5004" target="_blank">#5004</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>每个执行器的参数🏃</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>可以使用语法 <code>executorname__paramname</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="color:#24292f">向每个​​ Executor 发送特定参数。</span></p> 
<div style="text-align:start"> 
 <pre><code>from jina import Flow, DocumentArray
with Flow().add(name='exec1').add(name='exec2') as flow:
    flow.index(
        DocumentArray.empty(size=5),
        parameters=&#123;'exec1__traversal_path': '@r', 'exec2__traversal_path': '@c'&#125;,
    )</code></pre> 
</div> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4939" target="_blank">#4939</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>将多个 Executor 端点映射到同一个方法🗺️</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>现在可以将不同的端点动态映射到同一个 Executor。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<div style="text-align:start"> 
 <pre><code>from jina import Flow, requests, Executor, Document, DocumentArray, Client

class MyExec(Executor):
    @requests(on='/foo')
    def foo(self, docs, **kwargs):
        for d in docs:
            d.text = 'foo'


# change bind to bar()
f = Flow().add(uses=MyExec, uses_requests=&#123;'/index': 'foo', '/search': 'foo'&#125;)
with f:
    req = Client(port=f.port).post(
        '/index', Document()
    )

    print(req[0].text)</code></pre> 
</div> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5009" target="_blank">#5009</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从已安装的 Python 模块导入 Executor</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<div style="text-align:start"> 
 <pre><code>f = Flow().add(uses='MyExecutor', py_modules=['module.path.to.my_executor'])</code></pre> 
</div> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4954" target="_blank">#4954 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5013" target="_blank">#5013</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在每个 Runtime 上公开 Jina 环境信息ℹ️</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>每个 Flow 微服务都提供一个端点，该端点公开有关其运行环境的相关信息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4902" target="_blank">#4902</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li>在本地运行 Flow 时，支持为每个副本传递不同的监控端口 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4961" target="_blank">#4961</a></li> 
 <li>在日志中显示副本的监控端口 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4956" target="_blank">#4956</a></li> 
 <li>无需序列化 DocumentArray protobuf ，即可从 Request 中高效访问参数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4991" target="_blank">#4991</a></li> 
 <li>从网关异步发送收集端点请求，而不等待它们 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5015" target="_blank">#5015</a></li> 
</ul> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li>修复网关如何处理预取的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F5012" target="_blank">#5012</a></li> 
 <li>修复网关尝试重新连接到重新生成的执行器时观察到的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4941" target="_blank">#4941</a></li> 
 <li>修复存在通信异常时某些监控指标的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4974" target="_blank">#4974</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Freleases%2Ftag%2Fv3.7.0" target="_blank">https://github.com/jina-ai/jina/releases/tag/v3.7.0</a></p>
                                        </div>
                                      
</div>
            