
---
title: 'SVG 入门基础（2）形状元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac87769c35024346bf37ed41cb18d142~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 20:23:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac87769c35024346bf37ed41cb18d142~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">1. 图形元素</h4>
<p><strong>1.1 矩形</strong></p>
<p>矩形使用 < rect > < /rect > 标签来进行绘制。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">rx</span>=<span class="hljs-string">"5"</span> <span class="hljs-attr">ry</span>=<span class="hljs-string">"5"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>x：左上角x的坐标，距离左边的距离，相当于margin-left；</p>
<p>y：左上角y的坐标，距离顶部的距离，相当于margin-top；</p>
<p>width：矩形的宽度（单位：像素）；</p>
<p>height：矩形的高度（单位：像素）；</p>
<p>rx：圆角矩形，x轴方向的半径；</p>
<p>ry：圆角矩形，y轴方向的半径</p>
<p>fill：填充颜色</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac87769c35024346bf37ed41cb18d142~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.2 圆形</strong></p>
<p>圆形使用 < circle > < /circle > 标签来进行绘制。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>cx：圆形的x坐标；</p>
<p>cy：圆心的y做标；</p>
<p>r：半径</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84cf81e13d1f479389e9d57ba9b40ecd~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.3 椭圆形</strong></p>
<p>椭圆形使用标签 < ellipse > < /ellipse > 标签进行绘制，与圆形的绘制方法类似。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ellipse</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">rx</span>=<span class="hljs-string">"40"</span> <span class="hljs-attr">ry</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span>></span><span class="hljs-tag"></<span class="hljs-name">ellipse</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>cx：圆心的x坐标；</p>
<p>cy：圆心的y坐标；</p>
<p>rx：水平方向上的半径；</p>
<p>ry：垂直方向上的半径</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fa2b4353e6e4bb0b0ae6d371cc9c994~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.4 线段</strong></p>
<p>线段使用 < line > < /line > 标签进行绘制。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">line</span> <span class="hljs-attr">x1</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y1</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">x2</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">y2</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"yellow"</span>></span><span class="hljs-tag"></<span class="hljs-name">line</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>x1：起点的 x 坐标；</p>
<p>y1：起点的 y 坐标；</p>
<p>x2：终点的 x 坐标；</p>
<p>y2：终点的 y 坐标;</p>
<p><strong>1.5 折线和多边形</strong></p>
<p>折线和多边形的绘制方法类似，都是用 <strong>points 属性</strong>设置各个点的坐标。</p>
<p>折线使用标签 < polyline > < /polyline > 进行绘制，而多边形使用标签 < polygon >< /polygon > 进行绘制，且多边形会将起点和终点连接起来，折线不会。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* 图一 折线，不会将起点与终点连接 */</span>
<svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">polyline</span> 
  <span class="hljs-attr">points</span>=<span class="hljs-string">"50,10 80,90 10,30 90,30 20,90"</span> 
  <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> 
  <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"3"</span> 
  <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">polyline</span>></span></span>
</svg>
 
<span class="hljs-comment">/* 图二 多边形，将起点与终点连接 */</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">polygon</span> 
  <span class="hljs-attr">points</span>=<span class="hljs-string">"50,10 80,90 10,30 90,30 20,90"</span> 
  <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> 
  <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"3"</span> 
  <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">polygon</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>ponits：设置各个点的坐标，各组坐标之间使用空格分隔，x坐标和y坐标之间使用逗号分开。</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17c5534d153f4909b881e58fde543a2d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.6 路径</strong></p>
