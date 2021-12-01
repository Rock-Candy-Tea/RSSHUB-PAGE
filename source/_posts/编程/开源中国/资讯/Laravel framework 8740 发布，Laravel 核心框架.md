
---
title: 'Laravel framework 8.74.0 发布，Laravel 核心框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5567'
author: 开源中国
comments: false
date: Wed, 01 Dec 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5567'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">Laravel framework</span><span style="background-color:#ffffff; color:#000000"> </span><span style="background-color:#ffffff; color:#57606a">包含  PHP 框架 Laravel 的核心代码，目前更新了 8.74.0 版本，主要更新内容如下：</span></p> 
<h2><span style="background-color:#ffffff; color:#57606a">新增</span></h2> 
<ul> 
 <li><span style="background-color:#ffffff; color:#2e3033">在 PruneCommand 命令中增加了可选的 except 参数 </span><span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39749" target="_blank">#39749</a><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2Fbe4afcc6c2a42402d4404263c6a5ca901d067dd2" target="_blank">be4afcc</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
 <li>添加<code>Illuminate/Foundation/Application::hasDebugModeEnabled()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39755" target="_blank">#39755</a>）</li> 
 <li>添加<code>Illuminate/Support/Facades/Event::fakeExcept()</code>和<code>Illuminate/Support/Facades/Event::fakeExceptFor()</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39752" target="_blank">#39752</a>）</li> 
 <li>为 <span style="background-color:#ffffff; color:#24292f">Eloquent 驱动添加聚合方法 <span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39772" target="_blank">#39772</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
 <li><span style="background-color:#ffffff; color:#2e3033">在 Arr 助手和集合中添加了 undot() 降噪方法</span><span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39729" target="_blank">#39729</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">为字符串加入反转方法（<span> </span></span><code>reverse</code><span style="background-color:#ffffff; color:#24292f"><span> </span>method）(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39816" target="_blank">#39816</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
 <li><span style="background-color:#ffffff; color:#2e3033">现在可以在数据库通知中使用 databaseType 方法自定义类型列 </span><span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39811" target="_blank">#39811</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">添加全文索引功能 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39821" target="_blank">#39821</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
</ul> 
<h2><span style="background-color:#ffffff; color:#24292f">修复</span></h2> 
<p><span style="background-color:#ffffff; color:#2e3033">修正了在框架外加载总线服务提供者的问题 </span><span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39740" target="_blank">#39740</a><span style="background-color:#ffffff; color:#24292f">)</span></p> 
<p><span style="background-color:#ffffff; color:#2e3033">修复了空驱动不存在时的日志弃用问题 </span><span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39809" target="_blank">#39809</a><span style="background-color:#ffffff; color:#24292f">)</span></p> 
<h2>变更</h2> 
<ul> 
 <li>在解析队列连接之前验证连接的名称 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39751" target="_blank">#39751</a> )</li> 
 <li>将 Symfony 升级到 5.4 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39827" target="_blank">#39827</a> )</li> 
 <li>优化唯一方法（<span style="background-color:#ffffff; color:#24292f">unique method</span>）的执行时间 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39822" target="_blank">#39822</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.74.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.74.0</a></p>
                                        </div>
                                      
</div>
            