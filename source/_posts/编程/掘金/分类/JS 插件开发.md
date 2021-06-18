
---
title: 'JS 插件开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6041'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 05:05:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=6041'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>jQuery 插件两种函数的开发</strong>：</p>
<p><strong>1. 类级别的插件开发</strong>：
类级别的插件开发最直接的理解就是给 jQuery 类添加类方法，可以理解为添加静态方法。典型的例子就是"$.ajax()"这个函数，将函数定义于jQuery的命名空间中。</p>
<p>类级别插件开发的几种形式进行扩展：</p>
<ul>
<li>添加一个新的全局函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">$.hello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    alert(<span class="hljs-string">"Hello！"</span>) ;
&#125; ;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>增加多个全局函数添加多个全局函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">$.extend(&#123;
    <span class="hljs-attr">hello</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-comment">// put your code here</span>
    &#125; ,
    <span class="hljs-attr">world</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// put your code here</span>
    &#125;
&#125;) ;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用jQuery.extend(object)</li>
<li>使用命名空间</li>
</ul>
<p>说明：”$.extend(target, [object1], [objectN])“（该方法主要用于合并两个或更多对象的内容(属性)到第一个对象，并返回合并后的第一对象。</p>
<p>如果该方法只有一个参数target，则该参数将扩展jQuery的命名空间，即作为静态方法挂在jQuery全局对象下）。</p>
<p><strong>2. 对象级别的插件开发</strong></p>
<p>对象级别的插件开发需要如下的两种形式：</p>
<ul>
<li>通过“$.fn.extend()”为原型动态挂载相关的属性。</li>
</ul>
<pre><code class="copyable">(function($)&#123;  
    $.fn.extend(&#123;  
        pluginName : function(opts)&#123;  
            // put your code here
        &#125;  
    &#125;) ;  
&#125;)(jQuery) ; 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>直接添加动态属性到原型链上。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>) </span>&#123;    
     $.fn.pluginName = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;  
         <span class="hljs-comment">// put your code here </span>
     &#125; ;  
 &#125;)(jQuery) ; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：二者是等价的，对于一个 jQuery 插件，一个基本的函数就可以很好地工作，但是对于复杂一点的插件就需要提供各种各样的方法和私有函数。</p>
<p><strong>jQuery 插件开发的规范</strong>：</p>
<ul>
<li>使用闭包：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>)</span>&#123;
    <span class="hljs-comment">//Code goes here</span>
&#125;)(jQuery);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是来自jQuery官方的插件开发规范要求，使用这种编写方式有什么好处呢？</p>
<p>a) 避免全局依赖
b) 避免第三方破坏
c) 兼容 jQuery 操作符 ’$’ 和 ’jQuery’</p></div>  
</div>
            