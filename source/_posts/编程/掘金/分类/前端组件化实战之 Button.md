
---
title: '前端组件化实战之 Button'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58285f3cce144972b2ccb88e11efd73f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 16:34:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58285f3cce144972b2ccb88e11efd73f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<blockquote>
<p>大家好，我是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyoungjuning.js.org" target="_blank" rel="nofollow noopener noreferrer" title="https://youngjuning.js.org" ref="nofollow noopener noreferrer">洛竹🎋</a>，一只住在杭城的木系前端🧚🏻‍♀️，如果你喜欢我的文章📚，可以通过点赞帮我聚集灵力⭐️。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在 <a href="https://juejin.cn/post/6983854006124675108" target="_blank" title="https://juejin.cn/post/6983854006124675108">《每个前端都应该拥有自己的组件库,就像每个夏天都有西瓜🍉》</a> 一文中，洛竹带领小黑从零搭建了一个组件库项目，完成了项目结构、构建、测试、文档等基础工程化工作并完成了第一个组件 Icon。本期延续上期的组件工程化的主题，夏日炎热，点上一杯杨枝甘露，和洛竹赴一场 Button 开发之约吧。赴约后，你将会收获以下的内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58285f3cce144972b2ccb88e11efd73f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>PS：配合<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fvant-react-native" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/vant-react-native" ref="nofollow noopener noreferrer">仓库</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvant-react-native.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vant-react-native.js.org/" ref="nofollow noopener noreferrer">组件库文档</a>阅读本文效果更佳喲！</p>
</blockquote>
<h2 data-id="heading-1">Button 与设计心理学</h2>
<p>作为前端工程师，入行至今接触最多的就是设计师了。耳濡目染下虽说没学会什么设计工具，但是对设计与人的心理有了一定认识。</p>
<p>洛竹认为任何事物都不可能凭空出现，自有其传承。使用广泛的基础界面元素 Button 也不例外，我们生活中就有随处可见的按钮。举个栗子🌰，每天上班下班必然要按的电梯按钮、手机音量按钮、小米 9 鸡肋的小爱同学唤起按钮。要搞清楚为什么需要按钮，我们有必要探究下生活中这些按钮的作用。</p>
<h3 data-id="heading-2">点一下按钮的快感</h3>
<p>想象一下把键盘按键换成触摸屏，你最在乎的一定是完美还原物理键的敲击感，像洛竹用手机虚拟键盘就喜欢设置按键震动和音效。通过打击（点击）获得快感是较为普遍的人性。按钮在按下、松开时有丰富的质感和交互感，完美满足了人们点一下的快感。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/542a6bbb880e4594ae384ee0bd1e511d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">现实的实用性</h3>
<p>从 BB 机到诺基亚再到如今的智能机，实体按钮削减到只剩下音量键和开关机键。按键虽然光秃秃没有任何标识，但我们就是知道它的功能。试想一下没有这个来自远古时代的开关键，你手里的手机就是一块板砖。</p>
<h3 data-id="heading-4">疯狂暗示用户，达到不可告人目的</h3>
<p>小米 9 单独唤起小爱同学的按键经常会被误按，之前我还不理解这么蠢的设计的目的。在简单研究了点设计心理学我明白了。小爱的设计者为了 产品日活和 AI 训练就是故意这个设计的。</p>
<p>小米 10 虽然移除了单独的唤起键，却把原来的电源键改成了一键多用。每次想要重启手机还得先唤起一下小爱同学。不得不说，小爱同学小米亲女儿。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/633381b8c2c342ed94bf024dbc19cf76~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>吐槽归吐槽，小米这个按钮确实起到了培养用户习惯的任务。当用户知悉某个按钮能指向某个操作，或者获取某类信息后，长此以往用户就会形成使用习惯。如果某操作能够为用户和厂商持续带来价值，那就可以让按钮的位置更加醒目，持续培养用户点击习惯。</p>
<h3 data-id="heading-5">指引用户操作</h3>
<p>这个在 Web 开发中是最常见的使用场景，每个可交互页面上都有这类按钮的出现，用来指引用户下一步该怎么做。比如表单的提交和重置。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2c2a8abbe84471f96a67e18196c53fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然按钮也常作为表单元素，但是区别于其他表单元素，按钮因其天然地自说明性，不需要 Label 对其进行辅助说明，啰嗦这么多，掘友们应该在看到一个按钮时，应该也会有从设计上品鉴的意识了，欢迎将对下图的品鉴在评论区告诉洛竹。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88c6754b28984fc3866319c35790fc03~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">组件主题化</h2>
<p>在开始开发具体组件之前，我们必须先约定好组件主题化的规范。之前 antd-mobile-rn 就因为设计问题，中途花费大力气重构。几乎所有的组件库都会将色彩、布局这些以 css 变量的形式提供给使用者和开发者为，React Native 不同的是样式基于 CSS in JS，不过道理相通，参照 vant 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyouzan%2Fvant%2Fblob%2Fdev%2Fsrc%2Fstyle%2Fvar.less" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youzan/vant/blob/dev/src/style/var.less" ref="nofollow noopener noreferrer">设计资源</a>，我们抽出了一套 JavaScript 常量：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// packages/themes</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> Theme &#123;
  <span class="hljs-string">'animation-duration-base'</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-string">'animation-duration-fast'</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-string">'animation-timing-function-enter'</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-string">'animation-timing-function-leave'</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-string">'font-size-xs'</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-string">'font-size-sm'</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-string">'font-size-md'</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-string">'font-size-lg'</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-string">'font-weight-bold'</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-comment">// 变量过多，这里仅展示部分变量</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了这些 JS 常量，我们就可以设计主题系统。基于 CSS in JS 的主题化设计一般是基于 React Context 实现，需要提供 ThemeProvider 传入主题上下文，ThemeConsumer、WithTheme（高阶类组件）、withTheme（高阶函数组件） 或 useTheme（React Hooks）作为消费者获取上下文。自己实现也不难，不过更文任务比较紧急，我们先基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcssinjs%2Ftheming" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cssinjs/theming" ref="nofollow noopener noreferrer">cssinjs/theming</a> 实现功能，后期有需要再回来造轮子也不迟。下面👇就是我们基于 theming 的 <code>createTheming</code> 函数创建自定义主题上下文。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createTheming &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'theming'</span>;
