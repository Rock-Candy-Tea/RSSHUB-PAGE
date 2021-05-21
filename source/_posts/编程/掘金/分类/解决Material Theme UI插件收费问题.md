
---
title: '解决Material Theme UI插件收费问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f8703b4a224ed09d71638f3c060781~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 06:34:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f8703b4a224ed09d71638f3c060781~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>webstorm 2021.1 版本更新后，一直使用的Material Theme UI主题开始收费了，如果不付费的话，文件树那里格外的小，看起来十分的难受。</p>
<p>在<a href="https://www.v2ex.com/t/769033" target="_blank" rel="nofollow noopener noreferrer">v2ex</a>上也看到有人讨论了这件事，在一个偶然的机会下，我找到了解决办法，本文就跟大家分享下这个方法，欢迎各位感兴趣的开发者阅读本文。</p>
<h2 data-id="heading-1">Material Theme UI介绍</h2>
<p>这是<strong>jetbrains</strong>公司旗下所有软件(webstorm、idea、datagrap等)都可以使用的一款主题插件，它有10几种主题可以选择，可以让你的编辑器看起来十分美观。</p>
<p>我用的是<strong>Atom One Dark Theme</strong>和<strong>Atom One Light Theme</strong>主题，分别对应的是夜间模式和白天模式，此处给大家展示下两种模式下的效果，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f8703b4a224ed09d71638f3c060781~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa64a07c5b5a40109677217315b82ebb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>上述效果图中除了使用了Material Theme UI插件外，我还安装了Atom Material lcons插件，这个是用于图标美化的。</p>
<p>大家可能还看到了效果图中还有git提交记录的显示，这里我安装的是GitToolBox插件，大家需要的话可以去webstorm的plugins选项下搜索安装。</p>
</blockquote>
<h2 data-id="heading-2">解决方案</h2>
<p>在Material Theme UI插件官网上找了下它的<a href="https://plugins.jetbrains.com/plugin/8006-material-theme-ui/versions/stable" target="_blank" rel="nofollow noopener noreferrer">历史版本</a>，都尝试了下，发现5.7.0版本是最后一个免费版本，且支持最新的webstorm。</p>
<h3 data-id="heading-3">下载安装包</h3>
<p>去它的版本记录中找到5.7.0或者直接点<a href="https://plugins.jetbrains.com/plugin/8006-material-theme-ui/versions/stable/109027" target="_blank" rel="nofollow noopener noreferrer">此处</a>进行下载，如下图所示，直接点<strong>Download</strong>按钮即可</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488cdb52b5c449068c66467e6e54c260~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">安装插件</h3>
<p>下载成功后，你会得到一个名为<strong>Material_Theme-5.7.0.zip</strong>的压缩包，打开webstorm的plugins面板，如下图所示。</p>
<p>按顺序点击，在弹出的选择文件窗口选择你刚下载的压缩包，安装成功后，重启webstorm即可。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b254cdac9e994fdda86a24b9d0a16340~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">写在最后</h2>
<p>至此，文章就分享完毕了。</p>
<p>我是<strong>神奇的程序员</strong>，一位前端开发工程师。</p>
<p>如果你对我感兴趣，请移步我的<a href="https://www.kaisir.cn/" target="_blank" rel="nofollow noopener noreferrer">个人网站</a>，进一步了解。</p>
<ul>
<li>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞和关注😊</li>
<li>本文首发于掘金，未经许可禁止转载💌</li>
</ul></div>  
</div>
            