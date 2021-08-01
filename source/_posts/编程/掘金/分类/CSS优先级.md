
---
title: 'CSS优先级'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1592'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 04:20:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=1592'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在说css优先级之前，先要了解一个情况，
实际上，<code>1000,100,10,1</code>不是十进制中的<code>1000,100,10,1</code>，而是进制数，不是<code>2</code>进制，不是<code>10</code>进制，而是<code>256</code>进制，就是<code>0</code>到<code>255</code>后<code>+1</code>才是<code>1</code>，比如通配符的权重为<code>0</code>，伪元素的权重为<code>1</code>，中间相差了<code>255</code>，依次类推。</p>
<p>并且，<code>!important</code>的权重虽然为正无穷，但也是可以计算的，比如正无穷<code>+1</code>或者<code>*2</code>就比正无穷大，原因是计算机中的正无穷是有界的，不是数学上无界的概念。</p>
<h3 data-id="heading-0">CSS选择器类型</h3>
<p><strong>样式类型</strong></p>
<p>行内样式：<code><style></style></code></p>
<p>内联样式：<code><div style="color:red;"></code></p>
<p>外部样式：<code><link>或@import引入</code></p>
<p><strong>选择器类型</strong></p>
<p>id选择器、class选择器、属性选择器、*、伪类选择器、伪元素、后代选择器、子类选择器、兄弟选择器</p>
<h3 data-id="heading-1">权重计算规则</h3>
<ul>
<li>第一优先级：<code>!important</code>会覆盖页面内任何位置的元素样式</li>
<li>1.内联样式，如<code>style="color: green"</code>，权值为<code>1000</code></li>
<li>2.ID选择器，如<code>#app</code>，权值为<code>0100</code></li>
<li>3.类、伪类、属性选择器，如<code>.foo, :first-child, div[class="foo"]</code>，权值为<code>0010</code></li>
<li>4.标签、伪元素选择器，如<code>div::first-line</code>，权值为<code>0001</code></li>
<li>5.通配符、子类选择器、兄弟选择器，如<code>*, >, +</code>，权值为<code>0000</code></li>
<li>6.继承的样式没有权值</li>
</ul>
<h3 data-id="heading-2">优先级注意点:</h3>
<ol>
<li>
<p>权重是有4组数字组成,但是不会有进位。</p>
</li>
<li>
<p>可以理解为类选择器永远大于元素选择器, id选择器永远大于类选择器,以此类推..</p>
</li>
<li>
<p>等级判断从左向右，如果某一位数值相同，则判断下一位数值。</p>
</li>
<li>
<p>可以简单记忆法: 通配符和继承权重为0, 标签选择器为1,类(伪类)选择器为 10, id选择器 100, 行内样式表为1000, !important 无穷大.</p>
</li>
<li>
<p>继承的权重是0， 如果该元素没有直接选中， 不管父元素权重多高，子元素得到的权重都是 0.通配符、子选择器、兄弟选择器，虽然权重为<code>0000</code>，但是优先于继承的样式</p>
</li>
<li>
<p>权重相同的情况下，位于后面的样式会覆盖前面的样式</p>
</li>
</ol>
<h3 data-id="heading-3">权重叠加：</h3>
<p>如果是复合选择器，则会有权重叠加，需要计算权重。</p>
<pre><code class="hljs language-js copyable" lang="js"> div ul li ------> <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span> 
.nav ul li ------> <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span> 
 <span class="hljs-attr">a</span>:hover -----—> <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span> 
.nav a ------> <span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            