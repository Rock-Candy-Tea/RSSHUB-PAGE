
---
title: 'txtai 4.6 发布，项目 2 周年'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 07:44:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">txtai 4.6 已发布，这是 </span>txtai 的第 25 个版本，发布于项目 2 周年纪念日之际<span style="background-color:#ffffff; color:#333333">。</span>txtai 4.6 是一个大型但向后兼容的版本，此版本在嵌入和工作流之间添加了更好的集成；还添加了许多重要的性能改进和错误修复。</p> 
<p><span style="background-color:#ffffff; color:#333333">txtai 是一个人工智能驱动的搜索引擎，可以在文本的各个部分上建立一个 AI 驱动的索引。 txtai 支持构建文本索引以执行相似性搜索并创建基于问 - 答的系统。此外，txtai 还具有用于 zero-shot 分类的功能。</span></p> 
<p><img height="336" src="https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif" width="500" referrerpolicy="no-referrer"></p> 
<p>具体更新内容包括：</p> 
<p><strong>New Features</strong></p> 
<ul> 
 <li>将转换工作流操作添加到应用程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F281" target="_blank">#281</a>）</li> 
 <li>添加在应用程序中解析工作流的能力 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F290" target="_blank">#290</a> )</li> 
 <li>sql 查询语句中的 OFFSET（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F293" target="_blank">#293</a>）</li> 
 <li>添加网页摘要图像生成 notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F299" target="_blank">#299</a>）</li> 
 <li>添加关于用 native code 运行 txtai 的 notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F304" target="_blank">#304</a>）</li> 
 <li>将 mmap 参数添加到 Faiss ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F308" target="_blank">#308</a> )</li> 
 <li>为文档添加索引指南（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F312" target="_blank">#312</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Improvements</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>更新 pipeline workflow notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F292" target="_blank">#292</a>）</li> 
 <li>更新 tabular notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F297" target="_blank">#297</a>）</li> 
 <li>降低 Pillow 库所需的版本以防止不必要的升级 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F303" target="_blank">#303</a> )</li> 
 <li>Embeddings vector batch 改进 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F309" target="_blank">#309</a> )</li> 
 <li>对当前的 pickle 协议使用单个常量（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F310" target="_blank">#310</a>）</li> 
 <li>将量化配置参数移动到 Faiss ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F311" target="_blank">#311</a> )</li> 
 <li>使用新的演示和图表更新文档（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F313" target="_blank">#313</a>）</li> 
 <li>改善大查询限制下的嵌入性能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F318" target="_blank">#318</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>ModuleNotFoundError：没有名为“transformers.hf_api”的模块（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F274" target="_blank">#274</a>）</li> 
 <li>ONNX 和 Protobuf 的依赖性问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F285" target="_blank">#285</a> )</li> 
 <li>key 应该是 writable，而不是path（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fpull%2F287" target="_blank">#287</a>）</li> 
 <li>修复 mkdocstrings bug 对构建脚本的破坏性改变 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F289" target="_blank">#289</a> )</li> 
 <li>在 Embeddings 中插入多种数据类型（文本、文档、对象）时的索引 id 同步问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F294" target="_blank">#294</a>）</li> 
 <li>处理列表字段时 Tabular pipeline 抛出错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F296" target="_blank">#296</a> )</li> 
 <li>txtai 负载测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F305" target="_blank">#305</a>）</li> 
 <li>将云配置添加到 application.upsert 方法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F306" target="_blank">#306</a> )</li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Freleases%2Ftag%2Fv4.6.0" target="_blank">https://github.com/neuml/txtai/releases/tag/v4.6.0</a></p>
                                        </div>
                                      
</div>
            