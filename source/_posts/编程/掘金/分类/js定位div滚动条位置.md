
---
title: 'js定位div滚动条位置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://upload-images.jianshu.io/upload_images/2500256-302e9a9bb00a094d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:25:07 GMT
thumbnail: 'https://upload-images.jianshu.io/upload_images/2500256-302e9a9bb00a094d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>如图：<img src="https://upload-images.jianshu.io/upload_images/2500256-302e9a9bb00a094d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1.找到需要定位元素的位置，已Y轴为例，使用offsetTop找到距离父元素顶部的距离。
2.使用scrollTop属性使其父元素滚动到相应的位置，看下列代码。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function dw()&#123;
      let [parentDoc,childDoc]= [document.querySelector('#fjd'),document.querySelector('.zjd')];
parentDoc.scrollTop = childDoc.offsetTop - parentDoc.offsetHeight /2 ; //如果大于div高度使其居中
      childDoc.style.background = 'red'
    &#125;
</script>
</head>
<body>
<button onclick="dw()">定位<button>
<div id="fjd" style="height:100px;overflow:auto;width: 200px;">
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div  >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div class="zjd" >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div>
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
        <div >
          找到了
        </div>
   </div>

</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对你有帮助的话点关注，不定时更新js有趣小知识。</p></div>  
</div>
            