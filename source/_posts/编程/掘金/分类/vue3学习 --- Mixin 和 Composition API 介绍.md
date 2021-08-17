
---
title: 'vue3学习 --- Mixin 和 Composition API 介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7353'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 15:23:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=7353'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Mixin</h3>
<p>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>组件和组件之间有时候会存在相同的代码逻辑，我们希望对<code>相同的代码逻辑进行抽取</code>。</p>
<p>在Vue2和Vue3中都支持的一种方式就是<code>使用Mixin来完成</code>：</p>
<ul>
<li>Mixin提供了一种非常灵活的方式，来<code>分发Vue组件中的可复用功能</code></li>
<li>一个Mixin对象可以包含<code>任何组件选项</code></li>
<li>当组件使用Mixin对象时，<code>所有Mixin对象的选项将被 混合 进入该组件本身的选项</code>中</li>
</ul>
<p><code>mixin定义者 --- /mixins/fooMixin.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">'something in fooMixn'</span>
    &#125;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mixin使用者 --- App.vue</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"foo"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> fooMixin <span class="hljs-keyword">from</span> <span class="hljs-string">'./mixins/fooMixin'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-comment">// mixin本质上是一个对象</span>
  <span class="hljs-comment">// 一个组件可以混入多个，所以mixins所对应的值是一个对象</span>
  <span class="hljs-attr">mixins</span>: [fooMixin]
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">合并规则</h4>
<ol>
<li>
<p>如果是data函数的返回值对象</p>
<ul>
<li>返回值对象默认情况下会进行合并</li>
<li>如果data返回值对象的属性发生了冲突，那么会<code>保留组件自身的数据</code></li>
</ul>
</li>
<li>
<p>如何生命周期钩子函数</p>
<ul>
<li>
<p>生命周期的钩子函数会被<code>合并到数组</code>中，都会被调用</p>
</li>
<li>
<p>先执行Mixin中对应的逻辑，在执行组件中对应生命周期钩子的逻辑</p>
</li>
</ul>
</li>
<li>
<p>值为对象的选项，例如 methods、components 和 directives，将被合并为同一个对象</p>
<ul>
<li>比如都有methods选项，并且都定义了方法，那么它们都会生效</li>
<li>但是如果对象的<code>key相同</code>，那么会<code>取组件对象的键值对</code></li>
</ul>
</li>
</ol>
<h4 data-id="heading-2">全局混入</h4>
<p>如果组件中的某些选项，是所有的组件都需要拥有的，那么这个时候我们可以使用全局的mixin：</p>
<ul>
<li>全局的Mixin可以使用 应用app的方法 mixin 来完成注册</li>
<li>一旦注册，那么全局混入的选项将会影响每一个组件</li>
<li>全局混入的生命周期会优先执行 --- 因为最早被插入到数组中</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">const</span> app = createApp(App)

app.mixin(&#123;
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'全局混入'</span>)
  &#125;
&#125;)

app.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">extends</h3>
<p>另一个和Mixins十分相似的属性，就是extends</p>
<p><code>基础组件</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--
      如果使用继承，只能继承script中的内容
      无法继承模板中的内容
    --></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Base<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'BaseComponent'</span>,

  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'base msg'</span>
    &#125;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用继承组件</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"foo"</span>></span>click ms<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> BaseComponent <span class="hljs-keyword">from</span> <span class="hljs-string">'./BaseComponent.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-comment">// 继承自BaseComponent, 对其进行扩展</span>
  <span class="hljs-comment">// 组件只能进行单继承</span>
  <span class="hljs-attr">extends</span>: BaseComponent
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Composition API</h3>
<p>在Vue2中，我们编写组件的方式是Options API:</p>
<p>Options API的一大特点就是在对应的属性中编写对应的功能模块</p>
<p>比如data定义数据、methods中定义方法、computed中定义计算属性、watch中监听属性改变，也包括生命 周期钩子</p>
<p>但是这么做有一个很大的弊端：</p>
<ul>
<li>
<p>当我们实现某一个功能时，这个功能对应的<code>代码逻辑会被拆分</code>到各个属性中</p>
</li>
<li>
<p>当我们组件变得更大、更复杂时，逻辑关注点的列表就会增长，那么<code>同一个功能的逻辑就会被拆分的很分散</code></p>
</li>
<li>
<p>尤其对于那些一开始没有编写这些组件的人来说，这个组件的代码是难以阅读和理解的(阅读组件的其他人)</p>
</li>
</ul>
<p>Composition API（Vue Composition API ---> VCA）就是为了解决上述问题而存在的</p>
<p>Composition API能将同一个逻辑关注点相关的代码收集在一起</p>
<h4 data-id="heading-5">Setup</h4>
<p>为了开始使用Composition API，我们需要有一个可以实际使用它(编写代码)的地</p>
<p>在Vue组件中，这个位置就是 setup 函数</p>
<h5 data-id="heading-6">参数</h5>
<p>setup函数，主要有两个参数:</p>
<p>第一个参数:props:</p>
<ul>
<li>
<p><strong>父组件传递过来的属性</strong>会被<strong>放到props对象</strong>中，我们在<strong>setup中如果需要使用</strong>，那么就可 以直接<strong>通过props参数获取</strong></p>
</li>
<li>
<p>对于定义props的类型，我们还是和之前的规则是一样的，在props选项中定义</p>
</li>
<li>
<p>并且在template中依然是可以正常去使用props中的属性，比如message</p>
</li>
<li>
<p>如果我们在setup函数中想要使用props，那么不可以通过 this 去获取</p>
</li>
<li>
<p>setup函数中，是没有this关键字的</p>
</li>
<li>
<p>因为props有直接作为参数传递到setup函数中，所以我们可以直接通过参数来使用即可</p>
</li>
</ul>
<p>第二个参数:context</p>
<p>另外一个参数是context，我们也称之为是一个<strong>SetupContext</strong>，它里面<strong>包含三个属性</strong>：</p>
<ul>
<li>attrs:所有的非prop的attribute</li>
<li>slots:父组件传递过来的插槽</li>
<li>emit:当我们组件内部需要发出事件时会用到emit(因为我们不能访问this，所以不可以通过 this.$emit发出事件)</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,

  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">message</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    <span class="hljs-comment">// 获取父组件传递过来的数据</span>
    <span class="hljs-built_in">console</span>.log(props)

    <span class="hljs-comment">// 类似于vue2中的this.$emit方法 </span>
    emit(<span class="hljs-string">'homeClick'</span>)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">返回值</h5>
