
---
title: 'JavaScript的轮播图'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'images/1.jpg'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:52:19 GMT
thumbnail: 'images/1.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>轮播图：在一个模块或者说窗口，通过电脑上鼠标点击、手机上手指滑动后，可以看到多张图片。这些图片就都是轮播图，这个模块就叫做轮播模块。</p>
<p>如何才能在js里面做成一个轮播图呢，比如下面这种的，可以自动生成图片对应的小圆点、点击左右箭头可以跳到上或下一张图片、每隔几秒自动轮播，还可以点击小小圆点去到指定的图片。</p>
<h2 data-id="heading-0">HTML结构</h2>
<p>首先我们创建一个HTML页面，这个结构很简单，用一个大的div嵌套两个div，取个名字叫slider，上面的div用来装图片，取个名字叫slider-img，下面的div就是控件，用来装上下张图片的按钮和小圆点，这个就叫做slider-ctrl。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <link rel="stylesheet" href="css/index.css"/>
    <script src="../public.js"></script>
    <script src="./js/index.js"></script>
</head>
<body>
    <div class="slider" id="slider">
        <div class="slider-img">
            <ul>
                <li><a href="#"><img src="images/1.jpg" alt=""/></a></li>
                <li><a href="#"><img src="images/2.jpg" alt=""/></a></li>
                <li><a href="#"><img src="images/3.jpg" alt=""/></a></li>
                <li><a href="#"><img src="images/4.jpg" alt=""/></a></li>
                <li><a href="#"><img src="images/5.jpg" alt=""/></a></li>
                <li><a href="#"><img src="images/6.jpg" alt=""/></a></li>
            </ul>
        </div>
        <div class="slider-ctrl">
        //在这里自动生成小圆点
            <span class="prev" id="prev"></span>
            <span class="next" id="next"></span>
        </div>
    </div>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">CSS代码</h2>
<pre><code class="copyable">* &#123;
    margin: 0;
    padding: 0;
&#125;
.slider &#123;
    width: 310px;
    height: 265px;
    margin: 100px auto;
    position: relative;
    overflow: hidden;
&#125;
.slider-img &#123;
    width: 310px;
    height: 220px;
&#125;
ul &#123;
    list-style: none;
&#125;
li &#123;
    position: absolute;
    top: 0;
    left: 0;
&#125;
.slider-ctrl &#123;
    text-align: center;
    padding-top: 10px;
&#125;
.slider-ctrl-con &#123;
    display: inline-block;
    width: 24px;
    height: 24px;
    background: url(../images/icon.png) no-repeat -24px -780px;
    text-indent: -99999px;
    margin: 0 5px;
    cursor: pointer;
&#125;
.slider-ctrl-con.current &#123;
    background-position: -24px -760px;
&#125;
.prev,.next &#123;
    position: absolute;
    top: 40%;
    width: 30px;
    height: 35px;
    background: url(../images/icon.png) no-repeat;
&#125;
.prev &#123;
    left: 10px;
&#125;
.next &#123;
    right: 10px;
    background-position: 0 -44px;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">js代码</h2>
