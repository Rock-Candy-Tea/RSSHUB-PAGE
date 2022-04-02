
---
title: 'Webpack v5.71.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8070'
author: 开源中国
comments: false
date: Sat, 02 Apr 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8070'
---

<div>   
<div class="content">
                                                                                            <p>Webpack v5.71.0 已发布，带来如下改动：</p> 
<h3>特性</h3> 
<ul> 
 <li>使用包含占位符的 output.library 时，为 uniqueName 选择更智能的默认值</li> 
 <li>支持带有 in 导入绑定的表达式</li> 
 <li>尽可能使用箭头函数生成 UMD 代码</li> 
</ul> 
<h3 style="margin-left:0px"><strong>Bug 修复</strong></h3> 
<ul> 
 <li>将 ContextModule 的源映射源名称修复为 <span style="color:#24292f">relative</span></li> 
 <li>修复模块模块中的 chunkLoading 选项 </li> 
 <li>修复 evaluateExpression 返回 null 的边缘情况 </li> 
 <li>在导入的绑定中保留可选链 </li> 
 <li>即使不使用块加载，也包括基本 URI 的运行时代码 </li> 
 <li>通过 ESM 导入 node.js 内置模块时，不在持久缓存中抛出错误 </li> 
 <li>修复使用 <code>lazy-once</code>上下文模块时的崩溃</li> 
 <li>改进对具有多个上下文的上下文模块的处理 </li> 
 <li>在 HMR 更新期间导入块时，修复竞争条件的 HMR 块加载 </li> 
 <li>处理 runAsChild 回调中的错误</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.71.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.71.0</a></p>
                                        </div>
                                      
</div>
            