<span class="hljs-keyword">const</span> context = React.createContext(defaultTheme);
<span class="hljs-keyword">const</span> theming = createTheming(context);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; ThemeProvider, withTheme, useTheme &#125; = theming;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>主题功能是通用的，因此我将主题相关的能力都放在 <code>@vant-react-native/theme</code> 包中发布。</p>
</blockquote>
<h2 data-id="heading-7">Button 的实现</h2>
<p>React Native 内置的 Button 组件的样式是固定的，只能进行一些简单的设置。且内置的 Button 组件在 Android 和 ios 两个平台上的表现并不一致。所以我们需要根据更底层的组件进行封装。我们对比 ant-design-mobile-rn 和 react-native-elements 后采用了前者使用的 <code>TouchableHighlight</code> 组件。由于继承自 TouchableHighlight，所以我们组件的 Props 类型如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; TouchableHighlightProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">interface</span> ButtonProps <span class="hljs-keyword">extends</span> TouchableHighlightProps &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">按钮类型</h3>
<p>vant 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyouzan.github.io%2Fvant%2F%23%2Fzh-CN%2Fbutton%23an-niu-lei-xing" target="_blank" rel="nofollow noopener noreferrer" title="https://youzan.github.io/vant/#/zh-CN/button#an-niu-lei-xing" ref="nofollow noopener noreferrer">Button</a> 支持 <code>default</code>、<code>primary</code>、<code>info</code>、<code>warning</code>、<code>danger</code> 五种类型，默认为 <code>default</code>。现在，组件的基本定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">import</span> React, &#123; FunctionComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; Text, View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;

<span class="hljs-keyword">interface</span> ButtonProps &#123;
  <span class="hljs-keyword">type</span>?: <span class="hljs-string">'default'</span> | <span class="hljs-string">'primary'</span> | <span class="hljs-string">'info'</span> | <span class="hljs-string">'warning'</span> | <span class="hljs-string">'danger'</span>;
&#125;

