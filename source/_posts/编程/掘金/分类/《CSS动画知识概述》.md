
---
title: '《CSS动画知识概述》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4e03b512ca14d5cb0aef31a33cdf361~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 20:13:45 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4e03b512ca14d5cb0aef31a33cdf361~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.浏览器的渲染原理</h2>
<p>首先，简单概括下浏览器渲染的步骤：</p>
<ul>
    <li>根据HTML构建HTML树。(DOM)</li>
    <li>根据CSS构建CSS树。(CSSOM)</li>
    <li>将两棵树合并成一棵渲染树。(render tree)</li>
    <li>Layout,布局。(文档流、盒模型、计算大小和位置)</li>
    <li>Paint,绘制。(绘制边框颜色、文字颜色、阴影等元素)</li>
    <li>Compose,合成。(根据层叠关系合成展示画面)</li>
</ul>
<em>如下图所示，三棵树示意图。</em>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4e03b512ca14d5cb0aef31a33cdf361~tplv-k3u1fbpfcp-watermark.image" alt="render-tree-construction.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后浏览器根据更新的样式进行渲染，达到一种“动画”的视觉效果。</p>
<p>如下所示，三种更新的方式：</p>
<ol>
<li>JS / CSS > 样式 > 布局 > 绘制 > 合成</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4731027fbe4cdb996e7e3235876d4b~tplv-k3u1fbpfcp-watermark.image" alt="frame-full.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例：<code>div.remove()</code>会触发当前消失，其他元素relayout。</p>
<ol start="2">
<li>JS / CSS > 样式 > 绘制 > 合成</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4cba8f354444fe9a084004f97258c47~tplv-k3u1fbpfcp-watermark.image" alt="frame-no-layout.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例：改变背景颜色，直接repaint > composite.</p>
<ol start="3">
<li>JS / CSS > 样式 > 合成</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f835381ea96c4157b968b1e34c5ffa57~tplv-k3u1fbpfcp-watermark.image" alt="frame-no-layout-paint.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例：改变<code>transform</code>，只需composite</p>
<p><em>在 <code>iframe</code> 查看 Paint flashing 有问题，需全屏查看。</em></p>
<p><strong>在这个分享社区<a href="https://csstriggers.com/" target="_blank" rel="nofollow noopener noreferrer">csstriggers.com/</a>，分享了每个元素在不同的浏览器内核触发什么流程的测试结果。</strong></p>
<h2 data-id="heading-1">二.CSS动画的两种做法</h2>
<ol>
<li>通过<code>transform</code>的位移<code>translate</code>、缩放 <code>scale</code>、旋转 <code>rotate</code> 和倾斜 <code>skew</code>，配合 <code>transition</code> 过渡补帧和 <code>::hover</code> 悬浮，通过鼠标触发显示动画。</li>
</ol>
<p>示例代码:<a href="http://js.jirengu.com/qufobikacu/1/edit?html,css,output" target="_blank" rel="nofollow noopener noreferrer">动画例子</a>
鼠标放在红心上变大效果动画。</p>
<ol start="2">
<li>通过 <code>transform</code> , <code>transition</code> 和 <code>animation</code> 生成自动效果动画。</li>
</ol>
<p><a href="https://gatekeeper1989.github.io/CSS-heartbeat/" target="_blank" rel="nofollow noopener noreferrer">效果动画</a> 跳动的红心。</p>
<p><a href="http://js.jirengu.com/visilucune/1/edit?html,css,output" target="_blank" rel="nofollow noopener noreferrer">示例代码</a></p>
<p><em>注：<code>inline</code> 元素不支持 <code>transform</code>,需要先变成 <code>block</code> 元素。</em></p>
<h2 data-id="heading-2">三、其他感想</h2>
<p>CSS常用的样式和属性的学习也有一周，将要告一段落。CSS复杂繁多的样式和属性，且还在不停地更新和增加，故对CSS的学习不在于死记上百条样式，而在于活用。要善于在谷歌查找MDN样式文档，不求一次细读文档即可理解，而是活用MDN文档的demo，语法和演示，不停地进行CMR，即拷贝、修改和运行，通过不停地试错，在实践中理解文档，补全文档的解释。而对于今后CSS的学习，要把其当做工具书、标准化文档看待，因CSS不正交，在层叠样式中产生的bug，解决bug的方法，应当成是一种修正方案，而不应该对其原因过多的进行深究。</p>
<h3 data-id="heading-3">参考资料</h3>
<p><a href="https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction" target="_blank" rel="nofollow noopener noreferrer">渲染树构建、布局及绘制</a><br>
<a href="https://developers.google.com/web/fundamentals/performance/rendering/" target="_blank" rel="nofollow noopener noreferrer">渲染性能</a><br>
<a href="https://developers.google.com/web/fundamentals/performance/rendering/stick-to-compositor-only-properties-and-manage-layer-count" target="_blank" rel="nofollow noopener noreferrer">使用transform来实现动画</a></p>
©right;转载声明</div>  
</div>
            