
---
title: 'Laravel framework 8.81.0 发布，Laravel 框架核心库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1514'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1514'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Laravel framework 包含  PHP 框架 Laravel 的核心代码，目前更新了 8.81.0 版本，主要更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加<span> </span><code>Illuminate/Support/Stringable::scan()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40472" target="_blank">#40472</a>）</li> 
 <li><span style="color:#2e3033">允许在返回对象的虚拟属性访问器中禁用缓存</span><span> </span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40519" target="_blank">#40519</a><span> </span>)</li> 
 <li>添加了更好的按位运算符支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40529" target="_blank">#40529</a>）</li> 
 <li>在集合上添加了 getOrPut (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40535" target="_blank">#40535</a><span> </span>)</li> 
 <li>改进 PhpRedis 刷新逻辑 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40544" target="_blank">#40544</a><span> </span>)</li> 
 <li>添加<span> </span><code>Illuminate/Support/Str::flushCache()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40620" target="_blank">#40620</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 unicode 的 Str::headline/Str::studly 问题，并添加 Str::ucsplit 方法 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40499" target="_blank">#40499</a><span> </span>)</li> 
 <li>使用 MailFake 修复<span> </span><span style="color:#24292f">forgetMailers</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40495" target="_blank">#40495</a>）</li> 
 <li><span style="color:#24292f">Pruning Models</span>：从方法中获取模型的默认路径（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40539" target="_blank">#40539</a>）</li> 
 <li>修复 predis 集群的 flushdb  (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40446" target="_blank">#40446</a><span> </span>)</li> 
 <li>尽量避免未定义的数组键<span> </span><code>0</code><span> </span>的相关错误 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40571" target="_blank">#40571</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>PostgreSQL 的 PDO dbname 允许空格 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40483" target="_blank">#40483</a><span> </span>)</li> 
 <li>允许 authorizeResource 方法接收模型和参数数组 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40516" target="_blank">#40516</a><span> </span>)</li> 
 <li>逆可变形类型和 id 过滤语句，以防止 SQL 错误 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40523" target="_blank">#40523</a><span> </span>)</li> 
 <li>将 voku/portable-ascii 升级到 v1.6.1（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40588" target="_blank">#40588</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40610" target="_blank">#40610</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.81.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.81.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            