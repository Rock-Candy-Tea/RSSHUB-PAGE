
---
title: 'slate-angular 正式开源'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a8e51034c60434289af3d96e0f0a2a6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 03:20:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a8e51034c60434289af3d96e0f0a2a6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一句话介绍</h2>
<p>﻿<a href="https://github.com/worktile/slate-angular" target="_blank" rel="nofollow noopener noreferrer">slate-angular</a> 是一个基于 Angular 和 Slate.js 的编辑器视图层，帮助开发者使用 Angular + Slate.js 构建Web富文本编辑器。</p>
<h2 data-id="heading-1">Slate.js 介绍</h2>
<p>Slate.js 是一个特别优秀的富文本编辑器框架，代码整洁、架构良好、扩展性强，目前市面上基于 Slate.js 开发的富文本编辑器及产品已经数不胜数。而且 Slate.js 足够有魔力，从开始接触富文本编辑器开发到现在两年左右的时间，感觉 Slate.js 一直是我成长的良师，从最初的入门调研，到开发出第一个版本编辑器，然后是视图层架构的升级，再到后面的性能及稳定性的优化，每一个阶段都能从 Slate.js 身上学到很多东西，当然对它的了解也越来越深。我觉得 Slate.js 就是一个自身在不断地迭代和改进的编辑器框架，专注于视图层和模型层，架构实现一直紧跟社区主流技术的发展，内容编辑的实现机制也在不断地向现行标准事件靠拢，已经开源5年左右的时间，目前社区仍然非常活跃，还在不断地扩展更多的适用场景，是非常厉害的一个存在。</p>
<h2 data-id="heading-2">自研Angular视图层</h2>
<p>我们的前端技术栈是 Angular，开源社区中基于 Angular 开发的富文本编辑器极其稀缺，而我们要做的 PingCode Wiki 产品又对富文本编辑器的易用性和可扩展性要求极高，调研发现Slate编辑器框架非常符合我们的需求，核心模型层不依赖任何前端框架，可扩展性极其高，有完整的测试覆盖，所以我们尝试自研基于 Angular 的视图层，可以理解为自研视图层的核心驱动来源于产品。</p>
<p>个人觉得开发基于 Angular 的视图层是一个很有意义的过程，并且当前开源社区中还没有使用 Angular 开发 Slate 编辑器的实现，所以我们想把我们的这种实践成果开源出去，以回馈 Slate 和 Angular 社区，让更多的开发者可以基于 Angular + Slate 开发富文本编辑器。</p>
<h2 data-id="heading-3">开源之路</h2>
<p>当前 slate-angular 已经支持企业级知识库产品 PingCode Wiki 稳定运行超过1年，最初版本是基于 <a href="mailto:Slate@0.47.0">Slate@0.47.0</a>版本（JavaScript版本Slate），第二版是基于最新Slate的实现（TypeScript），当前已经是第三版，从年初就开始准备，包括公开Github仓储、统一底层的实现及API风格、搭建在线Demo、补充单元测试、同步升级最新 Slate 等。</p>
<p>Demo 功能：﻿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a8e51034c60434289af3d96e0f0a2a6~tplv-k3u1fbpfcp-zoom-1.image" alt="slate-angular-demo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>github：<a href="https://github.com/worktile/slate-angular" target="_blank" rel="nofollow noopener noreferrer">github.com/worktile/sl…</a>﻿</p>
<p>demo ：<a href="http://slate-angular.ngnice.com/" target="_blank" rel="nofollow noopener noreferrer">slate-angular.ngnice.com/</a>﻿</p>
<blockquote>
<p>slate-angular 可能不是一个开箱即用的富文本编辑器，它属于Slate框架的一个视图层，对接Slate框架底层与用户交互界面的一个中间层，它仅提供基础的富文本编辑能力和功能扩展的插槽，但这也是slate-angualr的优势，它只专注底层的实现：兼容浏览器、移动端、代理输入事件、代理光标、支持自定义Element/Text/Leaf节点的渲染、处理基础交互等，基于它可以很快开发出像 Quill、Prosemirror 这类有一定基础功能的富文本编辑器，并且它的可扩展上限很高，经过一定的时间完全可以构建出像 Confluence、Notion、PingCode Wiki 这种功能级别的富文本编辑器。</p>
</blockquote>
<h2 data-id="heading-4">特性支持</h2>
<ul>
<li><strong>集成块级元素前后光标方案</strong></li>
</ul>
<p>支持扩展指定元素渲染前后光标，方便在块级元素前后插入段落（表格Demo中已经实现块级光标的基本交互）</p>
<ul>
<li><strong>自定义组件/模版渲染块级元素</strong></li>
</ul>
<p>支持多层级元素内容的自定义渲染，可方便实现像表格这类复杂场景的需求，同时维持了自定义组件之间的正确的依赖注入链，也就是单元格组件可以通过依赖注入获取父级表格组件的服务</p>
<ul>
<li><strong>自定义渲染 Text</strong></li>
</ul>
<p>支持自定义Text节点的内容渲染，这个在 slate-react 中是不提供的，slate-angular 中单独提出来了，主要用于实现加粗、斜体、下划线、颜色、背景色等需求</p>
<ul>
<li><strong>自定义渲染 Leaf</strong></li>
</ul>
<p>支持自定义Leaf 节点的渲染，Leaf是对Text的拆分，每一个Text节点默认对应一个Leaf，而Text节点拆分Leaf的依据是Decoration装饰器，主要用于实现对文本的动态修饰，配合自定义Leaf组件实现搜索高亮、划词评论等需求</p>
<ul>
<li><strong>Decoration 装饰器</strong></li>
</ul>
<p>提供对文本内容的动态修饰，是由外部数据驱动定位、装饰文本内容。它的特点是在不改变原始数据的情况下实现对文本的装饰，是处理动态需求的一种方式</p>
<ul>
<li><strong>Void元素</strong></li>
</ul>
<p>Void意为不可编辑，所有内容属于一个整体，slate-angular 支持扩展Void元素，通过Void元素可以把任意复杂的Angular组件的嵌入到编辑器中，比如图片、代码编辑器、甘特图等都可以嵌入到编辑器内容区域中。</p>
<p>﻿</p>
<h2 data-id="heading-5">兼容浏览器</h2>
<p>Chrome、Edge、Safari、Firefox、QQ Browser</p>
<p>﻿</p>
<h2 data-id="heading-6">已解决常见Slate.js兼容问题</h2>
<ol>
<li>
<p>中文输入重复问题</p>
</li>
<li>
<p>中文输入崩溃</p>
</li>
<li>
<p>Safari浏览器输入中文焦点跳动</p>
</li>
<li>
<p>\n 导致内容混乱</p>
</li>
<li>
<p>a标签 导致内容混乱</p>
</li>
<li>
<p>表格结构约束问题</p>
</li>
<li>
<p>angular comment问题</p>
</li>
<li>
<p>...</p>
</li>
</ol>
<p>这些问题当前已经在 slate-angular 中得到解决，在此不做更多的说明，如有任何疑问欢迎给 <a href="https://github.com/worktile/slate-angular" target="_blank" rel="nofollow noopener noreferrer">slate-angular</a> 提 Issues。</p>
<p>﻿</p>
<h2 data-id="heading-7">技术路线</h2>
<p>接下来聊点技术相关的内容，个人其实一直想对 Slate.js 的架构设计以及内部机制进行一些剖析，所以借助这次开源跟大家简单聊聊 slate.js 和 slate-angular 的技术路线以及比较重要的一些底层机制。</p>
<h3 data-id="heading-8">先从 Slate 架构说起：</h3>
<p>Slate 框架核心主要包含模型层和视图层，模型层定义描述富文本内容的基本数据结构（一个支持嵌套的节点树）和对该数据的基础操作，视图层对接前端框架，处理基础输入行为、选区代理，内容渲染、插件扩展等等。</p>
<p>值得一提的是Slate的数据模型定义都是都是参照DOM标准实现的，对新手还算友好，比如数据模型的概念Block、Inline-block、Text等都跟DOM中的意义一致，选区也一样有Selection、Anchor、Focus、Collapsed等概念。</p>
<p>Slate 富文本编辑器架构概貌：</p>
<p>﻿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d55f3add6dfa4282893e9d95188cabc8~tplv-k3u1fbpfcp-zoom-1.image" alt="三层架构.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">基于Angular开发富文本编辑器</h3>
<p>slate-angular 作为一个独立的视图层，是Slate底层与上层功能实现之间的桥梁，核心作用就是发挥框架的优势，更好的组织编辑器功能的开发。</p>
<p>基于 slate-angular 开发富文本编辑器可以说是原汁原味的Angular味道，无论是基础功能修改、还是扩展新功能，你都可以使用Angular组件或者服务组织代码的实现，而不再是使用组件对JavaScript库进行简单的封装：</p>
<p>你可以使用 Angular 组件或者模板自定义插件的渲染。</p>
<p>你可以基于 Angular 组件封装复杂的交互行为。</p>
<p>你可以复用 Angular 组件库。</p>
<p>你也可以使用服务在父子级节点组件之间共享数据，它们维持了正确的依赖注入链。</p>
<p>总之 Angular 的一切特性你都可以使用。</p>
<h3 data-id="heading-10">内容编辑基础原理</h3>
<p>当前技术框架下想实现对输入内容的控制大概有两种实现思路，一种是事件代理，另外一种是监控内容变化，Slate主要采用的是事件代理，就是通过监控一系列内容输入的DOM事件，然后通过事件类型及其它上下文判断该输入对应的数据操作，最后把它转化为针对数据模型的一系列操作。</p>
<blockquote>
<p>监控内容变化的方式在Slate中也有用到，是为了支持Android浏览器，大概是因为Android浏览器下某些场景的输入事件无法被正确捕获，进而无法响应用户的操作，所以使用MutationObserver监控内容变化以正确响应用户的输入行为。</p>
</blockquote>
<p>﻿</p>
<p>因为视图层中事件代理的实现主要是与输入事件打交道，各个浏览器对于输入事件的实现不完全统一，加上又要区分普通英文输入和中文组合输入，所以需要针对不同浏览器做很多兼容性处理，可以说打的是一套<strong>组合拳</strong>，招式概览：</p>
<ol>
<li>
<p>理想情况下：使用beforeinput事件完成基础输入代理，因为 beforeinput 语义化清晰，可以作为输入行为判断标准。</p>
</li>
<li>
<p>非理想情况：浏览器不支持 beforeinput 事件，使用React的合成事件onBeforeInput处理英文输入(Angular中需要自己实现)，对于其它输入交互如回车、删除使用keydown事件处理。</p>
</li>
<li>
<p>IME输入处理使用事件compositionstart和compositionend处理，这三个事件非常可靠，没有任何浏览器兼容性问题。</p>
</li>
<li>
<p>除此之外撤销/重做、焦点移动等是在keydown事件中处理，复制、剪切等逻辑使用原生 copy、cut事件即可，而粘贴、拖拽等逻辑和基础输入一样依赖beforeinput事件，如果浏览器不支持 beforeinput事件则在paste、drop等事件中处理。</p>
</li>
</ol>
<p>事件代理过程概貌：</p>
<p>﻿</p>
<p>﻿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7e829250a684b7c8b4b6522c00070f6~tplv-k3u1fbpfcp-zoom-1.image" alt="slate-angular-event-proxy.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">选区同步机制</h3>
<p>和浏览器的选区一样，Slate的数据模型也需要选区，当数据变更发生时标识数据修改的位置，并且这个位置需要跟浏览器原生的选区保持一致，无论是浏览器的选区变化了，还是Slate的选区变化了都需要实现互相同步。</p>
<p>下面介绍下 slate-angular 视图层中选区的双向同步机制：</p>
<p>一、DOM Selection -> Slate Selection：</p>
<p>监控原生Document对象的 selectionchange 事件，当DOM Selection改变时查询对应的Slate Selection，修改Slate Selection与DOM Selection一致。</p>
<p>交互行为 -> DOM Selection 改变 -> selectionchange -> sync Slate Selection</p>
<p>交互行为包括鼠标Click、按方向键等</p>
<p>﻿</p>
<p>二、Slate Selection -> DOM Selection：</p>
<p>Slate数据Change导致Slate Selection发生变化，需要在Change事件中做处理，根据最新的Slate Selection查询对应的DOM Selection，修改DOM Selection与Slate Selection一致。</p>
<p>交互行为 -> 触发数据更新 -> 新的Slate Selection -> 视图刷新 -> sync DOM Selection</p>
<h3 data-id="heading-12">插件扩展</h3>
<p>Slate 使用插件来扩展编辑器功能，并且插件是一等公民（slate-angular也可以理解为是一个基础插件），任何高级交互都可以通过开发编辑器插件来实现。</p>
<p>﻿</p>
<p>一、可重写方法</p>
<p>Slate 底层通过抽象出一个一个的可重写方法（deleteBackward、insertBreak、insertText、apply等等）供外部扩展，比如我要实现粘贴时识别Markdown数据格式，可以重写insertText实现，实现回车的特殊处理可以重写insertBreak，相比直接暴露基础事件，提供可重写方式是一个很高级的实现，在slate-angular视图层也单独提供了几个可重写的方法：insertData（处理粘贴数据）、isBlockCard（块级卡片）、onError（错误处理）、onKeydown（基础事件）。</p>
<p>二、自定义渲染</p>
<p>视图层UI部分主要由三层渲染组成，对应三个层级的数据：Element、Text、Leaf ，每一个层级的数据都支持自定义组件/模版渲染，主要是通过renderElement、renderText、renderLeaf实现。</p>
<p>视图层自定义渲染组件的过程概貌：</p>
<p>﻿</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0943686b23114fb8bbdd9b2d6d05f11a~tplv-k3u1fbpfcp-zoom-1.image" alt="三级扩展.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>﻿</p>
<p>这部分主要介绍跟 slate-angular 关联比较大的几个部分：组件化开发编辑器、事件代理、选区同步、插件扩展等，核心还是希望大家可以更多的了解 slate.js 以及 slate-angular，技术上就点到为止，有兴趣的可以阅读源代码或者其它技术资料。</p>
<h2 data-id="heading-13">写在最后</h2>
<p>富文本编辑器是前端中非常复杂的一个领域，未来的道路还很长，我们也希望有更多的开发者能够参与进来，发现并解决诸如浏览器兼容性、兼容移动端、中文输入、标准交互的问题，优化输入代理的机制，优化底层架构，探索基于Slate的协同方案等等。</p>
<p>如有任何问题，欢迎大家给 <a href="https://github.com/worktile/slate-angular" target="_blank" rel="nofollow noopener noreferrer">slate-angular</a> 提 Issues 或者 PRs ！</p></div>  
</div>
            