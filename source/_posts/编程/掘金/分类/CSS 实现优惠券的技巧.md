
---
title: 'CSS 实现优惠券的技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f729c401c34192b314771cd610b603~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 02:48:10 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f729c401c34192b314771cd610b603~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="企业微信截图_119053c6-c109-4f59-b201-b640f5ac0921.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f729c401c34192b314771cd610b603~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>本文作者：严文彬</p>
</blockquote>
<blockquote>
<p>原创声明：本文为阅文前端团队 YFE 成员出品，请尊重原创，转载请联系公众号 (id: yuewen_YFE) 获取授权，并注明作者、出处和链接。</p>
</blockquote>
<p>在实际 Web 开发过程中，总会遇到各种各样的布局。有公司同事问我这样一种布局有没有什么好的实现方式，就是一种在活动充值页非常普遍的优惠券效果，如下</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0c1da3302004cd0a7205eb9efd94839~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>还有这样的</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b272ec7e03aa4692b92cca94fd31e84a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>考虑到各种可能出现的场景，抽象出以下几种案例，一起来看看实现吧</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d740ae184484a968bbb00ed6f5ef21b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、最佳实现方式</h2>
<p>首先，碰到这类布局的最佳实现肯定是<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/mask?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">mask遮罩</a>。关于遮罩，可以看一下<a href="https://jelly.jd.com/article/6006b1045b6c6a01506c87bb?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">CSS3 Mask 安利报告</a>。这里简单介绍一下</p>
<p>基本语法很简单，和<strong>background</strong>的语法基本一致</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-string">'遮罩图片'</span> ;
&#125;
<span class="hljs-comment">/*完整语法*/</span>
<span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-string">'遮罩图片'</span> [position] / [size] ;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的遮罩图片和背景的使用方式基本一致，可以是<strong>PNG图片</strong>、<strong>SVG图片</strong>、也可以是<strong>渐变绘制</strong>的图片，同时也支持<strong>多图片叠加</strong>。</p>
<p>遮罩的原理很简单，<strong>最终效果只显示不透明的部分，透明部分将不可见，半透明类推</strong></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e5bb8ccbded457e985db7ad1d564c59~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>事实上，除了根据透明度（Alpha）来作为遮罩条件，还可以通过亮度（luminance）来决定，比如白色表示隐藏，黑色表示可见。不过目前只有 Firefox 支持</p>
</blockquote>
<p>所以，只要能绘制以上各种形状，就可以实现了。</p>
<h2 data-id="heading-1">二、内凹圆角</h2>
<p>优惠券大多有一个很明显的特点，就是<strong>内凹圆角</strong>。提到圆角，很容易想到<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/radial-gradient()?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">radial-gradient</a>。这个语法有点复杂，记不住没关系，可以看看张老师的这篇<a href="https://www.zhangxinxu.com/wordpress/2017/11/css3-radial-gradient-syntax-example/?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">10个demo示例学会CSS3 radial-gradient径向渐变</a>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at left center, transparent <span class="hljs-number">20px</span>, red <span class="hljs-number">20px</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b15a32f51134672bd5ed4e829f6816c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样就绘制了一个半径为 20px 的透明的圆，不过代码层面还有很多优化的空间。</p>
<ol>
<li>在实现边界分明的渐变时，后面颜色的位置只需要小于等于前面颜色的位置就行了，比如<strong>0</strong></li>
<li>透明颜色可以用<strong>16进制</strong>缩写比如**#0000<strong>来代替</strong>，<strong>不透明的部分随便用一个颜色就好，我喜欢用</strong>red**，主要是这个单词比较短</li>
<li>还有渐变的位置默认是居中的，所以第二个center可以去除，left 可以用<strong>0</strong>来表示</li>
</ol>
<p>进一步简化就得到了</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不错，又少了好几个B的流量~ 可以查看在线实例<a href="https://codepen.io/xboxyan/pen/BaQXQXB?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现1</a></p>
<h2 data-id="heading-2">三、优惠券效果</h2>
<p>上面是一个最基本的内凹圆角效果，现在来实现下面几种布局，比如两个半圆的，根据上面的例子，再复制一个圆不就可以了？改一下定位的方向</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at right, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3469ba7ab1b94e46852fbd6ce74c2164~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这时发现一个圆都没有了。原因其实很简单，如下演示，<strong>两层背景相互叠加，导致整块背景都成了不透明的</strong>，所以 mask 效果表现为全部可见。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1759b6a6937f4f1cb277ecb1d266e944~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>解决方式有2个，分别是：</p>
<ol>
<li><strong>把两个凹角的地方错开，这里可以通过修改尺寸和位置，同时还需要禁止平铺</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
-webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at right, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>);
-webkit-<span class="hljs-attribute">mask</span>-size: <span class="hljs-number">51%</span>; <span class="hljs-comment">/*避免出现缝隙*/</span>
-webkit-<span class="hljs-attribute">mask</span>-<span class="hljs-attribute">position</span>: <span class="hljs-number">0</span>, <span class="hljs-number">100%</span>; <span class="hljs-comment">/*一个居左一个居右*/</span>
-webkit-<span class="hljs-attribute">mask</span>-repeat: no-repeat;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2820f5e92a4243f785ded5c052c89abb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>动态演示如下，这样就不会互相覆盖了</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18d270df14ae4577946083bad3106c6c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/WNoVjmb?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现2</a></p>
<ol start="2">
<li><strong>使用遮罩合成</strong><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/mask-composite?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">mask-composite</a><strong>，这个可能不太熟悉，简单介绍一下</strong></li>
</ol>
<p>标准属性下<strong>mask-composite</strong>有 4 个属性值（Firefox支持）</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* Keyword values */</span>
<span class="hljs-attribute">mask</span>-composite: add; <span class="hljs-comment">/* 叠加（默认） */</span>
<span class="hljs-attribute">mask</span>-composite: subtract; <span class="hljs-comment">/* 减去，排除掉上层的区域 */</span>
<span class="hljs-attribute">mask</span>-composite: intersect; <span class="hljs-comment">/* 相交，只显示重合的地方 */</span>
<span class="hljs-attribute">mask</span>-composite: exclude; <span class="hljs-comment">/* 排除，只显示不重合的地方 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个可能有些不好理解，其实可以参考一些图形软件的形状合成操作，比如 photoshop</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24631564d6547d8bb62637cdc59ea7d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-mask-composite?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">-webkit-mask-composite</a>与标准下的值有所不同，属性值非常多，看下面</p>
<pre><code class="hljs language-css copyable" lang="css">-webkit-<span class="hljs-attribute">mask</span>-composite: clear; <span class="hljs-comment">/*清除，不显示任何遮罩*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: copy; <span class="hljs-comment">/*只显示上方遮罩，不显示下方遮罩*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: source-over; 
-webkit-<span class="hljs-attribute">mask</span>-composite: source-in; <span class="hljs-comment">/*只显示重合的地方*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: source-out; <span class="hljs-comment">/*只显示上方遮罩，重合的地方不显示*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: source-atop;
-webkit-<span class="hljs-attribute">mask</span>-composite: destination-over;
-webkit-<span class="hljs-attribute">mask</span>-composite: destination-in; <span class="hljs-comment">/*只显示重合的地方*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: destination-out;<span class="hljs-comment">/*只显示下方遮罩，重合的地方不显示*/</span>
-webkit-<span class="hljs-attribute">mask</span>-composite: destination-atop;
-webkit-<span class="hljs-attribute">mask</span>-composite: xor; <span class="hljs-comment">/*只显示不重合的地方*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是一下就懵了？不用慌，可以看到上面有几个值是<strong>source-</strong>*，还有几个是**destination-***开头的，<strong>source 代表新内容</strong>，也就是上面绘制的图层，<strong>destination 代表元内容</strong>，也就是下面绘制的图层（<strong>在CSS中，前面的图层会覆盖后面的图层</strong>），这里的属性值其实是借用了Canvas 中的概念，具体可以查看<a href="https://www.canvasapi.cn/CanvasRenderingContext2D/globalCompositeOperation?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">CanvasRenderingContext2D.globalComposite</a></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6294063c5a64e5889714e72f687cf9c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>记不住没关系，实际开发可以逐一试验[\捂脸]。具体差异可以查看<a href="https://codepen.io/xboxyan/pen/RwKbGwN?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen -webkit-mask-composite 属性值演示</a></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f2657a9169441fb5f870e8e59fb8ff~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>了解这个属性后，上面的叠加问题就很简单了，设置<strong>只显示重合的地方</strong>就行了</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at right, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
  -webkit-<span class="hljs-attribute">mask</span>-composite: source-in | destination-in ; <span class="hljs-comment">/*chrome*/</span>
  <span class="hljs-attribute">mask</span>-composite: intersect; <span class="hljs-comment">/*Firefox*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba7a41090aea4deb8695eec37c96fb06~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>动态演示如下，这样只会显示<strong>互相重合的地方</strong></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/745518f635964f339387cb59391f868c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/rNWXmbm?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现3</a></p>
<p>2个圆角的实现了，4个的就很容易了，画4个圆就行，同样利用遮罩合成可以轻易实现</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span> <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at right <span class="hljs-number">0</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">0</span> <span class="hljs-number">100%</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>), <span class="hljs-built_in">radial-gradient</span>(circle at right <span class="hljs-number">100%</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); <span class="hljs-comment">/*4个角落各放一个圆*/</span>
  -webkit-<span class="hljs-attribute">mask</span>-composite: source-in | destination-in ; <span class="hljs-comment">/*chrome*/</span>
  <span class="hljs-attribute">mask</span>-composite: intersect; <span class="hljs-comment">/*Firefox*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b1a85cc170f4dfa8fd01f42d4af9367~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/jOVgwOq?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现4</a></p>
<h2 data-id="heading-3">四、优惠券平铺效果</h2>
<p>上面的例子展示了2个圆角和4个圆角的效果，分别绘制了2个和4个圆，其实这是可以通过平铺来实现的，只需要一个圆就可以。实现步骤如下</p>
<ol>
<li><strong>画一个左中的靠边的透明圆</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4df9811251c9485fa25273de0bad3292~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><strong>向左平移自身的一半</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
  -webkit-<span class="hljs-attribute">mask</span>-<span class="hljs-attribute">position</span>: -<span class="hljs-number">20px</span>
&#125;
<span class="hljs-comment">/*也可以缩写为*/</span>
<span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/629259f3b8ca4eacbd56785de787909e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>效果就出来了，是不是很神奇？其实就是利用到了默认的<strong>repeat特性</strong>，这里用一张动图就能明白了</p>
<blockquote>
<p>下面<strong>红色边框内表示视区范围</strong>，也就是最终的效果，这里为了演示，把视线之外的<strong>平铺</strong>做了半透明处理，移动表示 position 改变的过程</p>
</blockquote>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b53ef019d3804b71a66a4488ee39c066~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/MWbNozQ?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现5</a></p>
<p>同样原理，4个圆角也可以采用这种方式实现</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
  -webkit-<span class="hljs-attribute">mask</span>-<span class="hljs-attribute">position</span>: -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span>;
