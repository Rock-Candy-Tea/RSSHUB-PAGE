
---
title: 'Jina 3.0.0 正式发布，云原生神经搜索框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7896'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7896'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Jina 是一个神经搜索框架，它使任何人都可以在几分钟内</span>在云上构建可扩展且可持续的神经搜索系统<span style="color:#333333">。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Jina 3.0.0 正式发布，该版本的内容主要关于<strong>云就绪和集成（cloud-readiness and integration），</strong>通过重构架构/通信层，使 Executor 通信更稳定，比以前版本<strong>更具可扩展性和健壮性。</strong></p> 
<h2 style="margin-right:0; text-align:start"><strong>Executors: 试用功能</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">使用 Jina 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jina.ai%2Fhow-to%2Fsandbox%2F" target="_blank">新沙箱</a>，甚至不需要从<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.jina.ai%2F" target="_blank">Jina Hub</a>下载 Executor 来测试。只需使用<span> </span><code>jinahub+sandbox://ExecutorName</code>，就可以<strong>在云上运行该 Executor</strong>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这意味着可以更快地评估 Executors ，以找到适合的执行程序，无需下载任何内容或使用本地计算。</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">from docarray import Document
from jina import Flow

flow = Flow().add(uses='jinahub+sandbox://Hello')

with flow:
  docs = flow.post('/', inputs=Document(text='world'))
  print(docs.texts)</pre> 
<h3 style="margin-right:0; text-align:start">Flow：<strong>使用 Kubernetes 和 Docker Compose 运行</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jina.ai%2Fhow-to%2Fkubernetes%2F" target="_blank"><strong>Kubernetes</strong></a><strong>：</strong><span style="color:#2e3033">使用<span> </span><code>Flow .to_k8s_yaml('./k8s_flow')</code><span> </span>从一个 Flow 中生成一组部署的 YAML 文件，然后使用 Kubernetes 和 kubectl 来启动和协调 Executors。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jina.ai%2Fhow-to%2Fdocker-compose%2F" target="_blank"><strong>Docker Compose</strong></a><strong>：</strong><span> </span>使用<span> </span><code>flow.to_docker_compose_yaml()</code><span> </span>从<span style="color:#2e3033">一个 Flow 中</span>生成一个<span> </span><code>docker-compose.yml</code><span> </span>文件，然后运行<span> </span><code>docker-compose up</code><span> </span>。</li> 
</ul> 
<h2 style="margin-right:0; text-align:start"><strong>DocumentArray：可视化、共享、文档存储</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该版本将 Jina 的 DocumentArray 拆分为自己的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocarray.jina.ai%2F" target="_blank"><code>docarray</code></a><span> </span>包，<span style="color:#24292f">让 Jina 专注于扩展云上的非结构化数据处理：</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>2.x</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">from jina import Document, DocumentArray, Flow</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>3.0</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:start">from docarray import Document, DocumentArray
from jina import Flow</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这意味着 Jina 受益于 3.0 版本在 Document 和 DocumentArray 中所做的所有改进，包括<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocarray.jina.ai%2Ffundamentals%2Fdocumentarray%2Fvisualization%2F" target="_blank"><strong>强大的可视化</strong></a>和对<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocarray.jina.ai%2Fadvanced%2Fdocument-store%2F" target="_blank"><strong>多个文档存储</strong></a>的支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">要了解 Jina 3.0.0 的更多信息，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jina.ai%2Fget-started%2Fmigrate%2F" target="_blank">迁移指南</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jina.ai%2F" target="_blank">文档</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2F" target="_blank">全新的 README</a>。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新特性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fc07f3c151d985b207af87ccc9115bc94c3164e55" target="_blank"><code>c07f3c15</code></a>]<span> </span><strong>-</strong>推送后添加沙箱（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4349" target="_blank">#4349</a>）</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F0eae3281cd2afb4582d07616345ddf9b140a7f1f" target="_blank"><code>0eae3281</code></a>]<span> </span><strong>-</strong>添加 blacken docs 到 precommit (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4342" target="_blank">#4342</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fa5935ab2b1cd44e809c20b7e0df0292ba503255d" target="_blank"><code>a5935ab2</code></a>]<span> </span>- hub：将 --verbose 选项添加到“jina hub push”cli (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4278" target="_blank">#4278</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F43bf89862f39edec9ffedb9cffcb7aea962acbaa" target="_blank"><code>43bf8986</code></a>]<span> </span>-<span> </span>沙箱：使用给定端口（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4262" target="_blank">#4262</a>）</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F5081722f360436f2c265dac592eb37c794c29bb5" target="_blank"><code>5081722f</code></a>]<span> </span>- hubble：升级到 hubble api v2 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4269" target="_blank">#4269</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F6e24af633387ca19e0944a71150b82c2add53733" target="_blank"><code>6e24af63</code></a>]<span> </span><strong>-</strong>从 k8s 中隐藏更多参数并编写 yamls (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4242" target="_blank">#4242</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F48871dd73f85c2750baa2a68ce22231e015ada66" target="_blank"><code>48871dd7</code></a>]<span> </span><strong>-</strong>更改从 Executors 返回参数的方式 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4243" target="_blank">#4243</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F1d6c077692c39047c3b234ee3ecc8945a6ade1c0" target="_blank"><code>1d6c0776</code></a>]<span> </span><strong>-</strong>使用来自 k8s 的外部 pod (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4223" target="_blank">#4223</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F6a9ed78f13905fb78c786914d5da1733dd20caf9" target="_blank"><code>6a9ed78f</code></a>]<span> </span><strong>-</strong>将 docarray 集成为外部依赖项 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4160" target="_blank">#4160</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Feea04c36350e86b3b0f16217cd37e630bfb81b57" target="_blank"><code>eea04c36</code></a>]<span> </span><strong>-</strong>支持 jinahub+sandbox (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4130" target="_blank">#4130</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fa813b15132df422aa9b5c0925cf62e587ad0aa61" target="_blank"><code>a813b151</code></a>]<span> </span><strong>-</strong>将流程导出到 docker compose yaml (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4125" target="_blank">#4125</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2Fdef0a12f6a312b1133d10750226f485b42e319f8" target="_blank"><code>def0a12f</code></a>]<span> </span><strong>-</strong>Flow 后返回 DocumentArray (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4137" target="_blank">#4137</a><span> </span>)</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F6e9e7ef32f61cab04c6efc7a9f21659d26b50fdb" target="_blank"><code>6e9e7ef3</code></a>]<span> </span><strong>-</strong>将 Flow 导出到 k8s yamls 集（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F4089" target="_blank">#4089</a>）</li> 
 <li>[<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fcommit%2F933415bfa1f9eb89f935037014dfed816eb9815d" target="_blank"><code>933415bf</code></a>]<span> </span><strong>-</strong>星形路由 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Fpull%2F3900" target="_blank">#3900</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多内容请查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjina-ai%2Fjina%2Freleases%2Ftag%2Fv3.0.0" target="_blank">https://github.com/jina-ai/jina/releases/tag/v3.0.0</a></p>
                                        </div>
                                      
</div>
            