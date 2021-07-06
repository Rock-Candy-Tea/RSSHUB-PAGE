
---
title: 'css 基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92aca6126cf8438f96f7f9eff1835533~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 19:02:40 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92aca6126cf8438f96f7f9eff1835533~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">css 标准盒子模型</h3>
<blockquote>
<p>标准（W3C）盒子模型：width = 内容宽度（content） + padding + border + margin</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92aca6126cf8438f96f7f9eff1835533~tplv-k3u1fbpfcp-watermark.image" alt="标准盒子模型.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">标准文档流</h3>
<blockquote>
<p>文档流指的是元素排版布局过程中，元素会默认自动从左往右，从上往下的流式排列方式。并最终窗体自上而下分成一行行，并在每行中从左至右的顺序排放元素。</p>
</blockquote>
<h3 data-id="heading-2">行内元素有哪些?块级元素有哪些?</h3>
<blockquote>
<p>行内元素： a、b、 span、img、 input、 strong、 select、 label、 em、 button、 textarea； <br>
块级元素： div、 ul、 li、 dl、 dt、 dd、 p、 h1-h6； <br></p>
</blockquote>
<h3 data-id="heading-3">CSS优先级</h3>
<blockquote>
<p>考虑到就近原则，同权重情况下样式定义以最近者为准 <br>
载入的样式按照最后的定位为准 <br>
优先级排序： <br>
同权重情况下： !important > # > . > tag <br>
!important 比 内联优先级高</p>
</blockquote>
<h3 data-id="heading-4">CSS 权重</h3>
<ol>
<li>内联样式，如: style="..."，权值为1000。</li>
<li>ID选择器，如：#content，权值为0100。</li>
<li>类，伪类、属性选择器，如.content，权值为0010。</li>
<li>类型选择器、伪元素选择器，如div p，权值为0001。</li>
<li>通配符、子选择器、相邻选择器等。如* > +，权值为0000。</li>
<li>继承的样式没有权值</li>
</ol>
<h3 data-id="heading-5">CSS选择器</h3>
<ol>
<li>id选择器（#content）</li>
<li>类选择器（.content）</li>
<li>标签选择器（div, p, span等）</li>
<li>相邻选择器（h1+p）</li>
<li>子选择器（ul>li）</li>
<li>后代选择器（li a）</li>
<li>通配符选择器（ * ）</li>
<li>属性选择器（a[rel = "external"]）</li>
<li>伪类选择器（a:hover, li:nth-child）</li>
</ol>
<h3 data-id="heading-6">CSS3新增伪类选择器</h3>
<blockquote>
<p>:first-child  选择属于其父元素的首个子元素  <br>
:last-child   选择属于其父元素的最后一个个子元素 <br>
:nth-child(n) 匹配父元素下指定子元素，在所有子元素中排序第n <br>
:nth-child(even) 匹配父元素下偶数行子元素 <br>
:nth-child(odd) 匹配父元素下奇数行子元素 <br></p>
</blockquote>
<h3 data-id="heading-7">display</h3>
<blockquote>
<p>none   使用后元素将不会显示 <br>
block  使用后元素将变为块级元素显示，元素前后带有换行符 <br>
inline-block  使用后变为行内元素显示，前后无换行符 <br></p>
</blockquote>
<h3 data-id="heading-8">display: none; 与 visibility: hidden; 有什么区别</h3>
<blockquote>
<p>从占据空间角度看：display: none;会让元素完全从渲染树中消失，渲染的时候不占据任何空间；visibility: hidden;不会让元素从渲染树消失，渲染师元素继续占据空间，只是内容不可见； <br>
从继承方面角度看：display: none;是非继承属性，子孙节点消失由于元素从渲染树消失造成，通过修改子孙节点属性无法显示；visibility:hidden;是继承属性，子孙节点消失由于继承了hidden，通过设置visibility: visible;可以让子孙节点显式； <br>
从重绘和重排角度看：修改常规流中元素的display通常会造成文档重排。修改visibility属性只会造成本元素的重绘 <br></p>
</blockquote>
<h3 data-id="heading-9">position</h3>
<blockquote>
<p>relative（相对定位）： 生成相对定位的元素，定位原点是元素本身所在的位置； <br>
absolute（绝对定位）：生成绝对定位的元素，定位原点是离自己这一级元素最近的一级 <br>
position设置为absolute或者relative的父元素的左上角为原点的 <br>
fixed （老IE不支持）：生成绝对定位的元素，相对于浏览器窗口进行定位。 <br>
static：默认值。没有定位，元素出现在正常的流中 <br></p>
</blockquote>
<h3 data-id="heading-10">CSS3有哪些新特性</h3>
<ol>
<li>选择器</li>
<li>圆角（border-raduis）</li>
<li>阴影（shadow）</li>
<li>文字特效（text-shadow）;</li>
<li>旋转（rotate）/缩放（scale）/倾斜（skew）/移动（translate）</li>
<li>媒体查询（@media）</li>
</ol>
<h3 data-id="heading-11">伪元素</h3>
<h3 data-id="heading-12">元素塌陷</h3>
<h3 data-id="heading-13">line-height</h3>
<h3 data-id="heading-14">margin-top 问题</h3>
<h3 data-id="heading-15">精灵图</h3>
<h3 data-id="heading-16">flex</h3>
<h3 data-id="heading-17">字体图标</h3></div>  
</div>
            