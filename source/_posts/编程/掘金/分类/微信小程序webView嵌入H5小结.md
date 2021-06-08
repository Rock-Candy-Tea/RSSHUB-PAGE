
---
title: '微信小程序webView嵌入H5小结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c840678589eb44b1ab357ea49efecbe6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:38:12 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c840678589eb44b1ab357ea49efecbe6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>tips:个人类型的小程序暂不支持web-viwe引用H5，同时需要在小程序管理后台配置H5的域名为业务域名</strong></p>
<h3 data-id="heading-0"><strong>1.直接引入页面地址；</strong></h3>
<p><code><web-view :src="url"></web-view> </code>
url为需要跳转的地址，可以用encodeURIComponent对url进行编码,小程序用decodeURIComponent解码，<br>url里面可以用?和&带参,小程序可以直接在onLoad中option接收参数;</p>
<h3 data-id="heading-1"><strong>2.小程序顶部设置透明；</strong></h3>
<h6 data-id="heading-2"><strong>web-view嵌入的H5页面不能设置透明，只能修改页面顶部的颜色;</strong></h6>
<ul>
<li>a.所有页面设置透明（在app.json里面的window增加navigationStyle:custom ,顶部导航栏就会消失,只保留右上角胶囊状的按钮）;</li>
<li>b.单独页面设置透明（在每个单独的json里面增加navigationStyle:custom）；</li>
</ul>
<h3 data-id="heading-3"><strong>3.小程序跳转到H5页面</strong></h3>
<p><strong>注意：使用redirectTo跳转到H5页面之后，所有嵌入的H5页面没有返回按钮，左侧只有一个返回首页按钮</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c840678589eb44b1ab357ea49efecbe6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4"><strong>4.H5跳转到小程序页面</strong></h3>
<p>需要引入<code><script type="text/javascript" src="https://res.wx.qq.com/open/js/jweixin-1.3.2.js"></script></code>才能用参数<br>
wx.miniProgram.switchTab(&#123; url:url&#125;); //跳转到小程序tabbar页，<strong>不能传参</strong><br>
wx.miniProgram.navigateTo(&#123; url:url,query:&#123;//填写参数&#125;&#125;);//跳转到小程序非tabbar页，<strong>可以传参</strong>
其他的跳转参考下图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b2c6d1e7ac48c09319957fa7508eff~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210608155307.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5"><strong>5.H5使用bindmessage向小程序传参</strong></h3>
<p>tips：<strong>使用bindmessage时只有用户点击了小程序的后退、分享按钮或者是小程序嵌入的H5页面销毁才能触发参数的传递，否则是不会触发。</strong></p>
<h3 data-id="heading-6"><strong>6.H5使用其他小程序的接口，可以参考API，因为我自己没有涉及到，所以给个链接给大家参考</strong></h3>
<p>参考链接：<a href="https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p></div>  
</div>
            