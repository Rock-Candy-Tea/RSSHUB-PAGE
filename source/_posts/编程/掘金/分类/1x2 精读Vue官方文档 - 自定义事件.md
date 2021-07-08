
---
title: '1x2 精读Vue官方文档 - 自定义事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4958'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 02:42:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=4958'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<h2 data-id="heading-1">事件名</h2>
<p>”事件“与”组件“或”Prop“不同，它不存在大小写转换的问题，事件的监听与触发都是基于事件名的<strong>全匹配</strong>。但我们仍然推荐使用 <code>kebab-case</code> 风格为事件命名。</p>
<h2 data-id="heading-2">自定义组件的 v-model</h2>
<ul>
<li><code>v-model</code> 本质是一个语法糖，用来实现数据的双向绑定（注意此时组件之间的数据传递不在是单向下行绑定的，因为子组件也可以修改父组件中的数据（事件触发））。</li>
<li><code>v-model</code> 在组件上封装了一个名为 <code>value</code> 的 Prop 与名为 <code>input</code> 的事件。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-comment"><!--v-model 完整形式--></span>
<span class="hljs-tag"><<span class="hljs-name">base-input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"value=$event"</span> /></span>

<span class="hljs-comment"><!--v-model 语法糖--></span>
<span class="hljs-tag"><<span class="hljs-name">base-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是并不是所有组件的值和事件名都是 <code>value</code> 与 <code>input</code>，例如单选按钮、复选框以及自定义组件等。</p>
<p>特别是自定义组件的 <code>v-model</code> 功能需要开发者自己去实现。</p>
<p>一旦我们组件使用了 <code>v-model</code> 指令，Vue 会默认在这个组件上附加 <code>value</code> 属性用来保存值，并绑定一个 <code>input</code> 事件来接收和改变值，所以，利用这一默认的行为，我们可以快速的在自定义组件中实现 <code>v-model</code> 功能：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">"base-checkbox"</span>, &#123;
    <span class="hljs-attr">inheritAttrs</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">value</span>:<span class="hljs-built_in">Boolean</span> <span class="hljs-comment">//v-model 指令会自动绑定一个 value 属性来向组件内部传递值,这个值会在组件外，被对应的 input 事件更新。</span>
    &#125;,
    <span class="hljs-comment">//v-model 指令会自动绑定一个 input 事件来改变 value，并循环向通过 props 向组件内部传递。</span>
    <span class="hljs-attr">template</span>:<span class="hljs-string">`<input type="checkbox" :checked="value" @change="$emit('input', $event.target.value)"`</span> 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，通过组件的 <code>model</code> 配置选项，我们就可以自定义 <code>v-model</code> 的属性与事件名称，实现更大程度的自定义。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">"base-checkbox"</span>, &#123;
    <span class="hljs-attr">inheritAttrs</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">model</span>:&#123;
        <span class="hljs-attr">prop</span>:<span class="hljs-string">'checked'</span>,
        <span class="hljs-attr">event</span>:<span class="hljs-string">'change'</span>
    &#125;,
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">checked</span>:<span class="hljs-built_in">Boolean</span>
    &#125;,
    <span class="hljs-attr">template</span>:<span class="hljs-string">`<input type="checkbox" :checked="checked" @change="$emit('change', $event.target.value)"`</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>虽然 <code>v-model</code> 默认 Prop 是 <code>value</code> 或者基于 <code>model.prop</code> 选项进行自定义的 Prop，但我们仍然需要在组件的 props 进行声明。</p>
