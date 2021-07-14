
---
title: 'Hbuilder X开发工具多端调试 配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72027e859d624e739d9530a2bec63faf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:55:10 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72027e859d624e739d9530a2bec63faf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>小程序开发中使用HbuilderX来书写代码，相对于使用微信开发者工具我们来讲一讲他们的区别，以及开发的效率</p>
<h5 data-id="heading-0">微信开发者工具</h5>
<p>微信开发者工具是将css，js，html分成了三个独立的文件在一个主体文件目录下</p>
<h5 data-id="heading-1">HbuilderX工具</h5>
<p>只有一个独立文件，这个独立文件分为了三个部分template，script，style，类似于vue的写法。当我们使用微信开发者工具打开我们的使用HbuilderX编写的代码，微信开发者工具将HbuilderX的代码模版，按他自己的规则进行转译，进行展示。HbuilderX还支持支付宝小程序，字节跳动小程序，华为小程序等多端小程序。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72027e859d624e739d9530a2bec63faf~tplv-k3u1fbpfcp-watermark.image" alt="1626254011(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们建立一个模块时，pages配置页面的路由会自动给我们生成，不需要我们手动去写当前新增页面的路由，提高了开发效率。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4744f30ab4364ddd93142ab90b667884~tplv-k3u1fbpfcp-watermark.image" alt="1626255385(4).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">使用浏览器调试</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8308935e2e7b4884bf9247fbdc4b5bbd~tplv-k3u1fbpfcp-watermark.image" alt="1626255772(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">HbuilderX   配置开启微信开发者工具</h4>
<p>第一步打开 工具 ---> 设置  --->  运行设置  --->  写入微信开发者工具安装的路径</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9d1efac069b4c03b76a9a9a2f781aa0~tplv-k3u1fbpfcp-watermark.image" alt="1626255385(3).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步 打开微信开发者工具  设置 ---> 安全 ---> 服务端口改为开启</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7c48b3151354322bc452c2c3a1e91f9~tplv-k3u1fbpfcp-watermark.image" alt="1626255385.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三步，在HbuilderX中使用微信开发者工具调试，直接选择 小程序模拟器</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb5817dd8aec4f438ff7b2b920c2db18~tplv-k3u1fbpfcp-watermark.image" alt="1626255916(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">配置真机调试</h4>
<p>第一步手机通过数据线连接到电脑<br>
在使用360助手检测当前电脑连接的手机
显示为以通过数据线进行了连接
直接在运行上选择真机调试即可
（这里我使用了360手机助手进行检测手机和电脑进行连接，连接上以后，选择在手机上运行时，会显示我们的手机型号，点击运行后会打包小程序，然后再我们手机上安装，安装完成后有一个HbuilderX的图标，每次再真机调试，都是打一个新的包安装到手机）</p>
<h4 data-id="heading-5">如果使用真机调试运行时，没有看到手机型号的选项，那就检查一下，使用360助手时，电脑和手机上是否都安装了并且开启了360手机助手</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/074ab7c1fd874e76943f2a7bbaf33dda~tplv-k3u1fbpfcp-watermark.image" alt="1626255385(2).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02036e911fc640e494328f95e3068964~tplv-k3u1fbpfcp-watermark.image" alt="1626255385(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            