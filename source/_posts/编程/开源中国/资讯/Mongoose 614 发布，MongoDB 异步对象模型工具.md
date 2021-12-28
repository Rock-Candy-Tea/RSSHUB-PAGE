
---
title: 'Mongoose 6.1.4 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3194'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3194'
---

<div>   
<div class="content">
                                                                                            <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。Mongoose 6.1.4 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>fix(document): <span style="background-color:#ffffff; color:#2e3033">处理subdoc下未定义嵌套文档的保存 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11110" target="_blank">#11110</a></li> 
 <li>fix(document):<span style="background-color:#ffffff; color:#2e3033">允许使用 create() 手动填充子文档引用 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10856" target="_blank">#10856</a></li> 
 <li>fix(populate): 处理子文档映射下的 refPath <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F9359" target="_blank">#9359</a></li> 
 <li>fix(update): 使用未定义的 id 调用 findByIdAndUpdate 时抛出错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11079" target="_blank">#11079</a></li> 
 <li><span style="color:#24292f">fix(mongoose)</span>：导出 ConnectionStates <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11133" target="_blank">#11133</a></li> 
 <li>fix(index.d.ts): 在使用泛型类型覆盖时解压数组 <code>populate()</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11027" target="_blank">#11027</a></li> 
 <li>fix(index.d.ts): 在 Merge 阶段修复类型<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11132" target="_blank">  #11132</a></li> 
 <li>fix(index.d.ts): PipelineStage.Merge 接口定义错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11109" target="_blank">#11109</a></li> 
 <li>docs(typescript)：在文档定义中添加关于 Schema.Types.ObjectId 与 Types.ObjectId 的注释 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10949" target="_blank">#10949</a></li> 
 <li>docs(connection): 阐明 “connected” 和 “open” 是不同的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10886" target="_blank">#10886</a></li> 
 <li>docs(populate): 添加<span style="color:#2e3033">不使用 on 作为模式路径名的正确 refPath 示例</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11113" target="_blank">#11113</a></li> 
 <li>文档：修复<code>strictQuery</code>示例  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11135" target="_blank">#11135 </a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.1.4" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.1.4</a></p>
                                        </div>
                                      
</div>
            