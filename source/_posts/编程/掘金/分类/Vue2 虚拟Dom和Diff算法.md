
---
title: 'Vue2 虚拟Dom和Diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=779'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 18:06:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=779'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是虚拟Dom:</h3>
<h5 data-id="heading-1"><em>通过一个对象去保存和记录页面真实Dom节点,当我们的页面发生变化时,会生成对应的新的虚拟Dom,新的虚拟Dom则会和旧的虚拟Dom进行比对,如果对比发现旧的虚拟Dom和新的虚拟Dom之间发生了变化,则新的虚拟Dom则会替换到旧的虚拟Dom,同时在页面生成新的真实Dom</em></h5>
<h3 data-id="heading-2">虚拟Dom的表现形式</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> nodeDom = &#123;
      <span class="hljs-string">"sel"</span>: <span class="hljs-string">"div"</span>,
      <span class="hljs-string">"data"</span>: &#123;
        <span class="hljs-string">"class"</span>: &#123; <span class="hljs-string">"box"</span>: <span class="hljs-literal">true</span> &#125;
      &#125;,
      <span class="hljs-string">"children"</span>: [
        &#123;
          <span class="hljs-string">"sel"</span>: <span class="hljs-string">"span"</span>,
          <span class="hljs-string">"data"</span>: &#123;&#125;,
          <span class="hljs-string">"text"</span>: <span class="hljs-string">"我是文字"</span>
        &#125;,
        &#123;
          <span class="hljs-string">"sel"</span>: <span class="hljs-string">"ul"</span>,
          <span class="hljs-string">"data"</span>: &#123;&#125;,
          <span class="hljs-string">"children"</span>: [
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"苹果"</span> &#125;,
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"香蕉"</span> &#125;,
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"柠檬"</span> &#125;
          ]
        &#125;
      ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">如果此时我们在ul中新插入一条信息 则新的虚拟Dom的表现形式为:</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> nodeDom = &#123;
      <span class="hljs-string">"sel"</span>: <span class="hljs-string">"div"</span>,
      <span class="hljs-string">"data"</span>: &#123;
        <span class="hljs-string">"class"</span>: &#123; <span class="hljs-string">"box"</span>: <span class="hljs-literal">true</span> &#125;
      &#125;,
      <span class="hljs-string">"children"</span>: [
        &#123;
          <span class="hljs-string">"sel"</span>: <span class="hljs-string">"span"</span>,
          <span class="hljs-string">"data"</span>: &#123;&#125;,
          <span class="hljs-string">"text"</span>: <span class="hljs-string">"我是文字"</span>
        &#125;,
        &#123;
          <span class="hljs-string">"sel"</span>: <span class="hljs-string">"ul"</span>,
          <span class="hljs-string">"data"</span>: &#123;&#125;,
          <span class="hljs-string">"children"</span>: [
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"苹果"</span> &#125;,
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"香蕉"</span> &#125;,
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"柠檬"</span> &#125;,
            &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"橘子"</span> &#125;,
          ]
        &#125;
      ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">虚拟Dom的一个重要函数: h函数</h4>
<ul>
<li>h函数用来生成虚拟节点(Vnode)</li>
<li>h函数是这样调用的</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">h(<span class="hljs-string">'a'</span>,&#123;<span class="hljs-attr">props</span>:&#123;<span class="hljs-attr">href</span>:<span class="hljs-string">'https://www.baidu.com'</span>&#125;&#125;,<span class="hljs-string">'百度'</span>)
<span class="hljs-comment">//通过调用h函数的到的虚拟节点为</span>
&#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"a"</span>, <span class="hljs-string">"data"</span>: &#123; <span class="hljs-string">"props"</span>: &#123; <span class="hljs-string">"href"</span>: <span class="hljs-string">"https://www.baidu.com"</span> &#125; &#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"百度"</span> &#125;
<span class="hljs-comment">//页面真正的节点为:</span>
<a href=<span class="hljs-string">"https://www.baidu.com"</span>>百度</a>

<span class="hljs-comment">//h函数可以嵌套使用</span>
<span class="hljs-keyword">const</span> myNode = h(<span class="hljs-string">'ul'</span>,&#123;&#125;,[
    h(<span class="hljs-string">'li'</span>,&#123;&#125;,<span class="hljs-string">'苹果'</span>),
    h(<span class="hljs-string">'li'</span>,&#123;&#125;,<span class="hljs-string">'香蕉'</span>),
    h(<span class="hljs-string">'li'</span>,&#123;&#125;,<span class="hljs-string">'柠檬'</span>)
])

<span class="hljs-comment">//此时得到的虚拟Dom</span>
&#123;
  <span class="hljs-string">'sel'</span>:<span class="hljs-string">'ul'</span>,
  <span class="hljs-string">'data'</span>:&#123;&#125;,
  <span class="hljs-string">'children'</span>:[
    &#123;<span class="hljs-string">'sel'</span>:<span class="hljs-string">'li'</span>,<span class="hljs-attr">data</span>:&#123;&#125;,<span class="hljs-string">'text'</span>:<span class="hljs-string">'苹果'</span>&#125;,
    &#123;<span class="hljs-string">'sel'</span>:<span class="hljs-string">'li'</span>,<span class="hljs-attr">data</span>:&#123;&#125;,<span class="hljs-string">'text'</span>:<span class="hljs-string">'香蕉'</span>&#125;,
    &#123;<span class="hljs-string">'sel'</span>:<span class="hljs-string">'li'</span>,<span class="hljs-attr">data</span>:&#123;&#125;,<span class="hljs-string">'text'</span>:<span class="hljs-string">'柠檬'</span>&#125;,
  ]
&#125;

<span class="hljs-comment">//此时的虚拟Dom需要通过patch函数上树  今天只手写h函数和diff算法  不考虑patch函数上树</span>

<span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>)
patch(box, myNode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>未完待续</p></div>  
</div>
            