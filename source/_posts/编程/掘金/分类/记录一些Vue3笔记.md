
---
title: '记录一些Vue3笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=91'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 05:30:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=91'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vue3</h2>
<h4 data-id="heading-1">Vue3 生命周期</h4>
<pre><code class="copyable">与 2.x 版本生命周期相对应的组合式 API
    beforeCreate -> 使用 setup()
    created -> 使用 setup()
    beforeMount -> onBeforeMount
    mounted -> onMounted
    beforeUpdate -> onBeforeUpdate
    updated -> onUpdated
    beforeDestroy -> onBeforeUnmount
    destroyed -> onUnmounted
    errorCaptured -> onErrorCaptured
新增的钩子函数
组合式 API 还提供了以下调试钩子函数：
onRenderTracked
onRenderTriggered
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">Composition API（常用部分）</h4>
<h5 data-id="heading-3">setup</h5>
<pre><code class="copyable">1.新的option，所有的组合API函数都在此使用，只在初始化时执行一次
2.函数如果返回对象，对象中的属性或方法，模板中可以直接使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">setup细节</h5>
<pre><code class="copyable">/* setup执行的时机 */
    在beforeCreate之前执行(一次), 此时组件对象还没有创建
    this是undefined, 不能通过this来访问data/computed/methods / props
    其实所有的composition API相关回调函数中也都不可以
/* setup的返回值 */
    一般都返回一个对象: 为模板提供数据, 也就是模板中可以直接使用此对象中的所有属性/方法
    返回对象中的属性会与data函数返回对象的属性合并成为组件对象的属性
    返回对象中的方法会与methods中的方法合并成功组件对象的方法
    如果有重名, setup优先
    注意:
    一般不要混合使用: methods中可以访问setup提供的属性和方法, 但在setup方法中不能访问data和methods
    setup不能是一个async函数: 因为返回值不再是return的对象, 而是promise, 模板看不到return对象中的属性数据