<span class="hljs-keyword">const</span> Button: FunctionComponent<ButtonProps> = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的组件为了适应主题化需求，样式不能是写死在组件里的，而是要通过上下文获取样式常量。我们思路是首先使用 <code>useTheme</code> 从上下文中获取主题，然后由于样式定义较多，我们为每个组件编写一个 <code>useStyle</code> hook 放在单独的 style.ts 文件中：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; StyleSheet &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>;
<span class="hljs-keyword">import</span> &#123; Theme, useTheme &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vant-react-native/theme'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useStyle = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> theme = useTheme<Theme>();

  <span class="hljs-keyword">const</span> getBackgroundColor = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">switch</span> (props.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'primary'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'success-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'info'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'primary-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'warning'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'warning-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'danger'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'danger-color'</span>];
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> theme.white;
    &#125;
  &#125;;

  <span class="hljs-keyword">const</span> getTextColor = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (props.type === <span class="hljs-string">'default'</span>) &#123;
      <span class="hljs-keyword">return</span> theme.black;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> theme.white;
    &#125;
  &#125;;

  <span class="hljs-keyword">const</span> getBorderRadius = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (props.round) &#123;
      <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'border-radius-max'</span>];
    &#125;
    <span class="hljs-keyword">if</span> (props.square) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'border-radius-sm'</span>];
  &#125;;

  <span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
    <span class="hljs-attr">container</span>: &#123;
      <span class="hljs-attr">alignItems</span>: <span class="hljs-string">'center'</span>,
      <span class="hljs-attr">backgroundColor</span>: getBackgroundColor(),
      <span class="hljs-attr">borderColor</span>: getBorderColor(),
      <span class="hljs-attr">borderRadius</span>: theme[<span class="hljs-string">'border-radius-sm'</span>],
      <span class="hljs-attr">borderWidth</span>: theme[<span class="hljs-string">'border-width-base'</span>],
      <span class="hljs-attr">flexDirection</span>: <span class="hljs-string">'row'</span>,
      <span class="hljs-attr">flex</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">justifyContent</span>: <span class="hljs-string">'center'</span>,
      <span class="hljs-attr">opacity</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">paddingHorizontal</span>: <span class="hljs-number">15</span>,
    &#125;,
    <span class="hljs-attr">indicator</span>: &#123;
      <span class="hljs-attr">marginRight</span>: theme[<span class="hljs-string">'padding-xs'</span>],
    &#125;,
    <span class="hljs-attr">textStyle</span>: &#123;
      <span class="hljs-attr">color</span>: getTextColor(),
      <span class="hljs-attr">fontSize</span>: <span class="hljs-number">14</span>,
    &#125;,
    <span class="hljs-attr">wrapper</span>: &#123;
      <span class="hljs-attr">borderRadius</span>: theme[<span class="hljs-string">'border-radius-sm'</span>],
      <span class="hljs-attr">height</span>: <span class="hljs-number">44</span>,
    &#125;,
  &#125;);
  <span class="hljs-keyword">return</span> styles;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于 <code>useStyle</code> 我们便可完成一个支持多类型的 Button 组件：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> Button: FunctionComponent<ButtonProps> = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> styles = useStyle(props);
  <span class="hljs-keyword">const</span> &#123; style, ...restProps &#125; = props;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">TouchableHighlight</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;[styles.wrapper,</span> <span class="hljs-attr">style</span>]&#125; &#123;<span class="hljs-attr">...restProps</span>&#125;></span>
      <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.container&#125;</span>></span>
        &#123;typeof props.children === 'string' ? (
          <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.textStyle&#125;</span>></span>&#123;props.children&#125;<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        ) : (
          props.children
        )&#125;
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">TouchableHighlight</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：子组件可能是字符串，也可能是组件，所以需要判断类型。</p>
</blockquote>
<p>实现效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a0b412c227e4dc994b818294165240d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">朴素按钮</h3>
<p>朴素按钮的文字为按钮颜色，背景为白色，我们通过 <code>plain</code> 属性将按钮设置为朴素按钮。调研了 antd 和 react-native-elements 发现它们都是定义了很多样式，然后在组件内通过逻辑判断计算具体样式的值。个人很不喜欢这种方式，不是彻底的 CSS in JS，我的处理方式是将所有有关样式计算的都封装在每个组件的 <code>useStyle</code> 钩子中，比如当引入朴素按钮属性时，相对于普通按钮改变的有容器背景色、容器边框和字体颜色。所以我们将这三个属性的值都通过一个单独的函数计算。对比 antd 的源码，会发现不仅代码更易读，甚至代码量也少了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getBackgroundColor = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (props.plain) &#123;
    <span class="hljs-keyword">return</span> theme.white;
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;;

<span class="hljs-keyword">const</span> getTextColor = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (props.plain) &#123;
    <span class="hljs-keyword">switch</span> (props.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'primary'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'success-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'info'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'primary-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'warning'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'warning-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'danger'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'danger-color'</span>];
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'gray-3'</span>];
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (props.type === <span class="hljs-string">'default'</span>) &#123;
    <span class="hljs-keyword">return</span> theme.black;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> theme.white;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fc1bedf56fe4dd0a31e6d18b048665c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">细边框</h3>
<p>vant 实现细边框是通过设置 <code>hairline</code> 属性可以展示 0.5px 的细边框。但是手机上由于分辨率的影响，贸然设置 0.5 会导致边框不显示的兼容问题。好在 React Native 为我们提供了 <code>StyleSheet.hairlineWidth</code> 常量来兼容最细边框问题，下面是官方对它的定义：</p>
<blockquote>
<p>hairlineWidth 这一常量始终是一个整数的像素值（线看起来会像头发丝一样细），并会尽量符合当前平台最细的线的标准。可以用作边框或是两个元素间的分隔线。然而，你不能把它“视为一个常量”，因为不同的平台和不同的屏幕像素密度会导致不同的结果。</p>
<p>如果模拟器缩放过，可能会看不到这么细的线。</p>
</blockquote>
<p>由于 <code>hairline</code> 只影响了容器 <code>borderWidth</code> 属性，我们不需要编写单独的样式计算函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">borderWidth</span>: props.hairline ? theme[<span class="hljs-string">'border-width-hairline'</span>] : theme[<span class="hljs-string">'border-width-base'</span>],
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43d80d537b07487d9043d718e6541f7e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">禁用状态</h3>
<p>表单元素或者说可触摸可点击的元素一般都有禁用状态，vant 中是通过 disabled 属性来禁用按钮，禁用状态下按钮不可点击。TouchableHighlight 继承地有 <code>disabled</code> 属性，我们只需要设置一些禁用状态下的按钮样式就可以，查看 vant 源码我们发现只需要修改透明度为 0.5 即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">opacity</span>: props.disabled ? <span class="hljs-number">0.5</span> : <span class="hljs-number">1</span>,
    <span class="hljs-comment">// ...</span>
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892589086d07426a8346319d8466bccf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">加载状态</h3>
<p>vant 是通过 <code>loading</code> 属性设置按钮为加载状态，加载状态下默认会隐藏按钮文字，可以通过 <code>loading-text</code> 设置加载状态下的文字。我们借助 React Native 的 ActivityIndicator 组件可以轻松实现这个特性：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// ...</span>
<TouchableHighlight &#123;...restProps&#125;>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.contentWrapper&#125;</span>></span>
    &#123;props.loading ? (
      <span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">ActivityIndicator</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"small"</span> <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;indicatorColor&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.indicator&#125;</span> /></span>
        &#123;props.loadingText ? <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;styles.textStyle&#125;</span>></span>&#123;props.loadingText&#125;<span class="hljs-tag"></<span class="hljs-name">Text</span>></span> : null&#125;
      <span class="hljs-tag"></></span></span>
    ) : <span class="hljs-literal">null</span>&#125;
  </View>
