
---
title: '探索 Vue 3 中的 JSX'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bef087605cbf439dabe402ce39ff272a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 02:24:57 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bef087605cbf439dabe402ce39ff272a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天（5月22日），字节跳动大力智能团队前端工程师林成璋参加了《Vue Conf 21》大会，与各位前端技术爱好者进行了交流，并在会上做了一篇题为《探索 Vue 3 中的 JSX》的分享。以下为此次分享的全部内容。</p>
<h1 data-id="heading-0">引言</h1>
<p>各位同学下午好，我是来自字节跳动大力智能前端团队的林成璋，最近半年的业余时间（再加上一些摸鱼的时间）主要在维护 Vue 3 的 <a href="https://github.com/vuejs/jsx-next" target="_blank" rel="nofollow noopener noreferrer">Babel JSX Plugin</a>，今天来给大家做一个关于 JSX 的分享。</p>
<p>下面是我的 Github 账号，全网除了 P 站应该都是这个头像。其实最早做这个插件主要是为了帮助 Ant Design Vue 和 Vant 能够快速升级到 Vue 3，看过他们源码的同学应该知道，他们的源码大部分都是用 JSX 来撸的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bef087605cbf439dabe402ce39ff272a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然目前在 NPM 上的周下载量是 56 万多（甚至超过了 Vue 3 🤪），但是这里的下载量非常大的原因主要是通过 vue-cli 创建的项目（不管是 Vue 2 还是 Vue 3）都会下载 <code>@vue/babel-plugin-jsx</code> 这个包，实际使用 JSX 的用户应该远比这个数字要小，到底有多少用户是通过的 JSX 的方式开发的也没有办法统计到，绝大用户还是使用 <code>template</code> 的开发方式为主。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c6127c2cecb435f9d7681f77ec485fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">基本概念</h1>
<ul>
<li><strong>template</strong></li>
</ul>
<p>在 Vue 里，<code>sfc</code> 是一个以 <code>.vue</code> 结尾的文件，通常包含三种类型的顶级语言块 <code><template></code>、<code><script></code> 和 <code><style></code>，可以理解为 HTML 、JS 以及 CSS 的组合。每一个 <code>.vue</code> 文件结尾的文件都是一个组件，而且只能 export defualt 出一个组件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa2cafd8f21b40e58ec5e801933e4262~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>JSX</strong></li>
</ul>
<p>本身就是 JS</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00471a51c4d44c8d975b429ac969ea59~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">为什么在 Vue 里也支持 JSX</h1>
<p>Vue 官方推荐的开发方式是 template，从 Vue 2 开始，template 在运行之前，会被编译成 JavaScript 的 render function。这些 <code>render function</code> 在运行时阶段，就是传说中的 <code>Virtual DOM</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee1a66a1fad14c66b03a59809fcd12b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>每当讲到 template 和 JSX，可能就会讨论到一个比较大的问题，<code>React</code> 和 <code>Vue</code> 哪个好。一些人可能就不太喜欢通过 JavaScript 直接来表示 UI，然而也会有相当一部分人会认为用 template 来写可能比较烦，特别是 React 资深玩家。由于 vue 是全球最友好的 UI 框架，有广大的群众基础，一些群众习惯于直接用 HTML 和 CSS 来干代码，对他们来说，把写 UI 的逻辑从 HTML 转到 template ，比让他们的思路完全变更到开始思考如何用 JavaScript 来构建 UI 要简单得多。 但是也不得不承认，对于一些之前是搞后端的同学， 或者 iOS 和 Android 的开发者来说，之前没有怎么接触过 HTML 的，通过字符串模板的方式来编写 UI 也不太行。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e464c05269b4bf88d363307438e6777~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不同用户的口味不太一样，萝卜白菜，各有所爱。就像这张 PPT，有些人看了可能很兴奋，一些人可能觉得我是个傻X。你可以说一堆模板怎么怎么不好的例子，他也同样也给 JSX 一顿喷，谁也说服不了谁。所以 Vue 干脆把两个事都干了。</p>
<h1 data-id="heading-3">什么是「真正的」JSX</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4de975c8ef14c8db74e7a3ae75ad325~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://facebook.github.io/jsx/" target="_blank" rel="nofollow noopener noreferrer">JSX</a> 最早是由 facebook 起草的一个规范，后面的这个 <code>X</code> 可以理解为它是 JavaScript 的语法扩展，感兴趣的同学可以从这个链接进去看看里面的具体内容。由于各个前端框架的实现不一样，所以它不会由引擎或浏览器实现，需要 Transform 之后转成常规的 JS 之后，这一步操作我们可以理解为「赋能」，才能在浏览器里面运行。JSX 其实也和模板语言类似，但它具有 JavaScript 的全部功能，但是由于在模板中的一些限制，用模板写出来的代码性能要比 JSX 好得多。</p>
<pre><code class="copyable"><h1>Hello, world!</h1>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 JSX 语法编译之后其实就是：</p>
<pre><code class="copyable">import &#123; createVNode as _createVNode &#125; from "vue"

