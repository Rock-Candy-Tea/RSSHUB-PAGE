
---
title: 'node.js实现一个"图片压缩到指定目录"的小工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c14183eba0b4b2ca744d19816b83c95~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 23:53:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c14183eba0b4b2ca744d19816b83c95~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第26天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">背景</h1>
<p>项目里面经常需要将某个图片压缩到对应目录下，基本上都是使用网站<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftinypng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tinypng.com/" ref="nofollow noopener noreferrer">tiny-png</a>来实现。</p>
<p>但是这里有一个问题，就是每次都得反复的操作文件来将图片从一个目录移到另一个目录，非常的不方便，所以就萌生了一个想法，我能不能实现一个小工具，一条命令直接图片压缩并移到指定目录呢；</p>
<p>于是，就有个这个项目。</p>
<p>下面讲一下详细的实现步骤</p>
<h1 data-id="heading-1">项目准备，tinify库</h1>
<p>在查找合适的图片压缩包时，我发现了tinify,即tiny-png官方给出的一个图片压缩包。这个是将图片传到tiny-png的服务器上，然后再将压缩后的图片返回给我们；</p>
<h2 data-id="heading-2">如何使用tinify</h2>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-number">1</span> <span class="hljs-keyword">const</span> tinify = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tinify"</span>);
<span class="hljs-number">2</span> tinify.key = <span class="hljs-string">"467Kbym9jl55NmS54HcK54Cr5wCP"</span>; <span class="hljs-comment">// 这个是假的</span>
<span class="hljs-number">3</span> tinify.fromBuffer().toBuffer()
...
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>第一行，就是一个包的引入，没什么问题;</li>
<li>第二行，是tiny-png官方给出的一个key密钥，因为本质上我们还是使用的他们的服务，所以需要在tiny-png官网注册，然后拿到一个密钥</li>
<li>第三行，就是一个图片压缩的核心代码</li>
</ol>
<p>1⃣️点击这里登陆
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c14183eba0b4b2ca744d19816b83c95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2⃣️点这里生成一个key</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bddc5573a124e56bfe3ce82715cfe55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">实现思路</h1>
<ol>
<li>读文件，将所有的png格式图片读取出来。</li>
<li>通过tinify将图片压缩</li>
<li>将压缩的图片写入目标目录</li>
</ol>
<p>所以，上面三个步骤我们可以看出，需要一个源目录将图片读出来，然后一个目标目录将图片写进去，这个通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/minimist" ref="nofollow noopener noreferrer">minimist</a>库来实现。</p>
<p>具体node实现命令工具的方法，可以参考我之前写的<a href="https://juejin.cn/post/6976493789905059871" target="_blank" title="https://juejin.cn/post/6976493789905059871">从0开始，用node实现一个命令行工具</a></p>
<h1 data-id="heading-4">总结</h1>
<p>代码我就不放出来了，思路大概就是这样。这个npm包已经传到了npmjs.com，大家感兴趣的话可以自行体验<br>
名字是：<strong>compress-pngs</strong></p></div>  
</div>
            