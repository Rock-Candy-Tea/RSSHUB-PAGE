
---
title: '探究下commonJs中require实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 04:51:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">疑问：</h1>
<p>这里提出几个问题，大家可以带着问题来看下面的分析，这样有助于理解：</p>
<ul>
<li>
<ol>
<li>esmodule 以及require有什么不同</li>
</ol>
</li>
<li>
<ol start="2">
<li>exports 和 module.exports有什么区别</li>
</ol>
</li>
<li>
<ol start="3">
<li>commonJs中this指的什么</li>
</ol>
</li>
</ul>
<h1 data-id="heading-1">源码断点</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfa11c4f12d1467da69728ae11a315e0~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer">
上面是我源码的断点过程，也许大家看了后很懵，我来给大家简单说下执行流程：</p>
<h1 data-id="heading-2">源码执行流程</h1>
<ul>
<li>
<ol>
<li>require方法 =》 Module.prototype.require方法</li>
</ol>
</li>
<li>
<ol start="2">
<li>Module._load方法记载</li>
</ol>
</li>
<li>
<ol start="3">
<li>Module._resolveFileName 方法就是把路径变成了绝对路径 进行尝试添加后缀 &#123;.js, .json&#125;</li>
</ol>
</li>
<li>
<ol start="4">
<li>new Module 拿到一个绝对路径创建一个模块</li>
</ol>
</li>
<li>
<ol start="5">
<li>使用module.load 加载模块</li>
</ol>
</li>
<li>
<ol start="6">
<li>根据文件后缀Module._extensions['.js']去进行策略模式加载</li>
</ol>
</li>
<li>
<ol start="7">
<li>进行同步代码的读取</li>
</ol>
</li>
<li>
<ol start="8">
<li>增加一个函数壳子，并且让函数执行，让module.exports作为this</li>
</ol>
</li>
<li>
<ol start="9">
<li>用户会默认拿到module.exports结果</li>
</ol>
</li>
</ul>
<h1 data-id="heading-3">手写实现，结果分析：</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68185f0c58c5410485f0a50c6a5e1d85~tplv-k3u1fbpfcp-watermark.image" alt="require手写实现.png" loading="lazy" referrerpolicy="no-referrer">
这个就是node require的手写实现，所有的代码都已经截图了。说下重点代码：</p>
<ul>
<li>
<ol>
<li>其实我们文件中的module.exports 其实就是源码中的方法Module的一个实现&#123;const module = new Module&#125;，方法中包含着属性exports</li>
</ol>
</li>
<li>
<ol start="2">
<li>exports 其实就是实例的一个属性，会将结果保存到这里</li>
</ol>
</li>
<li>
<ol start="3">
<li>在用函数包裹的过程中，其实是使用call进行this强绑定的</li>
</ol>
</li>
</ul>
<h1 data-id="heading-4">疑问解答：</h1>
<ul>
<li>
<ol>
<li>其实require的实现原理就是通过读取文件内容，如果解析文件是js，最后通过包裹函数来实现调用。但是esmodule其实通过发送get请求，来请求文件内容。所以他们都是基于大环境的。</li>
</ol>
</li>
<li>
<ol start="2">
<li>其实module.exports 以及exports其实都是指的一个内容，内存引用指向一个值</li>
</ol>
</li>
<li>
<ol start="3">
<li>在执行js的时候，我们通过call来进行强绑定this的，所以其实this就是exports。我们可以在node中运行下 this === exports === module.exports 都是相等的</li>
</ol>
</li>
</ul>
<h1 data-id="heading-5">结尾</h1>
<p>好了，这下终于明白require实现原理了，同时也知道module.exports 以及exports都是干什么的了。恭喜各位了。记得点赞啊</p></div>  
</div>
            