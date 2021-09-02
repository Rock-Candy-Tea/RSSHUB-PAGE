
---
title: 'jQuery 的功能概述'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7407'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 00:00:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=7407'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.  jQuery 如何获取元素</h2>
<blockquote>
<p>操作网页元素，最常见的需求是取得它们的值，或者对它们进行赋值。</p>
</blockquote>
<blockquote>
<p>就是使用同一个函数，来完成取值（getter）和赋值（setter），即"取值器"与"赋值器"合一。到底是取值还是赋值，由函数的参数决定。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">`$('h1').html();`</span> <span class="hljs-comment">//html()没有参数，表示取出h1的值</span>

　　<span class="hljs-string">`$('h1').html('Hello');`</span> <span class="hljs-comment">//html()有参数Hello，表示对h1进行赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-string">`[.html()]`</span>  取出或设置html内容

　　<span class="hljs-string">`[.text()]`</span>  取出或设置text内容

　　<span class="hljs-string">`[.attr()]`</span>  取出或设置某个属性的值

　　<span class="hljs-string">`[.width()]`</span> 取出或设置某个元素的宽度

　　<span class="hljs-string">`[.height()]`</span>取出或设置某个元素的高度

　　<span class="hljs-string">`[.val()]`</span>   取出某个表单元素的值
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.  jQuery 的链式操作是怎样的</h2>
<blockquote>
<p>最终选中网页元素以后，可以对它进行一系列操作，并且所有操作可以连接在一起，以链条的形式写出来：</p>
</blockquote>
<p><code>$('div').find('h3').eq(2).html('Hello');</code></p>
<ul>
<li>分解开来，就是下面这样：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    $(<span class="hljs-string">'div'</span>) <span class="hljs-comment">//找到div元素</span>

　　　 .find(<span class="hljs-string">'h3'</span>) <span class="hljs-comment">//选择其中的h3元素</span>

　　　 .eq(<span class="hljs-number">2</span>) <span class="hljs-comment">//选择第3个h3元素</span>

　　　 .html(<span class="hljs-string">'Hello'</span>); <span class="hljs-comment">//将它的内容改为Hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>jQuery还提供了[.end()]方法:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">   $(<span class="hljs-string">'div'</span>)

　　　.find(<span class="hljs-string">'h3'</span>)

　　　.eq(<span class="hljs-number">2</span>)

　　　.html(<span class="hljs-string">'Hello'</span>)

　　　**.end() <span class="hljs-comment">//退回到选中所有的h3元素的那一步**</span>

　　　.eq(<span class="hljs-number">0</span>) <span class="hljs-comment">//选中第一个h3元素</span>

　　　.html(<span class="hljs-string">'World'</span>); <span class="hljs-comment">//将它的内容改为World</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.  jQuery 如何创建元素</h2>
<ul>
<li>把新元素直接传入jQuery的构造函数就行:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    $(<span class="hljs-string">'<p>Hello</p>'</span>);

　　$(<span class="hljs-string">'<li class="new">new list item</li>'</span>);

　　$(<span class="hljs-string">'ul'</span>).append(<span class="hljs-string">'<li>list item</li>'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.  jQuery 如何移动元素</h2>
<ul>
<li>第一种方法是使用<code>[.insertAfter()]</code>，把div元素移动p元素后面：</li>
</ul>
<p><code>$('div').insertAfter($('p'));</code></p>
<p>第二种方法是使用<code>[.after()]</code>，把p元素加到div元素前面：</p>
<p><code>$('p').after($('div'));</code></p>
<ul>
<li>
<p>使用这种模式的操作方法，一共有四对：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    [.insertAfter()]和[.after()]：  在现存元素的外部，从后面插入元素

　　[.insertBefore()]和[.before()]：在现存元素的外部，从前面插入元素

　　[.appendTo()]和[.append()]：    在现存元素的内部，从后面插入元素

　　[.prependTo()]和[.prepend()]：  在现存元素的内部，从前面插入元素
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上引自<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2011%2F07%2Fjquery_fundamentals.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2011/07/jquery_fundamentals.html" ref="nofollow noopener noreferrer">jQuery设计思想 - 阮一峰的网络日志 (ruanyifeng.com)</a></p>
<h2 data-id="heading-4">5.  jQuery 如何修改元素的属性</h2>
<ul>
<li><code>jquery</code>中用<code>attr()</code>方法来<strong>获取和设置元素属性</strong>,attr是<strong>attribute</strong>（属性）的缩写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
  $(selector).attr(attribute) <span class="hljs-comment">//attribute 规定要获取其值的属性。</span>

  $(selector).attr(attribute,value)<span class="hljs-comment">//attribute 规定属性的名称; value 规定属性的值。</span>
  

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            