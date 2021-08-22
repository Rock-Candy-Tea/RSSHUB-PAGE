
---
title: 'WPF的通关之路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052d29cb5ddc437e99ab96efe21d8341~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 17:34:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052d29cb5ddc437e99ab96efe21d8341~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先说明两点，一是个人是业余爱好桌面开发(单纯以找工作去学客户端开发，这种行为不太推荐哦)，二是WPF的样式比Winform真的要好看很多（因为自定义的很自由）。</p>
<p>基本除了3D之类的图像和相关动画效果没有涵盖进去  其他的常用的基本都涵盖了在里面。</p>
<p>里面主要分类为基本控件、布局控件、视图控件、条目控件、其他UI（弄 的实际项目可用的界面），其实分类并不是很精准，只是便于区分而已。</p>
<h4 data-id="heading-0">部分截图：</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052d29cb5ddc437e99ab96efe21d8341~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da1750ffef774eefb7a0be32f7eb4bd8~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c376c53e583d4cffa1d3e716dc3fa34a~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4976073272ca4d60b3957a759ded9f3c~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c4662800ad4ccaa3effe11f9894eea~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c6268af45034d54adf00152791144a2~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a5e3086fb304a01a1da2c562f652b50~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">自定义的播放器：</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c26ba9a250144f5ba3c037012b30cda~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ps: 这播放基本的功能都实现了，没有清空列表的功能，页面缩放的自适应基本没问题。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Ften-ken%2FKen_WPF_UI" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/ten-ken/Ken_WPF_UI" ref="nofollow noopener noreferrer">源码：https://gitee.com/ten-ken/Ken_WPF_UI</a></p>
<blockquote>
<p>欢迎关注我的公众号：程序员ken，程序之路，让我们一起探索，共同进步。</p>
</blockquote></div>  
</div>
            