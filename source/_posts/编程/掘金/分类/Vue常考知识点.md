
---
title: 'Vue常考知识点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e91829acc174f01a7eb78a13d308a68~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 00:27:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e91829acc174f01a7eb78a13d308a68~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">watch 和 computed 和 methods 区别是什么？</h3>
<p>methods是方法，computed是计算属性，watch是监听属性</p>
<ol>
<li><code>computed</code>和<code>methods</code>：两者最大的区别就是<code>computed</code>有缓存，如果<code>computed</code>所依赖的属性没有发生变化，就不会重新进行计算，而<code>methods</code>每调用一次就会重新计算一次</li>
<li><code>watch</code>和<code>computed</code>：两者最大的区别就是<code>computed</code>是计算出一个属性，而<code>watch</code>则可以做一些其他的事情，比如说将一个数据进行上报，让这个数据也能实现双向绑定</li>
</ol>
<h3 data-id="heading-1">Vue 有哪些生命周期钩子函数？分别有什么用？</h3>
<ol>
<li>beforeCreate</li>
<li>created</li>
<li>beforeMount</li>
<li>mounted</li>
<li>beforeUpdate</li>
<li>updated</li>
<li>beforeUnmount</li>
<li>unmounted</li>
</ol>
<h3 data-id="heading-2">（1）生命周期是什么？</h3>
<p>Vue 实例有一个完整的生命周期，也就是从开始创建、初始化数据、编译模版、挂载 Dom -> 渲染、更新 -> 渲染、卸载等一系列过程，称这是 Vue 的生命周期。</p>
<h3 data-id="heading-3">（2）各个生命周期的作用</h3>

















































<table><thead><tr><th>生命周期</th><th>描述</th></tr></thead><tbody><tr><td>beforeCreate</td><td>组件实例被创建之初，组件的属性生效之前</td></tr><tr><td>created</td><td>组件实例已经完全创建，属性也绑定，但真实 dom 还没有生成，<code>$el</code>还不可用</td></tr><tr><td>beforeMount</td><td>在挂载开始之前被调用：相关的 render 函数首次被调用</td></tr><tr><td>mounted</td><td>el 被新创建的 <code>vm.$el</code>替换，并挂载到实例上去之后调用该钩子</td></tr><tr><td>beforeUpdate</td><td>组件数据更新之前调用，发生在虚拟 DOM 打补丁之前</td></tr><tr><td>update</td><td>组件数据更新之后</td></tr><tr><td>activited</td><td>keep-alive 专属，组件被激活时调用</td></tr><tr><td>deactivated</td><td>keep-alive 专属，组件被销毁时调用</td></tr><tr><td>beforeUnmount</td><td>组件销毁前调用</td></tr><tr><td>unmounted</td><td>组件销毁后调用</td></tr></tbody></table>
<h3 data-id="heading-4">（3）生命周期示意图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e91829acc174f01a7eb78a13d308a68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">Vue 如何实现组件间通信？</h3>
<pre><code class="copyable">1.props/$emit
2.$emit/$on
3.vuex
4.$attrs/$listeners
5.provide/inject
6.$parent/$children与ref
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 组件间通信是面试常考的知识点之一。Vue 组件间通信只要指以下 3 类通信：父子组件通信、隔代组件通信、兄弟组件通信，下面分别介绍每种通信方式且会说明此种方法可适用于哪类组件间通信。</p>
<p>（1）<code>props</code> / <code>$emit</code> 适用 父子组件通信</p>
<p>这种方法是 Vue 组件的基础，相信大部分同学耳闻能详，所以此处就不举例展开介绍。</p>
<p>（2）<code>ref</code> 与 <code>$parent</code> / <code>$children</code> 适用 父子组件通信</p>
<ul>
<li><code>ref</code>：如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素；如果用在子组件上，引用就指向组件实例</li>
<li><code>$parent </code>/ <code>$children</code>：访问父 / 子实例</li>
</ul>
<p>（3）EventBus （<code>$emit</code> / <code>$on</code>） 适用于 父子、隔代、兄弟组件通信</p>
<p>这种方法通过一个空的 Vue 实例作为中央事件总线（事件中心），用它来触发事件和监听事件，从而实现任何组件间的通信，包括父子、隔代、兄弟组件。</p>
<p>（4）<code>$attrs</code>/<code>$listeners</code> 适用于 隔代组件通信</p>
<ul>
<li><code>$attrs</code>：包含了父作用域中不被 prop 所识别 (且获取) 的特性绑定 ( class 和 style 除外 )。当一个组件没有声明任何 prop 时，这里会包含所有父作用域的绑定 ( class 和 style 除外 )，并且可以通过 v-bind="$attrs" 传入内部组件。通常配合 inheritAttrs 选项一起使用。</li>
<li><code>$listeners</code>：包含了父作用域中的 (不含 .native 修饰器的) v-on 事件监听器。它可以通过 v-on="$listeners" 传入内部组件</li>
</ul>
<p>（5）<code>provide</code> / <code>inject</code> 适用于 隔代组件通信</p>
<p>祖先组件中通过 <code>provider</code> 来提供变量，然后在子孙组件中通过 <code>inject</code> 来注入变量。<code>provide</code> / <code>inject</code> API 主要解决了跨级组件间的通信问题，不过它的使用场景，主要是子组件获取上级组件的状态，跨级组件间建立了一种主动提供与依赖注入的关系。</p>
<p>（6）Vuex 适用于 父子、隔代、兄弟组件通信</p>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。每一个 Vuex 应用的核心就是 store（仓库）。“store” 基本上就是一个容器，它包含着应用中大部分的状态 ( state )。</p>
<ul>
<li>Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。</li>
<li>改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样使得可以方便地跟踪每一个状态的变化。</li>
</ul>
<h3 data-id="heading-6">Vue 数据响应式怎么做到的？</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02771ede4e864059bfb47b74fc128b52~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>响应式系统简述：</p>
<ul>
<li>任何一个Vue Component都有一个与之对应的Watcher实例</li>
<li>Vue的data上的属性会被添加getter和setter属性</li>
</ul>

