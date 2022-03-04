
---
title: 'Laravel v9.3.0 发布，经典 PHP 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=989'
author: 开源中国
comments: false
date: Fri, 04 Mar 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=989'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Laravel framework 包含  PHP 框架 Laravel 的核心代码，目前更新了 9.3.0 版本，主要更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41232" target="_blank">#41232</a><span> </span>) 添加 NotificationFake::assertNothingSentTo( )</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40931" target="_blank">#40931</a><span> </span>) 支持 --ssl-ca 模式加载和转储</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41096" target="_blank">#41096</a><span> </span>) 将 whereNot() 添加到 Query Builder 和 Eloquent Builder</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41123" target="_blank">#41123</a><span> </span>) 在数组验证消息中支持索引和位置占位符</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41233" target="_blank">#41233</a><span> </span>) 添加资源绑定</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41256" target="_blank">#41256</a><span> </span>) 新增通过 chain($pipes) 将其他管道推送到管道上的功能</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41254" target="_blank">#41254</a><span> </span>) 在 route:list 命令中添加选项，以过滤供应商包中定义的路由</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41215" target="_blank">#41215</a><span> </span>) 修复查询 PostgresBuilder 重命名的配置 'search_path'</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41245" target="_blank">#41245</a><span> </span>) 改进 Eloquent Factory 方法的文档类型</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41270" target="_blank">#41270</a><span> </span>) 修复 Conditional::when 和 Conditional::unless 被调用的问题</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41272" target="_blank">#41272</a><span> </span>) 改进 Support\Collection ，减少方法类型定义</li> 
 <li>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41257" target="_blank">#41257</a>）修复使用 withCasts() 时 firstOrNew() 的不一致结果</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41282" target="_blank">#41282</a><span> </span>) 修复无 SoftDeletes 特征子组件的 implicitBinding 和 withTrashed 路由</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41216" target="_blank">#41216</a><span> </span>) 取消设置连接解析器扩展回调</li> 
 <li>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F41255" target="_blank">#41255</a><span> </span>) 更新 Mailgun 传输类型</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv9.3.0" target="_blank">https://github.com/laravel/framework/releases/tag/v9.3.0</a></p>
                                        </div>
                                      
</div>
            