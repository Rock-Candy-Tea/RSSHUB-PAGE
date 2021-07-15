
---
title: 'Vue - The Good Parts_ transition'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1299ba4794ca4adaa093fad591f110df~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 19:34:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1299ba4794ca4adaa093fad591f110df~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>随着大家对于交互更高的要求，在很多场景下我们的交互设计是都会要求在页面中适当的加入一些动画来增强用户的感知，或者有一些过渡效果来提升连贯性。</p>
<p>在 Vue 中提供了十分友好、极其好用的过渡组件，可以帮助我们很容易的实现过渡动画需求。So easy!</p>
<p>那里边是如何实现的，有哪些是很值得我们学习的？</p>
<h2 data-id="heading-1">正文分析</h2>
<h3 data-id="heading-2">What</h3>
<p>Vue 中 transition 相关的有两个组件：单个过渡的 transition 组件以及列表过渡 transition-group 组件。</p>
<p>和过渡相关的工具大概：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1299ba4794ca4adaa093fad591f110df~tplv-k3u1fbpfcp-watermark.image" alt="image2021-7-6_15-27-24.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>功能还是很多，开发者完全可以根据自己的场景来决定使用什么样的工具去完成需要的过渡动效。</p>
<p>典型的场景：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd9b08882bd748e7b9d621b83dd9326b~tplv-k3u1fbpfcp-watermark.image" alt="image2021-7-6_15-33-3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当点击 Toggle 的时候，下放的 hello 文本就会有一个透明度的过渡动效。</p>
<p>整个过渡的过程可以详细的描述为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c411074d825e459181bc7d6a204efe13~tplv-k3u1fbpfcp-watermark.image" alt="transition (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有列表过渡的示例：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b28230ca895c43e594cba8985ca75f15~tplv-k3u1fbpfcp-watermark.image" alt="image2021-7-6_15-38-44.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击 Shuffle 按钮，会打散数的排列，即对 items 进行洗牌，会出现神奇的动画过渡效果。</p>
<p>这些就是 Vue 中 transition 和 transition-group 组件提供的强大能力。</p>
<h3 data-id="heading-3">How</h3>
<p>那如此神奇的组件到底是怎么实现的呢？我们一起来看下。</p>
<h4 data-id="heading-4">transition</h4>
<p>先来看 transition，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fv2.6.14%2Fsrc%2Fplatforms%2Fweb%2Fruntime%2Fcomponents%2Ftransition.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/v2.6.14/src/platforms/web/runtime/components/transition.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// props 定义</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> transitionProps = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">appear</span>: <span class="hljs-built_in">Boolean</span>,
  <span class="hljs-attr">css</span>: <span class="hljs-built_in">Boolean</span>,
  <span class="hljs-attr">mode</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">enterClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">leaveClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">enterToClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">leaveToClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">enterActiveClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">leaveActiveClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">appearClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">appearActiveClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">appearToClass</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">duration</span>: [<span class="hljs-built_in">Number</span>, <span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>]
&#125;
 
<span class="hljs-comment">// in case the child is also an abstract component, e.g. <keep-alive></span>
<span class="hljs-comment">// we want to recursively retrieve the real component to be rendered</span>
<span class="hljs-comment">// 得到真实的 child，抛掉 abstract 的</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRealChild</span> (<span class="hljs-params">vnode: ?VNode</span>): ?<span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> compOptions: ?VNodeComponentOptions = vnode && vnode.componentOptions
  <span class="hljs-keyword">if</span> (compOptions && compOptions.Ctor.options.abstract) &#123;
    <span class="hljs-keyword">return</span> getRealChild(getFirstComponentChild(compOptions.children))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> vnode
  &#125;
&#125;
 
<span class="hljs-comment">// 提取 transition 需要的数据 data，包括了 props 和 events</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">extractTransitionData</span> (<span class="hljs-params">comp: Component</span>): <span class="hljs-title">Object</span> </span>&#123;
  <span class="hljs-keyword">const</span> data = &#123;&#125;
  <span class="hljs-keyword">const</span> options: ComponentOptions = comp.$options
  <span class="hljs-comment">// props</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> options.propsData) &#123;
    data[key] = comp[key]
  &#125;
  <span class="hljs-comment">// events.</span>
  <span class="hljs-comment">// extract listeners and pass them directly to the transition methods</span>
  <span class="hljs-keyword">const</span> listeners: ?<span class="hljs-built_in">Object</span> = options._parentListeners
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> listeners) &#123;
    data[camelize(key)] = listeners[key]
  &#125;
  <span class="hljs-keyword">return</span> data
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">placeholder</span> (<span class="hljs-params">h: <span class="hljs-built_in">Function</span>, rawChild: VNode</span>): ?<span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/\d-keep-alive$/</span>.test(rawChild.tag)) &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'keep-alive'</span>, &#123;
      <span class="hljs-attr">props</span>: rawChild.componentOptions.propsData
    &#125;)
  &#125;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasParentTransition</span> (<span class="hljs-params">vnode: VNode</span>): ?<span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-comment">// 一直查找 vnode 的parent 直至没有，只要有一层出现了 transition 则代表父级有 transition</span>
  <span class="hljs-keyword">while</span> ((vnode = vnode.parent)) &#123;
    <span class="hljs-keyword">if</span> (vnode.data.transition) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isSameChild</span> (<span class="hljs-params">child: VNode, oldChild: VNode</span>): <span class="hljs-title">boolean</span> </span>&#123;
  <span class="hljs-keyword">return</span> oldChild.key === child.key && oldChild.tag === child.tag
&#125;
 
<span class="hljs-keyword">const</span> isNotTextNode = <span class="hljs-function">(<span class="hljs-params">c: VNode</span>) =></span> c.tag || isAsyncPlaceholder(c)
 
