
---
title: '聊聊JSON与XML的各自优缺点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4671'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 04:25:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=4671'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>JSON已成web数据传输的首要选择，今天就来谈谈XML与JSON，包括两者的相同点与共同点，以及优缺点。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">JSON</h2>
<p>一种轻量级的数据交换格式，是JavaScript的子集，由于是一种语言层面的规范，因此得以更好地在客户端解析使用。</p>
<ul>
<li>
<p>数据格式：数字、布尔、字符串（双引号）、对象、数组、null，没有undefined。</p>
</li>
<li>
<p>良好的API支持（JSON.stringify,JSON.parse），可以在客户端实现javascript对象 与 JSON字符串之间的相互转化</p>
</li>
<li>
<p>stringify(jsonObj,function()&#123; //对序列化做过滤限制 &#125;，space);space用于对序列号结果做缩进结构化，增强易读性。</p>
</li>
<li>
<p>parse(jsonString,function()&#123; //对解析做过滤限制 &#125;)</p>
</li>
<li>
<p>JSON的序列化和解析目标如果是对象或数组，需要注意的是会首先解析这个主题（key值为""）,每遇到一个对象成员，都会递归式地进行序列化或解析，<strong>首先处理好对象本身，才能过滤对象成员</strong>。因此，要做限制的时候需要注意。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">///错误写法</span>
<span class="hljs-keyword">var</span> jsonObj = &#123; <span class="hljs-attr">name</span>:<span class="hljs-string">"Andrew"</span>,<span class="hljs-attr">sex</span>:<span class="hljs-string">"male"</span> &#125;
<span class="hljs-built_in">JSON</span>.stringify(jsonObj,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key,value</span>)</span>&#123;
    <span class="hljs-keyword">if</span>( key === <span class="hljs-string">"name"</span> )&#123;
        <span class="hljs-keyword">return</span> value
    &#125;
&#125;)
<span class="hljs-comment">//返回 ： undefined</span>


<span class="hljs-comment">//正确写法</span>
<span class="hljs-keyword">var</span> jsonObj = &#123; <span class="hljs-attr">name</span>:<span class="hljs-string">"hezebing"</span>,<span class="hljs-attr">sex</span>:<span class="hljs-string">"male"</span> &#125;
<span class="hljs-built_in">JSON</span>.stringify(jsonObj,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key,value</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(key === <span class="hljs-string">""</span>)&#123;
        <span class="hljs-comment">//对象本身</span>
        <span class="hljs-keyword">return</span> value
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>( key === <span class="hljs-string">"name"</span> )&#123;
        <span class="hljs-keyword">return</span> value
    &#125;
&#125;)
<span class="hljs-comment">//返回 ： "&#123;"name":"hezebing"&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">XML</h2>
<p>一种可扩展的标记语言，优点在于描述数据凸显其结构性，在良好的UI层面增加新元素非常简单而清晰。</p>
<ul>
<li>
<p>描述一个实体（person），没有限定属性或者子元素来定义实体的属性（身高，年龄，性别等等），带来了很多的灵活性，也造成了不同程序之间的差异习惯，可扩展意味着"多形态",某种层面的不统一。</p>
</li>
<li>
<p>当服务端发送XML文档至客户端后，需要客户端做解析为DOM树再做节点遍历来获取数据。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><school name=<span class="hljs-string">"北大"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">colleages</span>></span>
        <span class="hljs-comment"><!-- 经济学院 --></span> 
        <span class="hljs-tag"><<span class="hljs-name">economy</span>></span><span class="hljs-tag"></<span class="hljs-name">economy</span>></span>
        <span class="hljs-comment"><!-- 新增 达摩学院 --></span> 
        <span class="hljs-tag"><<span class="hljs-name">damo</span>></span><span class="hljs-tag"></<span class="hljs-name">damo</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">colleages</span>></span></span>
</school>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">总结</h2>
<p>json轻便、解析简单，对客户端更加友好。</p>
<p>XML更加笨重，解析为DOM树并遍历节点来取数据，优点是结构清晰，扩展性好。</p></div>  
</div>
            