
---
title: 'Vue2源码解析（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 00:30:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>微信公众号：  <strong>[大前端驿站]</strong><br>
关注大前端驿站。问题或建议，欢迎公众号留言。</p>
</blockquote>
<p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>我们在上一章<a href="https://juejin.cn/post/6991732239503458341" target="_blank" title="https://juejin.cn/post/6991732239503458341">vue2源码解析(一)</a>简单介绍了Vue的执行流程，本章我们创建一个例子来看一下挂载前的处理流程。
还是之前的编码环境下，我们在examples目录下新建一个my-test目录,然后创建一个init.html</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>test Vue</title>
  <script src="../../dist/vue.js"></script>
</head>
<body>
  <div id="app" @click="add">&#123;&#123;counter&#125;&#125;</div>
</body>
<script>
  const app = new Vue(&#123;
    el: '#app',
    data: function() &#123;
      return &#123;
        counter: 1
      &#125;
    &#125;,
    methods: &#123;
      add() &#123;
        this.counter++ 
      &#125;
    &#125;
  &#125;).$mount()
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过这个例子来看下Vue的初始化的流程，首先new了一个Vue实例，那我们通过源码可以定位到instance目录下的index.js中，可以找到Vue的构造方法</p>
<p><strong>src\core\instance\index.js</strong></p>
<pre><code class="copyable">...
function Vue (options) &#123;
  if (process.env.NODE_ENV !== 'production' &&
    !(this instanceof Vue)
  ) &#123;
    warn('Vue is a constructor and should be called with the `new` keyword')
  &#125;
  this._init(options)
&#125;

initMixin(Vue)
stateMixin(Vue)
eventsMixin(Vue)
lifecycleMixin(Vue)
renderMixin(Vue)
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造方法中触发了一个_init方法，此时我们发现这个_init方法有点难找，但是同时可以看到构造方法下面又多个Mixin的方法，并且都是通过传入Vue作为参数。</p>
<p>我们先来看看initMixin之外的其他几个Mixin做了哪些事情</p>
<ul>
<li>stateMixin： 给Vue原型对象设置属性$data、$props、$set、$del</li>
<li>eventsMixin： 给Vue原型对象设置属性$on、$once、$off、$emit</li>
<li>lifecycleMixin： 给Vue原型对象设置属性_update、$forceUpdate、$destroy、$emit</li>
<li>renderMixin： 给Vue原型对象设置属性$nextTick、_render</li>
</ul>
<p>由此可见这些Mixin都是起到丰富Vue的功能的作用，这些原型对象上的方法或者属性大多是我们在日常工作中用过的，这里就不贴代码细讲，同学们可以逐个去过一遍这部分代码。</p>
<p>然后我们重点分析一下initMixin做了哪些工作。在initMixin中就可以看到给Vue的原型对象设置了_init,构造方法正是触发了这个方法。</p>
<p><strong>src\core\instance\init.js</strong></p>
<pre><code class="copyable">  Vue.prototype._init = function (options?: Object) &#123;
    // merge options 第一步工作合并选项
    if (options && options._isComponent) &#123;
      ...
      initInternalComponent(vm, options)
    &#125; else &#123;
      vm.$options = mergeOptions(
        resolveConstructorOptions(vm.constructor),
        options || &#123;&#125;,
        vm
      )
    &#125;
    /* istanbul ignore else */
    // 第二步工作是设置代理
    if (process.env.NODE_ENV !== 'production') &#123;
      initProxy(vm)
    &#125; else &#123;
      vm._renderProxy = vm
    &#125;
    // expose real self
    vm._self = vm
    // 接下来是一系列处理options的工作
    initLifecycle(vm)
    initEvents(vm)
    initRender(vm)
    callHook(vm, 'beforeCreate')
    initInjections(vm) // resolve injections before data/props
    initState(vm)
    initProvide(vm) // resolve provide after data/props
    callHook(vm, 'created')

    /* istanbul ignore if */
    if (process.env.NODE_ENV !== 'production' && config.performance && mark) &#123;
      vm._name = formatComponentName(vm, false)
      mark(endTag)
      measure(`vue $&#123;vm._name&#125; init`, startTag, endTag)
    &#125;
    // 最后触发$mount方法执行挂载的操作
    if (vm.$options.el) &#123;
      vm.$mount(vm.$options.el)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>合并选项</strong></em></p>
<p>处理组件实例与父组件实例或者根实例的选项合并，还有我们用到mixin方式传入的选项，需要先进行选项的合并，然后将合并后的选项赋值给实例的$options属性</p>
<p><em><strong>设置代理</strong></em></p>
<p>这一步不要理解为响应式的处理，很多同学看到Proxy就以为是响应式的处理。那这里设置的代理是为什么的，我们回到init.html的例子中</p>
<pre><code class="copyable">...
add() &#123;
  this.counter++ 
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们都知道add方法中这个this是指向的Vue实例，那么为什么这里可以直接this.counter这么拿到设置在data属性里面的counter呢，这里就是这一步代理的作用，这里将选项里设置的data里面的属性都代理到Vue实例上面。</p>
<p><em><strong>处理options</strong></em></p>
<ul>
<li>initLifecycle(vm)：定义vm：$parent、$root、$children、$refs等</li>
<li>initEvents(vm)：初始化事件：_events、_hasHookEvent，如果有父组件传入的事件更新到本组件上</li>
<li>initRender(vm)：初始化render相关的属性，并且给$attrs和$listeners属性做响应式处理</li>
<li>callHook(vm, 'beforeCreate')：触发beforeCreate钩子函数</li>
<li>initInjections(vm)：处理Injections注入的属性</li>
<li>initState(vm)：依次处理props、methods、data、computed、watch等选项</li>
<li>initProvide(vm)：处理Provide提供给后代组件的属性</li>
<li>callHook(vm, 'created')：触发created钩子函数</li>
</ul>
<p><em><strong>触发$mount方法</strong></em></p>
<p>接下来就开始进入编译和挂载的阶段了，这部分我们下一章再细讲</p>
<p>~~</p>
<p>感谢观看！未完待续......</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae0fd1b178b646ae83a7a9231542fb66~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<div align="center">关注下方【大前端驿站】</div>
<div align="center">让我们一起学，一起进步</div>
<p><strong>【分享、点赞、在看】三连吧，让更多的人加入我们~~</strong></p></div>  
</div>
            