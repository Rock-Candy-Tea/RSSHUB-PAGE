
---
title: 'clip-path属性的探秘之旅🧐'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172e58305d4f41bd94c94f7644c46575~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 00:44:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172e58305d4f41bd94c94f7644c46575~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>最近在搭建自己微前端应用的过程中，发现了一个自己之前不曾了解但是却非常有用的css属性: <strong>clip-path</strong>，在经过一番摸索后，决定将所知所学整理成文，方便日后回顾</p>
<p>接下来我们就一起进入 <strong>clip-path</strong> 属性的探秘之旅吧~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172e58305d4f41bd94c94f7644c46575~tplv-k3u1fbpfcp-watermark.image" alt="ppx.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">clip-path的前辈：clip</h2>
<p>在我们了解clip-path之前，我们先将目光转移到它的前辈: <strong>clip</strong> 身上</p>
<p>clip属性是用于<strong>裁剪</strong>元素的，它可以在对应元素内指定一个矩形区域进行裁剪，最终拿到对应元素的矩形子域，它的用法示例如下：</p>
<pre><code class="copyable">/* 不支持百分比的写法，如 clip:rect(50%, 60%, 30%, 50%)是不合法的 */
div&#123;
  position:absolute;
  clip:rect(0px,60px,200px,0px); 
  clip:rect(50px 250px 250px 50px); /* 兼容IE6, IE7，需要将值之间的逗号去掉 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到它的用法十分简单：<strong>以对应元素的左上角为坐标原点，分别设置top, right, bottom, left，同时将该元素的定位设置为absolute或fixed</strong>。虽然用法简单，但是它有如下两个缺点：</p>
<ul>
<li>只对绝对定位(absolute,fixed)的元素有效，而对于relative和static的元素无效</li>
<li>因为只有rect()函数可用，所以只能用来裁剪出矩形</li>
</ul>
<p>我们再来看看它的兼容性如何</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e63a7634274131b2c9a565bd429963~tplv-k3u1fbpfcp-watermark.image" alt="clip.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到clip的兼容性还是很喜人的，但是由于它存在上述两个缺点，所以导致它的适用场景并不是很多，而本文的主角 <strong>clip-path</strong> 就是为了解决这两个使用痛点而诞生的，那么接下来我们就好好认识下这个神奇的属性吧~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f079f143bc3d405fa8bbf1ecac3c50dc~tplv-k3u1fbpfcp-watermark.image" alt="qiangda.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">生来便是主角</h2>
<p>clip-path可以应用于任何元素，由于没有clip的第一条限制，因此大大拓宽了适用场景，它支持设置三个属性，列举如下：</p>
<ul>
<li><strong>clip-source</strong>：可以使用形如 clip-path:url(resources.svg#c1) 的方式从svg导入裁剪元素的路径</li>
<li><strong>basic-shape</strong>：绘制图形的函数，种类很多，列举如下：
<ul>
<li>circle，用于裁剪出圆形</li>
<li>ellipse，用于裁剪出椭圆形</li>
<li>inset，用于裁剪出矩形</li>
<li>polygon，用于裁剪出任意图形，最为强大的一个api</li>
</ul>
</li>
<li><strong>geometry-box</strong>：可以看成裁剪区域的坐标系，里的api的坐标都将以指定的盒子进行定位，如果不指定，默认是border-box，它的取值列举如下：
<ul>
<li>margin-box</li>
<li>border-box</li>
<li>padding-box</li>
<li>content-box</li>
<li>fill-box</li>
<li>stroke-box</li>
<li>view-box</li>
</ul>
</li>
</ul>
<p>通过属性可以知道clip-path非常强大，借助它我们可以实现任何天马行空的创意~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1769935db0f46af90b9876fdd18d07f~tplv-k3u1fbpfcp-watermark.image" alt="nice.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面列出中各个api的具体用法</p>
<pre><code class="copyable">/*
    需要注意的是，所有api里面的百分比都是以元素宽度作为基准来计算的
*/


/* 
    circle(radius at x-axis y-axis) 
    为了创建圆形，需要给circle传入三个值：圆心的坐标（X值和Y值）以及半径。当定义圆的半径时，我们可以用at关键字来定义圆心坐标。
*/
div &#123;   
  clip-path: circle(50% at 50% 50%);   
&#125;  

/* 
    ellipse(x-radius y-radius at x-axis y-axis) 
    为了实现椭圆，需要给ellipse提供4个值：椭圆的x轴半径、y轴半径、定位椭圆位置的x坐标和y坐标，后面两个值用at关键字和前面两个值分开。
*/
div &#123;   
  clip-path: ellipse(100px 200px at 50% 50%);  
&#125; 

/* 
    inset(<top> <right> <bottom> <left> round <top-radius> <right-radius> <bottom-radius> <left-radius>)
    使用四个值（对应“上 右 下 左”的顺序）来裁剪矩形和设置圆角半径。 
*/
div &#123;   
  clip-path: inset(25% 0 25% 0 round 0 25% 0 25%);  
  clip-path: inset(25% 0 round 0 25%); /* 简写形式 */
&#125; 

/* 
    polygon(x1-axis y1-axis, x2-axis y2-axis, … )   
    指定各个节点的坐标，不限制数量，最终将所有点连接起来形成裁剪框，从而裁剪出我们需要的形状
    它是最强大的api，通过它我们可以裁剪出包括但不限于上述所有api的图形 
*/
div &#123;   
  clip-path: polygon(0% 0%, 100% 0%, 100% 75%, 75% 75%, 75% 100%, 50% 75%, 0% 75%);   
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后贴一下clip-path的兼容性截图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff54f38e1070477f9cfe7af3e1b8e889~tplv-k3u1fbpfcp-watermark.image" alt="clip-path.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到该属性的兼容性十分不乐观，IE全系不支持，chrome也要到54才能完全支持，因此造成了该属性虽然强大，但是比较冷门的局面，因为历史包袱的原因让这么牛逼的css属性不能被广泛普及，真是可惜呀~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8d9bdb059e04d88918f6a64bee209d9~tplv-k3u1fbpfcp-watermark.image" alt="cat.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">结语</h2>
<p>css虽然相对于其他语言更简单一些，但是还是有很多地方可以去挖掘，类似于clip-path这样冷门但非常强大的属性应该还有很多，唯有不断去钻研才能开拓自己的眼界，所以加油吧，骚年！🤪</p>
<h2 data-id="heading-3">一点小小的请求</h2>
<p>既然都看到这里啦，如果你喜欢我的文章，那么请动动你的手指，帮我的文章点个赞或收个藏，xdm的支持是我创作的最大动力，自己单机真不好玩！</p>
<p>最近自己搭建了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.carlblog.site" target="_blank" rel="nofollow noopener noreferrer" title="http://www.carlblog.site" ref="nofollow noopener noreferrer">个人博客</a>，上面会最先发布我写的文章，希望感兴趣的小伙伴都去逛逛，如果能评论留言就更好啦，嘿嘿，期待你们的光临哦~</p></div>  
</div>
            