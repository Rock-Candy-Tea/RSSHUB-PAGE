
---
title: 'vue中mixin用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebef9025e04b46b6b920e0c1668e0097~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 23:11:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebef9025e04b46b6b920e0c1668e0097~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebef9025e04b46b6b920e0c1668e0097~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">mixins出现的原因？</h1>
<p>我们在开发组件的过程中，常常会遇到一些具有相同逻辑和功能的组件，如果每个组件各写一套方法会导致代码冗余，后期更改的时候也要一个个的改非常的浪费时间和精力，所以需要将这些多个相同的逻辑抽离出来，各个组件只需要引入，就能实现一次写代码，多组件复用，由此mixin便来了。</p>
<h1 data-id="heading-1">mixins是什么？</h1>
<blockquote>
<p>混入 (mixin) 提供了一种非常灵活的方式，来分发Vue组件中的可复用功能。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。</p>
<p>mixin可以简单理解为一个普通的js文件。</p>
</blockquote>
<p>例子：</p>
<pre><code class="copyable">// 定义一个混入对象
var myMixin = &#123;
  created: function () &#123;
    this.hello()
  &#125;,
  methods: &#123;
    hello: function () &#123;
      console.log('hello from mixin!')
    &#125;
  &#125;
&#125;
​
// 定义一个使用混入对象的组件
var Component = Vue.extend(&#123;
  mixins: [myMixin]
&#125;)
​
var component = new Component() // => "hello from mixin!"
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">mixin和mixins区别</h1>
<h2 data-id="heading-3">mixin</h2>
<blockquote>
<p><code>mixin</code> 用于全局混入，会影响到每个组件实例，通常插件都是这样做初始化的。使用时格外小心！一旦使用全局混入，它将影响<strong>每一个</strong>之后创建的 Vue 实例。使用恰当时，这可以用来为自定义选项注入处理逻辑</p>
</blockquote>
<pre><code class="copyable">// 为自定义的选项 'myOption' 注入一个处理器。
Vue.mixin(&#123;
  created: function () &#123;
    var myOption = this.$options.myOption
    // 这种方式会影响到每个组件的created钩子函数
    if (myOption) &#123;
      console.log(myOption)
    &#125;
  &#125;
&#125;)
​
new Vue(&#123;
  myOption: 'hello!'
&#125;)
// => "hello!"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<p>请谨慎使用全局混入，因为它会影响每个单独创建的 Vue 实例 (包括第三方组件)。大多数情况下，只应当应用于自定义选项，就像上面示例一样。</p>
<h2 data-id="heading-4">mixins</h2>
<p>组件中单独混入，即局部混入。是我们最常使用的扩展组件的方式了。如果多个组件中有相同的业务逻辑，就可以将这些逻辑剥离出来，通过 <code>mixins</code> 混入代码。</p>
<h1 data-id="heading-5">mixins如何使用</h1>
<ol>
<li>用一个js文件将vue的script部分抽离出来，如下形式</li>
<li>在需要引入mixins的组件引入即可</li>
</ol>
<p>看个例子：</p>
<pre><code class="copyable">// common.js
export default &#123;
  data()&#123;
    return &#123;&#125;
  &#125;,
  methods:&#123;&#125;,
  computed:&#123;&#125;,
  filters:&#123;&#125;,
  created()&#123;&#125;,
  mounted()&#123;
    console.log("我是mixins");
  &#125;
&#125;
​
// .vue组件
<template>
  <div class="wrapper">
    了解mixin
  </div>
</template>
​
<script>
import common from '@/mixin/common.js'
export default &#123;
  mixins: [common],
  mounted()&#123;
    console.log('我是当前组件');
  &#125;
&#125;
</script>
// 输出
我是mixins
我是当前组件
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">选项合并</h2>
<p>当组件和混入对象含有同名选项时，这些选项将以恰当的方式进行“合并”，比如，数据对象在内部会进行递归合并，并在发生冲突时以组件数据优先。</p>
<pre><code class="copyable">var mixin = &#123;
  data: function () &#123;
    return &#123;
      message: 'hello',
      foo: 'abc'
    &#125;
  &#125;
&#125;
​
new Vue(&#123;
  mixins: [mixin],
  data: function () &#123;
    return &#123;
      message: 'goodbye',
      bar: 'def'
    &#125;
  &#125;,
  created: function () &#123;
    console.log(this.$data)
    // => &#123; message: "goodbye", foo: "abc", bar: "def" &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同名钩子函数将合并为一个数组，因此都将被调用。另外，混入对象的钩子将在组件自身钩子<strong>之前</strong>调用</p>
<pre><code class="copyable">var mixin = &#123;
  created: function () &#123;
    console.log('混入对象的钩子被调用')
  &#125;
&#125;
​
new Vue(&#123;
  mixins: [mixin],
  created: function () &#123;
    console.log('组件钩子被调用')
  &#125;
&#125;)
​
// => "混入对象的钩子被调用"
// => "组件钩子被调用"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值为对象的选项，例如 <code>methods</code>、<code>components</code> 和 <code>directives</code>，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对</p>
<pre><code class="copyable">var mixin = &#123;
  methods: &#123;
    poo: function () &#123;
      console.log('poo')
    &#125;,
    conflicting: function () &#123;
      console.log('from mixin')
    &#125;
  &#125;
&#125;
​
var vm = new Vue(&#123;
  mixins: [mixin],
  methods: &#123;
    far: function () &#123;
      console.log('far')
    &#125;,
    conflicting: function () &#123;
      console.log('from self')
    &#125;
  &#125;
&#125;)
​
vm.foo() // => "poo"
vm.bar() // => "far"
vm.conflicting() // => "from self"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<code>Vue.extend()</code> 也使用同样的策略进行合并</p>
<h1 data-id="heading-7">mixins合并规则总结</h1>
<ol>
<li>
<p>如果是data函数的返回值对象</p>
<ul>
<li>返回值对象默认情况下会进行合并</li>
<li>如果data返回值对象的属性发生了冲突，那么会保留组件自身的数据</li>
</ul>
</li>
<li>
<p>生命周期钩子函数合并</p>
<ul>
<li>生命周期的钩子函数会被合并到数组中，都会被调用</li>
<li>先执行Mixin中对应的逻辑，在执行组件中对应生命周期钩子的逻辑</li>
</ul>
</li>
<li>
<p>值为对象的选项，例如 methods、components 和 directives，将被合并为同一个对象</p>
<ul>
<li>比如都有methods选项，并且都定义了方法，那么它们都会生效</li>
<li>但是如果对象的key相同，那么会取组件对象的键值对</li>
</ul>
</li>
</ol>
<h1 data-id="heading-8">mixins的一些特性</h1>
<ol>
<li>
<p><strong>mixins中的生命周期会与引入mixins的组件的生命周期整合在一起调用</strong></p>
</li>
<li>
<p><strong>值为对象的选项, 组件的data、methods、filters会覆盖mixins里的同名data、methods、filters</strong></p>
<p>如methods,components等，选项会被合并，键冲突的组件会覆盖混入对象的，比如混入对象里有个方法A，组件里也有方法A，这时候在组件里调用的话，执行的是组件里的A方法</p>
</li>
<li>
<p><strong>值为函数的选项，不同mixin里的同名方法，按照引进的顺序，最后的覆盖前面的同名方法</strong></p>
<p>如created,mounted等，就会被合并调用，混合对象里的钩子函数在组件里的钩子函数之前调用，同一个钩子函数里，会先执行混入对象的东西，再执行本组件的</p>
</li>
<li>
<p><strong>方法和参数在各组件中不共享</strong></p>
<p>如混入对象中有一个 cont:1的变量,在组件A中改变cont值为5，这时候在组件B中获取这个值，拿到的还是1，还是混入对象里的初始值，数据不共享</p>
</li>
<li>
<p><strong>与vuex的区别</strong></p>
<p>vuex：用来做状态管理的，里面定义的变量在每个组件中均可以使用和修改，在任一组件中修改此变量的值之后，其他组件中此变量的值也会随之修改</p>
<p>mixins：可以定义共用的变量，在每个组件中使用，引入组件中之后，各个变量是相互独立的，值的修改在组件中不会相互影响</p>
</li>
<li>
<p><strong>与公共组件的区别</strong></p>
<p>组件：在父组件中引入组件，相当于在父组件中给出一片独立的空间供子组件使用，然后根据props来传值，但本质上两者是相对独立的</p>
</li>
</ol>
<h1 data-id="heading-9">mixins的缺点</h1>
<ol>
<li>
<p><strong>变量来源不明确（隐式传入）</strong> ：不利于阅读，使代码变得难以维护</p>
<p>组件里可以引入多个mixin，并直接隐式调用mixin里的变量/方法， 这会让我们有时候混乱这些变量/方法分别是哪个mixin里的</p>
</li>
<li>
<p><strong>属性命名冲突</strong>：多个mixins的生命周期会融合到一起运行，但是同名属性、同名方法无法融合，可能会导致冲突</p>
<p>比如组件1中的方法要输出属性info， 但是组件2中也有同名属性info，且覆盖了组件1中的属性info， 那么当执行组件1中的方法时，输出的确实组件2中的属性， 这个可以避免，但是一不小心就会导致冲突，很容易制造混乱</p>
</li>
<li>
<p><strong>复杂度较高</strong>：mixins和组件可能出现多对多的关系，（即一个组件可以引用多个mixins，一个mixins也可以被多个组件引用）</p>
</li>
<li>
<p><strong>不能轻易的重用代码</strong></p>
</li>
</ol></div>  
</div>
            