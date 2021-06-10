
---
title: '教你三种 jQuery 框架实现元素显示及隐藏动画方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2b56dcae204e9aaf9d47a66b3b165f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 23:42:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2b56dcae204e9aaf9d47a66b3b165f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：在 jQuery 框架中对元素对象进行显示和隐藏有三种方式，分别是“默认方式显示和隐藏”、“滑动方式显示和隐藏”、“淡入淡出显示和隐藏”。</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/277408?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《jQuery框架实现元素显示及隐藏动画【附案例分析】》</a>，原文作者：灰小猿。</p>
<p>首先来看一个简单的动画效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2b56dcae204e9aaf9d47a66b3b165f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我之前也和小伙伴们讲过使用 jQuery 框架可以很好的对 html 中元素的属性等进行操作，所以上面显示和隐藏的也只是一个 div，而并不是一个图片。下面我就来和小伙伴们讲一个如何对元素的属性进行操作，使其显示或者隐藏！</p>
<p>在 jQuery 框架中对元素对象进行显示和隐藏有三种方式，分别是**“默认方式显示和隐藏”、“滑动方式显示和隐藏”、“淡入淡出显示和隐藏”。**接下来我们就分别对这三种方法进行介绍。</p>
<h2 data-id="heading-0">一、默认方式显示和隐藏</h2>
<p>在默认方法下显示元素的方法是</p>
<p><strong>show([speed,[easing],[fn]])</strong></p>
<p><strong>其中的参数含义为：</strong></p>
<ul>
<li><strong>speed</strong>：动画的速度。三个预定义的值("slow","normal","fast")或表示动画时长的毫秒数值(如：1000)</li>
<li><strong>easing</strong>：用来指定切换效果，默认是"swing"，可用参数"linear"。* swing：动画执行时效果是 先慢，中间快，最后又慢。* linear：动画执行时速度是匀速的</li>
<li><strong>fn</strong>：在动画完成时执行的函数，每个元素执行一次。</li>
</ul>
<p>同时在这里提醒一点就是，以上的三个参数是可有可无的，如果不对其进行设置，那么将以默认值执行。</p>
<p>如下实例代码：</p>
<pre><code class="copyable">// 显示div
 $("#showDiv").show("slow","swing");
 linear 匀速
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在默认方式下实现元素隐藏的方法是</p>
<p><strong>hide([speed,[easing],[fn]])</strong></p>
<p>其中的参数含义和 show 方法中的一样。同样也是三个参数是可有可无的，如果不对其进行设置，那么将以默认值执行。在这里我们增加一个最后的执行函数，让其弹出一个窗口“隐藏了...”。</p>
<p>如下实例代码：</p>
<pre><code class="copyable">// 隐藏div
$("#showDiv").hide("slow","swing",function () &#123;
    alert("隐藏了...")
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么难道我们每次都要定义一个方法用于元素显示，再定义一个方法用于元素隐藏吗？并不是的，jQuery 中也充分的考虑到了这一点，所以在有一个既能实现显示又能实现隐藏的方法</p>
<p><strong>toggle([speed],[easing],[fn])</strong></p>
<p>当调用该方法的时候，元素就会被隐藏掉，类似于 hide()方法，当再次调用时，元素又会被显示出来，类似于 show()方法。</p>
<p>其中的参数含义和上面一样</p>
<p>实例代码如下：</p>
<pre><code class="copyable">// 能显示能隐藏
 $("#showDiv").toggle("slow","linear");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​默认方式下实现效果如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea79be4e208d48e98cf44f67457d6159~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、滑动方式显示和隐藏</h2>
<p>从名字上我们应该也能区分出，**滑动方式和默认方式的不同之处其实就是显示和隐藏时的动画不一样罢了，**下面我们就来介绍一下在滑动方式下进行元素的显示、隐藏、既显示又隐藏，</p>
<p>滑动方式下显示</p>
<p><strong>slideDown([speed],[easing],[fn])</strong></p>
<p>实例代码：</p>
<pre><code class="copyable">// 滑动显示div
$("#showDiv").slideDown("slow");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滑动方式下隐藏</p>
<p><strong>slideUp([speed,[easing],[fn]])</strong></p>
<p>实例代码：</p>
<pre><code class="copyable">// 滑动隐藏div
$("#showDiv").slideUp("fetch");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滑动方式下既显示又隐藏：</p>
<p><strong>slideToggle([speed],[easing],[fn])</strong></p>
<p>实例代码：</p>
<pre><code class="copyable">// 滑动能显示能隐藏
$("#showDiv").slideToggle("slow");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滑动方式下实现效果如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ce59a3978b4a6a8c700f90ffe437cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三、淡入淡出方式显示和隐藏</h2>
<p>淡入淡出方式下进行元素的显示和隐藏其实和上面两种方法一样的，不同的也只是显示的效果不一样罢了，</p>
<p>淡入淡出方式下显示使用的方法是：</p>
<p><strong>fadeIn([speed],[easing],[fn])</strong></p>
<p>实现代码：</p>
<pre><code class="copyable">// 淡出显示div
$("#showDiv").fadeIn("slow")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>淡入淡出方式下实现隐藏</p>
<p><strong>fadeOut([speed],[easing],[fn])</strong></p>
<p>实现代码：</p>
<pre><code class="copyable">// 淡出隐藏div
$("#showDiv").fadeOut("fetch");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>淡入淡出方式下既显示又隐藏</p>
<p><strong>fadeToggle([speed,[easing],[fn]])</strong></p>
<p>实现代码：</p>
<pre><code class="copyable">// 淡入淡出显示和隐藏div
$("#showDiv").fadeToggle("fetch")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>淡入淡出方式下运行的效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c78d8ce53c9496a86faf4b5c1ce8b76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是利用 jQuery 框架对元素进行显示和隐藏的方法，下面是上面实例的完整实现代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>默认方式显示和隐藏动画</title>
    <script type="text/javascript" src="../js/jquery-3.3.1.min.js"></script>
    
    <script>
        function hideFn() &#123;
            // 隐藏div
            /*$("#showDiv").hide("slow","swing",function () &#123;
                alert("隐藏了...")
            &#125;);*/


            // 滑动隐藏div
            $("#showDiv").slideUp("fetch");


            // 淡出隐藏div
            // $("#showDiv").fadeOut("fetch");


        &#125;
        
        function showFn() &#123;
            // 显示div
            // $("#showDiv").show("slow","swing");
            // linear 匀速


            // 滑动显示div
            // $("#showDiv").slideDown("slow");


            // 淡出显示div
            $("#showDiv").fadeIn("slow")
        &#125;
        
        function toggleFn() &#123;
            // 能显示能隐藏
            // $("#showDiv").toggle("slow","linear");


            // 滑动能显示能隐藏
            // $("#showDiv").slideToggle("slow");


            // 淡入淡出显示和隐藏div
            $("#showDiv").fadeToggle("fetch")
        &#125;
        
    </script>
    
</head>
<body>
<input type="button" value="点击按钮隐藏div" onclick="hideFn()">
<input type="button" value="点击按钮显示div" onclick="showFn()">
<input type="button" value="点击按钮切换div显示和隐藏" onclick="toggleFn()">


<div id="showDiv" style="width:300px;height:300px;background:pink">
    div显示和隐藏
</div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">四、案例：广告的自动显示和隐藏</h2>
<p>既然现在我们已经知道了 jQuery 框架下是如何进行元素的显示和隐藏的，那么就应该将其应用到实际的案例中去，下面通过实现广告的自动显示和隐藏的案例，来对该技术进一步加强实践。</p>
<p>我们要实现的是，在一个简单的网页中，页面打开三秒后将广告图显示出来，显示五秒后再将广告隐藏，这里对广告图片显示和隐藏的操作，根据上面的讲解，现在实现图片的显示和隐藏应该是很容易的了，那么到底应该如何实现延时显示和隐藏呢？</p>
<p>这里就要用到 js 中的一个定时器 setTimeout(方法,时间);</p>
<p>该方法的第一个参数是一个方法名，如显示或隐藏图片的方法，第二个参数是毫秒数，表示页面加载完成后多少秒执行该方法。</p>
<p>那么根据思路，我们就可以在 jQuery 的入口函数中写入，页面加载完成 3000 毫秒，也就是三秒后调用显示图片的方法；页面加载完成 8000 毫秒，也就是八秒后调用隐藏图片的方法，中间空余的五秒为显示图片的时间。</p>
<p>下面我们来讲上述需求实现，完整代码如下：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>广告的自动显示与隐藏</title>
    <style>
        #content&#123;width:100%;height:500px;background:#999&#125;
    </style>


    <!--引入jquery-->
    <script type="text/javascript" src="../js/jquery-3.3.1.min.js"></script>
    <script>
        // 图片延时显示和隐藏的步骤
        // 1、在页面加载完成之后调用定时器setTimeout()方法
        // 2、在定时器中调用显示广告和隐藏广告的函数
        // 3、使用show和hide方法实现图片的显示和隐藏


        // 设置入口函数
        $(function () &#123;
            // 延时3秒后显示图片
            setTimeout(adShow,3000);
            // 延时6秒后隐藏图片
            setTimeout(adHide,8000);
        &#125;);
        // 显示图片
        function adShow() &#123;
            $("#ad").show("slow");
        &#125;


        // 隐藏图片
        function adHide() &#123;
            $("#ad").hide("fast");
        &#125;


    </script>
</head>
<body>
<!-- 整体的DIV -->
<div>
    <!-- 广告DIV -->
    <div id="ad" style="display: none;">
        <img style="width:100%" src="../img/adv.jpg" />
    </div>


    <!-- 下方正文部分 -->
    <div id="content">
        正文部分
    </div>
</div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f7c9cae06fc4dc7b62e78db708817d5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            