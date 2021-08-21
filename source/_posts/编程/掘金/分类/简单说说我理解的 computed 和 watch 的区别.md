
---
title: '简单说说我理解的 computed 和 watch 的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8382'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 01:47:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=8382'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. computed</h1>
<ul>
<li>computed 即计算属性，会根据所依赖的数据动态显示新的计算结果。</li>
<li>它不需要调用（即后面不用加圆括号）即可使用。</li>
<li>计算属性会根据依赖来自动缓存，如果依赖不变， computed 的值就不会重新计算。</li>
</ul>
<h4 data-id="heading-1">示例代码</h4>
<pre><code class="copyable">var vm = new Vue(&#123;
  el: '#app',
  data: &#123;
    message: 'hello'
  &#125;,
  template: `
  <div>
  <p>我是原始值: "&#123;&#123; message &#125;&#125;"</p>
  <p>我是计算属性的值: "&#123;&#123; computedMessage&#125;&#125;"</p> // computed 在 DOM 里直接使用不需要调用
  </div>
  `,
  computed: &#123;
    // 计算属性的 getter
    computedMessage: function () &#123;
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：<br>
我是原始值: "Hello"<br>
我是计算属性的值: "olleH"</p>
<h1 data-id="heading-2">2. watch</h1>
<ul>
<li>watch 即监听/侦听，是一个对象，键是 data 对应的数据，值是对应的回调函数。</li>
<li>值也可以是方法名，或包含选项的对象，当 data 的数据发生变化时，就会执行这个回调函数。</li>
<li>watch 有两个参数，一个 Val（修改后的 data 数据），一个 oldVal（原来的 data 数据）。</li>
<li>Vue 实例会在实例化时调用 $watch()，遍历 watch 对象的每一个属性。</li>
</ul>
<h4 data-id="heading-3">示例代码</h4>
<pre><code class="copyable">new Vue(&#123;
  data: &#123;
    n: 0,
    obj: &#123;
      a: "a"
    &#125;
  &#125;,
  template: `
    <div>
      <button @click="n += 1">n+1</button>
      <button @click="obj.a += 'hi'">obj.a + 'hi'</button>
      <button @click="obj = &#123;a:'a'&#125;">obj = 新对象</button>
    </div>
  `,
  watch: &#123;
    n() &#123;
      console.log("n 变了");
    &#125;,
    obj:&#123;
      handler: function (val, oldVal) &#123; 
      console.log("obj 变了")
    &#125;,
      deep: true // 该属性设定在任何被侦听的对象的 property 改变时都要执行 handler 的回调，不论其被嵌套多深
    &#125;,
    "obj.a":&#123;
      handler: function (val, oldVal) &#123; 
      console.log("obj.a 变了")
    &#125;,
      immediate: true // 该属性设定该回调将会在侦听开始之后被立即调用
    &#125;
  &#125;
&#125;).$mount("#app");
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">watch 有2个属性：immediate 和 deep</h3>
<ul>
<li>immediate 表示是否在第一次渲染时执行这个函数，对应的值为（ true / false ）。</li>
<li>deep 表示如果我们监听一个对象，是否需要监听对象里面属性的变化，对应的值为（ true / false ）。</li>
<li>注意应该使用箭头函数来定义 watch 函数，因为箭头函数没有 this ，它的 this 会继承它上面的函数，所以箭头函数的 this 指向了 window.this 而不是 Vue 实例。</li>
</ul>
<h3 data-id="heading-5">vm.$watch() 的用法和 watch 回调类似</h3>
<ul>
<li>vm.$watch('data 属性名', fn, &#123;deep: true / false, immediate: true / false&#125;)</li>
</ul>
<h4 data-id="heading-6">示例</h4>
<pre><code class="copyable">vm.$watch("n", function(val, newVal)&#123;
     console.log("n 变了");
&#125;,&#123;deep: true, immediate: true&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">总结</h1>
<ul>
<li>如果数据要<strong>通过复杂计算得出结果</strong>，就使用 <strong>computed</strong> 。</li>
<li>如果数据需要被<strong>监听</strong>并对其<strong>进行一些操作</strong>就使用 <strong>watch</strong> 。</li>
</ul></div>  
</div>
            