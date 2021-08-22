
---
title: '一篇文章搞定Vue中的混入mixin！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4848'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 23:57:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=4848'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue-mixin(混入)</h1>
<h3 data-id="heading-1">1.官方定义：</h3>
<h6 data-id="heading-2">混入 (mixin) 提供了一种非常灵活的方式，来分发 Vue 组件中的可复用功能。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。</h6>
<h3 data-id="heading-3">2.功能：</h3>
<h6 data-id="heading-4">把多个组件共用的配置提取成一个混入对象</h6>
<h3 data-id="heading-5">3.使用场景</h3>
<h6 data-id="heading-6">多个组件中都用到了一些公用的方法、数据时。</h6>
<h3 data-id="heading-7">4.使用方法：</h3>
<h5 data-id="heading-8">第一步定义混合</h5>
<p>新建一个mixin文件夹，创建一个JS文件</p>
<pre><code class="copyable">export const myMixin = &#123;
 mounted() &#123;
  console.log("1111")
 &#125;,
 data() &#123;
  return &#123;
   x: 1
  &#125;
 &#125;,
 methods: &#123;
  showModel() &#123;
   alert(this.name);
  &#125;
 &#125;,
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">记得导出~</h6>
<h5 data-id="heading-10">第二步使用混入</h5>
<h6 data-id="heading-11">首先在要使用的组件中import引入</h6>
<pre><code class="copyable">import &#123;myMixin&#125; from "../mixin/mixin1.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">然后注册</h6>
<p>（1）.局部混入：<strong>mixins: [myMixin1，myMixin2 ]</strong></p>
<p>（2）.全局混入： Vue.mixin(xxxx)</p>
<h5 data-id="heading-13">混入可以进行全局注册。使用时格外小心！一旦使用全局混入，它将影响<strong>每一个</strong>之后创建的 Vue 实例。使用恰当时，这可以用来为自定义选项注入处理逻辑。</h5>
<h3 data-id="heading-14">5.选项合并</h3>
<p>（1） 数据对象data在内部会进行递归合并，并在发生冲突时以组件数据优先。</p>
<p>（2）同名钩子函数将合并为一个数组，因此都将被调用。另外，混入对象的钩子将在组件自身钩子<strong>之前</strong>调用。</p>
<p>（3）值为对象的选项，例如 <code>methods</code>、<code>components</code> 和 <code>directives</code>，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对。</p>
<h3 data-id="heading-15">6.拓展</h3>
<h5 data-id="heading-16">（1）.组件引入多个混入时，执行顺序问题</h5>
<h6 data-id="heading-17">执行顺序与引入（import）顺序无关，而与注册顺序（<strong>mixins: [myMixin1，myMixin2]</strong> ）有关，先注册的先执行。</h6>
<h5 data-id="heading-18">（2）.组件引入多个混入时，冲突问题</h5>
<h6 data-id="heading-19">数据对象（data）在内部会进行递归合并，在发生冲突时，后注册的混入中的数据会覆盖前面的数据。</h6>
<h6 data-id="heading-20">同名钩子函数将合并为一个数组，因此都将被调用。执行顺序与注册顺序一致。</h6>
<h6 data-id="heading-21">值为对象的选项，例如 <code>methods</code>、<code>components</code> 和 <code>directives</code>，将被合并为同一个对象。发生冲突时，取后注册的键值对。</h6>
<h5 data-id="heading-22">（3）. 与vuex的区别</h5>
<h6 data-id="heading-23">vuex：用来做状态管理的，里面定义的变量在每个组件中均可以使用和修改，在任一组件中修改此变量的值之后，其他组件中此变量的值也会随之修改</h6>
<h6 data-id="heading-24">Mixins：可以定义共用的变量，在每个组件中使用，引入组件中之后，各个变量是相互独立的，值的修改在组件中不会相互影响</h6>
<h5 data-id="heading-25">（4）.与公共组件的区别</h5>
<h6 data-id="heading-26">组件：在父组件中引入组件，相当于在父组件中给出一片独立的空间供子组件使用: 然后根据props来传值，但本质上两者是相对独立的</h6>
<h6 data-id="heading-27">Mixins：则是在引入组件之后与组件中的对象和方法进行合并，相当于扩展了父组件的对象与方法，可以理解为形成了一个新的组件</h6>
<h5 data-id="heading-28">（5）.与Vue.extend()区别</h5>
<h6 data-id="heading-29">Vue.extend()</h6>
<ul>
<li>
<p><strong>用法</strong>：</p>
<h6 data-id="heading-30">使用基础 Vue 构造器，创建一个“子类”。参数是一个包含组件选项的对象。</h6>
<p><code>data</code> 选项是特例，需要注意 - 在 <code>Vue.extend()</code> 中它必须是函数</p>
<pre><code class="copyable"><div id="mount-point"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 创建构造器
var Profile = Vue.extend(&#123;
  template: '<p>&#123;&#123;firstName&#125;&#125; &#123;&#123;lastName&#125;&#125; aka &#123;&#123;alias&#125;&#125;</p>',
  data: function () &#123;
    return &#123;
      firstName: 'Walter',
      lastName: 'White',
      alias: 'Heisenberg'
    &#125;
  &#125;
&#125;)
// 创建 Profile 实例，并挂载到一个元素上。
new Profile().$mount('#mount-point')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<pre><code class="copyable"><p>Walter White aka Heisenberg</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>区别</strong>：</p>
<h6 data-id="heading-31">①.两个都可以理解为继承，</h6>
<h6 data-id="heading-32">mixins接收对象数组，可引入多个</h6>
<h6 data-id="heading-33">extends接收的是对象或函数,只能暴露一个<code>extends</code>对象。</h6>
<h6 data-id="heading-34">②.<code>extends</code>会比<code>mixins</code>先执行。</h6>
<h6 data-id="heading-35">③.mixins类似于面向切片编程（AOP）</h6>
<h6 data-id="heading-36">extend用于创建Vue实例，他类似于面向对象编程</h6>
</li>
</ul>
<h5 data-id="heading-37">(6).<code>mixins</code>中的异步请求</h5>
<ul>
<li>
<h6 data-id="heading-38">当混合里面包含异步请求函数，而我们又需要在组件中使用异步请求函数的返回值时，我们应不要返回结果而是直接返回异步函数</h6>
</li>
</ul>
<p>参考文章链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_45045593%2Farticle%2Fdetails%2F107895946" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_45045593/article/details/107895946" ref="nofollow noopener noreferrer">blog.csdn.net/weixin_4504…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_26443535%2Farticle%2Fdetails%2F107803358%3Fops_request_misc%3D%25257B%252522request%25255Fid%252522%25253A%252522162920279716780271594474%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fall.%252522%25257D%26request_id%3D162920279716780271594474%26biz_id%3D0%26utm_medium%3Ddistribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-3-107803358.pc_search_download_positive%26utm_term%3Dmixin%25E4%25B8%258Eextend%26spm%3D1018.2226.3001.4187" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_26443535/article/details/107803358?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162920279716780271594474%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=162920279716780271594474&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-3-107803358.pc_search_download_positive&utm_term=mixin%E4%B8%8Eextend&spm=1018.2226.3001.4187" ref="nofollow noopener noreferrer">blog.csdn.net/qq_26443535…</a></p>
<p>\</p></div>  
</div>
            