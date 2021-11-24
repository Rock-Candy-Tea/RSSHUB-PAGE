
---
title: 'Laravel framework 发布 8.72.0 和 8.73.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7970'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 06:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7970'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Laravel framework 是</span><span style="color:#57606a"><span> </span> PHP 框架 Laravel 的核心部分，目前发布了 8.72.0 和 8.73.0 版本，主要更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">8.72.0 版本变更：</h3> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 PasswortReset 中添加了额外的方法来重置 URL， 以匹配 VerifyEmail 的结构（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39652" target="_blank">#39652</a>）</li> 
 <li><span style="color:#2e3033">在复数表达式（</span><span style="color:#24292f"><code>Str::plural</code></span><span style="color:#2e3033">）中添加对可数值（</span><span style="color:#24292f">countable values</span><span style="color:#2e3033">）的支持。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39641" target="_blank">#39641</a><span style="color:#24292f">)</span></li> 
 <li>允许用户为 DatabaseMigration trait 指定 migrate:fresh 选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39637" target="_blank">#39637</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><code>Illuminate/Database/Query/Builder::limit()</code><span> </span>不是空值时，</span><span style="color:#2e3033">允许将 $value 转换为整型（int）值。</span><span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39644" target="_blank">#39644</a><span style="color:#24292f">)</span></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f">变更</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> <code>SortedMiddleware</code><span style="color:#24292f"><span> </span> 使用父节点来解析中间件优先级。(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39647" target="_blank">#39647</a><span style="color:#24292f">)</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.72.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.72.0</a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">8.73.0 版本变更：</h3> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">在验证器中为被阻塞的 PHP 扩展添加了.phar 方法</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39666" target="_blank">#39666</a>)</li> 
 <li><span style="color:#2e3033">允许闭包作为 ttl 在<span> </span><code>Cache remember()</code><span> </span>方法中传递</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39678" target="_blank">#39678</a>)</li> 
 <li><span style="color:#2e3033"><code>dependentRules</code><span> </span>属性添加了禁止验证规则</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39677" target="_blank">#39677</a>)</li> 
 <li><span style="color:#24292f">按降序实现 lazyById (</span><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39646" target="_blank">#39646</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<span> </span><code>Illuminate/Auth/Notifications/ResetPassword::toMail()</code><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2F969f1014ec07efba803f887a33fde29e305c9cb1" target="_blank">969f101</a>)</li> 
 <li>修复<span> </span><code>assertSoftDeleted</code><span> </span>和<span> </span><code>assertNotSoftDeleted</code><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39673" target="_blank">#39673</a>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.73.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.73.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            