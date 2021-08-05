
---
title: '企业项目微前端改造——qiankun框架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=851'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:16:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=851'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">讲述之前在一家公司，经历了一次巨石项目的微前端改造(本篇几乎不涉及开发代码)。代码又是由第三方公司外包，后续公司拿来自己开发维护，由于公司业务发展迅猛，前期并没有合理规划前端架构，在开发一年后决定技术改造，提出微前端的方式进行改造，同时提供一套兜底方案。这就面临着，一边是叠加的业务模块，一边是技术改造，两条腿同时走路的问题就在于，资源不够。</h5>
<h3 data-id="heading-1">背景</h3>
<ol>
<li>运营平台业务模块多达100+，近乎于巨石项目</li>
<li>代码的打包发版时间过长</li>
<li>多人协作开发，test环境频繁发版，造成环境不稳定</li>
<li>共用模块频繁冲突，util模块冗余</li>
</ol>
<p><code>基于上述4点，进行项目改造</code></p>
<h3 data-id="heading-2">预研</h3>
<ol>
<li>拆服务——对于运营平台各个模块进行领域划分</li>
<li>方案一：iframe 作为沙盒容器承载着各个服务</li>
<li>方案二：拆服务，以一个服务作为主入口，关联其他服务(子入口)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">这里做个小结
- 两套方法的思想其实是差不多的，大容器套小容器，关键是容器直接的通信、用户鉴权
- 微前端是个微服务的思想，如果从<span class="hljs-number">0</span>-<span class="hljs-number">1</span>做微前端是容易的，技改成微前端，存在一定挑战

<span class="copy-code-btn">复制代码</span></code></pre>
<p>后续预研中，大佬提出使用qiankun框架，这个框架说是大厂做背书，应该不会有太多问题，(那会儿，qiankun刚开源没多久)。后面就是在已有项目中demo、申请服务资源、登陆权限。</p>
<h3 data-id="heading-3">qiankun 摘要</h3>
<p><code>yarn add qiankun # or npm i qiankun -S</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
<span class="hljs-comment">// 加载微应用</span>
loadMicroApp(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'reactApp'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:7100'</span>,
  <span class="hljs-attr">container</span>: <span class="hljs-string">'#container'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">slogan</span>: <span class="hljs-string">'Hello Qiankun'</span>,
  &#125;,
&#125;);
<span class="hljs-comment">// https://qiankun.umijs.org/zh</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>qiankun框架中，提供了父、子服务的概念，它为我们实现的是父、子之间的通信，登陆权限、用户状态、解决缓存</p>
<h3 data-id="heading-4">巨石项目需要处理的问题</h3>
<ol>
<li>本地权限的拆分</li>
<li>node中间层(用于前端鉴权)交由后端负责</li>
<li>限制发版次数</li>
<li>共用模块拆分</li>
</ol>
<h3 data-id="heading-5">总结</h3>
<pre><code class="hljs language-js copyable" lang="js">- 对巨石项目的拆解，套用qiankun框架，最后失败
- 在已经拆分的服务的基础上，采用兜底方案处理
- 失败的原因，qiankun社区尚未丰富，平台自身业务发展迅速，完全的qiankun化改造，跟不上预期效果
- 探索qiankun的过程中，一部分拆解也在兜底方案中得以应用，也是有一定成果
- 微前端，是一种前端分发的理念。
- 之前，遇到的项目，也是微前端思想，采用的是我们的兜底策略，只是人家把公共组件使用npm分发的方式
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            