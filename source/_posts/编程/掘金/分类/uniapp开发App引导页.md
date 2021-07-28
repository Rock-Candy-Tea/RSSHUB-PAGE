
---
title: 'uniapp开发App引导页'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=399'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 08:34:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=399'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>App的引导页是当用户第一次打开一款App时所展示的3-5精美的图片，用于告知用户产品的功能及特点。好的引导页会促使用户对产品增加更多的兴趣，当然这是UI设计的能力体现了，尽管很多人都会快速的滑过。对于开发人员怎么去添加这几张图片只有在用户第一次打开app时展示呢。</p>
<h5 data-id="heading-0">其实原理很简单，在本地设置标识flag，默认为false，从而进入引导页，进入之后，flag设置为true，下次进入自然不会展示的；当然这个引导页可以设置为一个页面，用轮播图放置几张引导页；只要不清除本地的flag缓存，则引导页只会出现一次；</h5>
<p>以uniapp开发的项目为例：在onLaunch函数中，检查flag是否为false，如果为false,则跳转到引导页面，在引导页中可设置跳转到首页。注意，最好用reLaunch，避免，用户物理按键返回；为true，则存储flag到本地。原理既是如此；但是实际开发时，会发现，存在闪屏现象，这样用户的体验就不太好，所以比较关键的地方就在于这块，还是以uniapp为例，需要在uniapp的源码视图下将splashscreen的设置进行修改，将autoclose改为false，在onLaunch中通过设置延迟时间调用plus.navigator.closeSplashscreen方法来关闭启动图。delay设置为0。这样启动图的设置就ok了。<br>
以下封装了检查是否进入引导页的方法，仅供参考下：</p>
<pre><code class="copyable">guidePage()&#123;
    try &#123;
         // 获取本地存储中launchFlag标识
         console.log(uni.getStorageSync('first_flag'))
         if(!uni.getStorageSync('first_flag'))&#123;//第一次进入app,为false
            // 进入引导页
            uni.reLaunch(&#123;
                url:'/pages/GuidePage/GuidePage',
            &#125;)
        &#125;
    &#125; catch(e) &#123; //error
        // 设置为true
        uni.setStorageSync('first_flag', true);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Tip:在多次的应用中发现，如果在手机本身比较卡的情况下，用户在第一次开启app时，还是会存在首页在引导页之前出现，这种情况的处理方式是将引导页默认设置为主页，即在路由管理中，将引导页写在第一个，然后通过flag去判断是否跳转到首页；<br>
以上的引导页开发只是提供一种思路，还有很多其他的方式，比如后端去控制是否展示引导页，引导页的动态变化。当然问题本身不难实现，关键在于实际应用时所存在的问题。</p></div>  
</div>
            