
---
title: '电商技术总结之SpringCloud+SpringBoot+mybatis+uniapp 前后端分离 b2b2c o2o 微服务商城电商之直播带货模块设计分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ce2141c6c454a4682a7d7a37ee4e8ce~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:57:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ce2141c6c454a4682a7d7a37ee4e8ce~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>近期我参与了公司电子商务平台中“海播”模块设计，其中包括直播、短视频带货两个模块，下面介绍一下直播带货模块：</strong></p>
<h1 data-id="heading-0"><strong>业务流程如下</strong></h1>
<p>第一步：商家以“商家入驻”模式入驻电子商务平台后，对自己的店铺进行装修、发布商品等操作（具体会在后面商家详情里面进行讲解）。</p>
<p>第二步：商家对商品设置分销，商家在发布商品的时候，设置商品分销比例，如：一个杯子标价为120元，其中拿出20元进行分销设计，其中14元钱设置为一级分销，剩下的6元钱设置为二级分销。</p>
<p>第三步：如果用户在平台上进行直播带货，首先要开通直播服务，如：上传真实资料，购买主播服务（不是所有人都可以进行免费直播）。</p>
<p>第四步：主播提交资料后，后台进行严格审核后方可直播。</p>
<p>第五步： 成为主播后，主播可以打开主播端，可直接进行直播，如：创建直播间、分享直播间、创建预播、可以去平台选择自己要带的货（商品），数据统计等。</p>
<h1 data-id="heading-1"><strong>平台、技术、架构、设计思想</strong></h1>
<p><strong>涉及平台</strong></p>
<p>平台管理、商家端（PC端、手机端）、买家平台（H5/公众号商城、小程序商城、APP端（IOS/Android）、微服务平台（业务服务）、系统服务（SpringCloud相关：Eureka、Config、Gateway）</p>
<p><strong>核心架构</strong></p>
<p>Spring Cloud、Spring Boot、Mybatis、Redis、RabbitMQ、</p>
<p><strong>前端框架</strong></p>
<p>VUE、Uniapp、Bootstrap/H5/CSS3、IOS、Android、小程序</p>
<p><strong>核心思想</strong></p>
<p>分布式、微服务、云架构、模块化、原子化、热插拔</p>
<p><strong>开发模式</strong></p>
<p>前后端分离、微服务开发、持续集成、集群部署、前后端分离、支持阿里Docker</p>
<h1 data-id="heading-2"><strong>创建直播间介绍</strong></h1>
<p>进入主播端，点击“创建直播”，进入创建直播界面，添加直播间封面、直播标题、添加宝贝（商品），如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ce2141c6c454a4682a7d7a37ee4e8ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bc03d191c4746588b8c466d9886af9e~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c2b5d57e7c4415a9349e0892c2bb0e2~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc8cbcffa719492ea1ab3b87ed26f455~tplv-k3u1fbpfcp-watermark.image" alt="4.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6df4c292b8f495b925fe0c09e25eb57~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9836e9ff89154fa6a6f9865dc95ba2ab~tplv-k3u1fbpfcp-watermark.image" alt="6.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3"><strong>前端直播列表（C端观看）</strong></h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96788dde03be4e998fc1bf332e083b02~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72016b91275b4281ad3d14aba932fc9f~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4"><strong>后台管理截图</strong></h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78295168828a49dfa0c3ea386d0866a6~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ad47ceae1ce4e51ae49532c8e6e95ea~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            