_createVNode("h1", null, "Hello, world!");
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">Vue 3 带来的改变</h1>
<p>Vue 2 早期是用纯 JavaScript 来编写的，随着项目越来越庞大，引入了 Facebook 的 <a href="https://flow.org/" target="_blank" rel="nofollow noopener noreferrer">Flow</a>。虽然 Flow 在一定程度上起到了帮助作用，但还是存在一些问题，尤大也曾经公开表示当初没有选择 TypeScript 选择了 Flow 是「押错宝」了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86830b07db2545498f4845f9505215ce~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Vue 2 中，JSX 的编译需要依赖 <code>@vue/babel-preset-jsx</code> 和 <code>@vue/babel-helper-vue-jsx-merge-props</code> 这两个包。前面这个包来负责编译 JSX 的语法，后面的包用来引入运行时的 <code>mergeProps</code> 函数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd03148a222647a6bcf19b386a6010b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是如果你要用 TSX 的环境来写，还需要额外安装 <a href="https://github.com/wonderful-panda/vue-tsx-support" target="_blank" rel="nofollow noopener noreferrer">vue-tsx-support</a>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf2fccd1c734aafbee7e419355d7d80~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Vue 3 中，只要安装一个 Babel 插件就完事了，可以理解为不再需要额外的第三方库，源码中就有 <a href="https://github.com/vuejs/vue-next/blob/master/packages/runtime-dom/types/jsx.d.ts" target="_blank" rel="nofollow noopener noreferrer">jsx.d.ts</a> 用来支持 JSX 的类型检查</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e174bd6f6a7f4e7688756b3401a228ee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">使用 JSX 的场景</h1>
<p>我们现在来看下有哪些场景用 JSX 会比模板更加优雅。</p>
<h2 data-id="heading-6">一个文件写多个组件</h2>
<p>一个 <code>.vue</code> 文件里面只能写一个组件，这个说实话在一些场景下还是不太方便，很多时候我们写一个页面的时候其实可能会需要把一些小的节点片段拆分到小组件里面进行复用，这些小组件其实写个简单的函数组件就能搞定了。如果你现在没有这个习惯可能就是因为 SFC 的限制让你习惯了全部写在一个文件里面。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96f11b0531694b54aa29f80f16c72ff0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如这里我们封装了一个 Input 组件，我们希望同时导出 Password 组件和 Textarea 组件来方便用户根据实际需求使用，而这两个组件本身内部就是用的 Input 组件，只是定制了一些 props。在 JSX 里面就很方便，写个简单的函数组件基本上就够用了，通过 interface 来声明 props 就好了。但是如果是用模板来写，可能就要给拆成三个文件，或许还要再加一个 <code>index.js</code> 的入口文件来导出三个组件，摸鱼的时间又少了。</p>
<h2 data-id="heading-7">强依赖编译时的检查</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee8003d39e847b4bc01385ea9dd2c74~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>模板中引用了一个未在 <code>script</code> 中声明的 a，vscode 插件可以帮忙检查出来，但是仍然可以跑起来。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91534ce6fa0349818df07e2c7de85644~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是用 TS 来写，这里引用了一个未声明的 c 变量，TS 在编译阶段就能让代码直接跑不起来。目前模板还是会被直接编译成 JS，因此还做不到在 <code>template</code> 就进行编译时的类型检查。</p>
<h2 data-id="heading-8">拥有 JS 完全编程能力</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e2180661f1d4d59b723d303a949c2ef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于 JSX 的本质就是 JavaScript，所以它具有 JavaScript 的完全编程能力。举个例子，我们需要通过一段逻辑来对一组 DOM 节点做一次 reverse，如果在模板里面写，那估计要写两段代码。</p>
<p>虽然这个例子可能不太常见，但是不得不否认，在一些场景下，JSX 还是要比模板写起来更加顺手。</p>
<h2 data-id="heading-9">范型组件</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48316b27ad648dab29ebbf38be6e21d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在模板里面，由于一些历史的原因，目前范型组件确实还支持不了，但是不代表以后不行。如果非要用范型，可以先用函数组件给包一层，但是注意不要声明 <code>FunctionalComponent</code> 的类型。这里我们在 <code>.tsx</code> 文件里面声明 <code>Foo</code> 组件，Props 是一个范型。声明完之后，再回到模板里面，可以我们看到，刚刚定义的范型组件已经生效了。SFC 的 TS IDE 支持可以用 volar。volar 还支持了范型组件，用起来感觉和 TSX 已经没多大区别了。</p>
<h1 data-id="heading-10">使用 JSX 需要注意的点</h1>
<h2 data-id="heading-11">对 Props 的处理</h2>
<p>在模板中，对 props 的处理是 merge。为了满足不同用户的需求，开了一个可以覆盖的口子。</p>
<h2 data-id="heading-12">对插槽的处理</h2>
<p>插槽是一种内容分发（content distribution）的 API，洋文叫 Slot，也就是 <code>createVNode</code> 的最后一个参数。适合用在结果比较复杂，组件内容可以复用的地方，简单来说就是在组件中可以预留空间，从父级把内容给传进去。在 JSX 中，父组件给子组件来传递 VNode 通过属性来传递就完事了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dda25068bec4c1bbdaf10fc36a52c31~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在模板中，传递属性的时候，<code>template</code> 里面是不能写 VNode 的，因此 Vue 里出现了插槽这个概念，插槽只在组件的 children 里面才有。</p>
<p>我们来看下 Vue 是怎么处理插槽的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75628a9329e246769b3a9413705bbf5e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Vue 对插槽的要求最好是一个 function，对运行时的性能提升会有很大的帮助。因此 A 组件的子节点会被编译成，<code>&#123; default: () => [123] &#125;</code>。对应到 JSX 中，按照正常用户的心智模式，只有一个 children 的时候，写成<code>&#123; default: () => [123] &#125;</code>也不太现实，正常的写法就是直接塞一个 children。但是在编译阶段要处理成 function，否则在开发时会报 warning，对开发者来说是非常不友好的体验。对编译器来说其实也好办，给子节点的 VNode 包一层函数就完事了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc07843f2002400281499cc6211add9a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在多个插槽的情况下，稍微比单个的场景要复杂点。除了 default 之外的插槽，通过 props 的方式来传是不可能的，只能想办法通过类似「指令」的方式来传递，因此最早设计了 <code>v-slots</code> 的命令来处理插槽。但是 <code>v-slots</code> 对于一些开发者来说可能会不够直观。更直观的方式应该像这样，也就是 <code>obejct slots</code>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/083f805d8d2c4c59ae55ef0b6feff81e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先简单讲一下两个概念：编译和运行时。编译就是把我们的代码转成 JavaScript 引擎可以看懂的代码，运行时就是 JavaScript 引擎开始跑你的代码。就好比我们招聘中的简历筛选和面试，简历筛选可以对应编译，面试来运行时。这个候选人到底怎么样，单纯看简历是看不出来的。再回到刚刚的问题，如果直接把 children 写成一个内联的对象还好办，但如果是一个变量的话，在编译的时候，编译器是无法知道传过来的到底是个什么玩意儿，是 slots 还是 VNode 其实编译的时候看不出来。如果是一个文件里面的，编译器或许还能判断，但是从另一个文件 import 进来，是无法判断的。Babel 处理每一个的文件都是一个「闭环」 。所以这时候就需要加一个运行时的判断：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9b3ca3077c54a43a325c4921dd005f3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然解决了判断是不是 slots 的问题，但是每一个变量给加上运行时判断，会对编译产物的体积有一些影响。<a href="https://github.com/vuejs/jsx-next/issues/255" target="_blank" rel="nofollow noopener noreferrer">jsx-next #255</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/449fd188dad64f10b4636d0d7fcf47b9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了保持编译产物体积和直观语义上的平衡，就让开发自己来选择是否需要上述的 feature，提供了 <code>enableObjectSlots</code> 的开关。</p>
<h1 data-id="heading-13">模板与 JSX 的性能对比</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50977d22df0b438db254a899bf65fda7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>刚刚说了一些在哪些场景下用 JSX 可能会更加地合适。这里简单地对比了下实现相同功能，JSX 和模板的性能差异。左右两个 demo 里面，整了两万个节点，奇数节点里面 <code>class</code> 是动态的，偶数节点的 <code>textContent</code> 是动态的，点击 shuffle。在这个例子里面，用模板写的代码 比用 JSX 写的要快十几毫秒。在实际的场景中，组件的层级嵌套远比这里给出的 demo 要复杂，这个时候就更加能够体现模板的优势了。</p>
<p>在传统的 VDOM 树中，我们在运行时不能够得到用于优化的信息。在 Vue 3 中，充分利用了模板静态信息，最终体现到 VDOM 树上。比方说在 diff 的时候，可以知道哪些节点是动态的，节点的哪些属性是动态的。有了这些信息我们就可以在创建 VNode 的时候来标记哪些属性是不是动态的（靶向更新），也就是传说中 PatchFlags。除了 <code>PatchFlags</code> 之外，Vue 3 的 VDOM 在运行时，还做了一些缓存，比如 children 的缓存。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74de8b310b9242e1845c286b9dd083ef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先来解释一下 <code>PatchFlags</code> 是怎么运作的，其实它就是一个数字，只不过在运行的时候被赋予了不同的含义：</p>
<ul>
<li>
<p>数字 2 (PatchFlags.CLASS)：表示 class 是动态的</p>
</li>
<li>
<p>数字 4 (PatchFlags.STYLE)：表示 style 是动态的</p>
</li>
</ul>
<p>可能一些同学不太明白这样来表示有啥好处 <code>CLASS = 1 << 1</code>，这其实就是用二进制来表示，在上面的代码中：</p>
<pre><code class="copyable">TEXT = 0000000001