</TouchableHighlight>
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useIndicatorColor = (props: ButtonProps): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  <span class="hljs-keyword">const</span> theme = useTheme<Theme>();
  <span class="hljs-keyword">if</span> (props.plain) &#123;
    <span class="hljs-keyword">switch</span> (props.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'primary'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'success-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'info'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'primary-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'warning'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'warning-color'</span>];
      <span class="hljs-keyword">case</span> <span class="hljs-string">'danger'</span>:
        <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'danger-color'</span>];
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> theme.black;
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (props.type === <span class="hljs-string">'default'</span>) &#123;
    <span class="hljs-keyword">return</span> theme.black;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> theme.white;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c4340df2254245a3c830bf667a2e28~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">按钮形状</h3>
<p>默认的按钮有值为 2 的圆角，vant 中通过 <code>square</code> 设置方形按钮，通过 <code>round</code> 设置圆形按钮。按例，我们通过判断设置样式：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getBorderRadius = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (props.round) &#123;
    <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'border-radius-max'</span>];
  &#125;
  <span class="hljs-keyword">if</span> (props.square) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-keyword">return</span> theme[<span class="hljs-string">'border-radius-sm'</span>];
&#125;;
<span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-attr">borderColor</span>: getBorderColor(),
  &#125;,
  <span class="hljs-attr">wrapper</span>: &#123;
    <span class="hljs-attr">borderRadius</span>: getBorderRadius(),
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1402517566e49d1a1920fd9b3f7bb20~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">按钮尺寸</h3>
<p>Antd RN 只提供了 large、small 两个尺寸，而在 vant 中支持 large、normal、small、mini 四种尺寸，默认为 normal。虽然写到这里已经很疲倦了，杨枝甘露也早喝完了，但是为了完整复原，还是续上一杯咖啡继续肝。根据 vant 设计稿我们新增三个样式获取函数并动态化指定样式：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> getSizeHeight = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">switch</span> (props.size) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'large'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">50</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'small'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">32</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'mini'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">24</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">44</span>;
  &#125;
&#125;;
<span class="hljs-keyword">const</span> getSizePadding = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">switch</span> (props.size) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'small'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">8</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'mini'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">4</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">15</span>;
  &#125;
&#125;;
<span class="hljs-keyword">const</span> getSizeFontSize = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">switch</span> (props.size) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'large'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">16</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'small'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">12</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'mini'</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">10</span>;
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-number">14</span>;
  &#125;
&#125;;

