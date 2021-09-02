
---
title: 'js中的只读数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3611'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:59:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=3611'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"></h2>
<p>分享一些javaScript中的一些只读属性的数据 (持续更新中...)</p>
<ul>
<li>eg1</li>
</ul>
<p>字符串用数组关联法获取的值是只读属性的，并不能修改里面的值</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> a = <span class="hljs-string">'string'</span>;
    <span class="hljs-built_in">console</span>.log(a[<span class="hljs-number">0</span>]); <span class="hljs-comment">//s</span>
    a[<span class="hljs-number">0</span>] = <span class="hljs-string">'q'</span>;<span class="hljs-comment">//下面第二行输出还是原来那个数据，并没有改变</span>
    <span class="hljs-comment">//只读属性，跟数组不一样</span>
    <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//string</span>
    <span class="hljs-built_in">console</span>.log(a[<span class="hljs-number">0</span>])<span class="hljs-comment">//s</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>eg2</li>
</ul>
<p>字符对象中的charAt()是从一个字符串中返回一个指定的字符,如果赋值会报错</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> a = <span class="hljs-string">'string'</span>;
    <span class="hljs-built_in">console</span>.log(a.charAt(<span class="hljs-number">0</span>)) <span class="hljs-comment">//s</span>
    a.charAt(<span class="hljs-number">0</span>) = <span class="hljs-string">'q'</span>;
    <span class="hljs-comment">//Invalid left-hand side in assignment</span>
    <span class="hljs-comment">//会报错,charAt()方法是从一个字符串中返回指定的字符</span>
    <span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>eg3</li>
</ul>
<p>HTMLElement.offsetTop和HTMLElement.offsetLeft也是为只读属性,<br>
offsetTop返回当前元素相对于其offsetParent元素的<strong>顶部内边距的距离</strong>,注意要是块级元素</p>
<ul>
<li>eg4</li>
</ul>
<p>除了偏移量，获取页面的元素的宽高等属性,也是只读属性<br>
offsetWidth、offsetHeight(包括边框)<br>
clientWidth、clientHeight(不包括边框)</p>
<ul>
<li>eg5</li>
</ul>
<p>诸如类似时间对象方法里面的获取年份方法.getFullYear()一样以get开头的都是只读属性,一般也会有对应的set开头的方法来设置它,</p>
<h3 data-id="heading-1">设置只读属性的目的</h3>
<p>只读属性的值一般都是基础数据类型，一般存在栈中，节省了在堆中开辟新空间。(个人理解,)</p></div>  
</div>
            