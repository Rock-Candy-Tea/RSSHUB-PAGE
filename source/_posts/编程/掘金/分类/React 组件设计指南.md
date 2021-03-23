
---
title: 'React 组件设计指南'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 21:42:42 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在我过往的经历里, 在面试与被面之间通常都会夹杂一些关于组件设计方面的问题, 但通常面试官和候选人都只能通过一些实际的项目经历来就设计进行讨论, 相比服务端面试中可能还涉及一些设计原则和基本思路, 但是在前端的面试过程中, 设计似乎成了一种经验.</p>
<p>但设计真的只是一种经验么?</p>
<p>显然不是, 因为经验是对过去问题的总结, 并且经验是没有标准没有约束的, 每个人经历的项目, 团队, 业务形成了每个人属于自己的独特的研发经验. 而设计其实就是在这些经验上不断提炼加工总结出来了的研发标准.</p>
<p>而前端组件研发在设计方面就目前来看是毫无标准可言的, 这种现状导致前端组件研发成了一项经验性技能, 是否能开发出高度可扩展, 结构清晰易于使用的前端组件不是通过科学合理的设计, 而是基于开发者过往的经验. 这导致有经验的前端组件库维护者成了一种稀缺资源.</p>
<p>基于这样的现状, 我想试着从 React 组件设计的角度去展示过去几年我从各种组件研发经验中提炼出来的一些东西, 或许能给各位带来一些灵感.</p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">前端组件发展简史</h3>
<p>要聊前端组件设计, 必然离不开对前端组件发展历史的探究, 关于这块我不会长篇大论, 毕竟这不是本文的核心内容.</p>
<p>以我的经验来看, 前端组件大致经历了这样几个阶段.</p>
<h4 data-id="heading-3">早年门户网站下, 以原生 JavaScript 为主的脚本化组件</h4>
<p>我记得 8 年前我刚开始写前端的时候, 做的第一个组件就是一个悬浮的广告组件, 如果你工作年限够长, 应该对 2010 年左右流行的大门户网站的左右悬浮广告颇有印象.</p>
<p>此时的前端组件通常就是一段的 JavaScript 脚本, 利用锚定特定的 DOM Id, 通过 IIFE, 来构建一个相对独立的运行环境.</p>
<p>这时候的前端组件符合当时主流开发对 JavaScript 的印象 - 玩具语言.</p>
<blockquote>
<p>2013 年其实是此类组件的末期, 因为 jQuery 崛起了.</p>
</blockquote>
<p>随着 jQuery 的崛起, 大幅提升了 DOM 操作的便捷性, 同时 jQuery 内生的插件机制将前端组件引入了插件化时代.</p>
<h4 data-id="heading-4">jQuery 带来插件化组件</h4>
<p>jQuery 插件能够大幅提升当时前端研发的效率, 彼时 AJAX 虽然较为流行, 但前端的角色还是更贴视觉交互这一层, 类似 bootstrap 将常用的 jQuery 插件进行整合, 提炼了在我看来是当时第一代通用前端组件的雏形.</p>
<p>包含了最常见的轮播图, 导航菜单, Tips 等.</p>
<blockquote>
<p>那个年代, 是否能手写轮播图是考验一个前端工程师的黄金标准</p>
</blockquote>
<h4 data-id="heading-5">一代神作 Angular 1.0</h4>
<p>15 年以后加入这个行业的年轻人可能很难理解当时我们对 Angular 的那种痴迷. 可以说 Angular 很大程度上奠定了目前前端研发中的一些核心要素.</p>
<p>包括</p>
<ul>
<li>模块化</li>
<li>基于前端的单页路由</li>
<li>ViewModel</li>
<li>数据驱动</li>
</ul>
<p>当然最重要的一点, Angular 带来了有别于 jQuery 的前端组件研发思路, 通过内置的模块系统将前端组件拆解成了几种不同的类型</p>
<ul>
<li>数据型组件</li>
<li>操作 DOM 的指令</li>
<li>带有路由的组件</li>
</ul>
<p>可惜好景不长, Angular 大包大揽的路线最终没能适应时代发展的需求. 随着 React 和 Vue 的快速崛起, 一家独大变成了三足鼎立</p>
<h4 data-id="heading-6">虚拟 DOM 和 JSX</h4>
<p>React 的走红给前端组件研发带来了两个重量级的概念, 虚拟 DOM 和 JSX, 这两个特性分别解决了在此之前前端组件研发的两个问题</p>
<ul>
<li>手动操作 DOM 的低效和不易维护</li>
<li>Angular 带来的前端组件设计上的分裂.</li>
</ul>
<p>基于 React, 无论是数据型还是交互型, 在前端组件设计上都统一了. 都是标准的 React 组件.</p>
<blockquote>
<p>Google 主导的 webcompoent 虽然红极一时, 但从现在的情况来开有点无疾而终的意思. 不过我依然倾向于认为前端组件的 web 化是未来的趋势, 至于是不是 webcompoent, 可以拭目以待</p>
</blockquote>
<p>上述简史不包含各种有趣的细节和历史的分支, 我只是大概罗列了下几个相对重要的节点, 如果你对这段历史有兴趣可以留言, 后续我会单独开一篇详细讲讲</p>
<h3 data-id="heading-7">当下 React 组件设计上存在的问题</h3>
<p>虽然 React 通过框架级的设计将前端组件统一成 React 给定的模型, 但在实际研发的过程中, 大统一的方式并不能解决组件类型的问题, 并且随着前端研发日趋复杂, 这一块就我看来几经进入了混沌领域.</p>
<p>让我们换个角度来看 React 组件设计, 比如提个问题, 现在的 React 组件有设计可言么?</p>
<p>当我们用 React 进行开发的时候, 我们如何定义组件?</p>
<p>我想答案是千差万别的, 因为这成了一种经验.</p>
<p>通过不同的维度, 我们会发现现有的 React 组件设计中存在大量的不确定性</p>
<ul>
<li>
<p>基于通信的角度, 我们将组件定义为父子组件, 一个组件既可以是父组件也可以是子组件. 所以父组件和子组件的标准是什么? 如果是平行通信又该叫什么? 兄弟组件? 那深层嵌套下, 难道叫爷孙, 爷爷爷爷孙孙孙孙组件么?</p>
<ul>
<li>另外组件通信在实现上也缺乏标准, 基于事件管道? 广播, 单播, 基于路由?</li>
<li>还是通过 context / props? 或者挂在 classComponent 的 this 上?</li>
<li>引入 redux  mobx 或者其他的状态管理库?</li>
<li>用 hook 不用 hook</li>
</ul>
</li>
<li>
<p>基于 React 框架的角度又可以定义各种不同类型的组件, 比如 classComponent, functionComponent, HOC, 受控和非受控组件, 自定义 hook 算组件么? 状态什么时候用 useState, 什么时候用 useReducer, useContext 的使用标准是什么?</p>
</li>
<li>
<p>基于业务角度的定义, 用户中心, 账户组件, 通知, 和公司特定业务挂钩的组件</p>
</li>
<li>
<p>基于视觉角度的定义, 表格, 表单, 导航, 对话框</p>
</li>
</ul>
<p>这些缺乏设计标准的不确定性给 React 组件设计带来了非常大的困难, 可以说正是因为这些不确定性, React 组件, 或者说前端组件压根就没有设计可言.</p>
<blockquote>
<p>类似 AntD 这样的组件库更多是从视觉和用户体验的角度出来来定义前端组件, 但是正如我上面提到的, 前端组件包含的角度非常多, 单纯通过一个角度去定义组件, 组件的扩展性就会收到很大的影响, 就拿 AntD 的表单组件来看, 实际使用中要扩展成符合自己公司业务的就很难, 你只有二次开发这一条路可选.</p>
</blockquote>
<p>如果用 React 和 Vue 做个对比, 我觉得从这个角度看, React 和 Vue 并不是同一种东西, React 是一个并不关心真实研发的 UI 库, 它的重点在于如何更高效的实现 UI 渲染, 并在这种高效渲染中能够完成和外部状态的连接</p>
<p>可以看成 React 是一个渲染函数的管理引擎, 从设计上, 他们一直致力于提升渲染函数的执行效率和性能, 同时让注入参数不会对这种效率和性能产生影响, 这也是为什么会有 hook. 因为 classComponent 在性能和效率上有明显的瓶颈</p>
<p>但是 Vue 不同, Vue 更像 Angular, 是一种包含了前端研发各方面诉求的研发框架, 虽然有些杂.</p>
<p>因此我认为两者并不等价, 也不具备可比性.</p>
<p>扯远了, 让我们回到本文的主题 React 组件设计</p>
<h3 data-id="heading-8">让我们试着消除 React 组件设计中的不确定性.</h3>
<p>假设我们基于以上的不确定性, 讨论 React 组件的设计标准, 那这个设计标准应该具备</p>
<ul>
<li>可实施, 可以转化为某种框架</li>
<li>多角度, 不从单一角度去定义前端组件</li>
<li>更高的抽象, 在多个角度之上统一进行组件抽象.</li>
</ul>
<p>结合上述的不确定性, 我们可以将 React 组件抽象出一些特性</p>
<ul>
<li>视觉性</li>
<li>交互性</li>
<li>数据性</li>
</ul>
<p>考虑到 React 是状态驱动的, 其核心就是对 State 的管控. 因此围绕 React 组件的设计可以进一步将特性扩展为</p>
<ul>
<li>
<p>特性性</p>
<ul>
<li>状态</li>
<li>操作函数</li>
</ul>
</li>
<li>
<p>视觉性状态和视觉性操作函数</p>
</li>
<li>
<p>交互性状态和交互性操作函数</p>
</li>
<li>
<p>数据性状态和数据性操作函数</p>
</li>
</ul>
<p>在此基础上, 根据不同特性处理的问题我们可以进一步给出定义</p>
<ul>
<li>
<p>视觉性状态</p>
<ul>
<li>直接用于渲染的文本/数字...</li>
<li>样式, 用于增强视觉</li>
<li>动效, 在样式的基础上加入绘制过程</li>
</ul>
</li>
<li>
<p>视觉性状态操作函数, 将输入状态转换为视觉性状态的函数, 例如 transform</p>
</li>
<li>
<p>交互性状态</p>
<ul>
<li>描述交互动作的标志, 例如 open, close...</li>
<li>描述页面间的状态, 例如 url 上的 query</li>
<li>组件运行环境变化带来的状态, 例如浏览器下的 onLoading</li>
</ul>
</li>
<li>
<p>交互性状态操作函数, 触发用户和组件交互的行为控制函数, 例如 controller</p>
</li>
<li>
<p>数据性状态</p>
<ul>
<li>来自外部输入的数据, 比如接口</li>
<li>本地缓存的数据, localStorage, 磁盘, 文件</li>
</ul>
</li>
<li>
<p>数据性状态操作函数, 用于和外部数据进行互通的控制函数, 例如调用 api 的 service</p>
</li>
</ul>
<p>根据这些标准, 在 React 组件设计中可以酌情去判断一些设计的合理性.</p>
<p>例如</p>
<ul>
<li>
<p>状态的定义是否不符合标准, 常见的将服务端传回来的数据直接渲染在界面上. 对于组件来说, 这回导致视觉性和数据性混淆, 当接口变更时产生连带的影响. 也不利于组件的可复用性.</p>
</li>
<li>
<p>在 onClick 又写交互又写样式控制, 将视觉性和交互性混淆, 这种往往会导致一些性能问题, 尤其是在编写一些动画效果的时候, 同时影响代码的复用性.</p>
</li>
</ul>
<p>除了这些还有 交互性和数据性混淆, 数据性操作函数直接操作视觉性和交互性状态等等.</p>
<blockquote>
<p>事实上在实际操作中, 即使明确了标准也很难严格的执行, 这和开发团队本身的能力有很大关系, 但就像建筑行业, 有高水平的施工团队, 牛逼的设计事务所, 也有门口摆摊的包工头, 全凭经验的小施工队, 一个成熟的行业是有其包容性的, 但不能全是小施工队.</p>
</blockquote>
<p>要将这些标准实施, 将设计融入到日常的组件开发里, 仅仅靠约定是远远不够的, 所以我提到了标准要具备可实施可转换为框架的可能性.</p>
<p>我们团队目前就在尝试研发此类框架, 之前在几篇文章中也有提到, 有兴趣的可以看看.</p>
<p>git 地址: <a href="https://github.com/kinop112365362/structured-react-hook" target="_blank" rel="nofollow noopener noreferrer">github.com/kinop112365…</a></p>
<p>事实上对于这块内容我们一直在实践和调整. 目前来看核心目标是希望能在 React 组件研发上形成可实施的设计标准, 同时提供研发配套.</p>
<p>至于更长远的目标, 应该是推动前端组件的 web 化吧.</p>
<h2 data-id="heading-9">后话</h2>
<p>一个没有标准的行业是不成熟的, 一个凭经验办事的行业是低效的, 前端面对的问题, 促使前端天然就对组件化有很强的诉求, 前端研发的过程也是组件研发, 装配, 调试, 运行的过程, 前端组件不应该仅仅是几个组件库那么简单, 而是应该结合科学合理的设计标准, 在日常的研发工作中也可以被很好的应用. 只有融入设计, 前端"工程师" 才名副其实, 虽然这条路看起来还很长.</p>
<p>如果你对此有强烈的兴趣, 并且想参与这个过程, 欢饮加入我们团队, 你可以通过微信(sh112365362)或者留言联系到我 😁</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            