
---
title: '理解node.js中的buffer'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6742'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 08:20:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6742'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么node.js中要引入buffer</h2>
<h3 data-id="heading-1">buffer的英文释义</h3>
<p>buffer在英文中是缓冲，缓存的意思，从这个意思中可以初步获悉引入buffer是为了在node服务器上面做缓冲的。</p>
<h3 data-id="heading-2">node服务器在什么场景需要缓冲</h3>
<p>既然node是用于服务器，那就需要应对网络请求（net，http），操作文件系统(fs，readline)，处理图片，文件的上传与下载等场景。node选中了js，同时需要V8引擎来执行js，强大的V8引擎难道不能胜任了吗？</p>
<h3 data-id="heading-3">V8的限制</h3>
<p>为什么V8会有限制呢？V8的诞生是用于chrome浏览器的，浏览器用于呈现网页；对于网页的展示，V8设计时在64位操作系统下使用内存约为1.4G，32操作系统下约为0.7G内存，这样的内存大小对于网页的展示是足够的，但是对于服务器端的使用就会捉襟见肘。</p>
<h3 data-id="heading-4">node底层C++来分配内存</h3>
<p>既然V8限制了内存的使用，node底层使用C++来分配内存，确实可以获取到更大的内存，但是老子曰：道可道，非常道，名可名，非常名；同理分配的内存有大小，就会有被占满，阻塞，继而服务缓慢，甚至崩溃。</p>
<h2 data-id="heading-5">缓冲区buffer怎么处理上述场景的问题</h2>
<h3 data-id="heading-6">火星移民</h3>
<p>想象这个场景，需要将地球（C盘）上10亿生物（英文字符，汉字，阿拉伯文字等）转移到火星（D盘），我们在地球和火星之间建立了可容纳1千万生物的空间站（内存）；如果10亿生物同时进入空间站，将是一场灾难（崩溃）；地球的航天飞船（缓冲区buffer）有1000个位置（字节）来运载生物到空间站；然后去火星的航天飞船（缓存区buffer）有1000个位置（字节），再运载生物到火星。</p>
<h3 data-id="heading-7">概念提取</h3>
<ul>
<li><code>Buffer:</code> 用于表示固定长度的字节序列，好比：固定1000个位置的飞船</li>
<li><code>UTF-8:</code>是一种变长的编码方式。它可以使用1~4个字节表示一个符号，根据不同的符号而变化字节长度。好比：飞船会规定英文生物占用1个位置，汉字生物占用2个或者3个，4个位置</li>
</ul></div>  
</div>
            