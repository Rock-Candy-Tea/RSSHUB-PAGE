
---
title: '腾讯开源企业级设计体系 TDesign'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/pEde6hJEe2a7A9vjLTt0.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 27 Dec 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/pEde6hJEe2a7A9vjLTt0.jpg'
---

<div>   
<blockquote><p>编辑导语：TDesign是腾讯打造的一款企业级设计体系，那么TDesign是一个什么样的设计体系？它又有哪些设计特性值得注意？本篇文章里，作者对腾讯打造的这款企业级设计体系TDesign做了详细解读，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5266723 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/pEde6hJEe2a7A9vjLTt0.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>TDesign 是来自腾讯内部近 300 名设计师与开发者共同打造，经由 500+ 项目使用、验证和锤炼过的企业级设计体系， 秉承包容、多元、进化、连接的价值观，TDesign 期望与用户、行业及合作伙伴等一起打造具有竞争力的产品体验。</p>
<p>从设计出发，TDesign 提供了完整的设计语言、视觉风格指南和设计资源，以及基于 Vue2、Vue3、React （Vue3、React 目前仍在 Alpha 版本迭代中）等业界主流技术栈的组件，帮助开发者可以快速开发桌面端、移动端和小程序端等多个版本的应用程序。</p>
<p><img data-action="zoom" class=" wp-image-5266692 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/k72RkMPnucL1g9RmRK5C.gif" alt width="621" height="349" referrerpolicy="no-referrer"></p>
<p>如果你对于 TDesign 感兴趣，可以打开 TDesign 官网，体验 TDesign 。如果你对 TDesgin 诞生的历史感兴趣，不妨来看看 TDesign 诞生背后的故事。</p>
<h2 id="toc-1">一、腾讯开源协同，TDesign 成长的土壤</h2>
<p>自 2019 年开始，腾讯正式宣布在内部推行开源协同，鼓励所有源代码对公司内部全部开放，共同协作。</p>
<p><img data-action="zoom" class=" wp-image-5266695 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/43StjmoqXH90Uo830R3F.jpg" alt width="622" height="350" referrerpolicy="no-referrer"></p>
<p>也正是这样的开源协同的背景，使得腾讯的设计师和开发者们思考到：“有没有可能通过开源协同，解决过去腾讯内部团队分别维护设计体系，各设计体系之间质量参差不齐的问题”。出于这样的目的，在腾讯内部建立起了开源协同团队，来共同思考和研究这个问题，在 2020 年 2 月份，通过多次远程会议，确定了 TDesign 的产品目标和技术路线，并在全员的参与下共同投票选出 TDesign 的名字。</p>
<p>但 TDesign 应该是什么样的设计体系？</p>
<p>设计师们找到了答案：<strong>TDesign 应当是一个拥有包容、多元、进化、连接的价值观，期望为用户、行业及合作伙伴等打造具竞争力的品牌与产品体验的设计体系。</strong></p>
<p><img data-action="zoom" class=" wp-image-5266697 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/th9FNXx4r5KfS1b2erWa.gif" alt width="635" height="357" referrerpolicy="no-referrer"></p>
<ul>
<li>包容，是为了让 TDesign 兼容并蓄，既能满足当下需求，也能应用于更广泛场景；</li>
<li>多元，是 TDesign 应当能够赋能不同业务，探索无限可能；</li>
<li>进化，是 TDesign 应当成为一个动态的设计体系，在“以用户价值为依归”的基础上，成长进化；</li>
<li>连接，是 TDesign 需要用最大的努力去连接赋能，联动融通。</li>
</ul>
<p>有了目标和价值观，TDesign 也真正开始进入落地的阶段。</p>
<h2 id="toc-2">二、从协同到开源，TDesign 成长的历程</h2>
<p>在项目刚刚落地时，通过内部发起的贡献者招募，大批设计师和开发者带着原有业务组件的经验、成果和满腔的热血，在很短的时间内产出了大量的设计稿和组件，完成了项目的初始化建设。但因为对跨技术栈维护组件库的复杂度认识不够，各个框架中对同一组件的文档和 API 实现都有差异，用户使用组件库体验不一致的问题，一直困扰着 TDesign 团队。</p>
<p>为了解决协作的问题，TDesign 在进行第二期迭代时，通过一系列工具和工作流程来规范组件的开发过程，选择更加开源风格的异步 issue 讨论，开发了工具来自动生成各个框架的 API 定义和描述文档，引入 CI / CD 流程来降低人工参与的比率，从而减少因为人而犯错的可能。通过引入机器人的方式，来提升信息推送的效率，让每一个人都可以时刻知道什么事情是需要做的，什么事情是不需要做的。</p>
<p>借助于这些更加“开源”风格的工具和协作方式，TDesign 的效率得以提升，让 TDesign 在进行二期开发时，比预期更快地完成任务。</p>
<p><img data-action="zoom" class=" wp-image-5266698 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/aT2a9PJpfJEyHjIq97Ld.png" alt width="652" height="367" referrerpolicy="no-referrer"></p>
<p>借助于异步和聚焦的讨论方式<strong>，</strong>问题可以被更加深刻地讨论和思考，从而更容易得出一个符合预期的结论，在开发时能够以更高的效率完成组件的封装和代码的编写。也正是这样更加开源的方式，最终构建出了如今的 TDesign。</p>
<p><img data-action="zoom" class=" wp-image-5266701 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/hs7CODcYoGbLFjbGT603.jpg" alt width="647" height="364" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、从设计到研发，TDesign 的特性有哪些？</h2>
<p>作为一款企业级设计体系，TDesign 的特性可以总结为如下三点。</p>
<h3>1. 完整：完整的技术、设计资源，将设计与开发者从重复劳动中释放出来</h3>
<p>TDesign 为开发者提供了多种主流开发技术栈的支持：TDesign 已经支持了 Vue2、Vue3、React 和移动端小程序的开发，其他技术栈如 Augular、Flutter 也有相应贡献团队正在开发。</p>
<p><img data-action="zoom" class=" wp-image-5266700 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/y0qzwA3TSaoK8u9VTx1S.png" alt width="644" height="362" referrerpolicy="no-referrer"></p>
<p>为了实现开发与设计之间的高效协同，TDesign 中包含了丰富可复用的设计组件资源，如色彩体系、文字系统、动效设计、图标元素、布局结构等，覆盖支持 Axure、Sketch、Figma、Adobe Xd 等各大产品设计软件，将设计和开发者从重复劳动中释放出来。</p>
<p>除了常规设计资源，TDesign 还提供了辅助设计工具如 Sketch 设计插件，也支持在腾讯 CoDesign、即时设计、Pixso、墨刀等市面常用设计工具中使用 TDesign 设计物料。</p>
<p><img data-action="zoom" class=" wp-image-5266704 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/SBIzGECqtIafvOam0muk.png" alt width="645" height="363" referrerpolicy="no-referrer"></p>
<h3>2. 一致：一致的设计和开发体验</h3>
<p>TDesign 将腾讯内部多年设计经验提炼总结为专业的设计指南，其所提供的通用设计解决方案，能够帮助产品经理、设计师、开发者等角色高效完成企业级产品的设计和研发，并保持设计语言和风格的一致，满足用户体验的要求。</p>
<p>基于 TDesign 的设计体系规范，TDesign 同时上线了组件库的桌面端和移动端，提供了多个技术栈实现版本。通过一系列协作流程和辅助工具，保证各技术栈组件 API 和实现产物一致。借助这些能力，使得项目即便使用了多种不同的技术架构或技术栈，开发者也可通过 TDesign 通用设计组件库进行开发，显著降低学习成本，在构建统一/多端覆盖/跨技术栈的前端应用时更具优势。</p>
<p><img data-action="zoom" class=" wp-image-5266703 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/drPgaaKeWvbesbIaGnXt.png" alt width="645" height="363" referrerpolicy="no-referrer"></p>
<h3>3. 易用：清晰的设计指南和开箱即用的解决方案</h3>
<p>TDesign 设计体系在形成过程中，提炼了不同业务、场景的设计经验，提供了通用的设计指南以降低使用门槛。对于不同企业产品的品牌定制需求，TDesign 支持使用者对设计风格进行扩展，目前已经将设计样式梳理归纳为 Design Token，形成一套企业内部的语义化设计规范，方便后续进行统一的管理和使用扩展。</p>
<p><img data-action="zoom" class=" wp-image-5266705 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/LcvycEd5D5qKDibdrtQs.png" alt width="644" height="362" referrerpolicy="no-referrer"></p>
<p>在主题配置方面，TDesign 提供了明亮和暗色两种模式，支持一键切换，提升用户的使用体验。后续，TDesign 还会推出针对于不同垂直领域的行业组件，覆盖更多的业务范围。产品团队可以借助内置的行业主题，快速配置对应需求，启动业务开发。</p>
<p><img data-action="zoom" class=" wp-image-5266706 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/GHqkoqrElxhKs8Hi3TJb.gif" alt width="644" height="362" referrerpolicy="no-referrer"></p>
<p>TDesign 同步上线了一款开箱即用的中后台框架 TDesign Starter Kit，开发者可以通过它快速体验组件功能，也可以将它修改为项目基础脚手架工程，快速实现从 0 到 1 的产品开发上线。</p>
<h2 id="toc-4">四、从过去到未来，TDesign 还将做些什么？</h2>
<p>通过开源，TDesign 期待持续打磨出更加完善易用的组件库，包括在国际化、无障碍和适老化方面有更成熟的解决方案，对更多的产品和使用者有帮助。</p>
<p>借助社区，TDesign 期待与更多产品设计师和开发者有专业交流<strong>，</strong>甚至是收获一个积极活跃的 TDesign 社区。</p>
<p>非常期待你对 TDesign 的持续关注和反馈意见。更欢迎同道中人的你参与 TDesign 的开源共建，与 TDesign 从开源到更加成熟的旅程中一起进步。</p>
<h2 id="toc-5">五、如何体验 TDesign ？</h2>
<p>您有两种方式使用或体验 TDesign：</p>
<ol>
<li>访问 TDesign 的官网：https://tdesign.tencent.com</li>
<li>访问 TDesign 的 GitHub 主页：https://github.com/Tencent/tdesign</li>
</ol>
<h2 id="toc-6">六、致谢</h2>
<ul>
<li>感谢参与 TDesign 的近 300 名同学的支持，在 TDesign 从 0 到 1 的过程中贡献了宝贵的经验、代码、组件、文档、建议等等所有的付出，使 TDesign 得以起步，得以服务用户；</li>
<li>感谢腾讯内部开源协同的文化和技术委员会的机制，让 TDesign 得以在企业内部孵化孕育，让 TDesign 凝聚满腔的热血；</li>
<li>感谢开源的前行者，为 TDesign 的发展提供了理论和实践上的参考和各类开源工具的帮助；</li>
<li>感谢 InfoQ、CSDN、开源中国、51CTO、人人都是产品经理、优设网 等平台以及 前端之巅、前端早读课、前端大全、web前端开发、前端新世界、前端大学、龙爪槐守望者等自媒体，让 TDesign 可以为更多人所知。</li>
<li>感谢所有 TDesign 的使用者和关心者，你们是 TDesign 的启明灯，指引 TDesign 的前进方向，TDesign 与大家共成长。</li>
</ul>
<p><img data-action="zoom" class=" wp-image-5266708 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/qARjkiet5rJ39ZlnjsuM.png" alt width="645" height="352" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图为 TDesign 的贡献者们</p>
<p> </p>
<p><strong>推荐关注公众号 “腾讯设计”（ 微信ID：TencentDesign ），第一时间获取腾讯官方的设计方法论</strong></p>
<p>本文由 @腾讯设计 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5264024" data-author="1310486" data-avatar="http://image.woshipm.com/wp-files/2021/08/ngyC6ihPsBUeFSC3GYJZ.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            