</blockquote>
<h2 data-id="heading-3">通过 <code>.sync</code> 修饰符来规范双向数据绑定</h2>
<p>虽然 <code>v-model</code> 提供了强大的双向数据绑定功能，但与之带来的问题就是父子组件的数据流向变得不再清晰，因为子组件也可以修改父组件中的数据，数据传递不再遵循<strong>单向下行绑定</strong>的原则。</p>
<p><code>.sync</code> 修饰符目的就是尽可能的在语意上进行规范,让数据流向更加直观易懂。
它分别从两个方面来规范数据的双向绑定：</p>
<ol>
<li>对子组件内部触发事件的事件名称进行规定，让由内到外的数据流向更清晰（通过事件名即可知道要更新的外部属性是什么）。</li>
<li>组件使用时用已有的 <code>v-bind</code> 指令来替换 <code>v-model</code> 指令，减少心智负担，并让从上到下的数据流向更直观（通过 <code>v-bind</code> 与 <code>.sync</code> 修饰符结合使用，可以很直观的说明当前的属性不仅会传递数据，还会被子组件同步修改）。</li>
</ol>
<blockquote>
<p>推荐以 <strong>update:myPropName</strong> 的格式触发事件。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'base-input'</span>, &#123;
    <span class="hljs-attr">props</span>:[<span class="hljs-string">'value'</span>],
    <span class="hljs-attr">template</span>:<span class="hljs-string">`<input type="text" :value="value" @input="$emit('update:value' $event.target.value)" />`</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父组件中使用时，不使用 <code>.sync</code> 修饰符的完整形式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-input</span> <span class="hljs-attr">v-bind:value</span>=<span class="hljs-string">"value"</span> <span class="hljs-attr">v-on:update:value</span>=<span class="hljs-string">"value=$event"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>.sync</code> 修饰符的方式为：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-input</span> <span class="hljs-attr">:value.sync</span>=<span class="hljs-string">"value"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：通过 <code>.sync</code> 修饰的 <code>v-bind</code> 指令或者 <code>v-model</code> 的值不能和表达式或函数一起使用，它只能对要绑定的 Prop 进行修改。</p>
</blockquote>
<h2 data-id="heading-4"><code>.native</code> 修饰符</h2>
<p><code>v-on</code> 指令的 <code>.native</code> 修饰符可以为组件的根元素监听一个<strong>原生事件</strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-button</span> @<span class="hljs-attr">click.navitve</span>=<span class="hljs-string">"handleClick"</span>></span>click me!<span class="hljs-tag"></<span class="hljs-name">base-button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的是，往往自定义组件内部的 DOM 结构与渲染后呈现的 UI 并不一致。为了解决这个问题，我们可以使用 <code>$listeners</code> 实例属性，来跨 DOM 层级进行事件绑定。</p>
</blockquote>
<h2 data-id="heading-5"><code>$listeners</code> 实例属性</h2>
<p>使用 <code>v-on="$listeners"</code> 的方式我们可以跨 DOM 层级为指定的目标元素绑定所有事件。这位编写高级组件提供了便利与基础。</p>
<blockquote>
<p>注意 <code>$listeners</code> 实例属性中并不会保存带有 <code>.native</code> 修饰符的原生事件。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'base-input'</span>, &#123;
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'label'</span>, <span class="hljs-string">'value'</span>],
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">inputListeners</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> vm = <span class="hljs-built_in">this</span>
      <span class="hljs-comment">// `Object.assign` 将所有的对象合并为一个新对象</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,
        <span class="hljs-comment">// 我们从父级添加所有的监听器</span>
        <span class="hljs-built_in">this</span>.$listeners,
        <span class="hljs-comment">// 然后我们添加自定义监听器，</span>
        <span class="hljs-comment">// 或覆写一些监听器的行为</span>
        &#123;
          <span class="hljs-comment">// 这里确保组件配合 `v-model` 的工作</span>
          <span class="hljs-attr">input</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
            vm.$emit(<span class="hljs-string">'input'</span>, event.target.value)
          &#125;
        &#125;
      )
    &#125;
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <label>
      &#123;&#123; label &#125;&#125;
      <input
        v-bind="$attrs"
        v-bind:value="value"
        v-on="inputListeners"
      >
    </label>
  `</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在 <code><base-input></code> 组件是一个<strong>完全透明的包裹器</strong>了，也就是说它可以完全像一个普通的 <code><input></code> 元素一样使用。</p></div>  
</div>
            