<span class="hljs-keyword">const</span> styles = StyleSheet.create(&#123;
  <span class="hljs-attr">container</span>: &#123;
    <span class="hljs-attr">paddingHorizontal</span>: getSizePadding(),
  &#125;,
  <span class="hljs-attr">textStyle</span>: &#123;
    <span class="hljs-attr">fontSize</span>: getSizeFontSize(),
  &#125;,
  <span class="hljs-attr">wrapper</span>: &#123;
    <span class="hljs-attr">height</span>: getSizeHeight(),
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59c01002f25b477d85ed26fa1e21c86b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">自定义颜色</h3>
<p>如果不是自己亲自复刻 Vant，是没想到一个 Button 能玩出这么多花，支持特性这么多耐心和代码管理都是一个挑战。当然了，洛竹采取的样式管理方式比较偏激，大家有好的方式也可以在评论区讨论。</p>
<p>通过 <code>color</code> 属性自定义按钮的颜色。我们可以得出需求，不管 type 是什么，<code>color</code> 属性需始终覆盖原有样式，color 能影响的就是背景色、字体颜色和边框颜色，所以我们修改 <code>getBackgroundColor</code>、<code>getTextColor</code>、<code>getBorderColor</code> 样式函数在合适的地方加上以下代码即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (props.color) &#123;
  <span class="hljs-keyword">return</span> props.color;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8efffdbfd6424618be6152895a53e8ee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">双击事件的实现</h2>
<p>我们从 React Native 内置的 TouchableHighlight 组件继承了很多事件，其中 onPress、onLongPress 分别代表单击和长按。但唯独“双击 666”的双击事件没有姓名。之前在实际业务曾经封装过双击事件，这次我们就直接就内置了。</p>
<p>实现思路是延时执行单击事件（默认 200 毫秒），然后记录点击次数和两次时间间隔，当识别为第二次点击且时间间隔小于单击延时时间。那么就取消单击事件延时，并立即执行双击事件。完整代码如下：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">let</span> lastTime = <span class="hljs-number">0</span>;
<span class="hljs-keyword">let</span> clickCount = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> timeout = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">const</span> _onPress = <span class="hljs-function">(<span class="hljs-params">event: GestureResponderEvent</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> now = <span class="hljs-built_in">Date</span>.now();
  <span class="hljs-keyword">if</span> (timeout) &#123;
    <span class="hljs-built_in">clearTimeout</span>(timeout);
  &#125;
  timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    props.onPress(event);
    clickCount = <span class="hljs-number">1</span>;
    lastTime = <span class="hljs-number">0</span>;
  &#125;, props.delayDoublePress);
  <span class="hljs-keyword">if</span> (clickCount === <span class="hljs-number">2</span> && now - lastTime <= props.delayDoublePress) &#123;
    <span class="hljs-built_in">clearTimeout</span>(timeout);
    clickCount = <span class="hljs-number">1</span>;
    lastTime = <span class="hljs-number">0</span>;
    props.onDoublePress(event);
  &#125; <span class="hljs-keyword">else</span> &#123;
    clickCount++;
    lastTime = now;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家会发现这里的实现糅合了函数防抖、节流以及计数器的原理，有兴趣的小伙伴可以自行复习下原理，这里就不展开了。</p>
<h2 data-id="heading-17">API 文档</h2>
<p>一个组件的文档，除了 Demo，还需要展示出来可用的 Props，Dumi 内置的 <code><API></API></code> 组件可以根据组件自动生成 API 文档。首先我们像下面一样编写 Props 注释：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> ButtonProps <span class="hljs-keyword">extends</span> TouchableHighlightProps &#123;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@description       </span>Can be set to primary、info、warning、danger
   * <span class="hljs-doctag">@description</span>.zh-CN 类型，可选值为 primary、info、warning、danger
   */</span>
  <span class="hljs-keyword">type</span>?: <span class="hljs-string">'default'</span> | <span class="hljs-string">'primary'</span> | <span class="hljs-string">'info'</span> | <span class="hljs-string">'warning'</span> | <span class="hljs-string">'danger'</span>;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@description       </span>Can be set to large、small、mini
   * <span class="hljs-doctag">@description</span>.zh-CN 尺寸，可选值为
   */</span>
  size?: <span class="hljs-string">'large'</span> | <span class="hljs-string">'normal'</span> | <span class="hljs-string">'small'</span> | <span class="hljs-string">'mini'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 Markdown 中引入 API 组件即可：</p>
<pre><code class="hljs language-md copyable" lang="md"><span class="xml"><span class="hljs-tag"><<span class="hljs-name">API</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./index.tsx"</span>></span></span><span class="xml"><span class="hljs-tag"></<span class="hljs-name">API</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内置组件 API 没有处理继承的情况，我们后续会自定义一个 API 组件，这里就不展开了，浏览 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvant-react-native.js.org%2Fcomponents%2Fbutton%23api" target="_blank" rel="nofollow noopener noreferrer" title="https://vant-react-native.js.org/components/button#api" ref="nofollow noopener noreferrer">Button 文档</a> 可以查看现在的效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bedac7240334ff79c4142005a66b158~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">工程化串讲</h2>
<p>由于很难在一篇文章中将组件开发相关的工程化讲完，在本篇开始 Button 之旅前，我们还是有一些工程化相关的事情要介绍一下。</p>
<h3 data-id="heading-19">组件创建脚手架</h3>
<blockquote>
<p>小黑：洛竹，<code>lerna create</code> 命令创建出来的模块并不是我们想要的，以后要创建很多很多组件，我们可以写一个创建组件模块的脚手架吗？</p>
</blockquote>
<p>lerna 使用起来是有不少痛点的，<code>lerna create</code> 命令没办法指定模板，考虑到之后的几十上百个组件每次创建都要进行项目结构、Typescript 配置、单元测试配置、Babel 配置等等工作步骤，我们有必要写一个脚手架。</p>
<h4 data-id="heading-20">模板解析</h4>
<p>说到模板解析，相信大家和我一样想到的是 vue-cli 的 template 解析。通过阅读 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Fvue-cli%402.9.6%2Flib%2Fgenerate.js" target="_blank" rel="nofollow noopener noreferrer" title="https://cdn.jsdelivr.net/npm/vue-cli@2.9.6/lib/generate.js" ref="nofollow noopener noreferrer">vue-cli@2.9.6 generate.js</a> 源码，我们可以分析出尤大是基于 metalsmith、handlebars、consolidate 这三个包来实现模板解析能力的。让人不安的是其中 metalsmith 库有长达 5 年没有维护了，洛竹挑选开源项目一般对维护度很敏感，本着轮子要用自己造的原则，我翻看了 Metalsmith 的 Readme 发现这个插件无非是通过递归读文件的方式渲染模板，并且它的静态网站生成的能力对我们模板解析的需求也是多余的。</p>
<p>说干就干，在和 <a href="https://juejin.cn/user/3175045313873943" target="_blank" title="https://juejin.cn/user/3175045313873943">@林小帅</a> 同学简单沟通后，我动手造了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fhandlebars-template-compiler" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/handlebars-template-compiler" ref="nofollow noopener noreferrer">handlebars-template-compiler</a> 这个轮子，其主要原理如下：</p>
<ol>
<li>使用 recursive-readdir 递归获取所有文件路径</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> files = <span class="hljs-keyword">await</span> recursive(rootDir);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用 <code>handlebars.compile</code> 方法使用元数据对模板进行渲染</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> content = fs.readFileSync(file).toString();
<span class="hljs-keyword">const</span> result = handlebars.compile(content)(meta);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用 <code>fs.writeFileSync</code> API 重写文件</li>
</ol>
<p>另外，通过引入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fmicromatch" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/micromatch" ref="nofollow noopener noreferrer">glob</a> 模式匹配实现了 <code>exclude</code> 配置以及只处理指定后缀（默认 <code>**/*.tpl.*</code>）的文件来避免不必要的渲染。（PS：NPM 一周有了 300 多下载，有需要的掘友值得一试😄）</p>
<h4 data-id="heading-21">Node CLI（@vant-react-native/scripts）搭建</h4>
<p>这里洛竹尝试用最简洁的语言为大家描述一个脚手架的诞生，源码在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fvant-react-native%2Ftree%2Fmain%2Fpackages%2Fscripts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/vant-react-native/tree/main/packages/scripts" ref="nofollow noopener noreferrer">packages/scripts</a> 目录下，没有接触过 CLI 的掘友请相信我，Node CLI 很容易上手的。接触过的同学也可以查漏补缺借鉴一二。</p>
<ol>
<li><code>package.json</code> 文件的 <code>bin</code> 字段是我们脚手架的入口</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 指定可执行文件的位置以及别名</span>
<span class="hljs-string">"bin"</span>: &#123;
  <span class="hljs-attr">"vant"</span>: <span class="hljs-string">"./bin/cli.js"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>定义 <code>./bin/cli.js</code> 为可执行文件并调用 <code>init</code> 方法。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 由于我们的脚本是 Node 编写的，所以需要指定 node 所在位置</span>
#!<span class="hljs-regexp">/usr/</span>bin/env node
<span class="hljs-keyword">const</span> &#123; init &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../lib'</span>);
<span class="hljs-comment">// 这个地方参考了 create-react-native 的设计</span>
<span class="hljs-comment">// 本文点赞过 300，下一篇洛竹带小黑为大家带来《基于 TypeScript 重构 create-react-native》</span>
init();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>然后在 <code>src/index.ts</code> 中初始化 commander 这个久负盛名的命令行框架</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> init = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-keyword">const</span> packageJson = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>);
  program.version(packageJson.version).description(packageJson.description);
  <span class="hljs-comment">// ...</span>
  program.parse(process.argv);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>为了方便管理命令，我们将命令都放置在 <code>src/commands</code> 目录下并通过 <code>fs.readdirSync</code> API 动态扫描注册。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> init = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 这段代码借鉴自 NeteaseCloudMusicApi 项目，作者的代码很有设计感，推荐阅读。</span>
  fs.readdirSync(path.join(__dirname, <span class="hljs-string">'commands'</span>)).forEach(<span class="hljs-function">(<span class="hljs-params">file: <span class="hljs-built_in">string</span></span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!file.endsWith(<span class="hljs-string">'.js'</span>)) <span class="hljs-keyword">return</span>;
    <span class="hljs-built_in">require</span>(path.join(__dirname, <span class="hljs-string">'commands'</span>, file));
  &#125;);
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>最后在 <code>commands</code> 目录下新建一个 <code>create.ts</code> 文件编写命令</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; program &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
program
  .command(<span class="hljs-string">'create <name> [loc]'</span>)
  .description(<span class="hljs-string">'Create a new vant-react-native package'</span>)
  .action(<span class="hljs-function">(<span class="hljs-params">name,loc</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello Luozhu'</span>);
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">脚手架实现</h4>
<p>上一小结，我们初始化了 CLI 并添加了 <code>create</code> 命令，这一小节我们就来实现一下脚手架功能。</p>
<p>我们首先在 <code>packages/scripts</code> 目录下创建组件模板</p>
<pre><code class="hljs language-sh copyable" lang="sh">.
├── README.tpl.md <span class="hljs-comment"># tpl 后缀在生成组件模板的时候会被 handlebars-template-compiler 自动去掉。</span>
├── package.tpl.json
├── src
│   └── index.ts <span class="hljs-comment"># 没有 tpl 后缀则不会被编译，模板很大时可以节省时间。</span>
└── tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们明确我们的模板元数据的数据结构，我这里的数据结构是：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> IMeta &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  version: <span class="hljs-built_in">string</span>;
  description: <span class="hljs-built_in">string</span>;
  author: <span class="hljs-built_in">string</span>;
  email: <span class="hljs-built_in">string</span>;
  url: <span class="hljs-built_in">string</span>;
  directory: <span class="hljs-built_in">string</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了数据结构，我们就可以使用 inquirer 模块引导用户输入信息。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> inquirer <span class="hljs-keyword">from</span> <span class="hljs-string">'inquirer'</span>;
<span class="hljs-comment">// ...</span>
<span class="hljs-comment">// getQuestions 过长，感兴趣的同学可以查看：http://tny.im/UFbg</span>
<span class="hljs-keyword">const</span> answer: IMeta = <span class="hljs-keyword">await</span> inquirer.prompt(getQuestions(name));
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一步，我们使用 <code>tmp-promise</code> 模块创建一个系统临时文件夹，并将前文提到的 template 文件夹的内容拷贝进去：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> tmp <span class="hljs-keyword">from</span> <span class="hljs-string">'tmp-promise'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> tmpdir = <span class="hljs-keyword">await</span> tmp.dir(&#123; <span class="hljs-attr">unsafeCleanup</span>: <span class="hljs-literal">true</span> &#125;);
fs.copySync(path.join(__dirname, <span class="hljs-string">'../../template'</span>), tmpdir.path);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们对临时文件夹的内容进行编译再拷贝到指定位置即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> htc <span class="hljs-keyword">from</span> <span class="hljs-string">'handlebars-template-compiler'</span>;
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">await</span> htc<IMeta>(answer, tmpdir.path);
fs.copySync(tmpdir.path, <span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/packages/<span class="hljs-subst">$&#123;locPath&#125;</span>`</span>);
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>折腾这一顿，让我们来看下成果吧：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ba477bcbd8b4ef6b880c7e8e5a095bc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">Github CODEOWENERS</h3>
<p>大型的开源项目最难的不是技术问题，技术大咖永远不会缺。最难的其实是协作和后期维护。试想一下一个成百上千人参与的项目当有新的 pr 时，正常人根本无力去快速检索出需要谁去 review 代码。我们的 vant-react-native 由于是将每个组件单独发包维护，当参与的小伙伴多了也会产生这个困扰。</p>
<p>而 GitHub CODEOWNERS（代码所有者）就是为了解决这个问题的，在 5000+ 贡献者参与的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FDefinitelyTyped%2FDefinitelyTyped" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/DefinitelyTyped/DefinitelyTyped" ref="nofollow noopener noreferrer">DefinitelyTyped</a> 项目中我们就可以看到它的身影。官方对代码所有者定义如下：</p>
<blockquote>
<p>你可以使用 CODEOWNERS 文件定义负责仓库代码的个人或团队。当有人修改代码并打开一个 pull request 时，将自动请求代码所有者进行审查。</p>
</blockquote>
<p>CODEOWNERS 文件使用遵循 gitignore 文件中所用大多数规则的模式，CODEOWNERS 文件位置一般位于 <code>.github/</code> 目录下。</p>
<p>在 vant-react-native，洛竹是仓库的最终负责人，所以是期望每个 pr 都可以分配给自己审查一下的。那么我们这就来实验一下吧，新建一个 <code>.github/CODEOWNERS</code> 文件并写入以下内容：</p>
<pre><code class="copyable"># This is a comment.
# Each line is a file pattern followed by one or more owners.

# These owners will be the default owners for everything in
# the repo. Unless a later match takes precedence,
# @youngjuning will be requested for review when someone opens a pull request.
*       @youngjuning

# In this example, @doctocat owns any files in the build/logs
# directory at the root of the repository and any of its
# subdirectories.
/packages/ @luozhu1994
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般如果文件具有代码所有者，则在打开拉取请求之前可以看到代码所有者是谁。在仓库中，你可以找到文件并悬停于一个锁图标上，悬浮之后会告诉你该文件所有者是谁：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/726bd5144a104902ae27ad31e1d46f93~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们提交一个 pr 看看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4cb8b7ef5c41989660e735e621fc4e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">NPM 发包自动化</h3>
<p>发包权限一般只有仓库所有者一个人拥有，但是 owner 同时维护好几个 NPM 账号，或者是 owner 忽然很忙将发布权限交给其他人管理员但是不便告知 NPM 账号该怎么办呢？答案是将 NPM 发包 CD（持续部署）化，公司一般会基于 Gitlab 或自建平台实现该功能。作为开源项目，我们当然是使用 GitHub Action。</p>
<p>正常的单包项目，使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FJS-DevTools%2Fnpm-publish" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/JS-DevTools/npm-publish" ref="nofollow noopener noreferrer">npm-publish</a> 或 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpascalgn%2Fnpm-publish-action" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pascalgn/npm-publish-action" ref="nofollow noopener noreferrer">npm-publish-action</a> 这两个 GitHub Action，这并没有好讲的。但是基于 lerna 的多包单体仓库并没有现成的插件可以用，照例，我们来看下自己实现的步骤：</p>
<ol>
<li>判断 commit message 是否以 <code>chore(release):</code> 开头
<blockquote>
<p>通过 GitHub Action <code>startsWith(github.event.head_commit.message, 'chore(release):')</code> 实现</p>
</blockquote>
</li>
<li>通过 NPM publish token 认证登录
<blockquote>
<p>通过 <code>npm config set //registry.npmjs.org/:_authToken=$&#123;&#123; secrets.NPM_TOKEN &#125;&#125;</code> 认证</p>
</blockquote>
</li>
<li>执行 <code>lerna publish from-package --yes</code> 发布
<blockquote>
<p>需要本地先执行 <code>lerna version</code> 系列命令提升版本</p>
</blockquote>
</li>
</ol>
<p>完整 GitHub Action 实现如下：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">name:</span> <span class="hljs-string">npm-publish</span>

<span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-attr">branches:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">main</span>

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">npm-publish:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">if:</span> <span class="hljs-string">startsWith(github.event.head_commit.message,</span> <span class="hljs-string">'chore(release):'</span><span class="hljs-string">)</span>
    <span class="hljs-attr">steps:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">c-hive/gha-yarn-cache@v2</span> <span class="hljs-comment"># 缓存 node_modules 加快构建速度</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">Packages</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">yarn</span> <span class="hljs-string">install</span> <span class="hljs-string">--registry=https://registry.npmjs.org/</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Authenticate</span> <span class="hljs-string">with</span> <span class="hljs-string">Registry</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">|
          npm config set //registry.npmjs.org/:_authToken=$&#123;NPM_TOKEN&#125;
</span>        <span class="hljs-attr">env:</span>
          <span class="hljs-attr">NPM_TOKEN:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.NPM_TOKEN</span> <span class="hljs-string">&#125;&#125;</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Publish</span> <span class="hljs-string">package</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">lerna</span> <span class="hljs-string">publish</span> <span class="hljs-string">from-package</span> <span class="hljs-string">--yes</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了在发布后及时获取通知，洛竹使用了 <code>peter-evans/commit-comment</code> 插件在发布失败或成功后对相应 commit 进行评论，这样我们就可以收到邮件和站内通知。</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">commit</span> <span class="hljs-string">comment</span> <span class="hljs-string">after</span> <span class="hljs-string">publish</span> <span class="hljs-string">successfully</span>
  <span class="hljs-attr">if:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">success()</span> <span class="hljs-string">&#125;&#125;</span>
  <span class="hljs-attr">uses:</span> <span class="hljs-string">peter-evans/commit-comment@v1</span>
  <span class="hljs-attr">with:</span>
    <span class="hljs-attr">body:</span> <span class="hljs-string">|
      Hello Dear @youngjuning. This commit has been publish to NPM successfully.
      > Created by [commit-comment][1]
</span>
      [<span class="hljs-number">1</span>]<span class="hljs-string">:</span> <span class="hljs-string">https://github.com/peter-evans/commit-comment</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">commit</span> <span class="hljs-string">comment</span> <span class="hljs-string">after</span> <span class="hljs-string">publish</span> <span class="hljs-string">unsuccessfully</span>
  <span class="hljs-attr">if:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">failure()</span> <span class="hljs-string">&#125;&#125;</span>
  <span class="hljs-attr">uses:</span> <span class="hljs-string">peter-evans/commit-comment@v1</span>
  <span class="hljs-attr">with:</span>
    <span class="hljs-attr">body:</span> <span class="hljs-string">|
      Hello Dear @youngjuning. This commit has been publish to NPM unsuccessfully.
      > Created by [commit-comment][1]
</span>
      [<span class="hljs-number">1</span>]<span class="hljs-string">:</span> <span class="hljs-string">https://github.com/peter-evans/commit-comment</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">致谢</h2>
<p>截止发稿时，<a href="https://juejin.cn/post/6983854006124675108" target="_blank" title="https://juejin.cn/post/6983854006124675108">每个前端都值得拥有自己的组件库，就像每个夏天都拥有西瓜🍉</a> 已获得近 1600 赞、超 4 万阅读📖，再次再次感谢掘友的支持、编辑 Zoe 的鞭策，月影大佬的转载、朋友的转发以及自己的坚持。</p>
<h2 data-id="heading-26">近期好文</h2>
<ul>
<li><a href="https://juejin.cn/post/6983854006124675108" target="_blank" title="https://juejin.cn/post/6983854006124675108">每个前端都值得拥有自己的组件库，就像每个夏天都拥有西瓜🍉</a></li>
<li><a href="https://juejin.cn/post/6969544464113074189" target="_blank" title="https://juejin.cn/post/6969544464113074189">基于 lerna 的多包 JavaScript 项目搭建维护</a></li>
<li><a href="https://juejin.cn/post/6877462747631026190" target="_blank" title="https://juejin.cn/post/6877462747631026190">一文搞定 Conventional Commits</a></li>
<li><a href="https://juejin.cn/post/6955402195311263751" target="_blank" title="https://juejin.cn/post/6955402195311263751">2021 年最值得使用的 Node.js 框架</a></li>
<li><a href="https://juejin.cn/column/6972556324022255624" target="_blank" title="https://juejin.cn/column/6972556324022255624">React 面试必知必会系列</a></li>
<li><a href="https://juejin.cn/column/6962102040684134436" target="_blank" title="https://juejin.cn/column/6962102040684134436">Go 语言教程系列</a></li>
</ul>
<blockquote>
<p>本文首发于「<a href="https://juejin.cn/user/325111174662855" target="_blank" title="https://juejin.cn/user/325111174662855">掘金专栏</a>」，同步于公众号「程序人生」和「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyoungjuning.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://youngjuning.js.org/" ref="nofollow noopener noreferrer">洛竹的官方网站</a>」。</p>
</blockquote></div>  
</div>
            