&#125;
<span class="hljs-comment">/*也可以缩写为*/</span>
<span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee1376b457844f9390a2d6f1c45ea416~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实现原理演示如下</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05e41d4d58dd4b9bb1b11af9a1c99e0b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/mdONMwR?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现6</a></p>
<p>6个圆角就需要改一下平铺尺寸了。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>); 
  -webkit-<span class="hljs-attribute">mask</span>-<span class="hljs-attribute">position</span>: -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span>;
  -webkit-<span class="hljs-attribute">mask</span>-size: <span class="hljs-number">50%</span>;
&#125;
<span class="hljs-comment">/*也可以缩写为*/</span>
<span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span> / <span class="hljs-number">50%</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0990fa22ba4741399525680ce66acc68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实现原理演示如下</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5745f206eadb4b1ab14e233777c36e2b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/PobMKyE?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现7</a></p>
<p>如果继续缩小背景图的尺寸，还可以得到最后的效果</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">10px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">10px</span>, red <span class="hljs-number">0</span>); 
  -webkit-<span class="hljs-attribute">mask</span>-<span class="hljs-attribute">position</span>: -<span class="hljs-number">10px</span>;
  -webkit-<span class="hljs-attribute">mask</span>-size: <span class="hljs-number">100%</span> <span class="hljs-number">30px</span>;
