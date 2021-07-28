
---
title: '前端经典圣杯布局和双飞翼布局(适用于pc端)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e7e24470ea544ceaa4c078dd909bbcd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 02:14:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e7e24470ea544ceaa4c078dd909bbcd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">介绍</h2>
<p>圣杯布局和双飞翼布局解决的问题是一样的
<strong>就是两边顶宽，中间自适应的三栏布局，中间栏要在放在文档流前面以优先渲染。</strong></p>
<p>圣杯布局和双飞翼布局解决问题的方案在前一半是相同的，也就是三栏全部float浮动，但左右两栏加上负margin让其跟中间栏div并排，以形成三栏布局。</p>
<h2 data-id="heading-1">区别</h2>
<p>不同在于解决”中间栏div内容不被遮挡“问题的思路不一样：
<strong>圣杯布局</strong>，为了中间div内容不被遮挡，将中间div设置了左右padding-left和padding-right后，将左右两个div用相对布局position: relative并分别配合right和left属性，以便左右两栏div移动后不遮挡中间div。</p>
<p><strong>双飞翼布局</strong>，为了中间div内容不被遮挡，直接在中间div内部创建子div用于放置内容，在该子div里用margin-left和margin-right为左右两栏div留出位置。
多了1个div，少用大致4个css属性（圣杯布局中间divpadding-left和padding-right这2个属性，加上左右两个div用相对布局position: relative及对应的right和left共4个属性，一共6个；而双飞翼布局子div里用margin-left和margin-right共2个属性，6-2=4），个人感觉比圣杯布局思路更直接和简洁一点。</p>
<h2 data-id="heading-2">简单而言</h2>
<p>简单说起来就是”双飞翼布局比圣杯布局多创建了一个div，但不用相对布局了“，而不是你题目中说的”去掉relative"就是双飞翼布局“。
效果演示</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e7e24470ea544ceaa4c078dd909bbcd~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210728181359.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>对比图</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bbf421ddcad4d70ad086dacbf86b6ae~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
废话不多说直接上代码</p>
<h2 data-id="heading-3"><strong>圣杯布局：</strong></h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #hd &#123;
            height: 50px;
            background: #666;
            text-align: center;
        &#125;

        #bd &#123;
            /*左右栏通过添加负的margin放到正确的位置了，此段代码是为了摆正中间栏的位置*/
            padding: 0 200px 0 180px;
            height: 100px;
        &#125;

        #middle &#123;
            float: left;
            width: 100%;
            /*左栏上去到第一行*/
            height: 100px;
            background: blue;
        &#125;

        #left &#123;
            float: left;
            width: 180px;
            height: 100px;
            margin-left: -100%;
            background: #0c9;
            /*中间栏的位置摆正之后，左栏的位置也相应右移，通过相对定位的left恢复到正确位置*/
            position: relative;
            left: -180px;
        &#125;

        #right &#123;
            float: left;
            width: 200px;
            height: 100px;
            margin-left: -200px;
            background: #0c9;
            /*中间栏的位置摆正之后，右栏的位置也相应左移，通过相对定位的right恢复到正确位置*/
            position: relative;
            right: -200px;
        &#125;

        #footer &#123;
            height: 50px;
            background: #666;
            text-align: center;
        &#125;
    </style>
</head>

<body>
    <div id="hd">header</div>
    <div id="bd">
        <div id="middle">middle</div>
        <div id="left">left</div>
        <div id="right">right</div>
    </div>
    <div id="footer">footer</div>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">双飞翼布局</h1>
<p>代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #hd&#123;
    height:50px;
    background: #666;
    text-align: center;
&#125;
#middle&#123;
    float:left;
    width:100%;/*左栏上去到第一行*/     
    height:100px;
    background:blue;
&#125;
#left&#123;
    float:left;
    width:180px;
    height:100px;
    margin-left:-100%;
    background:#0c9;
&#125;
#right&#123;
    float:left;
    width:200px;
    height:100px;
    margin-left:-200px;
    background:#0c9;
&#125;

/*给内部div添加margin，把内容放到中间栏，其实整个背景还是100%*/ 
#inside&#123;
    margin:0 200px 0 180px;
    height:100px;
&#125;
#footer&#123;  
   clear:both; /*记得清楚浮动*/  
   height:50px;     
   background: #666;    
   text-align: center; 
&#125; 
    </style>
</head>
<body>
    <div id="hd">header</div> 
  <div id="middle">
    <div id="inside">middle</div>
  </div>
  <div id="left">left</div>
  <div id="right">right</div>
  <div id="footer">footer</div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            