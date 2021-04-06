
---
title: '【本文可抽奖】爽！uniapp加uniCloud前后端一站式开发！记一个互动抽奖助手的诞生！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa66ea8110c24cb2a83adcadde5971fb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 02:29:55 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa66ea8110c24cb2a83adcadde5971fb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><em>这是一篇流水账式的技术分享</em></p>
<h1 data-id="heading-0">前言</h1>
<p>我在B站看到有UP主在玩<code>互动抽奖</code>，我也想用这个功能。但是B站只给大UP主开，而我要开启这个功能还不知道要猴年马月。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa66ea8110c24cb2a83adcadde5971fb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>身为一个老程序猿嘛，不给我开那就自己做一个吧~也不是啥麻烦的事！</p>
<h1 data-id="heading-1">B站官方互动抽奖的优缺点</h1>
<h2 data-id="heading-2">缺点</h2>
<p>B站官方这个互动抽奖的限制挺多，比如每月之内使用一次，玩法也单一。就是参与然后等待。</p>
<h2 data-id="heading-3">优点</h2>
<p>官方的嘛，入口更加直接。利用站内信通知这些机制更加完整</p>
<h1 data-id="heading-4">我设计的互动抽奖优缺点</h1>
<h2 data-id="heading-5">缺点</h2>
<p>入口差一点，得自己分享网址，并且B站还很讨厌的让简介和评论里的网址不可直接点击。</p>
<h2 data-id="heading-6">优点</h2>
<ul>
<li>除了支持B站，我也支持咱掘金社区呀</li>
<li>定制化的抽奖互动，比如按点赞数开奖，按播放数开奖等都可以自定义</li>
<li>公平公正公开，抽奖的逻辑代码已开源</li>
</ul>
<h1 data-id="heading-7">说干就干吧</h1>
<p>思考了一个多礼拜，花了两天来做前后端开发，目前版本<code>0.5 beta</code>吧。抽奖部分的功能都完成了，但暂时没做用户自己发布抽奖活动，暂时不做有几个重要的考量：</p>
<ul>
<li>用户自己发布，就得做用户登录注册</li>
<li>要发布就要可以修改，如果可以修改，如何保证参与抽奖者的权益。</li>
<li>相同文章或视频的抽奖活动，要不要验证是作者才可以发起抽奖。</li>
</ul>
<p>截图展示1：
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b303407ebf1445dac180deaef09fefe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>截图展示2：
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f1227da538b4708a32902b55a94dc0e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>截图展示3：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83a3521f08654cb786b5f7457216ee26~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">HBuilderX+uniCloud一站式开发</h1>
<h2 data-id="heading-9">uniCloud</h2>
<p>uniCloud云开发背后的服务商可以自由选用阿里云或者腾讯云，阿里云尤其大气，目前是全免费的，最多可以创建50个空间。腾讯云只能创建1个免费空间。但如果是发行微信小程序的话，由于是腾讯云的环境，在做登录授权解密等操作时，使用腾讯云会更简单一些。</p>
<h2 data-id="heading-10">uniapp</h2>
<p>不用多介绍了，vue系最强跨端框架...大厂估计不太用，但二三线城市的小外包公司大部分靠它养活。</p>
<h2 data-id="heading-11">HBuilderX</h2>
<p>这货其实一点不比VSCode差，vue的代码提示部分甚至超过VSCode。并且在支持了uniCloud后，你可以在HBuilderX里一键发行网页，阿里云还包含免费的静态网页托管服务。自带免费CDN....</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df9803755534fc598bc0c3d104255c4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在HBuilderX里，你写完前端写后端，开发时连接本地云函数。完成后上传云函数以及公共模块。然后一键将网页发布到前端网页托管服务里。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dc77e7eed8d4a978037e24f5825a43d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b8bdb0fca5d484eaaf4d3dd6e6352b1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ceb082a09d548fb9ab3b35b0b1f2967~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>无须域名，无须自建服务器，完全免费，你的项目就这样可以发行了。</p>
<h1 data-id="heading-12">抽奖吧！抽奖吧！</h1>
<p><a href="https://www.bilibili.com/video/BV1A5411A7jP/" target="_blank" rel="nofollow noopener noreferrer"><img alt="Snipaste_2021-04-05_17-45-15.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39a1623d95043748f7ceadb936cae6a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a>
这个B站视频里可以抽一个掘金官方周边鼠标垫</p>
<hr>
<p>本文也开启了互动抽奖，奖品是掘金搪瓷茶缸子一个</p>
<p><a href="http://luckyfans.jnsii.com/detail?id=606bc8e349586100016ea4f8" target="_blank" rel="nofollow noopener noreferrer">luckyfans.jnsii.com/detail?id=6…</a></p>
<p>参与规则：
先评论，然后点赞，当点赞数达到200时，从评论区随机抽取1名用户获奖，获奖者必须关注作者，否则不予发奖</p>
<p>大家快试试自己的<code>欧气</code>吧</p>
<h1 data-id="heading-13">最后</h1>
<p>谢谢掘金，谢谢掘金的<code>张哥们</code> @优弧 @船长 ...奖品都是写文章得的~都送出去之后，我要再多得一些。：P</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            