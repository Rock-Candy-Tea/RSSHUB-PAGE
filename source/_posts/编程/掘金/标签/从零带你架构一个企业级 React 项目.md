
---
title: '从零带你架构一个企业级 React 项目'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512ebe159614b24848aedbe1b489698~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 18:00:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512ebe159614b24848aedbe1b489698~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKieSun%2Ffucking-frontend" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KieSun/fucking-frontend" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3512ebe159614b24848aedbe1b489698~tplv-k3u1fbpfcp-zoom-1.image" width="350px" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p><strong>本文没有只针对 React 读者，除了强相关 React 技术栈的内容，其他东西完全是可以应用进任意技术栈的项目。</strong></p>
<p>一般在公司内部开发一个新项目，脚手架一把梭然后就开干了。由此一部分开发人员会缺失一些知识点，比如说为什么我们要选择这套技术栈进行开发；项目里的工程化配置到底应该怎么搞，一旦自己上手就懵逼；脚手架到底是个什么东西（相当一部分读者朋友认为脚手架是个很厉害的东西），如何整一个适合业务开发的企业级脚手架。</p>
<p>一个 React 项目会涉及到很多通用的东西，同时又存在很多选择性。单人开发可以按照自己的喜好来随意整合，但是在多人开发多项目的场景下，势必需要一整套规范来限制大家。文章将根据以下大纲和各位读者聊聊我们如何架构一个企业级 React 项目，以及最终如何将这套东西整合进脚手架。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331908ebd29146a5bb76e8b55209e828~tplv-k3u1fbpfcp-zoom-1.image" alt="大纲" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>接下来假定你目前处于一家主要使用 React 开发的公司。多人团队，且已有项目上线，随着业务的发展及人员的增加，你们急需建立一套完整统一且规范的开发流程，老板需要你全权负责这块内容并最终产出一个脚手架。</strong></p>
<h2 data-id="heading-0">技术栈选择</h2>
<p>对于一个 React 项目来说，通用的技术栈肯定需要考虑以下内容：</p>
<ul>
<li>TS 还是 JS？</li>
<li>选择 Hooks 还是非 Hooks 还是混合？</li>
<li>CSS 方案，是 Saas 这类预处理亦或者 CSS-In-JS、Atom CSS？</li>
<li>状态管理怎么选？</li>
<li>Route 怎么选？其实这个选择性很少</li>
</ul>
<p>首先在考虑某个技术优劣之前，我们先需要对团队情况进行分析。</p>
<p>比如说我们现在需要考虑是选择 TS 还是 JS，那么首先应该先考虑团队成员是否大部分已经了解或者开发过 TS 项目。如果大部分成员对 TS 是一个不熟练、有抵触心理的状态，那么强上 TS 势必会带来开发效率的降低，项目里 <code>any</code> 遍地飞。当然如果 Leader 能承受短期的效率降低，那么TS 的方案就可以摆在选项上，否则该选项可能就需要稍稍靠后，或者说只在部分项目里慢慢开始推广。</p>
<p>接下来我会以上述技术栈为例来说明在选型时我们需要从哪些角度去考虑问题。</p>
<h3 data-id="heading-1">选择 Hooks 还是非 Hooks 还是混合？</h3>
<p>下表中的上手成本针对于团队成员已经会用类组件写 React 项目的前提下。</p>









































<table><thead><tr><th align="center"></th><th align="center">Hooks</th><th align="center">非 Hooks</th><th align="center">混合</th></tr></thead><tbody><tr><td align="center">上手成本</td><td align="center">高</td><td align="center">无</td><td align="center">高</td></tr><tr><td align="center">功能复用性</td><td align="center">高</td><td align="center">低</td><td align="center">中</td></tr><tr><td align="center">代码可读性</td><td align="center">高</td><td align="center">低</td><td align="center">中</td></tr><tr><td align="center">各自常见缺陷</td><td align="center">闭包陷阱、对比类组件生命周期不全</td><td align="center">JS Class 缺陷</td><td align="center">都有</td></tr><tr><td align="center">老项目迁移成本</td><td align="center">高</td><td align="center">无</td><td align="center">中</td></tr></tbody></table>
<p>Hooks 的选择其实早几年就有文章开始聊了，所以我这里就不再班门弄斧来大聊特聊各自的优缺点了，上表也只是列了些常见的对比。</p>
<p>这个小节主要是给大家一个思路，在遇到选型的时候，我们该从哪几个方向去考虑。</p>
<h3 data-id="heading-2">CSS 方案</h3>









































