
---
title: 'TypeScript 每日挑战，你敢来试试吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2207'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 07:46:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=2207'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
</blockquote>
<p>其实大多数 TypeScript 开发者，对 TypeScript 的利用，还停留在初级水平。</p>
<p>不信吗？来试试每日挑战吧！</p>
<h2 data-id="heading-0">今日题目</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 我有一堆必填字段</span>
<span class="hljs-keyword">interface</span> DocType &#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">bbb</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">ccc</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-comment">// 函数类型定义，等你来改写 ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeDoc</span>(<span class="hljs-params">part1: <span class="hljs-built_in">any</span>, part2: <span class="hljs-built_in">any</span></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一个名为 <code>DocType</code> 的 <code>interface</code>，包含一组必填字段</p>
<p>需要实现一个名为 <code>makeDoc</code> 的函数定义，它有 2 个参数：<code>part1</code>、<code>part2</code>，它们都拥有 <code>DocType</code> 的部分字段（<code>Partial<DocType></code>）</p>
<p>需要你在 TypeScript 类型定义层面，实现 <code>makeDoc</code> 两个参数的类型校验：</p>
<ol>
<li><code>part1</code> 和 <code>part2</code> 的字段合并后，即 <code>Object.assign(&#123;&#125;, part1, part2)</code>，满足 <code>DocType</code> 的类型定义。</li>
<li><code>part1</code> 和 <code>part2</code> 中不能有重复字段。</li>
</ol>
<h2 data-id="heading-1">测试用例</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 合法</span>
makeDoc(&#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'111'</span>,
    <span class="hljs-attr">bbb</span>: <span class="hljs-string">'222'</span>
&#125;, &#123;
    <span class="hljs-attr">ccc</span>: <span class="hljs-string">'333'</span>
&#125;)

<span class="hljs-comment">// 合法</span>
makeDoc(&#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'111'</span>,
    <span class="hljs-attr">bbb</span>: <span class="hljs-string">'222'</span>,
    <span class="hljs-attr">ccc</span>: <span class="hljs-string">'333'</span>
&#125;, &#123;&#125;)

<span class="hljs-comment">// 合法</span>
makeDoc(&#123;<span class="hljs-attr">ccc</span>: <span class="hljs-string">'333'</span>&#125;, &#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'111'</span>,
    <span class="hljs-attr">bbb</span>: <span class="hljs-string">'222'</span>
&#125;)

<span class="hljs-comment">// 应该报错（因为缺少必填字段 ccc）</span>
makeDoc(&#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'111'</span>,
&#125;, &#123;
    <span class="hljs-attr">bbb</span>: <span class="hljs-string">'222'</span>
&#125;)

<span class="hljs-comment">// 应该报错（因为 aaa 字段重复出现）</span>
makeDoc(&#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'111'</span>,
    <span class="hljs-attr">bbb</span>: <span class="hljs-string">'222'</span>
&#125;, &#123;
    <span class="hljs-attr">aaa</span>: <span class="hljs-string">'333'</span>,
    <span class="hljs-attr">ccc</span>: <span class="hljs-string">'444'</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>欢迎你将答案或者思路留言在评论区~</p>
<p>答案将在 <strong>周五下午 17:00</strong> 揭晓。</p></div>  
</div>
            