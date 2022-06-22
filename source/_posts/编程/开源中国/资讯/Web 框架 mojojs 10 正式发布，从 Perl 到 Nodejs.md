
---
title: 'Web 框架 mojo.js 1.0 正式发布，从 Perl 到 Node.js'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7604'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7604'
---

<div>   
<div class="content">
                                                                                            <p>历经一年多的开发，mojo.js 终于发布了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmojojs.org%2Fnews%2Fmojo.js-1-released" target="_blank">首个主要版本 1.0</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">mojo.js 是 Node.js 实时 Web 框架，可将它视作采用 TypeScript 重写的 <a href="https://www.oschina.net/p/mojolicious">Mojolicious</a>（Mojolicious 是 Perl 开发的 Web 框架）。mojo.js 使用了所有最新的 JavaScript 特性，专为聚焦超媒体 (hypermedia) 的后端 Web 服务精心设计。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>主要特性</strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li><strong>实时 Web 框架</strong>，开发者可轻松地将单文件原型扩展为结构良好的 MVC Web 应用程序。 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li>开箱即用的强大 RESTful 路由、WebSockets、插件、命令、日志记录、模板、内容协商 (content negotiation)、会话管理、表单和 JSON 验证、测试框架、静态文件服务器、集群模式、CGI 检测、一等公民的 Unicode 支持等</li> 
  </ul> </li> 
 <li>强大的 <strong>Web 开发工具包</strong>，开发者可以将它用于各种应用程序，独立于 Web 框架。 
  <ul style="list-style-type:square; margin-left:0; margin-right:0"> 
   <li>高性能 HTTP 和 WebSocket 客户端 / 服务器实现，支持 HTTPS/WSS、cookie、重定向、urlencoded/multi-part 表单、文件上传、JSON/YAML、HTML/XML、模拟数据、API 测试、HTTP/SOCKS 代理和 gzip 压缩。</li> 
   <li>支持 CSS 选择器的 HTML/XML 解析器。</li> 
  </ul> </li> 
 <li>基于<span> </span><code>class</code>、<code>async</code>/<code>await</code><span> </span>的 API，采用 TypeScript 编写，几乎不需要依赖，因此可避免 NPM 依赖地狱。</li> 
 <li>基于具有数十年积累的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmojolicious.org%2F" target="_blank">Mojolicious</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcatalyst.perl.org%2F" target="_blank">Catalyst</a> 的代码，免费且开源。</li> 
</ul> 
<p>下面的代码示例是一个"hello world"单文件应用，包含 WebSockets：</p> 
<pre><code class="language-javascript">import mojo from '@mojojs/core';

const app = mojo();

app.get('/', async ctx => &#123;
  await ctx.render(&#123;inline: inlineTemplate&#125;);
&#125;);

app.websocket('/echo', ctx => &#123;
  ctx.plain(async ws => &#123;
    for await (const message of ws) &#123;
      ws.send(message);
    &#125;
  &#125;);
&#125;);

app.start();

const inlineTemplate = `
<script>
  const ws = new WebSocket('<%= ctx.urlFor('echo') %>');
  ws.onmessage = event => &#123; document.body.innerHTML += event.data &#125;;
  ws.onopen    = event => &#123; ws.send('Hello World!') &#125;;
</script>
`;</code></pre> 
<p>但 mojo.js 并不是真正的单文件应用程序。作为一个非常传统的超媒体框架和 Mojolicious 的精神继承者，它鼓励开发者采用 MVC 模式，同时还支持这些单文件应用程序进行原型化。</p> 
<p>上文提到了 mojo.js 与 Mojolicious 的渊源。事实上，mojo.js 的诞生与 <a href="https://www.oschina.net/news/110510/perl-6-rename-to-raku">Perl6</a>（已被重命名为 Raku）也有一定关系。当 Perl6 发布时，官方就已计划将 Mojolicious 移植到除 Perl5 外的更多语言。此时，JavaScript 不断发展，添加了<span style="background-color:#ffffff; color:#445555"> ES6 classes,<span> </span></span><code>async</code><span style="background-color:#ffffff; color:#445555">/</span><code>await</code><span style="background-color:#ffffff; color:#445555">, ES modules, 箭头函数,<span> </span></span><code>const</code><span style="background-color:#ffffff; color:#445555">/</span><code>let</code><span style="background-color:#ffffff; color:#445555"><span> 关键字等特性。Node.js 也将 JavaScript 带到了服务器端。</span>在语言层面上，Perl 和 JavaScript 之间有着非常密切的关系，凭借着这些契机，</span>Mojolicious 团队创建了 <span style="background-color:#ffffff; color:#445555">mojo.js</span> 项目。</p> 
<p>Mojolicious 开发团队表示，打造 mojo.js 并不是意味着他们要放弃 Mojolicious，因为目前仍有许多非常喜欢 Perl 的开发，他们会继续开发和维护 Mojolicious。</p> 
<p> </p>
                                        </div>
                                      
</div>
            