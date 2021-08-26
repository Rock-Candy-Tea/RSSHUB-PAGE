
---
title: 'overflow_ hidden隐藏溢出内容的几种情况'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25fe8b2a116425f9bf242846251f680~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:14:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25fe8b2a116425f9bf242846251f680~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">什么是溢出</h4>
<p>当使用DIV+CSS布局时，会出现很多的div嵌套——父div内嵌套一个或多个的子div。默认情况下，父div的高度是auto——它可以被子div任意的撑大。然而父div也可以有固定的高度(或宽度)，比如height:100px，那么如果子div的高度超过了这个值，在默认情况下，子div会超出父div的束缚，这就是溢出。我们可以通过设置父div的CSS属性——overflow来对子div进行控制。这里使用<code>overflow:hidden</code>来隐藏子元素溢出的部分。</p>
<h4 data-id="heading-1">父元素高度确定</h4>
<p>父元素高度确定时，设置overflow: hidden，会隐藏子元素超出父元素宽高的内容，且被隐藏的元素不占位。</p>
<pre><code class="copyable"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        #father&#123;
            width: 50px;
            height: 50px;
            overflow: hidden;
        &#125;
        #son&#123;
            width: 100px;
            height: 100px;
            background-color: darksalmon;
        &#125;
    </style>
</head>
<body>
    <div id="father">
        <div id="son">我的宽度是100px</div>
    </div>
    <p>检测占位</p>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25fe8b2a116425f9bf242846251f680~tplv-k3u1fbpfcp-watermark.image" alt="WX20210825-101221.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">父元素高度不确定</h4>
<p>如文章开头所说，父元素高度为auto，默认情况下，子元素会超出父元素的束缚。但是如果设置了定位，可能导致不同的情况。</p>
<p>我们先来看下面一段代码：</p>
<pre><code class="copyable"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        #father&#123;
            overflow: hidden;
        &#125;
        #son&#123;
            position: absolute;
            width: 100px;
            height: 100px;
            background-color: darksalmon;
        &#125;
    </style>
</head>
<body>
    <div id="father">
        <div id="son">我的宽度是100px</div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看表现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c6cc67d6f604c11b54e36ab7734df30~tplv-k3u1fbpfcp-watermark.image" alt="企业微信20210825-101107.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然，子元素溢出的内容并没有被隐藏。原因是给子元素设置了绝对定位。绝对定位元素相对的元素是它最近的一个祖先，<strong>该祖先必须满足：position的值必须是：relative、absolute、fixed</strong>，若没有这样的祖先则相对于body进行定位。因此，子元素此时相对于body定位，溢出内容不会被隐藏。</p>
<p>我们再来看下面一段代码：</p>
<pre><code class="copyable"><html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        #father&#123;
            position: relative;
            overflow: hidden;
        &#125;
        #son&#123;
            position: absolute;
            width: 100px;
            height: 100px;
            background-color: darksalmon;
        &#125;
    </style>
</head>
<body>
    <div id="father">
        <div id="son">我的宽度是100px</div>
    </div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器打开HTML文件，可以看到页面上一片空白😨！！！原因是：子元素脱离了文档流，父元素并没有被撑开——此时父元素高度为0。且子元素相对于父元素定位，此时设置<code>overflow: hidden</code>... ...so，子元素被完全隐藏了。</p>
<p>因此，如果想要达到子元素定位为absolute，溢出内容被隐藏的效果，需要给父元素设置宽高，且定位设置为relative/absolute，读者可自行尝试。</p></div>  
</div>
            