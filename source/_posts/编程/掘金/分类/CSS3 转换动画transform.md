
---
title: 'CSS3 转换动画transform'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8114'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:06:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=8114'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">CSS3 转换：</h2>
<pre><code class="copyable">通过 CSS3 转换，我们能够对元素进行移动、缩放、转动、拉长或拉伸。
您可以使用 2D 或 3D 转换来转换您的元素。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">一、transform：2D 转换方法：子属性：translate()、rotate()、scale()、skew()</h2>
<pre><code class="copyable">1.translate(x,y);偏移
        a)： translate(x,y)水平方向和垂直方向同时移动（也就是X轴和Y轴同时移动）。
        b)： translateX(x)仅水平方向移动（X轴移动）。
        c)： translateY(y)仅垂直方向移动（Y轴移动）。

2.rotate(ndeg):旋转n为数字
3.scale(x,y) 缩放  让元素根据中心原点对对象进行缩放   x,y表示倍数
        a)： scale(x,y)使元素水平方向和垂直方向同时缩放（也就是X轴和Y轴同时缩放）。
            注意：Y是一个可选参数，如果没有设置Y值，则表示X，Y两个方向的缩放倍数是一样的。
        b)： scaleX(x)元素仅水平方向缩放（X轴缩放）。
        c)： scaleY(y)元素仅垂直方向缩放（Y轴缩放）。
4.skew(xdeg,ydeg) 倾斜变形
        a)：skew(x,y)使元素在水平和垂直方向同时扭曲（X轴和Y轴同时按一定的角度值进行扭曲变形）。
            第一个参数对应X轴，第二个参数对应Y轴。如果第二个参数未提供，则值为0，也就是Y轴方向上无斜切。
        b)： skewX(x)仅使元素在水平方向扭曲变形（X轴扭曲变形）。
        c)： skewY(y)仅使元素在垂直方向扭曲变形（Y轴扭曲变形）。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">二、原点 transform-origin(x,y) x，y可以用百分比来表示</h2>
<p>表示原点的横向距离和纵向距离
在没有重置transform-origin改变元素原点位置的情况下，
CSS变形进行的旋转、位移、缩放，扭曲等操作都是以元素自己中心位置进行变形。
我们可以通过transform-origin来对元素进行原点位置改变
例： transform-origin: 0 0;  以左上角为原点
50% 0;  以上中为原点
100% 50%    以右中为原点</p>
<h2 data-id="heading-3">三、transtion:过渡动画：</h2>
<pre><code class="copyable">transition属性是一个复合属性，主要包括以下几个子属性：

    1、transition-property：指定过渡或动态模拟的CSS属性。
        所有的css属性用all
    2、transition-duration：指定完成过渡所需的时间。
        单位是s秒或者ms毫秒
    3、transition-timing-function：指定过渡函数。
        ease:由快到慢
        linear:匀速
        ease-in:加速
        ease-out:减速
        ease-in-out:先加速再减速
    4、transition-delay：指定开始出现的延迟时间。
            单位是s秒或者ms毫秒。
transition:要改变的属性或all 时间;
例如：transtion:width 2s;
    transtion:all 3s
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">四、@keyframes介绍：</h2>
<pre><code class="copyable">keyframes被称为关键帧，。在CSS3中其主要以“@keyframes”开头，后面紧跟着是动画名称加上一对花括号“&#123;…&#125;”，括号中就是一些不同时间段样式规则。
如在“0%”到“100%”之间创建更多个百分比，分别给每个百分比中给需要有动画效果的元素加上不同的样式，从而达到一种在不断变化的效果
在@keyframes中定义动画名称时，其中0%和100%还可以使用关键词from和to来代表，其中0%对应的是from，100%对应的是to。

第一步：在css样式中，先定义动画样式
    @keyframes  动画名&#123;
        from&#123; css样式&#125;
        to&#123; css样式 &#125;
    &#125;
    或者使用百分号
    @keyframes 动画名 &#123;
            0%&#123;
                left: 0;
                top: 0;
            &#125;
            30%&#123;
                left: 800px;
                top:0;
                border-radius: 50%;
            &#125;
            60%&#123;
                left: 800px;
                top:400px;
                background-color: red;
                border-radius: 50%;
                transform: scale(.5);
            &#125;
            90%&#123;
                left: 0;
                top:400px;
                background-color: green;
                border-radius: 50%;
            &#125;
            100%&#123;
                left: 0;
                top: 0;
            &#125;
        &#125;
第二步：使用animation应用动画

        animation:动画名
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5"></h2>
<h2 data-id="heading-6">五、animation：</h2>
<pre><code class="copyable">组合写法（简写）：animation: myfirst 5s linear 2s infinite alternate both;

分开写
    1、调用动画 animation-name: 主要是用来调用 @keyframes 定义好的动画名

    2、设置动画播放时间 animation-duration:  单位：s

    3、置动画时间外属性 animation-fill-mode: 
                none: 默认值，表示动画将按预期进行和结束，在动画完其最后一帧时，动画会反转到初始帧处
                forwards: 表示动画结束后继续应用最后的关键帧的位置
                backwards: 会在向元素应用动画样式时迅速应用动画的初始帧
                both: 元素动画同时具有forwards和backwards效果

    4、设置动画播放方式 animation-timing-function: ease(由快到慢）/ linear(匀速) / ease-in(加速) / ease-out(减速) ease-in-out(先加速再减速)

    5、设置动画播放之前等待的时间 animation-delay: 单位：s

    6、设置动画播放次数 animation-iteration-count: 通常设置为整数, 默认值为1; 取值为infinite，动画将会无限次的播放

    7、设置动画播放方向 animation-direction: normal是默认值,动画的每次循环都是向前播放;另一个值是alternate，他的作用是，动画播放在第奇数次向前播放，第偶数次向反方向播放

    8、设置动画的播放状态 animation-play-state: paused将正在播放的动画停下来; running将暂停的动画重新播放，这里的重新播放不一定是从元素动画的开始播放，而是从暂停的那个位置开始播放
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            