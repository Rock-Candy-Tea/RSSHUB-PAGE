
---
title: 'jQuery入门（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6402'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 00:56:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=6402'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">元素操作</h2>
<ul>
<li>
<p>创建一个元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> div = $(<span class="hljs-string">'<div></div>'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>内部插入元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 向 div 元素中插入一个 p 元素，放在最后</span>
$(<span class="hljs-string">'div'</span>).append($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 把 p 元素插入到 div 中去，放在最后</span>
$(<span class="hljs-string">'<p>hello</p>'</span>).appendTo($(<span class="hljs-string">'div'</span>))

<span class="hljs-comment">// 向 div 元素中插入一个 p 元素，放在最前</span>
$(<span class="hljs-string">'div'</span>).prepend($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 把 p 元素插入到 div 中去，放在最前</span>
$(<span class="hljs-string">'<p>hello</p>'</span>).prependTo($(<span class="hljs-string">'div'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>外部插入元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在 div 的后面插入一个元素 p</span>
$(<span class="hljs-string">'div'</span>).after($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 在 div 的前面插入一个元素 p</span>
$(<span class="hljs-string">'div'</span>).before($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 把 p 元素插入到 div 元素的后面</span>
$(<span class="hljs-string">'div'</span>).insertAfter($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 把 p 元素插入到 div 元素的前面</span>
$(<span class="hljs-string">'div'</span>).insertBefore($(<span class="hljs-string">'<p></p>'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>替换元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 把 div 元素替换成 p 元素</span>
$(<span class="hljs-string">'div'</span>).replaceWith($(<span class="hljs-string">'<p></p>'</span>))

<span class="hljs-comment">// 用 p 元素替换掉 div 元素</span>
$(<span class="hljs-string">'<p></p>'</span>).replaceAll($(<span class="hljs-string">'div'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>删除元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 删除元素下的所有子节点</span>
$(<span class="hljs-string">'div'</span>).empty()

<span class="hljs-comment">// 把自己从页面中移除</span>
$(<span class="hljs-string">'div'</span>).remove()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>克隆元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 克隆一个 li 元素</span>
<span class="hljs-comment">// 接受两个参数</span>
<span class="hljs-comment">//   参数1： 自己身上的事件要不要复制，默认是 false</span>
<span class="hljs-comment">//   参数2： 所有子节点身上的事件要不要复制，默认是 true</span>
$(<span class="hljs-string">'li'</span>).clone()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-1">元素尺寸</h2>
<ul>
<li>
<p>操作元素的宽和高</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取 div 元素内容位置的高，不包含 padding 和 border</span>
$(<span class="hljs-string">'div'</span>).height()
<span class="hljs-comment">// 设置 div 内容位置的高为 200px</span>
$(<span class="hljs-string">'div'</span>).height(<span class="hljs-number">200</span>)

<span class="hljs-comment">// 获取 div 元素内容位置的宽，不包含 padding 和 border</span>
$(<span class="hljs-string">'div'</span>).width()
<span class="hljs-comment">// 设置 div 内容位置的宽为 200px</span>
$(<span class="hljs-string">'div'</span>).width(<span class="hljs-number">200</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取元素的内置宽和高</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取 div 元素内容位置的高，包含 padding 不包含 border</span>
$(<span class="hljs-string">'div'</span>).innerHeight()

<span class="hljs-comment">// 获取 div 元素内容位置的宽，包含 padding 不包含 border</span>
$(<span class="hljs-string">'div'</span>).innerWidth()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取元素的外置宽和高</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取 div 元素内容位置的高，包含 padding 和 border</span>
$(<span class="hljs-string">'div'</span>).outerHeight()
<span class="hljs-comment">// 获取 div 元素内容位置的高，包含 padding 和 border 和 margin</span>
$(<span class="hljs-string">'div'</span>).outerHeight(<span class="hljs-literal">true</span>)

<span class="hljs-comment">// 获取 div 元素内容位置的宽，包含 padding 和 border</span>
$(<span class="hljs-string">'div'</span>).outerWidth()
<span class="hljs-comment">// 获取 div 元素内容位置的高，包含 padding 和 border 和 margin</span>
$(<span class="hljs-string">'div'</span>).outerWidth(<span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-2">元素位置</h2>
<ul>
<li>
<p>元素相对页面的位置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取 div 相对页面的位置</span>
$(<span class="hljs-string">'div'</span>).offset() <span class="hljs-comment">// 得到的是以一个对象 &#123; left: 值, top: 值 &#125;</span>

<span class="hljs-comment">// 给 div 设置相对页面的位置</span>
$(<span class="hljs-string">'div'</span>).offset(&#123; <span class="hljs-attr">left</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">top</span>: <span class="hljs-number">100</span> &#125;)
<span class="hljs-comment">// 获取定位到一个距离页面左上角 100 100 的位置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>元素相对于父元素的偏移量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 获取 div 相对于父元素的偏移量（定位的值）</span>
$(<span class="hljs-string">'div'</span>).position()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>获取页面卷去的高度和宽度</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.onscroll = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 获取浏览器卷去的高度</span>
    <span class="hljs-built_in">console</span>.log($(<span class="hljs-built_in">window</span>).scrollTop())
&#125;

<span class="hljs-built_in">window</span>.onscroll = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 获取浏览器卷去的宽度</span>
    <span class="hljs-built_in">console</span>.log($(<span class="hljs-built_in">window</span>).scrollLeft())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            