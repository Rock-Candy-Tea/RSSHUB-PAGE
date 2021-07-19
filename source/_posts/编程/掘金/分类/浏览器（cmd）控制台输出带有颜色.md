
---
title: '浏览器（cmd）控制台输出带有颜色'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdc97915ffc942ce9e8379199e8750c8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 05:59:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdc97915ffc942ce9e8379199e8750c8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>一般在浏览器中看到人家打印的带有颜色，所以咋也来实现一下。如下：</p>
</blockquote>
<h2 data-id="heading-0">效果</h2>
<h2 data-id="heading-1">在浏览器的效果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdc97915ffc942ce9e8379199e8750c8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">使用方式</h2>
<pre><code class="copyable">console.log('\x1B[3m%s\x1B[23m', 'italic')
console.log('\x1B[1m%s\x1B[22m', 'bold')

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">在cmd里面的效果</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2db39d3847dc4e5b87dfe1601cb6fd9a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">使用方式</h2>
<pre><code class="copyable">console.log('\x1B[3m%s\x1B[23m', 'italic')
console.log('\x1B[1m%s\x1B[22m', 'bold')

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">一些常用的<code>颜色</code>代码</h2>
<pre><code class="copyable">    'bold'          : ['\x1B[1m%s\x1B[22m'],
    'italic'        : ['\x1B[3m%s\x1B[23m'],
    'underline'     : ['\x1B[4m%s\x1B[24m'],
    'inverse'       : ['\x1B[7m%s\x1B[27m'],
    'strikethrough' : ['\x1B[9m%s\x1B[29m'],
    'white'         : ['\x1B[37m%s\x1B[39m'],
    'grey'          : ['\x1B[90m%s\x1B[39m'],
    'black'         : ['\x1B[30m%s\x1B[39m'],
    'blue'          : ['\x1B[34m%s\x1B[39m'],
    'cyan'          : ['\x1B[36m%s\x1B[39m'],
    'green'         : ['\x1B[32m%s\x1B[39m'],
    'magenta'       : ['\x1B[35m%s\x1B[39m'],
    'red'           : ['\x1B[31m%s\x1B[39m'],
    'yellow'        : ['\x1B[33m%s\x1B[39m'],
    'whiteBG'       : ['\x1B[47m%s\x1B[49m'],
    'greyBG'        : ['\x1B[100m%s\x1B[49m'],
    'blackBG'       : ['\x1B[40m%s\x1B[49m'],
    'blueBG'        : ['\x1B[44m%s\x1B[49m'],
    'cyanBG'        : ['\x1B[46m%s\x1B[49m'],
    'greenBG'       : ['\x1B[42m%s\x1B[49m'],
    'magentaBG'     : ['\x1B[45m%s\x1B[49m'],
    'redBG'         : ['\x1B[41m%s\x1B[49m'],
    'yellowBG'      : ['\x1B[43m%s\x1B[49m']
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>本文使用 <a href="https://juejin.cn/post/6940875049587097631" target="_blank" title="https://juejin.cn/post/6940875049587097631">文章同步助手</a> 同步</p>
</blockquote></div>  
</div>
            