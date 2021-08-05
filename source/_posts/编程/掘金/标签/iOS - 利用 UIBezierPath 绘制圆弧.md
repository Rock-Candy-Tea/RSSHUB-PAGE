
---
title: 'iOS - 利用 UIBezierPath 绘制圆弧'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda387b634444c62bac38bcd497b49f9~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 21:50:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda387b634444c62bac38bcd497b49f9~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近要写个「会话气泡」，由于没有找到合适的背景图片，所以需要直接用 UIBezierPath 进行绘制。期间用到之前还不太熟悉的绘制圆弧相关知识，于是写下此文进行记录。</p>
<h1 data-id="heading-1">API 浅析</h1>
<p>UIBezierPath 绘制圆弧主要利用以下方法：</p>
<pre><code class="copyable">- (void)addArcWithCenter:(CGPoint)center 
  radius:(CGFloat)radius
  startAngle:(CGFloat)startAngle 
    endAngle:(CGFloat)endAngle 
   clockwise:(BOOL)clockwise
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法中各参数含义：</p>
<ul>
<li>center：圆心</li>
<li>radius：半径</li>
<li>startAngle：开始弧度</li>
<li>endAngle：结束弧度</li>
<li>clockwise：绘制方向，YES 为顺时针，NO 为逆时针</li>
</ul>
<p>相关参数的含义可以参考下图：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda387b634444c62bac38bcd497b49f9~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实这还是比较容易理解的，<strong>要想一段圆弧，就得确定圆上的两点，然后选择某个方向（顺时针或逆时针）来连接两</strong></p>
<p><strong>点。而确定圆上的点，可以通过确定圆心、半径和角度（或弧度）来实现。</strong></p>
<p>看到这里，你大概理解理解这个 API 的使用了，但是 startAngle，endAngle 的传值是弧度，如果你不理解弧度的表</p>
<p>示的话，可能你还是无法使用。 </p>
<h1 data-id="heading-2">弧度的表示</h1>
<p>弧度的表示其实在高中已经学过了，这里就简单复习一下。</p>
<p>其实圆上的一个弧度有两种表示方法，顺时针（正方向）一种，逆时针（负方向）一种。可以参考下文图示以及文字描述：</p>
<ul>
<li>从0 PI 的点开始顺时针数算是正方向的弧度，用正数表示</li>
<li>从0 PI 的点开始逆时针数算是反方向的弧度，用负数表示</li>
</ul>
<p>注：PI 表示 π \piπ<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f93fded566d24889a856bfb8bafd6f2d~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面这些系统提供的宏，能帮助我们方便的表示圆上任意点的弧度。</p>
<pre><code class="copyable">#define M_PI        3.14159265358979323846264338327950288   /* pi             */
#define M_PI_2      1.57079632679489661923132169163975144   /* pi/2           */
#define M_PI_4      0.785398163397448309615660845819875721  /* pi/4           */
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">实战演练</h1>
<p>我们要利用 UIBezierPath 绘制如下图形。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c0ba8844853441fa1d00ab1d3f68ea8~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将重点放在后面的圆弧绘制部分。可以按照如下步骤：</p>
<ul>
<li>确定圆心 center</li>
<li>确定半径 radius</li>
<li>确定起点和终点 startAngle，endAngle</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/499113c4d709495092f320616015dc83~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>我们可以有如下设置</p>
<ul>
<li>startAngle 为 <code>M_PI</code> 或 <code>-M_PI</code></li>
<li>endAngle 为 <code>1.5 * M_PI</code> 或 <code>-0.5 * M_PI</code></li>
</ul>
</li>
<li>
<p>确定绘制方向 clockwise</p>
</li>
<li>
<p>如果设置 clockwise 为 <code>YES</code> （顺时针）</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f3edeaac9f24652b6ee1bcfb8c6ca55~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终版参考代码如下：</p>
<pre><code class="copyable">CGFloat radius = 40;
CGPoint startPoint = CGPointMake(50, 200);
CGPoint endPoint = CGPointMake(150, 200);
CGPoint centerPoint = CGPointMake(150 + radius, 200);

UIBezierPath *path = [UIBezierPath bezierPath];
[path moveToPoint:startPoint];
[path addLineToPoint:endPoint];
[path addArcWithCenter:centerPoint radius:radius startAngle:M_PI endAngle:1.5 * M_PI clockwise:NO];

CAShapeLayer *layer = [CAShapeLayer layer];
layer.path = path.CGPath;
layer.fillColor = [UIColor clearColor].CGColor;
layer.strokeColor = [UIColor blueColor].CGColor;

[self.view.layer addSublayer:layer];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDT25JSVR4SllGVUlj" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.qq.com/doc/DT25JSVR4SllGVUlj" ref="nofollow noopener noreferrer">资料收录</a></h2>
<p>由于文章篇幅有限，只能点到即止地介绍当前一些工作成果和思考，如果你对 iOS 底层原理、架构设计、构建系统、如何面试有兴趣了解，你也可以关注我及时获取最新资料以及面试相关资料。如果你有什么意见和建议欢迎给我留言！</p>
<h3 data-id="heading-5">写的不好的地方欢迎大家指出，希望大家多留言讨论，让我们共同进步！</h3>
<h3 data-id="heading-6">喜欢iOS的小伙伴可以关注我，一起学习交流！！！</h3>
<p>链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin%255C_42292229%2Farticle%2Fdetails%2F113813588" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin%5C_42292229/article/details/113813588" ref="nofollow noopener noreferrer">blog.csdn.net/weixin\_422…</a></p></div>  
</div>
            