<p>路径使用标签 < path > < /path > 进行绘制，使用 d 属性控制路径的类型和绘制。</p>
<p>路径的功能最多，前面的所有图形都可以使用路径进行绘制。</p>
<p><strong>d 属性值的书写有两种:使用逗号分隔坐标，如：d="M10, 10"，也可以使用空格的形式，如：d="M 10 10"</strong></p>
<p><strong>注意: 大写字母：表示坐标系中使用绝对坐标，小写字母：使用相对坐标（相对当前画笔所在的点)；</strong></p>
<p><strong>1.6.1 移动类参数</strong></p>
<p><strong>M：moveto，将画笔移动到指定坐标；</strong></p>
<p>eg：d="M10,10"，表示将画笔移动到坐标(10,10)的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M 10 10 L 180 180"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e8eddbb64ad487785e2a6faf843f50c~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.6.2 绘制直线类参数</strong></p>
<p><strong>L：lineto，绘制直线到指定坐标</strong></p>
<p>eg：d="M 10 10 L 80 80"，表示绘制一条起点坐标为(10,10)，终点坐标为(80,80)的直线。</p>
<p><strong>H：horizontal  lineto，绘制水平直线到指定坐标</strong></p>
<p>eg：d="M 10 10 H 100"，表示是绘制一条起点坐标为(10,10)，终点坐标为(100,10)的直线</p>
<p><strong>注意：</strong> H只需要设置一个值，如果设置了多个值，则最后取最后一个值。</p>
<p><strong>V：vertical，绘制垂直直线到指定坐标</strong></p>
<p>eg：d="M 10 10 V 100"，表示绘制一条起点坐标(10,10)，终点坐标为(10,100)的直线</p>
<p><strong>注意：</strong> V只需要设置一个值，如果是多个值，则取最后一个值。</p>
<p><strong>1.6.3 绘制曲线类参数</strong></p>
<p><strong>C：curveto，绘制三次方贝塞尔曲线到终点坐标，中间经过两个控制点控制曲线的弧度，所以需要制定三个坐标来实现绘制曲线；</strong></p>
<p>eg：d="M10,10 C40,5 40,140 100,100"</p>
<p><strong>S：shorthand/smooth curveto，绘制平滑三次方贝塞尔曲线到终点坐标，与上一条三次方贝塞尔曲线相连，第一个控制点为上一条曲线第二个控制点的对称点，所以还需制定一个控制点坐标和终点坐标。</strong></p>
<p>eg：d="M10,10 C40,5 40,140 100,100 S140,180 160,160"，如果不与贝塞尔曲线相连，即：d="M10,10 S140,180 160,160"，则绘制的图线接近于二次贝塞尔曲线。</p>
<p><strong>Q：quadratic Bezier curveto，绘制二次贝塞尔曲线到终点坐标，中间经过一个控制点控制曲线的弧度。</strong></p>
<p>eg：d="M10,10 Q40,140 100,100"</p>
<p><strong>T：shorthand/smooth quadratic Bezier curveto，绘制平湖二次贝塞尔曲线到终点坐标，与上一条二次贝塞尔曲线相连，控制点为上一条曲线控制点的对称点，所以还需指定一个终点坐标。</strong></p>
<p>eg：d="M10,10 Q40,140 100,100 T160,160"，如果不与贝塞尔曲线相连，即：d="M10,10 T160,160"，则绘制的图线是一条直线。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/* 图一 三次方贝塞尔曲线 */</span>
<svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,10 C40,5 40,140 100,100"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4px"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span></span>
</svg>
 
<span class="hljs-comment">/* 图二 三次方贝塞尔曲线，与上一条曲线相连 */</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,10 C40,5 40,140 100,100 S140,180 160,160"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4px"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
 
<span class="hljs-comment">/* 图三 二次贝塞尔曲线 */</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,10 Q40,140 100,100"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4px"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
 
