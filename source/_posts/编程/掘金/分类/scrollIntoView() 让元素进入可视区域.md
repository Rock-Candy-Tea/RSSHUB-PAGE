
---
title: 'scrollIntoView() 让元素进入可视区域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd91ec2ef6d437d822e1579d01f1098~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 17:12:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd91ec2ef6d437d822e1579d01f1098~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我，解锁前端成长新姿势。</p>
<blockquote>
<p>最近更新文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6963071339108237319" target="_blank">图片瀑布流，就是如此简单（so easy）</a></li>
<li><a href="https://juejin.cn/post/6961968236837470216" target="_blank">梳理ajax跨域常用4种解决方案（简单易懂）</a></li>
<li><a href="https://juejin.cn/post/6960852275724025870" target="_blank">JS的静态类型检测，有内味儿了</a></li>
</ul>
</blockquote>
<p>以下正文：</p>
<h2 data-id="heading-0">介绍</h2>
<p>DOM元素的 <code>scrollIntoView()</code>方法是一个IE6浏览器也支持的原生JS API，可以让元素进入视区，通过触发滚动容器的定位实现。</p>
<h2 data-id="heading-1">语法</h2>
<pre><code class="hljs language-js copyable" lang="js">element.scrollIntoView(); <span class="hljs-comment">// 等同于element.scrollIntoView(true)</span>
element.scrollIntoView(boolean); <span class="hljs-comment">// Boolean型参数,true or false</span>
element.scrollIntoView(options); <span class="hljs-comment">// Object型参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当参数为Boolean时：</p>
<ul>
<li>
<p>如果为 <code>true</code>，元素的顶端将和其所在滚动区的可视区域的顶端对齐。相应的 options: <code>&#123;block:"start",inline:"nearest"&#125;</code>。</p>
</li>
<li>
<p>如果为 <code>false</code>，元素的底端将和其所在滚动区的可视区域的底端对齐。相应的options: <code>&#123;block:"end",inline:"nearest"&#125;</code>。</p>
</li>
</ul>
<p>当参数为options对象时，属性有：</p>
<ul>
<li>
<p><code>behavior</code>：定义动画过渡效果， "auto"或 "smooth（平滑滚动）" 之一。默认为 "auto"。</p>
</li>
<li>
<p><code>block</code>：定义垂直方向的对齐， "start", "center", "end", 或 "nearest"之一。默认为 "start"。</p>
</li>
<li>
<p><code>inline</code>：定义水平方向的对齐， "start", "center", "end", 或 "nearest"之一。默认为 "nearest"。</p>
</li>
</ul>
<blockquote>
<p>PS：CSS平滑滚动方式：</p>
<pre><code class="copyable">.box &#123;
    scroll-behavior: smooth; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h2 data-id="heading-2">参考文档</h2>
<p><a href="https://www.zhangxinxu.com/wordpress/2018/10/scroll-behavior-scrollintoview-%E5%B9%B3%E6%BB%91%E6%BB%9A%E5%8A%A8/" target="_blank" rel="nofollow noopener noreferrer">www.zhangxinxu.com/wordpress/2…</a></p>
<hr>
<p>原创不易，如果觉得对你有帮助，也欢迎点赞，分享，加收藏！</p>
<p>听说点赞的人，一个月后都会升职加薪，迎娶白富美，走上人生巅峰~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd91ec2ef6d437d822e1579d01f1098~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210427113225.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            