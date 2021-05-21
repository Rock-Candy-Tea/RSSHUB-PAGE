
---
title: '今天聊：腾讯 IVWeb 的组件即服务 - CAAS 实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 19:50:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十七届|前端 Flutter 专场，了解 Web 渲染引擎|UI 框架|性能优化，6-5 下午直播，6 位讲师(淘宝/京东/闲鱼等)，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十六届 - 前端早早聊组件化专场，也是早早聊第 113 场，来自腾讯 - Vincent 的分享。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dc4356018a54527af733fdb5a2948a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家好，非常高兴今天能为大家做一个技术分享，今天我要分享的是如何实践组件即服务这样的一个议题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f89d1b9cac488492d882723294cc99~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">自我介绍</h2>
<p>首先做一下个人介绍，我是 Vincent，毕业于华南理工大学，目前是在腾讯的 IVWEB 团队工作，我们在业务上主要是做一些直播相关的产品，围绕着业务我们也对性能、效率等方面开展各类技术探索。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6184916463cf4275ab685e74f5ccb518~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天我们要聊的是组件即服务，也就是所谓的 components as a service，简称为 CaaS。今天的分享会分以下 4 个部分：</p>
<ol>
<li>首先是阐述一下这个方案的应用场景，因为其实不同的方案会有自己的适用范围，我们需要明确能够发挥它优点的实际场景是什么样的。</li>
<li>第二个是今天分享的重点，就是我们在实践这样一个方案的时候，比如说在技术选型和我们在路上踩过的一些坑，这些经验跟大家交流一下，让大家遇到类似的场景的时候，可以思考应该怎样去做。</li>
<li>第三点就是给大家展示一下这样一个方案在我们的业务中所实践的一个效果。</li>
<li>最后是总结，给大家回顾一下整个方案的情况。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94236f6940044e28b08d21c8486fd78~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">一、应用场景</h2>
<p>第一个应用场景的部分。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84d39bb55ed043fc818a84c98549cab0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">前端页面复杂性的演变</h4>
<p>首先我们来思考一下，前端发展了这么多年，今天的前端与过去有什么不同。在我看来，前端页面已经不再是以前那种比较简单的 UI 呈现，而是会包含很多背后的逻辑。这里演化的重要原因是现在的产品设计，也不像以前那么原始，比如说产品经理可能拍个脑袋，他觉得这个页面应该怎么做我们就怎么做。现在的产品设计上会更加的科学，更加的讲究工业化，也就是说会有很多更有逻辑和科学的方式来决定我们的产品最终呈现应该是什么样子。</p>
<p>而产品设计上的进步，就会导致前端页面，你看到的跟它背后所包含的内容会很不一样，其实我们看到的只是其中很少的一个部分。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ebe762c17b243399304a697c8200382~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">页面的复杂性- ABTest</h4>
<p>页面的复杂性在今天为什么会变得越来越高了。有个非常典型的例子就是 ABTest，在我们的业务中，这两年 ABTest 运用得非常的广泛。所谓 ABTest，对于页面中 UI、交互，或者是产品逻辑，通过做对比实验的方式，开发不同的组件，然后再投放到真实的用户中，最后分析每个用户最终的数据上报，来确定说方案是不是更优的。在做 ABTest 的时候就会引入一个问题，我们的页面里面它所包含的组件会越来越多，比如说一个页面我们分了几个模块，每个模块都可以做实验，而每个模块都有两个实验，一个是对照组，一个是实验组。那么通过排列组合的话，可能就会有几十种页面呈现的结果，这正是导致页面复杂性指数级增加的一个点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90d8242f16054584b3f0ff1134b8ae6e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">页面的复杂性-跨平台</h4>
<p>另外一点是在我们的业务里面会存在很多跨平台的场景，比如说我们同样一个页面可能要投放很多不同的平台，常见的例子是在安卓和 iOS 上，它们之间可能会有些微的差异。另外就是像我们如果要投放微信和 QQ，因为它的客户端环境不一样，我们经常会需要调用一些客户端的能力，客户端的宿主环境不一样，那么它的客户端接口就会存在一些差异，这些也是我们需要在代码里兼容的一些地方。所以这种跨平台性也就进一步的增加了我们整个页面的复杂性。结合上面的两种，我们知道今天我们所看到的页面跟它所包含的复杂性是不成正比的，有很多页面的复杂度已经到了非常夸张的程度，与此同时我们在开发这些页面的时候，还需要充分考虑他们的性能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89f5f3c0620b4f849ec940e20bfbc7b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">页面性能优化-SSR</h4>
<p>在性能优化领域有一个非常重要的手段，就是通过服务端渲染的方式去提升性能。对于服务端渲染跟客户端渲染这两种方式，服务端渲染它的优势在于第一个是首屏渲染性能会更高，这里面的原因有很多，包括在服务器上去请求后台的数据要比用户从他的浏览器里发出请求，网络链路会更短，那么在获取数据这一块可能就会更快。</p>
<p>另外一点是服务端渲染本身也可以通过一些缓存的方式，可以让它的渲染性能要比客户端渲染的效率要更高。服务端渲染还有一个很明显的优势，就是它对于 SEO 会更友好，因为服务端渲染所得到的结果就是一个可以直接展示的 HTML 的片段。那么对于搜索引擎来说，它的爬虫去抓取那些关键的信息，会更有优势一些。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/def84dabf0164396af2cefbc42450f8a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>言归正传，经过上述分析，今天我们要考虑的是一方面我们的页面会变得越来越复杂，另外一方面我们需要兼顾它的性能，不能让这种复杂性拖了页面的性能。图上更形象的展示这个场景，页面所包含的组件会越来越多，但是更夸张的是除了它展示出来的组件，其实它背后很多没有展示出来的组件也非常的多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87c853af6b6041f7a99c171f4ee51cd4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">待解决问题</h4>
<p>我们要解决这样上面的问题，我们可以抽象出来其实就是三个点：</p>
<p>第一个点是要保证组件的隔离，也就是说每一个组件尽量把它拆出来，每一个前端工作者其实在面对这种复杂页面的时候，都很自然的会选择的一种方式，就是去拆组件，把组件拆到一个单独的地方，然后更好的去开发和维护，这是一个非常通用的做法，所以第一点是我们要保证组件的独立开发的隔离性。</p>
<p>第二个是动态性，其实一个页面到底要展示什么组件，这个是在运行的时候才能决定的。如果用传统的方式把所有展示的组件都一起打包到一个页面上，那么这个页面就变得非常的冗余繁杂，所以我们要做到可以实现动态加载、按需加载的这样一个能力。</p>
<p>第三点就是前面提到的性能优化，我们希望我们的组件本身就可以支持服务端渲染，再结合其他的性能优化手段，可以让我们的整个首屏渲染的性能得到更大的提升。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/282c39bcf87d48a39690b2c6603e8e4b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了解决这样的一个问题，我们团队就有一个思考，<strong>能否让整个组件去实现服务化</strong>。特别是今天我们知道像云函数、Serverless 等概念也非常的热门，结合 Serverless 的能力，我们把我们的组件直接搬上了 Serverless 运行，组件其实可以理解成是一个微型的服务端渲染的页面，然后我们的主页面在向这些云函数请求组件渲染的结果，将这些渲染结果展示出来，这样的话就可以做到更细粒度的组件级别的服务端渲染，并且每个组件都可以相对的隔离。</p>
<p>通过云函数的方式去实现服务部署有个好处，对于前端来说，我们不太需要去关心部署运维的事情了，在一般场景中运维成本是整个 CI/CD 环节的这些比较繁琐的事情，都可以通过云函数方式去简化，这便是整个方案的初衷。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1ebfa6680345a4abe556da5ec39060~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">二、方案设计与演进</h2>
<p>第二个部分给大家介绍一下整个方案的设计跟演进的过程。给大家阐述一下，我们在遇到不同问题的时候，可能会有很多技术选型，具体是怎么样选，最后怎么样得到一个最终方案的过程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebdc63eccc584278ba30dcb3dcb9e72b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">动态加载-BigPipe</h4>
<p>第一点是关于动态加载，动态加载我们是使用了 BigPipe，简单介绍一下 BigPipe 就是由 Facebook 提出的一种提高网页加载速度的方案，它包含两个环节， 第一是对网页进行分块，称之为 PageLet，这个是非常通用的一个做法。分块之后，对它进行静态交付。具体是什么样的一个过程我们可以看一下示例。</p>
<p>首先是类似于骨架屏的概念，现在大家都不陌生了。我们的页面会有一个基础的占位图，这个是静态的，可以在第一时间就可以返回给用户，可以减少用户这样一个等待渲染的时间，可以对用户体验会更好一些。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb85d722422c4f0197ea2ab0beaaf178~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们基于 BigPipe 的做法是当我们的用户从浏览器发起请求到服务器的时候，我们首先直接将静态的骨架屏的 HTML 直接返回，那么用户就可以在最短的时间内看到一个基本的结果，然后再通过服务器向组件的服务发起请求。在组件服务渲染结束之后再分段，哪个组件渲染完，哪个组件就可以先返回，然后逐步的渲染到用户的一个页面上，这就是一个基本的方案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1842a3bf084ff6bf36f1e30b2c140a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">页面切块</h4>
<p>那么在这个思路的指引下，我们就做了两个事情，第一个事情是页面的分块，这个事情其实就是通过骨架屏的方式，我们首先对页面把组件抽离出来，不管是需要展示的，还是不需要展示的，都将其独立出来，作为一个单独的仓库单独去维护，这样对于我们开发维护的成本也可以降到更低。</p>
<p>另外一点就是在部署的时候，就像前面说的，我们将其直接部署到 Serverless 上，这样对于开发者来说，就不太需要去关心它的部署、维护运维等等这些繁琐的这种服务端的这些工作。然后对于主页面，主页面我们是把它理解成一个<strong>基座</strong>，在这个基座上面，一方面是你可以正常的开发，包括有一些组件可能并不需要服务端渲染，它本身是一个相对来说不依赖数据，可以直接展示的部分，我们完全可以直接在以非服务端渲染的方式去开发，然后再需要服务端渲染这些要动态组件的时候，再通过一个 SDK 去动态的引入，将其渲染。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f9cb34e2e94963b099f5c1bcd6486b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">按需引入</h4>
<p>按需引入其实会有不同的诉求，比如说第一种诉求就是直接渲染非常简单，我需要渲染什么组件，我就声明什么组件，然后将其渲染出来。</p>
<p>这里面可以看到，每一个组件服务都是有自己特定的名称，相当于是一个名字服务，可以通过这个名称去寻址，找到它所对应的 Serverless 的函数，然后拿到结果之后<strong>直接渲染</strong>出来；第二种方式也可以这样进行，通过 <strong>JSX</strong> 的方式直接插入到我们原本的页面中，利用 CSR 方式去渲染；第三个<strong>懒加载</strong>，像 React 本身就有 React.lazy 这样一个懒加载能力，我们可以将我们这些组件服务拉回来的结果，也就是渲染的结果，以懒加载的方式去渲染到页面上，它会在组件没有拉回来的时候，展示一个 loading 的状态，在拉回来之后会把组件的渲染结果展示出来。通过这种方式，我们解决的是一部分组件在运行时加载的一个能力：第一时间将骨架屏的静态的时间表先展示，然后再通过主 JS 向我们的组件服务去发起请求，去拉取组件的渲染结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec5b07cac5c54f1693b4993cc27125ed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">组件异步</h4>
<p>前面我们提到除了要解决组件本身的动态性和隔离性，第二个我们还需要关注的是组件的性能问题，正是因为这一点，所以我们没有直接使用社区的一些现有的动态引入方案。因为很多人可能会有疑问，像 React 的社区，本身提供了可以动态去引导一个组件的能力，它可以在你打包的时候，不把组件直接打包到你的主页面，而是在你运行的时候再将其他引入进来，但是有个问题，这本身的方案是不支持服务端渲染的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1052894f6ea24412a02a72db934d8ffe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们把这套方案直接放到服务器上去执行的话，就会抛出异常。React 官方文章里面也有声明，这种方式不支持服务端渲染。所以如果我们需要使用服务端渲染，React 也给了一个社区方案，我们也去尝试了社区的这个叫 Loadable components 的库，然而这种方式并没有达到我们的要求。主要原因是它的服务端渲染并不是彻底的，它最终只是渲染了 loading 的部分。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a63297bead504e7b983bda1450aa452f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看这个官方代码片段。在这个代码片段里面，我们在服务端部署中，它真正渲染的其实只是 loading 式的服务端渲染，而对于组件本身其实还是需要通过客户端去执行一下，所以并不彻底。</p>
<p>当然有人会想到另一个思路，我们可不可以在构建的时候将组件的依赖进行搜集？在服务端渲染的时候，通过 FS 也就是通过文件系统在服务器上去读取组件的代码，然后再这样执行去渲染出来。</p>
<p>这种方式其实就是 Next.js 所采用的一种方式。我们这里面也尝试了一下，这里给出了示例代码，下面简单介绍一下这块代码的具体做的事情：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d37855aafda84894bdc638a3509dee4a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里面我写了一个判断条件，这个是模拟一个 ABTest 的场景，因为我们知道 ABTest <strong>一般来说就是需要去判断用户操作如果符合特定条件的话</strong>，<strong>它就会渲染上面的所谓的 white card</strong>，<strong>如果不符合就是渲染 black card</strong>，这就是一个非常典型的 ABTest 的场景。</p>
<p>在这种条件下，如果它是 true 的话，它是可以动态去加载 white card 组件，而且 white card 组件是可以支持服务端渲染的，如果它为 false 的话，它就可以动态去加载 black card 组件，看起来这种方案是符合我们之前所设想的，第一点它是可以去动态的去拉取，第二点它可以支持服务端渲染。</p>
<p>但是并没有想的那么美好，因为这里面隐含了一个小小的问题。我们可以看到 if 这个部分，我们这里面是为了演示写成 1 > 0.5，我们可以看到这是一个同步代码，也就是说它执行的时候是同步的，但是我们知道在 ABTest 里面，往往我们得选择使用什么策略渲染是异步的，比如说这里面可以是发起一个请求，if 发起一个请求，到 ABTest 的中心服务，然后经过相应的算法，将用户根据一些条件分到不同的实验组对照组等等，之后会把结果返回给页面，页面再去决定它渲染上面的 white card 还是 black card。而在 NEXT.js 这种模式下，如果本身就是一个异步再套异步的话，这种方式就会失败。因为这种异步套异步的场景在 ABTest 里面非常的典型，所以这个方案也不能够完全满足我们的需要。我们对比了这几种方案之后，我们最终决定使用这样一个方式。</p>
<p>我们可以看一下这样一个时序图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18335806550447a9bdca388fc83a6f0f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">CaaS BigPipe SSR 时序图</h4>
<p>从用户这一端请求的时候，指向一个云服务，云服务其实可以理解成服务端渲染的页面服务，但这里面我们可以去做一些逻辑的处理，比如说可以有一个 ABTest 的逻辑的处理，也可以是前面讲的跨平台的逻辑处理等等，那么这里面处理完之后最终会得到一个结果，就是我需要渲染什么组件，然后再向云函数上的一些组件服务发请求，这些组件服务会向各自的后台接口去发起请求。可以看到的是像云服务，云函数，后台接口这些，因为都是走的内网，内部网络肯定访问速度要比从用户客户端直接发起请求去查询后台接口要快的。</p>
<p>这里面云服务其实第一时间已经把骨架屏返还，用户可以第一时间去得到骨架屏的现场结果。然后云函数的那些组件，在渲染结束之后就会逐步的去返回给用户，用户的页面上就会逐步的去呈现这些组件的内容。</p>
<p>我们可以看到像这种方式，为什么说在性能上更优有几个点：第一个就是前面提到的，在内网进出接口要比从客户端经过漫长的网络抵达内网的接口要快。另外一点就是它有这种分块返回的能力，哪一个组件先确认完就可以先返回，可以先展示，就不需要像传统的服务端渲染一样，需要等到所有的组件渲染结束之后再统一返回。另外还有一个点就是分块开始，因为我们知道像服务端渲染本身是可以有缓存的，但是这种缓存能力是基于整个页面为粒度的。比如说我们这样一个页面，我们直接去用服务端渲染缓存的话，它的缓存命中率其实是很差的。因为大部分情况下它的缓存都没有用。</p>
<p>这个页面非常典型，上面是一个相对固定的一个组件，就是指主播当前直播状态已经结束了，基本上是不太会变了。除非主播可能换个头像或者昵称可能会变一下，频率会比较低，它的缓存其实就很有价值，因为大部分时间都是有效的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e2f7a335bff44a884e7b0f1d95a44b5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面这一部分叫“大家都在看”，其实它展示的是最近比较热门的这些主播的信息，这个是经常会刷新的。如果你去缓存下面这部分的组件内容的话，其实就没有太大意义，反而会造成用户体验的一个下滑，因为用户会先看到一个老的这样的结果，然后会闪一下，再渲染到最新正确的这样结果上，这样体验会更差。而我们通过 CaaS 的方式，可以在上面这一块组件缓存，那么它所展示的缓存命中率基本上都是有效的，下面这一块经常变动的部分我们就可以不缓存，这样的话整个页面的缓存粒度可以做到组件级别，会比传统的这种页面级别来的更有意义一些。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd828ef6e5014668b2e7ebb15329e572~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">链路调用</h4>
<p>当然通过这种方式之后，我们的整个请求和链路会变得更长更复杂。比如我们中间会有很多环节，要考虑到整个服务的稳定性的话，需要对每一个链路进行监控。我们可以利用云函数本身的监控，这就看你所选择的云厂商的一个能力了。但是根据实际的业务情况，我们也可以考虑把云服务和云函数这一块进行整合，也就是你的服务端渲染服务进行整合。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02afb4deea944a889c6a6d8a035d1e25~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的好处就是减少一层链路，你在中间的错误也好，包括网络访问的速度也会有些许的提升。所以这需要根据你实际业务情况来去做一个判断，当然判断的基本逻辑就是云函数上的组件服务是否被复用。如果你的复用情况特别的多，比如说某一个组件用的特别多，每一个页面可能都会用到，那我是更建议将其独立部署到一个地方。如果复用率并不是那么高的话，会更建议直接将其整合到云服务里面去，来降低整个方案的复杂性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e2b0d2e44e4b9c9d25aaf670a47f7c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外一点就是我们需要考虑服务降级的情况，因为服务本身有可能有稳定性的问题，比如说流量突然增加或者是服务异常等等，那么我们也是有这样的方式的，当我们发现整个请求超时或者说失败的话，我们会将其转发到常规的 CDN 的这样一个路径上，就是正常的 HTML、JS、CSS 这样一个请求的方式，然后由客户端去渲染。这种方式它虽然效率会低一些会慢一些，但是它能够保证整个页面的正常打开，所以这会有一个服务降级的方案去规避异常的情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97668abcfd8148d08b31b85b9d7d98b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">组件冲突</h4>
<p>我们在做了这些事情之后，还有一个需要考虑的事情是组件是有可能会出现冲突的。这里面需要考虑主要是三个点：</p>
<p>第一个点是我们的 JS 需要隔离，特别是当你的 JS 如果有用到一些全局的能力的时候，或者组件代码对全局有副作用的时候，不同的组件如果互相影响的话，那么可能会超出设计的预期。</p>
<p>另外一个是 CSS 的隔离， CSS 隔离简单来说是样式污染，避免不同组件之间写的相同的样式，造成互相覆盖这种情况。现在的隔离其实比较简单，有很多方式，我们采用的是 CSS Modules 的方式，其实就是会自动的给 CSS 的标签做一个命名上的差异，来避免不同的组件，它的样式是相同的。还有一些其实业界也还有一些其他的实践，在很多微前端的方案里面也都会有提及，这里就不再展开去讲。</p>
<p>第三个就是组件依赖共享的问题，可以想到一个问题，比如说组件 A 依赖了一个库，组件 B 也依赖这个库，如果组件 A 打包一份基础库，组件 B 也打包一份基础库，那么最终我们页面就会重复加载很多这种基础库，所以我们需要解决这样一个问题，让这种公用的依赖提取出来。而对于不公用的依赖才打包到组件本身，后面我会去单独讲讲这两个 JS 隔离跟组件依赖的一个解决方案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f78bf2337af4fc889cc32149681aadf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">沙箱</h4>
<p>JS 隔离主要是有一个叫沙箱的概念，就是给你的每个组件去创建一个独立的环境，来隔离你跟其他组件之间的一个关系。同时还有一点要注意副作用的清除，像一些定时器，组件 A 的定时器跟组件 B 的定时器不能互相影响。这里面其实也有很多种方式，主要都是在微前端领域，都普遍会涉及到一个要点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76c6402406764c259e974aacfab2058c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>沙箱其实有两大类，第一类就是所谓的单例模式，你页面中其实会只有一个沙箱，所有东西都是在沙箱里面去完成的。而第二种就是多例的模式，就是你每个组件会有一个自己的沙箱，通过多沙箱的方式来实现。这两个方式分别怎么做的，有多种方式，这里面只是给大家抛砖引玉，其实具体要看实际的业务场景来决定。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/993c253a76be469eb8bfa5d04e429f2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一种是闭包的方式，简单来说，通过函数作用域，在全局最外层去包一个函数，这个函数来创建一个隔离的作用域，它可以把你 window 对象传进来之后，这样去赋予一个值，这样的方式就会使得在这个函数作用域里面，它的 window 跟外界真正全局的 window 是隔离的。</p>
<p>当然有人会问一个问题，假设我在函数的作用域里面（就是组件在某个沙箱里面），它需要用到比如说 windows 中 location 能力的时候，又该怎么办呢？有这两种思路：第一种思路就是你可以自己去模拟实现，通过编码去模拟这些浏览器的一些基本的能力，当然这种就比较复杂，你可以想象自己写代码去实现这种原本就有的基础能力，工作量会很大。第二种取巧的方式就是可以在里面去 new 一个 iframe，用了 iframe 之后，然后将你在组件里面的 window 就挂到 iframe 的里面去，这是一个很取巧的方式。这种取巧的方式只需几行代码，就可以获得一个完整的全局 window 的能力。当然它也有一些小问题，就是要避免出现跨域的情况，总而言之闭包是一大类的解决方式。</p>
<p>第二类就是快照，即前面讲的单例这种方式，我们可以在全局只有一个沙箱，但是每个组件在使用这些全局能力的时候，你需要在使用结束之后保存现场，这样就清理还原成原始的状态，然后给另一个组件用，另一个组件用完，当你这个组件需要用的时候，再这样还原。这里面会有很多这种切换现场的代码，也是一种方式。还有像代理的方式也是也是可以考虑的。目前我们现在也在探索这一块，其实怎么样做更好，这一块还没有一个最终完全确定的方式，各有各的优点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f284024a31c47ba8d776fd4c1eeeea3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下一个是关于怎么样解决组件依赖共享的问题。前面讲到的如果我多个组件依赖同样一个库，比如说大部分情况下，我的组件可能都依赖于 React 基础库等等，不可能每个组件都去打包一份，这个时候怎么做呢？</p>
<p>我们原来使用的方式就是通过 Webpack 的 external 的方式，它的作用就是说如果你的组件有公共依赖，它会把那些组件的公共依赖在打包的时候不打到你的这种产物里面去，而在运行的时候通过全局变量的方式去访问，这样的方式就可以保证每个组件都不会把这些基础库打包，保证你每个组件的代码量也好，整个文件大小可以控制在相对较小，也不会出现重复引用的情况。这种方式非常简单，只要稍微改一下 Webpack 的配置就可以实现，但是它也有一些潜在的问题，比如说有一些公共包是不支持这种模式，它不能够导成一个变量挂到全局上面去，这样这个时候你就用不了这种方案了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd09beb1ab8c445ab4d8a77797756337~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">Module federation</h4>
<p>幸运的是前几天 Webpack5 正式发布了，里面有一个非常有意思的特性，叫 Module Federation。它的作用是你可以依赖另一个应用的组件或者说依赖，使用它的好处就是让你两个应用在开发的时候都不需要考虑依赖的问题。在运行的时候，它通过一种特殊的模式可以去动态的加载其他应用里面的一些基础模块。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6fc9fb7bc0d4fc784f0809cc9c6db79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>来看我这个模块联邦的一个示例的代码，其实就是在你的构建里面去加一个插件，这个插件里面就说明你需要依赖的另外一个应用和它的一些库的情况。比如说这里设置你需要使用的是另外一个应用里面的 React 基础包，那么它自己打包的时候是不会把它打出去的，而在运行的时候，它可以从另外一个应用里面读进来，也就是说通过 Webpack 模块联邦这样一个功能，我们可以让应用从另一个应用里面去加代码，这种方式其实就可以很优雅的去解决我们组件之间这种依赖共享的这样的一个问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cc7a536d7e64294be9296496dc79ec9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">小结</h4>
<p>那么通过前面我们讲到了几个点，也是围绕着我们要解决的这三个核心的问题：</p>
<ul>
<li>第一个是隔离的问题，组件怎么样去独立的开发？我们是通过将其独立成一个服务单独去部署，而不跟你原来的页面去绑定。</li>
<li>然后怎样去实现它的按需加载？通过 BigPipe 的方式可以去实现快速的返回，并且动态的拉取你的组件。</li>
<li>包括在实现这种多组件的情况下，需要考虑多组件的冲突问题。像 JS 沙箱的这个方案，CSS 隔离的解决方案，还有组件依赖共享的方案。</li>
</ul>
<p>通过我们上述前面讲到的这些方式，我们的整个不管是页面本身还是组件本身，都是支持服务端渲染，可以利用到服务端渲染的优势，来保持整个渲染的性能，也是处于一个比较好的状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/830331d6f8624a9c863db7083f362f39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">三、实践与效果</h2>
<p>那么接下来来看一下在我们业务中具体实践的效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24169c9176884910b3110348c1fc01e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">开发成本</h4>
<p>前面讲的就是这个方案会有一定的开发成本，我们需要对组件本身做一些改造，让它可以部署到一个服务上面去，然后另外一个对主页面也要做一个基本的改造，让这个页面可以去加载它所需要的组件。我们针对这种情况，开发了一个工具链，分别去解决这些问题。对于组件来说，其实大部分不管是 CI/CD 的这种部署也好，或者是它的这种开发的 Webpack 配置等等，这些都是固定的，通过一个脚手架的方式都可以快速的解决这些问题。</p>
<p>对于我们所谓的基座，也就是基本的页面，通过 SDK 来封装很多调用组件服务能力和怎么样去生成骨架屏的这些能力。通过这样一个工具链的建设，就像我们业务中现在如果有这个诉求，比如说像 ABTest 特别重的业务的话，对于开发者来说，改造成本是比较低的，并不需要去关心太多的事情，你可以按照正常的开发模式去开发就可以了。</p>
<p>还有一个很重要的点就是我这边提到的性能上的点，我们这里面以一个当前上线的业务页面为例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee5e7fcae6b847b888fbe614e57b0c0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这种方式你可以想象是首先他跟非服务端渲染的这种页面相比，它的性能明显是要好的。而对于本身就是服务端渲染的页面来说，由于有了分块渲染能力，也比完整页面渲染的时长要更高效一些。这种特性，特别是在慢速网络里面会更明显。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a721552c5bc746dbbc3572b4c976cdc8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在慢网络上，我们做的一个实验结果，可以看到首屏的性能可以从 4 秒提升到 2000 毫秒，更详细的在不同的测试条件下都可以看到有一个性能上的提升。这里面也是我们一个现网的测速上报情况，通过这样的方式，整体性能都会有一个比较明显的提升。但其实目前的整个方案来说，在性能上也不是完全极致的，会有一些环节可以进一步的优化，比如说在前面客户端与服务端连接的时候，我们想的是因为我们将我们的组件服务化之后，组件本身是部署在一个中心的云函数上面，而传统的方式是可以利用到 CDN 的能力来做一个加速。我们可以看到各种 CDN 厂商，都有在探索 CDN 上动态计算的能力，这样可以进入到另一个话题，就是关于边缘计算的领域，我们可以再利用到 CDN 的节点去部署我们的组件服务，这样可以更快的跟用户有一个建立连接的这样一个过程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d5faa6307cd49aaa4980aea43eccaa4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">性能优化方案</h4>
<p>另外一点就是我们的业务中其实也会发现有很多是重数据依赖的，你需要去请求很多的数据，这些数据有一些是比较快的，有一些可能就是慢查询，我们可以对这些接口数据去做一个优化，对于所谓的冷热分离，就是说将这些热数据、快速的数据尽快的返回，而且冷的数据可以在后续渲染之后再慢慢的返回，这种方式也是一个提升的点。另外还有一些就是使用了 Serverless 之后的一些常规优化手段，像 Serverless 本身会有一个冷启动的问题，就是说如果你长期没被调用，可能它的实例会缩小到很小，然后你再次触发调用的时候，它有一个启动的这样一个耗时，那么这个启动上是会比较慢，Serverless 也会有一些常规的这种优化场景的一些手段。</p>
<h2 data-id="heading-22">四、总结</h2>
<p>最后第四部分总结一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bb94677ac7d4c2fb098e2116456b5b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13400b6a05c84e5bb0c82fbe6d3f5703~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们知道有一句很有名的话叫软件工程没有银弹，就是说在软件工程领域其实没有什么方案可以包治百病，CaaS 其实也是一样，它专注解决的一些特定的场景：就是<strong>在复杂的组件场景下</strong>，<strong>要实现组件的隔离</strong>和<strong>动态加载</strong>，<strong>并且在解决这些问题的情况下能够兼顾页面的性能</strong>，<strong>使得整个将来的性能仍然保持在一个比较优秀的状态中</strong>。所以我们最终得出的是这样的一个方案，将组件放在服务中，而组件放在服务中之后还会带来一个新的想象空间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0220b7eabbd64fecad8c0dad03623924~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前我们可以看到在很多云服务的厂商里面都有提到一个概念，就是边缘计算的概念，一种是基于边缘的物理服务器，边缘容器等等，另外一种是基于 CDN 的能力，直接在 CDN 上去做边缘计算，简单来说就是我们传统的 CDN 只是拿来加速你的静态资源访问的，比如说 JS、CSS 借助 CDN 你可以更快的去获取，因为 CDN 离用户会更近， CDN 的节点，以后可能会有这种动态的能力，在 CDN 节点上也可以做一些运算，我们可以在上面去做服务的渲染，然后可以做到更快的给用户一个服务端渲染的结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bf54e9bebb4cea904c527d77853787~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外一点就是当下也可以做的一些，包括在代码管理上、组件复用上，其实组件复用这一块也有非常多，像前面的一些老师也有讲到，在组件复用上也可以进一步的去优化。还有就是关于 Server Push，在 HTTP2 里面有一个能力可能会被大家不怎么注意：Server Push 能力，服务端可以直接提前去推动一些文件到客户端，比如说我们组件的 JS， CSS 完全可以提前推送给用户，然后都在客户端做一个缓存，这样可以进一步的去减少我们的可交付时间。页面除了渲染出来的一个结果，用户在上面操作的时候，他必须要 JS 加载完成，才能够响应用户的操作。所以如果能够更早的把 JS 推送到客户用户的手里面，用户可以更快的去交互，这也是一个可以优化的点。另外前面提到的这种接口层的分离，针对于接口本身的一个优化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b88b4001a2f74e7d89d1b843f3b28fd7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">团队介绍</h2>
<p>最后就介绍一下团队的环节，我们团队是腾讯的 IVWeb 团队，团队位于深圳，业务上主要做直播相关的一些产品，像腾讯内部的一些直播产品都是由我们团队来承接去开发的，我们团队也非常注重社区建设跟对外交流分享，像每一年都会举办 TLC 大会，同时我们的团队成员也会到各个大会里面去做一个技术分享，是一个技术氛围比较好的团队，也有一些开源的产品有兴趣的话可以到 GitHub 上去看一看。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a99cf83d00f4438e8955107819290428~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">推荐书籍</h2>
<p>最后是推荐书籍，我们推荐的书籍是这一本《深入浅出 WebAssembly》，这本书是于航老师撰写的，他是上海的 PayPal 公司的一个高级工程师。为什么会推荐这本书？一方面是因为 WebAssembly 是一个我觉得非常酷的一个技术，是一个面向未来的技术，在未来基于 WebAssembly 是有很大的这样一个发挥空间的，完全可以把前端的边界拓得更加的广泛。另外一个很重要的原因是我也有在线下听过于航老师的分享，于航老师算是国内 WebAssembly 布道者，他对于 WebAssembly 理解是非常的深刻的，并且也有非常多优秀的实践。在线下听的时候就有很多的收获，所以大家如果对 WebAssembly 感兴趣的话通过这本书去了解更多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18f683560244e1a919e2621e226aad4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天的分享就到这里了，谢谢大家。</p>
<h2 data-id="heading-25">附录</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b0a3b23f961446aaca9ad82b2990227~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40362b23f4714c34ad9e1bfe0d01a3e4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c4b131eeb8346fbab3328973ebb1b39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8c253f8ad5b4a3f8f48d8dcc17745b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/922f9c71190340cabed00b3414691548~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/023eea36beba4f8595af9fe25c6767c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>别忘了6-5 下午直播哦，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<p>期待更多文章，点个赞</p></div>  
</div>
            