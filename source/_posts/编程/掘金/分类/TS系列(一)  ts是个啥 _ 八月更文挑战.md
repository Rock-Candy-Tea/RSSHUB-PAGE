
---
title: 'TS系列(一)  ts是个啥 _ 八月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/508447763b314e1c9f2c83fb84d1be42~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 18:06:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/508447763b314e1c9f2c83fb84d1be42~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>在前端项目越来越大的今天,我们急需一种方式能够在开发阶段发现潜在问题,而不是在运行阶段排查错误。为了解决此类问题，微软带着<code>TypeScript</code>来了，下文<code>TypeScript</code>简称<code>TS</code>。</p>
<h1 data-id="heading-1">1、TS是什么</h1>
<ul>
<li>1.1 TS是微软开发的开源编程语言，可以在任何运行JS的地方运行</li>
<li>1.2 TS是JS的超集，也就是说TS在包含了所有JS实现的基础上，又对JS进行了补充(增加了类型支持)，请看下图，TS包含了JS的所有实现和JS的类型支持
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/508447763b314e1c9f2c83fb84d1be42~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h1 data-id="heading-2">2、我们为什么要用TS</h1>
<ul>
<li>2.1 JS的类型系统存在"先天缺陷"，JS代码中的绝大部分错误都是UncaughtTypeError,增加了在开发过程中找bug、该bug的时间</li>
<li>2.2 TS属于静态类型的编程语言，JS则属于动态类型的编程语言，TS在编译期做类型检查可以更早的发现错误；JS则会在执行期做类型检查，需要等到代码真正执行的时候才能发现问题</li>
<li>2.3 TS开发项目，程序中的任何位置都会有代码提示，提高了开发体验</li>
<li>2.4 TS支持最新的<code>ECMAScript</code>语法，使用最新的语法开发项目，享受极致的开发体验</li>
<li>2.5 TS强大的类型系统，提升了代码的可维护性，降低项目重构的难度</li>
<li>2.6 基于TS强大的<code>类型推断</code>，不需要我们在写代码的时候显示的标注类型，降低了开发成本</li>
</ul>
<h1 data-id="heading-3">3、 安装TS</h1>
<pre><code class="hljs language-js copyable" lang="js"> npm i -g typescript
 <span class="hljs-comment">// 查看ts版本</span>
 tsc -v
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.1 TS的包提供了<code>tsc</code>命令，可以实现TS --> JS的转换(浏览器只识别JS代码，不认识TS代码),如图</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5f12b55eddc41bd82e501287812f80d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">4、TS初体验</h1>
<ul>
<li>4.1 首先创建一个<code>index.ts</code>文件,并写入以下代码</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7ddb219319f407089cc6d55779d4363~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.2 接下来我们通过<code>tsc</code>把TS代码编译成JS代码</li>
</ul>
<pre><code class="copyable">    tsc ./index.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0954da355cd441e987182ddfc580410c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个时候我们就可以看到<code>index.js</code>文件被<code>tsc</code>命令编译成功</p>
<h1 data-id="heading-5">结尾</h1>
<ul>
<li>这个时候，我们就了解了什么是TS，TS能做什么</li>
</ul>
<h1 data-id="heading-6">写在最后</h1>
<ul>
<li>TS系列文章会由浅入深的逐步带你领略TS的魅力</li>
<li>欢迎大家评论，指出不完善的地方</li>
</ul></div>  
</div>
            