&#125;
<span class="hljs-comment">/*也可以缩写为*/</span>
<span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">10px</span> / <span class="hljs-number">100%</span> <span class="hljs-number">30px</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761e37382176444a8d0b7e715439f386~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实现原理演示如下，其实就平铺</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05f720725e71437ea81899c6cb294b1f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/zYogbQJ?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现8</a></p>
<h2 data-id="heading-4">五、反向镂空叠加</h2>
<p>有些情况下可能单一的一层渐变绘制不了很复杂的图形，这就需要用到反向镂空技术了，其实就是上面提到过的<strong>遮罩合成</strong>，这里再运用一下</p>
<ol>
<li><strong>先把上面的实现拿过来</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span> / <span class="hljs-number">50%</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8091c9b608c64a0580e98a8efdacd283~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><strong>直接在这个基础上打一排小洞</strong></li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>( circle at <span class="hljs-number">50%</span>, red <span class="hljs-number">5px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">0</span>) <span class="hljs-number">50%</span> <span class="hljs-number">50%</span> / <span class="hljs-number">100%</span> <span class="hljs-number">20px</span>, <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span> / <span class="hljs-number">50%</span>;
  -webkit-<span class="hljs-attribute">mask</span>-composite: destination-out;
  <span class="hljs-attribute">mask</span>-composite: subtract; <span class="hljs-comment">/*Firefox*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1166e3e5a134328aad77c467da7f846~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>注意这里用到了**-webkit-mask-composite: destination-out**，<strong>表示减去，只显示下方遮罩，重合的地方不显示</strong></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51b69328c64e49aa966ad2d97c6b362e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/vYyoMoZ?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现9</a></p>
<p>也可以放在两边，改一下<strong>position</strong>就可以了</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>: <span class="hljs-built_in">radial-gradient</span>( circle at <span class="hljs-number">5px</span>, red <span class="hljs-number">5px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">0</span>) -<span class="hljs-number">5px</span> <span class="hljs-number">50%</span> / <span class="hljs-number">100%</span> <span class="hljs-number">20px</span>, <span class="hljs-built_in">radial-gradient</span>(circle at <span class="hljs-number">20px</span> <span class="hljs-number">20px</span>, <span class="hljs-number">#000</span>0 <span class="hljs-number">20px</span>, red <span class="hljs-number">0</span>) -<span class="hljs-number">20px</span> -<span class="hljs-number">20px</span> / <span class="hljs-number">50%</span>;
  -webkit-<span class="hljs-attribute">mask</span>-composite: destination-out;
  <span class="hljs-attribute">mask</span>-composite: subtract; <span class="hljs-comment">/*Firefox*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/890ef27c1b104061b3fede8cd30ae1d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/BaQXeNV?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen 优惠券实现10</a></p>
<h2 data-id="heading-5">六、边框遮罩</h2>
<p>有些同学觉得<strong>径向渐变太复杂，实在是写不出来，能不能用图片代替呢</strong>？其实也是可行的。这里说的边框遮罩指的是<a href="https://www.w3.org/TR/css-masking-1/#mask-borders?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">mask-border</a>, 目前还在 W3C 草案当中，不过有一个替代属性<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-mask-box-image?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">-webkit-mask-box-image</a></p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c42470a8a1c74b6cae151307d1679ae0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>语法和概念和<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/border-image?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">border-image</a>非常相似，关于<strong>border-image</strong>可参考这篇文章<a href="https://jelly.jd.com/article/6006b1045b6c6a01506c87bc?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">border-image 的正确用法</a>，这里主要了解一下用法和效果</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>-box-image: <span class="hljs-string">'遮罩图片'</span> [<top> <right> <bottom> <left> <x-repeat> <y-repeat>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如有一张这样的图片</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb1ae763e8a24aa9ab43503c99d9fe95~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>SVG代码长这样，很多工具都可以导出来，实在不会可以直接找设计同学</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"60.031"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"60.031"</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 60.031 60.031"</span>></span><span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40 60.027H20.129A20.065 20.065 0 0 0 .065 40H0V20.127h.065A20.066 20.066 0 0 0 20.131.061v-.065H40v.065a20.065 20.065 0 0 0 20.027 20.064V40A20.063 20.063 0 0 0 40 60.027z"</span> <span class="hljs-attr">fill-rule</span>=<span class="hljs-string">"evenodd"</span>/></span><span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要转义一下，可借助张老师的<a href="https://www.zhangxinxu.com/sp/svgo/?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">SVG在线合并工具</a></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>-box-image: <span class="hljs-built_in">url</span>(<span class="hljs-string">"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60.031' height='60.031' viewBox='0 0 60.031 60.031'%3E%3Cpath d='M40 60.027H20.129A20.065 20.065 0 0 0 .065 40H0V20.127h.065A20.066 20.066 0 0 0 20.131.061v-.065H40v.065a20.065 20.065 0 0 0 20.027 20.064V40A20.063 20.063 0 0 0 40 60.027z' fill-rule='evenodd'/%3E%3C/svg%3E"</span>) <span class="hljs-number">20</span>;
  <span class="hljs-comment">/*这里的20表示四周保留20像素的固定区域，剩余部分平铺或者拉伸*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就实现了这样一个形状，同样是自适应的</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f1ff835e384f71a82e3868b52c5a10~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/oNBvZmb?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen -webkit-mask-box-iamge 实现1</a></p>
<p>再比如有一张这样的图片</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e307f65e69cf450bb4e7976e1f3bbda9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>-box-image: <span class="hljs-built_in">url</span>(<span class="hljs-string">"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60.031' height='60.031' viewBox='0 0 60.031 60.031'%3E%3Cpath d='M55.186 30.158a4.965 4.965 0 0 0 4.841 4.959V40A20.063 20.063 0 0 0 40 60.027H20.129A20.065 20.065 0 0 0 .065 40H0v-4.888c.054 0 .1.016.158.016a4.973 4.973 0 1 0 0-9.945c-.054 0-.1.014-.158.015v-5.074h.065A20.066 20.066 0 0 0 20.131.058v-.065H40v.065a20.065 20.065 0 0 0 20.027 20.064v5.07a4.965 4.965 0 0 0-4.841 4.966z' fill-rule='evenodd'/%3E%3C/svg%3E"</span>) <span class="hljs-number">20</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以得到这样一个形状，两侧的半圆被拉伸了</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b880cbbe134ee392ef613255b4ad87~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这时只需要设置平铺方式**-webkit-mask-box-image-repeat ,**这个和<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/border-image-repeat?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">border-image-repeat</a>是一样的概念，有以下 4 个值</p>
<pre><code class="hljs language-css copyable" lang="css">-webkit-<span class="hljs-attribute">mask</span>-box-image-repeat: stretch; <span class="hljs-comment">/*拉伸(默认)，不会平铺*/</span>
-webkit-<span class="hljs-attribute">mask</span>-box-image-repeat: repeat; <span class="hljs-comment">/*重复*/</span>
-webkit-<span class="hljs-attribute">mask</span>-box-image-repeat: round; <span class="hljs-comment">/*重复，当不能整数次平铺时，根据情况拉伸。*/</span>
-webkit-<span class="hljs-attribute">mask</span>-box-image-repeat: space; <span class="hljs-comment">/*重复，当不能整数次平铺时，会用空白间隙填充*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>几种平铺方式的差异如下</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/969db0388c3e420fb3858895305e68dd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里我们可以采用<strong>round</strong>或者<strong>repeat</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.content</span>&#123;
  -webkit-<span class="hljs-attribute">mask</span>-box-image: <span class="hljs-built_in">url</span>(<span class="hljs-string">"..."</span>) <span class="hljs-number">20</span>;
  -webkit-<span class="hljs-attribute">mask</span>-box-image-repeat: round;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de049448aabd4533ae953d6d8ad58878~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以查看在线实例<a href="https://codepen.io/xboxyan/pen/gOgYWej?fileGuid=fKc3ePJfifoZewha" target="_blank" rel="nofollow noopener noreferrer">codepen -webkit-mask-box-iamge 实现2</a></p>
<h2 data-id="heading-6">七、总结和说明</h2>
<p>以上一共介绍了12种绘制优惠券的案例，应该可以解决掉绝大部分这类布局的问题，这里总结以下几点</p>
<ol>
<li><strong>CSS mask</strong>一定是这类布局最完美的实现方式</li>
<li>需要<strong>CSS radial-gradient</strong>绘制图形的技巧</li>
<li>尽可能采用<strong>repeat</strong>来重复相同的元素</li>
<li>多种形状叠加时需要灵活运用<strong>mask-composite</strong></li>
<li>也可以采用图片来代替CSS渐变，需要使用<strong>mask-border</strong></li>
</ol>
<p>关于兼容性，其实不考虑 IE 都没有什么大问题，最后的 mask-border 目前只兼容 chrome 内核，移动端可放心使用</p>
<p>感谢阅读，希望能对日后的工作有所启发。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            