<ul>
<li>当Vue Component render函数被执行的时候，data上会被触碰（touch），即被读，getter方法会被调用，此时Vue会去记录此Vue component所依赖的所有data。（这一过程被称为依赖收集）</li>
<li>data被改动时（主要是用户操作），即被写，setter方法会被调用，此时Vue会去通知所有依赖于此的data的组件去调用他们的render函数进行更新。</li>
</ul>
<h3 data-id="heading-7">Vue.set 是做什么用的？</h3>
<p>由于Vue不能直接检测到对象内部属性的添加或者修改，因此为了能够实现数据的双向绑定，便需要手动调用<code>vue.set</code>或者<code>this.$set</code></p>
<h3 data-id="heading-8">Vuex 你怎么用的？</h3>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。每一个 Vuex 应用的核心就是 store（仓库）。“store” 基本上就是一个容器，它包含着应用中大部分的状态 ( state )。</p>
<p>（1）Vuex 的状态存储是响应式的。当 Vue 组件从 store 中读取状态的时候，若 store 中的状态发生变化，那么相应的组件也会相应地得到高效更新。</p>
<p>（2）改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation。这样使得可以方便地跟踪每一个状态的变化。</p>
<p>主要包括以下几个模块：</p>
<ul>
<li>State：定义了应用状态的数据结构，可以在这里设置默认的初始状态。</li>
<li>Getter：允许组件从 Store 中获取数据，mapGetters 辅助函数仅仅是将 store 中的 getter 映射到局部计算属性。</li>
</ul>

<ul>
<li>Mutation：是唯一更改 store 中状态的方法，且必须是同步函数。</li>
<li>Action：用于提交 mutation，而不是直接变更状态，可以包含任意异步操作。</li>
</ul>

<ul>
<li>Module：允许将单一的 Store 拆分为多个 store 且同时保存在单一的状态树中。</li>
</ul>
<h3 data-id="heading-9">VueRouter 你怎么用的？</h3>
<p><code>vue-router</code>是<code>vue.js</code>的路由插件，（常用<code>router-link</code>和<code>router-view</code>）
VueRouter是一个vue.js官方的路由管理器</p>
<p>VueRouter中有几个核心概念，分别是 <code>History模式</code> / <code>导航守卫</code> / <code>路由懒加载</code>等</p>
<ol>
<li><code>History模式</code>：VueRouter默认的是<code>Hash模式</code>，<code>Hash模式</code>和<code>History模式</code>最直观的区别就是在于URL里面有没有带<code>#</code>，如果有的话就是<code>Hash模式</code>，否则就是<code>History模式</code>，不过<code>History模式</code>需要后端的支持。</li>
<li><code>导航守卫</code>：导航守卫就是路由跳转时的一些钩子函数，这些函数可以在路由跳转的时候做一些事情。</li>
</ol>

