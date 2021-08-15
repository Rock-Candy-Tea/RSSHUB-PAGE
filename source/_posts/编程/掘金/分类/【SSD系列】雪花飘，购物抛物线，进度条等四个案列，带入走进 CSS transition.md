
---
title: '【SSD系列】雪花飘，购物抛物线，进度条等四个案列，带入走进 CSS transition'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af390fc619a4f1f8758a437d03e37c4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 17:42:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af390fc619a4f1f8758a437d03e37c4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于关于<a href="https://juejin.cn/column/6991252706941730852" target="_blank" title="https://juejin.cn/column/6991252706941730852">【SSD系列】</a>：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>今天从四个案例，我们一起走进 CSS Transition。</p>
<h2 data-id="heading-1">源码 以及 在线演示地址</h2>
<p>源码地址： <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2Fdocs%2FcssTransition%2Fcss%2Ftransition" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/docs/cssTransition/css/transition" ref="nofollow noopener noreferrer">四个案例， CSS Transition 源码</a></strong></p>
<p>在线演示地址：(<strong>兼容移动端</strong>)</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Ftiming-fun.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/timing-fun.html" ref="nofollow noopener noreferrer">贝塞尔曲线运动</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fprogress.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/progress.html" ref="nofollow noopener noreferrer">进度条</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fsnow.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/snow.html" ref="nofollow noopener noreferrer">雪花飘飘效果</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fprod.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/prod.html" ref="nofollow noopener noreferrer">购物车抛物线效果</a></li>
</ul>
<h2 data-id="heading-2">案例演示</h2>
<h3 data-id="heading-3">内置贝塞尔函数运动效果</h3>
<p>效果有：</p>
<ul>
<li>ease</li>
<li>linear</li>
<li>easy-in</li>
<li>easy-out</li>
<li>easy-in-out</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Ftiming-fun.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/timing-fun.html" ref="nofollow noopener noreferrer">贝塞尔曲线运动-演示地址</a><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af390fc619a4f1f8758a437d03e37c4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">进度条</h3>
<p>思路</p>
<ul>
<li>两个div, 一个outer, 一个inner</li>
<li>box-shadow</li>
<li>transition</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fprogress.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/progress.html" ref="nofollow noopener noreferrer">进度条-演示地址</a><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f184a8b807424f87852b5023d5d80696~tplv-k3u1fbpfcp-watermark.image" alt="进度条" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">雪花飘飘</h3>
<p>思路：</p>
<ul>
<li>n个postion为absolute的HTML节点</li>
<li>transition 随机贝塞尔曲线和动画时间</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fsnow.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/snow.html" ref="nofollow noopener noreferrer">雪花飘飘效果</a><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43797ffad934441abbdd7d2aa2b436a5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">购物车抛物线</h3>
<p>思路：
top和left的属性一个用linear，一个easy-in 贝塞尔时间函数</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FjuejinBlogsCodes%2FcssTransition%2Fcss%2Ftransition%2Fprod.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/juejinBlogsCodes/cssTransition/css/transition/prod.html" ref="nofollow noopener noreferrer">购物车抛物线效果</a><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f097d83e490a4d1cb6e2cdb4689a3dbc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">Transition属性：</h2>
<p>那我们就先说说transition的属性</p>



































<table><thead><tr><th>属性</th><th>描述</th><th>CSS</th></tr></thead><tbody><tr><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transition.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/cssref/pr_transition.asp" ref="nofollow noopener noreferrer">transition</a></td><td>简写属性，用于在一个属性中设置四个过渡属性。</td><td>3</td></tr><tr><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transition-property.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/cssref/pr_transition-property.asp" ref="nofollow noopener noreferrer">transition-property</a></td><td>规定应用过渡的 CSS 属性的名称。默认值all。</td><td>3</td></tr><tr><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transition-duration.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/cssref/pr_transition-duration.asp" ref="nofollow noopener noreferrer">transition-duration</a></td><td>定义过渡效果花费的时间。默认是 0。</td><td>3</td></tr><tr><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transition-timing-function.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/cssref/pr_transition-timing-function.asp" ref="nofollow noopener noreferrer">transition-timing-function</a></td><td>规定过渡效果的时间曲线。默认是 ease。</td><td>3</td></tr><tr><td><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transition-delay.asp" target="_blank" rel="nofollow noopener noreferrer" title="http://www.w3school.com.cn/cssref/pr_transition-delay.asp" ref="nofollow noopener noreferrer">transition-delay</a></td><td>规定过渡效果何时开始。默认是 0</td><td>3</td></tr></tbody></table>
<p>额外提一下两个属性：</p>
<ul>
<li>transition-property</li>
</ul>
<p>all: 所有属性， none: 也就是不生效。<br>
当然也不是所有的属性都可以来动效， 具体的参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FCSS_animated_properties" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties" ref="nofollow noopener noreferrer">Certain CSS properties can be animated </a><br>
<strong>不支持的动画属性：background-image,  float,  display,  position,visibility。</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fxiaohuochai%2Fp%2F5347930.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/xiaohuochai/p/5347930.html" ref="nofollow noopener noreferrer">深入理解CSS过渡transition</a>有一个简单分类的总结，当然相对全面还是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FCSS_animated_properties" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties" ref="nofollow noopener noreferrer">Certain CSS properties can be animated </a></p>
<pre><code class="copyable">颜色: color background-color border-color outline-color
位置: backround-position left right top bottom
长度: 
    [1]max-height min-height max-width min-width height width
    [2]border-width margin padding outline-width outline-offset
    [3]font-size line-height text-indent vertical-align  
    [4]border-spacing letter-spacing word-spacing
