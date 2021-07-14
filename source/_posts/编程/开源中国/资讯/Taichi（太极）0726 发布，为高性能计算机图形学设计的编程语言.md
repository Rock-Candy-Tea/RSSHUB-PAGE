
---
title: 'Taichi（太极）0.7.26 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://attachments.tower.im/tower/43963cc20256e177dcb41b2ef5370a8f?version=auto'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 07:30:00 GMT
thumbnail: 'https://attachments.tower.im/tower/43963cc20256e177dcb41b2ef5370a8f?version=auto'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taichi（太极）0.7.26 已经发布，这是专为高性能计算机图形学设计的编程语言。<img alt src="https://attachments.tower.im/tower/43963cc20256e177dcb41b2ef5370a8f?version=auto" referrerpolicy="no-referrer"></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif" referrerpolicy="no-referrer"></p> 
<p>此版本具体更新内容如下：</p> 
<p><strong>Highlights </strong></p> 
<p>从此版本开始，你可以在调用内核后创建新的<code>ti.field</code>实例。值得注意的是，该功能目前在 CPU 和 CUDA 后端支持。</p> 
<p><strong>Full changelog </strong></p> 
<ul> 
 <li>[refactor] 删除 kernel.cpp 中的 global_program ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2508" target="_blank">#2508</a> ) </li> 
 <li>[misc] 在 taichi GUI 中为圆圈添加了调色板 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2504" target="_blank">#2504</a> )</li> 
 <li>[lang] 支持 ti.fields with shape after materialized ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2503" target="_blank">#2503</a> )</li> 
 <li>[doc] 添加解释如何运行太极 CPP 测试的基本文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2502" target="_blank">#2502</a> ) </li> 
 <li>[lang] 支持 ti.FieldsBuilder() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2501" target="_blank">#2501</a> )</li> 
 <li>[misc] 为 SNode 添加 Needs_grad 属性 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2500" target="_blank">#2500</a> )</li> 
 <li>[lang] 支持具有相同内存位置的 fake FieldsBuilder() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2493" target="_blank">#2493</a> )</li> 
 <li>[ci] 修复 appveyor ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2496" target="_blank">#2496</a> )</li> 
 <li>[ir] 为 CFG 优化和分析的实现添加一些 comments ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2474" target="_blank">#2474</a> )</li> 
 <li>[Doc] 添加 .md 文档（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2494" target="_blank">#2494</a>）</li> 
 <li>[Example] 重构示例库（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2475" target="_blank">#2475</a>）</li> 
 <li>[Doc] 删除所有 .rst 文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2492" target="_blank">#2492</a> ) </li> 
 <li>[Refactor] [cuda] 清理 CUDA AtomicOpStmt codegen ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2490" target="_blank">#2490</a> ) </li> 
 <li>[Perf] [cuda] 使用 warp reduction 提高 reduction performance ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2487" target="_blank">#2487</a> )</li> 
 <li>[vulkan] 添加内核元数据和实用程序 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2481" target="_blank">#2481</a> )</li> 
 <li>[opengl] [refactor] 使用宏生成原子浮点函数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2486" target="_blank">#2486</a> ) </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.7.26" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.7.26</a></p>
                                        </div>
                                      
</div>
            