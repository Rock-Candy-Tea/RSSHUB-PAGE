
---
title: '_UI 调试技巧_ CSS的outline调试法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70e1f80fb585475d98a8f792d89e987e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 17:48:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70e1f80fb585475d98a8f792d89e987e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>本文转载自 yck 的文章： <a href="https://github.com/KieSun/Dream/issues/27" target="_blank" rel="nofollow noopener noreferrer">github.com/KieSun/Drea…</a></strong></p>
<p>在业务开发过程中，想必大家经常会需要查看一个元素的位置及大小并修改它的 CSS，因此就会频繁使用到 DevTools 中的选择元素功能。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70e1f80fb585475d98a8f792d89e987e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实我们可以使用一个 CSS 技巧给所有元素加上 outline，这样就能迅速了解自己所需的元素位置信息，无须再选择元素查看了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07ad56ac0ca843eb993edaa6783cb814~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们只需要添加以下 CSS 就能为任何网站添加这样的效果</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span> * &#123;
    <span class="hljs-attribute">outline</span>: <span class="hljs-number">1px</span> solid red
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是这里我没有使用 border 的原因是 border 会增加元素的大小但是 outline 不会。</strong></p>
<p>通过这个技巧不仅能帮助我们在开发中迅速了解元素所在的位置，还能帮助我们方便地查看任意网站的布局。</p>
<p>笔者最喜欢用这个技巧来查看元素是否对齐。</p>
<p>但是当下这个技巧需要我们手动添加 CSS 来实现，显得略微有点鸡肋，是否可以通过一个开关来实现任意网页开启关闭这个功能呢？</p>
<p>答案是有的，我们需要借助 Chrome 的书签功能。</p>
<ol>
<li>打开书签管理页</li>
<li>右上角三个点「添加新书签」</li>
<li>名称随意，粘贴以下代码到网址中</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">javascript: (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> elements = <span class="hljs-built_in">document</span>.body.getElementsByTagName(<span class="hljs-string">'*'</span>);
<span class="hljs-keyword">var</span> items = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < elements.length; i++) &#123;
<span class="hljs-keyword">if</span> (elements[i].innerHTML.indexOf(<span class="hljs-string">'html * &#123; outline: 1px solid red &#125;'</span>) != -<span class="hljs-number">1</span>) &#123;
items.push(elements[i]);
&#125;
&#125;
<span class="hljs-keyword">if</span> (items.length > <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
items[i].innerHTML = <span class="hljs-string">''</span>;
&#125;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-built_in">document</span>.body.innerHTML +=
<span class="hljs-string">'<style>html * &#123; outline: 1px solid red &#125;</style>'</span>;
&#125;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们就可以在任意网站上点击刚才创建的书签，内部会判断是否存在调试的 style。存在的话就删除，不存在的话就添加，通过这种方式我们就能很方便的通过这个技巧查看任意网页的布局了。</p>
<p>PS：以上书签的技巧参考自<a href="https://gist.github.com/vcastroi/e0d296171842e74ad7d4eef7daf15df6" target="_blank" rel="nofollow noopener noreferrer">此处</a>，原内容略微繁琐，笔者改动了 style 中的内容。</p></div>  
</div>
            