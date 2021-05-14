
---
title: 'chrome浏览器渲染进程工作流程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3890fbc76a12489ea6dace932b8a148d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 02:17:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3890fbc76a12489ea6dace932b8a148d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.浏览器架构</h2>
<p>学习浏览器的工作原理首先要了解浏览器的架构设计，通过浏览器<strong>多进程架构</strong>的学习，可以更好的理解浏览器的网络流程、页面渲染过程、js流程、以及web安全等等，从而可以从更好维度理解web应用</p>
<h3 data-id="heading-1">1.首先要了解进程和线程的概念</h3>
<ol>
<li><strong>进程: 当我们启动一个应用的时候，计算机会开启一个进程，会给应用分配一块内存，你可以在这块内存中开发你的应用，我们可以将这块内存看做一个”工厂”，一个进程还可以向操作系统申请开启另一个进程，两个进程可以用IPC（inter Process Communication）进行通信</strong></li>
<li><strong>线程：就像是工厂里的员工，每一个员工都做自己的事，也可以互相配合工作，由工厂统一调配</strong></li>
</ol>
<h3 data-id="heading-2">2.chrome浏览器多进程架构模式</h3>
<p>其中浏览器主进程协调其他进程，包括GPU进程，渲染进程，插件进程等,我们打开浏览器的任务管理器可以看到每个进程</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3890fbc76a12489ea6dace932b8a148d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3.主要的几个进程以及每个进程的职责</h3>
<ol>
<li>
<p>Browser Process 浏览器主进程<br>
a: 负责地址栏，书签栏，刷新前进后退操作等界面交互，用户交互<br>
b: 子进程管理</p>
</li>
<li>
<p>Render Process 渲染进程<br>
a: 我理解一个Tab页就是一个渲染进程，也是我们接下来主要讨论的进程，主要负责页面呈现，将HTML、CSS、JS转换为用户看到的网页，排版引擎是Blink,js引擎是V8</p>
</li>
<li>
<p>Plugin Process 插件进程<br>
a: 负责控制页面的所有插件，flash,chrome Extensinon等</p>
</li>
<li>
<p>GPU Process<br>
a: 负责3D CSS效果，UI界面绘制</p>
</li>
<li>
<p>NetWork Process 网络进程<br>
a: 加载页面网络资源</p>
</li>
</ol>
<h3 data-id="heading-4">4.chrome多进程架构的优缺点</h3>
<p>优点：</p>
<ul>
<li>稳定：由于进程之间是隔离的，当一个页面或者插件崩溃，只影响当前的页面或者插件，不影响其他的页面，关闭崩溃的页面或者插件时候，会将内存回收</li>
<li>安全：渲染进程和插件进程支持安全沙箱，可以理解为操作系统给进程上了一把锁，沙箱里面的程序可以运行，但是不能读取硬盘上的数据，也不能读取敏感位置数据，这样恶意程序就不能获取到系统权限</li>
</ul>
<p>缺点：</p>
<ul>
<li>更高的占用资源，每个渲染进程都包含多个线程，这就意味着会消耗更多的内存资源</li>
</ul>
<h2 data-id="heading-5">2.渲染进程如何工作</h2>
<h3 data-id="heading-6">1.渲染进程包含的线程</h3>
<p>Renderer Process 渲染进程，一个浏览器的Tab就是一个渲染进程，将html,css,js转化为web页面，渲染进程包含多个线程</p>
<ol>
<li><strong>GUI渲染线程</strong>：负责渲染浏览器界面，解析html,css,DOM Tree, render Tree ，layout,绘制等</li>
<li><strong>js引擎线程</strong>：解析js脚本，运行代码</li>
<li><strong>事件触发线程</strong>：用于控制事件轮询，鼠标点击，AJAX异步请求等，对应任务会被添加到事件触发线程中，符合触发条件时，事件会被添加到任务队列等待JS引擎处理</li>
<li><strong>定时器触发线程</strong>：定时器setInterval 和 setTimeout</li>
<li><strong>http请求线程</strong>：用于http请求</li>
</ol>
<h3 data-id="heading-7">2.GUI线程渲染流程</h3>
<ul>
<li>
<p>1.构建DOM Tree <br>
当渲染开始时，渲染进程的<strong>主线程</strong>开始解析HTML,当遇到图片，CSS ,JS等资源，主进程会在构建DOM过程中请求这些资源，为了加速资源请求，preload scanner会扫描html中如果有img,link等标签时候，会把请求传递给Browser process中的network 线程进行资源下载，<br>
当遇到script时候，渲染线程主线程会停止解析HTML，去加载，解析，执行JS代码</p>
</li>
<li>
<p>2.样式计算<br>
主进程同时会解析CSS文本，最终给每一个节点计算出最终的样式值</p>
</li>
<li>
<p>3.布局<br>
通过遍历DOM以及元素的计算样式，主线程会构建出包含每个元素坐标信息及盒子大小的布局树Render Tree, 与DOM Tree 不同的是 Render Tree 只包含可见的元素，head及下面的全部标签和设置display的元素都不会出现在布局树中</p>
</li>
<li>
<p>4.分层<br>
页面中有很多复杂的效果，3D变换，页面滚动，定位元素，z-index进行z轴排序等，主线程为<strong>特定的节点生成专用的图层，并生成一颗对应的图层树（LayerTree）</strong>,浏览器中可以直观看到图层，打开开发者工具，选择Layers，就可以看到页面的分层情况了<br>
什么情况下元素会分层呢？<br>
<strong>拥有层叠上下文属性的元素会单独一层</strong><br>
position: fixed<br>
z-index: 2<br>
filter: blue(5px)<br>
opacity: 0.5<br>
**需要剪裁的地方也会被创建为图层<br>
**当文字内容超过容器高度就会产生剪裁或者出现滚动条</p>
</li>
<li>
<p>5.图层绘制<br>
图层构建完成后会对每个图层进程绘制，把图层绘制拆分成很多的小的指令，按照指令顺序生成绘制列表，绘制列表是用来记录绘制顺序和绘制指令的</p>
</li>
<li>
<p>6.栅格化<br>
绘制操作是由合成线程来完成的，当绘制列表完成主线程会把绘制列表提交到<strong>合成线程</strong>，<br>
合成线程将图层分为图块（tile）,合成线程会按照视口（viewport）,也就是用户可以看到的区域优先来生成位图，所以**栅格化就是将图块生成位图，图块是栅格化的最小单位，**通常栅格化会使用GPU加速,并存储在GPU内存中</p>
</li>
<li>
<p>7.显示<br>
图块都被光栅化了之后合成线程就会通知浏览器进程将内容会知道屏幕上</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/009d7446c0204fda82b0d0684a21dcb8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-8"></h3>
<h2 data-id="heading-9">5.问题</h2>
<ol>
<li>
<p><strong>渲染过程遇到JS文件怎么处理？</strong><br>
答：html代码从上到下读取js的加载，解析和执行会阻塞DOM的构建，当构建DOM时，如果遇到了js代码，会暂停构建DOM，将控制权交给js引擎，等js运行完毕，再从中断的地方恢复DOM构建<br>
当然js也会阻塞CSSOM的构建，因为js可以修改样式规则，所以在执行js时候必须拿到完整的CSSOM，所以直到CSSOM下载并构建完成之后才会去执行js，然后再构建DOM</p>
</li>
<li>
<p><strong>async 和 defer 区别</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08eb4f03798c4704b1396e77987c642f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
a: <strong>没有加async和defer,</strong> 遇到script标签会暂停解析HTML然后加载js并执行，执行js之后会继续解析HTML<br>
b: <strong>当标签中添加async</strong> ,可以理解为异步，遇到script标签时候，加载js的时候不影响HTML解析，但是当加载完js解析时候会暂停HTML,直到js执行完毕才会接着解析HTML<br>
c: **当标签中有defer，**我理解就是延迟执行，加载js不影响HTML解析，当DOM解析完成，DOMContentLoaded前执行</p>
</li>
<li>
<p><strong>元素的哪些变化会引起回流和重绘</strong><br>
<strong>重排（回流）</strong>：当render tree中的一部分(或全部)因为元素的规模尺寸，布局，隐藏等改变而需要重新构建<br>
1. 任何改变元素位置和尺寸大小的操作<br>
2. 添加或者删除可见的DOM元素<br>
3. 浏览器窗口尺寸变化-resize<br>
4. 计算offsetWidth 和 offsetHeight属性<br>
<strong>重绘</strong>：当render tree中的一些元素需要更新属性，而这些属性只是影响元素的外观，风格，而不会影响布局的，比如background-color。<br>
color,background等不引起元素位置变化的属性</p>
</li>
<li>
<p>**如何减少重排和重绘<br>
**a: 合并多次对样式的修改，一次处理掉，**可以一次使用cssText或者改变class名方式<br>
**b: 多次操作DOM元素时候，让元素脱离文档流，操作DOM,然后再将元素恢复到文档流中，**比如隐藏元素，修改，显示元素 最多两次重排；<br>
**c: 当访问一些元素的属性（比如offsetWidth等）时候，浏览器会强制清空队列，进行重排，所以用到这种属性的时候可以适当做缓存<br>
d: 使用GPU加速，<strong>可以让transform、opacity、filters、Will-change这些不会引起回流重排重绘</strong></p>
</li>
</ol></div>  
</div>
            