<p>首先需要做一波需求分析，能够理清思路，然后在来一步一步的写代码。我们先获取相关的元素，然后根据图片数量生成对应的小圆点，由于图片是堆叠在一起的，我们把其他的图都放到右边隐藏起来，显示第一张图片即可。随后需要点亮第一个小圆点，保证小圆点和图片是绑定在一起的。然后我们需要实现点击右箭头看到下一张图，点击左箭头看到上一张图，点击小圆点可以显示对应的图片，且都要点亮相对于的图片。最后就是让他自动轮播图片，鼠标移入时停止轮播，鼠标移出时继续轮播</p>
<pre><code class="copyable">window.onload = function()&#123;
    // 0 获取相关元素
    // 总容器
    var slider = document.getElementById('slider');
    // 所有图片li的集合
    var imgLiS = slider.children[0].children[0].children;
    // 控制按钮的容器
    var ctrlDiv = slider.children[1];
    // 左箭头（上一张按钮）
    var prev = document.getElementById('prev')
    // 右箭头（下一张按钮）
    var next = document.getElementById('next')
    // 容器的宽度
    var width = slider.offsetWidth;
    // 用一个变量记录当前显示的图片的索引
    var index = 0;

    // 1 根据图片数量生成对应的小圆点
    for(var i=imgLiS.length-1;i>=0;i--)&#123;
        var newPoint = document.createElement('span');
        // 给每个节点里面记录他是第几个节点，方便后期点击时候知道是第几个
        newPoint.className = "slider-ctrl-con";
        newPoint.innerHTML = i;
        // 放到最前面
        ctrlDiv.insertBefore(newPoint,ctrlDiv.children[0])

        // 2 所有的图片都放到右边
        imgLiS[i].style.left = width+"px"
    &#125;

    // 2 轮播图显示第一幅图
    imgLiS[index].style.left = 0;

    // 获取所有的小圆点
    var ctrlS = ctrlDiv.children;
    // 3 点亮第一个小圆点
    light()

    // 4 点击左箭头可以看前一幅图，点亮对应的小圆点
    prev.onclick = prevImg;

    // 5 点击右箭头可以看后一幅图，点亮对应的小圆点
    next.onclick = nextImg;

    // 6 点击小圆点，点亮这个小圆点，并显示对应的图片
    for(var i=0;i<imgLiS.length;i++)&#123;
        ctrlS[i].onclick = function()&#123;
            var num = +this.innerHTML;
            if(num>index)&#123;
                // 我认为后面的图在右边
                imgLiS[num].style.left = width+"px";
                // 当前图去左边
                move(imgLiS[index],'left',-width)
                // 我要看的图去中间
                move(imgLiS[num],'left',0)                
            &#125;
            if(num<index)&#123;
                // 我认为前面的图在左边
                imgLiS[num].style.left = -width+"px";
                // 当前图去右边
                move(imgLiS[index],'left',width)
                // 我要看的图去中间
                move(imgLiS[num],'left',0)                
            &#125;

            // 更新index
            index = num;
            // 点亮小圆点
            light()
        &#125;
    &#125;

    // 7 可以自动轮播图： 每隔3秒看下一张
    var timer = setInterval(nextImg,3000)
    // 8 鼠标移入停止轮播
    slider.onmouseenter = function()&#123;
        clearInterval(timer)
    &#125;
    // 9 鼠标移出继续轮播 
    slider.onmouseleave = function()&#123;
        clearInterval(timer)
        timer = setInterval(nextImg,3000)
    &#125;
    
    
    
    // 由于点亮小圆点多次执行，封装成函数
    function light()&#123;
        for(var i=0;i<imgLiS.length;i++)&#123;
            ctrlS[i].className = "slider-ctrl-con"
        &#125;
        ctrlS[index].className = "slider-ctrl-con current"
    &#125;

    // 看上一张图的函数
    function prevImg()&#123;
        var num = index-1;
        if(num<0)&#123;
            // 索引最小是0，如果要看的索引比0小，就是最后一张，也就是第length-1张
            num = imgLiS.length-1;
        &#125;
        // 我认为前一张图一定在左边
        imgLiS[num].style.left = -width+"px";
        // 当前图片运动到右边
        move(imgLiS[index],'left',width)
        // 要看的图片运动到中间
        move(imgLiS[num],'left',0)
        // 运动完成以后容器里面显示的是num这个图
        // 所以记录当前索引的index里面的值变成num
        index = num;
        light()

    &#125;

    // 看下一张图的函数
    function nextImg()&#123;
        var num = index + 1;
        if(num>imgLiS.length-1)&#123;
            num = 0;
        &#125;
        // 我认为下一张一定在右边
        imgLiS[num].style.left = width+"px";
        // 当前图片去左边
        move(imgLiS[index],'left',-width)
        // 我要看的下一张去中间
        move(imgLiS[num],'left',0)
        // 更新index的值
        index = num;
        light()
    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>每天进步一点点，分享每一份知识</p></div>  
</div>
            