
---
title: 'Windows安装MongoDB'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a9080b5066041a48131b90e58f9397a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:25:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a9080b5066041a48131b90e58f9397a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第30天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<ul>
<li>前段时间出了个<code>node</code>够用系列，在分享<code>「从零开始」前端node够用指北(五)⚡---连接数据库</code>之前我们需要安装一个数据库。</li>
<li>对于数据库可以选择<code>MySQL</code>和<code>MongoDB</code>，这里我们就用<code>MongoDB</code>演示。</li>
</ul>
<h2 data-id="heading-1">下载安装</h2>
<ul>
<li>我们一共需要下载两个东西，一个是数据库服务另一个是可视化界面</li>
</ul>
<h3 data-id="heading-2">数据库服务</h3>
<ul>
<li><code>MongoDB</code>的服务我们可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mongodb.com%2Ftry%2Fdownload%2Fcommunity" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mongodb.com/try/download/community" ref="nofollow noopener noreferrer">MongoDB官网</a>下载</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a9080b5066041a48131b90e58f9397a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>选择我们自己电脑的版本点击下载即可，随后我们会得到一个<code>msi</code>安装包直接双击使用。</li>
<li>前面同意之后点击自定义安装。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32a3a1e83faf42f2947a10bd8a20a8c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>记得选择自己存放的地址后下一步。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5844384e21ac4bd0ab0b9613a803ea0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>他接下来会帮我们自动生成这两个文件，先不用管他直接下一步。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2036a5ab21c2462d8325c27ead03072f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这个是问你要不要一起安装可视化界面，这里我们先不选等下再安装。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/464ddc8d98324302969a6c6f6fe2a3a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>最后安装后如果弹出警告不用理他直接忽略即可。</li>
<li>现在我们的<code>MongoDB</code>就安装好了。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8626a13d445e4f14a7516a5e17a54d07~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们可以看到这个文件夹里面是由<code>data</code>和<code>log</code>文件夹的，在老的版本中我们需要自己新增文件下，现在他帮我们下载好了但是我们还需要在<code>data</code>中新增一个<code>db</code>文件夹。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mkdir D:\mongoDB\data\db
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接下来我们进入<code>bin</code>目录执行<code>mongod -dbpath D:\mongoDB\data\db</code>,这个路径是你电脑存放<code>db</code>的路径。</li>
<li>这一步是为了开启数据库服务，只要我们需要用到数据库的时候这个命令窗口就不能关闭。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/683abb80c06b49ff87c2c8ada7179193~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接下来打开另一个终端窗口进入<code>bin</code>目录输入<code>mongo</code>,这样我们就可以正常使用<code>MongoDB</code>了。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96c3fb84446443fea6dcf375dce01881~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>我们打开<code>http://localhost:27017/</code>可以发现已经运行服务了！！！</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5751e52466574db28d887bbad25e7be5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">可视化界面</h3>
<ul>
<li>当然为了以后方便操作，我们可以下载一个可视化界面<code>MongoDB Compass</code>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mongodb.com%2Ftry%2Fdownload%2Fcompass" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mongodb.com/try/download/compass" ref="nofollow noopener noreferrer">MongoDB Compass</a>里面提供了下载方式。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bd9217ba0c640e2abb0dc46d9988a66~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>下载后是一个压缩包直接解压就可以使用了，双击<code>MongoDBCompass.exe</code>即可。</li>
<li>进去之后直接点击连接就可以啦~，我们的<code>MongoDB</code>就安装完成了。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d231788fe6a549528ffe8bcb40781527~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a665b2dbca944f5b1980aafe4231759~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">👋 写在最后</h2>
<ul>
<li>这次简单分享了一下<code>MongoDB</code>的下载安装，希望可以帮助到有需要的同学。</li>
<li>如果您觉得这篇文章有帮助到您的的话不妨<strong>🍉关注+点赞+收藏+评论+转发🍉</strong>支持一下哟~~😛您的支持就是我更新的最大动力。</li>
</ul>
<h2 data-id="heading-5">🌅 往期精彩</h2>
<p><a href="https://juejin.cn/post/7001779766852321287" target="_blank" title="https://juejin.cn/post/7001779766852321287">一个"剑气"加载🌪️</a></p>
<p><a href="https://juejin.cn/post/7000652451435003918" target="_blank" title="https://juejin.cn/post/7000652451435003918">一个"水"按钮💧</a></p>
<p><a href="https://juejin.cn/post/7000300247947673630" target="_blank" title="https://juejin.cn/post/7000300247947673630">产品经理：你能不能让词云动起来？</a></p>
<p><a href="https://juejin.cn/post/6997978246839042079" target="_blank" title="https://juejin.cn/post/6997978246839042079">一文搞定echarts地图轮播高亮⚡</a></p></div>  
</div>
            