
---
title: 'uni-app系列（一）：安装开发工具 HBuilderx 并创建 uniapp 项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6d576c012b4689bdbf5858ba761f4a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 16:16:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6d576c012b4689bdbf5858ba761f4a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">📖摘要</h2>
<p><code>心态好了，就没那么累了。心情好了，所见皆是明媚风景。</code></p>
<blockquote>
<p><strong><code>“一时解决不了的问题，那就利用这个契机，看清自己的局限性，对自己进行一场拨乱反正。”正如老话所说，一念放下，万般自在。如果你正被烦心事扰乱心神，不妨学会断舍离。断掉胡思乱想，社区垃圾情绪，离开负面能量。心态好了，就没那么累了。心情好了，所见皆是明媚风景。</code></strong></p>
</blockquote>
<blockquote>
<p><strong>今天分享下 —— <code>uni-app</code>系列（一）：安装开发工具 的一些基本知识，欢迎关注！</strong></p>
</blockquote>
<p><strong>欢迎阅读，总结系列：<a href="https://juejin.cn/column/7000630716681682980" target="_blank" title="https://juejin.cn/column/7000630716681682980">野蛮生长的 uni-app 学习之路</a></strong></p>
<hr>
<h3 data-id="heading-1">🌂安装 <code>HBuilderx</code></h3>
<p><strong><code>uni-app</code> 是一个用 <code>vue</code> 语法来开发小程序、App、H5 的框架，其官方推荐的开发工具为 <code>HBuilderX</code> ，使用起来有很好的开发体验。 <code>HBuilderX</code> 是官方力荐并长期维护的开发工具很好使哦！</strong></p>
<p><strong>官方推荐的：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.dcloud.io%2Fhbuilderx.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.dcloud.io/hbuilderx.html" ref="nofollow noopener noreferrer">www.dcloud.io/hbuilderx.h…</a></strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6d576c012b4689bdbf5858ba761f4a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>因为是uni-app开发，所以我们这里下载安装App开发版：（下载完成直接解压找到 <code>HBuilderx.exe</code> 启动即可）</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/460ffca5320f4e4497d65ec88d8ed769~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>安装后如下退图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e303abf42b843728f1a5d5a83456d81~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-2">🌂用 <code>HBuilderx</code> 创建 <code>uniapp</code> 项目</h3>
<p><strong>如下所示点击：文件 --> 新建 --> 项目</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38f456f46b684b3899351e39211eeea2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>选择创建 <code>uni-app</code> 项目，填入项目名称和存储路径，模板可以选择自行尝试：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4733cc573b3f48ab9235f5f7d62cc387~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>到这里简单的安装和创建 <code>uniapp</code> 项目就结束了，快去试试吧！</strong></p>
<p><strong>最后感谢大家耐心观看完毕，原创不易，六个点赞收藏是您对我最大的鼓励！</strong></p>
<hr>
<h3 data-id="heading-3">🎉总结：</h3>
<ul>
<li>
<p><strong>更多参考精彩博文请看这里：<a href="https://juejin.cn/user/862483929905639/posts" title="https://juejin.cn/user/862483929905639/posts" target="_blank">《陈永佳的博客》</a></strong></p>
</li>
<li>
<p><strong>喜欢博主的小伙伴可以加个关注、点个赞哦，持续更新嘿嘿！</strong></p>
</li>
</ul></div>  
</div>
            