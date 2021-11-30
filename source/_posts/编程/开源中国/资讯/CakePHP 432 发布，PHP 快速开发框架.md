
---
title: 'CakePHP 4.3.2 发布，PHP 快速开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1553'
author: 开源中国
comments: false
date: Tue, 30 Nov 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1553'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CakePHP 是一个运用了诸如 ActiveRecord、Association Data Mapping、Front Controller 和 MVC（model–view–controller） 等著名设计模式的开源 Web 框架。CakePHP 用 PHP 编写，以 Ruby on Rails 的概念为模型，并在 MIT 许可下进行分发。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">CakePHP 4.3.2 现已发布，这是 4.3 分支的一个维护版本，修正了几个社区报告的问题：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">增加了控制器动作的数组类型强制转换，现在带<span> </span></span><span style="color:#24292f"><code>,</code></span><span style="color:#2e3033"><span> </span>分隔值的列表现在可以解压缩到数组里面。</span></li> 
 <li><span style="color:#2e3033">确保在控制器中设置了<span> </span><code>$defaultTable</code></span>。</li> 
 <li><span style="color:#2e3033">放宽了对<span> </span><code>psr/container</code><span> </span>的版本限制。</span></li> 
 <li><span style="color:#2e3033">更新了<span> </span><code>Table::get()</code><span> </span>生成的缓存键，以前的密钥与基于文件的缓存不兼容。（这个修复的副作用是缓存键会改变。）</span></li> 
 <li><span style="color:#2e3033">增加了<span> </span><code>_urldecode</code><span> </span>路由选项，以增加更多请求 url  的解码方式。</span></li> 
 <li><span style="color:#24292f">修复了日志消息中丢失的毫秒数。</span></li> 
 <li><span style="color:#2e3033">修正了 Router::reverse() 不能正确处理使用 Route::setPass() 创建的参数问题。</span></li> 
 <li>添加对<span> </span><code>308</code><span> </span>HTTP 状态代码的支持。</li> 
 <li><span style="color:#2e3033">从<span> </span><code>PaginatorComponent</code><span> </span>中移除<span> </span><code>_defaultConfig</code>，以修复子类中定义的默认配置不会被忽略的问题。</span></li> 
 <li><span style="color:#2e3033">改进 API 文档。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcakephp%2Fcakephp%2Freleases%2Ftag%2F4.3.2" target="_blank">https://github.com/cakephp/cakephp/releases/tag/4.3.2</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            