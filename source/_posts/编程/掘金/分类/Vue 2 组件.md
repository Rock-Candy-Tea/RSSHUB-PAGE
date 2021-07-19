
---
title: 'Vue 2 组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9885'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 06:16:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=9885'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">系列文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6985353677519192078" target="_blank" title="https://juejin.cn/post/6985353677519192078">Vue 2 基础</a></li>
<li><a href="https://juejin.cn/post/6986269594516193293" target="_blank" title="https://juejin.cn/post/6986269594516193293">Vue 2 组件</a></li>
<li><a href="https://juejin.cn/post/6986271549875552287" target="_blank" title="https://juejin.cn/post/6986271549875552287">Vue 2 动效</a></li>
<li><a href="https://juejin.cn/post/6986272436761133070" target="_blank" title="https://juejin.cn/post/6986272436761133070">Vue 2 插件</a></li>
</ul>
<h2 data-id="heading-1">参考</h2>
<ul>
<li>Youtube 频道 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCEL8871qFEakpqYpwBSjHNA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/channel/UCEL8871qFEakpqYpwBSjHNA" ref="nofollow noopener noreferrer">Alex 宅幹嘛</a> 的《Re Vue 重頭說起》系列教程</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/" ref="nofollow noopener noreferrer">Vue 2 官方文档</a></li>
</ul>
<p>🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbenbinbin.github.io%2Fblog-web%2Ffrontend%2FJS-Framework%2FVue2%2F%25E7%25BB%2584%25E4%25BB%25B6.html" target="_blank" rel="nofollow noopener noreferrer" title="https://benbinbin.github.io/blog-web/frontend/JS-Framework/Vue2/%E7%BB%84%E4%BB%B6.html" ref="nofollow noopener noreferrer">原文</a>内嵌了 Youtube 播放器可以直接播放片段，而本文则可以点击 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyoutube.com%2Fplaylist%3Flist%3DPLEfh-m_KG4daEhioHKZqrkGXAedXIQ2Cn" target="_blank" rel="nofollow noopener noreferrer" title="https://youtube.com/playlist?list=PLEfh-m_KG4daEhioHKZqrkGXAedXIQ2Cn" ref="nofollow noopener noreferrer">🎬</a> 图标可以打开相应的 Youtube 视频片段的网址。</p>
<hr>
<p>Vue 中的组件是页面中的一部分，通过层层拼装和复用，最终形成了一个完整的页面。</p>
<p>使用组件的一般场景：</p>
<ul>
<li>代码复用</li>
<li>功能分类管理（每个组件实现一个功能）</li>
</ul>
<p>组件必须先注册以便 Vue 应用能够识别，有两种组件的注册类型：</p>
<ul>
<li>全局注册</li>
<li>局部注册</li>
</ul>
<p>类似标签一样，通过组件名称来引用组件 <code><component-name></code>，💡 由于 HTML 不支持大小写，所以在 name 使用驼峰式命名法时，<strong>在引用组件写到 HTML 中时需要改为采用连字号</strong>，因此<strong>组件名称建议字母全小写，且对于多个单词组成的名字使用连字符号 <code>-</code> 分隔</strong></p>
<p>💡 组件的 <strong>data 选项必须是函数</strong>，从中 <code>return</code> 对象</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'myComponent'</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'Ben'</span>
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">全局组件</h2>
<p>使用 Vue 原型 prototype 上的方法 <code>Vue.component()</code> 注册一个全局组件，第一个参数 <code>name</code> 是组件名称，第二个参数是一个对象包含组件相关的选项</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'name'</span>, &#123;
  options,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`...`</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️ <em>需要在 <code>new Vue(&#123;&#125;)</code> <strong>之前</strong>进行全局组件的注册</em>，之后它可以在任何地方（根组件或其他子组件的模板中）使用。</p>
<p>💡 如果有大量基础组件，同时使用 webpack 工具，可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2Fv2%2Fguide%2Fcomponents-registration.html%23Automatic-Global-Registration-of-Base-Components" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.org/v2/guide/components-registration.html#Automatic-Global-Registration-of-Base-Components" ref="nofollow noopener noreferrer">入口文件</a>进行配置，<strong>使用 <code>require.context</code> 实现自动引入并进行全局注册这些组件</strong>。</p>
<h2 data-id="heading-3">局部组件</h2>
<p>通过一个普通的 JavaScript 对象来定义组件（提供组件的 options），然后在 Vue 实例的 <code>components</code> 选项中进行注册，之后它只能在该父级组件内使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ComponentA = &#123; <span class="hljs-comment">/* ... */</span> &#125;
<span class="hljs-keyword">const</span> ComponentB = &#123; <span class="hljs-comment">/* ... */</span> &#125;
<span class="hljs-keyword">const</span> ComponentC = &#123; <span class="hljs-comment">/* ... */</span> &#125;

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-string">'component-a'</span>: ComponentA,
    <span class="hljs-string">'component-b'</span>: ComponentB
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D1177%26end%3D1821%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=1177&end=1821&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 全局组件虽然可以在整个项目的所有其他组件（包括自己）中都可用，但是这可能造成构建项目时体积增大，用户下载 JavaScript 的无谓增加，因此不能滥用全局组件，视情况而定，如果组件自在特定父级中使用，应该将其注册为局部组件。</p>
<h2 data-id="heading-4">动态组件</h2>
<p>基于标签 <code><component></code> 的 <code>is</code> 属性值（组件名），动态在不同组件之间进行切换</p>
<h2 data-id="heading-5">组件间数据传递</h2>
<ul>
<li>父组件将需要传递的数据绑定到子组件的属性上，子组件内部通过 props 接收。</li>
<li>子组件可以通过抛出事件 <code>$emit(eventName, value)</code> 同时传递数据，父组件监听事件并接收数据</li>
</ul>
<h3 data-id="heading-6">props</h3>
<p>props 用于接收父组件传递的数据，需要在子组件的选项 <code>props</code> 中预先设置会有哪些 prop，可以以<strong>字符串数组</strong>形式列出，也可以以<strong>对象</strong>形式列出（可指定 prop 接收的数据类型、默认值、是否必须、验证条件等）。</p>
<p>需要注意以下几点：</p>
<ul>
<li>如果在父组件中传入的数据是非字符串的，需要<strong>通过绑定 <code>v-bind:propName</code> 的方式来传递</strong>（即使传递纯数字这一类的静态值）；否则<strong>直接传递数据都会转换为字符串</strong>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D3884%26end%3D4176%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=3884&end=4176&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 如果 prop 是 Boolean 类型，但在使用组件中没有设置该 prop 时，则实例化后该组件的这个 prop 预设为 <code>false</code>；而使用组件时，设置了该 prop 但没有提供 true/false 值（no value 的情况），就会设置为 <code>true</code>。由于布尔类型不是字符串，正确传递方式是使用 <code>v-bind</code> 来传递非字符串的数据</li>
</ul>
<p>如果希望将一个对象的所有属性「拆分」为多个 prop 分别传入，可以使用不带参数的 <code>v-bind</code>（即 <code>v-bind="obj"</code>，而非 <code>v-bind:propName="obj"</code>），<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D4633%26end%3D4896%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=4633&end=4896&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 所以可以将大量的 prop 包装进一个对象，一次绑定到组件上</p>
<p>可以对 prop 进行限制，确保传递进来的值符合要求。有多个属性可以进行设置</p>
<pre><code class="copyable">// ...
props: &#123;
  propA: &#123;
    type: String,
    required: true,
    default: 'abc',
    validator: func()   // 自定义验证函数，返回 true/false
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️ prop 会在一个组件实例创建之前进行验证，所以该组件的 <code>data</code> 或 <code>computed</code> 数据在 <code>validator</code> 验证函数中无法进行访问</p>
<h3 data-id="heading-7">emit</h3>
<p>当组件需要修改父层控管的数据（这些数据通过 props 传递进来）时，基于<strong>单向数据流原则</strong>不能在组件内进行修改，而是需要通过 <code>$emit('eventName', value)</code> 向外抛出自定义的事件，通知父层进行数据修改，其中 <code>value</code> 一般是向外传递的需要变动的数据。</p>
<p>💡 <strong>自定义事件名推荐使用 kebab-case 方式</strong>（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fdw2oFaLu5II%3Fstart%3D352%26end%3D572%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/dw2oFaLu5II?start=352&end=572&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 小写单词之间用连字符 <code>-</code> 连接，因为与组件和 prop 名称不同，Vue 不会对事件名进行任何大小写转换），以便于 HTML 正确识别</p>
<p>Vue 对于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2Fv2%2Fguide%2Fcomponents-custom-events.html%23Customizing-Component-v-model" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.org/v2/guide/components-custom-events.html#Customizing-Component-v-model" ref="nofollow noopener noreferrer">具有表单元素 <code><input></code> 的输入型组件</a>，支持使用 <code>v-model</code> 实现类似「双向绑定」的效果。<strong>但在该组件内部需要进行 <code>input</code> 事件监听，并手动 <code>$emit('change'， $event.target.value)</code> 抛出该事件和用户输入的数据，让变量数据的修改仍在父层完成</strong>。</p>
<ul>
<li>在外部（引用该组件时，在组件的标签上）通过指令 <code>v-model</code> 双向绑定需要同步的变量，它的数据作为 prop 传递到组件内（<strong>因此记得在组件内部需要在 <code>props</code> 选项里声明 <code>value</code> 作为 prop</strong>），作为子组件内部表单元素的 <code>value</code> 属性的值</li>
<li>在组件内使用指令 <code>v-bind</code> 将表单元素表单元素的 <code>value</code> 属性绑定到以上声明的 prop 变量上，即 <code>v-bind：value="value"</code>（这样就可以将外部传进来的值作为表单的值，实现与外部数据的「同步」）</li>
<li>在组件内使用指令 <code>v-on</code> 监听表单元素 <code>input</code> 输入事件，并通过抛出相同的事件 <code>$emit('input', $event.target.value)</code> 向外传递相应的数据，然后外部通过指令 <code>v-model</code> 绑定的变量就会基于抛出的数据进行改变 <strong>（即数据的修改的操作还是在父层完成）</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// conpoment</span>
Vue.component(<span class="hljs-string">'base-checkbox'</span>, &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'value'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <input
      type="text"
      v-bind:value="value"
      v-on:change="$emit('input', $event.target.value)"
    >
  `</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"inputText"</span>></span><span class="hljs-tag"></<span class="hljs-name">base-input</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过遵守这种设置在使用输入型的组件时，<strong>仅需简单地以 <code>v-model</code> 的方式</strong>，方便地实现数据从父组件传递给子组件，并将用户输入改动 <code>$emit</code> 给父组件进行修改，实现类似「双向绑定」的效果。</p>
<p>💡 如果输入型组件需要绑定的 <code>prop</code> 名称不是 <code>value</code>，且监听的事件不是 <code>input</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fdw2oFaLu5II%3Fstart%3D733%26end%3D1800%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/dw2oFaLu5II?start=733&end=1800&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 可以<strong>在组件中选项 <code>model</code> 进行配置</strong>，例如表单类型为 <code>checkbox</code> 时，需要绑定的是属性是 <code>checked</code>，监听的事件是 <code>change</code></p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'base-checkbox'</span>, &#123;
  <span class="hljs-attr">model</span>: &#123;
    <span class="hljs-attr">prop</span>: <span class="hljs-string">'checked'</span>,
    <span class="hljs-attr">event</span>: <span class="hljs-string">'change'</span>
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">checked</span>: <span class="hljs-built_in">Boolean</span>
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <input
      type="checkbox"
      v-bind:checked="checked"
      v-on:change="$emit('change', $event.target.checked)"
    >
  `</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">base-checkbox</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"lovingVue"</span>></span><span class="hljs-tag"></<span class="hljs-name">base-checkbox</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>lovingVue</code> 的值将会传入这个名为 <code>checked</code> 的 prop。同时当 <code><base-checkbox></code> 触发一个 <code>change</code> 事件并附带一个新的值的时候，这个 <code>lovingVue</code> 的 property 将会被更新。</p>
<h3 data-id="heading-8">sync</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fdw2oFaLu5II%3Fstart%3D2235%26end%3D3261%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/dw2oFaLu5II?start=2235&end=3261&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> Vue 还为一般的组件<strong>提供 <code>.sync</code> 修饰符，和一个以特定前缀 <code>update</code> 命名的事件，让 prop 变量实现类似于「双向绑定」的效果</strong>，更方便地从子组件中「修改」父层传入的数据。</p>
<p>在使用组件设置 prop 时，如果在绑定变量时 <code>v-bind:propName.sync="variable"</code> 添加 <code>.sync</code> 修饰符，<strong>就可以省略在父层设置监听事件和回调函数这一步</strong>，Vue 会自动监听子组件抛出的以特殊形式命名的事件<code>this.$emit('update:propName', newValue)</code>（<strong>事件以特定模式 <code>update:propName</code> 命名</strong>)，然后在父层进行 prop 绑定的变量的数据更新。</p>
<p>💡 而且支持以 <code>v-bind.sync="obj"</code> 的形式同时设置多个具有「双向绑定」效果的 prop，其中对象 obj 的每一个 property 都作为一个独立的 prop 传进去，然后可以在组件内部使用 <code>this.$emit('update:propName', newValue)</code> 抛出事件来更新数据。</p>
<h2 data-id="heading-9">非 prop 属性</h2>
<p>非 prop 的 attribute是指未在组件的 <code>props</code> 选项中显式声明的，但在引用组件时传递给子组件的 attribute，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D6820%26end%3D6973%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=6820&end=6973&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 这些 attribute 会默认被添加到这个组件的<strong>根元素</strong>上（即在组件的模板中作为容器的第一层的 <code><tag></code> 上。</p>
<p>如果组件的根节点 <code><tag></code> 上已有预设了相应的 attribute，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D7576%26end%3D7810%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=7576&end=7810&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 该属性就会被新传入的值<strong>覆盖</strong>；如果这个 attribute 是 <code>class</code> 或 <code>style</code>，会将它们与组件根元素上的 <code>class</code> 或 <code>style</code> <strong>合并</strong>。</p>
<p>💡 如果希望 attribute 添加到组件的特定元素上，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FQ5xKDRdr0x8%3Fstart%3D6973%26end%3D7506%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Q5xKDRdr0x8?start=6973&end=7506&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 可以设定组件的选项 <code>inheritAttrs: false</code>，然后将特殊的变量 <code>$attrs</code>（这是一个包含所有非 prop 的 attribute 的对象）绑定 <code>v-bind="$attrs"</code> 到指定的节点上，<strong>但 <code>class</code> 和 <code>style</code> 不能指定到组件的非根元素上</strong>。也可指定某个 attribute 绑定 <code>:attributeName="$attrs.propertyName"</code></p>
<h2 data-id="heading-10">监听事件</h2>
<p>有时候希望在使用组件时才添加事件监听，这样就会将事件监听添加到组件的根元素上，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fdw2oFaLu5II%3Fstart%3D1801%26end%3D1938%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/dw2oFaLu5II?start=1801&end=1938&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> <strong>但此时监听的事件都被认为是自定义事件（即监听从子组件手动 <code>$emit</code> 出来的事件）</strong> ，如果希望监听 JS 预设的原生事件，如 <code>click</code>、<code>`focus</code> 等，需要在其后添加 <code>.native</code> 修饰符。</p>
<p>如果希望在引用组件时添加事件监听，<strong>但又不是添加到组件的根元素上</strong>，而是添加到组件内的特定元素上，可以在组件中配置选项 <code>inheritAttrs: false</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fdw2oFaLu5II%3Fstart%3D1944%26end%3D2224%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/dw2oFaLu5II?start=1944&end=2224&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 并在模板非根元素的标签上使用 <code>v-on="$listener"</code>，这样在使用组件时才设置的事件监听器，都指向该特定节点上。</p>
<p>Vue 提供了一个 <code>$listeners</code> property，它是一个对象，里面包含了作用在这个组件上的所有监听器。例如：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">focus</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123; <span class="hljs-comment">/* ... */</span> &#125;
  <span class="hljs-attr">input</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123; <span class="hljs-comment">/* ... */</span> &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2Fv2%2Fguide%2Fcomponents-custom-events.html%23Binding-Native-Events-to-Components" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.org/v2/guide/components-custom-events.html#Binding-Native-Events-to-Components" ref="nofollow noopener noreferrer">官方的例子</a>实现了将外部添加的事件监听器（通过 <code>$listeners</code> 获取），和内部为了配合 <code>v-model</code> 设置的 <code>input</code> 事件监听器合并，再一起绑定到组件的 <code><input></code> 元素上。</p>
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
<h2 data-id="heading-11">插槽</h2>
<p>插槽 slot 是 Vue 实现的一套<strong>内容分发</strong>的 API，一般用于组件作为布局 layout 使用。</p>
<p>在子组件的模板中使用标签 <code><slot></code> 作为「占位符」预留位置，在使用组件时，内嵌在组件 <code><component-name>content</component-name></code> 中的内容 <code>content</code>（插入的内容可以是 HTML，也包含模板代码或其他组件） 会替代 <code><slot></code> 标签，渲染出来。</p>
<p>💡 可以在组件模板的插槽中设置<strong>默认内容</strong>，但是只要在使用组件时，有提供插入内容就会替换默认内容。如果组件定义模板时没有包含一个 <code><slot></code> 元素，则使用该组件时，即使组件起始标签和结束标签之间有内容，都会被抛弃。</p>
<h3 data-id="heading-12">具名插槽</h3>
<p>可以在组件定义的模板中设置多个插槽，并为它们设置属性 <code>name</code>，它们称为具名插槽 <code><slot name="slotName"></slot></code>。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTn1X7jJNoL4%3Fstart%3D1644%26end%3D3282%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Tn1X7jJNoL4?start=1644&end=3282&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 在使用组件时，使用 <code><template></code> 元素作为容器（该标签本身不会被渲染到页面上），并以带<strong>参数</strong>的指令 <code>v-slot:slotName</code> 的形式 <code><template v-slot:slotName>content</template></code> 将提供的内容分发到相应名称的插槽。</p>
<p>💡 和其他指令一样，<code>v-slot:slotName</code> 指令有缩写形式 <code>#slotName</code></p>
<p>当模板中存在多个具名插槽 <code><slot></code> 时，<strong>可以有一个不具名插槽，它作为默认插槽（实际上带有隐含的名字 <code>v-slot:default</code>）</strong> 。在使用组件时，任何没有被包裹在带有指令 <code>v-slot:slotName</code> 的 <code><template></code> 中的内容都会被视为默认插槽的内容。</p>
<h3 data-id="heading-13">作用域插槽</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTn1X7jJNoL4%3Fstart%3D1087%26end%3D1389%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Tn1X7jJNoL4?start=1087&end=1389&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 由于使用组件时，是在父层指定插入的内容，所以<strong>这些内容现在父级作用域进行编译，它们只能访问父层的数据</strong>。</p>
<p>如果希望可以访问组件中才有的数据，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTn1X7jJNoL4%3Fstart%3D3356%26end%3D3976%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/Tn1X7jJNoL4?start=3356&end=3976&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 需要使用作用域插槽 <code><slot v-bind:variable="value"></code>，即在组件的插槽中预先将允许访问的数据绑定到属性上，这些绑定到 <code><slot></code> 的 attribute 称为<strong>插槽 props</strong></p>
<p>然后在使用组件时，可以为指令 <code>v-slot</code> 设置<strong>值</strong> <code><template v-slot:slotName="objName"></code>，该值是一个对象，它包含所有在组件内绑定的插槽 props，然后就可以通过 <code>objName.property</code> 的方式来读取子作用域才有的数据。除了使用 <code>objName</code>「接收」内层抛出的所有 props，还可以使用 ES6 <strong>解构</strong>的方式直接 <code><template v-slot:slotName="&#123; property &#125;"></code> 获取单个 <code>property</code>，便于后面调用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 子组件 current-user 的模板 --></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">v-bind:user</span>=<span class="hljs-string">"user"</span>></span>
    &#123;&#123; user.lastName &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 使用组件 current-user --></span>
<span class="hljs-tag"><<span class="hljs-name">current-user</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:default</span>=<span class="hljs-string">"slotProps"</span>></span>
    &#123;&#123; slotProps.user.firstName &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">current-user</span>></span>

<span class="hljs-comment"><!-- 解构的方式接收特定的 prop --></span>
<span class="hljs-tag"><<span class="hljs-name">current-user</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; user &#125;"</span>></span>
  &#123;&#123; user.firstName &#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">current-user</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 <strong>如果组件只有默认插槽时，组件的标签可以被当作插槽的模板来使用</strong>，即可以省略 <code><template></code> 标签，直接在组件标签上设置 <code>v-slot="objName"</code> 来接收内层抛出的 props</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">current-user</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"slotProps"</span>></span>
  &#123;&#123; slotProps.user.firstName &#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">current-user</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">混入</h2>
<p>混入 mixin 是指将组件选项中可复用的部分「抽取」出来成为一个对象（可以包含 <code>computed</code>、<code>method</code>、<code>watch</code> 等），以供其他组件复用。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FXJKXQjihqpo%3Fstart%3D437%26end%3D866%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/XJKXQjihqpo?start=437&end=866&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 然后在组件（包括根组件）的选项 <code>mixin</code> 中使用该对象即可复用。</p>
<p>在组件或 Vue 实例中添加选项 <code>mixins: [mixinName]</code> 引入预设的选项，它们将被「混合」进入该组件本身的选项。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个混入对象</span>
<span class="hljs-keyword">var</span> myMixin = &#123;
  <span class="hljs-attr">created</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.hello()
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-attr">hello</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello from mixin!'</span>)
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 定义一个使用混入对象的组件</span>
<span class="hljs-keyword">var</span> Component = Vue.extend(&#123;
  <span class="hljs-attr">mixins</span>: [myMixin]
&#125;)

<span class="hljs-keyword">var</span> component = <span class="hljs-keyword">new</span> Component() <span class="hljs-comment">// => "hello from mixin!"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 当组件和混入对象含<strong>有同名选项</strong>时，这些选项将以恰当的方式进行 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FXJKXQjihqpo%3Fstart%3D867%26end%3D1906%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/XJKXQjihqpo?start=867&end=1906&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a>「合并」：</p>
<ul>
<li>
<p>同名生命周期钩子函数，如 <code>created</code>、<code>mounted</code> 等，将合并为一个数组<strong>都将被调用</strong>，而且混入对象的钩子函数优先级更高，将在组件自身钩子函数<strong>之前</strong>调用。</p>
</li>
<li>
<p>当选项的值为对象，如 <code>methods</code>、<code>components</code>，将被合并为同一个对象。如果合并时<strong>两个对象键名冲突，取组件对象的键值对</strong></p>
</li>
<li>
<p>如果 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fembed%2FXJKXQjihqpo%3Fstart%3D2271%26end%3D2981%26modestbranding%3D1%26rel%3D0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/embed/XJKXQjihqpo?start=2271&end=2981&modestbranding=1&rel=0" ref="nofollow noopener noreferrer">🎬</a> 希望（针对相同选项）自定义混入时合并策略，可以向 <code>Vue.config.optionMergeStrategies</code> 添加一个函数</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.config.optionMergeStrategies.myOption = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">toVal, fromVal</span>) </span>&#123;
  <span class="hljs-comment">// 返回合并后的值</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>可以通过 Vue 原型 prototype 上的方法 <code>Vue.mixin(&#123;options&#125;)</code> 设置 global mixin 全局混入，这样在所有组件中都会引入该 mixin（不需要手动以 <code>mixins: [mixinName]</code> 的方式添加）⚠️ 由于全局混入会影响每个单独创建的 Vue 实例（包括第三方组件），可能会导致一些冲突。</p></div>  
</div>
            