
---
title: 'Vue配置起步(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c65ac36b8e44399fa98c9f3aa9e642~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 17:25:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c65ac36b8e44399fa98c9f3aa9e642~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">前言</h1>
<p>有小伙伴看见标题开头就可能觉得是水文章的，至于为啥要写个这么基础的文章呢？因为Vue系列的文章也写了有几篇了，有<code>组件、反向传值、Vuex</code>等等，感兴趣的可以在<strong>文末</strong>查看或<a href="https://juejin.cn/user/1601308361494712/columns" target="_blank" title="https://juejin.cn/user/1601308361494712/columns">前往专栏</a>查阅。所以啊，纯粹是想补全一下<code>Vue系列的知识点</code>罢了，希望能帮助刚踏进Vue大门的hxd。因为可能刚开始看文档肯定是比较的不熟悉的（大佬懂的，不敢说话...）。后面几篇文章也有可能是一些比较基础的文章，然后<code>案例伪代码的话也不是单文件演示的形式，我猜大家一开始不会用脚手架吧，当然也有例外，纯粹个人看法啊（勿喷）</code>。好吧。废话不多说，进入我们的正题。</p>
<h2 data-id="heading-1">介绍</h2>
<p>是一套基于<code>MVVM设计模式</code>用于构建用户界面的<code>渐进式框架</code>。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与<code>现代化的工具链</code>以及各种<code>支持类库</code>结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。</p>
<blockquote>
<p><code>MVC</code>全名是<code>Model View Controller</code>，是模型<code>(model)</code>－<code>视图(view)</code>－<code>控制器(controller)</code>的缩写，一种软件设计典范</p>
</blockquote>
<p>说起MVC，这里引用斯坦福大学公开课上的这幅图来说明，可以说是最经典和最规范的MVC标准</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c65ac36b8e44399fa98c9f3aa9e642~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="mvc.png" loading="lazy" referrerpolicy="no-referrer">（图片来源于网络）</p>
<blockquote>
<p><code>MVVM</code>全名是<code>Model View ViewModel</code>是<code>模型(model)</code>－<code>视图(view)</code>－<code>视图模型(view-model)</code>的缩写,其实 MVVM真实应该叫做<code>MVCVM</code></p>
</blockquote>
<h2 data-id="heading-2">安装</h2>
<ul>
<li>方法一: 在html 文件中引入vue.js</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><script src=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue/dist/vue.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方法二: 通过npm下载vue模块</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">npm i -s vue
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方法三: 通过Vue 官方脚手架 vue-cli 搭建vue组件化项目</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">#全局安装 vue-cli 环境变量中
npm install -g @vue/cli 
# 使用 vue-cli指令搭建单页面应用项目
vue create hello-world
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">起步</h2>
<p>实例化一个Vue对象，<code>后面的话如果没有特别说明也是基于这个模板进行伪代码的演示</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-comment"><!--引入Vue三方库--></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

    <span class="hljs-comment"><!--创建一个DOM元素--></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 实例化一个Vue对象</span>
    <span class="hljs-comment">// Vue 构造函数接收配置对象</span>
    <span class="hljs-keyword">new</span> Vue(&#123;
           <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span> <span class="hljs-comment">// el 指定页面中DOM元素,Vue就会以这个DOM为挂载对象</span>
    &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">配置</h2>
<h3 data-id="heading-5">el</h3>
<p>提供一个在页面上已存在的 DOM 元素作为 Vue 实例的挂载目标。可以是 CSS 选择器，也可以是一个 HTMLElement 实例。挂载完毕后当前DOM内部渲染将会由当前Vue实例对象所管理与控制</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">data</h3>
<p>(<code>属性</code>)存放当前Vue实例对象数据的配置。Vue 将会<code>递归</code>将 <code>data</code> 的 <code>property</code> 转换为 <code>getter/setter</code>，从而让 <code>data</code> 的 <code>property</code> 能够<code>响应数据变化</code>。<code>对象必须是纯粹的对象</code> (含有零个或多个的 key/value 对)：浏览器 API 创建的原生对象，原型上的 property 会被忽略。大概来说，data 应该只能是数据 - <code>不推荐观察拥有状态行为的对象</code>。</p>
<blockquote>
<p>注意: data 对象自身可以被实例对象的$data所访问,在所有data直接子属性都可以被实例对象直接访问.</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'小明'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
        <span class="hljs-attr">detail</span>: &#123;
            <span class="hljs-attr">tel</span>: <span class="hljs-number">138121345678</span>,
            <span class="hljs-attr">eMail</span>: helloworld@<span class="hljs-number">163.</span>com,
            <span class="hljs-attr">address</span>: <span class="hljs-string">'广州'</span>
        &#125;
    &#125;
&#125;)

vm.$data <span class="hljs-comment">// data对象</span>
vm.age <span class="hljs-comment">// 等价于 vm.$data.age</span>
vm.detail.tel <span class="hljs-comment">// vm.$data.detail.tel 因为tel不是直接子属性不能直接访问</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Vue数据双向绑定是通过数据劫持结合<code>发布者-订阅者模式</code>的方式来实现的,Vue在初始化使用<code>Object.defineProperty</code>递归的将data的属性添加一个<code>getter/setter (监听器Observer)</code>，用来劫持并监听所有属性（Vue 解析器Compile，可以扫描和解析每个节点的相关指令，并根据初始化模板数据以及初始化相应的订阅器即调用当前属性getter方法的元素就是订阅者）。Vue会把所有当前data的订阅者存放在一个dep名单中，如果有变动的，就通过dep名单通知所有订阅者。从而更新视图。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e21e8718383644b3a6e084847061bdf3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="100.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">模板语法</h2>
<p>双大括号文本差值</p>
<p><strong>概念:</strong> Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：vue使用 &#123;&#123;&#125;&#125; (双大括号语法) 将实例中的属性或者其他js表达式插值绑定到模板的任何文本节点中</p>
<p><strong>语法：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
   内部都由Vue实例对象管理 
   <p>姓名:&#123;&#123;name&#125;&#125;</p>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>年龄:&#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>状态:&#123;&#123;age >= 18 ? '已成年':'未成年'&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
   <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'小明'</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<blockquote>
<p>双大括号语法会将内部的表达式以<code>纯文本的形式</code>插入到对应节点内部。这种模式可以预防xss攻击（注入攻击将一段恶意脚本发送到html页面从而获取用户的cookie信息）</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;script&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span> 
        <span class="hljs-comment">// 这里渲染的结果是'<div>hello world<div>'文本节点,而不是一个dom元素</span>
</div>

<script>
       let vm = new Vue(&#123;
            el: '#app',
            data: &#123;
                script: '<div>hello world<div>'
            &#125;
        &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">指令</h2>
<h3 data-id="heading-9">v-html</h3>
<p>可以将文本以html形式插入到指定节点内部而不用向上面一样插入一个纯文本。<strong>注意不要把这个方法暴露给用户！</strong></p>
<p><strong>指令语法:</strong> 在虚拟DOM标签上 <code>指令="js表达式"</code></p>
<pre><code class="hljs language-js copyable" lang="js"> <div id=<span class="hljs-string">"app"</span>>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;script&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>   <span class="hljs-comment">// 纯文本</span>
   <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"script"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> <span class="hljs-comment">// h3dom元素</span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
   <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">script</span>: <span class="hljs-string">'<h3>hello world</h3>'</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">v-once</h3>
<p>一次性地插值，当数据改变时，插值处的内容不会更新</p>
<h3 data-id="heading-11">v-bind属性差值</h3>
<p><strong>概念:</strong> 使用<code>指令 v-bind</code>:属性 ="js表达式" 形式将实例中的data或者其他js表达式插值绑定到标签的任何属性节点中</p>
<p><strong>语法:</strong></p>
<pre><code class="hljs language-js copyable" lang="js"> <div id=<span class="hljs-string">"app"</span>>
       已成年<input type=<span class="hljs-string">"radio"</span> v-bind:checked=<span class="hljs-string">"age >= 18"</span>/>
       未成年<input type=<span class="hljs-string">"radio"</span> v-bind:checked=<span class="hljs-string">"age < 18"</span>/>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
       <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
            &#125;
        &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<ol>
<li>v-bind:指令可以简写成一个冒号 ":"</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
       已成年<input type=<span class="hljs-string">"radio"</span> :checked=<span class="hljs-string">"age >= 18"</span>/>
       未成年<input type=<span class="hljs-string">"radio"</span> :checked=<span class="hljs-string">"age < 18"</span>/>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
       <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
            &#125;
        &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>v-bind 支持动态属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-bind:</span>[<span class="hljs-attr">attrname</span>]=<span class="hljs-string">"link"</span>></span> 百度 <span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>
       <span class="hljs-comment">// <a src="http://www.baidu.com"> 百度 </a></span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
       <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">attrname</span>: <span class="hljs-string">'src'</span>,
                <span class="hljs-attr">link</span>: <span class="hljs-string">'http://www.baidu.com'</span>
            &#125;
        &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<ol>
<li>动态参数预期会求出一个字符串，异常情况下值为 null。这个特殊的 null 值可以被显性地用于移除绑定。任何其它非字符串类型的值都将会触发一个警告。</li>
<li>空格和引号，放在 HTML attribute 名里是无效的</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-bind:</span>['<span class="hljs-attr">foo</span>' + <span class="hljs-attr">bar</span>]=<span class="hljs-string">"value"</span>></span> ... <span class="hljs-tag"></<span class="hljs-name">a</span>></span> // 错误
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">v-bind绑定class</h3>
<h4 data-id="heading-13">1. 对象语法</h4>
<p>我们观察下面代码,我们给每一段歌词元素都绑定了一个class类。内部js表达式逻辑就是当currentIndex 与歌词下标匹配时，歌词元素的class值就会变成active否则为空。但是我们发现，代码过于繁琐。Vue针对class提供对象语法来简化下面的代码</p>
<pre><code class="copyable"><div id="app">
    <p v-bind:class="currentIndex === 0 ? 'active': ''">第一段歌词 0</p>
    <p v-bind:class="currentIndex === 1 ? 'active': ''">第二段歌词 1</p>
    <p v-bind:class="currentIndex === 2 ? 'active': ''">第三段歌词 2</p>
    <p v-bind:class="currentIndex === 3 ? 'active': ''">第四段歌词 3</p>
    <p v-bind:class="currentIndex === 4 ? 'active': ''">第五段歌词 4</p>
</div>

<script>

    let vm = new Vue(&#123;
        el: '#app',
        data: &#123;
            currentIndex: 3
        &#125;
    &#125;)

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-bind绑定的class支持对象写法： <code>v-bind:class = &#123;class名: 判别式&#125;</code>.当判别式为真时,保留该类名否则删除该类名</p>
<p>上面的代码可以使用class 对象语法简写为</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"&#123;active: currentIndex === 0&#125;"</span>></span>第一段歌词 0<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"&#123;active: currentIndex === 1&#125;"</span>></span>第二段歌词 1<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"&#123;active: currentIndex === 2&#125;"</span>></span>第三段歌词 2<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"&#123;active: currentIndex === 3&#125;"</span>></span>第四段歌词 3<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"&#123;active: currentIndex === 4&#125;"</span>></span>第五段歌词 4<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">currentIndex</span>: <span class="hljs-number">3</span>
        &#125;
    &#125;)

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">2. 数组语法</h4>
<p>Vue还支持v-bind:class数组写法,数组中的每一项都可以是js表达式,并且数组中可以包含class对象写法</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"currentIndex === 0 ? 'active lry ' + className : 'lry '+ className"</span>></span>第一段歌词 0<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"[&#123;active: currentIndex === 1&#125;, 'lry', className]"</span>></span>第二段歌词 1<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"[&#123;active: currentIndex === 2&#125;, 'lry', className]"</span>></span>第三段歌词 2<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"[&#123;active: currentIndex === 3&#125;, 'lry', className]"</span>></span>第四段歌词 3<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"[&#123;active: currentIndex === 4&#125;, 'lry', className]"</span>></span>第五段歌词 4<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">currentIndex</span>: <span class="hljs-number">3</span>,
            <span class="hljs-attr">className</span>: <span class="hljs-string">'test'</span>
        &#125;
    &#125;)

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意 :</strong></p>
<ol>
<li>class 的数组语法,对象语法中的数组或对象都可以存放data中绑定给class (data中不要使用this)</li>
<li>一个dom元素中可以最对同时拥有 一个绑定的class属性和一个普通class属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><p v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"[&#123;active: currentIndex === 3&#125;, 'lry', className]"</span>>第四段歌词 <span class="hljs-number">3</span></p>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"lry"</span> <span class="hljs-attr">v-bind:class</span>=<span class="hljs-string">"[&#123;active: currentIndex === 4&#125;, className]"</span>></span>第五段歌词 4<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">v-bind绑定style</h3>
<h4 data-id="heading-16">1. 对象语法</h4>
<p><strong>概念:</strong> <code>v-bind:style</code> 的对象语法十分直观——看着非常像 CSS，但其实是一个 JavaScript 对象。CSS property 名可以用驼峰式 (camelCase) 或短横线分隔 (kebab-case，记得用引号括起来) 来命名：</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>

    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:style</span>=<span class="hljs-string">"&#123;
        color,
        backgroundColor,
        // 短横线命名需要加引号
        'font-size': '18px'
    &#125;"</span>></span>我是一段文本<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>

</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">'blue'</span>,
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'orange'</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">2. 数组语法</h4>
<p><strong>概念:</strong> <code>v-bind:style</code> 的数组语法可以将多个样式对象应用到同一个元素上</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"app"</span>>

    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-bind:style</span>=<span class="hljs-string">"[defaultStyle,&#123;
        color,
        backgroundColor,
        fontSize: '18px'
    &#125;]"</span>></span>我是一段文本<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>

</div>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">'blue'</span>,
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'orange'</span>,
            <span class="hljs-attr">defaultStyle</span>: &#123;
                <span class="hljs-attr">fontWeight</span>: <span class="hljs-number">700</span>,
                <span class="hljs-attr">border</span>: <span class="hljs-string">'1px solid #ccc'</span>
            &#125;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">3.v-bind:style的多重值</h4>
<p><strong>概念:</strong> style 绑定中的 样式属性可以提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><div :style=<span class="hljs-string">"&#123; display: ['-webkit-box', '-ms-flexbox', 'flex'] &#125;"</span>></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写<code>只会渲染数组中最后一个被浏览器支持的值</code>。在本例中，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 <code>display: flex</code>。</p>
<h4 data-id="heading-19">4.v-bind:style自动添加前缀</h4>
<p><strong>概念:</strong> 当 v-bind:style 使用需要添加浏览器引擎前缀的 CSS property 时，如 transform，Vue.js 会自动侦测并添加相应的前缀。</p>
<h2 data-id="heading-20">结尾</h2>
<p>今天就先到这里啦！我们下期再见！码字不易，觉得不错的可以动动小指头点点赞啥的哟~</p>
<h2 data-id="heading-21">系列文章</h2>
<h3 data-id="heading-22">Vue系列</h3>
<ul>
<li><a href="https://juejin.cn/post/6992750559350489096" target="_blank" title="https://juejin.cn/post/6992750559350489096">Vue配置起步（一）</a></li>
<li><a href="https://juejin.cn/post/6981610163509673992" target="_blank" title="https://juejin.cn/post/6981610163509673992">Vue组件</a></li>
<li><a href="https://juejin.cn/post/6981283588696178718Vue%E7%BB%84%E4%BB%B6" target="_blank" title="https://juejin.cn/post/6981283588696178718Vue%E7%BB%84%E4%BB%B6">Vue插槽&过滤器</a></li>
<li><a href="https://juejin.cn/post/6967164077831536648" target="_blank" title="https://juejin.cn/post/6967164077831536648">Vue的反向传值 ($emit事件)</a></li>
</ul>
<h3 data-id="heading-23">Vue-Router系列</h3>
<ul>
<li><a href="https://juejin.cn/post/6975305584392273933" target="_blank" title="https://juejin.cn/post/6975305584392273933">Vue-Router安装与使用</a></li>
<li><a href="https://juejin.cn/post/6975666797575929892" target="_blank" title="https://juejin.cn/post/6975666797575929892">Vue-Router的routes配置</a></li>
</ul>
<h3 data-id="heading-24">Vuex系列</h3>
<ul>
<li><a href="https://juejin.cn/post/6971964011684298782" target="_blank" title="https://juejin.cn/post/6971964011684298782">Vuex系列(一) -- Vuex的使用</a></li>
<li><a href="https://juejin.cn/post/6972334587875688455" target="_blank" title="https://juejin.cn/post/6972334587875688455">Vuex系列(二) -- 模块化的使用</a></li>
<li><a href="https://juejin.cn/post/6972704942695907358" target="_blank" title="https://juejin.cn/post/6972704942695907358">Vuex系列(三) -- store.commit和store.dispatch的区别及用法</a></li>
<li><a href="https://juejin.cn/post/6973080514215280647" target="_blank" title="https://juejin.cn/post/6973080514215280647">Vuex系列(四) -- 辅助函数mapMutations解析</a></li>
</ul></div>  
</div>
            