<ol start="3">
<li><code>路由懒加载</code>：<code>const Foo = () => &#123;import(',./Foo.vue')&#125;</code></li>
</ol>
<p>常用的API有：</p>
<ol>
<li><code>router-link</code>：跳转到哪</li>
<li><code>router-view</code>：在哪显示</li>
</ol>

<ol start="3">
<li><code>this.$router.push()</code>：实现路由跳转</li>
<li><code>this.$router.replace()</code>：和this.$router.push()很像，唯一不同的是，他不会在history中添加新的记录</li>
</ol>

<ol start="5">
<li><code>this.$router.params()</code>：动态路由匹配</li>
</ol>
<p>重定向：当用户访问<code>/a</code>的时候，跳转到<code>/b</code></p>
<pre><code class="copyable">const router = new VueRouter(&#123;
routes:[
    &#123;path:'/a', redirect:'/b'&#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>别名：假设<code>/a</code>的别名是<code>/b</code>，那么当用户访问<code>/b</code>的时候，URL仍然保持<code>/b</code>，但实际上路由匹配的是<code>/a</code></p>
<pre><code class="copyable">const router = new VueRouter(&#123;
routes:[
    &#123;path:'/a', component:A, alias:'/b'&#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">路由守卫是什么？</h3>
<p>简单的说，路由守卫就是路由跳转过程中的一些钩子函数，这些函数可以在路由跳转的时候做一些事情。</p>
<p>路由守卫主要分为三种，一种是<code>全局的</code>，一种是<code>组件内的</code>，一种是<code>单个路由独享的</code>。</p>
<ol>
<li><code>全局的</code>：指路由实例上直接操作钩子函数，特点是所有路由配置的组件都会触发</li>
</ol>

<ol>
<li><code>beforeEach</code>在路由跳转前触发</li>
<li><code>beforeResolve</code>和<code>beforeEach</code>相似，区别就是<code>beforeResolve</code>是在<code>beforeEach</code>和组件内<code>beforeRouteEnter</code>之后，<code>afterEach</code>之前调用</li>
</ol>

<ol start="3">
<li><code>afterEach</code>在路由跳转完成后触发</li>
</ol>

<ol start="2">
<li><code>组件内</code>：指在组件内执行钩子函数，相当于为配置路由的组件添加了生命周期钩子函数</li>
</ol>

<ol>
<li><code>beforeRouteEnter</code>在路由进入之前被调用，该钩子在<code>beforeEach</code>和<code>beforeEnter</code>之后，<code>beforeResolve</code>和<code>afterEach</code>之前被调用，也就是说，他是在<code>beforeCreate</code>之前就会被触发</li>
<li><code>beforeRouteUpdate</code>在当前路由改变并且该组件被复用的时候调用，可以通过this访问到实例</li>
</ol>

<ol start="3">
<li><code>beforeRouteLeave</code>在导航离开该组件对应路由的时候被调用，可以通过this访问到实例</li>
</ol>

<ol start="3">
<li><code>路由独享的</code>：指单个路由在配置的时候也可以设置钩子函数</li>
</ol>

<ol>
<li><code>beforeEnter</code>和<code>beforeEach</code>完全相同，如果两者同时设置的话，那么则会在<code>beforeEach</code>后执行</li>
</ol>
<p>总结：</p>
<p>当点击切换路由的时候，将按照下面的顺序执行钩子函数</p>
<ol>
<li><code>beforeRouteLeave</code></li>
<li><code>beforeEach</code></li>
</ol>

<ol start="3">
<li><code>beforeEnter</code></li>
<li><code>beforeRouteEnter</code></li>
</ol>

<ol start="5">
<li><code>beforeResolve</code></li>
<li><code>afterEach</code></li>
</ol>

<ol start="7">
<li><code>beforeCreate</code></li>
<li><code>created</code></li>
</ol>

<ol start="9">
<li><code>beforeMount</code></li>
<li><code>mounted</code></li>
</ol>

<ol start="11">
<li><code>beforeRouteEnter的next回调</code></li>
</ol></div>  
</div>
            