数字: opacity visibility z-index font-weight zoom
组合: text-shadow transform box-shadow clip
其他: gradient
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>transition-timing-function<br>
三阶贝塞尔曲线函数， 这里只要两个控制点的值。<br>
至于什么是贝塞尔曲线，可以看看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fyjbjingcha%2Fp%2F7350264.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/yjbjingcha/p/7350264.html" ref="nofollow noopener noreferrer">贝塞尔曲线扫盲</a>。<br>
内置了几个简单的：</p>
<p>1、ease：逐渐变慢, 贝塞尔曲线(0.25, 0.1, 0.25, 1.0)<br>
2、linear：匀速，linear 贝塞尔曲线(0.0, 0.0, 1.0, 1.0)<br>
3、ease-in：加速，ease-in 贝塞尔曲线(0.42, 0, 1.0, 1.0)<br>
4、ease-out：减速，ease-out贝塞尔曲线(0, 0, 0.58, 1.0)<br>
5、ease-in-out：加速然后减，ease-in-out 贝塞尔曲线(0.42, 0, 0.58, 1.0)</p>
<p>更多的可以在这里获得<a href="https://link.juejin.cn/?target=http%3A%2F%2Fyisibl.github.io%2Fcubic-bezier%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://yisibl.github.io/cubic-bezier/" ref="nofollow noopener noreferrer">在线贝塞尔</a>。</p>
<p>这里的取值还有一种steps函数，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fxiaohuochai%2Fp%2F5347930.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/xiaohuochai/p/5347930.html" ref="nofollow noopener noreferrer">深入理解CSS过渡transition</a></p>
</li>
</ul>
<hr>
<h3 data-id="heading-8"><strong>多值：多种属性同时变化的时候</strong></h3>
<p>依旧是两个总写法。 <strong>注意transition-property和其他属性数量不一致的情况。</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 方法一*/</span>
<span class="hljs-selector-class">.demo</span>&#123;
    <span class="hljs-attribute">transition-property</span>: width, height;
    <span class="hljs-attribute">transition-delay</span>: <span class="hljs-number">500ms</span>;
    <span class="hljs-attribute">transition-timing-function</span>: linear;
    <span class="hljs-attribute">transition-duration</span>: <span class="hljs-number">2000ms</span>;
&#125;
<span class="hljs-comment">/* 方法二*/</span>
<span class="hljs-selector-class">.demo</span>&#123;
  <span class="hljs-attribute">transition</span>: width <span class="hljs-number">2000ms</span> linear <span class="hljs-number">500ms</span>, height <span class="hljs-number">2000ms</span> linear <span class="hljs-number">500ms</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">触发方式</h3>
<ul>
<li>伪类触发</li>
</ul>
<p>:hover、:focus、:active等</p>
<ul>
<li>媒体查询触发</li>
</ul>
<p>@media</p>
<ul>
<li>javascript触发</li>
</ul>
<h2 data-id="heading-10">Transition事件</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement%2Ftransitioncancel_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/transitioncancel_event" ref="nofollow noopener noreferrer">transitioncancel</a><br>
转换取消事件 ， 该事件和transitionend互斥，只会有一个发生。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement%2Ftransitionend_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/transitionend_event" ref="nofollow noopener noreferrer">transitionend</a><br>
转换结束事件</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement%2Ftransitionrun_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/transitionrun_event" ref="nofollow noopener noreferrer">transitionrun</a><br>
转换进行事件</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLElement%2Ftransitionstart_event" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/transitionstart_event" ref="nofollow noopener noreferrer">transitionstart</a><br>
转换开始事件，<strong>因为转换有delay属性，所以进行，不一定真正的开始。</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> transition = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.transition'</span>);

transition.addEventListener(<span class="hljs-string">'transitioncancel'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Transition canceled'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Transition事件的触发次数是非复合的过渡属性的个数, 比如width, height同时变换，那么就是两次。<br>
还比较有趣的事， 比如hover到某元素的时候，开始变换，没变换结束，你就离开。
变换效果会倒着来。上面的demo，就会看到。</p>
<p>基本了解了属性和事件，基本就是进一步的应用了， 可以自行下载源码看看， 思想有多风骚，作用就有多大。</p>
<h2 data-id="heading-11">写在最后</h2>
<p>不忘初衷，【SSD系列】，3-5分钟，500-1000字，有所得，而不为所累，如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 dirge-cloud，一起学习。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fcss-transitions-1%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/css-transitions-1/" ref="nofollow noopener noreferrer">CSS Transitions</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FCSS_Transitions%2FUsing_CSS_transitions" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions" ref="nofollow noopener noreferrer">Using CSS transitions</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTransitionEvent" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent" ref="nofollow noopener noreferrer">TransitionEventSection</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%23feat%3Dcss-transitions" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/#feat=css-transitions" ref="nofollow noopener noreferrer">css-transitions | Can I Use</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fxiaohuochai%2Fp%2F5347930.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/xiaohuochai/p/5347930.html" ref="nofollow noopener noreferrer">深入理解CSS过渡transition</a></p>
</blockquote></div>  
</div>
            