/* setup的参数 */
    setup(props, context) / setup(props, &#123;attrs, slots, emit&#125;)
    props: 包含props配置声明且传入了的所有属性的对象
    attrs: 包含没有在props配置中声明的属性的对象, 相当于 this.$attrs
    slots: 包含所有传入的插槽内容的对象, 相当于 this.$slots
    emit: 用来分发自定义事件的函数, 相当于 this.$emit
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">ref</h5>
<pre><code class="copyable">作用：定义一个数据的响应式
语法：const xxx = ref(initValue);
创建一个包含响应式数据的引用对象
js中操作数据：xxx.value
模板中操作数据：不需要value
一般用来定义一个基本类型的响应式数据
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">ref获取元素</h5>
<pre><code class="hljs language-html copyable" lang="html">利用ref函数获取组件中的标签元素
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"inputRef"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">/* ref获取元素: 利用ref函数获取组件中的标签元素 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> inputRef = ref<HTMLElement|<span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>)

    onMounted(<span class="hljs-function">() =></span> &#123;
      inputRef.value && inputRef.value.focus()
    &#125;)

    <span class="hljs-keyword">return</span> &#123;
      inputRef
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">reactive</h5>
<pre><code class="copyable">作用: 定义多个数据的响应式
const proxy = reactive(obj): 接收一个普通对象然后返回该普通对象的响应式代理器对象
响应式转换是“深层的”：会影响对象内部所有嵌套的属性
内部基于 ES6 的 Proxy 实现，通过代理对象操作源对象内部数据都是响应式的
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">reactive与ref-细节</h5>
<pre><code class="copyable">是Vue3的 composition API中2个最重要的响应式API
ref用来处理基本类型数据, reactive用来处理对象(递归深度响应式)
如果用ref对象/数组, 内部会自动将对象/数组转换为reactive的代理对象
ref内部: 通过给value属性添加getter/setter来实现对数据的劫持
reactive内部: 通过使用Proxy来实现对对象内部所有数据的劫持, 并通过Reflect操作对象内部数据
ref的数据操作: 在js中要.value, 在模板中不需要(内部解析模板时会自动添加.value)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">vue2与vue3的响应式</h5>
<pre><code class="copyable">/* Vue2的响应式 */
核心:
    对象: 通过defineProperty对对象的已有属性值的读取和修改进行劫持(监视/拦截)
    数组: 通过重写数组更新数组一系列更新元素的方法来实现元素修改的劫持
问题
    对象直接新添加的属性或删除已有属性, 界面不会自动更新
直接通过下标替换元素或更新length, 界面不会自动更新 arr[1] = &#123;&#125;

/* Vue3的响应式 */
核心:
    通过Proxy(代理): 拦截对data任意属性的任意(13种)操作, 包括属性值的读写, 属性的添加, 属性的删除等...
    通过 Reflect(反射): 动态对被代理对象的相应属性进行特定的操作
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">计算属性与监视</h5>
<pre><code class="copyable">/* computed函数: */
    与computed配置功能一致
    只有getter
    有getter和setter
/* watch函数 */
    与watch配置功能一致
    监视指定的一个或多个响应式数据, 一旦数据变化, 就自动执行监视回调
    默认初始时不执行回调, 但可以通过配置immediate为true, 来指定初始时立即执行第一次
    通过配置deep为true, 来指定深度监视
/* watchEffect函数 */
    不用直接指定要监视的数据, 回调函数中使用的哪些响应式数据就监视哪些响应式数据
    默认初始时就会执行第一次, 从而可以收集需要监视的数据
    监视数据发生变化时回调
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">自定义hook函数</h5>
<pre><code class="copyable">1.使用Vue3的组合API封装的可复用的功能函数
2.自定义hook的作用类似于vue2中的mixin技术
3.自定义Hook的优势: 很清楚复用功能代码的来源, 更清楚易懂
4.利用TS泛型强化类型检查
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">toRefs</h5>
<pre><code class="copyable">把一个响应式对象转换成普通对象，该普通对象的每个 property 都是一个 ref
应用: 当从合成函数返回响应式对象时，toRefs 非常有用，这样消费组件就可以在不丢失响应式的情况下对返回的对象进行分解使用
问题: reactive 对象取出的所有属性值都是非响应式的
解决: 利用 toRefs 可以将一个响应式 reactive 对象的所有原始属性转换为响应式的 ref 属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">Composition API（其他部分）</h4>
<h5 data-id="heading-14">shallowReactive 与 shallowRef</h5>
<pre><code class="copyable">shallowReactive : 只处理了对象内最外层属性的响应式(也就是浅响应式)
shallowRef: 只处理了value的响应式, 不进行对象的reactive处理
什么时候用浅响应式呢?
    一般情况下使用ref和reactive即可
    如果有一个对象数据, 结构比较深, 但变化时只是外层属性变化 ===> shallowReactive
    如果有一个对象数据, 后面会产生新的对象来替换 ===> shallowRef
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">readonly 与 shallowReadonly</h5>
<pre><code class="copyable">readonly:
    深度只读数据
    获取一个对象 (响应式或纯对象) 或 ref 并返回原始代理的只读代理。
    只读代理是深层的：访问的任何嵌套 property 也是只读的。
shallowReadonly
    浅只读数据
    创建一个代理，使其自身的 property 为只读，但不执行嵌套对象的深度只读转换
应用场景:
    在某些特定情况下, 我们可能不希望对数据进行更新的操作, 那就可以包装生成一个只读代理对象来读取数据, 而不能修改或删除
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">toRaw 与 markRaw</h5>
<pre><code class="copyable">toRaw
    返回由 reactive 或 readonly 方法转换成响应式代理的普通对象。
    这是一个还原方法，可用于临时读取，访问不会被代理/跟踪，写入时也不会触发界面更新。
markRaw
    标记一个对象，使其永远不会转换为代理。返回对象本身
应用场景:
    有些值不应被设置为响应式的，例如复杂的第三方类实例或 Vue 组件对象。
    当渲染具有不可变数据源的大列表时，跳过代理转换可以提高性能。
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">toRef</h5>
<pre><code class="copyable">为源响应式对象上的某个属性创建一个 ref对象, 二者内部操作的是同一个数据值, 更新时二者是同步的
区别ref: 拷贝了一份新的数据值单独操作, 更新时相互不影响
应用: 当要将 某个prop 的 ref 传递给复合函数时，toRef 很有用
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">customRef</h5>
<pre><code class="copyable">创建一个自定义的 ref，并对其依赖项跟踪和更新触发进行显式控制
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">provide 与 inject</h5>
<pre><code class="copyable">provide和inject提供依赖注入，功能类似 2.x 的provide/inject
实现跨层级组件(祖孙)间通信
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">响应式数据的判断</h5>
<pre><code class="copyable">isRef: 检查一个值是否为一个 ref 对象
isReactive: 检查一个对象是否是由 reactive 创建的响应式代理
isReadonly: 检查一个对象是否是由 readonly 创建的只读代理
isProxy: 检查一个对象是否是由 reactive 或者 readonly 方法创建的代理
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">新组件</h4>
<h5 data-id="heading-22">Fragment(片断)</h5>
<pre><code class="copyable">在Vue2中: 组件必须有一个根标签
在Vue3中: 组件可以没有根标签, 内部会将多个标签包含在一个Fragment虚拟元素中
好处: 减少标签层级, 减小内存占用
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">Teleport(瞬移)</h5>
<pre><code class="copyable">Teleport 提供了一种干净的方法, 让组件的html在父组件界面外的特定标签(很可能是body)下插入显示
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">Suspense(不确定的)</h5>
<pre><code class="copyable">它们允许我们的应用程序在等待异步组件时渲染一些后备内容，可以让我们创建一个平滑的用户体验
<template>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            