<p>setup既然是一个函数，那么它也可以有<strong>返回值</strong></p>
<p>setup的返回值可以在模板template中被使用, 也就是说我们可以通过setup的返回值来替代data选项</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'message'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是setup函数的返回值默认情况下，只是一个普通变量，Vue并不会跟踪它的变化，来引起界面的响应式操作</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>

    <span class="hljs-comment">// 此时点击了按钮后，setup中的count发生了改变，但是界面中的count并不会发现相应的改变</span>
    <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> count++

    <span class="hljs-keyword">return</span>  &#123;
      count,
      increment
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">Reactive</h4>
<p>当我们使用reactive函数处理我们的数据之后，数据再次被使用时就会进行依赖收集</p>
<p>当数据发生改变时，所有收集到的依赖都是进行对应的响应式操作(比如更新界面)</p>
<p>事实上，我们编写的data选项，也是在内部交给了reactive函数将其编程响应式对象的</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>&#123;&#123; state.count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;)

    <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> state.count++

    <span class="hljs-keyword">return</span>  &#123;
      state,
      increment
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Ref</h4>
<p>reactive API对<strong>传入的类型是有限制的</strong>，它要求我们必须传入的是<strong>一个对象或者数组类型</strong></p>
<p>如果我们传入一个基本数据类型(String、Number、Boolean)会报一个警告</p>
<p>这个时候Vue3给我们提供了另外一个API: ref API</p>
<ul>
<li>ref 会返回一个可变的响应式对象，该对象作为一个 <strong>响应式的引用</strong> 维护着它内部的值，这就是ref名称的来源</li>
<li>它内部的值是在ref的 value 属性中被维护的</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 
      在模板中引入ref的值时，Vue会自动帮助我们进行解包操作，所以我们并不需要在模板中通过 ref.value 的方式来使用 
    --></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

    <span class="hljs-comment">// 在 setup 函数内部，它依然是一个 ref引用， 所以对其进行操作时，我们依然需要使用 ref.value的方式</span>
    <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> count.value++

    <span class="hljs-keyword">return</span>  &#123;
      count,
      increment
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">readonly</h4>
<p>我们通过reactive或者ref可以获取到一个响应式的对象，但是某些情况下，我们传入给其他地方(组件)的这个</p>
<p>响应式对象希望在另外一个地方(组件)被使用，但是不能被修改，这个时候如何防止这种情况的出现呢?</p>
<p>Vue3为我们提供了readonly的方法</p>
<p>readonly会返回原生对象的只读代理(也就是它依然是一个Proxy，只不过这个proxy的set方法被劫持，不能对进行值的修改操作)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 普通对象</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> counter = &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;

  <span class="hljs-keyword">const</span> readOnlyCounter = readonly(counter)

  <span class="hljs-keyword">const</span> change = <span class="hljs-function">() =></span> readOnlyCounter.count++ <span class="hljs-comment">// error</span>

  <span class="hljs-keyword">return</span> &#123;
    counter,
    readOnlyCounter,
    change
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// reactive对象</span>
<span class="hljs-keyword">const</span> counter = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;)

<span class="hljs-keyword">const</span> readOnlyCounter = readonly(counter)

<span class="hljs-keyword">const</span> change = <span class="hljs-function">() =></span> readOnlyCounter.count++ <span class="hljs-comment">// error</span>

<span class="hljs-keyword">return</span> &#123;
  counter,
  readOnlyCounter,
  change
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ref对象</span>
<span class="hljs-keyword">const</span> counter = ref(<span class="hljs-number">0</span>)

<span class="hljs-keyword">const</span> readOnlyCounter = readonly(counter)

<span class="hljs-keyword">const</span> change = <span class="hljs-function">() =></span> readOnlyCounter.value++ <span class="hljs-comment">// error</span>

<span class="hljs-keyword">return</span> &#123;
  counter,
  readOnlyCounter,
  change
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在readonly的使用过程中，有如下规则:</p>
<ul>
<li>readonly返回的对象都是不允许修改的</li>
<li>但是经过readonly处理的原来的对象是允许被修改的</li>
<li>其实本质上就是readonly返回的对象的setter方法被劫持了而已</li>
</ul>
<p>此时，如果我们传递给其他组件数据时，希望其他组件使用我们传递的内容，但是不允许它们修改时，就可以使用 readonly了</p></div>  
</div>
            