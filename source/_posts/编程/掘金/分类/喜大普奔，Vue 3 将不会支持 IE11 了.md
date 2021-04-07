
---
title: '喜大普奔，Vue 3 将不会支持 IE11 了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/687539319fc24425b0ddcff90dc2790e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 15:34:40 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/687539319fc24425b0ddcff90dc2790e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>清明时节雨纷纷，尤大发文欲断魂。没错，小长假这几天，大家又被爱在假期搞事情的尤大的新闻霸屏了，就在 4 月 3 日凌晨，尤大在知乎发了一篇名为“<strong>[RFC] 关于 Vue 3 的 IE11 支持</strong>”的文章， 内容是关于 Vue 3 不再支持 IE11 的提案：</p>
<p><img alt="截屏2021-04-06 上午6.46.59.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/687539319fc24425b0ddcff90dc2790e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看到这条消息，心里竟然毫无波澜，<strong>因为我们被 IE 拖累实在是太久了</strong>。相信很多仍然在做 PC 端页面的同学深受 IE 其害，还记得我在 2009 年第一次做出网页时，还要<strong>关注 IE5 的兼容性</strong>；曾几何时，IE 兼容性问题还是前端面试的高频题目。一晃 12 年过去，IE11 也终于被微软自己抛弃了。</p>
<p>很多社区的同学第一时间对 RFC 的原文进行了翻译，我假期打了疫苗，一直休息来着，昨天才开始翻译的。除了 RFC 译文之外，我们先来看看这个新闻的一些知识点：</p>
<h2 data-id="heading-0">知识点</h2>
<h3 data-id="heading-1">什么是 RFC</h3>
<p>RFC 是英文 <strong>Request For Comments</strong>，意思是征求意见。在 React 也有 RFC。无论是 React 或 Vue，当作者或者开发者想要对其<strong>做出大量变化或者添加新特性时</strong>，一般都需要撰写一个提案，提案里面需要包含这件事的<strong>动机</strong>和<strong>详细设计</strong>。</p>
<p>React 在 2018 年 React Conf 提出的 <strong>React Hooks</strong> 就是以 RFC 形式提出的。这次的“关于 Vue 3 的 IE11 支持”也是 RFC，也就意味着，<strong>这件事需要征求社区的意见，并不是最终的决定</strong>。</p>
<p>不过呢，一般而言，RFC 都是经过深思熟虑的，被提到 RFC 的提案，尤其是作者本人的提案，<strong>基本都会通过</strong>，只是在讨论中补充更多的细节。</p>
<h3 data-id="heading-2">IE11 的现状 —— 亲爹都不爱</h3>
<p>微软抛弃旧儿子 IE 浏览器，将更多的精力投入到新儿子 Edge 上来。其很多核心产品都已经不再支持 IE11 了，如 Microsoft 365。如今 IE11 的全球使用率已下降至不足 1%。如此不堪的境遇，老旧的 IE 是该早点消失了。</p>
<h3 data-id="heading-3">Vue 不支持 IE11 了吗，IE 用户怎么办</h3>
<p><strong>当然不是</strong>，Vue 在 2.X 版本仍然支持 IE11，如果你想使用类似 Vue 3 的新特性，<strong>可以等等 Vue 2.7 版本</strong>。这次的 RFC 宣布，将会对 2.7 版本做<strong>向后兼容</strong>，移植 3.x 的部分新功能，以保证两个版本之间相似的开发体验。看到尤大的这个做法，我也收获了很多，很多时候换一个思路，就会海阔天空。</p>
<h2 data-id="heading-4">RFC 译文</h2>
<blockquote>
<ul>
<li>原文地址：<a href="https://github.com/vuejs/rfcs/blob/ie11/active-rfcs/0000-vue3-ie11-support.md" target="_blank" rel="nofollow noopener noreferrer">vue3-ie11-support</a></li>
<li>原文作者：<a href="https://github.com/yyx990803" target="_blank" rel="nofollow noopener noreferrer">尤雨溪</a></li>
<li>原文发布时间：2021-04-03</li>
<li>本文永久链接：<a href="https://github.com/Ivocin/Translation/blob/master/Docs/0000-vue3-ie11-support.md" target="_blank" rel="nofollow noopener noreferrer">github.com/Ivocin/Tran…</a></li>
<li>翻译、校对：<a href="https://github.com/Ivocin/" target="_blank" rel="nofollow noopener noreferrer">清秋</a></li>
</ul>
</blockquote>
<ul>
<li>开始日期： 2021-04-02</li>
<li>目标版本: 3.x</li>
<li>参考 Issue： N/A</li>
<li>实现 PR： N/A</li>
</ul>
<h3 data-id="heading-5">摘要</h3>
<ul>
<li>移除 Vue 3 对 IE11 的支持。</li>
<li>将精力转为把兼容特性向前移植到 Vue 2.7 版本中。</li>
</ul>
<h3 data-id="heading-6">动机</h3>
<p>从 Vue 3 启动开发开始，一直到 2018 年底，我们一直被问到有关 IE11 支持的问题。很多用户都问过，Vue 3 是否会支持 IE11，我们原本都计划是先发布 Vue 3，让它稳定下来，然后在后续阶段增加对 IE11 的支持。在漫长的开发过程中，我们另外还做了兼容 IE11 的研究和实验，但是由于其复杂性以及手头大量的其他工作，这项工作的优先级就降低了。</p>
<p>当我们在 2021 年再来看这个问题时，浏览器和 JavaScript 的情况都发生了巨大变化。现在更多的开发者使用现代语言特性，更为重要的是，<a href="https://techcommunity.microsoft.com/t5/windows-it-pro-blog/the-perils-of-using-internet-explorer-as-your-default-browser/ba-p/331732" target="_blank" rel="nofollow noopener noreferrer">微软自己开始积极推动用户远离 IE</a>，并对 Edge 持续投入精力。它还在<a href="https://techcommunity.microsoft.com/t5/microsoft-365-blog/microsoft-365-apps-say-farewell-to-internet-explorer-11-and/ba-p/1591666" target="_blank" rel="nofollow noopener noreferrer">自己的主要产品（如 Microsoft 365）中移除了对 IE11 的支持</a>。而就在几天前， <a href="https://make.wordpress.org/core/2021/03/25/discussion-summary-dropping-support-for-ie11/" target="_blank" rel="nofollow noopener noreferrer">WordPress 也做出了移除 IE11 支持的决定</a>。IE11 的全球使用率已<a href="https://caniuse.com/usage-table" target="_blank" rel="nofollow noopener noreferrer">下降至不足 1%</a>。当我们谈论面向公众的网站和应用时，IE11 的下滑趋势十分明显。</p>
<p>我们认为这是一个重新思考 Vue 3 支持 IE11 的好机会。</p>
<h3 data-id="heading-7">Vue 3 中支持 IE11 的成本</h3>
<h4 data-id="heading-8">行为不一致</h4>
<p>Vue 2 的响应式系统是基于 ES5 的 getter/setters。Vue 3 利用了 ES2015 的 Proxy 实现了一个更高性能、更完备的响应式系统，但无法在 IE11 中 polyfill 这一特性。这是我们最大的障碍，因为这意味着如果我们要支持 IE11，就必须发布两个不同行为的的版本：一个是基于 Proxy 的响应式系统，另一个则是基于和 Vue 2 类似的基于 ES5 的 getter/setters 特性的响应式系统。</p>
<p>Vue 3 的基于 Proxy 的响应式系统提供了近乎完整的语言特性覆盖。它能够检测到许多在 ES5 中完全无法检测的操作，比如属性到添加或删除，数组的索引以及长度变化，<code>in</code> 操作符检查。基于 Proxy 版本的代码无法在 IE11 里运行。这不仅仅给我们带来了技术上的复杂性，同时也给开发者造成了持续的心智负担。</p>
<p>我们原本的计划是在支持 IE11 版本的开发中同时发布 Proxy 和 ES5 的两种响应式版本。当它在支持 Proxy 的开发环境中运行时，会检测并对不兼容 IE11 的一些用法做出警告。这虽然在理论上可行，但是带来了极大的复杂性，因为它需要将两种实现混合在一起，而且增加了开发和生产环境行为不一致的风险。</p>
<h4 data-id="heading-9">长期维护的负担</h4>
<p>支持 IE11 也意味着我们必须对整个代码库中使用的语言特性做出考量，并为我们的发布版本找到合适的 poliyfill / 编译策略。每一个在 IE11 中无法被 polyfill 的新特性都会带来新的行为警告。一旦 Vue 3 承诺支持 IE11，直到下一个大版本发布之前都无法摆脱它了。</p>
<h4 data-id="heading-10">给库开发者带来复杂性</h4>
<p>如果 Vue 本身能够完全处理掉这种复杂性，那么在某种程度上也是可以接受的。然而，在与社区成员讨论后，我们意识到，共存的两个响应式系统实现也不可避免地影响到了库作者。</p>
<p>通过在 Vue 3 中支持 IE11，本质上库作者也需要做同样的决定。库作者不得不考虑他们的库运行在哪种 Vue 3 版本上(可能还得支持 Vue 2)。如果他们决定支持 IE11，在编写库时，脑子里也必须时刻考虑 ES5 响应式系统的相关警告。</p>
<h4 data-id="heading-11">为 IE11 持续存在做贡献</h4>
<p>没人愿意支持 IE11。它是一个停留在过去的行将就木的浏览器。未来 Web 生态向前发展的越远，我们为了支持 IE11 所要填补的缺口就越大。具有讽刺意味的是，如果 Vue 3 支持 IE11，那么就等于我们给它注入了新的生命力。基于我们的用户基础，移除对 IE11 的支持可能会加快其被淘汰的速度。</p>
<h3 data-id="heading-12">对于那些实在需要 IE11 支持的用户</h3>
<p>我们也很清楚，对 IE11 的真正需求来源于那些无法升级的用户：金融机构、教育部门和那些依赖 IE11 的屏幕阅读器。如果你正在构建一个面向这些领域的应用，你可能别无选择。</p>
<p>如果你需要 IE11 支持，我们推荐使用 Vue 2 版本。与其为 Vue3 和未来的版本承担巨大的技术债，我们认为把工作重心放在让 Vue2 拥有向后兼容特性、确保两个大版本之间的拥有更加近似的开发体验这件事更有意义。</p>
<p>一些可以在 2.7 版本向后兼容的特性：</p>
<ul>
<li>把 <a href="https://github.com/vuejs/composition-api" target="_blank" rel="nofollow noopener noreferrer"><code>@vue/composition-api</code> plugin</a> 合并进 Vue 2。这会让使用 Composition API 开发的库同时支持 Vue2 和 Vue3。</li>
<li>单文件组件中的 <a href="https://github.com/vuejs/rfcs/pull/227" target="_blank" rel="nofollow noopener noreferrer"><code><script setup></code></a> 语法。</li>
<li><code>emits</code> 选项。</li>
<li>提升的 TypeScript 类型支持。</li>
<li>正式在 Vite 中支持 Vue 2(目前的支持是通过<a href="https://github.com/underfin/vite-plugin-vue2" target="_blank" rel="nofollow noopener noreferrer">非官方插件</a>实现的)</li>
</ul>
<p>注意：以上列表暂定，可能并不全面，我们会在单独的 RFC 中讨论这些内容，并做出最终决定。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            