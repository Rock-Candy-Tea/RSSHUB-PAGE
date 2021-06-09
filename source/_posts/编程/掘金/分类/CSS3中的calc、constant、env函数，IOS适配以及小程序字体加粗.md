
---
title: 'CSS3中的calc、constant、env函数，IOS适配以及小程序字体加粗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3902'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 17:43:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=3902'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 9 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">CSS3中的calc、constant、env函数，IOS适配以及小程序字体加粗</h1>
<h2 data-id="heading-1">1. css3中的calc()函数</h2>
<p>最近做项目，看到别人的css中出现的，发现此函数是用于动态计算长度值。</p>
<h3 data-id="heading-2">1.1 calc()使用注意点</h3>
<ul>
<li>需要注意的是，运算符前后都需要保留一个空格，例如：width: calc(100% - 10px)；</li>
<li>任何长度值都可以使用calc()函数进行计算；</li>
<li>calc()函数支持 "+", "-", "*", "/" 运算；</li>
<li>calc()函数使用标准的数学运算优先级规则；</li>
<li>在less预编译语言中 应该这样使用 width:calc(~"100% - 10px");</li>
</ul>
<h3 data-id="heading-3">1.2 calc()含义</h3>
<p>如下代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100%</span> - <span class="hljs-number">10px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般情况下这段代码的意思是，.box元素比父级元素总是小10px;</p>
<h3 data-id="heading-4">1.3 calc()的性能问题</h3>
<p>关于这个我查了一下在，前端这块避免使用calc（）表达式，因为它的重绘次数非常多，相当的影响性能。</p>
<h2 data-id="heading-5">2. canstant和env函数</h2>
<p>env() CSS 函数以类似于 var 函数和 custom properties 的方式将用户代理定义的环境变量值插入你的 CSS 中。区别在于，环境变量除了由用户代理定义而不是由用户定义外，还被全局作用在文档中，而自定义属性则限定在声明它们的元素中。</p>
<p>为了告诉浏览器使用屏幕上所有的可用空间，并以此使用env()变量，我们需要添加一个新的视口元值：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width,initial-scale=1,viewport-fit=cover"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.1基本使用</h3>
<p>env(< 自带值 > , < 回退值 >)</p>
<pre><code class="hljs language-css copyable" lang="css">env(safe-area-inset-<span class="hljs-attribute">top</span>);
env(safe-area-inset-<span class="hljs-attribute">right</span>);
env(safe-area-inset-<span class="hljs-attribute">bottom</span>);
env(safe-area-inset-<span class="hljs-attribute">left</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中回退值不是必须的，作用是当自带值不生效，就以回退值为准；
canstant（）函数也是类似</p>
<h2 data-id="heading-7">3.ios的适配问题</h2>
<h3 data-id="heading-8">3.1 ios中的安全距离问题</h3>
<p>综上2，其实constant和env函数是ios为了解决自身安全距离问题而生的
基本上使用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">padding-bottom</span>: <span class="hljs-built_in">constant</span>(safe-area-inset-bottom);
<span class="hljs-attribute">padding-bottom</span>: <span class="hljs-built_in">env</span>(safe-area-inset-bottom);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就能解决ios底部安全距离问题
如果是在小程序中就不必增加新的视口元值
如果是在H5中就得新增视口元值，其中viewport-fit=cover，其中viewport有三个可选值:</p>
<ul>
<li>auto:此值不影响初始布局视图端口，并且整个web页面都是可查看的。</li>
<li>contain:视图端口按比例缩放，以适合显示内嵌的最大矩形。</li>
<li>cover:视图端口被缩放以填充设备显示。强烈建议使用 safe area inset 变量，以确保重要内容不会出现在显示之外。</li>
</ul>
<h3 data-id="heading-9">3.2 ios中input按钮去掉自带的渐变效果</h3>
<p>解决：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">input</span>&#123;
<span class="hljs-attribute">outline</span>:<span class="hljs-number">0px</span>; 
-webkit-appearance:none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4. 微信小程序中字体加粗</h2>
<p>做过项目的小伙伴不知道发现没有，在小程序中font-weight:block；等不生效，虽然开发工具上是生效的，但是手机上显示依然还是没有加粗；</p>
<p>解决：</p>
<pre><code class="hljs language-css copyable" lang="css">//安卓解决方案
<span class="hljs-attribute">font-weight</span>: <span class="hljs-number">400</span>;
-webkit-text-stroke: <span class="hljs-number">0.02em</span>;
//ios解决方案
<span class="hljs-attribute">font-family</span>: PingFang-Midum;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            