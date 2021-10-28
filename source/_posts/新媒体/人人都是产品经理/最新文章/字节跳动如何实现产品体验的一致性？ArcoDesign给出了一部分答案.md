
---
title: '字节跳动如何实现产品体验的一致性？ArcoDesign给出了一部分答案'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/xw4LM0abrXClT0ijCTNR.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 28 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/xw4LM0abrXClT0ijCTNR.jpg'
---

<div>   
<blockquote><p>编辑导语：产品设计这一环节至关重要，它关乎到最终的用户使用体验。此时，若能降低设计和开发之间的沟通损耗，提升二者的协作效率，将可以有效保障产品落地后的用户体验。那么，不妨来看看文章里介绍的企业级设计系统——ArcoDesign。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5192497 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/xw4LM0abrXClT0ijCTNR.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在圣经的故事里，传说曾经全人类都讲同一种语言，并计划建造一座通天的巴别塔。为了阻止巴别塔的建成，上帝打乱了人类的语言。由于在建造过程中无法沟通交流，巴别塔的建造状况百出，最后不了了之。</p>
<p>一款互联网产品的诞生，往往要经过需求分析、产品分析、产品规划、产品设计和产品落地五个阶段，需要产品经理、UI、前端、后端之间的密切协作。其中，产品设计直接关乎到产品落地的形态和最终的用户体验，如何消除协作中面临的沟通信息损耗，让设计和开发的协作更加容易和高效，一套统一的“语言”或将起到事倍功半的作用。</p>
<p>近日，一款名为ArcoDesign的企业级设计系统，在由稀土掘金技术社区主办的首届稀土开发者大会上全新开源。设计系统是一种思维，也被视作设计师与前端开发沟通的一种语言。据ArcoDesign的开发者、来自字节跳动GIP UED和前端架构技术团队介绍，让<strong>设计和开发无缝协作，</strong>专注用户体验的提升，是ArcoDesign要重点解决的问题之一。</p>
<p>ArcoDesign官网：https://arco.design</p>
<p><img data-action="zoom" class=" wp-image-5192476 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/L6cre2KP2GZvBlpriXBt.png" alt width="718" height="345" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、关于ArcoDesign</h2>
<p>在正式推出并开源之前，ArcoDesign 曾经以技术中台的形式在字节跳动内部运行了三年，已经支持了字节内部超过 4000 个项目，是字节内部使用规模最大的设计系统。</p>
<p>ArcoDesign 拥有系统的设计规范和资源，依据此规范提供了覆盖 React、Vue、Mobile 的原子组件。基于丰富的原子组件，Arco 除了提供风格配置平台、物料平台的定制化工具外，还提供包括图标平台、品牌库、Arco Pro 最佳实践的资源平台，<strong>旨在帮助设计师与开发者解放双手、提升工作效率、高质量地打造符合业务规范的中后台应用。</strong></p>
<p><img data-action="zoom" class=" wp-image-5192480 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/OW10i59ie44tCdBGOqhi.png" alt width="717" height="403" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、ArcoDesign想解决哪些问题</h2>
<p>在过去的 3 年里，字节跳动内部中后台产品业务量的迅速增长对传统的设计与开发方式提出了很大的挑战。随着项目变大，模块和页面变多，视觉风格和交互越来越难以统一。</p>
<p>同一个业务平台下，不同模块的视觉风格和前端开发框架都可能大相径庭，这对于<strong>用户体验和平台的一致性</strong>造成了巨大的困扰。</p>
<p>ArcoDesign的初衷就是想从源头上去解决平台的差异性和一致性问题，又快又好地提升各个平台的设计质量。</p>
<p>具体来看，ArcoDesign在<strong>个性化定制能力</strong>、<strong>二次开发+复用能力</strong>、<strong>设计+开发更好地协作</strong>方面有所突破。</p>
<p><img data-action="zoom" class=" wp-image-5192481 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hAzsR8Dyr799wepAmKbB.png" alt width="716" height="392" referrerpolicy="no-referrer"></p>
<h3>1. 个性化定制能力</h3>
<p>不同的团队风格，不同的业务场景，对视觉风格会有不同的需求。</p>
<p>以往，不论有没有设计参与，整体的技术选型都是比较自由的，有的团队选择 React ，有的选择 Vue；有的组件库是面性设计，有的组件库是线性设计。当设计给出设计图，开发需要在项目里进行各式各样的样式魔改。</p>
<p>在项目变多之后，为了更小成本的维护和代码重用，一般会基于所选组件库封装一个新的组件库，这个二次开发的组件库对组件的风格样式和默认行为进行魔改，魔改需要开发花费大量的时间成本，但基本是唯一的解决方案。</p>
<p>然而，只要涉及到魔改，就不可避免地会遇到升级问题。只要升级底层组件库，就有可能导致样式甚至功能出现出现不可预知的改变，为了求稳，就需要锁版本，锁了版本又没办法享受版本升级带来的新特性和 bug 修复，陷入一个恶性循环的怪圈。</p>
<p><img data-action="zoom" class=" wp-image-5192482 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/0vkFgWSMJwMgAcckv91m.png" alt width="719" height="381" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">魔改容易造成的恶性循环</p>
<p>为了解决样式定制难这个痛点，Arco 从设计之初就对组件进行了细致的拆分。</p>
<p>组件是设计系统提供的最底层能力。Arco 提供了 67 个基础组件，这些基础组件足以支撑绝大多数的业务需求。</p>
<p><img data-action="zoom" class="aligncenter  wp-image-5192796" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Y94EyQnhjEDvrLANrApm.gif" alt width="722" height="451" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">一键切换“暗黑模式”</p>
<p><strong>1）风格样式定制</strong></p>
<p>ArcoDesign将影响组件视觉的样式都抽离到了 token 之中，token 是最小化描述组件样式的变量，组件库中是以 less 变量的形式存在。从全局变量到组件级变量，用 token 来解释组件，用上千个 token 变量，来保证通过配置变量，就能对样式风格进行任意定制。</p>
<p>比如现在越来越多的网站会考虑支持暗色风格切换，“暗黑模式”会让使用者更加专注自己的操作任务，同时在夜间或暗光环境使用下可以减少屏幕光对眼睛的刺激，避免在黑暗环境中长时间注视高亮光源带来的视觉刺激。ArcoDesign支持一键开启暗黑模式，无缝切换，流畅体验。</p>
<p><strong>2）默认行为定制</strong></p>
<p>Arco 支持 60+ 组件默认行为的全局配置，以极大的灵活性，减小维护成本、提升开发体验。用户只需要维护一份全局配置，就能定制每一个组件的默认交互。</p>
<p>值得注意的是，除了上述能力，ArcoDesign还有助于<strong>简化传统项目上线前反复验收的繁琐流程</strong>。</p>
<p><img data-action="zoom" class=" wp-image-5192484 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/358dDBQbwO9VYkGxPxcd.png" alt width="716" height="393" referrerpolicy="no-referrer"></p>
<p>传统的情况是，当设计确定设计稿，开发通过上述提到的样式定制和默认行为定制去定制符合设计规范的基础组件，在上线之前需要反复地跟 UI 进行样式还原验收，同时从设计稿到研发再到 UI 走查验收。</p>
<p>Arco 提供了样式可视化编辑的<strong>「风格配置平台」</strong>。基于风格配置平台<strong>所见即所得</strong>的组件配置能力，用户可以对全局样式和组件样式做细粒度的调整，实现<strong>「ArcoDesign to Any Design」，</strong>大幅提升流程效率。</p>
<p><img data-action="zoom" class="aligncenter wp-image-5192797" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/eWRqIuNMXZw75GihNHUR.gif" alt width="716" height="403" referrerpolicy="no-referrer"></p>
<p>在配置完成之后，用户可一键发布主题到主题市场，提供优秀的主题风格给社区。在主题市场上，用户可以浏览所有主题，自由地进行选用。</p>
<p><img data-action="zoom" class=" wp-image-5192486 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/JT2FE0SnNSrEDhSDHDkK.png" alt width="716" height="387" referrerpolicy="no-referrer"></p>
<p>依托系统的 ArcoDesign 设计规范，<strong>即便是无设计师参与的平台产品，ArcoDesign也可以帮助开发者快速构建专业、一致的体验。</strong></p>
<h3>2. 二次开发和复用能力</h3>
<p>得益于 Arco 组件灵活的 API 设计以及物料平台提供的定制化组件解决方案，用户可以基于 Arco 快速开发满足自身特定需求的定制组件。定制化的组件将更好地复用业务代码，促进团队协作，提升开发效率，更可与社区共享丰富的物料资源。</p>
<h3>3. 设计和开发更好地协作</h3>
<p>Arco希望通过提供全流程完善的生态体系，提升设计、开发全流程工作体验。</p>
<h2 id="toc-3">三、全流程完善的生态体系</h2>
<p><img data-action="zoom" class=" wp-image-5192487 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CHzLNVXAKzgNhu6uADNj.png" alt width="716" height="340" referrerpolicy="no-referrer"></p>
<h3>1. 生态平台</h3>
<ul>
<li>风格配置平台：通过协助用户构建个性化主题，帮助用户更好地管理不同风格的主题配置，提高设计和开发的协作效率。</li>
<li>物料平台：基于 Arco 脚手架工具快速进行定制化的业务组件开发、共享，实现业务模块的解耦与复用，提升开发效率，促进团队协作。</li>
<li>图标平台 IconBox：提供规范化、统一化的高质量业务图标库。</li>
<li>中后台最佳实践 Arco Pro：帮助用户快速的从 0 到 1 搭建项目，支持用户自由选用常见页面模版。</li>
<li>色彩配置工具 ：帮助设计师和开发者在线调试颜色，探索 Arco 色彩算法。</li>
</ul>
<h3>2. 开发工具</h3>
<p><img data-action="zoom" class=" wp-image-5192488 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/LoMWSZyuuQZAF1xF7OG3.png" alt width="720" height="379" referrerpolicy="no-referrer"></p>
<ul>
<li>Webpack 插件：帮助开发者在 Webpack 构建中方便地使用主题、实现按需加载、替换组件内置图标。</li>
<li>Arco CLI 脚手架工具：封装了物料操作命令，帮助用户快速创建物料项目并将其发布至 Arco 物料平台。</li>
<li>VSCode 插件：帮助用户在编辑器查阅文档、可视化操作物料等。</li>
<li>Figma 插件：聚合了常见的设计工具，帮助设计师更方便地使用 Arco 的各项能力。</li>
</ul>
<h3>3. 设计功能</h3>
<ul>
<li>为了方便设计师定位资源，Arco 提供了资源定位的 Figma 插件功能，让设计师可以一键轻松找到目标组件的设计资源以及开发资源。</li>
<li>为了提高设计师的配色效率，Arco 提供了色彩配置的 Figma 插件功能，可以根据指定颜色通过算法智能生成明亮以及暗黑模式下的梯度色板。</li>
<li>为了提高制作图标的效率，Arco 提供了一键拖拽使用 Arco 图标的 Figma 插件功能，在线颜色、线宽、尺寸调整，灵活配置，游刃有余。</li>
<li>为了降低设计师制作 Figma 变体的成本，提高设计师产出符合设计系统规范的设计稿的效率，Arco 探索了 Code to Design，提供了以组件为维度的 Figma 插件功能，设计师可以通过在插件里配置组件属性，自动生成对应的设计元素。同时打通了风格配置平台，让设计稿可以轻松实现 「一键换肤」</li>
<li>为了方便设计师管理图标，Arco 推出了<strong>Iconbox 图标平台</strong>，旨在让设计师可以在该平台上高效地管理自己的图标。并且提供了图标上传的 Figma 插件功能，支持设计师在 Figma 中直接选中图标一键上传至图标平台。</li>
</ul>
<p>经过了近三年的迭代和众多产品的验证，Arco Design已经成为字节跳动内部使用量最大的设计系统，助力众多字节优秀产品打造高质量的产品体验。未来，可视化建站平台、D2C 设计图转代码工具、C2D 代码转设计图工具、品牌库等功能将陆续上线并开放。</p>
<p><img data-action="zoom" class="aligncenter  wp-image-5192798" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/IqxMQykiOAA51uUM1y2f.gif" alt width="722" height="407" referrerpolicy="no-referrer"></p>
<p>正如 「Arco」 这个名字一样，遵循【Agreement / 一致】、【Rhythm / 韵律】、【Clear / 清晰】、【Open / 开放】的理念，Arco 希望能<strong>帮助更多的用户提升工作效率和愉悦程度，打造更好的产品。</strong></p>
<p>Arco Design 现已正式开放，欢迎使用和体验。Arco 非常重视每一位用户的意见，希望大家踊跃反馈，积极共建。</p>
<p>Github React 组件库：https://github.com/arco-design/arco-design</p>
<p>Github Vue 组件库：https://github.com/arco-design/arco-design-vue</p>
<p> </p>
<p>本文由 @Cindy 投稿发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            