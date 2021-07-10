
---
title: '1x5 精读Vue官方文档 - 处理边界情况'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2945'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 03:59:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=2945'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<h2 data-id="heading-1">访问元素 & 组件</h2>
<h3 data-id="heading-2">$root</h3>
<p>访问<strong>根组件实例</strong></p>
<h3 data-id="heading-3">$parent</h3>
<p>获取<strong>父组件实例</strong>，支持多次调用，获取连续多层父级的实例。</p>
<h3 data-id="heading-4">ref & $refs</h3>
<p><strong>获取子组件的实例</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">children</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"child"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>获取 DOM 元素的对象引用。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"input"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终，我们可以在组件的 <code>$refs</code> 属性中访问这些 <code>ref</code> 的对应的引用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">mountd</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.$refs.child.input.foucs();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当 <code>ref</code> 和 <code>v-for</code> 一起使用的时候，你得到的 <code>ref</code> 将会是一个包含了对应数据源的这些子组件的数组。</p>
</blockquote>
<h3 data-id="heading-5">依赖注入</h3>
<p>使用 <code>provide</code> 提供依赖，再使用 <code>inject</code> 注入依赖。</p>
<p><strong>Provider</strong></p>
<pre><code class="hljs language-js copyable" lang="js">provide: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">getMapData</span>: <span class="hljs-built_in">this</span>.getData
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Consumer</strong></p>
<pre><code class="hljs language-js copyable" lang="js">inject:[<span class="hljs-string">'getMapData'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这对组件选项必须要一起使用。以允许一个祖先组件向其所有后代组件注入一个依赖，不论组件的层级有多深。</p>
<p><code>provide</code> 的值是一个<strong>对象</strong>或者是返回一个对象的<strong>函数</strong>。对象的 key 便是向子孙组件中注入的依赖。
<code>inject</code> 的值是一个字符串数组，或者是一个对象选项。这些数组元素或者是对象的 key 都是对应的都是 <code>provide</code> 注入的依赖。</p>
<p>最基本的形式：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.extend(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
  <span class="hljs-attr">provide</span>: &#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>,
  &#125;,
&#125;);

Vue.extend(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Son"</span>,
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">"foo"</span>],
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.foo);
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>provide</code> 的值为一个函数，<code>inject</code> 的值是一个对象选项：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.extend(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
  <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>,
    &#125;;
  &#125;,
&#125;);

Vue.extend(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Son"</span>,
  <span class="hljs-attr">inject</span>: &#123;
    <span class="hljs-attr">bar</span>: &#123;
      <span class="hljs-attr">from</span>: <span class="hljs-string">"foo"</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">"new bar"</span>,
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code>inject</code> 的值是一个对象，那么<code>from</code> 便可以指定来源，<code>default</code> 用来设置依赖的默认值。但是当你的依赖默认值不是一个基本类型时，必须要使用一个工厂方法来返回这个值。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">inject</span>: &#123;
    <span class="hljs-attr">foo</span>: &#123;
      <span class="hljs-attr">from</span>: <span class="hljs-string">'bar'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，因为 <code>provide/inject</code> 的初始化优先于 <code>props</code>,<code>data</code> ，所以我们便可以用依赖注入来初始化它们的默认值。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.extend(&#123;
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">"foo"</span>],
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">bar</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.foo,
    &#125;,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">copy_bar</span>: <span class="hljs-built_in">this</span>.foo,
    &#125;;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>依赖注入解决了什么问题？</strong></p>
<ol>
<li>解决了 <code>$parent</code> 无法很好的扩展到更深层级的嵌套组件上。</li>
<li>给任意的后代提供数据或方法，免去了多层的 Prop 传递。</li>
<li>任意的后代也不需要关心 property 是从何处注入。</li>
</ol>
<p><strong>依赖注入的应用场景:</strong></p>
<ol>
<li>编写一个固定组件集，存在一个根组件和多层的子组件，且结构固定。</li>
<li>一个局部的数据中心化。</li>
</ol>
<p><strong>依赖注入的负面影响:</strong></p>
<ol>
<li>注入的数据或方法基于设计的考量不具有响应式的特性。</li>
<li>注入的数据虽然不会被处理为响应式数据，但是并不阻止依赖注入一个本是响应式的数据。</li>
<li>会将应用程序中相关的组件（使用依赖注入的组件）紧密的耦合在一起，使得重构变得比较困难（这是依赖注入的本质所决定的）。</li>
</ol>
<blockquote>
<p>相对于依赖注入的银弹 —— <code>vuex</code>，提供一个第三方独立的数据中心，并具有响应式更新功能。</p>
</blockquote>
<h2 data-id="heading-6">程序化的事件监听器</h2>
<p>程序化的事件监听器是建立在 Vue 系统上的，它区别于浏览器的事件系统（EventTarget API）。
通常我们使用 <code>v-on</code> 在组件上监听事件，使用 <code>$emit()</code> 在组件内触发事件，而 “程序化的事件监听器” 提供了一个可以在组件实例上监听事件的功能。</p>
<ul>
<li><code>$on('eventName', eventHandler)</code> 绑定/侦听一个事件。</li>
<li><code>$off('eventName, eventHandler')</code> 解绑/停止侦听一个事件。</li>
<li><code>$once(eventName, eventHandler)</code> 一次性绑定/监听一个事件。</li>
</ul>
<p>善用 <code>$once</code> 可以提高我们解决组件事件清理的麻烦。</p>
<p><strong>Bad</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 一次性将这个日期选择器附加到一个输入框上</span>
<span class="hljs-comment">// 它会被挂载到 DOM 上。</span>
<span class="hljs-attr">mounted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// Pikaday 是一个第三方日期选择器的库</span>
  <span class="hljs-built_in">this</span>.picker = <span class="hljs-keyword">new</span> Pikaday(&#123;
    <span class="hljs-attr">field</span>: <span class="hljs-built_in">this</span>.$refs.input,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'YYYY-MM-DD'</span>
  &#125;)
&#125;,
<span class="hljs-comment">// 在组件被销毁之前，</span>
<span class="hljs-comment">// 也销毁这个日期选择器。</span>
<span class="hljs-attr">beforeDestroy</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.picker.destroy()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Good</strong></p>
<pre><code class="hljs language-js copyable" lang="js">mounted: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> picker = <span class="hljs-keyword">new</span> Pikaday(&#123;
    <span class="hljs-attr">field</span>: <span class="hljs-built_in">this</span>.$refs.input,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'YYYY-MM-DD'</span>
  &#125;)

  <span class="hljs-built_in">this</span>.$once(<span class="hljs-string">'hook:beforeDestroy'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    picker.destroy()
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们还可以把这些操作封装成方法，便于多次执行相同的操作。</p>
</blockquote>
<h2 data-id="heading-7">递归组件</h2>
<p>所谓“递归”就是自己调自己，同理组件递归就是组件不断的调用自身。</p>
<p><strong>递归组件的入口：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">x-menu</span> <span class="hljs-attr">:menus</span>=<span class="hljs-string">"menus"</span>></span><span class="hljs-tag"></<span class="hljs-name">x-menu</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>递归组件的定义：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'x-menu'</span>, &#123;
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">menus</span>:&#123;
            <span class="hljs-attr">requried</span>:<span class="hljs-literal">true</span>,
            <span class="hljs-attr">type</span>:<span class="hljs-built_in">Array</span>
        &#125;
    &#125;,
    <span class="hljs-attr">template</span>:<span class="hljs-string">`
        <ul>
            <li v-for="menu in menus" :key="menu.key">
                <div>&#123;&#123; menu.name &#125;&#125;</div>
                <!--核心所在-->
                <x-menus v-if="menu.children"></x-menus>
            </li>
        </ul>
    `</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">循环引用</h2>
<p>与递归组件不同的是，递归是通过不断调用自己来实现所需的功能。而循环引用只会存在两个组件之间，A  组件使用了 B 组件，B 组件也使用了 A 组件。</p>
<blockquote>
<p>如果你是通过 <code>Vue.component</code> 注册的全局组件，则不存在此种情况。</p>
</blockquote>
<p>通常这种问题只会出现在使用模块化系统来引入具有相互引用关系的组件。</p>
<p>解决的办法有两种：</p>
<p><strong>1. 手动注册其中的一个组件</strong></p>
<pre><code class="hljs language-js copyable" lang="js">beforeCreate: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.$options.components.ComponetB = <span class="hljs-keyword">import</span>(<span class="hljs-string">'./components/componentB'</span>).default;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 使用异步组件</strong></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">components</span>:&#123;
        <span class="hljs-string">'component-b'</span>: <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">'./components/componentB'</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">模板定义的替代品</h2>
<p>我们更多的推荐使用单文件组件 SFC 的方式定义模板或者在 <code>template</code> 属性中编写字符串模板，并不建议将组件的模板与逻辑相分离。</p>
<h3 data-id="heading-10">内联模板</h3>
<p>当 <code>inline-template</code> 这个特殊的 attribute 出现在一个子组件上时，这个组件将会使用其里面的内容作为模板，而不是将其作为被分发的内容（不在是理解中 slot 的性质）。这使得模板的撰写工作更加灵活。</p>
<p><strong>内联模板</strong>需要定义在 Vue 所属的 DOM 元素内。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">my-component</span> <span class="hljs-attr">inline-template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>These are compiled as the component's own template.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Not parent's transclusion content.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其实就是自定义组件起始与结束标签的内容将会作为该自定义组件的模板，因此不会传递给 <code><slot></code> 元素，这会导致组件的模板与逻辑分离，通常不建议使用。</p>
</blockquote>
<h3 data-id="heading-11">X-Template</h3>
<p>与内联模板相比就是使用具有特殊 <code>type</code> 值与 <code>id</code> 属性的 <code><script></code> 标签来存储模板内容。</p>
<p><strong>x-template</strong> 需要定义在 Vue 所属的 DOM 元素外。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/x-template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"hello-world-template"</span>></span><span class="handlebars"><span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello hello hello<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>id</code> 的作用就是将模板内容与模板逻辑进行连接的凭据。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'hello-world'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'#hello-world-template'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>X-Template</code> 的方式也会导致组件的模板与逻辑相分离，所以也不建议使用。</p>
</blockquote>
<h2 data-id="heading-12">强制更新</h2>
<p>调用 <code>this.$forceUpdate()</code> 可以强制更新组件。</p>
<h2 data-id="heading-13">通过 <code>v-once</code> 创建低开销的静态组件</h2>
<p>当组件包含了大量静态内容时。我们可以在根元素上添加 <code>v-once</code> attribute 以确保这些内容只计算一次然后缓存起来，提供组件的渲染速度。</p>
<pre><code class="hljs language-html copyable" lang="html">Vue.component('terms-of-service', &#123;
  template: `
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-once</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Terms of Service<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      ... a lot of static content ...
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  `
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            