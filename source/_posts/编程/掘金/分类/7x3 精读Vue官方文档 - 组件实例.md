
---
title: '7x3 精读Vue官方文档 - 组件实例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8327'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 02:18:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=8327'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<hr>
<p><strong>组件实例</strong> 的方法与属性。</p>
<p>下面来直观获取一个组件实例—— <code>this</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> that;
<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        that = <span class="hljs-built_in">this</span>;
    &#125;
&#125;);
vm === that; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">组件实例 - 属性</h2>
<h3 data-id="heading-2">$data</h3>
<p>获取当前 Vue 实例的<strong>响应式数据</strong>。 Vue 实例代理了对其 property 的访问，所以你可以直接通过 <code>this</code> 访问。</p>
<blockquote>
<p>如果通过私有前缀添加的受保留的成员属性，依然需要通过 <code>$data.property</code> 方式访问。</p>
</blockquote>
<h3 data-id="heading-3">$props</h3>
<p>获取当前组件接收到的所有 <code>props</code> 。Vue 实例代理了对其 property 的访问，所以你可以直接通过 <code>this</code> 访问。</p>
<h3 data-id="heading-4">$el</h3>
<p>获取当前组件实例的根元素。</p>
<h3 data-id="heading-5">$options</h3>
<p>获取当前 Vue 实例上的自定义选项。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> customFilters = &#123;&#125;;
<span class="hljs-keyword">new</span> Vue(&#123;
  customFilters,
  <span class="hljs-attr">created</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.$options.router;
    <span class="hljs-built_in">this</span>.$options.customFilters
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">$parent</h3>
<p>获取当前组件实例的<strong>父实例</strong>。父实例也可以通过组件的 <code>parent</code> 选项进行手动指定。</p>
<h3 data-id="heading-7">$root</h3>
<p>获取 Vue 应用的根实例。</p>
<h3 data-id="heading-8">$children</h3>
<p>当前实例的直接子组件。需要注意 $children 并不保证顺序，也不是响应式的。</p>
<h3 data-id="heading-9">$slots</h3>
<p>用来访问当前组件接收到的所有插槽内容，值是一个对象，对象成员的 key 便是具名插槽的名称，如果没有指定具名插槽，则默认的插槽名称为 <code>default</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$slots.default; <span class="hljs-comment">//获取默认的插槽内容。</span>
<span class="hljs-built_in">this</span>.$slots.header; <span class="hljs-comment">//获取名称为 header 的插槽内容。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">$scopedSlots</h3>
<p>用来访问当前组件接收到的所有插槽内容, 值是一个对象，对象成员的 key 便是具名插槽的名称，与普通 <code>$slots</code> 不同的是，对象成员的 value 则是一个函数，通过执行这些函数并向其中传参，用来返回实际的插槽内容，而这就是作用域插槽的核心点，如何从组件内部向组件外部传递数据的关键。</p>
<blockquote>
<p>如果没有指定具名插槽，则默认的插槽名称为 <code>default</code>。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$scopedSlots.default(&#123;<span class="hljs-attr">props</span>:<span class="hljs-built_in">this</span>.props&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">$refs</h3>
<p>值是一个对象，保存所有绑定过 <code>ref</code> Attribute 的 DOM 元素对象和组件实例。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"anchor"</span>></span>Anchor<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$refs.anchor;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">$isServer</h3>
<p>当前 Vue 实例是否运行于服务器。</p>
<h3 data-id="heading-13">$attrs</h3>
<p>获取当前组件绑定的所有非 <code>props</code> 的 attribute，值是一个对象。
它可以通过 v-bind="$attrs" 一次性的传入内部组件——这在创建更高层次的组件时非常有用。</p>
<blockquote>
<p>注意，对 <code>class</code> 与 <code>style</code> 并无影响。</p>
</blockquote>
<h3 data-id="heading-14">$listeners</h3>
<p>包含了父作用域中的 (不含 <code>.native</code> 修饰符的) <code>v-on</code> 事件监听器。值是一个对象。
它可以通过 <code>v-on="$listeners"</code> 传入内部组件——在创建更高层次的组件时非常有用。</p>
<h2 data-id="heading-15">组件实例 - 方法</h2>
<h3 data-id="heading-16">$watch()</h3>
<p>现在监听数据变动，除了使用组件的 <code>watch</code> 选项，还可以选择组件实例的 <code>$watch</code> 方法。</p>
<p><code>vm.$watch(expOrFn, callback [,options])</code> 接收三个参数:</p>
<ul>
<li><strong><code>expOrFn</code></strong> : 要监听的Vue实例上的表达式或者是监听一个函数计算结果的变化。</li>
<li><strong><code>callback</code></strong> : 监听变动时触发的回调，它接收两个参数，分别是 <code>newValue</code> 与 <code>oldValue</code>。</li>
<li><strong><code>options</code></strong> : 配置项，可以提供更高级的监听配置，例如 <code>immediate</code> 以及 <code>deep</code> 等，这与组件的 <code>watch</code> 选项没有什么不同。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> unwatch =  vm.$watch(<span class="hljs-string">'a.b.c'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newVal, oldVal</span>) </span>&#123;
  <span class="hljs-comment">// 做点什么</span>
&#125;)

<span class="hljs-comment">// 函数</span>
vm.$watch(
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 表达式 `this.a + this.b` 每次得出一个不同的结果时</span>
    <span class="hljs-comment">// 处理函数都会被调用。</span>
    <span class="hljs-comment">// 这就像监听一个未被定义的计算属性</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a + <span class="hljs-built_in">this</span>.b
  &#125;,
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">newVal, oldVal</span>) </span>&#123;
    <span class="hljs-comment">// 做点什么</span>
  &#125;
)

<span class="hljs-comment">// 之后取消监听</span>
unwatch();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vm.$watch</code> 返回一个取消观察函数，用来停止触发回调：</p>
<p>注意在带有 immediate 选项时，你不能在第一次回调时取消侦听给定的 property。</p>
<p>如果你仍然希望在回调内部调用一个取消侦听的函数，你应该先检查其函数的可用性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> unwatch = vm.$watch(
  <span class="hljs-string">'value'</span>,
  <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    doSomething()
    <span class="hljs-keyword">if</span> (unwatch) &#123;
      unwatch()
    &#125;
  &#125;,
  &#123; <span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span> &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">$set()</h3>
<p>为组件实例的可嵌套响应式对象动态加入响应式成员，并确保组件的视图可以响应式更新。
这是全局 <code>Vue.set</code> 的别名。</p>
<h3 data-id="heading-18">$delete()</h3>
<p>删除组件实例的响应式对象成员。
这是全局 <code>Vue.delete</code> 的别名。</p>
<h2 data-id="heading-19">组件实例 - 事件</h2>
<h3 data-id="heading-20">$on()</h3>
<p>向当前组件实例绑定一个自定义事件，事件回调函数可以接收事件触发时传入的所有事件参数。</p>
<p><code>$on</code> 方法绑定的事件可以由 <code>$emit</code> 触发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> handler = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">msg</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(msg)
&#125;;

vm.$on(<span class="hljs-string">'test'</span>, handler);
vm.$emit(<span class="hljs-string">'test'</span>, <span class="hljs-string">'hi'</span>)
<span class="hljs-comment">// => "hi"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">$once()</h3>
<p>与 <code>$on</code> 使用方式相同，只是通过 <code>$once</code>绑定的自定义事件，只会触发一次，触发后就会被移除。</p>
<h3 data-id="heading-22">$off()</h3>
<p>移除自定义事件。</p>
<pre><code class="hljs language-js copyable" lang="js">vm.$off(); <span class="hljs-comment">//如果没有提供参数，则移除所有的事件监听器；</span>
vm.$off(<span class="hljs-string">'test'</span>); <span class="hljs-comment">//如果只提供了事件，则移除该事件所有的监听器；</span>
vm.$off(<span class="hljs-string">'test'</span>, handler); <span class="hljs-comment">//如果同时提供了事件与回调，则只移除这个回调的监听器。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">$emit()</h3>
<p>触发当前实例上的事件。附加参数都会传给监听器回调。</p>
<h2 data-id="heading-24">组件实例 - 生命周期</h2>
<h3 data-id="heading-25">$mount()</h3>
<p>如果 Vue 实例在实例化时没有收到 el 选项，则它处于“未挂载”状态没有关联的 DOM 元素。可以使用 <code>vm.$mount()</code> 手动地挂载一个未挂载的实例。</p>
<p>这个方法返回实例自身，因而可以链式调用其它实例方法。</p>
<h3 data-id="heading-26">$forceUpdate()</h3>
<p>迫使 Vue 实例重新渲染。</p>
<blockquote>
<p>注意它影响范围只有它自身与其插槽接收的子组件。</p>
</blockquote>
<h3 data-id="heading-27">$nextTick()</h3>
<p>将回调延迟到下次 DOM 更新循环之后执行。它跟全局方法 <code>Vue.nextTick</code> 一样，不同的是回调的 this 自动绑定到调用它的实例上。</p>
<h3 data-id="heading-28">$destory()</h3>
<p>完全销毁一个实例。清理它与其它实例的连接，解绑它的全部指令及事件监听器。</p>
<p>触发 <code>beforeDestroy</code> 和 <code>destroyed</code> 的钩子。</p>
<blockquote>
<p>在大多数场景中你不应该调用这个方法。最好使用 <code>v-if</code> 和 <code>v-for</code> 指令以数据驱动的方式控制子组件的生命周期。</p>
</blockquote></div>  
</div>
            