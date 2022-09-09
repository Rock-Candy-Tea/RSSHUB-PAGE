
---
title: '为何我司的业务模块都在往小程序化发展、选择 Go 还是 Rust？ 2021 年的 SwiftUI_ 优势、劣势和缺陷 _ 酱酱的下午茶第 69 期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=998'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 18:53:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=998'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">今日主理人｜下午茶</h2>
<p>本期每日掘金由<a href="https://juejin.cn/user/4424090519078430" target="_blank" title="https://juejin.cn/user/4424090519078430"><strong>战场小包</strong></a>负责制作。</p>
<p>PS：主理人目前正在招募中，有感兴趣的掘友们可以联系<a href="https://juejin.cn/user/3052665287739005" target="_blank" title="https://juejin.cn/user/3052665287739005"><strong>Captain</strong></a></p>
<p>酱酱们的下午茶新增优质作者介绍和码上掘金板块，专注于发掘站内优质创作者和优质内容，欢迎大家多提宝贵意见！</p>
<p><em>本文字数 1800+，阅读时间大约需要 8 分钟。</em></p>
<blockquote>
<p>【掘金酱的下午茶】亮点：</p>
<ul>
<li>为何我司的业务模块都在往小程序化发展</li>
<li>手拉手寥寥数行 js 实现一个有温度的前端部署工具</li>
<li>用 Rust 开发跨平台 App 探索和实践</li>
<li>选择 Go 还是 Rust？</li>
<li>月饼太贵？那就用Three.js自己制作一个月饼，无死角观看！</li>
<li>2021 年的 SwiftUI: 优势、劣势和缺陷</li>
<li>Android极简MVVM，从一个基类库谈起</li>
<li>……</li>
</ul>
<p><strong>筛选规则</strong>：文章发布时间在本期「掘金酱的下午茶」发布时间的1-3天内，且符合社区推荐标准，也会同步发布在掘金相关技术社群。</p>
</blockquote>
<h2 data-id="heading-1">每日干货｜下午茶</h2>
<p><strong>主理人们会对近期（1-3天）社区深度技术好文进行挖掘和筛选，优质的技术文章有机会出现在下方列表，排名不分先后。</strong></p>

























































































<table><thead><tr><th>文章分类</th><th>作者</th><th>文章</th><th>简介</th></tr></thead><tbody><tr><td>前端</td><td>前端修罗场</td><td><a href="https://juejin.cn/post/7139345030203834404" target="_blank" title="https://juejin.cn/post/7139345030203834404">用案例的方式解释 React 18 新特性：并发渲染、自动批处理、Ttransitions 等</a></td><td>在本文中，我将简要介绍 React 18，并通过案例解释并发渲染、自动批处理和 <code>transitions</code> 等几个主要概念。</td></tr><tr><td>前端</td><td>程序媛李李李李李蕾</td><td><a href="https://juejin.cn/post/7139697395679363086" target="_blank" title="https://juejin.cn/post/7139697395679363086">手拉手寥寥数行 js 实现一个有温度的前端部署工具</a></td><td>抛开自动化 CI 不谈，大多数公司或场景下，都会需要把文件上传到服务器上的场景。那么让我们来讨论其中需要提升效率的空间在什么地方</td></tr><tr><td>前端</td><td>35岁就退休的老狗</td><td><a href="https://juejin.cn/post/7140185024653066271" target="_blank" title="https://juejin.cn/post/7140185024653066271">谈谈前端性能优化的常见手段及知识原理</a></td><td>今天这篇文章，我将带大家一起学习一些前端常见的性能优化手段以及对应的知识原理！！</td></tr><tr><td>前端</td><td>前端修罗场</td><td><a href="https://juejin.cn/post/7140273112741838861" target="_blank" title="https://juejin.cn/post/7140273112741838861">提升 React 应用的安全性：从这几点入手</a></td><td>尽管 React 的攻击数量比其他框架少，但它仍然不是完全安全的。 我们发现由于 React 与<strong>其他开源组件兼容并且没有强大的默认安全设置</strong>，因此它容易受到安全漏洞的影响。下面我们列举了一些 React 应用常见的安全问题。</td></tr><tr><td>前端</td><td>Finbird</td><td><a href="https://juejin.cn/post/7140106359042736142" target="_blank" title="https://juejin.cn/post/7140106359042736142">为何我司的业务模块都在往小程序化发展</a></td><td>可能大佬们也会疑惑：大部分公司不是已经一直在用小程序吗？不算。因为这里不过是作为微信、支付宝等互联网大平台的内容贡献者、参与者，“免费”向互联网平台提供了自己的内容与服务，成为了别人的“生态一员”，换取流量的转化，以触达更多的互联网消费者。</td></tr><tr><td>后端</td><td>FeatureProbe</td><td><a href="https://juejin.cn/post/7139820296097251342" target="_blank" title="https://juejin.cn/post/7139820296097251342">用 Rust 开发跨平台 App 探索和实践</a></td><td>FeatureProbe 作为一个开源的『功能』管理服务，包含了灰度放量、AB实验、实时配置变更等针对『功能粒度』的一系列管理操作。需要提供各个语言的 SDK 接入，其中就包括移动端的 iOS 和 Android 的 SDK，那么要怎么解决跨平台 SDK 的问题呢？</td></tr><tr><td>后端</td><td>CloudWeGo</td><td><a href="https://juejin.cn/post/7140217577539633188" target="_blank" title="https://juejin.cn/post/7140217577539633188">选择 Go 还是 Rust？CloudWeGo-Volo 基于 Rust 语言的探索实践</a></td><td>本文整理自 CloudWeGo 开源一周年技术沙龙活动中字节跳动基础架构服务框架资深研发工程师<strong>吴迪</strong>的演讲分享，技术沙龙主题为《字节高性能开源微服务框架：CloudWeGo》。</td></tr><tr><td>后端</td><td>字节跳动技术团队</td><td><a href="https://juejin.cn/post/7140223037646831647" target="_blank" title="https://juejin.cn/post/7140223037646831647">网关 Zuul 科普</a></td><td>微服务网关是介于客户端和服务器端之间的中间层，所有的外部请求都会先经过微服务网关。</td></tr><tr><td>后端</td><td>插猹的闰土</td><td><a href="https://juejin.cn/post/7140651064725864485" target="_blank" title="https://juejin.cn/post/7140651064725864485">如何设计一个消息中心</a></td><td>如今的内容型产品，不管提供的是什么类型的内容，在其主功能之外，不可避免的会有另一个十分重要的功能——消息中心。今天我们将重心放在消息中心上，聊一聊如何设计一个消息中心。</td></tr><tr><td>移动端</td><td>yeanyue</td><td><a href="https://juejin.cn/post/7140825514108780580" target="_blank" title="https://juejin.cn/post/7140825514108780580">[译] 2021 年的 SwiftUI: 优势、劣势和缺陷</a></td><td>本文的目的是帮助你理解 SwiftUI 的利弊，这样你可以就 SwiftUI 是否适合下一个项目做出更明智的决定。</td></tr><tr><td>移动端</td><td>程序员江同学</td><td><a href="https://juejin.cn/post/7140672092550201381" target="_blank" title="https://juejin.cn/post/7140672092550201381">Gradle 进阶(二)：如何优化 Task 的性能？</a></td><td>本节主要介绍了<code>Provider API</code>的使用，它有着如上文所说的一系列优点，现在官方的<code>Task</code>属性都改成<code>Provider</code>了，我们在开发自定义<code>Task</code>时也应该尽量使用惰性属性</td></tr><tr><td>移动端</td><td>二流小码农</td><td><a href="https://juejin.cn/post/7140455497454321700" target="_blank" title="https://juejin.cn/post/7140455497454321700">Android极简MVVM，从一个基类库谈起</a></td><td>这篇文章，主要详细介绍如何封装一个MVVM的基类库，以及MVVM架构模式在实际业务中的用法，最后会把实际的封装代码开源，并提供远程依赖，方便给到大家使用以及二次修改，尽量做到细致入微，浅显易懂，OK，废话不多赘述，我们进入正文。</td></tr><tr><td>移动端</td><td>sy007</td><td><a href="https://juejin.cn/post/7140113885528326181" target="_blank" title="https://juejin.cn/post/7140113885528326181">Android点击事件防抖设计与实现</a></td><td>点击事件抖动是每个项目都会遇到的体验问题, 如何省时省心的处理是我们每一位开发者要思考的问题。这篇文章我将带你从原理到实践来完成一个功能完善的点击事件防抖插件。</td></tr></tbody></table>
<h2 data-id="heading-2">优秀作者推荐｜下午茶</h2>
<p>推荐作者来源于月榜上榜作者，欢迎大家关注榜单小助手，了解更多优质作者：<a href="https://juejin.cn/user/4433674252325966/posts" target="_blank" title="https://juejin.cn/user/4433674252325966/posts">juejin.cn/user/443367…</a></p>























