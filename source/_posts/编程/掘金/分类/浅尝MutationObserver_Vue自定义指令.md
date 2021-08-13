
---
title: '浅尝MutationObserver_Vue自定义指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30941dcfdbf44c09830188cc2b05246f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 08:25:30 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30941dcfdbf44c09830188cc2b05246f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">源码之旅</h2>
<p>Vue 的自定义指令，用来解决需要对普通 DOM 元素进行操作的问题。</p>
<p>看Element UI库的源码，其中 <a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2FinfiniteScroll" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/infiniteScroll" ref="nofollow noopener noreferrer">v-infinite-scroll</a>无限滚动可配置的属性：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30941dcfdbf44c09830188cc2b05246f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>源码传送门：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Finfinite-scroll%2Fsrc%2Fmain.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ElemeFE/element/blob/dev/packages/infinite-scroll/src/main.js" ref="nofollow noopener noreferrer">Element</a> &
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felement-plus%2Felement-plus%2Fblob%2Fdev%2Fpackages%2Finfinite-scroll%2Fsrc%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/element-plus/element-plus/blob/dev/packages/infinite-scroll/src/index.ts" ref="nofollow noopener noreferrer">Element-plus</a></p>
<p>按照自己的理解，截取了基于Vue2.x的部分源码，添加了一些注释，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'InfiniteScroll'</span>,
   <span class="hljs-comment">/**
   * <span class="hljs-doctag">@description</span>: 被绑定元素插入父节点时调用inserted
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>el 指令所绑定的元素，可以用来直接操作 DOM
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>binding 指令属性对象
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>vnode Vue 编译生成的虚拟节点
   */</span>  
  <span class="hljs-function"><span class="hljs-title">inserted</span>(<span class="hljs-params">el, binding, vnode</span>)</span> &#123;
    <span class="hljs-comment">// 该指令的绑定值，则该指令的滚动回调</span>
    <span class="hljs-keyword">const</span> cb = binding.value;  

    <span class="hljs-keyword">const</span> vm = vnode.context;
    <span class="hljs-comment">// 针对垂直滚动，获取目标节点</span>
    <span class="hljs-keyword">const</span> container = getScrollContainer(el, <span class="hljs-literal">true</span>);
    <span class="hljs-comment">// 获取配置的属性值</span>
    <span class="hljs-keyword">const</span> &#123; delay, immediate &#125; = getScrollOptions(el, vm);
    <span class="hljs-comment">// 监听滚动事件当然需要配合节流呀~</span>
    <span class="hljs-keyword">const</span> onScroll = throttle(delay, handleScroll.bind(el, cb));
    
    <span class="hljs-comment">// 定义目标DOM</span>
    el[scope] = &#123; el, vm, container, onScroll &#125;;

    <span class="hljs-keyword">if</span> (container) &#123;
      <span class="hljs-comment">// 监听滚动事件</span>
      container.addEventListener(<span class="hljs-string">'scroll'</span>, onScroll);
       
      <span class="hljs-comment">// 若立即执行加载（默认为true）</span>
      <span class="hljs-keyword">if</span> (immediate) &#123;
         <span class="hljs-comment">// 为观察DOM树结构发生变化：创建并返回一个观察器实例 MutationObserver</span>
         <span class="hljs-comment">// 当指定的DOM发生变化时，会执行回调函数 onScroll</span>
        <span class="hljs-keyword">const</span> observer = el[scope].observer = <span class="hljs-keyword">new</span> MutationObserver(onScroll);
        <span class="hljs-comment">// 配置MutationObserver，开始观察目标节点</span>
        observer.observe(container, &#123; <span class="hljs-attr">childList</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">subtree</span>: <span class="hljs-literal">true</span> &#125;);
        <span class="hljs-comment">// 立即执行：当然要执行一次onScroll，不然哪来的变化观察呢</span>
        onScroll();
      &#125;
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">unbind</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; container, onScroll &#125; = el[scope];
    <span class="hljs-keyword">if</span> (container) &#123;
      <span class="hljs-comment">// 指令与元素解绑时调用时，移除监听</span>
      container.removeEventListener(<span class="hljs-string">'scroll'</span>, onScroll);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，针对<code>infinite-scroll-immediate</code>的实现，使用到了<code>MutationObserver()</code>这个构造函数
（补充：Element-plus该属性的实现基本一致）</p>
<h2 data-id="heading-1">为什么用MutationObserver</h2>
<p>Element官方文档的说明：</p>
<blockquote>
<p>infinite-scroll-immediate：是否立即执行加载方法，以防初始状态下内容无法撑满容器。默认为true</p>
</blockquote>
<p>无限滚动这个指令，为了解决滚动加载的问题，v-infinite-scroll的绑定值，就是数据的加载回调函数</p>
<p>官方实例：</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"infinite-list"</span> <span class="hljs-attr">v-infinite-scroll</span>=<span class="hljs-string">"load"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"overflow:auto"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"i in count"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"infinite-list-item"</span>></span>&#123;&#123; i &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
      <span class="hljs-comment">// 用于加载滚动数据</span>
      <span class="hljs-keyword">const</span> load = <span class="hljs-function">() =></span> &#123;
        count.value += <span class="hljs-number">2</span>;
      &#125;;
      <span class="hljs-keyword">return</span> &#123;
        count,
        load,
      &#125;;
    &#125;,
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<strong>立即执行</strong>是针对<strong>初始</strong>状态下<strong>内容撑满容器</strong>的需求，必然要知道内容DOM的变化，以确认需要执行多少次回调函数：onScroll</p>
<h2 data-id="heading-2">MutationObserver是什么</h2>
<p>MutationObserver可监视对DOM树所做的更改，作为一个观察者对象，DOM变化执行触发回调，提供了一个接口操作DOM。</p>
<p>废话不多说，链接传送门：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FMutationObserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/MutationObserver" ref="nofollow noopener noreferrer"><em>MutationObserver</em> - Web API 接口参考</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fb5c9e4c7b1e1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/b5c9e4c7b1e1" ref="nofollow noopener noreferrer"><em>MutationObserver</em> 监听DOM树变化</a></p>
<ul>
<li><strong>observer.observe(target[, options])</strong></li>
</ul>
<p>若源码进行如下改动：会报错</p>
<pre><code class="copyable">// childList：观察目标节点的子节点的新增和删除
// subtree：观察目标节点的所有后代节点
observer.observe(container, &#123; childList: false, subtree: true &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>[Vue warn]</strong>: Error in directive infinite-scroll inserted hook: "TypeError: Failed to execute 'observe' on 'MutationObserver': The options object must set at least one of 'attributes', 'characterData', or 'childList' to true."</p>
<p>可知，options对象必须将"attributes"、"characterData"或"childList"中的至少一个设置为true。</p>
<ul>
<li><strong>observer.disconnect()</strong></li>
</ul>
<p>可停止观察DOM变化，回调函数不再执行，直至再次调用其observe()方法</p>
<ul>
<li><strong>异步执行</strong></li>
</ul>
<blockquote>
<p>Mutation Observer 是在DOM4中定义的，用于替代 mutation events 的新API，它的不同于events的是，所有监听操作以及相应处理都是在其他脚本执行完成之后异步执行的，并且是所以变动触发之后，将变得记录在数组中，统一进行回调的，也就是说，当你使用observer监听多个DOM变化时，并且这若干个DOM发生了变化，那么observer会将变化记录到变化数组中，等待一起都结束了，然后一次性的从变化数组中执行其对应的回调函数</p>
</blockquote>
<h2 data-id="heading-3">其他应用</h2>
<p>Vue 2.x有关<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Freactivity.html%23%25E5%25BC%2582%25E6%25AD%25A5%25E6%259B%25B4%25E6%2596%25B0%25E9%2598%259F%25E5%2588%2597" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/reactivity.html#%E5%BC%82%E6%AD%A5%E6%9B%B4%E6%96%B0%E9%98%9F%E5%88%97" ref="nofollow noopener noreferrer">异步更新队列</a>的说明，提到了MutationObserver</p>
<blockquote>
<p>Vue 在内部对异步队列尝试使用原生的 <code>Promise.then</code>、<code>MutationObserver</code> 和 <code>setImmediate</code>，如果执行环境不支持，则会采用 <code>setTimeout(fn, 0)</code> 代替</p>
</blockquote>
<p>提供了Vue.nextTick(callback)，保证在数据变化之后，DOM的更新完成，再执行后续操作：callback</p>
<p>有关$nextTick源码可阅读 <a href="https://juejin.cn/post/6995192695501094920" target="_blank" title="https://juejin.cn/post/6995192695501094920">Vue 2.x / nextTick</a></p>
<h2 data-id="heading-4">Last but not least</h2>
<p>如有不妥，请多指教~</p></div>  
</div>
            