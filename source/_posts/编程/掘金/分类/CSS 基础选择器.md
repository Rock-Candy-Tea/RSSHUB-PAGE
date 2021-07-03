
---
title: 'CSS 基础选择器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4437'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 05:40:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=4437'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">标签选择器</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
     <span class="hljs-attribute">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点:能快速为页面中同类型的标签统一设置样式</li>
<li>缺点:不能设计差异化样式，只能选择全部的当前标签</li>
</ul>
<h3 data-id="heading-1">类选择器</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.hobby</span> &#123;
    <span class="hljs-attribute">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">多类名开发中使用场景</h4>
<ul>
<li>可以把一些标签元素相同的样式放到一个类里面</li>
<li>这些标签都可以调用这个公共的类，然后再调用自己独有的类</li>
<li>各个类名中间用空格隔开</li>
<li>多类名选择器在后期布局比较复杂的情况下，还是比较多使用的</li>
</ul>
<h3 data-id="heading-3">id选择器</h3>
<p>id选择器以"#"来定义的</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#pink</span> &#123;
<span class="hljs-attribute">color</span>: pnik;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>id选择器和类选择器最大的不同在于使用次数上</li>
<li>类选择器在修改样式中用的最多，id选择器一般用于页面唯一性的元素上，经常和javascript搭配使用</li>
<li>id选择器只能调用一次，别人切勿使用</li>
</ul>
<h3 data-id="heading-4">通配符选择器</h3>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
属性<span class="hljs-number">1</span>:属性值<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通配符选择器不需要提调用，自动就给所有的元素使用样式</li>
<li>特殊情况才使用</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            