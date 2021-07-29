
---
title: 'vue2.0中.sync与v-model'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7336'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:08:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=7336'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">v-model 原来挺香的</h2>
<p>在用Vue开发前端时，不论使用原生还是封装好的UI库，对于表单组件，一般都会使用到v-model。虽然v-model是一个语法糖，但是吃到嘴里挺甜的啊。学会自定义v-model，还是很有必要的。</p>
<p>一个组件上的v-model默认是通过在组件上面定义一个名为value的props,同时对外暴露一个名为input的事件。</p>
<pre><code class="hljs language-js copyable" lang="js">
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-input"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleChange"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 定义一个名为value的属性</span>
    <span class="hljs-attr">value</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    handleChange (e) &#123;
      <span class="hljs-comment">// 对外暴露一个input事件</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, e.target.value)
    &#125;
    
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何使用</p>
<pre><code class="hljs language-js copyable" lang="js"><my-input v-model=<span class="hljs-string">"text"</span>></my-input>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常情况下，使用value属性与input事件没有问题，但是有时候有些组件会将value属性或input事件用于不同的目的，比如对于单选框、复选框等类型的表单组件的value属性就有其他用处，<a href="https://link.juejin.cn/?target=developer.mozilla.org%2Fen-US%2Fdocs%2F%25E2%2580%25A6" target="_blank" title="developer.mozilla.org/en-US/docs/%E2%80%A6" ref="nofollow noopener noreferrer">参考</a>。或者希望属性名称或事件名称与实际行为更贴切，比如active,checked等属性名。</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-check"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123; checked : checked &#125;"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChange"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-check-core"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 通过model可以自定义属性和事件名</span>
  <span class="hljs-attr">model</span>: &#123;
    <span class="hljs-attr">event</span>: <span class="hljs-string">'change'</span>,
    <span class="hljs-attr">prop</span>: <span class="hljs-string">'checked'</span>
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 定义一个名为checked的属性</span>
    <span class="hljs-attr">checked</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    handleChange () &#123;
      <span class="hljs-comment">// 对外暴露一个change事件</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'change'</span>, !<span class="hljs-built_in">this</span>.checked)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">使用.sync后，感觉.sync比v-model更香</h3>
<p>在<code>Vue</code>中，<code>props</code>属性是单向数据传输的,父级的<code>prop</code>的更新会向下流动到子组件中，但是反过来不行。可是有些情况，我们需要对<code>prop</code>进行“双向绑定”。上文中，我们提到了使用v-model实现双向绑定。但有时候我们希望一个组件可以实现多个数据的“双向绑定”，而<code>v-model</code>一个组件只能有一个(Vue3.0可以有多个)，这时候就需要使用到<code>.sync</code>。</p>
<p>.sync与v-model的异同</p>
<p>相同点:</p>
<ol>
<li>两者的本质都是语法糖，目的都是实现组件与外部数据的双向绑定</li>
<li>两个都是通过属性+事件来实现的</li>
</ol>
<p>不同点:</p>
<ol>
<li>一个组件只能定义一个v-model,但可以定义多个.sync</li>
<li>v-model与.sync对于的事件名称不同，v-model默认事件为input,可以通过配置model来修改，.sync事件名称固定为update:属性名</li>
</ol>
<h3 data-id="heading-2">自定义.sync</h3>
<p>在开发业务时，有时候需要使用一个遮罩层来阻止用户的行为（更多会使用遮罩层+loading动画），下面通过自定义.sync来实现一个遮罩层</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <!-- 遮罩层 -->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-loading"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"visible"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChange"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 定义一个名为checked的属性</span>
    <span class="hljs-attr">visible</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    handleChange () &#123;
      <span class="hljs-comment">// 通过update:visible 事件修改外部传入的visible</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:visible'</span>, <span class="hljs-literal">false</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><!--调用方式-->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">my-loading</span> <span class="hljs-attr">:visible.sync</span>=<span class="hljs-string">"visible"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-loading</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">后记</h3>
<p>不管<code>v-model</code>或者<code>.sync</code>只是一个语法糖，更多关于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-custom-events.html%23%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589%25E7%25BB%2584%25E4%25BB%25B6%25E7%259A%2584-v-model" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-custom-events.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E7%BB%84%E4%BB%B6%E7%9A%84-v-model" ref="nofollow noopener noreferrer">v-model</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-custom-events.html%23sync-%25E4%25BF%25AE%25E9%25A5%25B0%25E7%25AC%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-custom-events.html#sync-%E4%BF%AE%E9%A5%B0%E7%AC%A6" ref="nofollow noopener noreferrer">.sync</a>官方介绍。</p></div>  
</div>
            