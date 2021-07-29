
---
title: 'uniapp开发小程序时主包内存受限之分包解决'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2314ea270bf74b949f911c10e495608a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 20:54:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2314ea270bf74b949f911c10e495608a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一.分包</h1>
<h2 data-id="heading-1">分包（何为分包）</h2>
<p>分包——无疑就是将主包的内存大小进行分包，优化前端性能，提高项目的运行速度
具体分包详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fframework%2Fsubpackages%2Fbasic.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/basic.html" ref="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p>
<p>好了，前面我们了解了分包的相关知识之后呢，接下来我们开始分析项目是否需要分包</p>
<h1 data-id="heading-2">项目分析是否需要分包（主包大小是否超过微信内存大小的限制）</h1>
<h3 data-id="heading-3">1.如何判断是否超出限制</h3>
<p>出现以下这种报错则主包内存大小超出微信小程序的限制大小
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2314ea270bf74b949f911c10e495608a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2.分析原因</h3>
<p>1.打开详情——点击查看详情——点击代码依赖分析——结果如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b269ecbf1df447088863e4e9f8e36883~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
2.此刻我们需要分析主包内存超出限制大小的原因，分析结果造成内存超出限制大小的原因主要有以下几点</p>
<ul>
<li>pages包过大</li>
<li>本地静态资源占据一定的内存空间</li>
</ul>
<h2 data-id="heading-5">- 引入的外部的UI框架造成内存溢出</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0368139a3bf4ec880b3f63419817bc2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">解决方案</h3>
<p>（1）将pages包进行分包处理，将一些文件抽取到其他文件夹中，同是文件中使用到对应文件的路径也要随之改变（如下，pagesB就是我从pages文件下分出来的分包，此刻很明显发现主包内存明显减少了）
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0226e80d644a60a9fb2a17adaf6e71~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
（2）此刻我们的分包已经基本完成了，但总体项目主包的大小还是超出了限制要求，因此继续分析原因是
（3）不难发现，本地静态资源也占据了主包一定的内存空间，因此我们可以考虑将本地静态资源丢到服务器上去，然后通过http的形式使用服务器上的图片资源，这样可以减少主包的内存大小（具体如何丢，详见最后）
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b01e20efca964738a88d78f2e7adfb4d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此刻我们已经很明显发现存放静态资源的内存已经略有减少了（注意，将本地资源存放到服务器之后，项目中所有用到的资源路径必须全部修改成服务器上的资源，否则数据会丢失）</p>
<p>（4）此刻我们发现主包的内存还是超出微信内存的大小限制，继续分析项目，此刻发现引入的外部的UI框架也会造成内存溢出(我这里的项目引入的UI框架是uView，并且是全局引入)
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33da046d33bc404ab062ffc2dbec4a56~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时我们可以将外部的UI框架从全局引入改成按需引入，即可减少主包一些没必要的内存</p>
<p><strong>综上便是uniapp开发小程序时主包内存大小限制之分包的解决方案（如果主包的内存不是超出很多的话，可以考虑在uniapp开发工具中使用发行——小程序-微信，之后再去微信开发者工具查看项目中主包的内存，你会发现主包的内存会少很多）</strong></p>
<h2 data-id="heading-7">《备》如何将本地的静态资源丢到服务器上去</h2>
<ol>
<li>首先要先下载本地资源上传到服务器上的一个软件———Xftp</li>
</ol>
<p>下载路径：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jb51.net%2Fsofts%2F732920.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jb51.net/softs/732920.html" ref="nofollow noopener noreferrer">www.jb51.net/softs/73292…</a></p>
<ol start="2">
<li>
<p>启动xftp软件，链接服务器</p>
</li>
<li>
<p>将本地静态资源上传到服务器对应存放静态资源的文件夹下</p>
</li>
<li>
<p>在项目中使用http:............的形式使用服务器上的资源</p>
</li>
</ol>
<p><strong>以上便是将本地的静态资源丢到服务器上去的基本操作</strong></p></div>  
</div>
            