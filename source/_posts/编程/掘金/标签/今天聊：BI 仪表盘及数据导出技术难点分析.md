
---
title: '今天聊：BI 仪表盘及数据导出技术难点分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b309b184df1a489692a04a2dd9b5bde9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 15:51:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b309b184df1a489692a04a2dd9b5bde9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十九届|前端数据可视化专场，高强度一次性洞察可视化的前端玩法，7-17 全天直播，9 位讲师，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2Ftl29" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/tl29" ref="nofollow noopener noreferrer">报名上车👉 )：</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b309b184df1a489692a04a2dd9b5bde9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2F2021" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/2021" ref="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十五届 - 前端早早聊报表专场，也是早早聊第 109 场，来自 字节 - Jerry 的分享。</p>
</blockquote>
<h2 data-id="heading-1">一、开场</h2>
<h4 data-id="heading-2">简单的自我介绍</h4>
<p>Hello 大家好，我是来自字节跳动商业产品客增大前端团队的前端工程师 Jerry，很荣幸今天能代表团队向大家一起分享我们最近的一些业务实践，因为我们现在刚好在做一款商业 BI 系统，所以适逢今天的主题，我将为大家带来一场 title 为《<strong>如何实现商业报表的仪表盘及导出分享功能</strong>》的技术沉淀。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4d22a73bfff4113b14573512e62c8e4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">字节跳动最“挣钱”的前端团队</h4>
<p>首先先介绍一下我们的团队：我们是一个已经有百号人的前端团队，我们的同学也遍布在北京、上海、杭州以及北美这些地方，这些城市都有我们的 base，我们在做的事情，是致力于<strong>提供互联网商业变现的最佳解决方案</strong>，<strong>践行“信息创造价值”理念</strong>。</p>
<p>在这里，你将对接字节跳动百亿流量的<strong>全产品矩阵</strong>，见证公司<strong>全新业务线的孵化成长</strong>，支撑公司<strong>千亿规模的收入增长</strong>。在这里的每一分每一秒，你都能亲身感受到字节跳动的蓬勃生机。虽然我们是业务团队，但我们也在做很多与时俱进的技术建设，其中包括有：前端现代化工程化体系升级、Node 能力探索、一键式 CD 工具、组件服务化、前端国际化通用解决方案、可视化页面搭建系统、商业智能 BI 系统、前端自动化 E2E 测试、面向未来的微前端设计模式等等。</p>
<p><strong>在支撑业务不断演进的过程中</strong>，<strong>我们尝试不断探索技术赋能业务的更优实践</strong>。并且在分享的最后也有我们的福利环节噢，我将为大家献上咱们团队的内推绿色通道，如果大家听完我的分享，觉得我们在做的事情很有趣，你对此感兴趣，那就欢迎快来投递哟。</p>
<p>好吧，那题外话咱们就不多说啦。在我们正式开始今天分享之前，首先需要感谢下我们的组织同学。辛苦我们的主持人花花帮我们暖场，也感谢 Scott 提供了这样一个让我与大家能够一起交流的机会。那我们现在开始直奔咱们的主题吧。</p>
<h4 data-id="heading-4">分享大纲</h4>
<p>这是咱们今天分享的大纲：我会逐步带着大家切入咱们要开发一个报表系统的几个核心细节，带着大家从业务实际需求场景入手，一步步完成一个前端商业报表系统的搭建。其实我今天准备了五十多页的 PPT，因为做一个 BI 系统有太多有意思或者说值得去讲的东西了，我很希望把所有的都分享给大家，但因为时间关系，我可能只能抽出其中一部分，因此我尽可能让它们能更加通俗易懂，并且我会更多地专注在前端的一些主要功能的实现思路，当然一个 BI 系统肯定远远不止这些。整个分享的过程或许会比较漫长，希望今天来听我的分享的同学，听完之后也都能有所收获。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94105937920642ad96dba7f74fc58bca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以咱们今天的分享主要有以下几个部分：</p>
<ul>
<li>大数据时代下的前端商业分析方案</li>
<li>定制化数据分析能力的实现</li>
<li>仪表板制作</li>
<li>大数据分享及到处</li>
<li>对业务更深的思考与对未来的展望</li>
</ul>
<p>那现在，开始我们第一个主题吧。</p>
<h2 data-id="heading-5">二、大数据时代下的前端商业分析方案</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9864842ba394e51a122f4aae053fa64~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">大时代的趋势</h4>
<p>作为做互联网的我们，其实对过去几十年的历史进程都历历在目。首先，20 世纪的前十年，是 PC 端的时代，各类门户网站的崛起，也启蒙了现代的许多互联网巨头；过去的十年，是移动端的时代，各路诸侯都在争夺互联网的战场，最终的赢家，奠定了现如今的互联网格局。而现在，是数据的时代，因为很多时候，大量的数据或是强大的数据分析能力，能够成为一家公司的核心竞争力。因此，<strong>数据</strong>，<strong>是这个时代最核心的资源</strong>。现在不论是 B 端还是 C 端的团队，都会有大量的数据积累，例如我们平时常见的页面埋点、PV、UV，亦或是一些业务数据，都如同一座座数据金矿，等待我们去发掘其中价值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec54681a8454c468b09d7f6fa0fb687~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">业务的实际场景</h4>
<p>而我们，恰好在做这样一件事情。因为我们是商业化大部门下的团队，所以在我们的大部门中，沉淀了很多有意义有价值的数据，比如我们的一些销售业绩、或者是一些客户数据。为此，在我们的部门下，也聘请了很多专业的数据分析师同学，亦或是销售自己，平时可能都会做一些报表、周报，用以汇总数据，观察趋势，就如下面的这张图所示，左侧的日报图，就是我们业务中实际产出的报表，我们的同学可能会做一些日报类的报表，用以披露部门内的一些销售业绩动态。他们会自己通过 Excel 等工具，在拿到数据后自己绘制各种各样的图表，然后像这样组装起来，再发送出去。而右侧的报表图，就是我们的同学使用了我们研发的系统后，自己组装完成的报表，效果也符合他们的预期。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33d144b0f1294757a1fc11bbb4537e4c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">业内的竞品</h4>
<p>而且这样的业务场景其实是一件很常见的事，并不是说只在字节存在，就像我们刚刚提到的，在如今的时代大背景下，每家公司沉淀出了大量待发掘的数据已经是一件再普通不过的事情了，因此，也有很多公司发现了这样的商机，在业内也做出了很多成熟的产品。比如比较有名的 Tableau，虽然它已经开始逐步放弃中国市场了，但是功能和交互，也值得很多系统参考，国内也有很多很给力的产品，像阿里的 QuickBI，因为作为云服务的提供方，BI 类系统的产生可以说是再正常不过了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86f061114ad246859e4c9b30496d14f5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">我们为什么要做这样一件事？</h4>
<p>那业内已经有这么多成熟的产品了，为什么我们还需要做这样重复的事情呢？我们是在重复造轮子吗？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55f26961560e4b3a98436a532ae583fd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实主要是处于以下四点原因：</p>
<ul>
<li><strong>部门内现存大量有价值的数据</strong>：刚刚我们提到，因为我们是商业化部门，因此有大量的营销类数据沉淀也是一件再正常不过的事情了。</li>
<li><strong>大量重复性的报表工作</strong>：刚刚我们提到，其实我们的销售同学，或者数据分析师，都是下载了数据之后，自己通过 Excel 或者其他工具绘制好图表，然后制作成报表，而且周而复始，每次发周报，或者双月总结，都要不断重复做同样的事情。我们希望能帮助他们，提供能力自动化帮他们完成一些重复的工作。</li>
<li><strong>需要有特定的数据权限管控</strong>： 众所周知，其实数据在公司内是很敏感的，对于数据的权限也是需要严格管控的。传统的模式，用户直接讲数据下载走之后，数据的流向以及最后的分发，我们都无法追踪，这其实是一件很有风险的事情，我们希望借助我们商业化现有的鉴权体系，对我们的数据加以更严格的管控。</li>
<li><strong>我们希望用户在一个系统里，就能做完所有事</strong>：我们不希望就是用户还得在我们的系统里面下数据，然后切换到 Excel 里面去拼装数据，然后又得到另一个系统里面去发周报，我们希望能让用户，在我们自己研发的一个系统里，就能完成他们平时工作中的所有事情。</li>
</ul>
<h4 data-id="heading-10">我们该怎么做？</h4>
<p>根据我们刚刚的分析，其实用户每周的工作，主要就是以下三个核心的流程：制作他们所需要的每一张图表 -> 将这些图表组装成仪表板 -> 最终将这张图表以周报的形式分享出去，或者定时用以给自己回溯。顺着这样一套流程和思路，我们开始来逐步分析每一个阶段都需要哪些功能模块，并且又有哪些技术选型能够帮助我们实现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88687381095a4c568bfd12706457b317~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">三、定制化数据分析能力实现</h2>
<p>接下来来看业务流程的第一个环节，也是一份报表最核心的组成单元 —— <strong>图表</strong>。那图表从哪来呢，自然，我们需要为用户提供图表的生产能力，也就是我们的定制化数据分析能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2649fa9f38f744c3a1dbc5463686a701~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">用户需求分析</h4>
<p>那用户期望的效果又是怎么样的呢？参考业内的系统实现，用户其实根本不需要关心背后繁杂的 SQL 逻辑来满足自己的数据查询，也不用自己绘制图表，只需要通过简单的通过一些拖拖拽拽，就像我们图中的动图所示，比如说拖拽一些我们提供好的数据字段，我们就可以快速地查询出这样的一个他所想要的数据，或者说是快速地帮他绘制出来一张图表，然后用户也可以自由地选择图表的类型，比如说想要做成一个折线图，或者是我们普通的这样一个 Table 样的交叉表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f126bb55103141018020198e203825f1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">技术体系梳理</h4>
<p>所以要实现一个定制化的数据分析能力，我们大概需要哪些功能点去支撑呢？这里我们整体可以分为如下这几部分：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20abe52119df465d91b35b87520d1b16~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如刚刚一下就映入眼帘的<strong>拖拽能力</strong>，这也是市面上的竞品做的比较常见的一个能力，我们可以借助像 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-dnd%2Freact-dnd%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-dnd/react-dnd/" ref="nofollow noopener noreferrer">react-dnd</a> 这样的优秀的开源实践，来帮助我们去实现这样一个能力。</p>
<p>第二点的话是用户可能不会满足于我们提供好的一些默认字段，像比如说我们可以看到系统左侧这部分的字段 List，可能这些字段并不能满足用户他实际的更复杂的数据分析场景，用户可能需要自己来生产一些这样的一个字段表达式，其中可能包含像求和、求平均等一系列复杂的计算操作，能够让有更加定制化的能力。所以为了让功能更加定制化，我们也会提供自定义字段（或者更形象点说就是自定义查询查询表达式）的能力。</p>
<p>当然我们的这样一个定制化的分析的页面，核心肯定还是我们的图表展示。我们可以基于 antd 的 Table，去实现 Table 类型的像比如交叉表这类的数据呈现，并且我们可以使用 ECharts，来实现像图表类的数据呈现。
我们可以选择 Mobx 作为数据流支撑，因为它很“灵活”，至于为什么，咱们来看下面这张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f466eddb9919435a987d202b7fc09597~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将刚才页面其实可以做一下类似图中各部分的功能拆分。首先是我们左侧的这样一个字段拖拽的 List，用户可以从这边去把字段拖入到像我们刚才看到这样的一个有行、列、数值分类的一个个容器里面，这部分的区域我们就叫他分析区，因为他是用来产出可用于后端查询的一个字段分析配置。借助 Mbox 的 Autorun 能力，当分析区配置变化之后，会自动触发后端查询获取到对应的图表数据，交给我们底部的面积比较大的核心图标展示区，用于展示我们绘制后的图表。</p>
<p>不仅如此，我们还可以看到在页面的右侧还有这样一个侧边栏，提供给用户选择图表类型的这样一个能力，还有一些让用户能够自由定制化图表样式像比如说什么开启或关闭合并单格，或者是添加一些表格样式，比如隔行变色这样一些比较常见的能力。当配置改变之后，可以通过 Mbox 的 Observer 机制自动去更新一些图表的元数据或者状态，触发图表的重新渲染。</p>
<p>那梳理完清晰架构设计之后，我们就开始去逐个去击破吧</p>
<h4 data-id="heading-14">字段拖拽</h4>
<p>首先来看我们最开始说到的字段拖拽能力。前端如何实现一个拖拽功能呢？了解过这方面的同学肯定会想到比如 HTML 原生的 drag 事件等等。当然，我们也能借助一些工具库帮我们快速完成，比如我们系统中使用的 react-dnd，就是很不错的选择。</p>
<p>回到主题，我们想要实现一个拖拽能力，核心就是把握住 PPT 上的拖拽三要素，因为不论你的业务逻辑是什么样，这三个要素始终是你所有功能的基点：</p>
<ul>
<li><strong>拖拽环境（DragDropContext）</strong>：类似于我们平时包裹数据流的时候都需要用到的 Provider，能够为它的所有子元素提供这样一个拖拽底层支持的全局上下文；</li>
<li><strong>拖拽项（DragSource）</strong>：就是我们实际拖拽的东西，比如大家刚刚看到的一个个字段；</li>
<li><strong>放置容器（DropTarget）</strong>：我们拖拽的东西肯定不能一直拖着吧，它肯定需要被放到某个地方去，那这个地方就是我们所说的放置容器。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d0805f53ba4f9e9c9e79b16e702d14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那要如何用实际的代码逻辑实现拖拽三要素呢？我们可以借助 react-dnd 为我们提供的 DragSource 和 DragTarget 方法，对我们的组件进行包装即可，我们只要定义好可拖拽的类型、拖拽事件的回调、亦或是我们想要自定义的能力，比如图中所述，我们对拖拽中的元素会赋予特定的样式 —— 透明度增大，就能完成一个拖拽要素的封装。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4354cbb495e74f14b17652ef098c2169~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且，我们将重复的流程封装了高阶组件（因为我们的项目在启动时，react-hooks 还只是刚火起来的提案），这样
当我们要快速包装组件的时候，一切是不是变得简单了许多呢：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d279aa117934418b0572d69ddc29e34~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样一来，我们想要为系统中的哪个元素赋予一些拖拽能力，只需要包裹一个装饰器就 OK 啦。这样的工具函数，就能实现我们的拖拽能力“随时插拔，随处复用”。</p>
<p>并且细心的同学可能会发现，我们的字段其实是有不同的类型，分析区内也有不同的位置，并且顾名思义，像行、列这些分析区，在交叉表内自然是不同的逻辑或者呈现，举一个比较简单例子，像比如说我们把日期类的这样一个字段拖入到过滤器里面，它应该呈现的是一个像日历这样的一个组件，然后我们把一些维度类的字段拖入到过滤器里面，它可能展示的就是一个向下拉枚举或者说是一个搜索框的这样一个组件呈现。</p>
<p>我们可以用很多判断去堆砌，但怎样才能更优雅地去维护这块的逻辑呢？其实细心的同学可能发现了，我们将字段拖入分析区的结果，其实是一个二维的过程，它取决于字段的类型和拖拽终点的类型，因此我们使用一个矩阵来表述这样的过程，矩阵最终的求值，就对应着不同情况下，我们所需的组件和配置。比如我们右侧这样一个示例代码，我们把日期类这样一个字段，去拖入到我们这样的一个行中，它就映射到了我们这样的一个矩阵中的 date 字段下的第一项，然后这个配置就是对应着字段最终要产生的组件，还有它数据初始化元信息或者说一系列的配置信息。</p>
<p>这样一来，我们后面想要维护这样的一份配置，配合上直观的注释，其实就很简单了，像比如我们现在想要加一些什么分析区的配置，其实就只要在矩阵里面去额外的去增加一些项目就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf0d68e4f494ded98daf8709e3113a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">自定义计算表达式</h4>
<p>有了字段拖拽之后，用户并不满足于我们提供的默认字段，很多时候，用户都希望自己能有自定义字段表达式的能力。我们可能不会让用户完整去写复杂的 SQL，我们希望这个系统能够更加简易，能够降低门槛服务于更多的用户，因此我们有了自定义的语法结构，比如由我们提供的函数和字段，用户就可以快速地组装好一个表达式，正如我们图中的动图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1bb4d7892cd4f40a061167272b3f87c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>借助 CodeMirror，我们很快就能实现这样的能力。</p>
<p>首先，CodeMirror 能够为我们提供非常优秀的关键字高亮能力。了解过编译原理的同学一定知道，对于一段字符串的解析过程，会分为词法解析和语法解析等几个步骤，在这里，CodeMirror 为我们提供了在词法解析的环节，我们可以定制化处理关键字的能力，我们可以抛出每个 token 对应的类型，CodeMirror 就会为我们指定的关键字赋予特定的 class，我们就能为其定制想要的样式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aa1caccffe640e39085b870bf60e619~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不仅如此，CodeMirror 还支持让我们自定义语法提示菜单。我们只要准备好待提示的 List，在用户输入或者粘贴的时候，filter 好 list 喂给 CodeMirror 就行了。借助每个 list item 的 render 方法，我们还可以自由定制下拉菜单里的样式，开发起来起来就像使用 Echarts 或者 Antd 这样的组件库一样舒适。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7656afb76d54cf58430e57ef7d6c9b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里有一个小技巧，其实自动补全后光标是位于补全文案的最后的，对于函数类的文案，我们可能会更希望它的光标是落在函数的括号 ( ) 里，因此当我们检测到用户在通过自动补全键入函数的时候，手动操作移动光标，将它移动到括号内：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2982d8deeb594bf1a603c163ebba70e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">图表渲染</h4>
<p>有了字段，自然就可以从后端查询数据啦。那对于前端来说，我们最终要渲染的是如图所示的这样一张交叉表，很明显我们需要的是结构化的数据，而后端直接将字段通过 SELECT 查询出来的结果数据一定是铺平的，从接口响应到数据渲染，必然会需要有个数据格式化的过程。那这个过程谁去完成呢，如果前端来做，对服务器性能更友好，后端就不需要关注数据格式化，可以专注在数据分析而查询，而如果后端来做，对我更友好，哈哈，开个小玩笑。当然，肯定是极致的性能更为重要。那数据格式化我们有怎样的思路呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/440685ad46f6485c997c1720e951ad57~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以对数据图表进行细化，如果要渲染一个单元格的数据，那么这个数据单元格一定会有一个唯一的坐标，坐标从哪来呢？其实就是他的行列字段所组成的数据索引。我们可以封装一个数据处理器，就是我们图中的 Processor，对后端给到的数据 list 进行结构化，变成更加直观的 DataMap。</p>
<p>我们可以看到，经过格式化之后的 DataMap 里，一级的 Key，就对应着 DataSource 里的一行数据，而二级的 Key，就对应着当前数据所在的列，这样每一个单元格的数据，都可以通过这样的“坐标”被明确表示出来，当我们再拿着这个 DataMap 去生成 Antd 的 DataSource 和 Columns 时，一切是不是就清晰明朗多了。其实这个过程就是一个再普通不过的树生成逻辑，<strong>我们部门面试常考题噢</strong>，<strong>哈哈划重点</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0022b406d7e49ca9fcb439b7e65c3ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于 Echarts 相关的图表，今天我就不做过多介绍啦，我相信前端早早聊大会之前的数据可视化专场已经有很多类
似的议题啦。</p>
<p>终于搞定了我们的图表来源了，接下来就是咱们系统的核心，组装图表。</p>
<h2 data-id="heading-17">四、仪表板制作</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22df51c464984f4885b66ab2f4cf80cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么我们要把一张张图表组装起来呢？</p>
<p>因为：<strong>多张图表组合产生的价值</strong>，<strong>一定大于所有图表单张价值的总和</strong>。多张图表去做一个协同分析或者做一个数据关联的话，肯定是能够迸发出更多的价值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e876e4c6e4984e8da96261df2143a89d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那用户实际需要的，又是怎样的呢？</p>
<h4 data-id="heading-18">用户需求分析</h4>
<p>用户在业务中去制作的这样的一个报表，也就是像我们下方的图示，报表中会披露一些指标，会有一些图，其实就是咱们前一步做好的那些图表，同时也会有一些这样一个文案总结，比如总结一下部门或者说团队这个月去有没有什么上升的趋势。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab93be84efb4876b5943a6fa69fa671~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而要支撑起一个仪表板功能，我们需要哪些部分呢？</p>
<h4 data-id="heading-19">仪表板技术架构</h4>
<p>从下而上，我们可以使用这些技术为仪表板提供能力支撑。仪表板中会有一些原子组件组成仪表板的必要元素，比如我们刚刚做完的图表，还有一些富文本卡片，或者说是一些图片组件，当然也有在仪表板中很常见的全局筛选器，用以让用户全量地去过滤一些数据。</p>
<p>有了原子组件之后，我们也希望能赋予用户拖拽布局的能力，让用户可以在系统中自由组装这些原子组件，然后产出一份能让他自己满意的报表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e069de47267c4c18bd150cdca5cf746d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>梳理清晰了技术体系，那我们就自下而上逐步攻坚吧。</p>
<h4 data-id="heading-20">富文本能力实现</h4>
<p>原子组件里，比较有挑战的，应该就算是富文本编辑器了，这个曾经作为前端三大难题的技术点，如今优秀的前端社区已经为我们准备好了成熟的解决方案 —— Quill，它不仅能帮助我们快速实现富文本编辑功能，还能够让我们自由地自定义各项能力，这相比于其他的工具而言是更优秀的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4837864c0f428982bd0fdf9ad57af2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如我们可以自定义工具栏的内容。我们可以通过自由组装 HTML 标签的形式，自定义富文本工具栏的呈现。比如
说 Button 元素，它最终在这样一个工具栏中渲染出来的就是一个按钮，比如说我们这样的一个加粗功能的按钮，或者是一个添加下划线的功能按钮。然后像有一些下拉菜单这样的功能，我们可以通过 select 配合 option 快速实现，比如选择字体字号，这也是一个比较常用的实现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7e0506fe2bc4deca4734e578a276bb9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不仅如此，我们还可以为 Quill 增加一些自定义的功能，比如 Quill 默认只支持四种字号，所以我们也能赋予它定制化字号：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3f72b5feba2432a9d0c1459ca250dd7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>得益于 Quill 灵活的定制化能力，我们能接下很多 PM 给到的各式各样的定制化需求。</p>
<h4 data-id="heading-21">拖拽布局能力</h4>
<p>有了仪表板的基本元素之后，我们就可以开始关注自定义布局的实现了。其实社区已经有一款特别好的实现了，就是我们的使用的 react-grid-layout，可以看它官方提供的 demo，其实效果就已经足够满足我们的需求了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9215c4b69ff44688055c1f293da9dfb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过这里有一个小优化，大家也可以关注一下。就是官方提供了一个自适应宽度的能力，但是它本质是监听了window 的 resize 事件，然后大家刚刚如果有注意的话，其实我们的系统是有一个可伸缩的侧边栏的，所以当我们去伸缩侧边栏的时候，这个仪表板它不会去适配这样一个宽度。因此我们可以借助 react-resize-detector 对他进行一个扩展，简单优化一下官方的这个小痛点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4edbbc2ba5a1492e8b656d189170f78c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了让数据管理更加清晰，我们将布局和数据的渲染逻辑拆分开来，有单独的配置维护布局数据，另一份配置维护组件元数据。所以仪表板整理的布局流程就是类似图中所示：首先我们真正存在后端的，就是一份完整的仪表板数据，像比如说它里面有哪些组件，并且有怎样的布局。然后前端系统通过请求拉到这样的一个数据信息之后，我们会做一个解析，我们会把这样的布局信息映射到每一个对应的组件上。最终这些绑定了布局信息的各个原子组件，经过我们的布局器布局，最终呈现出来的就是用户自由组装的美观的仪表板啦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1707d49277da4382b03058ec7095fee6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">全局筛选器</h4>
<p>全局筛选器对于一份 BI 仪表板而言是再常见不过的一个功能了，很多时候，我们都会提供一个仪表板层面的筛选器，供给用户自定义筛选数据的能力。筛选器可以与任一图表相关联，并且这些筛选项也只会对关联的图表生效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58f8ac857173474aa8c1bbbfad857e9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们就举一个形象一点的例子（下图）。比如在我们的仪表板中有三个筛选器，筛选器 123，然后他们分别关联了不同的图表，筛选器 1 关联了图表 1，筛选器 2 关联了图表 1 和图表 2，筛选器 3 关联了图表 2，自然，当我们操作筛选器 1 的时候，只有图表 1 会刷新，操作筛选器 2 的时候，图表 1 和图表 2 都需要刷新，而操作图表 3 的时候，也只能有图表 2 刷新。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a578aacf410b43c48f4aae3b8f315772~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那这样的逻辑又要如何用技术实现呢？整理的流程就像我们图中所示，我们可以在 Store 里去统一收集所有的筛选器，筛选器上都会有一个字段标明关联的图表的信息，当筛选器发生变化时，就会自动更新我们的 Store，Store 会自动触发筛选器的生成器，针对不同的图表生成不同的筛选项，图表再根据不同的筛选项去向后端请求数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa29932650b1408fb911c221b595f191~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样一来，一个仪表板的核心骨架功能基本就已经搭建完成了，大家可以看看我们仪表板的最终使用效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/759f6b8ac6d047538576319e27685717~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但其实我们还没有完成所有的事情。</p>
<h2 data-id="heading-23">五、大数据分享及导出</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7c40135c8f3421790347f6d30d3259e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先有一点我们需要明确，那就是：用户制作的报表，一定是希望它能被带到更多系统之外的地方去展现。因为用户制作的报表，肯定不是自己做着玩的，或者自己欣赏它的“美”，更多的时候，他肯定是希望拿着这样的一份报表去发周报，或者是或者说去做这样的一个数据分析结果的汇报。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/828e5794fb12439abb7f2811dde6ad53~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，能够将数据导出或者分享，也是一个 BI 系统不可或缺的能力。</p>
<h4 data-id="heading-24">数据分享的形态</h4>
<p>数据的导出分享，其实可以归纳为以下三种形态：</p>
<ul>
<li><strong>链接分享</strong>：比如用户直接 copy 了浏览器地址栏里的系统链接，或者是我们的页面里有个按钮叫做类似“复制链接”，用户点击以下，就能自动把图表的链接复制到剪切板中，这样就能将他自己做的图表或者报表直接分享出去；</li>
<li><strong>图表导出</strong>：用户可能希望自己做的图表或者报表，能够导出成一张图片或者 Excel 文件，这样在他需要发送邮件或者消息的时候，就能更加直观；</li>
<li><strong>周报订阅</strong>：一个比较智能的系统，肯定不会说让用户每周或者每次他需要的时候，来系统里截个图，才能把它的报表分享出去，我们完全可以做的更智能化，比如说把这样一个流程做的更加自动，用户只需要快速配置，我们就可以定时地为用户去推送他所需要的报表信息，比如截图、链接等等。</li>
</ul>
<h4 data-id="heading-25">链接分享</h4>
<p>我们先来看分享的第一种形态 —— 链接分享。用户点击 Button 之后，就能把内容自动复制到剪切板。其实这也是一个比较常见的实现，我们只要创建好一个 input 标签，将需要复制的内容填充到里面，执行 input.select() 选中所有的内容，再通过浏览器提供的 document.execCommand('copy')，就能把对应的内容复制到剪切板中啦。这样的逻辑，我们也可以封装成常用的工具函数，用于其他场景下的复用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/581cd9e75ba940fc9f0b5d82082c0ac7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-26">图表导出</h4>
<p>对于图表导出的话，我们需要先掌握前端下载能力的实现。如果前端想要让用户下载一个文件的话，其实要做的事情很简单，就是创建一个 a 标签，它支持我们为 href 赋予 Blob 这样的 ObjectURL，并且再为它赋予一个 download 属性用来表示下载后的文件的文件名，这样我们只需要执行一下这个 a 标签的 click 操作，就能模拟出用户下载文件啦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca21c1a8b2744e8d8e77c1223bfa30e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于我们的文件而言，比较常见的就是一个 file string，图片类型的，大部分也可以导出一个 base64，我们都可以封装好工具函数，将他们转化成 Blob 对象。最终让用户能够灵活地完成下载。</p>
<p>有了前端下载能力的支持，就可以针对不同的文件进行定制化的处理。对于页面上的 Table 类元素，用户可能更希望的是导出一份所见即所得的 Excel 文件，我们可以借助 js-xlsx，它为我们提供了一个方法叫做 table_to_sheet，只需要传入一个我们页面中的 table HTML 元素，这个工具就会自动帮我们解析成 Excel 文件格式的数据，并且也会保留我们页面中的合并单元格等样式，最后生成一段 file string，我们直接就能使用刚刚提到的文件下载能力，将文件导出啦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/375af6dd2e0a49d78c47fd778b4d8760~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而对于图表类型的图表，熟悉 canvas 的同学可能就会比较亲切了，canvas 提供了一个名叫 toDataURL 的 API，能够快速将 canvas 内的内容导出一份 base64 数据。而对于一些非 canvas 的元素，比如我们的指标卡图表，他可能就是一个纯粹的 Card，我们也可以使用 html2canvas 快速将它变成一张图片。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9168b7cc277d48edbd861684b31df860~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-27">周报订阅</h4>
<p>刚才我们还说到一点，我们还可以把报表的导出流程做的更加自动化，用户不必要每次需要报表的时候再来我们的 BI 系统里生成一份报表导出，我们可以提供让用户自由配置的能力，比如用户选好什么时候需要为它推送报表，或者说是定期给某些人，系统就会自动去定时为用户推送报表。</p>
<p>最终一个形式化其实就是类似于我们右边这张图的呈现。如果用户订阅好了一份报表，系统就会定时地在飞书上为它推送这样一条消息，其中就包含了用户制作的报表的一个截图，然后还有一个报表对应的链接。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeed38b9742144c9b35b414f2356407b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后如果要实现这样一个订阅能力的话，如果大家有了解过 Linux 的话，就会知道 crontab 这样的一个实现定时能力的命令，整体的思路其实就是借助这样的能力去支撑，我们公司为我们封装好了这样的一个能力，我们称它为 cronjob，然后用户他如果创建了一个订阅任务之后，我们就可以把它写到我们的定时调度数据库里面，接下来去创建这样一个定时任务，当触发的时机到了的时候，我们就可以借助无头浏览器，类似业内比较成熟的 puppteer，自动打开报表为我们的用户去做报表的截图，最终再将截图带着我们的一些报表信息推送给用户。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b0fe0e2d514d5b8d26d71b52f4f934~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-28">六、对业务更深地思考与未来的展望</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb6f4f9bca84ca8845319486efb0735~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实在整个业务的迭代演进过程中，我们的 BI 系统也有了一个更深的思考，而且我们也希望对未来有更远的展望。其实我们是更希望现在 BI 系统能够成为一个更灵活的数据中台，不单单去服务于业务，像比如我们现在已经实现的能力，如果别的业务想要复用我们系统制作的报表，他直接通过 iframe 的形式将我们系统内的报表嵌入到他们的系统中。并且我们未来也希望能借助像微前端这样的能力，让我们系统中的报表，亦或是一些图表组件，能够不局限于我们的开发框架，也能快速地被其他系统更灵活地复用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a57853cdd0d433d8f171eae40c45ad6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>数据中台的真正意义</strong>，<strong>不单单是业务上的可复用性</strong>，<strong>我们也会不断探索技术上的可复用能力</strong>。</p>
<p>所以对我们而言：一切还只是开始，未来仍存挑战。我们后面还有微前端、移动端、大屏展示等等能力想要去做，我们也相信，很快我们也能做到，所以对我们所做的事情感兴趣的小伙伴，快快加入我们吧，咱们一起去做有挑战的事。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3c8f0477add4237b6596ba29a533406~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">七、总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61c8f56efabb477fb7110a2298cfccd2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们再整体回顾一下我们刚刚讲完的内容，我们也可以借助业内优秀的实践作为我们的技术底层实现，快速支撑起我们的报表系统的技术选型和基建，再将各种各样的技术抽象成通用的能力封装，创造出我们的定制化数据分析能力（提供了图表来源）、仪表板原子组件（提供仪表板的必要组成元素）以及数据导出分享能力（支持 BI 系统的必要功能），最终再将我们所拥有的资源进行整合封装，就产出了我们提供给用户的定制化报表解决方案。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/829416d018534767bd9daed6773bbe2a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-30">八、福利环节</h2>
<h4 data-id="heading-31">书籍推荐</h4>
<p>然后前端早早聊有一个惯例，就是每次分享的嘉宾都需要分享一本书，这里我推荐的就是这本《The Grammar Of Graphics》，当时 D3.js 的作者，就是看完了这本书之后，有了灵感，写出了 d3.js 这么优秀的框架。但其实我更想表达的，就是在 BI 系统的这段历程下来，我更深刻地理解到：<strong>做一个商业分析系统</strong>，<strong>最重要的事不是攻克哪些技术难点</strong>，<strong>而是要善于去发现数据的价值</strong>，<strong>用技术为数据赋予生命</strong>。因此我觉得这本书，再合适不过了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86ea58d9f80b4cf79aa6ec0b8e10603c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我也想要表达一下我对团队的感谢，一个系统的搭建，肯定不是一个人就能完美完成的，在这里我不仅要特别感谢一路来和我一同奋斗的同事们，这些成果是大家共同努力的结晶，我们也希望未来还能有更多的同学能够参与进来，因为就像我们刚刚说的，我们做的都还只是开始，我们还要做的事情还有很多，我们需要你。</p>
<p>​
前端路漫漫，与君共勉，大家对于大厂选拔标准有任何疑问，都可以在评论区留言，我都会回复，或者加我也行（codingdream），还可以围观我朋友圈。</p>
<hr>
<p>别忘了第二十九届|前端数据可视化专场，7-17 全天直播，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.huodongxing.com%2Fgo%2Ftl29" target="_blank" rel="nofollow noopener noreferrer" title="https://www.huodongxing.com/go/tl29" ref="nofollow noopener noreferrer">报名上车👉 )：</a></p></div>  
</div>
            