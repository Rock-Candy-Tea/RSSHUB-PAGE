
---
title: 'Rails 7.0 发布，实现愿景：真正的全栈 Web 开发方法'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2275'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2275'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rails 是一个 Web 应用程序框架，是 Ruby 最早也是最出名的一个框架，其中包括根据模型-视图-控制器（MVC） 模式，创建 Web 应用程序所需的所有内容 。Rails 可以说是 MVC 开发的先驱者，了解 MVC 模式是了解 Rails 的关键。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rails 7.0 是一个大版本，实现了一个愿景：一种真正的全栈 Web 开发方法，以可以同时应对前端和后端的挑战。比如 Rails 应用有新的默认选择： Hotwire，它的 Turbo 和 Stimulus 组合几乎包含所有增强用户体验的工具；又或者无需将 Webpack 与 Webpacker 紧密耦合，Rails 7.0 可以使用新的<span> </span><code>jsbundle -rails</code><span> </span>集成将任何 JavaScript 打包器松散结合，无论是 esbuild、rollup.js 或是Webpack。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本还有相当多更新项，下面摘录一些较为重要的更新内容作介绍：</p> 
<h2><strong>活动记录（Active Record）支持工作中加密</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rails 7.0 向 Active Record 添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Fpull%2F41659" target="_blank"><strong>活动记录加密属性</strong></a><strong>（</strong><span> </span>encrypted attributes to Active Record,<strong>）</strong>，除了传统的静态和传输中覆盖之外，应用程序还可以提供工作中加密（at-work encryption）。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">加密敏感属性会增加一个额外的安全层，就算恶意攻击者获取了数据库、快照或者日志的访问权限，也看不懂加密信息，另外，通过使用 Active Record Encryption，可以在代码级别中定义应用敏感信息的构成。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">点此查看关于使用加密属性的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fedgeguides.rubyonrails.org%2Factive_record_encryption.html" target="_blank"><strong>完整指南</strong></a>。</p> 
<h2><strong>使用 Marginalia 样式标记跟踪查询来源</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">大概十年前（2012），Rails 引入基于 Basecamp 的 Marginalia：使用 SQL 注释标记来跟踪查询来源。现在这个外部 gem 已经<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Fpull%2F42240" target="_blank"><strong>作为 QueryLogs 上传到 Active Record 中</strong></a>。</p> 
<h2><strong>异步查询加载</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">如果有一个控制器操作需要加载两个不相关的查询时，Rails 7.0 可以通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Fpull%2F41372" target="_blank"><strong>Relation#load_async</strong></a><strong><span> </span></strong>并发执行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">比如：以前如果有三个复杂的查询，每个查询需要 100 毫秒，那么就必须先花费 300 毫秒来逐一执行它们。现在可以并行运行，总共只花费 100 毫秒。</p> 
<h3>Zeitwerk</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Rails 的自动加载是它的特性之一，不过老的 const_missing 方法有一系列问题，因此引入新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffxn%2Fzeitwerk%23introduction" target="_blank"><strong>Zeitwerk 代码加载器</strong></a><strong><span> </span></strong>完全取代它。比较老的应用升级会比较麻烦，可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fguides.rubyonrails.org%2Fupgrading_ruby_on_rails.html%23autoloading" target="_blank">完整的升级指南</a>。</p> 
<h2><strong>其他一些亮点</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>默认情况下，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Fspring" target="_blank"><strong>Spring</strong></a><strong><span> </span></strong>不再启用。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Fpull%2F41488" target="_blank"><strong>ActionController::Live#send_stream</strong></a><strong><span> </span></strong>可以轻松地传输动作控制器实时生成的流文件。</li> 
 <li>现在并行测试将比较 CPU 内核计数和测试计数，并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Fpull%2F42761" target="_blank">相应地调整并行度</a>。</li> 
 <li>Active Storage 现在使用更快、更安全的<span> </span><code>libvips</code><span> </span>作为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fedgeguides.rubyonrails.org%2Fupgrading_ruby_on_rails.html%23activestorage-variant-processor-changed-to-vips" target="_blank">默认变体处理器</a>。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详尽内容可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frails%2Frails%2Freleases%2Ftag%2Fv7.0.0" target="_blank">在更新公告中查看</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            