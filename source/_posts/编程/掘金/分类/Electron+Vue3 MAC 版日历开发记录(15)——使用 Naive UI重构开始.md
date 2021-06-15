
---
title: 'Electron+Vue3 MAC 版日历开发记录(15)——使用 Naive UI重构开始'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 06:21:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第15天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于昨天打了一个包并且可以正常安装和使用，这让我自己有了信心继续往下写。但同时也让给我看到了界面的「丑陋」和对自己 CSS 技术的无奈，所以接下来我将基于已有的功能，开始我的代码重构之旅，尽可能在未来的 15 天内重构成功，真正意义上输出一版，并上线 Mac APP Store 或者 发布到 Brew，让大家使用。</p>
<p>好了，在开始重构之前，说一说我的想法来源。</p>
<h2 data-id="heading-0">FullCalendar 出了 Vue 3 Demo</h2>
<p>因为刚开始使用 FullCalendar 时，还没有提供 Vue 3 的版本 Demo，所以选择了 Primevue 前端框架；随着 FullCalendar Vue 3 的出来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dd86ffb55174b629f3b557161e9ad16~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从我个人角度不太喜欢继续使用 Primevue 了，首先它来自国外，对国内的展示不太好看，最主要因为它提供的一些能力需要付费，国内基于 Vue 3 的前端框架还是不少，值得使用的。</p>
<p>这也是为什么在这前 15 天里我没有开始着手 CSS 的原因。</p>
<p>所以今天我们将开始重新选择基于 Vue 3 的前端组件。</p>
<h2 data-id="heading-1">从崇拜 antfu 开始说起</h2>
<p>这几天我无意间看到 <a href="https://github.com/antfu" target="_blank" rel="nofollow noopener noreferrer">Anthony Fu</a> 提交了不少开源的项目，已然成为他的忠实粉丝了。</p>
<p>其中有三个项目是我想借鉴的：</p>
<ol>
<li><a href="https://github.com/vueuse/vueuse" target="_blank" rel="nofollow noopener noreferrer">github.com/vueuse/vueu…</a>，作为 Vue 3 开发作者之一，写的一些通用的代码集，没理由不用。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4008ce2d00943cca906b4571d7a7c67~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><a href="https://www.naiveui.com/zh-CN/light/docs/introduction" target="_blank" rel="nofollow noopener noreferrer">Naive UI</a>，是一个 Vue3 的组件库。有超过 70 个组件，希望能帮你少写点代码。它比较完整，主题可调，用 TypeScript 写的，不算太慢。对于我来说完全够用了，而且我自己又是一个不会写 css 的人，只要引用它的组件即可，同时，如果哪天觉得它的组件不够用，我们完全可以基于它去构建新的组件来满足自己的使用。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6472ea99fffa4cc1994b2a31570370c8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li><a href="https://cn.sli.dev/" target="_blank" rel="nofollow noopener noreferrer">Slidev</a>，为开发者打造的演示文稿工具。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7bdb2f828b14c14a5490a3ab26336e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中他用的技术栈很符合目前我所需要的：</p>
<p><img src="https://cn.sli.dev/screenshots/cover.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它终将成为我代码的参照物，我好好学习它的结构和开发思维。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1b5e8e970e42708c87359052902d46~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以本项目在接下来的重构，以 <code>Naive UI</code> 为主，如果真的需要 CSS，那我也或者使用 <a href="https://windicss.org/" target="_blank" rel="nofollow noopener noreferrer">Windi CSS</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cf403fe8f1d40a89e499b49fb2756ff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">第一个重构点</h2>
<blockquote>
<p>代替使用 FullCalendar Vue 3.</p>
</blockquote>
<p>先把 <code>5.6.0</code> 版本换成 <code>5.7.2</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f860e9ab3e34043b482a032558d5a07~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">"@fullcalendar/core": "^5.7.2",
"@fullcalendar/daygrid": "^5.7.2",
"@fullcalendar/interaction": "^5.7.2",
"@fullcalendar/timegrid": "^5.7.2",
"@fullcalendar/vue3": "^5.7.2",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，我们也需要更新 <code>Vite</code> 插件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f5f0a8ccbc347888c230328b703b713~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，代码中我们修改引入了：</p>
<pre><code class="copyable">import FullCalendar, &#123; CalendarOptions, EventApi, DateSelectArg, EventClickArg &#125; from '@fullcalendar/vue3'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保持其他不变，我看看运行看看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/649bff5771be4c48bc3ade37700b5cf1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>日历可以显示，但是当我们点「显示农历」时，提示报错了，跟踪代码发现属性不对：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eba2ae0ceb8745098ab4f7e3dfa380ab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，配置基本没问题了，明天结合请求报错的问题，把 Events 也调整过来。</p>
<h2 data-id="heading-3">小结</h2>
<p>今天算是前半个月的一个收尾，和下半个月的开始，从 0-0.5，再由 0.5 提升到 1 的过程，欢迎持续关注，未完待续！</p>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p></div>  
</div>
            