<span class="hljs-comment">/* 图四 二次方贝塞尔曲线，与上一条曲线相连 */</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M10,10 Q40,140 100,100 T160,160"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4px"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33952d189e5c424f888a7a27fbb414a1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.6.4 绘制弧线类参数</strong></p>
<p>A：el liptical arc，绘制椭圆曲线到指定坐标，</p>
<p><strong>参数说明：</strong></p>
<p>rx，ry：x轴方向半径，y轴方向半径；</p>
<p>x-axis-rotation：x轴与水平顺时针方向夹角；</p>
<p>large-arc-flag：角度弧线大小(1：大，0：小)；</p>
<p>sweep-flag：绘制方向(1：顺时针，0：逆时针)；</p>
<p>x y：终点坐标；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"500"</span> height=<span class="hljs-string">"500"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M50,50 A60 30 0 1,0 150,50 Z"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#fb3"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"4px"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">path</span>></span></span>
</svg>    
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>分析：</strong> 起点坐标(50,50)，终点坐标(150,50)，角度为0，角度弧线大小 large-arc-flag 为 1，选择大弧度，根据分析，即选择红色的弧线，又绘制方向 sweep-flag 为 0，为逆时针，即从起点沿着逆时针方向绘制到终点，所以是红色先位于下方。</p>
<p><strong>注意：</strong> 当 (起点与终点之间的直线距离／2) > (椭圆的水平半径) 时，角度为 0 的情况下，此时椭圆会等比放大，到相等为止。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/195fb9a4fe9247d2aa5d6ba8df5336a1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1.6.5 闭合类参数</strong></p>
<p>Z：closepath，绘制直线将终点与起点连接；</p>
<p><strong>再次提醒：大写字母：表示坐标系中使用绝对坐标，小写字母：使用相对坐标（相对当前画笔所在的点）</strong></p>
<h4 data-id="heading-1">2. 文字元素</h4>
<p><strong>2.1 基础</strong></p>
<p>在svg中使用 < text >< /text> 标签绘制文字。</p>
<p><strong>参数说明：</strong></p>
<p>x：文字的x坐标；</p>
<p>y：文字的y坐标；</p>
<p>dx：相对于当前位置x方向的距离；</p>
<p>dy：相对于当前位置的y方向的距离；</p>
<p>textLength：文字的显示长度；</p>
<p>rotate：旋转角度，也可以使用transform="rotate(30)"；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"200"</span> height=<span class="hljs-string">"200"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">dx</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">dy</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">textLength</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">rotate</span>=<span class="hljs-string">"20"</span>></span>示例文字<span class="hljs-tag"></<span class="hljs-name">text</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74510cbef9e44acea87703373af7b465~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2.2 文本路径</strong></p>
<p>如果要实现文字沿着路径进行排列，可使用 < textPath >< /textPath > 标签来实现。需要提前定义好路径 path，并指定 id，textPath 使用 xlink:href 定义文字要匹配的路径。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"600"</span> height=<span class="hljs-string">"600"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">path</span> 
    <span class="hljs-attr">id</span> = <span class="hljs-string">"textPath1"</span> 
    <span class="hljs-attr">d</span> = <span class="hljs-string">"M100,100 C140,50 140,240 200,200 S240,280 360,360"</span> 
    <span class="hljs-attr">stroke</span> = <span class="hljs-string">"#fb3"</span> 
    <span class="hljs-attr">stroke-width</span> = <span class="hljs-string">"4px"</span> 
    <span class="hljs-attr">fill</span> = <span class="hljs-string">"transparent"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">path</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">dx</span>=<span class="hljs-string">"-10"</span> <span class="hljs-attr">dy</span>=<span class="hljs-string">"-10"</span> <span class="hljs-attr">rotate</span>=<span class="hljs-string">"20"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">textPath</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#textPath1"</span> <span class="hljs-attr">textLength</span>=<span class="hljs-string">"300"</span>></span>
            很扭曲的测试示例文字
        <span class="hljs-tag"></<span class="hljs-name">textPath</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">text</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f382c556293e41febe3589088a62350d~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">3. 特殊元素</h4>
<p><strong>3.1 克隆元素 use</strong></p>
<p>use 标签用来克隆其他元素，克隆后的元素不能修改样式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">rect</span> 
  <span class="hljs-attr">id</span>=<span class="hljs-string">"rect1"</span>
    <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>
    <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#5588aa"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"5"</span>
    <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#rect1"</span>></span><span class="hljs-tag"></<span class="hljs-name">use</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>参数说明：</strong></p>
<p>x：相对被克隆元素 x 轴偏移量；</p>
<p>y：相对被克隆元素 y 轴偏移量；</p>
<p>xlink:href：指向被克隆元素的 ID；</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47efe4d9ce4c4627a7c56578c3c7e673~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.2 模板元素</strong></p>
<p><strong>3.2.1 symbol</strong></p>
<p>symbol标签用定义模版，需要结合use标签使用，模版在未被使用之前，不会展示在页面上，模版内部可包含多个元素。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">symbol</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"template1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> 
    <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>
        <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#5588aa"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"5"</span>
        <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"60"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"30"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"#5588aa"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"3"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span><span class="hljs-tag"></<span class="hljs-name">circle</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">symbol</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span> <span class="hljs-attr">xlink:href</span>=<span class="hljs-string">"#template1"</span>></span><span class="hljs-tag"></<span class="hljs-name">use</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8399c02ee6d44864b48bca9d297ba873~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.2.2 defs</strong></p>
