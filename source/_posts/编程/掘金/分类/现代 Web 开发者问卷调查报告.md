
---
title: '现代 Web 开发者问卷调查报告'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d63730dc62b49d283ae46e0fd230b93~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 19:13:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d63730dc62b49d283ae46e0fd230b93~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前些日子在 GMTC 北京 2021 技术大会上分享的《字节跳动的现代 Web 开发实践》，介绍了「现代 Web 开发」这场「范式转移」，在字节跳动如何转化成具体的技术栈和研发体系，在内部广泛落地和从中获益。分享中也预告了开源项目 Modern.js 发布了「现代 Web 开发者问卷调查」。截至 8 月 20 日，已经收到了 「612」 份有效回复，在汇总和交叉对比之后，可以看到很多跟「现代 Web 开发」有关的结果。</p>
<h2 data-id="heading-0">编程语言</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d63730dc62b49d283ae46e0fd230b93~tplv-k3u1fbpfcp-watermark.image" alt="问题1.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ES6+ 和 TypeScript 已经成为绝对的主流，分别有 88.4% 和 77.63% 的开发者勾选了这两项。</p>
<p>仍然有接近一半的开发者勾选了 ES5，由于问题设计的缺陷，从数据无法挖掘到很直观的原因，但能看到一些可能相关的数据：</p>
<ol>
<li>没勾选 ES5 的开发者，在「UI 技术」问题中勾选 Vue 的比例降低了（从 65.2% 降到 58.23%）</li>
<li>没勾选 ES5 的开发者，在「UI 技术」问题中勾选 Vanilla JS 的比例降低了（从 11.11% 降到 7.62%）</li>
</ol>
<p>在非 JS 语言中，Python、Go、Rust 的占比最高，分别为 12.75%、11.11%、7.35%。问题中没包含的 Java 在「其它语言」（6.54%）中出现的最多（50%）。选择 Ruby 的开发者很少，只有 1.31%。</p>
<p>勾选了这些非 JS 语言的开发者，在其他问题中勾选纯前端 CSS 技术（Less、PostCSS、styled-components）、React、SSR 的比例没有明显下降（分别是：从 82% 降到 76%，从 80% 降到 78%，从 50% 降到 49%），可见这次问卷调查的参与者多数都是前端开发者。</p>
<p>勾选了 Python、Go、Rust 的开发者，在「服务端技术」问题中勾选「其它语言」的比例，分别只有 16.67%、17.65%、6.67%，猜测开发者使用这些语言更多是用于机器学习、工具开发、WebAssembly 等场景。</p>
<p>选择 Dart 的开发者只有 5%，可见 Flutter 在前端开发场景中使用不多。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e8eedc500954a5b84f770f5ae3cabee~tplv-k3u1fbpfcp-watermark.image" alt="数据1.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">CSS 技术</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52944df40afe419cb7bcbe0313ab6007~tplv-k3u1fbpfcp-watermark.image" alt="问题2.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要先说明的是，由于最初的问卷不小心遗漏了「Utility Class / Atomic CSS」和 Tailwind CSS 这两项，直到 7 月才补上，所以这方面的结果没什么参考价值（有意思的是，在最初就有的「其它开源技术」选项里，基于 Tailwind CSS 的 WindiCSS 的出现比例排第二，达到了 22%）。</p>
<p>分别有 59.8% 和 55.72% 的开发者选择了 Less 和 Scss，在所有 CSS 技术中占比最高，可见这种技术在国内仍然很主流（虽然与全球社区不同，Less 在国内的使用是略超过 Scss 的）。</p>
<p>CSS Modules 的使用接近 Less 和 Scss，占比达到了 51.14%，体现了「CSS 模块化」的需求。</p>
<p>PostCSS 的占比仅次于上面三个传统主流技术，达到 38.24%，但在勾选了这项的开发者中，选 Scss 和 Less 的比例反而更高了（从 83.17% 提高到 88.46%），这种结果可能说明在国内用基于 PostCSS 的 CSS 开发完全取代 Scss 和 Less 还不普及，也可能体现了基于 Less 的 Ant Design 等开源项目在国内太流行。</p>
<p>接下来占比最高的是 styled-components，达到 34.31%，远远高于「其他 CSS In JS 技术」中的 styled-jsx、JSS 等（而这个选项里有 30% 填写的都是 Emotion，也算 styled-components 的一种）。</p>
<p>奇怪的是，勾选了 styled-components 的开发者，选 CSS Modules 的比例反而提高了（从 51.14% 提高到 64.76%），貌似没有体现出在「CSS 模块化」方面 styled-components 继承和取代 CSS Modules 的关系。反过来看，在勾选 CSS Modules 的开发者中，勾选 styled-components 的比例也从 34.31% 提高到 43.45%（在勾选 Less 的开发者中，就没有这种提高）。所以同时勾选这两项的，有可能是更充分认识到「CSS 模块化」需求的开发者，在旧项目中用 CSS Modules，现在逐步开始使用 styled-components。</p>
<p>选择 styled-components 的开发者中，选择 React 作为 UI 技术的占 89.52%，选择 Vue 作为 UI 技术的占 65.71%。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4e18327bf9c4ffdb5439c54871f7e5b~tplv-k3u1fbpfcp-watermark.image" alt="数据2.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">UI 技术</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee48af72d2044997a0dfa38bf680c7b8~tplv-k3u1fbpfcp-watermark.image" alt="问题3.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>React 和 Vue 都非常主流，大幅超过其他方案，分别有 80.07% 和 65.2% 的开发者勾选了这两项。</p>
<p>需要注意的是，在「语言」问题里勾选了 TypeScript 的开发者，勾选 React 的比例提高到 87.63%，而选 Vue 的比例反而略下降（63.54%）。如果在「工程技术」问题里勾选了 Next.js / Umi / CRA，勾选 React 的比例更是提高到接近 100%（选 Vue 的比例是 60.91%），这一定程度上体现了 Dan Abramov 的访谈里说的「如果你不会编程，React 的学习曲线确实会比较陡峭」（比如不熟悉编译、缺乏框架支持等）。</p>
<p>选择 Preact 和 Svelte 的比例很小，分别只有 4.08% 和 5.07%。</p>
<p>在勾选了 ES5 的开发者中，选 Vanilla JS（相当于 jQuery 吧）的比例从 11.11% 提高到 15.14%（反过来，勾选了 Vanilla JS 的开发者，选 ES5 的比例同样从 46.41% 提高到 63.24%）。</p>
<p>在跨端技术里，Electron 的使用最多（17.48%）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3ee3182aea4251b49af258b09eab27~tplv-k3u1fbpfcp-watermark.image" alt="数据3.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">数据逻辑</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a35a3cfa4d1f48f68fc32734050dba9a~tplv-k3u1fbpfcp-watermark.image" alt="问题4.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Redux 仍然是主流方案，占比最高，达到 55.56%。</p>
<p>进一步分析，选择了 Redux 的开发者，几乎全部（96.76%）都勾选了 React，勾选 Vue 的有 61.18%。选择了 Mobx 的开发者，也几乎全部（93.89%）都勾选了 React，勾选了 Vue 的有 61.83%。</p>
<p>在勾选了 Vue 的开发者中，占比最高的解决方案变成了 Vuex，达到 77.69%， 选择 Mobx 的比例也从 21.41% 提高到 52.13%，而选择 Redux 的比例降到 20.3%。</p>
<p>同时选择 Mobx 和 Redux 的开发者很少，只有 14.38%。</p>
<p>从以上数据可以看到一些「不可变数据」和「可变数据」方案的差别。</p>
<p>选择 Hooks + Context 的人仅次于 Redux 和 Vuex，达到 51.96%。需要注意的是，选择了 Redux 的开发者，59.41% 也同时选择 Hooks + Context，反之，选择 Hooks + Context 的开发者中，63.52% 也选择了 Redux。占比都略有提升，一定程度上体现 Redux 代表的「全局应用状态」方案和 Hooks + Context 代表的「局部状态」方案是互补、不矛盾的。</p>
<p>从数据可以看到，很多开发者不再直接使用 Redux 自身的「底层 API」，而是通过 RTK、Dva 这样的「上层 API」来间接使用，占比分别为 2.61% 和 20.75%，RTK 在国内还不普及。选择 Dva 的开发者，有 67.72% 也选择了 Umi。</p>
<p>Recoil 和 React Query 都能增加「局部状态」方案的适用范围。选择了 React Query 的开发者，选择 Redux 的比例下降到 48.65%，选择 Hooks + Context 的比例提高到 67.57%，而选择 Recoil 的开发者，选择 Redux 的比例没下降（63.64%），选择 Hooks + Context 的比例也提高到 78.79%。</p>
<p>选择 RxJS 的开发者仅次于 Dva，达到 13.73%。在选择 RxJS 的开发者中，同时选择 Dva 的比例从 20.75% 降低到 16.67%，同时选择 Redux 的比例提升到 65.48%。</p>
<p>选择 GraphQL 和 Apollo 的开发者加起来跟 RxJS 一样达到了 13.73%。</p>
<p>选择状态机方案（XState）的开发者只有 1.8%，还不普及。</p>
<p>其它开源方案和自研方案很少，只占 2.29% 和 0.65%。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efadb41c1e814e9194ec8b2c11446a67~tplv-k3u1fbpfcp-watermark.image" alt="数据4.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">服务端开发</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b51288f4710450d9a8363f84c50d684~tplv-k3u1fbpfcp-watermark.image" alt="问题5.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9afa2b07a4d1410daa897f2febddf189~tplv-k3u1fbpfcp-watermark.image" alt="问题6.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从数据中可以看到，前端开发者的服务器端开发需求，是以 BFF 为主的，因为不属于 BFF 的 RPC 开发（微服务）占比只有 17.16%，而 BFF（REST、WS 或 GraphQL）的占比达到 73.53%。其中 REST API 最主流，达到 66.18%，WebSocket 也达到了 30.56%，GraphQL 还缺乏普及，只有 14.38%。</p>
<p>SSR 的比例超过了静态 HTML 和动态 HTML。在选择了静态 HTML 或动态 HTML 的开发者中，选择 SSR 的比例都一样提高到 59%。</p>
<p>在选择了 SSR 的开发者，选择 REST API 的下降到 61.69%（可能是因为很多原本要写 API 的需求可以直接在 app 里实现了），在「工程技术」问题中选择 SSR 框架（NextJS / NuxtJS、Umi）的比例从 34.8% 提高到 43.51%。反过来，选择了 SSR 框架的开发者，选择 SSR 的比例也从 50.33% 提高到了 62.91%。</p>
<p>在「服务器端技术」问题中选择了非 JS 语言的开发者，选择 SSR 的比例大幅下降到 25%。</p>
<p>在「服务器端技术」问题中，Koa 和 Express 最主流，分别占比 54.74% 和 49.51%。其中选择了 Koa 的开发者，有 36.42% 也选择了 EggJS。</p>
<p>选择云函数的开发者达到了 20.42%，超过其他开发语言、开源项目和自研方案。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/420f1c75eb704b35ad323331d76abfb7~tplv-k3u1fbpfcp-watermark.image" alt="数据5.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47b53fbffeb64350a574d9d55eac6c78~tplv-k3u1fbpfcp-watermark.image" alt="数据6.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">工程技术</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d68d9b5f6f5412e90e5c71f9f16405d~tplv-k3u1fbpfcp-watermark.image" alt="问题7.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Webpack 仍然是绝对主流，占比高达 94.28%。需要注意的是，选择了 Rollup 的开发者几乎全部（99.56%）也都勾选了 Webpack。</p>
<p>Vite 和 ESBuild 得到了一定的应用，分别达到了 35.62% 和 22.71%。</p>
<p>Parcel 和其它开源构建工具、自研构建工具的占比都很小，分别只有 7.03%、1.63% 和 0.49%。</p>
<p>选择了 Umi 和 Next.js 的开发者分别有 25.33% 和 16.5%，CRA 则只有 10.62%。选择了这种框架级工程方案的开发者，在「服务器端开发需求」问题中选择 REST API 的比例从 66.18% 提高到 76.53%（对于 Next.js 开发者，进一步提高到 82.18%），选择 SSR 的比例从 50.33% 提高到 62.91%（对于 Next.js 开发者，进一步提高到 76.24%）。</p>
<p>微前端和 Monorepo 这种新的研发模式也都有一定的普及，分别达到 25.16% 和 19.93%。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97e87c45d4f0499d8734f2152b757831~tplv-k3u1fbpfcp-watermark.image" alt="数据7.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">研发环境</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fbc5e4d44bb4b5e9bdb7a8f10d956e2~tplv-k3u1fbpfcp-watermark.image" alt="问题8.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>VSCode 是绝对主流，占比达到 91.67%，WebStorm 只有 21.9%。</p>
<p>在「语言」问题中没有选择 ES6+ 或 TypeScript 的开发者，选择 VSCode 的比例降低到 84% 左右。</p>
<p>Prettier 的接受程度很不错，占比达到 42.97%，甚至超过了 ESlint（39.71%），选择了两者之一的开发者，选择另一个的比例也会大幅提升（78%、84%）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a10be9add174497cb37e834a2004f35e~tplv-k3u1fbpfcp-watermark.image" alt="数据8.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是这次现代 Web 开发者问卷调查的报告，数据结果都很符合 Modern.js 项目的预期、设计和实践，期待即将发布的 Modern.js 项目，也能如预期般全面支持这次问卷中反映的技术需求、趋势和问题。</p></div>  
</div>
            