<table><thead><tr><th align="center"></th><th align="center">CSS-In-JS</th><th align="center">Atom CSS</th><th align="center">预处理</th></tr></thead><tbody><tr><td align="center">上手成本</td><td align="center">高</td><td align="center">中</td><td align="center">几乎没有</td></tr><tr><td align="center">样式覆盖成本</td><td align="center">高，需要暴露给外部 class 或者单个节点的 style</td><td align="center">无</td><td align="center">无</td></tr><tr><td align="center">代码可读性</td><td align="center">高</td><td align="center">几乎没有</td><td align="center">高</td></tr><tr><td align="center">支持 postcss</td><td align="center">不支持，得用自己的</td><td align="center">支持</td><td align="center">支持</td></tr><tr><td align="center">SSR 支持度</td><td align="center">服务端那块需要额外写代码</td><td align="center">支持</td><td align="center">支持</td></tr></tbody></table>
<p>对于 CSS 方案的选择，笔者早在年初的时候就写过一篇<a href="https://juejin.cn/post/6927828841645735949" target="_blank" title="https://juejin.cn/post/6927828841645735949">文章</a>，大家有兴趣的话可以自行阅读，下面的话笔者来简单聊聊这些方案。</p>
<h4 data-id="heading-3">CSS-In-JS</h4>
<p>这个方案笔者已经用了两年了，具体用的是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstyled-components%2Fstyled-components" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/styled-components/styled-components" ref="nofollow noopener noreferrer">styled-components</a>这个库（下文简称 sc）。总的来说感觉这种方案对于 React 来说是很香的，并且解决了我很讨厌的传统写 CSS 的一些点，比如说得写一堆 class，真的是取名困难户。</p>
<p>通过这个库我们需要用 JS 来管理 CSS，因此就可以充分享受 JS 带来的工具链好处了。一旦项目中出现没有使用到的样式组件，那么 ESLint 就可以帮助我们找到那些死代码并清除，这个功能对于大型项目来说还是能减少一部分代码体积的。</p>
<p>除此之外，样式污染、取名问题、自动添加前缀这些问题也很好的解决了。除了以上这些，再来聊两点不容易注意到的。</p>
<p>首先是动态切换主题。因为我们是通过 JS 来写 CSS 了，那么我们就可以动态地控制样式。如果你的项目有切换主题这种类似的大量动态 CSS 的需求，那么这个方案会是一个不错的选择。</p>
<p>还有个点是按需加载。因为我们是通过 JS 写的 CSS，现阶段打包基本都走的 code split，那么就可以实现 CSS 文件的按需加载，而不是传统方式的一次性全部加载进来（当然也是可以优化的，只是没那么方便）。</p>
<p>说完了优先再来聊聊缺点，学习成本肯定存在，这个没啥好说的。另外也有运行时成本，sc 本身就有文件体积，加上还需要动态生成 CSS，那么这其中必定有性能上的损耗。项目越大影响的也会越大，如果你的项目对于性能有很高的要求，那么需要谨慎考虑使用。另外因为 CSS 动态生成，所以不能像传统 CSS 一样缓存 CSS 文件了。除此之外，样式覆盖成本相较其它方案也略高，同时也不支持 postcss，针对 SSR 方案也有额外的开发成本。</p>
<h4 data-id="heading-4">Atom CSS</h4>
<p>代码可读性差，学习成本不低，但是在存在成熟的 UI 规范下，该方案能提供通用样式来进行复用，从而降低 CSS 文件体积。</p>
<p>其实笔者并不看好这个方案在国内业务团队中的大范围应用，因为需求的频繁变更导致的 UI 变更以及绝大部分 UI 团队没有一个成熟的规范，这些问题会显著提高使用 Atom CSS 的成本。</p>
<h4 data-id="heading-5">预处理方案</h4>
<p>应该算是传统方案了，该有的都有，开发成本也低，无非存在 CSS 的通病：调试起来是真的蛋疼。</p>
<h4 data-id="heading-6">小结</h4>
<p>总的来说用 CSS-In-JS 需要考虑学习成本及团队成员的接受程度，毕竟确实存在一部分开发人员是不喜欢这种方式来书写 CSS 的。</p>
<p>Atom CSS 的话一定务必需要有一套成熟的 UI 规范，否则随着需求的变化频繁乱改 UI，相信我，一定会火葬场的。</p>
<p>预处理方案没啥好说的，几乎没有上手成本，代码也方便维护。如果团队成员不喜欢 CSS-In-JS 并且也没有一套成熟的 UI 规范，就选这个呗。</p>
<h3 data-id="heading-7">状态管理怎么选？</h3>
<p>状态管理真的有太多选择了，除了大家耳熟能详的 Redux 和 mobx，其它还有一大堆竞品，比如说：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fstatelyai%2Fxstate" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/statelyai/xstate" ref="nofollow noopener noreferrer">xstate</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebookexperimental%2FRecoil" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebookexperimental/Recoil" ref="nofollow noopener noreferrer">Recoil</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmndrs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pmndrs" ref="nofollow noopener noreferrer">pmndrs</a>家出品的 zustand、valtio、jotai</li>
<li>另外还有好多小众产品</li>
</ul>
<p>我们在对状态管理进行选型的时候，其实第一步应该考虑项目是否需要状态管理，实际上大部分项目需要的只是跨组件的通信，而不是管理。或者说实际上当你在考虑项目是否需要状态管理的时候，基本上此时就是不需要的。因为你可能压根还没遇到状态管理解决的痛点，而只是觉得跨组件通信麻烦。</p>
<p>如果你的项目还没上升到需要状态管理的时候，可以考虑选择状态共享库（类似<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fhox" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/hox" ref="nofollow noopener noreferrer">hox</a>）外加 hooks 一把梭，实际上这个方案基本可以覆盖大部分项目了，写出来的状态相关的代码也不容易屎山。</p>
<p><strong>如果项目真的需要状态管理，那么尽量别去考虑技术相关的东西，而是选择一个大家熟悉的东西直接用</strong>。因为状态管理太容易写出屎山了，我们巴拉巴拉对比了一堆技术相关的东西，最终如果选择了一个相对先进但大家不熟悉的产品，那么最后屎山应该是避免不了的。</p>
<h3 data-id="heading-8">Route 怎么选？</h3>
<p>路由这块其实个人认为没啥好选的，毕竟可选择的余地基本没有，选哪个都对开发没什么影响，所以爱选啥选啥吧。</p>
<h3 data-id="heading-9">其他</h3>
<p>除了上面所说的技术选型，我们可能还会根据项目的不同存在更多的技术需求，比如说单测等等。</p>
<h4 data-id="heading-10">单测</h4>
<p>业务团队写单测的不多，尤其是 UI 相关的。但是我们可以退而求其次，对工具函数或者一些关键节点做下单测，提高一下整体的代码质量。</p>
<p>工具函数测试的话，直接上 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fjest" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/jest" ref="nofollow noopener noreferrer">Jest</a> 或者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmochajs%2Fmocha" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mochajs/mocha" ref="nofollow noopener noreferrer">Mocha</a> 就行，反正也就是断言的事情。如果要测试 UI 相关的，那么 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fenzymejs%2Fenzyme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/enzymejs/enzyme" ref="nofollow noopener noreferrer">enzyme</a> 以及 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftesting-library%2Freact-testing-library" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/testing-library/react-testing-library" ref="nofollow noopener noreferrer">react-testing-library</a> 也是必不可少的。最后如果你们还想整一整自动化测试，那么就上 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cypress.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cypress.io/" ref="nofollow noopener noreferrer">cypress</a> 吧。</p>
<p>另外笔者之前也写过一篇<a href="https://juejin.cn/post/6844904018129453070" target="_blank" title="https://juejin.cn/post/6844904018129453070">单测的文章</a>，有兴趣的读者可以自己阅读下。</p>
<h3 data-id="heading-11">小结</h3>
<p>实际上在进行技术选型的时候，技术相关的内容很可能是最后才会考虑的，在这之前我们需要结合团队、项目工期、项目诉求等外部因素来权衡。</p>
<p>最后关于各个技术栈的选择大家可以浏览云谦大佬搞的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsorrycc%2Fawesome-javascript" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sorrycc/awesome-javascript" ref="nofollow noopener noreferrer">仓库</a>，应该算是覆盖的很全面了。</p>
<h2 data-id="heading-12">工程化配置</h2>
<p>项目中的工程化配置是相当重要的一环，这部分内容对于开发人员来说应该尽可能少的配置，在常见场景下要实现开箱即用，并且对于<strong>一部分配置强管控</strong>。</p>
<p>笔者和一些处在小公司的前端开发聊过，了解到他们的开发其实相当混乱。比如说：</p>
<ul>
<li>工程配置每个项目都不同，具体体现在 Webpack 配置混乱、ESLint 形同虚设、代码格式混乱等问题上</li>
<li>commit 提交没有规范，代码没人 review</li>
<li>等等。。。</li>
</ul>
<p>以上这类问题如果恰巧发生于正在阅读文章的你的团队，你也许可以按照笔者下文中的思路去尝试改进。</p>
<p>对于一个项目来说，以下内容应该是必须的：</p>
<ol>
<li>构建器配置，在应用中一般都是 Webpack</li>
<li>Babel 配置</li>
<li>TS 配置</li>
<li>ESLint 配置</li>
<li>Prettier 配置</li>
</ol>
<p>针对以上内容来说，个人认为除了第二和三点，其他几项都是需要强管控的。</p>
<p>对于 Webpack 而言，大家都知道配置起来挺麻烦的，但是其中相当一部分配置在各个应用中应该是通用的。我们是可以抽离出这部分通用的配置并做成一个内部的 preset 的，就像<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Fbabel-preset-env" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/babel-preset-env" ref="nofollow noopener noreferrer">@babel/preset-env</a>一样。这种做法简化了需要配置的内容，从而杜绝用户瞎搞造成各个项目 Webpack 混乱的局面。同时以后在升级 Webpack 的时候，也无需用户关注通用配置的修改，只需要对自己新增的配置做适配即可。</p>
<p>那么对于 ESLint 和 Prettier 来说，强管控是必须的，把配置封装起来直接让用户 <code>require</code> 就行。这样就能杜绝换个项目 ESLint 被关闭了、编码格式全变了的情况，这种问题其实对代码质量是有毁灭性打击的，大家都会破罐子破摔写代码。</p>
<p>总的来说，对于工程化配置我们最好尽可能少的让用户去接触配置，专心业务代码即可。能强管控的地方务必强管控起来，对于整个团队的代码质量都是有提升的。当然我们肯定不能把所有配置都强管控起来，有的地方还是需要开个口子让用户能自定义 / 合并配置项的，比如 Webpack。</p>
<h2 data-id="heading-13">目录结构</h2>
<p>一个好的项目目录是能提高项目的维护性的，否则代码没有条理的乱放，自己可能写爽了，但是对于接手的同事来说真的是会头大的。</p>
<p>笔者大致会把一个项目目录分为以下几块：</p>
<ul>
<li>pages，页面，其中每个文件夹按照功能模块划分</li>
<li>components，组件，分为 common 及业务组件</li>
<li>services，和后端打交道的地方</li>
<li>store，状态管理逻辑相关，如果需要的话</li>
<li>utils，常量、工具函数等</li>
<li>types，TS 项目需要，存放类型</li>
<li>assets，静态资源，比如说图片、svg 这类</li>
<li>tests，测试相关，如果需要的话</li>
</ul>
<p>根据以上分类，我们一个项目大致目录会长成这样：</p>
<pre><code class="copyable">└── /src
    ├── /pages
    ├── /components
    ├── /services
    ├── /store
    ├── /utils
    ├── /types
    ├── /assets
    ├── /tests
    ├── index.ts
    └── App.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了以上内容，根据我们不同的 CSS 选型以及工程化的选择，对应的文件也会有所不同。</p>
