
---
title: 'txtai 4.3 发布，构建 AI 驱动的语义搜索应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 07:38:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif'
---

<div>   
<div class="content">
                                                                                            <p>txtai 4.3 已发布。txtai<span> </span><span style="background-color:#ffffff; color:#333333">是一个人工智能驱动的搜索引擎，可以在文本的各个部分上建立一个 AI 驱动的索引。 txtai 支持构建文本索引以执行相似性搜索并创建基于问-答的系统。此外，txtai 还具有用于 zero-shot 分类的功能。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2021/0125/132438_duPt_2744687.gif" referrerpolicy="no-referrer"></p> 
<p>txtai 4.3 更新内容如下：</p> 
<p style="text-align:start"><strong>新特性</strong></p> 
<ul> 
 <li>添加涵盖 txtai 嵌入式索引文件结构的 notebook (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F237" target="_blank">#237</a>)</li> 
 <li>添加图像哈希管道 (Image Hash pipeline) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F240" target="_blank">#240</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">在嵌入式查询中添加对自定义 SQL 函数的支持 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F241" target="_blank">#241</a>)</li> 
 <li>为嵌入式 SQL 函数添加 notebook (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F243" target="_blank">#243</a>)</li> 
 <li>添加用于检测近似重复图像的 notebook (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F244" target="_blank">#244</a>)</li> 
</ul> 
<p style="text-align:start"><strong>改进</strong></p> 
<ul> 
 <li>将 SQLException 重命名为 SQLError (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F232" target="_blank">#232</a>)</li> 
 <li>将 API 实例重构为单独的 package (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F233" target="_blank">#233</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">如果尝试修改只读索引，会引起 API 错误 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F235" target="_blank">#235</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">将最后更新字段添加到索引元数据 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F236" target="_blank">#236</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">更新 </span>transcription <span style="background-color:#ffffff; color:#24292f">管道以使用 AutoModelForCTC </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F238" target="_blank">#238</a>)</li> 
</ul> 
<p style="text-align:start"><strong>Bugfix</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">确保始终在嵌入式搜索/批量搜索中设置限制</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F234" target="_blank">#234</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">修复解析多行 SQL 语句时出现的问题 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Fissues%2F242" target="_blank">#242</a>)</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneuml%2Ftxtai%2Freleases%2Ftag%2Fv4.3.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            