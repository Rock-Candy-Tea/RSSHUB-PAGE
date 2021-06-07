
---
title: 'DOM对象中的常用属性（innerHTML属性，innerText属性，className属性，style属性）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b342fca6b64912845ca542e9290873~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 00:22:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b342fca6b64912845ca542e9290873~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">innerHTML属性</h1>
<blockquote>
<p><strong>innerHTML 属性：用于设置或获取 HTML 元素中的内容。</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
<p>
    <span>这是一个段落</span>
</p>

<script>
    let obj = document.getElementById('one'); 
    console.log(obj.innerHTML);                  
    obj.innerHTML = '<span>hello world!</span>';  
</script>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b342fca6b64912845ca542e9290873~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">innerText属性</h1>
<blockquote>
<p><strong>innerText 属性：用于设置或获取 HTML 元素中的纯文本。</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
<p>
    <span>这是一个段落</span>
</p>

<script>
    let obj = document.getElementById('one');
    console.log(obj.innerText);    
    obj.innerText = 'hello world!'; 
</script>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2d742320034884b43b565e1124bc72~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">className属性</h1>
<blockquote>
<p><strong>className 属性：用于设置或获取 DOM 对象的类样式。</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
<div></div>

<script>
    let obj = document.getElementById('one');
    console.log(obj.className);                
    obj.className = 'two';
console.log(obj.className);                
</script>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ae0075b24ef4bd0ae2ab4df99b5ff9e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">style属性</h1>
<blockquote>
<p><strong>style 属性：用于设置或获取 DOM 对象的 style 样式。</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
<div>这是一个div</div>

<script>
    let obj = document.getElementById('one'); 
    obj.style.width = '500px';                
    obj.style.height = '300px';
    obj.style.backgroundColor = 'gray';
    obj.style.fontSize = '20px';
    obj.style.color = '#fff';
    obj.style.border = 'solid 5px red';
    obj.style.display = 'block';          
</script>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c0c14e5bb3240f7b8bb8f28d588b8c7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>写作不易，读完如果对你有帮助，感谢点赞支持！<br>
如果你是电脑端，看见右下角的 “一键三连” 了吗，没错点它 [哈哈]</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2046ec74fbc4cbda5e331c36a504c1a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>加油！</strong></p>
<p><strong>共同努力！</strong></p>
<p><strong>Keafmd</strong></p></div>  
</div>
            