<span class="hljs-keyword">const</span> isVShowDirective = <span class="hljs-function"><span class="hljs-params">d</span> =></span> d.name === <span class="hljs-string">'show'</span>
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'transition'</span>,
  <span class="hljs-attr">props</span>: transitionProps,
  <span class="hljs-comment">// 抽象组件</span>
  <span class="hljs-attr">abstract</span>: <span class="hljs-literal">true</span>,
 
  render (h: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">let</span> children: any = <span class="hljs-built_in">this</span>.$slots.default
    <span class="hljs-keyword">if</span> (!children) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
 
    <span class="hljs-comment">// filter out text nodes (possible whitespaces)</span>
    children = children.filter(isNotTextNode)
    <span class="hljs-comment">/* istanbul ignore if */</span>
    <span class="hljs-keyword">if</span> (!children.length) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
 
    <span class="hljs-comment">// warn multiple elements</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && children.length > <span class="hljs-number">1</span>) &#123;
      warn(
        <span class="hljs-string">'<transition> can only be used on a single element. Use '</span> +
        <span class="hljs-string">'<transition-group> for lists.'</span>,
        <span class="hljs-built_in">this</span>.$parent
      )
    &#125;
 
    <span class="hljs-keyword">const</span> mode: string = <span class="hljs-built_in">this</span>.mode
 
    <span class="hljs-comment">// warn invalid mode</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> &&
      mode && mode !== <span class="hljs-string">'in-out'</span> && mode !== <span class="hljs-string">'out-in'</span>
    ) &#123;
      warn(
        <span class="hljs-string">'invalid <transition> mode: '</span> + mode,
        <span class="hljs-built_in">this</span>.$parent
      )
    &#125;
 
    <span class="hljs-keyword">const</span> rawChild: VNode = children[<span class="hljs-number">0</span>]
 
    <span class="hljs-comment">// if this is a component root node and the component's</span>
    <span class="hljs-comment">// parent container node also has transition, skip.</span>
    <span class="hljs-comment">// 注意这里用的是 $vnode</span>
    <span class="hljs-keyword">if</span> (hasParentTransition(<span class="hljs-built_in">this</span>.$vnode)) &#123;
      <span class="hljs-keyword">return</span> rawChild
    &#125;
 
    <span class="hljs-comment">// apply transition data to child</span>
    <span class="hljs-comment">// use getRealChild() to ignore abstract components e.g. keep-alive</span>
    <span class="hljs-keyword">const</span> child: ?VNode = getRealChild(rawChild)
    <span class="hljs-comment">/* istanbul ignore if */</span>
    <span class="hljs-keyword">if</span> (!child) &#123;
      <span class="hljs-keyword">return</span> rawChild
    &#125;
 
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._leaving) &#123;
      <span class="hljs-keyword">return</span> placeholder(h, rawChild)
    &#125;
 
    <span class="hljs-comment">// ensure a key that is unique to the vnode type and to this transition</span>
    <span class="hljs-comment">// component instance. This key will be used to remove pending leaving nodes</span>
    <span class="hljs-comment">// during entering.</span>
    <span class="hljs-keyword">const</span> id: string = <span class="hljs-string">`__transition-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>._uid&#125;</span>-`</span>
    child.key = child.key == <span class="hljs-literal">null</span>
      ? child.isComment
        ? id + <span class="hljs-string">'comment'</span>
        : id + child.tag
      : isPrimitive(child.key)
        ? (<span class="hljs-built_in">String</span>(child.key).indexOf(id) === <span class="hljs-number">0</span> ? child.key : id + child.key)
        : child.key
 
    <span class="hljs-keyword">const</span> data: <span class="hljs-built_in">Object</span> = (child.data || (child.data = &#123;&#125;)).transition = extractTransitionData(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// 这里用的是 _vnode</span>
    <span class="hljs-keyword">const</span> oldRawChild: VNode = <span class="hljs-built_in">this</span>._vnode
    <span class="hljs-keyword">const</span> oldChild: VNode = getRealChild(oldRawChild)
 
    <span class="hljs-comment">// mark v-show</span>
    <span class="hljs-comment">// so that the transition module can hand over the control to the directive</span>
    <span class="hljs-keyword">if</span> (child.data.directives && child.data.directives.some(isVShowDirective)) &#123;
      child.data.show = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-comment">// 判断 oldChild 以及 oldChild 和 新的是不是相同的</span>
    <span class="hljs-comment">// 正常情况下，单个元素的情况下，是不会进入的，因为 如果是从隐藏到显示，old就是comment 如果是从显示到隐藏 child 就没有</span>
    <span class="hljs-keyword">if</span> (
      oldChild &&
      oldChild.data &&
      !isSameChild(child, oldChild) &&
      !isAsyncPlaceholder(oldChild) &&
      <span class="hljs-comment">// #6687 component root is a comment node</span>
      !(oldChild.componentInstance && oldChild.componentInstance._vnode.isComment)
    ) &#123;
      <span class="hljs-comment">// replace old child transition data with fresh one</span>
      <span class="hljs-comment">// important for dynamic transitions!</span>
      <span class="hljs-comment">// 更新 vnode data transition 值</span>
      <span class="hljs-keyword">const</span> oldData: <span class="hljs-built_in">Object</span> = oldChild.data.transition = extend(&#123;&#125;, data)
      <span class="hljs-comment">// handle transition mode</span>
      <span class="hljs-comment">// 多个元素，当前元素和新元素之间的动画过渡模式 两个 mode</span>
      <span class="hljs-comment">// 模式 out-in：当前元素先进行过渡，完成之后新元素过渡进入。</span>
      <span class="hljs-keyword">if</span> (mode === <span class="hljs-string">'out-in'</span>) &#123;
        <span class="hljs-comment">// return placeholder node and queue update when leave finishes</span>
        <span class="hljs-comment">// 标记 _leaving，等待</span>
        <span class="hljs-built_in">this</span>._leaving = <span class="hljs-literal">true</span>
        <span class="hljs-comment">// 监控 afterLeave</span>
        mergeVNodeHook(oldData, <span class="hljs-string">'afterLeave'</span>, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// reset & 更新</span>
          <span class="hljs-built_in">this</span>._leaving = <span class="hljs-literal">false</span>
          <span class="hljs-comment">// 此时已经 out 完毕，执行 forceUpdate 走 show 然后 in 的逻辑了</span>
          <span class="hljs-built_in">this</span>.$forceUpdate()
        &#125;)
        <span class="hljs-comment">// 考虑 keep-alive 场景，一般就会返回 undefined 了，也就是会触发 patch 然后把元素 remove 掉，即 out 逻辑</span>
        <span class="hljs-keyword">return</span> placeholder(h, rawChild)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (mode === <span class="hljs-string">'in-out'</span>) &#123;
        <span class="hljs-comment">// 模式 in-out：新元素先进行过渡，完成之后当前元素过渡离开。</span>
        <span class="hljs-keyword">if</span> (isAsyncPlaceholder(child)) &#123;
          <span class="hljs-comment">// 异步 先返回旧的</span>
          <span class="hljs-keyword">return</span> oldRawChild
        &#125;
        <span class="hljs-keyword">let</span> delayedLeave
        <span class="hljs-keyword">const</span> performLeave = <span class="hljs-function">() =></span> &#123; delayedLeave() &#125;
        <span class="hljs-comment">// 监听 afterEnter 钩子 执行之前保留下来的 leave 回调逻辑</span>
        <span class="hljs-comment">// 这样实现了先 in 后 out 的效果，因为是等到 afterEnter 之后才走的 leave 逻辑</span>
        mergeVNodeHook(data, <span class="hljs-string">'afterEnter'</span>, performLeave)
        mergeVNodeHook(data, <span class="hljs-string">'enterCancelled'</span>, performLeave)
        <span class="hljs-comment">// 回调设置，把 leave 执行的执行逻辑保留下来</span>
        mergeVNodeHook(oldData, <span class="hljs-string">'delayLeave'</span>, <span class="hljs-function"><span class="hljs-params">leave</span> =></span> &#123; delayedLeave = leave &#125;)
      &#125;
    &#125;
 
    <span class="hljs-keyword">return</span> rawChild
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出单纯从组件定义上讲，组件的 render() 主要做了这几件事：</p>
<ul>
<li>得到真实 children，得到第一个 child，因为只允许有一个 child 所以这里取第一个即可</li>
<li>设置 id 和 key，确保唯一</li>
<li>如果多个元素，根据 mode，决定监听不同的 hook 进行处理</li>
</ul>
<p>但是，从这些我们是不能够理解咋执行的，那是因为还缺少一部分核心的逻辑，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fv2.6.14%2Fsrc%2Fplatforms%2Fweb%2Fruntime%2Fmodules%2Ftransition.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/v2.6.14/src/platforms/web/runtime/modules/transition.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a> 中实现的：</p>
<p>PS：需要依赖我们在Vue - The Good Parts: 组件中讲述的 modules 知识，也就是在 patch 的过程中，会调用各个 module 的各个钩子 'create', 'activate', 'update', 'remove', 'destroy'，对应的就是 vnode 本身的一些更新。这里最核心的就是利用了 create 和 remove 钩子。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_enter</span> (<span class="hljs-params">_: any, vnode: VNodeWithData</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (vnode.data.show !== <span class="hljs-literal">true</span>) &#123;
    enter(vnode)
  &#125;
&#125;
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> inBrowser ? &#123;
  <span class="hljs-attr">create</span>: _enter,
  <span class="hljs-attr">activate</span>: _enter,
  remove (vnode: VNode, <span class="hljs-attr">rm</span>: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (vnode.data.show !== <span class="hljs-literal">true</span>) &#123;
      leave(vnode, rm)
    &#125; <span class="hljs-keyword">else</span> &#123;
      rm()
    &#125;
  &#125;
&#125; : &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来看下 enter 的逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enter</span> (<span class="hljs-params">vnode: VNodeWithData, toggleDisplay: ?() => <span class="hljs-keyword">void</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> el: any = vnode.elm
 
  <span class="hljs-comment">// call leave callback now</span>
  <span class="hljs-comment">// 如果 还没等到 leave 就又更新了 那么直接结束上次的 leave 相当于取消了 leave</span>
  <span class="hljs-keyword">if</span> (isDef(el._leaveCb)) &#123;
    el._leaveCb.cancelled = <span class="hljs-literal">true</span>
    el._leaveCb()
  &#125;
 
  <span class="hljs-keyword">const</span> data = resolveTransition(vnode.data.transition)
  <span class="hljs-keyword">if</span> (isUndef(data)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
 
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (isDef(el._enterCb) || el.nodeType !== <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 从 transition data 中直接获取配置的一些 props 以及绑定的事件们</span>
  <span class="hljs-keyword">const</span> &#123;
    css,
    type,
    enterClass,
    enterToClass,
    enterActiveClass,
    appearClass,
    appearToClass,
    appearActiveClass,
    beforeEnter,
    enter,
    afterEnter,
    enterCancelled,
    beforeAppear,
    appear,
    afterAppear,
    appearCancelled,
    duration
  &#125; = data
 
  <span class="hljs-comment">// activeInstance will always be the <transition> component managing this</span>
  <span class="hljs-comment">// transition. One edge case to check is when the <transition> is placed</span>
  <span class="hljs-comment">// as the root node of a child component. In that case we need to check</span>
  <span class="hljs-comment">// <transition>'s parent for appear check.</span>
  <span class="hljs-comment">// context 就是当前的 transition 组件实例</span>
  <span class="hljs-keyword">let</span> context = activeInstance
  <span class="hljs-keyword">let</span> transitionNode = activeInstance.$vnode
  <span class="hljs-keyword">while</span> (transitionNode && transitionNode.parent) &#123;
    context = transitionNode.context
    transitionNode = transitionNode.parent
  &#125;
  <span class="hljs-comment">// 是否可见了已经</span>
  <span class="hljs-keyword">const</span> isAppear = !context._isMounted || !vnode.isRootInsert
  <span class="hljs-comment">// 当然这里依旧可以通过 appear prop 属性来强制改变状态</span>
  <span class="hljs-keyword">if</span> (isAppear && !appear && appear !== <span class="hljs-string">''</span>) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 对 class 名字的一对处理</span>
  <span class="hljs-keyword">const</span> startClass = isAppear && appearClass
    ? appearClass
    : enterClass
  <span class="hljs-keyword">const</span> activeClass = isAppear && appearActiveClass
    ? appearActiveClass
    : enterActiveClass
  <span class="hljs-keyword">const</span> toClass = isAppear && appearToClass
    ? appearToClass
    : enterToClass
 
  <span class="hljs-comment">// hook 各种处理</span>
  <span class="hljs-keyword">const</span> beforeEnterHook = isAppear
    ? (beforeAppear || beforeEnter)
    : beforeEnter
  <span class="hljs-keyword">const</span> enterHook = isAppear
    ? (<span class="hljs-keyword">typeof</span> appear === <span class="hljs-string">'function'</span> ? appear : enter)
    : enter
  <span class="hljs-keyword">const</span> afterEnterHook = isAppear
    ? (afterAppear || afterEnter)
    : afterEnter
  <span class="hljs-keyword">const</span> enterCancelledHook = isAppear
    ? (appearCancelled || enterCancelled)
    : enterCancelled
 
  <span class="hljs-keyword">const</span> explicitEnterDuration: any = toNumber(
    isObject(duration)
      ? duration.enter
      : duration
  )
 
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && explicitEnterDuration != <span class="hljs-literal">null</span>) &#123;
    checkDuration(explicitEnterDuration, <span class="hljs-string">'enter'</span>, vnode)
  &#125;
 
  <span class="hljs-keyword">const</span> expectsCSS = css !== <span class="hljs-literal">false</span> && !isIE9
  <span class="hljs-keyword">const</span> userWantsControl = getHookArgumentsLength(enterHook)
  <span class="hljs-comment">// enter 回调，once 确保执行一次</span>
  <span class="hljs-keyword">const</span> cb = el._enterCb = once(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (expectsCSS) &#123;
      removeTransitionClass(el, toClass)
      removeTransitionClass(el, activeClass)
    &#125;
    <span class="hljs-comment">// 同样会存在 cancel 情况</span>
    <span class="hljs-keyword">if</span> (cb.cancelled) &#123;
      <span class="hljs-keyword">if</span> (expectsCSS) &#123;
        removeTransitionClass(el, startClass)
      &#125;
      enterCancelledHook && enterCancelledHook(el)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 调用 afterEnter 的 hook</span>
      afterEnterHook && afterEnterHook(el)
    &#125;
    el._enterCb = <span class="hljs-literal">null</span>
  &#125;)
 
  <span class="hljs-keyword">if</span> (!vnode.data.show) &#123;
    <span class="hljs-comment">// remove pending leave element on enter by injecting an insert hook</span>
    mergeVNodeHook(vnode, <span class="hljs-string">'insert'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> parent = el.parentNode
      <span class="hljs-comment">// 动画过程中的当前元素，如果被插入了，那么应该直接结束之前的 leave 动画</span>
      <span class="hljs-comment">// 数据是挂载到 父元素的 _pending 属性 prop 上的</span>
      <span class="hljs-keyword">const</span> pendingNode = parent && parent._pending && parent._pending[vnode.key]
      <span class="hljs-keyword">if</span> (pendingNode &&
        pendingNode.tag === vnode.tag &&
        pendingNode.elm._leaveCb
      ) &#123;
        pendingNode.elm._leaveCb()
      &#125;
      <span class="hljs-comment">// 调用 enter 的钩子</span>
      enterHook && enterHook(el, cb)
    &#125;)
  &#125;
 
  <span class="hljs-comment">// start enter transition</span>
  <span class="hljs-comment">// 调用 beforeEnter 钩子</span>
  beforeEnterHook && beforeEnterHook(el)
  <span class="hljs-keyword">if</span> (expectsCSS) &#123;
    <span class="hljs-comment">// 增加 css 过渡的 class</span>
    addTransitionClass(el, startClass)
    addTransitionClass(el, activeClass)
    <span class="hljs-comment">// 下一帧即 requestAnimationFrame 简称 raf</span>
    nextFrame(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 移除掉 startClass</span>
      removeTransitionClass(el, startClass)
      <span class="hljs-keyword">if</span> (!cb.cancelled) &#123;
        addTransitionClass(el, toClass)
        <span class="hljs-keyword">if</span> (!userWantsControl) &#123;
          <span class="hljs-comment">// 利用 timeout 或者监听 transitionend/animationend 结束事件 调用 cb</span>
          <span class="hljs-keyword">if</span> (isValidDuration(explicitEnterDuration)) &#123;
            <span class="hljs-built_in">setTimeout</span>(cb, explicitEnterDuration)
          &#125; <span class="hljs-keyword">else</span> &#123;
            whenTransitionEnds(el, type, cb)
          &#125;
        &#125;
      &#125;
    &#125;)
  &#125;
 
  <span class="hljs-keyword">if</span> (vnode.data.show) &#123;
    toggleDisplay && toggleDisplay()
    enterHook && enterHook(el, cb)
  &#125;
 
  <span class="hljs-keyword">if</span> (!expectsCSS && !userWantsControl) &#123;
    cb()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>enter 的时候最核心的就是<strong>在 nextFrame 中移除了 startClass，使得可以有一帧去渲染且马上移除进而做动画。</strong></p>
<p>再来看下 leave 的逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">leave</span> (<span class="hljs-params">vnode: VNodeWithData, rm: <span class="hljs-built_in">Function</span></span>) </span>&#123;
  <span class="hljs-comment">// rm 就是真正的 操作 DOM 移除元素的函数</span>
  <span class="hljs-keyword">const</span> el: any = vnode.elm
 
  <span class="hljs-comment">// call enter callback now</span>
  <span class="hljs-comment">// 相对等的逻辑 还没等到 enter 完成 就已经 leave 了</span>
  <span class="hljs-keyword">if</span> (isDef(el._enterCb)) &#123;
    el._enterCb.cancelled = <span class="hljs-literal">true</span>
    el._enterCb()
  &#125;
 
  <span class="hljs-keyword">const</span> data = resolveTransition(vnode.data.transition)
  <span class="hljs-keyword">if</span> (isUndef(data) || el.nodeType !== <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> rm()
  &#125;
 
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (isDef(el._leaveCb)) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
 
  <span class="hljs-keyword">const</span> &#123;
    css,
    type,
    leaveClass,
    leaveToClass,
    leaveActiveClass,
    beforeLeave,
    leave,
    afterLeave,
    leaveCancelled,
    delayLeave,
    duration
  &#125; = data
 
  <span class="hljs-keyword">const</span> expectsCSS = css !== <span class="hljs-literal">false</span> && !isIE9
  <span class="hljs-keyword">const</span> userWantsControl = getHookArgumentsLength(leave)
 
  <span class="hljs-keyword">const</span> explicitLeaveDuration: any = toNumber(
    isObject(duration)
      ? duration.leave
      : duration
  )
 
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && isDef(explicitLeaveDuration)) &#123;
    checkDuration(explicitLeaveDuration, <span class="hljs-string">'leave'</span>, vnode)
  &#125;
  <span class="hljs-comment">// leave 完成的 cb</span>
  <span class="hljs-keyword">const</span> cb = el._leaveCb = once(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 清除</span>
    <span class="hljs-keyword">if</span> (el.parentNode && el.parentNode._pending) &#123;
      el.parentNode._pending[vnode.key] = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">if</span> (expectsCSS) &#123;
      removeTransitionClass(el, leaveToClass)
      removeTransitionClass(el, leaveActiveClass)
    &#125;
    <span class="hljs-keyword">if</span> (cb.cancelled) &#123;
      <span class="hljs-keyword">if</span> (expectsCSS) &#123;
        removeTransitionClass(el, leaveClass)
      &#125;
      leaveCancelled && leaveCancelled(el)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 真正移除</span>
      rm()
      <span class="hljs-comment">// afterLeave 钩子</span>
      afterLeave && afterLeave(el)
    &#125;
    el._leaveCb = <span class="hljs-literal">null</span>
  &#125;)
  <span class="hljs-comment">// 如果是 delayLeave 即 in-out 模式</span>
  <span class="hljs-keyword">if</span> (delayLeave) &#123;
    delayLeave(performLeave)
  &#125; <span class="hljs-keyword">else</span> &#123;
    performLeave()
  &#125;
  <span class="hljs-comment">// 真正执行 leave 动画逻辑</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performLeave</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// the delayed leave may have already been cancelled</span>
    <span class="hljs-keyword">if</span> (cb.cancelled) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// record leaving element</span>
    <span class="hljs-comment">// 记录下 移除中 的元素，注意和 enter 中对应，挂载到 父元素上</span>
    <span class="hljs-keyword">if</span> (!vnode.data.show && el.parentNode) &#123;
      (el.parentNode._pending || (el.parentNode._pending = &#123;&#125;))[(vnode.key: any)] = vnode
    &#125;
    <span class="hljs-comment">// beforeLeave 钩子</span>
    beforeLeave && beforeLeave(el)
    <span class="hljs-keyword">if</span> (expectsCSS) &#123;
      <span class="hljs-comment">// 增加 class</span>
      addTransitionClass(el, leaveClass)
      addTransitionClass(el, leaveActiveClass)
      <span class="hljs-comment">// 相似的逻辑 下一帧 移除 class</span>
      nextFrame(<span class="hljs-function">() =></span> &#123;
        removeTransitionClass(el, leaveClass)
        <span class="hljs-keyword">if</span> (!cb.cancelled) &#123;
          addTransitionClass(el, leaveToClass)
          <span class="hljs-keyword">if</span> (!userWantsControl) &#123;
            <span class="hljs-keyword">if</span> (isValidDuration(explicitLeaveDuration)) &#123;
              <span class="hljs-built_in">setTimeout</span>(cb, explicitLeaveDuration)
            &#125; <span class="hljs-keyword">else</span> &#123;
              whenTransitionEnds(el, type, cb)
            &#125;
          &#125;
        &#125;
      &#125;)
    &#125;
    leave && leave(el, cb)
    <span class="hljs-keyword">if</span> (!expectsCSS && !userWantsControl) &#123;
      cb()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比下 enter 的部分，发现基本上的大概逻辑还是一致的。</p>
<p>整体还是利用 transition data 传递了来自 transition 的 prop 值以及对应的监听的事件钩子函数，将他们挂载在 vnode.data 上，这样在 transition module 中可以直接根据 vnode 上挂载的相关数据直接进行操作。</p>
<p>大概总结整体的逻辑关系就是：</p>
<ul>
<li>render() 根据新旧 children 的 vnode 信息决定返回的内容，以此决定了后续 patch 过程中是走 create 还是 remove 的钩子；这个过程中同样会把 transition 组件上传入的 props 以及相关事件监听附在 vnode.data 上</li>
<li>在 transition module 中，注册了 create 和 remove 的钩子，然后结合 vnode.data 中的 transition data 进行 leave 和 enter 相关的过渡动画处理</li>
</ul>
<h4 data-id="heading-5">transition-group</h4>
<p>除了上边分析的 transition 组件，Vue 还提供了在列表场景下的过渡组件 transition-group <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Ftransitions.html%23%25E5%2588%2597%25E8%25A1%25A8%25E8%25BF%2587%25E6%25B8%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/transitions.html#%E5%88%97%E8%A1%A8%E8%BF%87%E6%B8%A1" ref="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/tr…</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80e8ee38b654443ebd8a49584878b1a1~tplv-k3u1fbpfcp-watermark.image" alt="image2021-7-9_21-28-58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>讲述了 transition-group 组件的几个特点以及相关的注意事项。</p>
<p>那么这个组件详细背后的逻辑是啥，一起看看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fv2.6.14%2Fsrc%2Fplatforms%2Fweb%2Fruntime%2Fcomponents%2Ftransition-group.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/v2.6.14/src/platforms/web/runtime/components/transition-group.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// extend 了 transition 组件的 props</span>
<span class="hljs-keyword">const</span> props = extend(&#123;
  <span class="hljs-attr">tag</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">moveClass</span>: <span class="hljs-built_in">String</span>
&#125;, transitionProps)
<span class="hljs-comment">// 不支持 mode 了</span>
<span class="hljs-keyword">delete</span> props.mode
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  props,
 
  beforeMount () &#123;
    <span class="hljs-comment">// beforeMount 钩子中所做的事情</span>
    <span class="hljs-comment">// 劫持（代理了） _update 函数，我们知道这个函数的核心是 执行 patch 以及 更新当前活动的组件实例 active instance</span>
    <span class="hljs-keyword">const</span> update = <span class="hljs-built_in">this</span>._update
    <span class="hljs-built_in">this</span>._update = <span class="hljs-function">(<span class="hljs-params">vnode, hydrating</span>) =></span> &#123;
      <span class="hljs-comment">// 当 _update 被调用的时候 传入的 vnode 就是调用 render() 得到的</span>
      <span class="hljs-keyword">const</span> restoreActiveInstance = setActiveInstance(<span class="hljs-built_in">this</span>)
      <span class="hljs-comment">// force removing pass</span>
      <span class="hljs-comment">// 此时是将上次的 vnode 和 kept（列表中需要保留的）vnode 进行 patch</span>
      <span class="hljs-comment">// 进而将那些需要移除的节点删除</span>
      <span class="hljs-built_in">this</span>.__patch__(
        <span class="hljs-built_in">this</span>._vnode,
        <span class="hljs-built_in">this</span>.kept,
        <span class="hljs-literal">false</span>, <span class="hljs-comment">// hydrating</span>
        <span class="hljs-literal">true</span> <span class="hljs-comment">// removeOnly (!important, avoids unnecessary moves)</span>
      )
      <span class="hljs-comment">// 更新此时的新的 _vnode 为 kept 中的</span>
      <span class="hljs-built_in">this</span>._vnode = <span class="hljs-built_in">this</span>.kept
      <span class="hljs-comment">// 恢复 active instance</span>
      restoreActiveInstance()
      <span class="hljs-comment">// 执行原本的 patch 正常逻辑</span>
      update.call(<span class="hljs-built_in">this</span>, vnode, hydrating)
    &#125;
  &#125;,
 
  render (h: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> tag: string = <span class="hljs-built_in">this</span>.tag || <span class="hljs-built_in">this</span>.$vnode.data.tag || <span class="hljs-string">'span'</span>
    <span class="hljs-keyword">const</span> map: <span class="hljs-built_in">Object</span> = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> prevChildren: <span class="hljs-built_in">Array</span><VNode> = <span class="hljs-built_in">this</span>.prevChildren = <span class="hljs-built_in">this</span>.children
    <span class="hljs-keyword">const</span> rawChildren: <span class="hljs-built_in">Array</span><VNode> = <span class="hljs-built_in">this</span>.$slots.default || []
    <span class="hljs-keyword">const</span> children: <span class="hljs-built_in">Array</span><VNode> = <span class="hljs-built_in">this</span>.children = []
    <span class="hljs-keyword">const</span> transitionData: <span class="hljs-built_in">Object</span> = extractTransitionData(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// 首先遍历现在的 children</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < rawChildren.length; i++) &#123;
      <span class="hljs-keyword">const</span> c: VNode = rawChildren[i]
      <span class="hljs-keyword">if</span> (c.tag) &#123;
        <span class="hljs-comment">// 记录 tag 元素相关的</span>
        <span class="hljs-comment">// 一定要有 key，放入 children 中，且这个 key 不能是 自动生成的 key</span>
        <span class="hljs-comment">// 同时利用 map 做了一个按 key 缓存</span>
        <span class="hljs-keyword">if</span> (c.key != <span class="hljs-literal">null</span> && <span class="hljs-built_in">String</span>(c.key).indexOf(<span class="hljs-string">'__vlist'</span>) !== <span class="hljs-number">0</span>) &#123;
          children.push(c)
          map[c.key] = c
          ;(c.data || (c.data = &#123;&#125;)).transition = transitionData
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
          <span class="hljs-keyword">const</span> opts: ?VNodeComponentOptions = c.componentOptions
          <span class="hljs-keyword">const</span> name: string = opts ? (opts.Ctor.options.name || opts.tag || <span class="hljs-string">''</span>) : c.tag
          warn(<span class="hljs-string">`<transition-group> children must be keyed: <<span class="hljs-subst">$&#123;name&#125;</span>>`</span>)
        &#125;
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (prevChildren) &#123;
      <span class="hljs-keyword">const</span> kept: <span class="hljs-built_in">Array</span><VNode> = []
      <span class="hljs-keyword">const</span> removed: <span class="hljs-built_in">Array</span><VNode> = []
      <span class="hljs-comment">// 遍历之前的 children</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prevChildren.length; i++) &#123;
        <span class="hljs-keyword">const</span> c: VNode = prevChildren[i]
        <span class="hljs-comment">// 保存好之前的 transition data</span>
        c.data.transition = transitionData
        <span class="hljs-comment">// 增加位置信息</span>
        c.data.pos = c.elm.getBoundingClientRect()
        <span class="hljs-comment">// 如果这个 key 的元素在新的里边也存在 那么就放入 kept 中</span>
        <span class="hljs-keyword">if</span> (map[c.key]) &#123;
          kept.push(c)
        &#125; <span class="hljs-keyword">else</span> &#123;
          removed.push(c)
        &#125;
      &#125;
      <span class="hljs-comment">// 保存需要保留的元素</span>
      <span class="hljs-built_in">this</span>.kept = h(tag, <span class="hljs-literal">null</span>, kept)
      <span class="hljs-comment">// 保存需要删除的元素 其实这个是没有用的</span>
      <span class="hljs-built_in">this</span>.removed = removed
    &#125;
    <span class="hljs-comment">// 返回包含 children 的指定 tag 的 vnode 元素</span>
    <span class="hljs-keyword">return</span> h(tag, <span class="hljs-literal">null</span>, children)
  &#125;,
  updated () &#123;
    <span class="hljs-comment">// 之前的 children</span>
    <span class="hljs-keyword">const</span> children: <span class="hljs-built_in">Array</span><VNode> = <span class="hljs-built_in">this</span>.prevChildren
    <span class="hljs-comment">// move 的 class</span>
    <span class="hljs-keyword">const</span> moveClass: string = <span class="hljs-built_in">this</span>.moveClass || ((<span class="hljs-built_in">this</span>.name || <span class="hljs-string">'v'</span>) + <span class="hljs-string">'-move'</span>)
    <span class="hljs-keyword">if</span> (!children.length || !<span class="hljs-built_in">this</span>.hasMove(children[<span class="hljs-number">0</span>].elm, moveClass)) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 下面的就是实现和 https://cn.vuejs.org/v2/guide/transitions.html#%E5%88%97%E8%A1%A8%E7%9A%84%E6%8E%92%E5%BA%8F%E8%BF%87%E6%B8%A1 FLIP 相关动画</span>
    <span class="hljs-comment">// we divide the work into three loops to avoid mixing DOM reads and writes</span>
    <span class="hljs-comment">// in each iteration - which helps prevent layout thrashing.</span>
    <span class="hljs-comment">// 所有的 children 一起：</span>
    <span class="hljs-comment">// 1. 调用每个 child 的 _moveCb 和 _enterCb，上一次还没完成的，所以是 pending 的命名</span>
    <span class="hljs-comment">// 2. 记录每个 child 的位置信息</span>
    <span class="hljs-comment">// 3. 给每一个应用 0s 的 位置差 transform 动画 让元素”恢复“在原位（位置差）</span>
    children.forEach(callPendingCbs)
    children.forEach(recordPosition)
    children.forEach(applyTranslation)
 
    <span class="hljs-comment">// force reflow to put everything in position</span>
    <span class="hljs-comment">// assign to this to avoid being removed in tree-shaking</span>
    <span class="hljs-comment">// $flow-disable-line</span>
    <span class="hljs-comment">// 强制 reflow 确保浏览器重新绘制到指定位置</span>
    <span class="hljs-built_in">this</span>._reflow = <span class="hljs-built_in">document</span>.body.offsetHeight
 
    children.forEach(<span class="hljs-function">(<span class="hljs-params">c: VNode</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (c.data.moved) &#123;
        <span class="hljs-comment">// 如果有移动</span>
        <span class="hljs-keyword">const</span> el: any = c.elm
        <span class="hljs-keyword">const</span> s: any = el.style
        <span class="hljs-comment">// 增加 move class</span>
        addTransitionClass(el, moveClass)
        <span class="hljs-comment">// 重置 transform & transitionDuration</span>
        s.transform = s.WebkitTransform = s.transitionDuration = <span class="hljs-string">''</span>
        el.addEventListener(transitionEndEvent, el._moveCb = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cb</span> (<span class="hljs-params">e</span>) </span>&#123;
          <span class="hljs-comment">// 动画结束回调</span>
          <span class="hljs-keyword">if</span> (e && e.target !== el) &#123;
            <span class="hljs-keyword">return</span>
          &#125;
          <span class="hljs-keyword">if</span> (!e || <span class="hljs-regexp">/transform$/</span>.test(e.propertyName)) &#123;
            el.removeEventListener(transitionEndEvent, cb)
            el._moveCb = <span class="hljs-literal">null</span>
            <span class="hljs-comment">// 移除 class</span>
            removeTransitionClass(el, moveClass)
          &#125;
        &#125;)
      &#125;
    &#125;)
  &#125;,
 
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 判断是否应该应用移动 feat</span>
    hasMove (el: any, <span class="hljs-attr">moveClass</span>: string): boolean &#123;
      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-keyword">if</span> (!hasTransition) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      <span class="hljs-comment">/* istanbul ignore if */</span>
      <span class="hljs-comment">// 缓存</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._hasMove) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._hasMove
      &#125;
      <span class="hljs-comment">// Detect whether an element with the move class applied has</span>
      <span class="hljs-comment">// CSS transitions. Since the element may be inside an entering</span>
      <span class="hljs-comment">// transition at this very moment, we make a clone of it and remove</span>
      <span class="hljs-comment">// all other transition classes applied to ensure only the move class</span>
      <span class="hljs-comment">// is applied.</span>
      <span class="hljs-keyword">const</span> clone: HTMLElement = el.cloneNode()
      <span class="hljs-comment">// clone 一个 将之前的 _transitionClasses 移除</span>
      <span class="hljs-keyword">if</span> (el._transitionClasses) &#123;
        el._transitionClasses.forEach(<span class="hljs-function">(<span class="hljs-params">cls: string</span>) =></span> &#123; removeClass(clone, cls) &#125;)
      &#125;
      <span class="hljs-comment">// 只加上 move 的 class</span>
      addClass(clone, moveClass)
      clone.style.display = <span class="hljs-string">'none'</span>
      <span class="hljs-built_in">this</span>.$el.appendChild(clone)
      <span class="hljs-comment">// 得到新的 transition 信息</span>
      <span class="hljs-keyword">const</span> info: <span class="hljs-built_in">Object</span> = getTransitionInfo(clone)
      <span class="hljs-comment">// 移除这个 clone 的元素</span>
      <span class="hljs-built_in">this</span>.$el.removeChild(clone)
      <span class="hljs-comment">// 判断 动画中有没有做 transform 相关的动画</span>
      <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>._hasMove = info.hasTransform)
    &#125;
  &#125;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callPendingCbs</span> (<span class="hljs-params">c: VNode</span>) </span>&#123;
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (c.elm._moveCb) &#123;
    c.elm._moveCb()
  &#125;
  <span class="hljs-comment">/* istanbul ignore if */</span>
  <span class="hljs-keyword">if</span> (c.elm._enterCb) &#123;
    c.elm._enterCb()
  &#125;
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">recordPosition</span> (<span class="hljs-params">c: VNode</span>) </span>&#123;
  c.data.newPos = c.elm.getBoundingClientRect()
&#125;
 
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyTranslation</span> (<span class="hljs-params">c: VNode</span>) </span>&#123;
  <span class="hljs-keyword">const</span> oldPos = c.data.pos
  <span class="hljs-keyword">const</span> newPos = c.data.newPos
  <span class="hljs-keyword">const</span> dx = oldPos.left - newPos.left
  <span class="hljs-keyword">const</span> dy = oldPos.top - newPos.top
  <span class="hljs-keyword">if</span> (dx || dy) &#123;
    c.data.moved = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">const</span> s = c.elm.style
    s.transform = s.WebkitTransform = <span class="hljs-string">`translate(<span class="hljs-subst">$&#123;dx&#125;</span>px,<span class="hljs-subst">$&#123;dy&#125;</span>px)`</span>
    s.transitionDuration = <span class="hljs-string">'0s'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在让我们梳理下上边的逻辑搭配 Vue 的渲染逻辑的最终样子：</p>
<ul>
<li>beforeMount
<ul>
<li>劫持了 _update</li>
</ul>
</li>
<li>第一次 render()
<ul>
<li>children 节点设置 transition data，通过上边 transition 的分析我们知道 只要节点上保存了 transition data 信息，就可以执行对应的 transition 相关过渡动画逻辑</li>
</ul>
</li>
<li>调用 _update
<ul>
<li>约等于做了一次空 patch</li>
<li>执行真正的原始 patch 逻辑</li>
</ul>
</li>
<li>当有更新的时候，第二次 render()
<ul>
<li>核心对比，新旧 children，找出 kept 的节点数据</li>
<li>返回新的 vnode 数据</li>
</ul>
</li>
<li>再次 _update
<ul>
<li>进行一次 kept 和 现有的 vnode 数据的 patch，结论就是把需要删除的元素移除掉</li>
<li>然后进行正常的原始的 patch 逻辑，这个时候 patch 进行比较的是 kept 和 新得到的 vnode 数据</li>
</ul>
</li>
<li>updated
<ul>
<li>根据新的 DOM 得到最新的列表节点的位置信息</li>
<li>利用 transform 根据元素位置差 将元素“恢复”到原位</li>
<li>给元素增加 move 的 class（做过渡动画）</li>
</ul>
</li>
</ul>
<p>代理 _update 实现了列表项的增加、删除动画逻辑，updated 钩子中则完成了  move 这个 feature 的（如应用 FLIP 动画）逻辑。</p>
<h3 data-id="heading-6">Why</h3>
<p>个人认为，大概的原因，最核心的一个点，Vue 是一个框架，需要根据开发者的日常场景提供功能 feature（当然，选择权在 Vue 团队），考虑到在 Web 中过渡动画类需求如此场景，尤其是有了 CSS 相关的过渡动画规范之后，而且基本没啥兼容性了，当然考虑到利用 JS 精细控制过渡动画，还提供了友好的钩子，开发者可以自行选择。</p>
<p>而且，Vue 不但要做，还是做到很好，通过上边的分析，我们知道了过渡相关组件提供的能力，基本可以和官网说的一样：唯一的限制是你的想象力。Vue 已经提供了如此灵活强大的组件，你的场景都可以满足！</p>
<h2 data-id="heading-7">总结</h2>
<p>这次我们基本分析了 Vue 中提供的两个强大的过渡组件 transition 和 transition-group，对应的代码虽然不是很多，但是给开发者提供的功能却有很多，基本上涵盖了日常开发过渡动画的大多数场景，甚至借助于其动态过渡能力，可以很方便的自定义出满足复杂场景的过渡动画效果。</p>
<p>那从 transition 以及 transition-group 的分析中，我们可以学到什么呢？</p>
<h3 data-id="heading-8">过渡动画</h3>
<p>从上边分析我们知道，Vue 中实现过渡动画分为了三种过渡类名：</p>
<ul>
<li>过渡生效状态——定义整个过渡阶段，一般用于设置过渡时间、延迟等，会在整个动画结束后移除</li>
<li>过渡开始状态——元素插入后下一帧就会移除</li>
<li>过渡结束状态——开始状态移除后，就设置了结束状态，会在动画结束后移除</li>
</ul>
<p>以及提供了钩子（以Enter举例）：</p>
<ul>
<li>before-enter 未进入之前，元素还没插入</li>
<li>enter 元素插入之后</li>
<li>after-enter 过渡动画结束后</li>
<li>enter-cancelled 过渡动画被取消</li>
</ul>
<p>不仅仅满足了大家使用 CSS 做过渡动画的场景，同时也满足了利用 JS 做动画的诉求。API 或者类名切换的理解成本很低，这个是我们可以在自己抽象和设计过渡动画相关的 API 的时候，可以学习参考的。</p>
<h3 data-id="heading-9">代理模式</h3>
<p>在 transition-group 中，利用对 _update 的代理，实现了一次更新，两次 patch 的目标。代理模式是一种很有用的模式，在很多场景中我们都是可以使用，这种方式意味着我们可以在不修改原有代码的基础上就可以实现功能扩展，很符合开闭原则。</p>
<h3 data-id="heading-10">异步回调</h3>
<p>在分析中，我们看到了关于异步回调的处理，如 _enterCb、_leaveCb、_moveCb 这种处理，这些回调函数在正常流程中调用的话没问题，但是会存在一些异常情况，这里的典型就是数据再次更新，再次需要 enter 或者 leave 怎么办，因为处理过程是一个异步的，这个时候需要清除上一次更新的影响，Vue 中此时的处理是统一都会调用这个回调，回调内部根据这个 cb 的 cancelled 属性决定是取消模式还是支持回调的。</p>
<p>同时这里边也可以看到及时的消除引用关系，释放内存。</p>
<h3 data-id="heading-11">模块解耦</h3>
<p>我们此时已经知道了，transition 的功能实现依赖两个：一个是 transition 组件的定义，一个是 transition module 模块的钩子处理。本来这部分应该是一个强耦合的逻辑，在 Vue 中，因为有了 vnode 的存在，他们可以彼此解耦。</p>
<p>transition 过渡动画的核心逻辑都在 transition module 中，也正是因为这个，很容易实现了 transition-group 组件。</p>
<p>这里边的另一个解耦，就是利用钩子的处理，我们已经明显感知到了他们存在。</p>
<h3 data-id="heading-12">延迟设值</h3>
<p>在 transition 组件的 render 中存在这样一段逻辑：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// mode === 'in-out'</span>
<span class="hljs-keyword">let</span> delayedLeave
<span class="hljs-keyword">const</span> performLeave = <span class="hljs-function">() =></span> &#123; delayedLeave() &#125;
<span class="hljs-comment">// 监听 afterEnter 钩子 执行之前保留下来的 leave 回调逻辑</span>
<span class="hljs-comment">// 这样实现了先 in 后 out 的效果，因为是等到 afterEnter 之后才走的 leave 逻辑</span>
mergeVNodeHook(data, <span class="hljs-string">'afterEnter'</span>, performLeave)
mergeVNodeHook(data, <span class="hljs-string">'enterCancelled'</span>, performLeave)
<span class="hljs-comment">// 回调设置，把 leave 执行的执行逻辑保留下来</span>
mergeVNodeHook(oldData, <span class="hljs-string">'delayLeave'</span>, <span class="hljs-function"><span class="hljs-params">leave</span> =></span> &#123; delayedLeave = leave &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一段异步加异步的情况，通过在 delayLeave 钩子中，设置了 delayedLeave 这个回调的值，然后在其他场景（时机）去调用这个 delayedLeave 回调。</p>
<p>同时这里为了确保 afterEnter 的钩子函数是一定存在的，所以新增加了一个函数 performLeave，巧用了闭包的技巧实现了访问后设置的 delayedLeave。</p>
<h3 data-id="heading-13">其他小Tips</h3>
<ul>
<li>在组件中对 vnode 的各种使用，例如如何获取上一次的 children 信息，如果获取当前 children 信息</li>
<li>mergeVNodeHook 是如何实现的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue%2Fblob%2Fv2.6.14%2Fsrc%2Fcore%2Fvdom%2Fhelpers%2Fmerge-hook.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue/blob/v2.6.14/src/core/vdom/helpers/merge-hook.js" ref="nofollow noopener noreferrer">github.com/vuejs/vue/b…</a></li>
<li>FLIP 动画 <a href="https://link.juejin.cn/?target=https%3A%2F%2Faerotwist.com%2Fblog%2Fflip-your-animations%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aerotwist.com/blog/flip-your-animations/" ref="nofollow noopener noreferrer">aerotwist.com/blog/flip-y…</a></li>
<li>强制reflow</li>
<li>once 的实现以及应用</li>
<li>$forceUpdate API 以及其应用</li>
</ul>
<p><a href="https://juejin.cn/team/6943816493473726472" target="_blank" title="https://juejin.cn/team/6943816493473726472">滴滴前端技术团队的团队号</a>已经上线，我们也同步了一定的<a href="https://juejin.cn/team/6943816493473726472/hire" target="_blank" title="https://juejin.cn/team/6943816493473726472/hire">招聘信息</a>，我们也会持续增加更多职位，有兴趣的同学可以一起聊聊。</p></div>  
</div>
            