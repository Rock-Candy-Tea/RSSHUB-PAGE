
---
title: '盘点用 jQuery 框架实现_for 循环_的四种方式！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4588e600d28418385ef81c2f3871820~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 18:16:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4588e600d28418385ef81c2f3871820~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​​<a href="https://bbs.huaweicloud.com/blogs/278907?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">【本期推荐】为什么一到大促，我们的钱包总是被掏空？是大家自制力不够，还是电商平台太会读懂人心，从技术维度，抽丝剥茧一探究竟。</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4588e600d28418385ef81c2f3871820~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>​​​​摘要：分享在 jQuery 高级开发中对元素标签体的遍历常用的几种方法。</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/279501?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《盘点用jQuery框架实现“for循环”的四种方式！》</a>，原文作者：灰小猿 。</p>
<p>今天继续来和大家分享在 jQuery 高级开发中对元素标签体的遍历常用的几种方法。</p>
<p>我们以一个案例的形式进行讲解，假如我们需要遍历的是如下 ul 标签中的 li 标签：</p>
<pre><code class="copyable"><body>
<ul id="city">
    <li>北京</li>
    <li>上海</li>
    <li>天津</li>
    <li>重庆</li>
</ul>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">一、JS 的遍历方式</h2>
<p>首先第一种：利用 js 对象进行遍历</p>
<p>利用 js 对象的方法进行遍历和我们平常的 for 循环遍历是一样的思路和解法，首先我们应该获取到需要遍历的元素标签，然后使用 for 循环方法对其中存在的标签进行遍历：下面以一个实例来进行讲解。</p>
<p>遍历四个 li 标签，并且弹出其中的内容，如果标签体内容是“上海”,则不弹出！</p>
<pre><code class="copyable"> $(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")
            // 利用js中的for循环进行遍历
            // 将获取到的li标签数组进行遍历
            for (var i = 0; i < citys.length; i++) &#123;
                 // 循环内容判断
                if ("上海" == citys[i].innerHTML)&#123;
                  // break;
                    continue;
                &#125;
                // 输出获取到的li标签中的内容
                alert(i + citys[i].innerHTML);
            &#125;


        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、JQuery 的遍历方式</h2>
<h3 data-id="heading-2">1. jQuery 对象.each(callback)</h3>
<p>使用该方法时需要在 each()中实现 function()方法，在 function()方法中可以进行赋参数，也可以不赋参数</p>
<p>首先我们来看不用赋予参数的一种，这种方法只能用于获取元素，而不能显示当前是第几个元素。</p>
<p>如下：</p>
<pre><code class="copyable">$(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")


            // 利用jQuery对象的each进行遍历
            // 利用this进行遍历
            citys.each(function () &#123;
                // alert(this.innerHTML);
                alert($(this).html());
            &#125;);


        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中的 this 表示：集合中的每一个元素对象</p>
<p>第二种是在 function()中赋予参数：</p>
<p>jquery 对象.each(function(index,element)&#123;&#125;);</p>
<p>*index:就是元素在集合中的索引</p>
<p>*element：就是集合中的每一个元素对象</p>
<p>利用这种方式可以回调函数返回值：如结束本次循环或结束整个循环吗，但是并不是使用 break，</p>
<p>在这里使用的是 return true/false</p>
<p>* false:如果当前 function 返回为 false，则结束循环(break)。</p>
<p>* true:如果当前 function 返回为 true，则结束本次循环，继续下次循环(continue)</p>
<p>实例代码：</p>
<pre><code class="copyable">$(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")


            // 利用jQuery对象的each进行遍历
            // 利用给function赋值获取对象文本
            citys.each(function (index,element) &#123;


                if ("上海" == $(element).html())&#123;
                    return true;    //结束本次循环
                &#125;
                // js方式
                // alert(index + ":" + element.innerHTML);
                // jQuery方式s
                alert(index + ":" + $(element).text());


            &#125;);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.$.each(object, [callback])</h3>
<p>使用这种方法和上面那种方法相似，只不过最前面不是 jQuery 对象了，而是一个 $符号,jQuery 对象被放到了 each()里面，但实现还是和上面一样的。</p>
<p>如下：</p>
<pre><code class="copyable"> $(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")


            // 利用$.each()方法
           $.each(citys, function () &#123;
                alert($(this).html());
            &#125;);


        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. for..of 方法</h3>
<p>这种方法是 jquery 3.0 版本之后提供的方式</p>
<p>语法格式是：for(元素对象 of 容器对象)</p>
<p>同样是容 ul 标签中取出 li 标签元素，代码如下：</p>
<pre><code class="copyable"> $(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")


            // 利用for---of的方式
            for (li of citys)&#123;
                alert($(li).html())
            &#125;


        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后附上面四种实现的完整源码。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="../js/jquery-3.3.1.min.js" type="text/javascript" charset="utf-8"></script>
    <script type="text/javascript">
        $(function (message) &#123;
            // 获取到UI下的所有Li标签
            var citys = $("#city li")
            // 利用js中的for循环进行遍历
            // 将获取到的li标签数组进行遍历
            for (var i = 0; i < citys.length; i++) &#123;
                 // 循环内容判断
                if ("上海" == citys[i].innerHTML)&#123;
                  // break;
                    continue;
                &#125;
                // 输出获取到的li标签中的内容
                alert(i + citys[i].innerHTML);
            &#125;


            // 利用jQuery对象的each进行遍历
            // 利用this进行遍历
/*            citys.each(function () &#123;
                // alert(this.innerHTML);
                alert($(this).html());
            &#125;);
            */
            // 利用给function赋值获取对象文本
            /*citys.each(function (index,element) &#123;


                if ("上海" == $(element).html())&#123;
                    return true;
                &#125;
                // js方式
                // alert(index + ":" + element.innerHTML);
                // jQuery方式s
                alert(index + ":" + $(element).text());


            &#125;);*/


            // 利用$.each()方法
           /* $.each(citys, function () &#123;
                alert($(this).html());
            &#125;);*/


            // 利用for---of的方式
/*            for (li of citys)&#123;
                alert($(li).html())
            &#125;*/
            
        &#125;);
        
    </script>
</head>
<body>
<ul id="city">
    <li>北京</li>
    <li>上海</li>
    <li>天津</li>
    <li>重庆</li>
</ul>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            