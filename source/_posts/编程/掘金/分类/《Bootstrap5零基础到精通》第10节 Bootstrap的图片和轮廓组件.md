
---
title: '《Bootstrap5零基础到精通》第10节 Bootstrap的图片和轮廓组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'pic/taohua.jpg'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 23:47:30 GMT
thumbnail: 'pic/taohua.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>《Bootstrap5零基础到精通》 俺老刘原创，争取每天更新一节。</p>
</blockquote>
<h1 data-id="heading-0">10.1 图片</h1>
<p>本文节将学习如何让图片支持响应式行为（这样它们就不会超出父元素的范围）以及如何通过类（class）添加些许样式。</p>
<h2 data-id="heading-1">10.1.1 响应式图片</h2>
<p>通过 Bootstrap 所提供的.img-fluid 类让图片支持响应式布局。其原理是将max-width: 100%; 和 height: auto; 赋予图片，以便随父元素一起缩放。</p>
<pre><code class="hljs language-js copyable" lang="js"><!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <link href="bootstrap5/bootstrap.min.css" rel="stylesheet">
    <title>图片演示</title>
  </head>
  <body>
        <div class="container">

            <img src="pic/taohua.jpg" class="img-fluid" alt="桃花朵朵开">

        </div>
   
     <script src="bootstrap5/bootstrap.bundle.min.js" ></script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面container是为了让图片居中显示切四周有边距，不是图像组件的一部分，下面是演示录像。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aac39abfa6a642e184ecd7c66b8ba911~tplv-k3u1fbpfcp-watermark.image" alt="10.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">10.1.2 图片缩略图</h2>
<p>除了通用类提供的提供的border-radius外，你还可以使用.img-thumbnail 使图片的外观具有 1px 宽度的圆形边框。</p>
<pre><code class="hljs language-js copyable" lang="js"><!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <link href="bootstrap5/bootstrap.min.css" rel="stylesheet">
    <style>
      .div1&#123;width: 300;  height: 300px;text-align: center;padding-top: 50px;&#125;
    </style>
    <title>图片演示</title>
  </head>
  <body>
            <div class="div1">
                 <img src="pic/taohua.jpg"  width="50%" class="img-thumbnail" alt="点击查看大图">
            </div>
   
     <script src="bootstrap5/bootstrap.bundle.min.js" ></script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个组件也是响应式的，不过我只给出了截图,上面css的样式是为了让图片不靠近边上，不要不可能看不到边框，其实直接使用container也一样，在此只是为了不使用container免得大家以为container也是其中一部分。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd898d4a5b39463b86c1469cd5103df6~tplv-k3u1fbpfcp-watermark.image" alt="Image 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">10.1.3 picture标签</h2>
<p>picture元素通过包含一个或多个source元素和一个img元素再结合media（媒体查询）来使用，
根据屏幕匹配的不同尺寸显示不同图片，如果没有匹配到或浏览器不支持 picture 属性则使用 img 元素，一个picture元素无论指定几个source，只会显示其中的一个或者img。</p>
<p>如果你使用  元素为某个 <code><img></code> 指定多个 <code><source></code> 元素的话，请确保将 .img-* 类添加到 <code><img></code> 元素而不是<code><picture></code> 元素或者source元素上。</p>
<p>source元素排列是有顺序的。媒体查询的值，如果是max-width，则从小到大排序；如果是min-width，则按从大到小的顺序排列。下面是源码，源码中js代码是获取屏幕宽度，作为对照。</p>
<pre><code class="hljs language-js copyable" lang="js"><!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <link href="bootstrap5/bootstrap.min.css" rel="stylesheet">
    <title>图片演示</title>
  </head>
  <body>
        <div class="container">
            <p>
                <span id="info"></span>
                <script>
                getwidth();
                window.onresize = function()&#123;
                    getwidth();
                &#125;
                function getwidth()&#123;
                document.getElementById("info").innerHTML="宽度："+document.documentElement.clientWidth+"，高度："+document.documentElement.clientHeight;
                &#125;
                </script>
                    </p>
            <picture>
                <source media="(max-width: 600px)" srcset="pic/girl1.jpg">
                <source media="(max-width: 700px)" srcset="pic/girl2.jpg">
                <img src="pic/taohua.jpg" class="img-thumbnail">
            </picture>

            <picture>
                <source media="(min-width: 700px)" srcset="pic/girl1.jpg">
                <source media="(min-width: 600px)" srcset="pic/girl2.jpg">
                <img src="pic/taohua.jpg" class="img-thumbnail">
            </picture>
        </div>
   
     <script src="bootstrap5/bootstrap.bundle.min.js" ></script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是演示</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1f571945f44dc48214b232bf06c39a~tplv-k3u1fbpfcp-watermark.image" alt="10.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">10.2 轮廓（Figures）</h1>
<p>通过 Bootstrap 的轮廓（figure）组件来显示相关联的图片和文本。任何时候需要显示一段内容（例如带有可选标题的图片），请使用<code> <figure></code>标签。</p>
<p>使用内置的.figure、.figure-img和.figure-caption类别，可提供HTML5 <code><figure></code>和<code><figcaption></code>标签一些基本样式设定。图片没有明确尺寸，请务必在<code><img></code>标签加上 .img-fluid类别设定为响应式图片。</p>
<p>事实上，轮廓组件不仅用于图片，在前一节文字排版部分，引用来源部分就已经使用了轮廓组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <link href="bootstrap5/bootstrap.min.css" rel="stylesheet">
    <title>figure演示</title>
  </head>
  <body>
        <div class="container">

            <figure class="figure">
                <img src="pic/taohua.jpg" class="figure-img img-fluid rounded" alt="...">
                <figcaption class="figure-caption text-center">桃花朵朵开</figcaption>
                </figure>
        </div>
   
     <script src="bootstrap5/bootstrap.bundle.min.js" ></script>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3a80c70fdd445a85bfd1f0fb13ba81~tplv-k3u1fbpfcp-watermark.image" alt="Image 2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单解释一下img标签里面的类rounded是图片四周为圆角，不需要可以不写。
figcaption标签里面的类text-center是图片居中对齐，还可以用text-end为右对齐，默认可以不写为左对齐。</p>
<p>今天的课程就到这里。<strong>请关注我</strong>，及时学习 俺老刘原创的《Bootstrap5零基础到精通》第11节 Bootstrap中的表格，表格的用处非常广泛，设计起来也比较麻烦，幸运的是借助bootstrap我们可以很轻松地做出好看的表格。</p>
<p><strong>如果这篇文章对你有帮助，记得随手点赞哦！</strong></p></div>  
</div>
            