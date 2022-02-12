
---
title: 'Txtai 4.1.0 发布，人工智能驱动的搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9462'
author: 开源中国
comments: false
date: Sat, 12 Feb 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9462'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">Txtai 4.1.0 现已发布。Txtai 是一个人工智能驱动的搜索引擎，可以在文本的各个部分上建立了一个 AI 驱动的索引。</span><span style="color:#24292f">此版本添加了以下新功能、改进和错误修复：</span></p> 
<p style="margin-left:0"><span style="color:#24292f"><strong>新功能</strong></span></p> 
<ul> 
 <li>添加实体提取管道（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F203" target="_blank">#203</a>）</li> 
 <li>添加工作流调度（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F206" target="_blank">#206</a>）</li> 
 <li>将工作流搜索任务添加到 API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F210" target="_blank">#210</a> )</li> 
 <li>添加控制台任务（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F215" target="_blank">#215</a>）</li> 
 <li>添加导出任务 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F216" target="_blank">#216</a> )</li> 
 <li>添加用于工作流调度的 notebook（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F218" target="_blank">#218</a>）</li> 
</ul> 
<p><span style="color:#24292f"><strong>改进</strong></span></p> 
<ul> 
 <li>使用系统偏好的默认文档主题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F197" target="_blank">#197</a>）</li> 
 <li>改善工作流应用程序的多用户体验（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F198" target="_blank">#198</a>）</li> 
 <li>文档改进（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F200" target="_blank">#200</a>）</li> 
 <li>为文档添加社交​​预览图像 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F201" target="_blank">#201</a> )</li> 
 <li>在所有示例笔记本中添加指向 txtai 的链接（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F202" target="_blank">#202</a>）</li> 
 <li>为 API 搜索方法添加限制参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F208" target="_blank">#208</a> )</li> 
 <li>添加有关本地 API 实例的文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F209" target="_blank">#209</a> )</li> 
 <li>添加用于在 API 中创建工作流任务的速记语法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F211" target="_blank">#211</a> )</li> 
 <li>接受函数作为 API 中的工作流任务操作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F213" target="_blank">#213</a> )</li> 
</ul> 
<p><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>对象检测模型无法加载其他模型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F204" target="_blank">#204</a>）</li> 
 <li>更新单元测试以限制词向量测试的 cpu 使用 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F207" target="_blank">#207</a> )</li> 
 <li>围绕未索引的嵌入实例添加更好的错误处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F212" target="_blank">#212</a>）</li> 
 <li>修复工作流任务无输出时的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F214" target="_blank">#214</a> )</li> 
 <li>为 API 搜索方法添加 lock ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F217" target="_blank">#217</a> )</li> 
</ul> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Freleases%2Ftag%2Fv4.1.0" target="_blank">https://github.com/neuml/txtai/releases/tag/v4.1.0</a></p>
                                        </div>
                                      
</div>
            