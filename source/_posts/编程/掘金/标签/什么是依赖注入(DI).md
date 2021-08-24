
---
title: '什么是依赖注入(DI)'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31454be18324f6eb2d4539072a837e5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:25:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31454be18324f6eb2d4539072a837e5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文将会对依赖注入做一个简单的介绍。</p>
<p>假如我们要从零开始做一个 <code>to-B</code> 方向的平台，最开始的想法是什么呢？</p>
<ol>
<li>在前端蛮荒纪，什么都是从零开始，直接撸 html、js、css，所以现在是这样子的。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31454be18324f6eb2d4539072a837e5~tplv-k3u1fbpfcp-watermark.image" alt="（管理员用户）意见反馈.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>渐渐的前端涌入了很多人，大家开发出很多好用的模块，再后来，Grunt、Browserify、gulp、webpack 等前端打包工具，npm、yarn 等包管理工具横空出世，我们渐渐地可以使用其他人开发出的模块去开发我们的网站，这就是广义的<strong>依赖注入</strong>。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e147a5dd380c487db1e1bbf83e8e6702~tplv-k3u1fbpfcp-watermark.image" alt="（管理员用户）意见反馈 (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>再到后来，前端涌入了更多的人，<code>Angular、React、Vue</code> 横空出世，我们开始采用框架来开发网站，但是我们不需要关心 <code>React</code> 里面用了什么模块、进行了什么处理，这就是广义上的<strong>控制反转</strong>。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d3efe06e6144f26b005fbab68bf5d03~tplv-k3u1fbpfcp-watermark.image" alt="（管理员用户）意见反馈 (4).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总的来说，前端的发展史就是一个面向对象语言的进化史呢。</p>
<p>众所周知，javascript 是一门面向对象(Object-oriented programming，OOP)的语言，依赖注入(DI)和控制反转(IoC)是具体的手段，是OOP理论中<strong>依赖倒置原则</strong>的体现形式，通过<strong>信息隐藏</strong>来<strong>降低对象之间的耦合</strong>。</p>
<p><strong>将创建对象的任务转移给其他 class，并直接使用依赖项的过程，被称为“依赖项注入”。</strong>（DI）</p>
<p>IOC 就是一个可以自动实例化具体类并且管理各对象之间关系的<strong>容器</strong>，有了这个自动化的容器，我们关注的就不是具体的关系，而是上升到只需关注抽象之间的关系，而且还可以省去手动实例化。</p>
<p>事实上我们使用某些<code>npm</code> 的过程就是一种对依赖注入的使用了。再比如以下 <code>jquery</code> 的注入。</p>
<pre><code class="hljs language-js copyable" lang="js">!(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">$, <span class="hljs-built_in">window</span></span>) </span>&#123;
   ...
&#125;)(jQuery, <span class="hljs-built_in">window</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有使用依赖注入示例模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.js</span>
<span class="hljs-keyword">var</span> User = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./user'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTeam</span>(<span class="hljs-params">teamId</span>) </span>&#123;
  <span class="hljs-keyword">return</span> User.find(&#123;<span class="hljs-attr">teamId</span>: teamId&#125;);
&#125;

<span class="hljs-built_in">module</span>.exports.getTeam = getTeam;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用依赖注入示例模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Team</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.options = options;
&#125;

Team.prototype.getTeam = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">teamId</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.options.User.find(&#123;<span class="hljs-attr">teamId</span>: teamId&#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Team(options);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者尝试 es6 的写法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.js</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Team</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constuctor</span>(<span class="hljs-params">options</span>)</span> &#123;
<span class="hljs-built_in">this</span>.options = options;
&#125;

<span class="hljs-attr">getTeam</span>: <span class="hljs-function">(<span class="hljs-params">teamId</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.options.User.find(&#123;<span class="hljs-attr">teamId</span>: teamId&#125;)
&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Team(options);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较显示使用依赖注入的模块有：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Controller, Get &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nestjs/common'</span>;

<span class="hljs-meta">@Controller</span>(<span class="hljs-string">'cats'</span>)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CatsController</span> </span>&#123;
  <span class="hljs-meta">@Get</span>()
  findAll(): <span class="hljs-built_in">string</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'This action returns all cats'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（该代码截取自 nest 官网）</p>
<p>或者是这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

@Component(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'hello-world'</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <h2>Hello World</h2>
    <p>This is my first component!</p>
    `</span>,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorldComponent</span> </span>&#123;
  <span class="hljs-comment">// The code in this class drives the component's behavior.</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（该代码截取自 Angular 官网）</p>
<p>学习了依赖注入后，我们可以更专注于模块的封装，从而更好的实现高内聚低耦合的代码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a88e6aece847eba13a6eb02f1ae9e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">更多</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huaweicloud.com%2Farticles%2F9fafbcda1b487e833fa1cf6cfd283c7d.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huaweicloud.com/articles/9fafbcda1b487e833fa1cf6cfd283c7d.html" ref="nofollow noopener noreferrer">什么是IOC(控制反转)、DI(依赖注入)</a></p></div>  
</div>
            