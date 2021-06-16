
---
title: 'Flutter项目实战：我是从这些方面去提高开发效率的(持续更新)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/144e9387804046cea6553597acddf67d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 02:01:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/144e9387804046cea6553597acddf67d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>各位大佬，好久不见！</p>
<p>不摸鱼的程序员不是好程序员，所以今天和大家分享一些提高Flutter开发效率的小技巧。当然，各位大佬肯定也有更好更多的方法，请不吝赐教，多多留言。</p>
<h2 data-id="heading-1">Tips</h2>
<h3 data-id="heading-2">组件库</h3>
<p>程序员不反复造轮子，所以，在开发过程中，要有意识的去做自己的组件库，比如通用的ui组件，工具类，网络层的封装等。这样长时间的累积，会让你的开发效率越来越高。</p>
<p>在组件封装过程中，不一定要一次封装完美，只要能满足现有需求，且适当考虑后期的扩展就可以了，以后可以逐步迭代。组件库可以放本地，也可以远端仓库。远程仓库，如果在开发中经常迭代调式，可以在开发过程中把pubspec.ymal先改为本地引用，方便开发过程中的调试。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/144e9387804046cea6553597acddf67d~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">开发者调试信息</h3>
<p>为了方便App的测试，通常会在开发过程中，做一个开发者中心。我在项目中就只做了一个服务器的切换，以及网络数据抓包的配置。各位还可以根据自己的情况，去不断丰富，比如实现一个网络拦截器，记录网络错误日志等，方便bug回溯。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df832beeb2c34540b8058c94128ab4d5~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG59.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">自动生成路由表</h3>
<p>我们的项目中，每一个页面都需要去路由表中注册，为了统一路由的注册，所以通过build_runner和注解，实现了路由表的自动生成。开发只需要在需要生成路由的页面加上注解就可以了。路由参数和路由注释可选</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da252540bf14a6db9904ad5c43954f6~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG60.png" loading="lazy" referrerpolicy="no-referrer">
下面是自动生成的路由表片段：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14ce7645a07b421fadc323293a50ab6c~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG61.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">利用脚本生成页面骨架</h3>
<p>在项目中，页面的基础骨架都类似，为了不每一次创建页面都写相似的东西，所以，用python写了一个脚本去自动生成页面骨架。操作如下:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eb3b5fad6f24c73a6c248271d3767c0~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG62.png" loading="lazy" referrerpolicy="no-referrer">
按照引导输入和选择，就自动生成了不同类型的页面骨架。这里需要说明的是，我在项目中封装了scaffold，网络加载状态(请求中、请求失败、请求成功、空数据等)的样式都在scaffold中</p>
<h3 data-id="heading-6">批量处理图片资源</h3>
<p>ui资源从蓝湖下载后，每次都需要删除图片名称中的倍图标识，然后再拖入项目中对应的资源目录，这个过程极其繁琐，所以也是搞了个脚本来批量处理这些图片，只需要把下载的图片放到指定文件夹，执行脚本就可以了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ab3e50777424f74863261454419479b~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG63.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">待更新。。。</h3>
<h1 data-id="heading-8">端午快乐！！！</h1></div>  
</div>
            