<p>defs标签用于自定义形状，它内部的代码不会显示，仅供引用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"300"</span> height=<span class="hljs-string">"100"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCircle"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"25"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"20"</span>></span>圆形<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"20"</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">g</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">defs</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#myCircle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#myCircle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"blue"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#myCircle"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"white"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"blue"</span> /></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccac49279b54dd1a86939331a7196ee~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.2.3 pattern</strong></p>
<p>pattern标签用于自定义一个形状，该形状可以被引用来平铺一个区域。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"500"</span> height=<span class="hljs-string">"500"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">pattern</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"dots"</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">patternUnits</span>=<span class="hljs-string">"userSpaceOnUse"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#bee9e8"</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"35"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">pattern</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">defs</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"url(#dots)"</span> /></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，< pattern > 标签将一个圆形定义为 dots 模式。patternUnits="userSpaceOnUse" 表示< pattern > 的宽度和长度是实际的像素值。然后，指定这个模式去填充下面的矩形。</p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c613d4b7c391489fbdcaed5537946361~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.3 组元素g</strong></p>
<p>group的简写，用来创建分组，<strong>组内所有的元素都会继承 g 的属性，可以嵌套使用</strong>，也可以和use标签结合使用。</p>
<p>另外可使用 transform 属性定义控制整个组的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"500"</span> height=<span class="hljs-string">"500"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">stroke-width</span>=<span class="hljs-string">"3"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"transparent"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"120"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"120"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">g</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>g标签内部的两个矩形，都会继承g标签的样式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e31ab6740bb64c898bfa476dd7445208~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.4 clipPath 裁剪元素</strong></p>
<p>lipPath 元素主要用来剪裁元素，clipPath 元素定义范围外的内容将不会被展示。</p>
<p><strong>注意:</strong> 写在< clipPath >< /clipPath >标签内部的元素不会被显示，clipPath 标签需要放在 defs 标签内。其他元素在引用clipPath元素时，需要使用 clip-path="url(#ID)"。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg height=<span class="hljs-string">"200"</span> width=<span class="hljs-string">"200"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">clipPath</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"clip"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">clipPath</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">clip-path</span>=<span class="hljs-string">"url(#clip)"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span> /></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>分析图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9303fb076fe449196a09ba7bf1b5ca6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0c079cfaace4f67aa8dba15849f5199~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.5 image 定义图像</strong></p>
<p>< image >标签用于插入图片文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg height=<span class="hljs-string">"200"</span> width=<span class="hljs-string">"200"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">clipPath</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"clip"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">clipPath</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">circle</span> <span class="hljs-attr">cx</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">cy</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">r</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">clip-path</span>=<span class="hljs-string">"url(#clip)"</span> <span class="hljs-attr">stroke</span>=<span class="hljs-string">"none"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"yellow"</span> /></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，< image >的 xlink:href 属性表示图像的来源。</p>
<p><strong>3.6  动画</strong></p>
<p><strong>3.6.1 animate</strong></p>
<p>animate 标签用于产生动画效果</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"500px"</span> height=<span class="hljs-string">"500px"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#feac5e"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"x"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"2s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"width"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"2s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">rect</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，矩形会不断移动且宽度不断增加至500，产生动画效果。</p>
<p><strong>参数说明：</strong></p>
<p>attributeName：发生动画效果的属性名。</p>
<p>from：单次动画的初始值。</p>
<p>to：单次动画的结束值。</p>
<p>dur：单次动画的持续时间。</p>
<p>repeatCount：动画的循环模式。</p>
<p><strong>3.6.2 animateTransform</strong></p>
<p>< animate >标签对 CSS 的 transform 属性不起作用，如果需要变形，就要使用 < animateTransform > 标签。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><svg width=<span class="hljs-string">"500px"</span> height=<span class="hljs-string">"500px"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"250"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"250"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#4bc0c8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> 
    <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> 
    <span class="hljs-attr">type</span>=<span class="hljs-string">"rotate"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span> 
    <span class="hljs-attr">from</span>=<span class="hljs-string">"0 200 200"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"360 400 400"</span> 
    <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">rect</span>></span></span>
</svg>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，< animateTransform > 的效果为旋转（rotate），这时 from 和 to 属性值有三个数字，第一个数字是角度值，第二个值和第三个值是旋转中心的坐标。from="0 200 200"表示开始时，角度为0，围绕(200, 200)开始旋转；to="360 400 400"表示结束时，角度为360，围绕(400, 400)旋转。</p>
<h4 data-id="heading-3">本文仅列了部分常用元素属性，更多内容请移步<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fsvg%2Fsvg-reference.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/svg/svg-reference.html" ref="nofollow noopener noreferrer">SVG文档</a></h4></div>  
</div>
            