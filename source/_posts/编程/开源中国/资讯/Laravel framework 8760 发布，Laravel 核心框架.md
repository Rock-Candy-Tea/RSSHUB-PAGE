
---
title: 'Laravel framework 8.76.0 发布，Laravel 核心框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8040'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 23:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8040'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">Laravel framework</span><span style="background-color:#ffffff; color:#000000"> </span><span style="background-color:#ffffff; color:#57606a">包含  PHP 框架 Laravel 的核心代码，目前更新了 8.76.0 版本，主要更新内容如下：</span></p> 
<h3>新增</h3> 
<ul> 
 <li>添加了自定义子模型路由绑定分辨率的可能性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39929" target="_blank">#39929</a>）</li> 
 <li>添加了 Illuminate/Http/Client/Response::reason() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39972" target="_blank">#39972</a> )</li> 
 <li>添加了 afterRefreshingDatabase 测试方法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39978" target="_blank">#39978</a> )</li> 
 <li>向 Illuminate/Http/Client/Response 添加了 未授权-<span style="color:#24292f"><code>unauthorized()</code> 和 禁止-<code>forbidden()</code></span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39979" target="_blank">#39979</a>）</li> 
 <li>在 stub:publish 命令中发布 <code>view-component.stub</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40007" target="_blank">#40007</a> )</li> 
 <li>为 MySQL 列添加了不可见的修饰符 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40002" target="_blank">#40002</a> )</li> 
 <li>添加了 Str::substrReplace() 和 Str::of($string)->substrReplace() 方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39988" target="_blank">#39988</a>）</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>在视图中修复了父调用 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39909" target="_blank">#39909</a> )</li> 
 <li>修复了请求转储和 dd 方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39931" target="_blank">#39931</a>）</li> 
 <li><span style="color:#2e3033">修正了 php 8.1 在 <code>ValidatesAttributes::checkDateTimeOrder</code> 中的弃用</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39937" target="_blank">#39937</a>）</li> 
 <li>修复了在<span style="color:#24292f">路由上使用</span> withTrashed 时，检查是否在 <code>Model</code> 中使用 <code>SoftDeletes</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39958" target="_blank">#39958</a> )</li> 
 <li>修复 SoftDeletes 的  <span style="color:#24292f">model:prune </span>-- pretend 命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39991" target="_blank">#39991</a>）</li> 
 <li>修复了 SoftDeletes 强制删除，在删除成功时将“<span style="color:#24292f">exists</span>”属性设置为 false 的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39987" target="_blank">#39987</a> )</li> 
 <li>修复了从 Redis 驱动程序的缓存中通过引用键删除值时，可能出现的内存不足错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39939" target="_blank">#39939</a> )</li> 
 <li><span style="color:#2e3033">修正了密码验证不允许在最小规则后出现错误的问题</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F40030" target="_blank">#40030</a>）</li> 
</ul> 
<h3>更改</h3> 
<ul> 
 <li><span style="color:#2e3033">用纯枚举验证失败</span> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39926" target="_blank">#39926</a> )</li> 
 <li>删除多余的描述和本地化模板 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39928" target="_blank">#39928</a> )</li> 
 <li><span style="color:#2e3033">修复了记录器尚未准备好时，会报告弃用的问题</span> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39938" target="_blank">#39938</a> )</li> 
 <li><span style="color:#2e3033">在从属规则参数中，用占位符替换转义的圆点</span> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fpull%2F39935" target="_blank">#39935</a> )</li> 
 <li>从属性到基础查询对象的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2F127334acbcb8bb012a4831c9fc17bc520c20e320" target="_blank">传递</a>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Fcommit%2F127334acbcb8bb012a4831c9fc17bc520c20e320" target="_blank">127334a</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flaravel%2Fframework%2Freleases%2Ftag%2Fv8.76.0" target="_blank">https://github.com/laravel/framework/releases/tag/v8.76.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            