
---
title: 'React 系统复习如何做最高效（8.24直播总结 + 百道高频面试题整理）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c955f56127649d78517ad87c49bc585~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 21:56:55 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c955f56127649d78517ad87c49bc585~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一 前言</h2>
<p>哈喽，大家好，我是 我不是外星人 👽 ，8月24号，我作为分享嘉宾，线上参与了一场 《React 系统复习如何做最高效》 的技术分享，接下来我把直播的内容汇总分享给大家。在分享的过程中，也枚举了一些思考题和一些比较热门的面试题目，一同奉上。</p>
<p>这里<strong>非常感谢掘金平台提供一次分享技术的机会，也非常感谢掘友们的热心捧场</strong>，整体下来还算是成功的，可能刚开始比较紧张，因为毕竟是第一次直播，人生的第一次直播献给了掘金😂，后来渐渐地找回了状态。这里保存了直播过程中的一些截图，整体下来掘友们还是蛮给力的，也参与互动，提了很多问题。</p>
<p>直播场景：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c955f56127649d78517ad87c49bc585~tplv-k3u1fbpfcp-watermark.image" alt="1.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>掘友互动场景</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fadce32bd9994eda8746957c644824df~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG239.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想看直播回放的童鞋，请点击这里： <a href="https://live.juejin.cn/4354/3168473" target="_blank" title="https://live.juejin.cn/4354/3168473">直播回放</a></p>
<p>好的，废话不说，进入正题，本次直播分享主要按照以下模块进行的，这些模块是我工作几年来总结的一些经验，同学们可以按照对应的模块进行查缺补漏，</p>
<ul>
<li>React 基础模块。</li>
<li>React 优化手段。</li>
<li>React 生态掌握。</li>
<li>React 设计模式。</li>
<li>React 核心原理。</li>
<li>React 项目实战。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bda11176d1594d1786653e44e7b07f09~tplv-k3u1fbpfcp-watermark.image" alt="B549B364-1C38-4A2D-8EFC-B953CFC06F70.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二 知识点梳理</h2>
<p>上述的模块进行细化，总结的内容如下：</p>
<p><strong>React基础模块：</strong></p>
<ul>
<li>操作 <code>jsx</code> 。</li>
<li>掌握 class 和 function Component。</li>
<li>state 更新机制， <code>setState</code> 和 <code>useState</code> 的用法和区别。</li>
<li>理解 <code>props</code> ，React 中的 props 可以是什么？</li>
<li>类组件生命周期，函数组件生命周期替代方案， <code>useEffect</code> 和 <code>useLayoutEffect</code>。</li>
<li><code>Ref</code> 是什么，能做些什么？</li>
<li><code>css in React</code>。</li>
</ul>
<p><strong>React优化手段</strong></p>
<ul>
<li>渲染控制。</li>
<li>渲染调优。</li>
<li>处理海量数据。</li>
<li>细节处理。</li>
</ul>
<p><strong>React生态</strong></p>
<ul>
<li>React-Router。</li>
<li>React-Redux。</li>
<li>React-Mobx。</li>
<li>项目工程 umi | dva等。</li>
</ul>
<p><strong>React设计模式</strong></p>
<ul>
<li>组合模式。</li>
<li>render props 模式。</li>
<li>HOC | 装饰器模式。</li>
<li>提供者模式。</li>
<li>自定义 hooks 模式。</li>
</ul>
<p><strong>React核心原理</strong></p>
<ul>
<li>事件原理。</li>
<li>调和原理。</li>
<li>调度原理。</li>
<li>hooks 原理。</li>
<li>diff 流程等等。</li>
</ul>
<p><strong>React实战</strong></p>
<ul>
<li>实现表单系统。</li>
<li>实现状态管理工具。</li>
<li>实现路由功能。</li>
<li>自定义 hooks 实践。</li>
</ul>
<p>以上就是本次直播的提及的 React 应该学习的知识点。用一幅图来概括。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/546f231bb6c948f9ba382f9fcef43ba5~tplv-k3u1fbpfcp-watermark.image" alt="47A69B6D-65A9-4646-8951-D347C6DD739B.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来对每一个功能进行拆解。</p>
<h2 data-id="heading-2">三 功能拆解</h2>
<p>分享的内容细化成每一个我们需要掌握的功能点，以问题的形式切入，我们可以尝试一下？</p>
<h3 data-id="heading-3">1 React基础模块</h3>
<h4 data-id="heading-4">基础模块 jsx</h4>
<p>jsx 中总结的知识点：</p>
<ul>
<li>① 我们写的 jsx 语法最后变成了什么？ React JSX -> React element -> React fiber 流程。</li>
<li>② 如何理解 React element?</li>
<li>③ 老版本 React 为什么要引入 React，如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Index</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>let us learn React!<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>④ 如何操作 React Element ，使其变成可控的？ react createElement 和 react cloneElement。</p>
</li>
<li>
<p>⑤ <code>createElement</code> 和 <code>cloneElement</code> 区别。</p>
</li>
<li>
<p>⑥ React children 操作方法和应用场景？ map ，forEach ，count ，toArray ，only。</p>
</li>
<li>
<p>⑦ jsx 拓展尝鲜例子：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Test</span>(<span class="hljs-params">num</span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(num)
   useEffect(<span class="hljs-function">()=></span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1111'</span>)
   &#125;,[])
   <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>《React 进阶实践指南》<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Index</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ isShow , setIsShow  ]= useState(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setIsShow(!isShow)&#125; >点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
           &#123;isShow ? <span class="hljs-tag"><<span class="hljs-name">Test</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;1&#125;</span> /></span> : <span class="hljs-tag"><<span class="hljs-name">Test</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;2&#125;</span> /></span>&#125;
         <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上点击按钮 <code>button</code>，<code>useEffect</code> 中的 <code>console.log('1111')</code> 是否打印。</p>
<p><strong>错误分析：</strong> 点击按钮，切换 <code>isShow</code>，控制两个 Test 组件的挂载 ｜ 卸载，因为组件重复挂载，那么 <code>useEffect</code> 执行，打印 <code>console.log('1111') </code>，但是实际结果是这样吗？</p>
<p><strong>效果：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd38feef04a94078aed23148f5030f3c~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>流程分析：</strong> 为什么 useEffect 中的 console.log 没有打印呢 ？</p>
<ul>
<li>首先如果我们明白 jsx -> element -> fiber 流程之后，就不难解释这个现象了，写的两个 Test 组件，本质上被 babel 处理成两个 element 对象，<code>element</code> 对象中的 type 属性都指向了 Test 组件函数，两个 element 对象唯一区别是 props 不同。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/952d4b5287bb4b0ebafbf614389e3300~tplv-k3u1fbpfcp-watermark.image" alt="4DC0372C-EDDD-4889-990A-22A96090BA21.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>那么在 React 调和阶段 React ，判断 type 指向相同，就会判断它们是一个组件，所以一次更新的只是被判定 props 变化，走的更新逻辑。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9965e76324b74999bdd8a44c5f139cbd~tplv-k3u1fbpfcp-watermark.image" alt="E7B2C227-23FB-4403-AAE4-6E61142554C9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>然后在 Test 函数中，更新组件不会让依赖项为 <code>[]</code> 的 <code>useEffect</code>再次执行，所以 <code>console.log('1111')</code> 不会被打印。</li>
</ul>
<p><strong>解决问题：</strong></p>
<p>如果想要组件挂载 ｜ 卸载效果，那么很简单，给其中的 Test 加入一个 key，就可以解决问题，<code>key</code> 可以作为组件身份的标示，在下一次更新中，就会根据 key 找到复用的 fiber 节点，如果没有找到，那就会走正常的组件挂载 ｜ 卸载流程了。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"> &#123;isShow ? <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Test</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;1&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;1&#125;</span>  /></span></span> : <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Test</span> <span class="hljs-attr">num</span>=<span class="hljs-string">&#123;2&#125;</span> /></span></span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">基础模块 state</h4>
<p>state 中总结的知识点：</p>
<ul>
<li>① state 更新机制? state 改变到视图更新的流程。</li>
<li>② state 批量更新的规则，为什么会被打破？</li>
<li>③ setState 是同步还是异步的？</li>
<li>④ 类组件的 <code>setState</code> 和函数组件的 <code>useState</code> 有什么共性和区别？</li>
<li>⑤ 函数组件的状态管理方法 useState + useRef ?  useState 负责更新，useRef 负责保存状态。</li>
<li>⑥ state 打印问题：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">handleClick=<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">1</span>  &#125;)
    &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">2</span>  &#125;)
    ReactDOM.flushSync(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">3</span>  &#125;)
    &#125;)
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">number</span>: <span class="hljs-number">4</span>  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.number)
   <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.handleClick</span> &#125; ></span> 点击 <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮，打印顺序 ？</p>
<p>打印 3 4 1 ，相信不难理解为什么这么打印了。</p>
<p>首先 <code>flushSync</code> <code>this.setState(&#123; number: 3 &#125;)</code> 设定了一个高优先级的更新，所以 2 和 3 被批量更新到 3 ，所以 3 先被打印。
更新为 4。
最后更新 setTimeout 中的 number = 1。</p>
<h4 data-id="heading-6">基础模块 component</h4>
<p>component 模块包含的知识点：</p>
<ul>
<li>① 类组件特点，函数组件特点，两者有什么区别？</li>
<li>② 组件的通信方式？</li>
<li>③ 组件的强化方式？</li>
<li>④ React 对组件的处理和处理时机？</li>
<li>⑤ 公共组件的设计规范？</li>
</ul>
<h4 data-id="heading-7">基础模块生命周期</h4>
<p>生命周期知识点：</p>
<ul>
<li>① 生命周期的介绍，和用法？</li>
<li>② 生命周期的执行时机？ 父与子生命周期的执行顺序？</li>
<li>③ 函数组件生命周期的代替方案？</li>
<li>④ useEffect 和 useLayoutEffect 有什么区别，应用场景？</li>
<li>⑤ 废弃的生命周期，为什么要废弃？</li>
</ul>
<p>一幅图表示 <strong>函数组件</strong> 和 <strong>类组件</strong> 所有生命周期的执行时机（包括已经废弃的生命周期）：</p>
<h4 data-id="heading-8">基础模块 Ref</h4>
<p>ref 知识点总结：</p>
<ul>
<li>① Ref 对象，以及两种 ref 对象创建方法。 useRef 和 createRef</li>
<li>② Ref 有什么作用？ 1 获取组件实例，DOM元素 ； 2 组件通信 ； 3 保存状态；</li>
<li>③ Ref 原理 ？ <code>commitAttachRef</code> 和 <code>commitDetachRef</code>。</li>
<li>④ Ref 获取的三种方式？ function ； Ref 对象 ； String ；</li>
<li>⑤ 如何跨层级传递 ref ?</li>
<li>⑥ 父组件如何获取函数子组件内部状态？</li>
</ul>
<h4 data-id="heading-9">基础模块 Css in React</h4>
<p>css 模块总结：</p>
<ul>
<li>① React css 模块化方案。</li>
<li>② css module 掌握。</li>
<li>③ css in js 掌握。</li>
</ul>
<h3 data-id="heading-10">2 React 优化手段</h3>
<p>React 优化手段总结：</p>
<ul>
<li>① React 渲染控制的方法？。 缓存 react element ，pureComponent ，Memo ，shouldComponentUpdate</li>
<li>② shallowEqual 浅比较原理。</li>
<li>③ React 中节流防抖运用。</li>
<li>④ 合理运用状态管理。</li>
<li>⑤ 按需引入。减少项目体积。</li>
<li>⑥ 代码分割 lazy ，异步组件 Suspense 及其原理。</li>
<li>⑦ diff 算法，合理应用 key 。</li>
<li>⑧ 渲染错误边界，<code>componentDidCatch</code>。</li>
<li>⑨ 状态管理工具和 immutable.js 使用。</li>
<li>⑩ useMemo 缓存逻辑。</li>
<li>⑪ memo 的缓存策略。</li>
</ul>
<h3 data-id="heading-11">3 React 生态</h3>
<p>React 生态总结： react-router，react-redux ，react-mobx umi dva 等。</p>
<ul>
<li>① 两种路由模式 ｜ spa 单页面路由原理。</li>
<li>② React router 使用，实现动态路由，自定义路由。</li>
<li>③ Route. Router Switch 分工。</li>
<li>④ 权限路由封装。</li>
<li>⑤ Mobx-react 使用。</li>
<li>⑥ Mobx 和 React Redux 区别？</li>
<li>⑦ Mobx 原理，收集依赖，触发更新。</li>
<li>⑧ React Redux 和 Redux 使用。</li>
<li>⑨ Redux 设计模式 ｜ 中间件原理。</li>
<li>⑩ React Redux  原理？</li>
<li>⑪ react redux 衍生： dva React-saga 等</li>
<li>⑫ React Redux 中 connect 原理 （这里推荐大家看一下源码，学习一下 hooks使用）。</li>
</ul>
<h3 data-id="heading-12">4 React 设计模式</h3>
<p>React 设计模式总结：</p>
<ul>
<li>① React 几种设计模式总结。组合模式，render props模式，提供者模式， hoc 模式，自定义hooks 模式。</li>
<li>② 新老版本 context 用法特点。</li>
<li>③ React context 特点。逐层传递，发布订阅。</li>
<li>④ 新版本 context 消费者几种方式。contextType ，useContext ，consumer</li>
<li>⑤ hoc 两种方式，优缺点？属性代理，反向继承。</li>
<li>⑥ hoc 如何解决静态属性继承问题。</li>
<li>⑦ hoc 如何解决 ref 获取问题。</li>
<li>⑧ hoc 注意事项。</li>
<li>⑨ 自定义 hooks 设计。</li>
<li>⑩ 自定义 hooks 实践。</li>
</ul>
<p>以下是一些经典设计模式的代码片段（供大家参考）：</p>
<p><strong>组合模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><Form ref=&#123; form &#125; >
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">FormItem</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"我是"</span>  ></span>
        <span class="hljs-tag"><<span class="hljs-name">Input</span>   /></span>
    <span class="hljs-tag"></<span class="hljs-name">FormItem</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">FormItem</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"mes"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"我想对大家说"</span>  ></span>
        <span class="hljs-tag"><<span class="hljs-name">Input</span>   /></span>
    <span class="hljs-tag"></<span class="hljs-name">FormItem</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span>  <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"不需要的input"</span> /></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Input</span>/></span></span>
</Form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>提供者模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ConsumerDemo</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-keyword">const</span> &#123; color,background &#125; = React.useContext(ThemeContext)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color</span>,<span class="hljs-attr">background</span> &#125; &#125; ></span>消费者<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 
&#125;
<span class="hljs-keyword">const</span> Son = React.memo(<span class="hljs-function">()=></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ConsumerDemo</span> /></span></span>) <span class="hljs-comment">// 子组件</span>

<span class="hljs-keyword">const</span> ThemeProvider = ThemeContext.Provider <span class="hljs-comment">//提供者</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ProviderDemo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [ contextValue , setContextValue ] = React.useState(&#123;  <span class="hljs-attr">color</span>:<span class="hljs-string">'#ccc'</span>, <span class="hljs-attr">background</span>:<span class="hljs-string">'pink'</span> &#125;)
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ThemeProvider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">contextValue</span> &#125; ></span>
            <span class="hljs-tag"><<span class="hljs-name">Son</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">ThemeProvider</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;</span> ()=></span> setContextValue(&#123; color:'#fff' , background:'blue' &#125;)  &#125; >切换主题<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>render props模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> Index = <span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Container</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Children</span> /></span>
        &#123; (ContainerProps)=> <span class="hljs-tag"><<span class="hljs-name">Children</span> &#123;<span class="hljs-attr">...ContainerProps</span>&#125; <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;</span>'<span class="hljs-attr">haha</span>'&#125;  /></span>  &#125;
    <span class="hljs-tag"></<span class="hljs-name">Container</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>hoc模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js">@HOC1(styles)
@HOC2
@HOC3
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Componen</span></span>&#123;
    <span class="hljs-comment">/* ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>自定义hooks模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useXXX</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> value = React.useContext(defaultContext)
    <span class="hljs-comment">/* .....用上下文中 value 一段初始化逻辑  */</span>
    <span class="hljs-keyword">const</span> newValue = initValueFunction(value) <span class="hljs-comment">/* 初始化 value 得到新的 newValue  */</span>
    <span class="hljs-comment">/* ...... */</span>
    <span class="hljs-keyword">return</span> newValue
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5 React 核心原理</h3>
<p>React 核心原理总结：</p>
<p><strong>fiber原理</strong></p>
<ul>
<li>① 什么是fiber ? Fiber 架构解决了什么问题？</li>
<li>② Fiber root 和 root fiber 有什么区别？</li>
<li>③ 不同fiber 之间如何建立起关联的？</li>
<li>④ React 调和流程？</li>
<li>⑤ 两大阶段 commit 和 render 都做了哪些事情？</li>
<li>⑥ 什么是双缓冲树？ 有什么作用？</li>
<li>⑦ Fiber 深度遍历流程？</li>
<li>⑧ Fiber的调和能中断吗？ 如何中断？</li>
</ul>
<p><strong>调度原理</strong></p>
<ul>
<li>① 异步调度原理？</li>
<li>② React 为什么不用 settimeout ？</li>
<li>③ 说一说React 的时间分片？</li>
<li>④ React 如何模拟 requestIdleCallback？</li>
<li>⑤ 简述一下调度流程？</li>
</ul>
<p><strong>hooks原理</strong></p>
<ul>
<li>① React Hooks 为什么必须在函数组件内部执行？React 如何能够监听 React Hooks 在外部执行并抛出异常。</li>
<li>② React Hooks 如何把状态保存起来？保存的信息存在了哪里？</li>
<li>③ React Hooks 为什么不能写在条件语句中？</li>
<li>④ useMemo 内部引用 useRef 为什么不需要添加依赖项，而 useState 就要添加依赖项。</li>
<li>⑤ useEffect 添加依赖项 props.a ，为什么 props.a 改变，useEffect 回调函数 create 重新执行。</li>
<li>⑥ React 内部如何区别 useEffect 和 useLayoutEffect ，执行时机有什么不同？</li>
</ul>
<p><strong>事件原理</strong></p>
<ul>
<li>① React 为什么有自己的事件系统？</li>
<li>② 什么是事件合成 ？</li>
<li>③ 如何实现的批量更新？</li>
<li>④ 事件系统如何模拟冒泡和捕获阶段？</li>
<li>⑤ 如何通过 dom 元素找到与之匹配的fiber？</li>
<li>⑥ 为什么不能用 return false 来阻止事件的默认行为？</li>
<li>⑦ 事件是绑定在真实的dom上吗？如何不是绑定在哪里？</li>
<li>⑧ V17 对事件系统有哪些改变</li>
</ul>
<h3 data-id="heading-14">6 React 实践</h3>
<p>实践是检验真理的唯一标准，如果想要进阶 React ，在理论知识基础上，也需要去尝试敲代码。</p>
<ul>
<li>如过没有做过React 项目，尝试写一个 demo 。</li>
<li>尝试写一个公共组件。</li>
<li>尝试写一个高阶组件。</li>
<li>尝试写一个自定义 hooks。</li>
<li>尝试在项目中使用多种设计模式。</li>
</ul>
<h3 data-id="heading-15">7 React 学习的几个重要阶段</h3>
<p>进阶 React 可以按照以下阶段去进阶。</p>
<ul>
<li>
<p>第一阶段：明白基础 api ,尝试写项目，多尝试一些复杂的逻辑场景。会用一些React生态。</p>
</li>
<li>
<p>第二阶段：尝试封装一些基础组件，hoc，尝试使用一些设计模式。</p>
</li>
<li>
<p>第三阶段：学习一些原理，可以尝试看一下核心源码。</p>
</li>
<li>
<p>第四阶段：可以自己根据业务需求写一些库，考虑开源。</p>
</li>
</ul>
<h2 data-id="heading-16">四 总结</h2>
<p>以上就是本次直播分享 React 系统学习部分的内容，大家可以根据自己对 React 的掌握程度，进行查缺补漏，最后祝愿大家早日进阶 React 技术栈。</p>
<h2 data-id="heading-17">《React进阶实践指南小册》</h2>
<p>本次分享的知识点，在这本小册中都能找到答案。
目前小册已经完结，是终点亦是起点,  小册内容将持续更新，随着 React 版本升级持续维护，并有持续更新章节～
提前透露，小册接下来会补充：<code>React context</code> 原理部分，内容补充到第八章。
奉上几个小册 7 折 优惠码  <strong>F3Z1VXtv</strong> ，先到先得～</p>
<p>感兴趣的同学可以关注笔者公众号 ： <strong>前端Sharing</strong> 持续分享前端硬文。</p></div>  
</div>
            