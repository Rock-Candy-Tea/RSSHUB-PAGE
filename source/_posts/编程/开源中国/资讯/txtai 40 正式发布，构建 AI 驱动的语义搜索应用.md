
---
title: 'txtai 4.0 正式发布，构建 AI 驱动的语义搜索应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 07:51:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
---

<div>   
<div class="content">
                                                                                            <p>txtai 4.0 已正式发布，这是一个具有大量新特性的重要版本，同时也会兼容旧版本，增加了诸如内容存储、对象存储、使用 SQL 查询、索引压缩、重新索引(reindexing)、外部向量等功能。</p> 
<p>数据方面，新版发布之后，代码量增加了 50%，解决了 36 个问题，据称是迄今为止最大的版本。</p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新特性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持存储文本内容（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F168" target="_blank">#168</a>）</li> 
 <li>添加选项以索引内容字典（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F169" target="_blank">#169</a>）</li> 
 <li>添加 SQL 支持以生成结合嵌入 (embedding) + 数据库查询 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F170" target="_blank">#170</a> )</li> 
 <li>将 reindex 方法添加到嵌入（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F171" target="_blank">#171</a>）</li> 
 <li>添加对索引存档的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F172" target="_blank">#172</a>）</li> 
 <li>为嵌入添加关闭方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F173" target="_blank">#173</a>）</li> 
 <li>更新 API 以使用嵌入 + 数据库搜索 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F176" target="_blank">#176</a> )</li> 
 <li>为表格管道 (tabular pipeline) 添加内容选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F177" target="_blank">#177</a>）</li> 
 <li>更新工作流示例以支持嵌入内容 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F179" target="_blank">#179</a> )</li> 
 <li>将索引元数据添加到嵌入配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F180" target="_blank">#180</a>）</li> 
 <li>添加对象存储（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F183" target="_blank">#183</a>）</li> 
 <li>聚类时会聚合部分查询结果（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F184" target="_blank">#184</a>）</li> 
 <li>将函数参数添加到嵌入重新索引（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F185" target="_blank">#185</a>）</li> 
 <li>添加对用户定义的列别名的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F186" target="_blank">#186</a>）</li> 
 <li>使用 SQL 括号表示法支持多词和更复杂的 JSON 路径表达式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F187" target="_blank">#187</a> )</li> 
 <li>支持 SQLite 3.22+ ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F190" target="_blank">#190</a> )</li> 
 <li>添加预先计算的向量支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F192" target="_blank">#192</a>）</li> 
 <li>更改文档/对象插入以仅保留最新记录（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F193" target="_blank">#193</a>）</li> 
 <li>更新包含 4.0 变化的文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F196" target="_blank">#196</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修改工作流以选择带有切片的批处理 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F158" target="_blank">#158</a> )</li> 
 <li>为工作流添加张量支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F159" target="_blank">#159</a> )</li> 
 <li>如果作为文件路径提供，则读取 YAML 配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F162" target="_blank">#162</a> )</li> 
 <li>向 API 添加管道更容易（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F163" target="_blank">#163</a>）</li> 
 <li>支持同时处理任务动作（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F164" target="_blank">#164</a>）</li> 
 <li>添加张量工作流 notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F167" target="_blank">#167</a>）</li> 
 <li>更新默认 ANN 参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F174" target="_blank">#174</a> )</li> 
 <li>要求 Python 3.7+ ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F175" target="_blank">#175</a> )</li> 
 <li>一致地命名嵌入 id 字段（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F178" target="_blank">#178</a>）</li> 
 <li>添加 txtai <strong>版本</strong>属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F181" target="_blank">#181</a>）</li> 
 <li>修改嵌入以仅对输入文档进行一次迭代（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F189" target="_blank">#189</a>）</li> 
 <li>提升向量转换的效率 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F191" target="_blank">#191</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bugfix</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>在 API 写入调用周围添加线程锁 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F160" target="_blank">#160</a> )</li> 
 <li>通过 API 公开 caption 和 objects ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F161" target="_blank">#161</a> )</li> 
 <li>更改 pickle 调用以使用支持最低 Python 版本的协议 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F182" target="_blank">#182</a> )</li> 
 <li>HFOnnx 预期的 ORT provider 错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F195" target="_blank">#195</a> )</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Freleases%2Ftag%2Fv4.0.0" target="_blank">详情查看 release note</a>。</p> 
<p>txtai <span style="background-color:#ffffff; color:#333333">是一个人工智能驱动的搜索引擎，可以在文本的各个部分上建立了一个 AI 驱动的索引。 txtai 支持构建文本索引以执行相似性搜索并创建基于问-答的系统。此外，txtai 还具有用于 zero-shot 分类的功能。</span></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            