
---
title: '1x3 精读Vue官方文档 -  插槽'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448a132be4b2486086f5a508b14215ae~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 19:59:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448a132be4b2486086f5a508b14215ae~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<p>插槽 <code>Slot</code> 其设计灵感源自 <code>Web Components 规范草案</code>，将 <code><slot></code> 元素作为承载分发内容的出口。</p>
<p>关于内容分发，我们可以类比于 <code>$attrs</code> 实例属性分发所有的 Attribute；<code>$listeners</code> 实例属性可以分发所有的事件一样。</p>
<p><strong>插槽</strong>作用在组件的内部，用来接收自定义元素（自定义组件）开始标签与结束标签之间的内容，然后在组件内容指定位置进行输出，如果自定义组件的模板不含有 <code><slot></code> 元素，那么自定义元素的内容将会被抛弃。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'custom-element'</span>, &#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<p></p>'</span>
&#125;);
Vue.component(<span class="hljs-string">'custom-element-2'</span>, &#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<p><slot></slot></p>'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- This is custom element content 并不会显示 --></span>
<span class="hljs-tag"><<span class="hljs-name">custom-element</span>></span>This is custom element content<span class="hljs-tag"></<span class="hljs-name">custom-element</span>></span>

<span class="hljs-comment"><!-- 正常显示 --></span>
<span class="hljs-tag"><<span class="hljs-name">custom-element-2</span>></span>This is custom element content<span class="hljs-tag"></<span class="hljs-name">custom-element-2</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插槽可以接受任何类型的内容，也包括另一个组件。</p>
<h2 data-id="heading-1">编译作用域</h2>
<blockquote>
<p>父级模板里的所有内容都是在父级作用域中编译的；子模板里的所有内容都是在子作用域中编译的。</p>
</blockquote>
<p>插槽的内容定义在父级，编译在父级，属于父级的一部分，编译后的内容会传入到插槽元素所在的组件中由该组件执行后展示，遵循于 JavaScript 词法作用域的规定，插槽内容只能访问父级作用域里面的数据，而不能访问插槽元素所在子组件内的数据。</p>
<h2 data-id="heading-2">后备内容</h2>
<p><strong>插槽</strong>的默认值会在插槽没有接收到任何内容时默认被渲染。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'base-button'</span>, &#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<slot>button</slot>'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>父级会将内容放置在自定义元素的开始与结束标签之间来传递值，然后在自定义组件内部中通过 <code><slot></code> 元素来分发内容。</p>
</blockquote>
<h2 data-id="heading-3">具名插槽</h2>
<p>当需要多个插槽来分发内容时，可以为 <code><slot></code> 元素命名，用来锚定内容输出所对应的插槽。</p>
<blockquote>
<p>顾名思义，“具名插槽”就是存在多个插槽时为插槽命名以作区别。</p>
</blockquote>
<p>使用 <code>name</code> 属性为多个插槽命名，一个不带 <code>name</code> 的出口会带有隐含的名字“default”。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"base-layout-template"</span>></span><span class="handlebars"><span class="xml">
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"other"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
Vue.component(<span class="hljs-string">'base-layout'</span>, &#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'#base-layout-template'</span>,
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际使用时我们会通过 <code><template></code> 元素进行分组，每个 <code><template></code> 元素上绑定一个 <code>v-slot</code> 指令，并以<strong>插槽名称</strong>作为指令参数，来为锚定的具名插槽提供一块完整的内容输出。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-layout</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>></span>Header & Menu & Nav<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:footer</span>></span>Footer<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">base-layout</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>图示：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448a132be4b2486086f5a508b14215ae~tplv-k3u1fbpfcp-watermark.image" alt="slot.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">作用域插槽</h2>
<p>从插槽的编译作用域可知，定义在父组件作用域中的插槽内容是无法获取插槽元素 <code><slot></code> 所在组件内的数据。具有作用域的插槽就是为了打通插槽由内到外的数据传递，让插槽内容也能访问插槽元素 <code><slot></code> 所在组件内的数据。</p>
<p>步骤如下：</p>
<ol>
<li>使用 <code>v-bind</code> 指令来为当前组件内的 <code><slot></code> 元素绑定插槽 Prop，这个 Prop 编译后就会作为参数（组件内的数据）传递到作用域插槽中。</li>
<li>在父作用域的插槽内容 <code><template></code> 元素上使用 <code>v-slot</code> 指令并以插槽名称作为指令参数来接收上一步 <code><slot></code> 元素所绑定的插槽 Prop，从而实现在插槽中获取插槽所在组件内的数据。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'mouse-move'</span>, &#123;
    <span class="hljs-attr">template</span>:<span class="hljs-string">'<slot name="default" v-bind:pos="&#123;x:xAxis, y:yAxis&#125;"></slot>,
    data()&#123;
        return &#123;
            xAxis:0,
            yAxis:0
        &#125;
    &#125;,
    mounted()&#123;
        window.addEventListener('</span>mousemove<span class="hljs-string">',e=>&#123;
            this.xAxis = e.clientX;
            this.yAxis = e.clientY;
        &#125;,&#123;passive:true&#125;);
    &#125;
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">mouse-move</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:default</span>=<span class="hljs-string">"slotProps"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>xAxis:&#123;&#123;slotProps.x&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>yAxis:&#123;&#123;slotProps.y&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">mouse-move</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果存在多个具名插槽，分别单独接收每个插槽绑定的 Prop 即可，默认的插槽名称为 <code>default</code> 或者直接为空。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">slot-example</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"slotProps"</span>></span>&#123;&#123;slotProps.value&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:other</span>=<span class="hljs-string">"otherSlotProps"</span>></span>        &#123;&#123;otherSlotProps.value&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">独占默认插槽的写法</h3>
<p>若组件只提供了一个默认插槽，那么便可以直接将 <code>v-slot=”slotProps“</code> 指令添加在组件的自定义元素上。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">slot-example</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"slotProps"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等价于</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">slot-example</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:default</span>=<span class="hljs-string">"slotProps"</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以实现省去一个 <code><template></code> 元素的效果。</p>
<p>如果组件内部存在多个插槽，那么插槽内容必须要严格使用 <code><template></code> 元素并添加 <code>v-slot:[slotName]="&#123;&#123;slotName&#125;&#125;SlotProps"</code> 方式锚定需要输出的目标具名插槽。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">slot-example</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"slotProps"</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:other</span>=<span class="hljs-string">"otherSlotProps"</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意默认插槽的名称为 <code>default</code>，可省去不写。</p>
</blockquote>
<h3 data-id="heading-6">解构插槽</h3>
<p>插槽内容是在父级中编译，编译后的插槽内容会被包裹在一个拥有单个参数的函数里，再传递到子组件中，由子组件执行，当子组件执行时会同插槽 Prop 的值一同传入。</p>
<p>Vue 会将 <code><slot></code> 元素上绑定的所有 Props 以键值对的形式组合在 <code>slotProps</code> 对象中，然后作为参数传递给包裹插槽内容的方法里，这意味着，我们可以通过 ES6 的解构语法在模板中以更简洁的方式取得插槽 Prop 中的值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">slot-example</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123;x, y&#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">动态插槽名称</h2>
<p>具名插槽的名称可以是一个动态的值，这与动态指令参数的效果相同。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--Definition--></span>
<span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"slotName"</span> <span class="hljs-attr">:values</span>=<span class="hljs-string">"vals"</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>

<span class="hljs-comment"><!--Usage--></span>
<span class="hljs-tag"><<span class="hljs-name">slot-example</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:</span>[<span class="hljs-attr">slotName</span>]=<span class="hljs-string">"slotProps"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">slot-example</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">具名插槽简写</h2>
<p>与 <code>v-on</code>，<code>v-bind</code> 指令一样，我们可以使用 <code>#</code> 来缩写 <code>v-slot</code> 指令</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">default</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">other</span>=<span class="hljs-string">"otherSlotProps"</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>缩写 <code>v-slot</code> 指令时必须具有指令参数。</p>
</blockquote>
<h2 data-id="heading-9">其它应用</h2>
<p>当我们进行<strong>可复用组件设计时</strong>，既想基于子组件绑定的<strong>插槽Prop</strong>来渲染出不同的内容，又想让父组件也可以自定义部份布局，那么使用”作用域插槽“的模式将会很有效果。</p>
<p>下面是一些基于“作用域插槽”这思想实现的可复用的 Vue 组件。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fposva%2Fvue-promised" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/posva/vue-promised" ref="nofollow noopener noreferrer">github.com/posva/vue-p…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLinusBorg%2Fportal-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LinusBorg/portal-vue" ref="nofollow noopener noreferrer">github.com/LinusBorg/p…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FAkryum%2Fvue-virtual-scroller" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Akryum/vue-virtual-scroller" ref="nofollow noopener noreferrer">github.com/Akryum/vue-…</a></li>
</ul>
<h2 data-id="heading-10">总结</h2>
<p>使用 <code><slot></code> 元素的 <code>name</code> 属性来定义一个具名插槽，其中 name 的值可缺省，默认为 default ; 插槽的 <code><slot></code> 元素还可以通过 <code>v-bind</code> 指令将插槽所在组件内的数据绑定到 Prop 中，在插槽内容被执行时作为参数传递进入。</p>
<p>在父作用域中使用具有插槽元素的组件时，便可以通过为其绑定 <code>v-slot:[name]="slotProps"</code> 指令来接收对应具名插槽绑定的 Prop。</p>
<blockquote>
<ul>
<li><code>#</code> 可用于替代 <code>v-slot</code> 指令进行缩写，并且必须含有指令参数。</li>
<li>插槽默认名称为 <code>default</code>，可省略不写。</li>
</ul>
</blockquote></div>  
</div>
            