
---
title: 'vue-router学习之使用hash的方式实现一个简单的router插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9096'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 04:51:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=9096'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>学习了vue-router原理，记录一下，方便加深记忆。感谢<a href="https://juejin.cn/user/325111174926350" target="_blank">村长</a>！</p>
</blockquote>
<h1 data-id="heading-0">通过vue-router的使用方式创建测试用例</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 在./frouter/index.js 引入router插件并使用</span>
<span class="hljs-keyword">import</span> FRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'./frouter.js'</span>
Vue.use(FRouter)

<span class="hljs-comment">// 2.在./frouter/index.js创建router实例并导出</span>
<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
        <span class="hljs-attr">component</span>: Home
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
        <span class="hljs-comment">// 注意此处必须是以函数形式引入</span>
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/About.vue'</span>)
    &#125;
]
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> FRouter(&#123; routes &#125;)

<span class="hljs-comment">// 3.在main.js中引入router实例并挂载到Vue实例</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./frouter'</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    router
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="hljs-comment">// 4.在App.vue中添加路由导航和路由视图</span>
<router-link to=<span class="hljs-string">"/"</span>>Home</router-link>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">思考实现方式</h1>
<h2 data-id="heading-2">创建frouter插件</h2>
<ul>
<li>在插件中实现FRouter类
<ul>
<li>保存并处理router实例传过来的路由配置表</li>
<li>监控路由的变化并保存当前路由的信息</li>
<li>对当前路由做响应式处理，以便在路由变化的时候驱动路由视图进行变化</li>
</ul>
</li>
<li>在插件中实现install方法提供给Vue.use()使用
<ul>
<li>将$router写入Vue的原型链中，以便在所有组件中通过$router实例进行访问</li>
<li>全局注册router-link组件与router-view组件</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建frouter.js</span>
<span class="hljs-keyword">let</span> Vue;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FRouter</span> </span>&#123;
    <span class="hljs-title">constructor</span> (<span class="hljs-params">options = &#123;&#125;</span>) &#123;
        <span class="hljs-built_in">this</span>.$options = options
        <span class="hljs-built_in">this</span>.mapRouter = &#123;&#125;
        <span class="hljs-comment">// 保存path与route之间的映射关系，避免每次都需要循环查找</span>
        <span class="hljs-built_in">this</span>.$options.routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
            <span class="hljs-built_in">this</span>.mapRouter[route.path] = route
        &#125;);
        <span class="hljs-comment">// 获取hash值并截取#后面的值</span>
        <span class="hljs-keyword">const</span> initialCurrent = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>) || <span class="hljs-string">'/'</span>
        <span class="hljs-comment">// 使用Vue的工具函数defineReactive对初始化的当前路由做响应式处理</span>
        <span class="hljs-comment">// 此处的this指的是当前类</span>
        Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">'current'</span>, initialCurrent)
        <span class="hljs-comment">// 监听hashchange事件并绑定当前类作为上下文以防外界在定时器中访问onHashChange方法时改变this指向</span>
        <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-built_in">this</span>.onHashChange.bind(<span class="hljs-built_in">this</span>))
    &#125;
    onHashChange () &#123;
        <span class="hljs-built_in">this</span>.current = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>)
    &#125;
&#125;
FRouter.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_Vue</span>) </span>&#123;
    <span class="hljs-comment">// 传入Vue的构造函数方便修改它的原型，绑定$router</span>
    Vue = _Vue; <span class="hljs-comment">// 将传入的_Vue构造函数保存以便在FRouter类中使用Vue中的工具函数</span>
    <span class="hljs-comment">// 通过全局混入将router注入到Vue的原型链中</span>
    Vue.mixin(&#123;
        <span class="hljs-comment">// Vue中的所有组件都会进入beforeCreate生命周期</span>
        <span class="hljs-comment">// 判断只有当前组件实例中传入了router实例才将router实例写入到Vue的原型链中（查看测试用例中的第3点）</span>
        beforeCreate () &#123;
            <span class="hljs-comment">// 此处的this指的是当前的组件实例</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
                Vue.prototype.$router = <span class="hljs-built_in">this</span>.$options.router
            &#125;
        &#125;
    &#125;)
    <span class="hljs-comment">// 全局注册router-link组件</span>
    Vue.component(<span class="hljs-string">'router-link'</span>, &#123;
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">to</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;
        &#125;,
        render (h) &#123;
            <span class="hljs-comment">// 在runtime运行环境中不能放<template>标签，必须用render函数渲染</span>
            <span class="hljs-keyword">return</span> h (<span class="hljs-string">'a'</span>, &#123;
                <span class="hljs-attr">attrs</span>: &#123;
                    <span class="hljs-attr">href</span>: <span class="hljs-string">'#'</span> + <span class="hljs-built_in">this</span>.to
                &#125;
            &#125;, <span class="hljs-built_in">this</span>.$slots.default)
        &#125;
    &#125;)
    <span class="hljs-comment">// 全局注册router-view组件</span>
    Vue.component(<span class="hljs-string">'router-view'</span>, &#123;
        render (h) &#123;
            <span class="hljs-comment">// 此处的this指的是组件实例，通过vue组件实例访问路由$router实例中的$options与current及mapRouter</span>
            <span class="hljs-keyword">const</span> &#123; mapRouter, current &#125; = <span class="hljs-built_in">this</span>.$router
            <span class="hljs-keyword">const</span> component = mapRouter[current] ? mapRouter[current].component : <span class="hljs-literal">null</span>
            <span class="hljs-keyword">return</span> h(component)
        &#125;
    &#125;)
&#125;
<span class="hljs-comment">// 导出插件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> FRouter;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            