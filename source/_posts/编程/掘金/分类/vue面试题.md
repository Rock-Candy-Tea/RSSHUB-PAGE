
---
title: 'vue面试题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef71930433d4cf38c8e5072c9740c15~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:46:35 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef71930433d4cf38c8e5072c9740c15~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fshi%255C_xingwen%2Farticle%2Fdetails%2F114655369" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/shi%5C_xingwen/article/details/114655369" ref="nofollow noopener noreferrer">blog.csdn.net/shi\_xingwe…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.520mg.com%2Fa%2Finter%2Fvuetiku%2Fvuejichu%2F9098.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.520mg.com/a/inter/vuetiku/vuejichu/9098.html" ref="nofollow noopener noreferrer">www.520mg.com/a/inter/vue…</a></p>
<p>2、<strong>怎么定义vue-router的动态路由?怎么获取传过来的动态参数?</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fm0%255C_48560510%2Farticle%2Fdetails%2F110354840" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/m0%5C_48560510/article/details/110354840" ref="nofollow noopener noreferrer">blog.csdn.net/m0\_4856051…</a></p>
<p>3、<strong>vue- router有哪几种导航钩子？</strong></p>
<p>三种，<br>
第一种：是全局导航钩子：router.beforeEach(to,from,next)，作用：跳转前进行判断拦截。<br>
第二种：组件内的钩子<br>
第三种：单独路由独享组件</p>
<p>a、详解vue-router中的导航钩子</p>
<h3 data-id="heading-0">一：概念</h3>
<p><strong>作用：拦截导航，让他完成跳转或取消。</strong></p>
<pre><code class="copyable">const router = new VueRouter(&#123; ... &#125;);router.beforeEach((to, from, next) => &#123;    // do someting&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、<strong>vuex是什么？如何使用？在哪种功能场景中使用它？</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.520mg.com%2Fa%2Finter%2Fvuetiku%2Fvuejichu%2F9098.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.520mg.com/a/inter/vuetiku/vuejichu/9098.html" ref="nofollow noopener noreferrer">www.520mg.com/a/inter/vue…</a></p>
<p><strong>你是怎样认识vuex的？</strong></p>
<p>vuex可以理解为一种开发模式或框架。它是对 Vue. js框架数据层面的扩展。通过状态（数据源）集中管理驱动组件的变化。应用的状态集中放在 store中。改变状态的方式是提交 mutations，这是个同步的事务。异步逻辑应该封装在 action中。</p>
<p><strong>5、如何实现自定义指令？它有哪些钩子函数？还有哪些钩子函数参数？</strong></p>
<p><strong>6、Vue-router是什么？它有哪些组件？</strong></p>
<pre><code class="copyable"><router-link :to='' class='active-class'>   //路由声明式跳转 ，active-class是标签被点击时的样式

<router-view>                  //渲染路由的容器

<keep-alive>                    //缓存组件
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vue-router</code>路由，通俗来讲主要是来实现页面的跳转，通过设置不同的path，向服务器发送的不同的请求，获取不同的资源。</p>
<p>主要组件：<code>router-view</code>、<code>router-link</code></p>
<p>7、<strong>Vue.js的双向数据绑定原理是什么？</strong></p>
<p>Vue. js采用ES5提供的属性特性功能，结合发布者-订阅者模式，通过 Object.defineProperty()为各个属性定义get、set特性方法，在数据发生改变时给订阅者发布消息，触发相应的监听回调。 具体步骤如下。 </p>
<p> （1）对需要观察的数据对象进行递归遍历，包括子属性对象的属性，设置set和get特性方法。当给这个对象的某个值赋值时，会触发绑定的set特性方法，于是就能监听到数据变化。 </p>
<p> （2）用 compile解析模板指令，将模板中的变量替换成数据。然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者。一旦数据有变动，就会收到通知，并更新视图 </p>
<p> （3） Watcher订阅者是 Observer和 Compile之间通信的桥梁，主要功能如下。 在自身实例化时向属性订阅器（dep）里面添加自己。 自身必须有一个 update( )方法。 在 dep.notice()发布通知时，能调用自身的 updat()方法，并触发 Compile中绑定的回调函数。 </p>
<p>（4）MVVM是数据绑定的入口，整合了 Observer、 Compile和 Watcher三者，通过Observer来监听自己的 model数据变化，通过 Compile来解析编译模板指令，最终利用Watcher搭起 Observer和 Compile之间的通信桥梁，达到数据变化通知视图更新的效果。利用视图交互，变化更新数据 model变更的双向绑定效果。</p>
<p>8、<strong>请详细说明你对Vue.js生命周期的理解。</strong></p>
<p>总共分为8个阶段，分别为 beforeCreate、created、beforeMount、 mounted、beforeUpdate、 updated、 beforeDestroyed、 destroyed。 </p>
<p> beforeCreate：在实例初始化之后，数据观测者（ data observer）和 event/ watcher事件配置之前调用。</p>
<p> created：在实例创建完成后立即调用。在这一步，实例已完成以下的配置：数据观测者，属性和方法的运算， watch/event事件回调。然而，挂载阶段还没开始，$el属性目前不可见。</p>
<p> beforeMount：在挂载开始之前调用，相关的 render函数首次调用。</p>
<p> mounted: el被新创建的vm.$el替换，并且在挂载到实例上之后再调用该钩子如果root实例挂载了一个文档内元素，当调用 mounted时vm.sel也在文档内。</p>
<p> beforeUpdate：在数据更新时调用，发生在虛拟DOM重新渲染和打补丁之前。</p>
<p> updated：由于数据更改导致的虚拟DOM重新渲染和打补丁，在这之后会调用该钩。</p>
<p> beforeDestroy：在实例销毁之前调用。在这一步，实例仍然完全可用。</p>
<p> destroyed：在 Vue. js实例销毀后调用。调用后，Vue. js实例指示的所有东西都会解除绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。</p>
<p>当使用组件的kep- alive功能时，增加以下两个周期。 </p>
<p> activated在keep- alive组件激活时调用； </p>
<p>deactivated在keep-live组件停用时调用。</p>
<p> Vue2.5.0版本新增了一个周期钩子：ErrorCaptured，当捕获一个来自子孙组件的错误时调用</p>
<p>9、<strong>Vue- loader是什么？它的用途有哪些？</strong></p>
<p>它是解析.vue文件的一个加载器，可以将 template/js/style转换成 JavaScript模块。 用途是通过 vue-loader, JavaScript可以写 EMAScript 6语法， style样式可以应用scss或less, template可以添加jade语法等。</p>
<p>10、<strong>谈谈你对vue.js的 template编译的理解。</strong></p>
<p>简而言之，就是首先转化成AST（ Abstract Syntax Tree，抽象语法树），即将源代码语法结构抽象成树状表现形式，然后通过 render函数进行渲染，并返回VNode（ Vue. js的虚拟DOM节点）。 详细步骤如下。 （1）通过 compile编译器把 template编译成AST, compile是 create Compiler的返回值， createCompiler用来创建编译器。另外， compile还负责合并 option。 （2）AST会经过 generate（将AST转化成 render funtion字符串的过程）得到 render函数， render的返回值是 VNode, VNode是 Vue.Js的虚拟DOM节点，里面有标签名子节点、文本等。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef71930433d4cf38c8e5072c9740c15~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d2d7b523cc4855933d28b054fbd722~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            