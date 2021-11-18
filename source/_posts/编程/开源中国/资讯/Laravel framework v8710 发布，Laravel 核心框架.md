
---
title: 'Laravel framework v8.71.0 发布，Laravel 核心框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=734'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=734'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Laravel framework<span> </span><span style="color:#57606a">包含  PHP 框架 Laravel 的核心代码，目前更新了 8.71.0 版本，主要更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>新增</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了 denied 和 denied_if 验证规则 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39579" target="_blank">#39579</a><span> </span>)</li> 
 <li>Arrayable/collection 支持 Collection::splice() 替换参数 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39592" target="_blank">#39592</a><span> </span>)</li> 
 <li>引入<span> </span><code>@js()</code><span> </span>命令 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39522" target="_blank">#39522</a><span> </span>)</li> 
 <li>枚举类型转换现在可接受支持的值 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39608" target="_blank">#39608</a><span> </span>)</li> 
 <li>Macroable 特性添加了一个方法，用于删除所有配置的宏。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39633" target="_blank">#39633</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了自动生成的 Markdown 视图 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39565" target="_blank">#39565</a><span> </span>)</li> 
 <li>DB 指令：处理缺少的 mysql 驱动程序参数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39582" target="_blank">#39582</a>）</li> 
 <li>修复了<span> </span><code>Illuminate/Database/Connection</code><span> </span>连接属性名称中的拼写错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39590" target="_blank">#39590</a>）</li> 
 <li>修复：<span style="color:#2e3033">防止重新强制转换枚举值</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39597" target="_blank">#39597</a>）</li> 
 <li>将<span> </span><code>Illuminate/Database/Query/Builder::limit()</code><span> </span>的值强制转换为 int (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2F62273d20dd13b7e35885436d7327be31e3f54b0e" target="_blank">62273d2</a><span> </span>)</li> 
 <li><span style="color:#2e3033">修复了组件不呈现时 $component 不会被恢复的问题</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39595" target="_blank">#39595</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>make:model --all</code><span> </span>标志会使用 --requests 来自动触发 make:controller (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39578" target="_blank">#39578</a><span> </span>)</li> 
 <li>允许多个 JSON 验证错误的断言。 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39568" target="_blank">＃39568</a>）</li> 
 <li><span style="color:#2e3033">缓存目录的查看权限</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39591" target="_blank">#39591</a>）</li> 
 <li>更新存根的占位符（<span style="color:#24292f">placeholders for stubs</span>） (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39527" target="_blank">#39527</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.71.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.71.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            