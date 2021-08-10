
---
title: '【决战Koa之巅-5】使用Prettier让你的项目代码风格统一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b4118c027a47d9979f136e49c0b348~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 18:30:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b4118c027a47d9979f136e49c0b348~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、为什么要让代码风格统一？</h1>
<blockquote>
<p>试着想象一下，如果团队有三个前端，写的 <code>if...else</code>循环如下</p>
</blockquote>
<h3 data-id="heading-1">程序员A：</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a=<span class="hljs-string">'123'</span>
<span class="hljs-keyword">if</span>(a===<span class="hljs-string">'123'</span>)
alert(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">程序员B：</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a=<span class="hljs-string">'123'</span>;
<span class="hljs-keyword">if</span>(a===<span class="hljs-string">'123'</span>)&#123;
  alert(a);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">程序员C：</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-string">"123"</span>;
<span class="hljs-keyword">if</span> (a === <span class="hljs-string">"123"</span>) &#123;
  alert(a);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么以上三种风格，你觉得哪种最好呢？<br>
很显然，第三种<code>可读性</code>最好！</p>
<h1 data-id="heading-4">二、Prettier</h1>
<blockquote>
<p>本来写代码就已经有很重的心智负担了，还要去注重格式？那岂不是让我们更身心疲惫？</p>
</blockquote>
<p>是的，确实会增加心智负担，那么现在有一个工具，能够让你在保存代码的时候<code>自动格式化</code>，是不是想想就觉得很<code>兴奋</code>？</p>
<ul>
<li>引用下官网的介绍</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b4118c027a47d9979f136e49c0b348~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>效果预览</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18bd7891d2f7476097285784893b133b~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-10 09-29-21.2021-08-10 09_30_53.gif" loading="lazy" referrerpolicy="no-referrer">
<br><code>是不是很爽？</code></p>
<h1 data-id="heading-5">三、配置</h1>
<p>它支持市面上的主流编辑器：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e5cab72646e4f7780e0a7970c6c8a20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里，我主要说一说 <code>VS Code</code>配置方式</p>
<h2 data-id="heading-6">VS Code</h2>
<p>很简单，三步即可！</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
安装Prettier插件 --> 设置VSCode保存格式化规则
设置VSCode保存格式化规则 --> Package.JSON配置规则
</code></pre>
<h3 data-id="heading-7">安装Prettier插件</h3>
<p>搜索安装即可
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da64fb85d99648aba53ba0d269df11ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">配置保存格式化</h3>
<p>打开 <code>VS Code</code> 的设置界面<br>
Mac：CMD + ,<br>
Windows：Ctrl + ,
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6162baf4e6004eb6a7a43f0f98423e54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">Package.json配置规则</h3>
<blockquote>
<p>为什么要在这里进行配置呢？为了便于多人<code>GIT</code>协作时候，保持规则一致！</p>
</blockquote>
<p>增加如下规则：</p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"prettier"</span>: &#123;
    <span class="hljs-attr">"singleQuote"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"semi"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"tabWidth"</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">"useTabs"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"trailingComma"</span>: <span class="hljs-string">"none"</span>,
    <span class="hljs-attr">"bracketSpacing"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"arrowParens"</span>: <span class="hljs-string">"avoid"</span>,
    <span class="hljs-attr">"jsxBracketSameLine"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"proseWrap"</span>: <span class="hljs-string">"preserve"</span>,
    <span class="hljs-attr">"printWidth"</span>: <span class="hljs-number">80</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.prettier.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.prettier.cn/" ref="nofollow noopener noreferrer">Prettier官网</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F81764012" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/81764012" ref="nofollow noopener noreferrer">Prettier深入理解</a></p></div>  
</div>
            