<table><thead><tr><th>领域</th><th>用户名</th><th>简介</th><th>个人主页链接</th></tr></thead><tbody><tr><td>前端</td><td>不够优雅</td><td>while (true) &#123;</td><td><a href="https://juejin.cn/user/2137904993804951" title="https://juejin.cn/user/2137904993804951" target="_blank">juejin.cn/user/213790…</a></td></tr><tr><td>移动端</td><td>程序员江同学</td><td>公众号：程序员江同学</td><td><a href="https://juejin.cn/user/668101431009496" title="https://juejin.cn/user/668101431009496" target="_blank">juejin.cn/user/668101…</a></td></tr></tbody></table>
<h2 data-id="heading-3">趣味码上掘金分享｜下午茶</h2>















<table><thead><tr><th>作者</th><th>代码介绍</th><th>简介</th></tr></thead><tbody><tr><td>旺仔米苏</td><td><a href="https://juejin.cn/post/7140920925226172447" target="_blank" title="https://juejin.cn/post/7140920925226172447">总在手机消消乐？电脑版 "月饼配对消消乐" 🔥来了！</a></td><td>实现一个<strong>月饼配对消消乐</strong></td></tr></tbody></table>
<p><span href="https://code.juejin.cn/pen/7140180271881519141" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140180271881519141" data-src="https://code.juejin.cn/pen/7140180271881519141" style="display: none" loading="lazy"></iframe></span></p>















<table><thead><tr><th>作者</th><th>代码介绍</th><th>简介</th></tr></thead><tbody><tr><td>幸运凡</td><td><a href="https://juejin.cn/post/7140981432498782222" target="_blank" title="https://juejin.cn/post/7140981432498782222">月饼太贵？那就用Three.js自己制作一个月饼，无死角观看！</a></td><td>利用 Three 实现一个<strong>3D月饼</strong></td></tr></tbody></table>
<p><span href="https://code.juejin.cn/pen/7140889807718187038" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140889807718187038" data-src="https://code.juejin.cn/pen/7140889807718187038" style="display: none" loading="lazy"></iframe></span></p>
<h2 data-id="heading-4">📖 投稿专区｜下午茶</h2>
<blockquote>
<p>大家可以在评论区推荐认为不错的文章，并附上链接和推荐理由，有机会登上下一期。文章创建日期必须在近1-3天内；可以推荐自己的文章、也可以推荐他人的文章。</p>
</blockquote></div>  
</div>
            