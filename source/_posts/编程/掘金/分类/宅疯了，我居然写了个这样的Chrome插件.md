
---
title: '宅疯了，我居然写了个这样的Chrome插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87de8a64bcc4395b4dffc02fa24e61c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 04:29:19 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87de8a64bcc4395b4dffc02fa24e61c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">起因</h2>
<p>众所周知，在BilBil看宅舞对于我们男生来是一种无与伦比美妙的感觉。</p>
<p>然而很多人并不知道热心舞见小姐姐为什么有时候要配上竖屏版。</p>
<p>这时候有人会说：不是为了手机观看方便么。</p>
<p>那我就要说：No，No，No。</p>
<p>可能你们有些人还不知道当你有一个大寸又优秀的显示器，竖放播放着小姐姐的竖屏的宅舞视频时，
哪种感觉，OH MY GOD！就犹如舞见小姐姐亲自上门跳舞给你看一样。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d87de8a64bcc4395b4dffc02fa24e61c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>（截图出自bilbil视频 【聂俊桌面大公开！】）</p>
<p>可是在外漂泊打工那么久，每个月赚那点薄弱的工作，到现在都没钱给自己买个显示器，身边只有一台破笔记本，虽然公司有显示器配备给我们使用，但是身为腼腆又害羞的程序员又不好意思在公司里面用着竖屏看宅舞。</p>
<p>咋办捏，怎么用笔记本体验用竖屏看宅舞的快乐。对了要是bilbil有视频旋转功能不就解决了吗，但是我找了半天似乎没有这个功能。</p>
<p>怒了，这么重要的功能这个破站居然都没有，居然这个破站没有。身为一个前端工程师，这点小事情还能难到我不成！</p>
<h2 data-id="heading-1">开始解决</h2>
<ul>
<li>步骤一 打开有bilbil的竖屏宅舞视频</li>
</ul>
<p><img alt="WechatIMG281.jpeg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bfe6dad55ea446eb0e11d4a33ad9184~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>步骤二 打开Chrome开发者工具 找到video标签</li>
</ul>
<p><img alt="image-2.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f4a87e819d94f69a815db209e0d1544~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>步骤三 设置transform: rotate(-90deg);</li>
</ul>
<p><img alt="image-1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c1f66339a724fe4a6a0257d8519833e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>嗯嗯对了，就是这个样子，但是好像少了点什么。对了全屏，我要全屏。</p>
<ul>
<li>步骤四 在transform: rotate(-90deg) 后面再加 scale(2);</li>
</ul>
<p><img alt="2801617471999_.pic.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0797e4b03934bdd86112175ac054bdc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>哦吼吼～ 就是这个感觉。真是今生无悔入前端，就这么一句代码就能体验到这么纯粹的快乐。</p>
<p><img class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0350dbef24a4178b743db6e64afccd7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">分享</h2>
<p>快乐肯定不能只有我一个人独享，我按以上的方法把它做成了Chrome插件，大家有兴趣可以体验一下。</p>
<p>目前已经提交到Google应用商店，现在正在审核流程中。</p>
<p><img alt="WeChat156e2ef1d234ea65ac4d0c58a893f837.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1bff9bcb60d438192b7e74b47fafae3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我也把它放到了GitHub中，大家也可以直接下载下来体验。</p>
<p>在README.md中我已经写了具体的使用教程。</p>
<p><a href="https://github.com/Feng373712195/bilbil-verticalscreen-video" target="_blank" rel="nofollow noopener noreferrer">github.com/Feng3737121…</a></p>
<h2 data-id="heading-3">结束</h2>
<p>当然这只是一篇娱乐的文章，希望能博大家一乐。</p>
<p>希望大家在工作之余能发现更多生活的有趣的事情。</p>
<p>然后正是清明节假期，祝大家假期快乐，好好休息。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            