<h2 data-id="heading-14">整合进脚手架</h2>
<p>脚手架简单来说就是帮我们 <code>git clone</code> 了一个初始化项目过来，一个最基础的脚手架大概可以分为两块内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc065a6e4d0c42dc803adaebdd0d853f~tplv-k3u1fbpfcp-zoom-1.image" alt="基础脚手架" loading="lazy" referrerpolicy="no-referrer"></p>
<p>工程化配置和模板代码上文已经聊过一些了，大家可以根据自己业务的不同来整出这样一套东西，但是仅有这些还不足以做出一个好用的脚手架。</p>
<p>举个例子，有些业务需要做单测怎么办？又需要业务方自己去做一大堆配置么？</p>
<p>比如说根据业务的不同，模板可能也会存在细微的不同，这时候我们是重新再搞一套模板还是怎么办？</p>
<p>因此对于脚手架来说，我们需要在必备的工程化配置之上，再加上一些可选的内容。比如说业务方认为项目需要单测，那么在初始化项目的时候选上单测就可以自动加入单测所需的配置。</p>
<p>再然后因为业务的不同，模板代码上可能存在不同，这时候我们可以依照情况来决定是再拆分一套模板还是在原有的模板上支持编译，从而根据用户的输入来决定最终的模板输出。</p>
<p>做好以上这些东西我们可能才勉强做出一个好用点的且适合自身团队业务的脚手架。</p>
<h2 data-id="heading-15">最后</h2>
<p>文章没有代码，主要还是分享了从笔者的角度去考虑如何从零设计一个 React 项目，其中的技术栈选型大概是怎么样的、工程化这块该怎么搞的好用点、项目目录结构大概长什么样子，以及最后聊了聊如何做一个好用的脚手架。</p>
<blockquote>
<p>作者：yck</p>
<p>仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKieSun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KieSun" ref="nofollow noopener noreferrer">Github</a></p>
<p>公众号：<a href="https://user-gold-cdn.xitu.io/2019/12/22/16f2e3314a431c20?w=900&h=500&f=jpeg&s=148695" target="_blank" title="https://user-gold-cdn.xitu.io/2019/12/22/16f2e3314a431c20?w=900&h=500&f=jpeg&s=148695">前端真好玩</a></p>
<p>特别声明：原创不易，未经授权不得转载或抄袭，如需转载可联系笔者授权</p>
</blockquote></div>  
</div>
            