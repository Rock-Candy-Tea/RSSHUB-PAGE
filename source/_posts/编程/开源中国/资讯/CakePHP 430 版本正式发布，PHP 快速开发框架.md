
---
title: 'CakePHP 4.3.0 版本正式发布，PHP 快速开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=672'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 23:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=672'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">CakePHP 发布了<span> </span></span><span style="color:#24292f">4.3.0 正式版，</span><span style="color:#000000">CakePHP 是一个运用了诸如 ActiveRecord、Association Data Mapping、Front Controller 和 MVC（model–view–controller） 等著名设计模式的开源 Web 框架，用 PHP 编写，以 Ruby on Rails 的概念为模型，并在 MIT 许可下进行分发。</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>主要更新：</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">添加了一个新的 fixture 系统，它允许使用现有的<span> </span></span><span style="color:#24292f">migrations</span><span style="color:#2e3033"><span> </span>或 SQL 转储文件来</span><span style="color:#24292f">定义架构，（包括支持 cake's migrations 和<span> </span></span><span style="color:#2e3033">SQL 转储文件）。</span></li> 
 <li><span style="color:#24292f"> 加入<span> </span><code>TestSuite\HttpMockTrait</code><span> </span>，便于</span><span style="color:#2e3033">模拟 HTTP 客户端请求</span></li> 
 <li>加入<span> </span><code>LocatorAwareTrait::fetchTable() </code><span> </span>，让<span> </span><code>getTableLocator()->get()</code><span> </span>更符合人体工程学。</li> 
 <li><span style="color:#24292f">加入<span> </span><code>Controller::middleware()</code></span>，这个<span style="color:#2e3033">方法可以定义特定于控制器的中间件，或者当前控制器的操作。</span></li> 
 <li><code>deprecationWarning()</code><span> </span>不再发出重复的警告。</li> 
 <li><code>Form</code><span> </span>对象支持多个验证器，并利用与 ORM 类似的接口来使用这些验证器。</li> 
 <li><span style="color:#24292f">Logged SQL<span> </span></span><span style="color:#2e3033">查询现在使用布尔值，更容易粘贴到 repl 里面。</span></li> 
 <li><code>cake console</code><span> </span>指令被提取到一个新的<span> </span><code>cakephp/repl</code><span> </span>包中。</li> 
 <li><code>CspMiddleware</code><span style="color:#24292f"><span> </span></span><span style="color:#2e3033">可以透明地添加基于<span> </span><code>nonce</code><span> </span>的策略。</span></li> 
 <li><code>FormHelper</code><span> </span>将自动设置其他 ARIA 属性。</li> 
 <li><span style="color:#2e3033">ORM 现在可以清楚地将用户时区的日期和时间设置为应用的时区。</span></li> 
 <li><span style="color:#24292f">CakePHP 的依赖组件<span> </span><code>league/container</code><span> </span>升级到 4.1.1 版本。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcakephp%2Fcakephp%2Freleases%2Ftag%2F4.3.0" target="_blank">https://github.com/cakephp/cakephp/releases/tag/4.3.0</a></p>
                                        </div>
                                      
</div>
            