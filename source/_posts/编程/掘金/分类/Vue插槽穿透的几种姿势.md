
---
title: 'Vue插槽穿透的几种姿势'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6105'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 06:14:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=6105'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>用render函数开发高阶组件时经常会向下传递插槽，reat使用的是children异常方便，和Vue的插槽（静态插槽、作用域插槽）使用类似。</p>
<p>插槽穿透，大概有三种方式：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// 1.在子组件访问父级插槽</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$parent.$slots)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$parent.$scopedSlots)
<span class="hljs-comment">// 2. 分别传递静态，作用域插槽</span>
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$slots)
  <span class="hljs-keyword">return</span> h(<span class="hljs-string">'render-com'</span>, &#123;
    <span class="hljs-attr">scopedSlots</span>: &#123;
      <span class="hljs-comment">// 传递作用于插槽</span>
      <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-params">props</span> =></span> h(<span class="hljs-string">'span'</span>, props.text)
    &#125;
  &#125;, [...Object.keys(<span class="hljs-built_in">this</span>.$slots).map(<span class="hljs-function"><span class="hljs-params">slotName</span> =></span> <span class="hljs-built_in">this</span>.$slots[slotName])]
  )
&#125;
<span class="hljs-comment">// 3.同时传递静态插槽和作用域插槽</span>
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
  <span class="hljs-keyword">const</span> slots = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.$slots).map(<span class="hljs-function"><span class="hljs-params">slotName</span> =></span>
    <span class="hljs-built_in">this</span>._t(slotName, <span class="hljs-literal">null</span>, &#123; <span class="hljs-attr">slot</span>: slotName &#125;)
  )
  <span class="hljs-keyword">return</span> h(<span class="hljs-string">'render-com'</span>, &#123;
  &#125;, slots
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意第三种方式中的<code>this._t</code>函数,大名是<code>renderSlot</code>，如果是普通插槽，就直接调用函数生成 vnode，如果是作用域插槽，就直接带着 props 去调用函数生成 vnode。Vue 2.6 版本后对 slot 和 slot-scope 做了一次统一的整合，让它们全部都变为函数的形式，<strong>所有的插槽都可以在 <code>this.$scopedSlots</code> 上直接访问。</strong></p>
<h3 data-id="heading-0">renderSlot函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Runtime helper for rendering <slot>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderSlot</span> (<span class="hljs-params">
  name,
  fallback,
  props,
  bindObject
</span>) </span>&#123;
  <span class="hljs-keyword">var</span> scopedSlotFn = <span class="hljs-built_in">this</span>.$scopedSlots[name];
  <span class="hljs-keyword">var</span> nodes;
  <span class="hljs-keyword">if</span> (scopedSlotFn) &#123; <span class="hljs-comment">// scoped slot</span>
    props = props || &#123;&#125;;
    <span class="hljs-keyword">if</span> (bindObject) &#123;
      <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span> && !isObject(bindObject)) &#123;
        warn(
          <span class="hljs-string">'slot v-bind without argument expects an Object'</span>,
          <span class="hljs-built_in">this</span>
        );
      &#125;
      props = extend(extend(&#123;&#125;, bindObject), props);
    &#125;
    nodes = scopedSlotFn(props) || fallback;
  &#125; <span class="hljs-keyword">else</span> &#123;
    nodes = <span class="hljs-built_in">this</span>.$slots[name] || fallback;
  &#125;

  <span class="hljs-keyword">var</span> target = props && props.slot;
  <span class="hljs-keyword">if</span> (target) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$createElement(<span class="hljs-string">'template'</span>, &#123; <span class="hljs-attr">slot</span>: target &#125;, nodes)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> nodes
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于Vue 中 slot 和 slot-scope 的原理，参考大神文章：<a href="https://juejin.cn/post/6844904115886096392" target="_blank">juejin.cn/post/684490…</a></p></div>  
</div>
            