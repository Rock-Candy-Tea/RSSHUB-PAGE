
---
title: '高性能异步编排框架 Gobrs-Async 1.0.3-SNAPSHOT 版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://kevin-cloud-dubbo.oss-cn-beijing.aliyuncs.com/gobrs-async/image-20220809221727601.png'
author: 开源中国
comments: false
date: Fri, 12 Aug 2022 11:03:00 GMT
thumbnail: 'https://kevin-cloud-dubbo.oss-cn-beijing.aliyuncs.com/gobrs-async/image-20220809221727601.png'
---

<div>   
<div class="content">
                                                                                            <h1>Gobrs-Async 1.0.3-SNAPSHOT 版本更新</h1> 
<p><strong>更新内容</strong></p> 
<h2>关于</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMemorydoc%2Fgobrs-async" target="_blank"><strong>Gobrs-Async</strong></a> 是一款功能强大、配置灵活、带有全链路异常回调、内存优化、异常状态管理于一身的高性能异步编排框架。为企业提供在复杂应用场景下动态任务编排的能力。针对于复杂场景下，异步线程复杂性、任务依赖性、异常状态难控制性的现象提供了快速高效的解决方案。</p> 
<h2>一、可选的任务执行逻辑</h2> 
<p>在application.yml 中 配置的任务流程， 非必要执行配置的所有任务如下：</p> 
<p><img alt="image-20220809221727601" src="https://kevin-cloud-dubbo.oss-cn-beijing.aliyuncs.com/gobrs-async/image-20220809221727601.png" referrerpolicy="no-referrer"></p> 
<p><strong>配置任务</strong></p> 
<pre><code> "AService->BService->FService;HService,EService,GService"
</code></pre> 
<p>如果用户在使用时只希望执行 FService , 则在任务链中 只需要执行AService、BService、FService 即可。 无需执行H、E、G任务。</p> 
<p><strong>适应场景</strong></p> 
<p>在做 <strong>ISV</strong> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.51cto.com%2Farticle%2F712050.html" target="_blank">京东商城ISV组件化建设</a>) 建设时， 楼层中的多个组件可能存在着任务流程的编排， 所需要的上游数据数量多少不一，所以此时就需要进行编排流程中的任务选择执行处理了。</p> 
<blockquote> 
 <p>如下对每个组件进行编排数据编排处理</p> 
</blockquote> 
<p>![<img alt="image-20220809222627074" src="https://kevin-cloud-dubbo.oss-cn-beijing.aliyuncs.com/gobrs-async/image-20220809222627074.png" referrerpolicy="no-referrer"></p> 
<h2>二、修复issue</h2> 
<ul> 
 <li>修复任务链中某一任务执行异常，后续子任务无需执行的逻辑。当 failSubExec 为true 时， 单条流程中的任务异常不会影响后续子任务执行。 否则终止子任务的调用执行。</li> 
</ul> 
<p><img alt="image-20220809222738453" src="https://kevin-cloud-dubbo.oss-cn-beijing.aliyuncs.com/gobrs-async/image-20220809222738453.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxn--README-2g0ju63d.md" target="_blank">修复README.md</a> 编码格式</li> 
</ul> 
<h2>友情链接</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fasync.sizegang.cn%2F" target="_blank">官网地址</a></li> 
 <li><a href="https://gitee.com/dromara/gobrs-async">gitee</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fgobrs-async" target="_blank"><strong>gitHub</strong></a></li> 
</ul>
                                        </div>
                                      
</div>
            