
---
title: 'Vue全解_ 构造选项(基础)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2162'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:22:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=2162'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">创建一个 Vue 实例</h2>
<ul>
<li>Vue 是一个构造函数，对其使用 new 操作符，就得到了一个 Vue 的实例。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(options) 
    <span class="hljs-comment">// or</span>
    <span class="hljs-keyword">new</span> Vue(options)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>vm 对象<code>封装</code>了对视图的所有操作，包括<code>数据读写</code>、<code>事件绑定</code>、<code>DOM 更新</code>。
<ul>
<li>vm 的构造函数是 Vue，按照 ES6 的说法，vm 所属的类是 Vue。</li>
<li>options 是 new Vue 的参数，一般称之为<code>选项</code>或者<code>构造选项</code></li>
</ul>
</li>
</ul>
<h4 data-id="heading-1">vue 的响应式原理</h4>
<ul>
<li>当我们把 options.data 传给 Vue 之后：
<ul>
<li>data 会自动被 Vue 监听(getter 、setter)</li>
<li>data 会被 Vue 的实例(vm)代理</li>
<li>每次对 data 的读写都会被 Vue 监控</li>
<li>Vue 会在data 变化时更新 UI</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">options 构造选项</h2>
<ul>
<li>Vue 中文搜索 <code>选项</code>(英文搜 <code>options</code>)，会列出 options 的五个大类，点击其中一个，即可得到所有相关文档。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23%25E9%2580%2589%25E9%25A1%25B9-%25E6%2595%25B0%25E6%258D%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE" ref="nofollow noopener noreferrer">文档链接</a></p>
<h4 data-id="heading-3">DOM</h4>
<ul>
<li><code>el</code>(挂载点)
<ul>
<li>用来指定数据的挂载位置，它的蚕食可以是 CSS 选择器，可以用 <code>$mount</code> 代替</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>
    &#125;)
    <span class="hljs-comment">// 用 $mount 代替</span>
    <span class="hljs-keyword">new</span> Vue(&#123;
    
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-4">数据</h4>
<ul>
<li><code>data</code>(内部数据)
<ul>
<li><code>data</code> 支持对象和函数，请优先使用函数</li>
<li>可以简单理解为防止组件复用造成的内部数据共享</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>
        &#125;
        <span class="hljs-comment">// or</span>
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>
            &#125;
        &#125;
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><code>methods</code>(方法)
<ul>
<li><code>methods</code>包含了所有事件处理函数或者是普通函数</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123; 
               <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>,
               <span class="hljs-attr">array</span>: [<span class="hljs-number">11</span>, <span class="hljs-number">22</span>, <span class="hljs-number">33</span>, <span class="hljs-number">44</span>]
            &#125;
        &#125;,
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
            <div id="demo">
                &#123;&#123;n&#125;&#125;
                <button @click="add"> + 1 </button>
             &#123;&#123;filter()&#125;&#125;   
            </div>
        `</span>,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.n++
            &#125;,
            <span class="hljs-comment">// 页面中主动调用函数，每次渲染都会自动执行</span>
            <span class="hljs-function"><span class="hljs-title">filter</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.array.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>)
            &#125;
        &#125;
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><code>props</code>(外部属性)
<ul>
<li>不同于 <code>data</code> 的内部数据，允许从外部传入数据,传入的数据会自动绑定到 <code>this</code> 上</li>
<li>声明：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// demo.vue</span>
    <template>
        &#123;&#123;message&#125;&#125;
        <button @click=<span class="hljs-string">"fn"</span>>+<span class="hljs-number">1</span></button>
    </template>
    
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
            <span class="hljs-attr">props</span>: [<span class="hljs-string">'message'</span>,<span class="hljs-string">'fn'</span>]
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用：从外部传入一组 key = value</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// main.js</span>
    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">import</span> Demo <span class="hljs-keyword">from</span> <span class="hljs-string">'./demo.vue'</span>
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">components</span>:&#123;Demo&#125;,
        <span class="hljs-attr">template</span>:<span class="hljs-string">`
            <div>
                <Demo message="外部数据">
            <div>
        `</span>,
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
    
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>传入变量或者函数:</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// main.js</span>
    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">import</span> Demo <span class="hljs-keyword">from</span> <span class="hljs-string">'./demo.vue'</span>
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>
            &#125;
        &#125;
        <span class="hljs-attr">components</span>:&#123;Demo&#125;,
        <span class="hljs-attr">template</span>:<span class="hljs-string">`
            <div>
                &#123;&#123;n&#125;&#125;
                <Demo :message="n" :fn="add" />
            <div>
        `</span>,
       <span class="hljs-attr">methods</span>: &#123;
           <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
               <span class="hljs-built_in">this</span>.n++
           &#125;
       &#125;
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
    
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><code>computed</code>(计算属性)
<ul>
<li>computed 包含所有用于返回计算处理后的、可复用的属性的方法，有点绕，看下面例子</li>
<li>
<ol>
<li>展示用户的昵称或者电话或者邮箱，要求优先展示昵称</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">user</span>: &#123;
                    <span class="hljs-attr">nickname</span>: <span class="hljs-string">'aaa'</span>,
                    <span class="hljs-attr">email</span>: <span class="hljs-string">'bbb@b.com'</span>,
                    <span class="hljs-attr">phone</span>: <span class="hljs-string">'ccc'</span>
                &#125;
        &#125;,
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
            <div>
                &#123;&#123; user.nickname || user.email || user.phone &#125;&#125;
            </div>
        `</span>
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以上需求如果被复用多次，一旦需求改变(如优先展示邮箱)，代码将难以维护</li>
<li>用 computed 处理</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">nickname</span>: <span class="hljs-string">'aaa'</span>,
                <span class="hljs-attr">email</span>: <span class="hljs-string">'bbb@b.com'</span>,
                <span class="hljs-attr">phone</span>: <span class="hljs-string">'ccc'</span>
            &#125;
        &#125;,
        <span class="hljs-attr">computed</span>: &#123;
            <span class="hljs-comment">// 只读的</span>
            <span class="hljs-function"><span class="hljs-title">displayName</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">const</span> user = <span class="hljs-built_in">this</span>.user
                <span class="hljs-keyword">return</span> user.nickname || user.email || user.phone
            &#125;
            <span class="hljs-comment">// or 可读写的</span>
            <span class="hljs-attr">displayName</span>: &#123;
                <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
                    <span class="hljs-keyword">const</span> user = <span class="hljs-built_in">this</span>.user
                    <span class="hljs-keyword">return</span> user.nickname || user.email || user.phone
                &#125;,
                <span class="hljs-attr">ser</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
                   <span class="hljs-comment">// this.user.nickname = value</span>
                &#125;
            &#125;
        &#125;,
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
            <div>
                &#123;&#123;displayName&#125;&#125;
            </div>
        `</span>
    )&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>无论需求怎么变，只要修改 computed 属性里的方法就可以了</li>
</ul>
</li>
<li><code>watch</code>(监听 / 侦听)
<ul>
<li>当数据变化时，执行一个函数</li>
<li>使用 watch 实现撤销</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">history</span>:[],
                <span class="hljs-attr">isUndoMode</span>: <span class="hljs-literal">false</span>
            &#125;
        &#125;,
        <span class="hljs-attr">watch</span>: &#123;
            <span class="hljs-keyword">if</span>(!inUndoMode) &#123;
                <span class="hljs-function"><span class="hljs-title">n</span>(<span class="hljs-params">newValue, oldvalue</span>)</span>&#123;
                    <span class="hljs-built_in">this</span>.history.push(&#123;<span class="hljs-attr">from</span>: oldValue, <span class="hljs-attr">to</span>: newValue&#125;)
                &#125;
            &#125;
        &#125;,
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
            <div>
                &#123;&#123;n&#125;&#125;
                <br>
                <button @click="add">+1</button>
                <button @click="minus">-1</button>
                <br>
                <button @click="undo">撤销</button>
                <br>
                &#123;&#123;history&#125;&#125;
            </div>
        `</span>,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.n++
            &#125;,
            <span class="hljs-function"><span class="hljs-title">minus</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.n--
            &#125;,
            <span class="hljs-function"><span class="hljs-title">undo</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">const</span> last = <span class="hljs-built_in">this</span>.history.pop()
                <span class="hljs-keyword">if</span> (last) &#123;
                    <span class="hljs-built_in">this</span>.n = last.from
                &#125;
                <span class="hljs-built_in">this</span>.isUndoMode = <span class="hljs-literal">true</span>
                <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// watch 是异步的</span>
                    <span class="hljs-built_in">this</span>.inUndoMode = <span class="hljs-literal">false</span>
                &#125;, <span class="hljs-number">0</span>)
            &#125;
        &#125;
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>watch 的 <code>deep</code> 属性 (深度监听)
<ul>
<li><code>watch</code> 在监听数据变化时，如果监听的是简单数据类型，如果值变化，则视为变化，如果监听复杂数据类型，如果对象的地址变化，则视为变化，如果对象里属性的值变化，而对象的地址没变，则视为无变化。</li>
<li>修改 <code>deep</code> 属性的值为 true 可以改变这一点</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    ...
    <span class="hljs-attr">watch</span>: &#123;
        <span class="hljs-attr">obj</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">handle</span>(<span class="hljs-params"></span>)</span>&#123;...&#125;,
            <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>
        &#125;
    &#125;
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li><code>watch</code> 和 <code>computed</code> 的区别
<ul>
<li>computed 计算属性</li>
</ul>
<ol>
<li>支持缓存，只有依赖数据发生改变，才会重新进行计算</li>
<li>不支持异步，当 computed 内有异步操作时无效，无法监听数据的变化</li>
<li>computed 属性值会默认走缓存，计算属性是基于它们的响应式依赖进行缓存的，也就是基于 data 中声明过或者父组件传递的 props 中的数据通过计算得到的值</li>
<li>如果一个属性是由其他属性计算而来的，这个属性依赖其他属性，是一个多对一或者一对一，一般用 computed</li>
<li>如果 computed 属性属性值是函数，那么默认会走 get 方法；函数的返回值就是属性的属性值；在 computed 中的，属性都有一个 get 和一个 set 方法，当数据变化时，调用 set 方法。</li>
</ol>
<ul>
<li>watch 监听</li>
</ul>
<ol>
<li>不支持缓存，数据变，直接会触发相应的操作</li>
<li>支持异步</li>
<li>监听的函数接收两个参数，第一个参数是最新的值；第二个参数是输入之前的值</li>
<li>当一个属性发生变化时，需要执行对应的操作；一对多</li>
<li>监听数据必须是 data 中声明过或者父组件传递过来的 props 中的数据，当数据变化时，触发其他操作，函数有两个参数
<ul>
<li>immediate：组件加载立即触发回调函数执行</li>
<li>deep: 深度监听，为了发现对象内部值的变化，复杂类型的数据时使用，例如数组中的对象内容的改变，注意监听数组的变动不需要这么做。注意：deep 无法监听到数组的变动和对象的新增，参考 vue 数组变异,只有以响应式的方式触发才会被监听到</li>
</ul>
</li>
</ol>
</li>
</ul>
<h4 data-id="heading-5">资源</h4>
<ul>
<li><code>components</code>(组件)
<ul>
<li>Vue 组件有三种定义方式</li>
</ul>
<ol>
<li>单独创建一个 vue 文件 demo.vue</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <template>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
            &#123;&#123;n&#125;&#125;
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    </template>
    
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">n</span>:<span class="hljs-number">0</span> &#125; &#125;,
            <span class="hljs-attr">methods</span>:&#123;
                <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123; <span class="hljs-built_in">this</span>.n++ &#125;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
        ...
    <span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>引入组件,使用组件</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-comment">// 注意路径</span>
    <span class="hljs-keyword">import</span> demo <span class="hljs-keyword">from</span> <span class="hljs-string">'./demo.vue'</span>
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-comment">// 使用</span>
        <span class="hljs-attr">components</span>: &#123; demo &#125;，
        template： <span class="hljs-string">`
            <div>
                <demo />
            <div>
        `</span>
        ...
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>或者使用 component 函数,直接定义组件。函数的第一个参数接收组件的名字，第二个参数和 options 完全一样</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    Vue.component(<span class="hljs-string">'demo'</span>,&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`
            <div> content <div>
        `</span>
    &#125;)
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-comment">// 使用</span>
        template： <span class="hljs-string">`
            <div>
                <demo />
            <div>
        `</span>
        ...
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>第三种</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-comment">// 定义</span>
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-attr">newDemo</span>: &#123;
                <span class="hljs-attr">template</span>: <span class="hljs-string">`
                    <div> content <div>
                `</span>
            &#125;
        &#125;
        <span class="hljs-comment">// 使用</span>
        template： <span class="hljs-string">`
            <div>
                <newDemo />
            <div>
        `</span>
        ...
    &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-6">生命周期钩子</h4>
<ul>
<li>钩子可以简单理解为程序执行的某个重要节点，可以使用这些方法来做一些事情。
<ul>
<li><code>beforeCreate</code>、<code>created</code>(不会出现在页面中)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        ...
        <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'内容创建了'</span>)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>beforeMount</code>、<code>mounted</code>(会出现在页面中)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        ...
        <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'页面展示了'</span>)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>beforeUpdate</code>、<code>updated</code>(数据更新触发)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        ...
        <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数据更新了'</span>)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>beforeDestroy</code>、<code>destroyed</code>(数据从页面中消失)</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue
    <span class="hljs-keyword">new</span> Vue(&#123;
        ...
        <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'数据消亡了'</span>)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            