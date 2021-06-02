
---
title: '今天聊：如何从 0 到 1 搭建 Web 数据分析报表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365259abffa149929c01ff24c9477445~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 14:56:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365259abffa149929c01ff24c9477445~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十七届|前端 Flutter 专场，了解 Web 渲染引擎|UI 框架|性能优化，6-5 下午直播，6 位讲师(京东/满帮/闲鱼等)，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365259abffa149929c01ff24c9477445~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十五届 - 前端早早聊<strong>报表专场</strong>，也是早早聊第 106 场，来自 独立开发 - 独书 的分享。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ae92a6c993b4cceb640cbfcee0e235d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一、开场白</h2>
<p>各位前端的同仁们，大家中午好。今天由我来给大家分享《如何从 0 到 1 搭建外部数据分析报表》，而且我来讲一下，我这个是独书，不是独云，所以我要校正一下，也非常感谢我们的花花小姐姐，还有我们的 Micky 对我们会务支持的大力的帮助，非常的专业，也感谢我们前端早早聊，能够提供这样的平台，让我们能够在一起交流学习，同时也非常感谢我们的 Scott，也就是我们前端早早聊的创始人，他对我们本次专题有很大专业的建议和帮助，非常感谢 Scott。</p>
<h2 data-id="heading-2">二、个人介绍</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df69034da0549d5818f7b8bf1ed734c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面看一下我的个人介绍，刚才花花小姐姐已经讲过了，我可能在前端领域和数据领域从业年限都非常的久，而且我是一个 Excel 的深度用户，对 Excel 有非常多的使用，所以就制作出了 LuckySheet 这样一个在线电子表格，同时还是 BabylongJS 就是一款 3D 引擎中文网的发起人，各位有兴趣可以了解一下。</p>
<h2 data-id="heading-3">三、报表的演化</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f5ba6168004acf8335441aaa599508~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>言归正传，说到做一个数据分析报表，我们就要谈一谈报表演化的历史。我记得我从业的时候，报表承载的功能还不是那么多，数据量也不是那么大，可能几百条、几千条数据就已经差不多了，而且用户更多的是在报表里面进行查询和进行下载。查询出数据以后，下载到本地，然后用 Excel 进行进一步复杂的分析，而随着我们大数据的普及，还有我们企业里面数据驱动决策的这样一个发展，越来越多的用户已经不甘心报表只是一个简单的查询，它可能还要带一些分析的功能，是吧？展示的数据量也越来越大。比如说现在要求 5 千、上万甚至 10 万的数据展示，也不是一个比较稀奇的东西，所以在这样的大背景下，我们要介绍我们今天的主角，也就是 <strong>LuckySheet</strong>。</p>
<h2 data-id="heading-4">四、LuckySheet</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a465420fd7114781870410f41bb1ce8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>LuckySheet 是基于 Web 端的在线电子表格，它能够帮助各位在前端快速搭建我们的数据分析报表，那么它有 4 个特点。</p>
<ul>
<li>首先，它是<strong>开源</strong>的基于 MIT 协议，用在商业应用完全没有问题。</li>
<li>第二，它配置非常<strong>简单</strong>。用起来一行代码，就生成一个全功能的表格。</li>
<li>第三，功能也是非常<strong>强大</strong>。各位知道现在市场上的在线电子表格，葡萄城的 SpreadJS、还有 ONLYOFFICE 是非常强大的，但它们是收费的，而且开源的话像 ONLYOFFICE 会有开源版，功能也只限定于个人使用，公司使用是需要收费的，开源方面的还有 handsontable、x-spreadsheet 等等。在开源领域的话，目前 LuckySheet 它是一个生力军，大概是在六七月份左右开源的，但它其实年限非常久，大概从 2015～2016 年就开始启动了，所以年限其实非常的久，叫什么？老牌的新军，对吧，有这样一个说法，它的功能是非常强大，各位可以在接下来我们演示的时候看一看。</li>
<li>还有它的效率是非常高的，比较<strong>高效</strong>。展示百万级十几万级的数据都没有问题，只要你的电脑能够承载得了。</li>
</ul>
<h2 data-id="heading-5">五、分享大纲</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e230eb95ae44446ba1164d5ac1310c14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天依据 LuckySheet 这样一个在线电子表格，有 4 大分享的板块。</p>
<p>第一个主要介绍一下的<strong>功能与架构</strong>，更好的让各位去评估能不能用在各位的数据分析报表项目中，而且从我们的第二、第三和第四来看，我们介绍一下 LuckySheet 的一些干货，我们在制作 LuckySheet 的过程中遇到了哪些难解决的问题，我们是怎么思考的，然后怎么解决的，而且在第二、第三和第四板块里面我尽量用 3 点、3 步走、3 板斧来很简单的把原理讲一讲，方便各位就像自己造轮子对吧？自己开发一个在线电子表格，就可以做一个参考，所以从这 4 个方面，给各位做一个交流分享。</p>
<h2 data-id="heading-6">六、功能与架构</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29668e84aa374b8aad38885d36ec7476~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们看一下功能架构，我们先从演示开始，就是 LuckySheet 到底能做什么，这是我们录的一个十几秒的小视频。首先支持复杂的单元格显示、支持行内样式、支持 Alt + Enter 的换行、支持公式 385 个（非常全面）、支持数据验证、支持表格、支持我们的 sparkLine 小图、把图片展示在单元格里、支持屏备注、支持我们独有的一个叫数据透视表，可以根据数据像 Excel 一样操作、还有图表基于 ECharts、还有可以插入图片，最后可以进行数据验证、支持复选框、支持我们的下拉列表、支持日期、身份证、手机号码等等的验证，可以任意的去设置，这就是 LuckySheet 一个整体功能的概要，各位可以去体验一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ebf2da9dfa42599d86084449cb6283~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里对系统的功能做一个总结。</p>
<ul>
<li>首先最底层最核心的东西就是<strong>计算</strong>，不管是什么样的应用、不管是什么样的功能、不管是什么样的操作都是需要计算的，对吧？计算是我们的核心，这里列了一个简单的特点，包括定位、公式、溢出计算、矩阵计算、动态数组都是通过计算而来。</li>
<li>第二部分就是<strong>渲染</strong>。我们的行内样式、条件格式都是通过渲染引擎，然后画在画布上面，进行这样一个展示。</li>
<li>第三个就是<strong>操作</strong>，很多用户第一眼看到 LuckySheet 的时候，觉得这个东西很强大很好，为什么？因为我们把细节做到了非常的细致，按照我们的水平做到了完美，操作的话几乎和 Excel 一致，用户体验也是非常注意。</li>
<li>第四个就是我们的<strong>综合应用</strong>。在我们的计算、渲染和操作这几层上面，进行复杂的应用开发，就像刚才各位看到的图表、数据透视表、导入导出。LuckySheet 自带导入导出的，接下来会跟各位介绍一下，当然导入功能已经完成，现在导出功能还在开发当中，稍后会放出给各位进行验证。</li>
</ul>
<p>这是 LuckySheet 一个整体的功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21d217bc3f894f78b3a22509eb89305f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>四大步骤计算、渲染、操作和综合应用，有很多我们前端的同仁，还有包括我们后端有很多朋友会在群里面问到我们，现在语雀、石墨文档和腾讯文档那么火，他们是怎么做到这个数据的保存、做到协同办公、怎么做到的？怎么样保存数据？所以我这里跟各位提一提，我们当时做了一个前后端保存的这样一个架构，给各位也演示一下，这是我们前后端协同办公的这样一个保存的应用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcb9a8afa12f48aa9c1067642c230931~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>数据库</strong>
<ul>
<li>**关系型数据库 MySQL **进行用户信息，还有一些表格的原数据进行保存。</li>
<li><strong>非关系型数据库 MongoDB</strong>，也可以用 PostgreSql，这个不限制，只是举了个例子，因为 LuckySheet  的存储格式是基于 JSON，非常容易保存在我们的 MongoDB 非关系型数据库里的。</li>
<li><strong>内存数据库 Redis</strong>。可以对我们的数据进行一个缓存，有这三个数据的服务。</li>
</ul>
</li>
<li><strong>后台服务</strong>
<ul>
<li>**Ajax **用来承载一般的接口请求，还有我们的批量保存。打个比方我要对整个表格的数据进行保存，那就用 Ajax 保存大量的数据。</li>
<li>第二个 <strong>WebSocket</strong>。各位可以看语雀，还有我们的金山文档、腾讯文档，每一步操作都会有一个保存的动作，是用 WebSocket 进行操作的。每修改一个单元格，都会把单元格的对应信息发回到后台，后台保存到数据库当中，是这样一个流程。所以 LuckySheet 也内置了这样一个功能，它每一个操作都会向后台发送一个 WebSocket 的请求，各位只要配置好地址接收这个请求，然后再传到数据库，这样一个协同保存的功能就已经制作完成。</li>
<li>第三个<strong>协同服务</strong>。就是我们大家在一起编辑一个表格的时候，每个人都可以看到自己的选框，自己在编辑哪一列，在编辑哪一个单元格，LuckySheet 也做了相关的这样一个应用。编辑的同时，会提供接口，高亮就是你的界面上有同时几个人在编辑都会有这样一个提示。</li>
<li>第四个是我们觉得比较有创新点的一个服务<strong>分析运算</strong>。GoogleSheet 当然也有这个服务，一个 Excel 的函数，各位可以想象一下，它可以调用后台服务，返回结果在表格里面进行展示，包括我们复杂的一些聚类算法、分类算法、文本分析算法，都可以进行后台服务返回到前台这样的应用。还有一个比较好用的，比如我在电子表格里面输入了日期和股票代码，我用公式引用一下，在后台拿到当日的价格，就可以返回到我们的前台，进行股票价格的这样一个展示，包括在界面可以进行各种拖拽，展示股票的收盘价和开盘价都 ok。</li>
</ul>
</li>
<li><strong>前端应用</strong>。这是我们的一个重头，就像刚才讲到的，LuckySheet 没有基于我们现在流行的三套框架，因为它是 2015 年开始的，当时还是 jQuery 非常流行，所以当时基于的架构技术栈就是 HTML、CSS 和 jQuery，几乎是用原生应用写出来的，没有基于三大框架，在三大框架里应用现在也是没有问题的。右边就是我们 LuckySheet 的架构，渲染、计算、综合应用和数据保存，这样就形成了 LuckySheet 一个前后端服务的架构。</li>
</ul>
<h4 data-id="heading-7">嵌套公式计算&着色</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31ce3e2e596141cda6850d4061b62051~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来看一看 LuckySheet 有哪些特色功能。这里是一个公式的计算和着色，可以看到我们支持的公式非常复杂，层层嵌套，如果你的机器允许你嵌套 100 层的 <code>if</code>，或者是嵌任何的公式都是没有问题的，Excel 能解析什么公式，LuckySheet 都能完整的去解析，而且它里面的单元格和文本都是可以进行着色的，红色文本渲染成绿色，跟 Excel 也一致，渲染好之后，在引用的单元格会进行选区的高亮显示，选区可以继续进行操作，比如像拖拽选区，公司里面的参数会随着改变，就跟 Excel 的操作几乎一致。</p>
<h4 data-id="heading-8">导入渲染 & 公式导入</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6db75ae7f4aa438cbb5f177137624e47~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>右边是一个 Excel，一个非常漂亮的表。通过 LuckySheet 的导入功能导入到 LuckySheet 中，它会生成左边的格式。几乎两边看起来是一模一样的，这就是 LuckySheet 做到了很细致的，跟 Excel 做了一个匹配，基本渲染出来的样式都是一模一样，而且公式也可以完整的渲染出。可以看到左边红色的那一列，是不是 Sum F7:F41 就是一个公式的这样一个渲染。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b607f65b4caa46a8817ccf6d7f71542a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>给各位做一个演示，这是一个 Excel，各位可以看一下，就刚才我们图片中讲到的，进入我们的 Demo，导入刚才的 Excel，各位看一下是不是一模一样，而且支持公式，这就是 LuckySheet 的导入功能。导出功能正在开发当中，导入的话现在已经支持很复杂的格式了，包括旋转、换行和行内样式都可以完整的支持，都可以放心的使用。</p>
<h4 data-id="heading-9">数据透视表</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8ac5171a2cc44f99fd7a36c3275c1de~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个数据透视表，我们在葡萄城、包括在 ONLYOFFICE 没有发现这个功能，我们可能是第一个把这个功能嵌到电子表格里的一个插件，它可以对数据进行一个分析，就是用户不需要把数据下载下来了。几万条数据你查询出来之后在网页上做一个聚合，我就能大概知道它的这样一个数据统计信息，不需要进行再次下载，这个功能和我们当时 OLAP 比较关心的数据分析的功能有异曲同工之妙，之后我会跟各位进行进一步的介绍，这就是我们功能与架构的展示。</p>
<h2 data-id="heading-10">七、核心算法</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a00907ece50f4cad8e765eb2eec626cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们要讲到核心的算法，功能介绍完了，各位可能想自己搭建一套自己的在线电子表格。我不想要已有的轮子，我自己写出来的更牛逼，我想自己造轮子，ok，没问题，我们这里可以帮到你。首先我们讲一讲 LuckySheet 的核心算法：公式的解析和公式的联动更新。</p>
<h4 data-id="heading-11">公式解析基本思路</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43761c176acd4ac692bb2980849da415~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>什么是公式解析呢？在上方我们一个简单的公式 <code>SUM(A1:B3, E5)+1</code>。这是在 Excel 当中在 LuckySheet 当中一个非常简单的公式计算。蓝色表示公式名 <code>SUM</code>，绿色是参数，后面 <code>+1</code> 是算术运算，它其实是一个伪代码，怎么样把伪代码转换成为我们 JavaScript 能够识别的这样一个公式，是值得讨论的问题，其实这个和我们的 Java 语言，Python 语言，包括我们的 JavaScript 怎么解析成为 C 语言？怎么样在底层运行有相似的这样一个逻辑。</p>
<p>这里给出一个思路，首先要把伪代码生成我们的抽象语法树。抽象语法树就是这样的一个树形结构，它表示了公式完整的解析状态：<code>+</code>1 和 SUM。 <code>SUM</code> 后面是两个单元格参数，只要生成了这样一个抽象语法树，可以看到最后一行生成了我们可执行的 JavaScript 代码。为什么我以 <code>_.SUM</code> 这样一个形式去展示这个公式，因为 lodash（前端的工具库）各位可能用过，它就有 SUM 函数，也就是说其实这个 SUM  函数我们要在后台定义好，LuckySheet 支持 385 个函数，其实函数我们是一个一个把它已经实现了在后台，只要我们根据对应的字符串去引用到函数就 ok。</p>
<p>SUM 里面我们把单元的信息已经转换成为二维数组，因为 A1 到 B3 是二维数组，第二个 E5 它是一个单元格，它引用的是一个数字，所以 SUM 函数要解决的问题就是不管传入多少个参数（不管是二维数组一维数组或者数字），把里面的数字进行一个整体的加总，得到一个数字，最后再 +1，然后用我们的 Eval 函数（我们的 JavaScript 都有的函数）进行执行，是不是结果就已经产生了。</p>
<h4 data-id="heading-12">思考</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d0a7076901443668892e92244e2b9c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是我们公式解析的一个基本的思路，刚才是一个比较简单的公式，这个复杂的公式生成了我们的抽象语法树，非常的复杂。各位可以思考一下，可以看一看如何去做，这里跟各位提炼一下，就是怎么样去生成抽象语法树呢，我们就把问题规划到怎么样生成抽象语法树。</p>
<h4 data-id="heading-13">公式解析关键点</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dff30abe06d47739e103116b261379f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>两个关键点：第一个<strong>词法分析</strong>，第二个<strong>语法分析</strong>。这两个其实也是深层抽象语法树的两个通用步骤、两板斧。</p>
<p>首先怎么解析？我们需要用 <code>split</code> 把我们的字符串拆解开，一个一个字母的拆解、一个一个逐字进行读取，根据关键字，那关键字有哪些呢？可以分析一下刚才的这个公式，关键词有：左右括号、逗号、双引号、花括号和单引号。根据这些关键词，来识别我们的 Token。Token 就是公式的名称，也就是函数的名称，还有函数里面的参数名字，还有常数和运算符加、减、乘、除和取余，有这样一个 Token 的生成，词法分析阶段就是生成这样一些 Token。</p>
<p>第二步，语法分析就是组装成语法树，因为词法分析只是识别出了 Token，但是没有把它组装成语法树，所以第二步要通过语法分析来生成抽象语法树。首先传入的是我们的 Token，这里要<strong>注意</strong>的一点是为了避免括号的影响，因为在日常的计算当中，括号对计算顺序有很大影响的，所以需要把<strong>中缀表达式</strong>转换成<strong>后缀表达式</strong>。</p>
<p>什么是<strong>中缀表达式</strong>呢？例如 <code>1+(2+3)×4-5</code> 它就是一个中缀表达式，中缀表达式就是我们日常看到的数学学到的这样一个表达式的状态，它需要有括号，基本上机器是很难根据这个式子去计算的，所以为了方便于机器进行一个表达式的计算，我们需要把中缀表达式转化成我们的后缀表达式，也就是叫术语叫<strong>逆波兰式</strong>。可以看到这个形式 <code>1 2 3 + 4 x + 5 -</code>，这个形式可能比较奇怪，但是机器读起来就非常的舒服，想象成一个栈：入栈出栈去计算，会非常的便捷，所以这两步构成了我们生成公式解析的关键点，各位有兴趣可以去深入的挖掘。我这里可能讲的不是太深入，因为太深了也讲不了，也没有那么多时间，各位私下也可以找我进行沟通，公式解析这部分就结束。</p>
<h4 data-id="heading-14">公式链式更新</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a779da3b5394ae8b154360596ba9d5c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>想象一下 Excel 里面一个单元格的数据进行了更新，与它相关的单元格如果有公式的话是不是要进行更新？因为它引用到了我的单元格。可以看到图中的 B1 单元格，B1 单元格如果进行了更新之后，它会影响我们的公式 2、公式 3、公式 4 和公式 5，为什么？因为公式 2、公式 3 直接引用了 B1，但是公式 4 引用了公式 2，公式 5 引用了公式 3，所以就有这样一个公司链的更新关系。</p>
<p>我们要通过 B1 找出公式 2、公式 3、公式 4、公式5，而且要规定好它们的顺序，公式 3 要提前算好，供述给公式 2，公式 2 算好以后才到公式 4，再到公式 5，有这样一个计算的顺序在。如果不按照这样的顺序，打个比方我先更新了公式 4，但是我公式 2 更新是不是公式 4 的计算值就错误了，所以必须有这样一个算法，去把这样一个更新的关系给确定好，这就是我们公司链更新的一个三板斧。</p>
<h4 data-id="heading-15">链式计算要点</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40c08e0d3dd140d0baa43f9dba08f882~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>公式存储格式</strong>规定好。比如说 1000 个单元格，有 3 个公式，这 3 个公式是散落在 1000 个单元格当中，存在里面，这 3 个公式的话也要保存在全局里面，为什么？因为为了每一次存取这个公式方便，我不需要每次都遍历这 1000 个单元格就能够拿到这 3 个公式进行一个计算，所以全局也要存一份。存在全局有个好处，我可以规定好公式插入的顺序，在计算的时候也就有顺序计算，达到公式更新，顺序依然是正确的。</p>
<p>第二步是<strong>构建公式树</strong>。这里用到了出栈入栈的<strong>后进先出法</strong>，各位对这个应该是非常熟悉，它的作用是什么？生成一个函数之间的父子关系，你是不是也用到了我，你引用到了我，你就是我的子。如果我的子再有一个下级的引用，它就是孙关系，所以就是要形成这样一棵树，可解析的树，继续我们的计算。</p>
<p>第三步就是用<strong>深度优先遍历树</strong>，<strong>处理多级调用</strong>。想象一下，在我们树的根节点，是不是没有节点在引用它？它先计算以后，提供给上一级的数据，这样的话上一层的数据就会保证准确，所以要<strong>用深度优先</strong>的这样一个算法去遍历这棵树，然后来继续进行计算，这就是链式计算的要点，算法到这里就介绍结束了。</p>
<p>我们两个非常重要的点就是：<strong>公式的解析</strong>和<strong>公式的链式计算</strong>。</p>
<h2 data-id="heading-16">八、渲染</h2>
<p>渲染也非常的重要，计算讲完了我们讲渲染。渲染在 LuckySheet 里面也是非常有特色，为了展示大量的数据，它采用了惰性加载的这样一个特性，我看到哪里展示哪里，而并不是一次性加载全量的，显示全量的数据，可能会有 1000 万行数据，但是我看到的可能只有 100 行，所以我展示出来的只有这 100 行，看多少展示多少。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52835c4cd3b5456fb81f614ae85726c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">渲染方式</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea82dfb26a224cdda7e55c5a8073905d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们选择了 <strong>Canvas 作为画布渲染</strong>，为什么选择 Canvas。因为它的效率非常高，它可以保持和 Excel 这样一个样式的同步，不像 DOM 它比较难控制一点，用 Canvas 的话比较简单一点，这是选择它的理由。各位可以想象一下，我们选择了 Canvas 是不是就意味着我们缺少了和用户的交互？用户选中了某一个单元格，我怎么知道他选择了某一个单元格呢？因为它不是 DOM，它选中的是一个 Canvas，我不知道具体选择在哪里，所以我们的渲染也是基于计算的，也就是说用户在屏幕上点击了一个位置，我们根据你滚动条的位置、滚动条的偏移，加上你在屏幕上点中的位置的偏移，同时考虑决定好你点中的是某一个单元格，并且这个点中的单元格给你渲染出来的位置是一模一样，也要基于计算。</p>
<p>我们这里用到了<strong>二分查找</strong>。两分查找的话也是一个比较简单的算法，网上已经非常通用，但是它确实非常高效。100 万行的数据定位到某一个单元格，定位到你点击的单元格，可能只要十几次的预算就结束，非常的高效，所以我们的渲染都是基于 Canvas 惰性加载，还有计算而来。</p>
<h4 data-id="heading-18">自动换行</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ceacd3696945fa8a1c05054d97ed36~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里既然讲到了渲染，是不是就要讲到某一个单元格的渲染动作，因为单元格是构成表格的一个基本单位，所以这里重点介绍一下单元格的渲染。</p>
<p>单元格的渲染要规定它的宽度和高度，这里以<strong>自动换行</strong>为例，介绍一下，我们这个高度、宽度怎么判断，首先采用了 measureText 的方法，进行宽度和高度的测量。打个比方引用一段话：我在马路边捡到一分钱，交给警察叔叔。这句话我们发现在算第一个字没有超出，第二个字没有超出，一直到“给”超出了，我们回退到“交”这个宽度就是在这个单元格之内，所以把“给警察叔叔”这个字符换一行进行展示，得到计算后的结果，这就是我们简单的一个自动换行的一个设计，可以根据用户输入的内容自动进行换行。</p>
<h4 data-id="heading-19">文字旋转</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a59b60efe3c1494c9bf9a0269bb9358a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到我们的文本是有高度和宽度的，所以接下来讲一个知识点，就是我们的文字旋转。文字旋转是这样的：比如说我在马路边捡到一分钱，本来它是没有选任务，它是一个横向水平的动作，但是我们这里向上旋转了 alpha 的角度，得到了一个斜的文字样式，得到这样的样式以后，各位可以看，渲染它的关键点在哪里？我们要精确计算它的宽高，旋转后的宽高，我们这里遇到了一个坑，当时我们计算了蓝色区域的宽高，因为我们当时可能没有考虑到那么多，没有精确的计算出文本的宽高，所以导致它的位置有偏移，不是那么准确，告诉它的高度，判断显示也有问题。</p>
<p>后来我们研究发现，其实文字相比它的宽度来讲，它的高度非常有限，它这个高度是影响我们宽高的一个重要的因素。正确的整个旋转后的宽度高度应该根据我们的 beta 区域进行确定，所以我们直接给出一个公式：旋转后的宽度等于旋转前的宽度乘以 <code>cos(a)</code> 加上旋转前的高度乘以 <code>sin(a)</code>，旋转后的高度等于旋转前的宽度乘以 <code>sin(a)</code> 加上旋转前的高度乘以 <code>cos(a)</code>，这就得到了一个精确的宽高的计算。</p>
<h4 data-id="heading-20">文字旋转 + 换行</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/026888cf13d54db79e055db038aa0a3a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来开始复杂的这样一个渲染的介绍。各位想象一下，如果文字旋转加换行，会产生什么结果？最早 Excel 是一个大家觉得非常常见的动作，旋转和换行生成一个样式，但是我不知道有没有人去考虑过怎么样做到的，怎么样才能做到这样一个格式，为此我们花费了很大的代价去做这个事情，因为坑非常的多，考虑的步骤大概有 18 种结果，我们当时一个一个去写，非常的麻烦，这里我只讲解一个比较简单的情况。</p>
<p>首先看左边旋转后的高度，旋转后它超出了我们单元的高度，从“路”开始就已经超出了，所以我们要对它进行一个换行的计算，生成右边这样的结果。“我在马路”一行、“边检到一”一行，“分钱”再生成一行，得到这样一个结果，怎么样得到这样的结果？各位想象一下，它是旋转了 a，a 是它旋转了一个角度，我们把它还原，不要旋转 a 是什么样子的，所以就看中间“我在马路边捡到一分钱”，它是一个正常的从上至下渲染的过程。</p>
<p>我们发现这个过程像 a 一旋转就得到了右边的结果，这里的关键点是什么？如何得到我们的偏移，到“边”到“分”，它们之间的关系是怎么样的，怎么样计算得到这样的格式呢？所以我们这里直接给出公式，我们设定高度“我在马路”是 <code>H1</code>，“边检到一”是 <code>H2</code>，“分钱”是 <code>H3</code>。“边”偏移多少？就是上文字的高度 <code>H1</code> 除以我们的 <code>tan(a)</code> 得到偏移，“分钱”怎么偏移呢？它需要 <code>H1 + H2</code> 除以 <code>tan(a)</code> 得到偏移，所以生成这样的结构在旋转这样的角度之后，就得到最终的一个计算结果，这就是我们的换行加旋转的一个操作，看起来可能比较抽象，但是基本都是一些干货，各位可以看一看。</p>
<h4 data-id="heading-21">思考</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d1d41d14e3c4786acdc3decc09033e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再进行一个思考，打个比方，我们进行了文字旋转，又进行了换行，而且我们还加入了行内样式，也就是我们每一个字的大小、粗细和斜体，斜体程度都不一样，会造成什么样的结果呢？各位可以思考一下，这个东西怎么生成，有兴趣会后可以给我进行交流。</p>
<h4 data-id="heading-22">measureText 方法</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1817b9c6d3849b396140fb82addda92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里讲一下渲染我们遇到的一些比较有意思的方法，提炼一下。看一下 measureText 这个方法，它是测量文本的高度和宽度的方法，它有两个比较重要的属性，一个是 actualBoundingBoxAscent 和 actualBoundingBoxDescent，那么这两个属性就决定了文本的高度，这个属性在 Chrome 51 版本之前是没有的，当时计算高度是非常痛苦的， Chrome 51 版本之后再加上的，但是 Chrome 51 版本怎么办？当时我们就用了 DOM 的方法，先去测量文本的高度再进行渲染，效率也没有它高也有问题，算是做了一个兼容性的处理。</p>
<p>我们回到这两个属性，这两个属性非常有意思，它是跟着 textBaseLine 的属性进行渲染，可以看到 baseLine 这根线就相当于红色的这根线。</p>
<ul>
<li>默认情况下这根线是贴着 Abcdef 字母的底边进行渲染的，但是各位发现 gjp 它们就有尾巴，已经超出了 baseLine，显而易见 Ascent 等于 baseLine 往上的部分的高度，baseLine 往下就是 Descent，它俩加起来等于文本的高度。</li>
<li>如果是 Top 的话，因为这个 baseLine 是沿着上方进行渲染的，所以 Ascent 是 0，Descent 是整体的高度。</li>
<li>如果是 Bottom 的话，底边对齐。Descent 变成了 0，Asent 是整个的高度。</li>
</ul>
<p>这个方法非常有意思，但是对计算高度非常有效。</p>
<h4 data-id="heading-23">clip 方法</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97866884e61c4de8b509812760c93e1b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二个就是我们的 clip 方法，Canvas 考虑方法非常有效，它可以把内容局限在某一个局部进行渲染。想象一下单元格在绘制的时候是不是会互相影响，但只要用到了 clip 方法，就精确地把单元格限制在它想要渲染的范围之内，即使超出了，也不会影响下一个单元格，用到了 clip 方法，它效率也还不错，各位可以尝试一下。</p>
<h4 data-id="heading-24">渲染性能优化</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/730823a256c6434f9612b71e100d9646~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然我们介绍了 measureText 方法，但是这个方法其实对性能是有影响的。各位想象一下，LuckySheet 的 Canvas 在更新的时候，每滚动一下，它都会渲染几十次这样的界面，造成数据滚动的这样一个效果，所以对性能要求是非常高的，测试下来发现 measureText 不能用的太多，而且不能重复使用，重复使用之后会造成性能很大的浪费，会造成卡顿。</p>
<p>第二个建议对单元格的信息进行延时释放，也就是说在滚动第一次的时候，对单元格和文字进行一个缓存，即大小、宽高和位置进行一个缓存，滚动的过程当中，先不释放它，等用户可能停止滚动，我们在释放，这样也保证了效率的提升。</p>
<p>第三个就是使用 Web Worker 进行深拷贝。各位想象一下，如果有 100 万个单元格，在撤销和重做的时候，有时候会用到深拷贝 Copy 的功能，我们在深度拷贝的时候，对比了非常多的深度拷贝的方法都没用，都是慢。即使最高的那一个也是慢，因为 100 万个单元格太多了，所以我们用到了 Web Worker 进行深拷贝，让它在后台进行运行，用户基本上在前台能够顺利的操作，也就避免了这样一个感知。</p>
<p>第四个就是避免使用 putImagingData 这样一个方法，DrawImage 就比它的性能高出很多，所以各位要注意，避免使用这个方法，我觉得是有坑的。这就是渲染方面对各位的一些建议，渲染方面然后也介绍完毕。</p>
<h2 data-id="heading-25">九、数据透视表</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f8dc8a27ec04e3caeedc6630e67587e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果要进行数据分析，就避不开我们数据透视表的介绍，数据透视表目前我们好像是第一个在电子表格里有这样一个功能的，GoogleSheet 有，但是其它的文档好像我都没见到过，所以这一块我们已经把它做出来了，还是有一点心得的。</p>
<h4 data-id="heading-26">数据透视表是什么</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5c58c8efe5494f975661593410ebd2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先我们要知道什么是数据透视表。我先介绍一下，因为我们很多搞前端的，都是搞 IT 的，对产品可能有一部分误解，可能有部分不了解，就像黑盒子一样，我给各位打开这个黑盒子，知道数据透视表是干嘛的。它是用户用界面进行操作，对数据进行统计分析的这样一个功能。可以看左边的这样一个是原始数据，包含 4 列，其实就是 4个字段：学生、科目、性别和分数，如果我们在数据透视表进行操作，选择了学生和分数之后，对分数进行求和会得到学生 Alex 总分是多少、Joy 总分是多少和 Tim 总分是多少，得到这样一个结果，很好的对数据进行一个分析，这怎么做到的呢？</p>
<h4 data-id="heading-27">流程操作</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9af02b45fab149038e30e35308705a99~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Excel 里面、在 LuckySheet 里面，如果原始数据有 4 个字段，它就作为 4 个可选的字段摆在一旁，就像刚才右边就是它的一个功能区，我们把学生放在了行里面，把分数放在值的汇总里，所以它就得出了学生加分数的这样一个汇总的一个视图或表格。</p>
<h4 data-id="heading-28">列行代表纬度，值代表指标</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b50f31b53914514862104a7e32add00~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们再进一步，我们把科目放到了列上面会产生什么结果？各位看我们的行还是学生（第三个），但是我们的列增加了一列，把这个表格撑开了，科目在列标题已经出现了很多，生成了这样的格式，所以这是选择科目、学生、分数以后产生的这样一个结果，各位可以思考一下，怎么样产生这样一个格式，怎么样才能生成这样一个格式呢？</p>
<h4 data-id="heading-29">思路</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72aee54032e3465988a7455bac81538a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里提炼一下，记得我们选择了三个字段，其实分数对于合计的影响是没有作用的。我们只有学生和科目这两个字段，对汇总产生了组合的影响。有几种组合看一下：绿色、蓝色、橘色和黄色 4 种组合，学生加科目是一种组合、Alex English 108 分、Joy English 96 分，形成这样一个组合。</p>
<p>蓝色学生就代表学生的统计就是 Alex 总分是多少，橘色代表我们科目的总和就是 English 总分是 296，得到了这样一个汇总信息，最后黄色是整个表格的数据加总，所有行列加起来就等于 1687 这样一个数据，所以各位发现它生成了 4 种数据统计的组合，我们可以把它理解成为<strong>维度</strong>，维度就是现在数据分析领域比较常见的术语。</p>
<h4 data-id="heading-30">多维数据立方体</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e3386a75ee9492b86987ef9b421c699~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为维度，重要的概念就是如何知道这个表格要生成几种统计，我们现在选择了两种维度，生成了 4 种统计。如果有 3 个维度，该生产多少，有 4 个维度，该生成多少呢？所以我们这里直接给出答案，比如说我们选择了学生、班级、性别和科目这 4 个维度，我们就是 2 的 n 次方产生 16 种组合。只要把这 16 种组合里面的数据进行汇总，再进行组合，就生成了我们数据透视表的这样一个数据呈现的方式，至于怎么样展现，就是我们前端人员非常擅长的，这一块，我就不再深入讲了。这一块的内容属于是我们多维数据立方体的这样一个知识点，在数据分析的时候很多会涉及到这样一个概念，包括我们市场上流行的麒麟，就用到了这样一个数据组合、维度组合的算法。</p>
<h2 data-id="heading-31">十、分享总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fce2a812663472a9bb7624a99ac8e8d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是我们分享的几大块内容，在这里做一个分享总结，你要做好一个数据分析报表，首先要解决计算、渲染、操作和复杂应用这 4 个层面的问题。解决好了，你就能做一个不错的数据分析报表出来，当然各位也可以直接使用 LuckySheet 进行制作，现在我们在 Github 上面已经有 2k 的这样一个点赞数量，也希望动动各位发财的小手，给我们点上一个赞。</p>
<h4 data-id="heading-32">交流</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17eb4d6d15c2462baf6081f512920e61~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>各位也可以进到我们官方的交流群，加我们小编的微信进行继续的探讨，可以扫码。</p>
<h4 data-id="heading-33">好书推荐</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49d6b0c18e114c65a46172862635696f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后进行一个书籍的推荐，进行了那么多理性的思考，我们要换换脑子，进行一个文科性的思考，看看文史类的书籍，给各位是一个心理上的洗礼。这本书《资治通鉴》也是各位耳熟能详的一本书，为什么好呢？我这里也不展开讲，看右边的几个字，<strong>鉴前世之兴衰</strong>，<strong>考当今之得失</strong>，重点是<strong>得失</strong>。这个得失是什么？有得必有失，有失才有得，各位要坚持，就像我们现在的工作一样，坚持本职工作，坚持在我们前端的道路上走下去，成为大神，挣大钱、发大财，就是这样一个逻辑，所以把这本书送给各位。最后再次感谢我们 Scott 大神，感谢前端早早聊平台，今天我分享就到这里。</p>
<h4 data-id="heading-34">QA</h4>
<blockquote>
<p>语法分析和词法分析的关键点是什么？</p>
</blockquote>
<p>语法分析和词法分析的关键点就是刚才我讲到的，有它的<strong>关键词</strong>。我们伪代码，它的关键的一个字符是什么？就像我们现在在 Excel 里面的这样一个公式，它的关键的字就是括号、逗号、单引号和双引号，只要把我们的关键词给识别好，就可以通过这关键词进行分割，把我们的 Token（标识），包括我们公式的名字、参数、一些运算符给识别出来，这样的话就是词法分析的一个关键点。</p>
<p>然后说到语法分析的话，其实词法分析这边已经把 Token 准备好了。你厨师下菜，这个料给你准备好了，语法分析就是炒菜，把 Token 进行组合，生成一棵树。就是我刚才讲到的生成一个后缀表达式的这样一个方式，来进行再次的组装，然后生成一棵树，就组合成了我们这样一个抽象语法树的结构，生成了这样一个抽象语法树，很好的去解析我们这样的公式，当然各位也可以直接读我们的源码，然后看一看。好，谢谢。</p>
<hr>
<p>别忘了6-5 下午直播哦，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365259abffa149929c01ff24c9477445~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<p>期待更多文章，点个赞</p></div>  
</div>
            