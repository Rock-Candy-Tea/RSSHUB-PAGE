
---
title: 'PluginCore v0.9.3 发布，与前端更好集成，更强扩展性 !'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c6b44171716e24a84f5c890e2de08de85bf.png'
author: 开源中国
comments: false
date: Wed, 16 Mar 2022 19:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c6b44171716e24a84f5c890e2de08de85bf.png'
---

<div>   
<div class="content">
                                                                                            <h1><img alt height="254" src="https://oscimg.oschina.net/oscnet/up-c6b44171716e24a84f5c890e2de08de85bf.png" width="2500" referrerpolicy="no-referrer"></h1> 
<h1>项目简介</h1> 
<p><span style="background-color:#ffffff">适用于 ASP.NET Core 的轻量级插件框架</span></p> 
<blockquote> 
 <p><span style="background-color:#ffffff">PluginCore 与其它插件方案不同的是，PluginCore 本身以一个库方式存在，无需将源代码引入现有项目，只需引用包，两行代码即可接入，不会给现系统带来多余污染，同时 PluginCore 拥有现成完整的插件解决方案，真正开箱即用 !</span></p> 
 <p>PluginCore 现已拥有 JavaScript SDK, 能够通过插件在前端进行扩展（注入/修改页面）</p> 
</blockquote> 
<ul> 
 <li><strong>简单</strong><span> </span>- 约定优于配置, 以最少的配置帮助你专注于业务</li> 
 <li><strong>开箱即用</strong><span> </span>- 前后端自动集成, 两行代码完成集成</li> 
 <li><strong>动态 WebAPI</strong><span> </span>- 每个插件都可新增 Controller, 拥有自己的路由</li> 
 <li><strong>插件前后端分离</strong><span> </span>- 可在插件<span> </span><code>wwwroot</code><span> </span>文件夹下放置前端文件 (index.html,...), 然后访问<span> </span><code>/plugins/pluginId/index.html</code></li> 
 <li><strong>热插拔</strong><span> </span>- 上传、安装、启用、禁用、卸载、删除 均无需重启站点; 甚至可通过插件在运行时添加<span> </span><code>HTTP request pipeline middleware</code>, 也无需重启站点</li> 
 <li><strong>依赖注入</strong><span> </span>- 可在 实现<span> </span><code>IPlugin</code><span> </span>的插件类的构造方法上申请依赖注入项, 当然<span> </span><code>Controller</code><span> </span>构造方法上也可依赖注入</li> 
 <li><strong>易扩展</strong><span> </span>- 你可以编写你自己的插件sdk, 然后引用插件sdk, 编写扩展插件 - 自定义插件钩子, 并应用</li> 
 <li><strong>挂件</strong><span> </span>- 你可在前端埋扩展点, 然后通过插件插入挂件</li> 
 <li><strong>无需数据库</strong><span> </span>- 无数据库依赖</li> 
 <li><strong>0侵入</strong><span> </span>- 近乎0侵入, 不影响你的现有系统</li> 
 <li><strong>极少依赖</strong><span> </span>- 只依赖于一个第三方包 ( 用于解压的<span> </span><code>SharpZipLib</code><span> </span>)</li> 
</ul> 
<h1>更新</h1> 
<h2 style="text-align:start">Fixed</h2> 
<ul> 
 <li>更新 PluginCore Admin 前端:<span> </span><code>plugincore-admin-frontend-v0.3.1</code> 
  <ul> 
   <li>Fixed: 用户名验证错误</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">Fixed</h2> 
<ul> 
 <li><code>tokenCookieName = "PluginCore.Admin.Token"</code><span> </span>与<span> </span><code>PluginCore Admin</code><span> </span>前端一致, 而不是后端检索<span> </span><code>tokenCookieName = "token"</code> 
  <ul> 
   <li>插件可在<span> </span><code>Controller,Action</code><span> </span>上使用<span> </span><code>[Authorize("PluginCoreAdmin")]</code>, 来达到与<span> </span><code>PluginCore Admin</code><span> </span>相同的权限策略</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">Fixed</h2> 
<ul> 
 <li><code>ITimeJobPlugin</code><span> </span>多线程定时任务 执行问题 
  <ul> 
   <li>当上一个任务未完成, 下个任务就开始时导致, 修复: 加锁, 下个任务线程阻塞等待</li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">Added</h2> 
<ul> 
 <li>挂件 (Plugin Widget) 相关</li> 
</ul>
                                        </div>
                                      
</div>
            