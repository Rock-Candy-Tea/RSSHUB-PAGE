
---
title: '采用Rem适配大屏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9106'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:26:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=9106'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>需要为大屏在不同的设备上进行查看，但是在需求中有很多布局需要去设置具体的像素值，如果采用通常的百分比布局，无法满足需求，这个时候想到了移动端布局的解决方案<code>rem</code>.</p>
<h3 data-id="heading-0">rem是什么？</h3>
<p>rem（font size of the root element）是指相对于根元素的字体大小的单位。简单的说它就是一个相对单位。看到rem大家一定会想起em单位，em（font size of the element）是指相对于父元素的字体大小的单位。它们之间其实很相似，只不过一个计算的规则是依赖根元素一个是依赖父元素计算。</p>
<p>我们可以通过动态计算html跟标签的font-size大小来实现大屏的适配，具体实现代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> baseNumber = <span class="hljs-number">100</span>; <span class="hljs-comment">// 获取相对好计算的基数</span>

<span class="hljs-comment">/**
 * 设置html节点fontSize值得大小，需要动态计算
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>designWidth 设计稿大小
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setHtmlFontSize</span>(<span class="hljs-params">designWidth = <span class="hljs-number">1920</span></span>) </span>&#123; <span class="hljs-comment">// 设计稿宽度为1920，利用移动端rem的适配方案，动态修改html的值</span>
    <span class="hljs-keyword">const</span> clientWidth = <span class="hljs-built_in">document</span>.documentElement.clientWidth;

    <span class="hljs-comment">// 选取的是 1920 ， * 100是为了防止浏览器默认行为，如果小于12px默认会处理为12px进行计算。在css中一定要除以100.</span>
    <span class="hljs-keyword">var</span> fontSize = clientWidth / (designWidth) * baseNumber; <span class="hljs-comment">// 计算完毕后，在设计稿上量出的尺寸直接写入，只是把px换成rem即可，其他内部需要动态设置为px的可以乘这个基数（size * fontSize / 100 + 'px'）</span>
    <span class="hljs-keyword">var</span> elHtml = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'html'</span>)[<span class="hljs-number">0</span>];

    <span class="hljs-comment">// elHtml.style.fontSize = (fontSize > 80 ? 80 : fontSize < 50 ? 50 : fontSize) + 'px'; // 规定上限在80px，下限在50px，上下限值根据需求进行调整，也可以不进行调整。</span>
    elHtml.style.fontSize = fontSize + <span class="hljs-string">'px'</span>;
&#125;

<span class="hljs-comment">/**
 * 获取当前的实际像素
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUnitRem</span>(<span class="hljs-params">px</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> px === <span class="hljs-string">'string'</span>) px = <span class="hljs-built_in">parseFloat</span>(px);
    <span class="hljs-keyword">return</span> (<span class="hljs-built_in">isNaN</span>(px) ? <span class="hljs-number">0</span> : px / baseNumber) + <span class="hljs-string">'rem'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            