CLASS = 0000000010

STYLE = 0000000100
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如一个节点的 class 和 style 都是动态的，就给标记上 <code>PatchFlags.CLASS | PatchFlags.STYLE</code>，得到 <code>0000000011</code> 。想要判断它的 TEXT 是不是动态的，只需要<code>FLAG & TEXT > 0</code> 就行。</p>
<p>这么看起来只要把 <code>props</code> 的属性做标记好像 JSX 里面也能对 VDOM 做标记了？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26232489995b4fc2a823dfe02dbd31e5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们来看稍微复杂点的场景。我们看到 <code>textarea</code> 依赖了 attrs，所以编译完对应的 PatchFlag 应该是</p>
<pre><code class="copyable">_createVNode("textarea", _mergeProps(&#123;
  "id": "textarea"
&#125;, attrs), null, 16);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/683f473c484e45c49bb2b692f43fcf67~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>单独把这段代码拿出来跑是没问题的，但是由于 <code>textarea</code> 的外层还套了一些组件，attrs 是单独定义的一个变量，并不是响应式的。我们先不管 attrs 这个变量，把这段代码当做是模板里面的。在模板编译的时候，A 的 children 在编译的时候其实做了一层缓存，每次重新渲染的时候，不需要再去创建 children 的 VNODE，同时对于 children 来说，形成了一个闭包。如果这段代码编译的时候，把 children 做了缓存，会打上一个静态的标记，那么 attrs 拿到永远是第一次渲染的值。</p>
<pre><code class="copyable"><A>
  &#123;&#123;
      default: () => (
          // children
      )
   &#125;&#125;
</A>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以当点击 <strong>+1s</strong> 的时候，并不会触发视图的更新。这个时候只能放弃组件 A 的优化，children 不做缓存。因此一旦在某个子节点传入了一个非响应式的变量，它的所有父节点的 children 就要放弃缓存，因此在每次 re-render 的时候都会重新创建，优化并不是很明显。然而上面这种写法在 JSX 中还挺常见的。</p>
<p>除了 <code>PatchFlags</code> 之外，Vue 里有一个叫 <code>SlotFlags</code> 概念，来处理 children 的不同情况。上面的情况，需要把 children 标记为 <code>DYNAMIC</code>，来放弃对 children 的缓存。因此如果你用 JSX 来写 Vue 的话，基本上是享受不到 Vue 3 对模板做的优化。</p>
<h1 data-id="heading-14">总结</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3705512322a417a96df38520cc9bb8e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            