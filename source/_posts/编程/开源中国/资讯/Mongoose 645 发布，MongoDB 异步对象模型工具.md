
---
title: 'Mongoose 6.4.5 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5828'
author: 开源中国
comments: false
date: Wed, 20 Jul 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5828'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#333333">Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。Mongoose 6.4.5 现已发布，具体更新内容包括：</span></p> 
<ul> 
 <li>fix(model+timestamps)：在 insertMany() 中设置子文档的时间戳 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F12060" target="_blank">#12060</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix</span>：纠正 isAtlas 检查 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12110" target="_blank">#12110</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：修复自动 typed 模式的各种问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12042" target="_blank">#12042</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：允许 AddFields 的任何值 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F12096" target="_blank">#12096</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：允许 ConcatArrays 的任意表达式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F12058" target="_blank">#12058</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：使 $addToSet 字段可变以允许以编程方式构建 $addToSet <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F12091" target="_blank">#12091</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：将 $let 作为可能的表达式添加到 $addFields <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12087" target="_blank">#12087</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：修复 $switch 表达式类型<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12088" target="_blank">#12088</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：syncIndexes() 的正确选项类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12101" target="_blank">＃12101</a></li> 
 <li><span style="background-color:#ffffff; color:#24292f">fix(types)</span>：在<code>Require_id</code>中避免将|未定义的类型视为任何类型，以更好地支持<code>_id: String</code><span style="background-color:#ffffff; color:#24292f">auto-typed </span>模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F12070" target="_blank">#12070</a></li> 
 <li>docs：修复各种 jsdoc 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12086" target="_blank">#12086</a></li> 
 <li>docs：将 sanitizeFilter 添加到 mongoose.set() 选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F12112" target="_blank">#12112</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.4.5" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.4.5</a></p>
                                        </div>
                                      
</div>
            