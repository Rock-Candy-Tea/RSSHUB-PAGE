
---
title: 'vue3.0初体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://s3.ax1x.com/2021/03/15/6D9mi8.md.png'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 02:27:46 GMT
thumbnail: 'https://s3.ax1x.com/2021/03/15/6D9mi8.md.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>好久不见，甚是想念；一日不见，如隔三秋；一天不打上房揭瓦；我觉得我就属于最后一句话吧。虽说二月很短但是也不是一直不学习的理由，虽然二月有个新年，也并不是我 不学习的理由；每次来总是这样哈哈哈哈，但是闲下来是真的需要学习啊 ，我还是需要挣money ，毕竟还要面朝大海春暖花开；毕竟还要劈柴喂马周游世界；还有粮食和蔬菜；还有未来媳妇的包包哈哈哈哈未来孩子的奥利奥。尤大已经发布vue3.0 有一阵子了，各大UI库也正完成适配，可以说vue3势在必行，所以还是跟紧我们的潮流，毕竟这是一个前端人员应有的敏锐感。</p>
</blockquote>
<ol>
<li>
<h4 data-id="heading-0">安装</h4>
<ul>
<li></li>
<li>
<p>和vue2.X类似使用vue-cli进行脚手架安装，当然我们一会讲一下vite工具安装</p>
<pre><code class="copyable">vue create hello 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://imgtu.com/i/6D9mi8" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.ax1x.com/2021/03/15/6D9mi8.md.png" alt="6D9mi8.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</li>
<li>
<p>如果没有上述界面说明需要升级你的vue-cli的版本</p>
<pre><code class="copyable">vue update -g @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>可以选择Vue 3 Preview，也可以选择Manually Select features 进行版本选择</p>
<p><a href="https://imgtu.com/i/6DCX4K" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.ax1x.com/2021/03/15/6DCX4K.md.png" alt="6DCX4K.md.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</li>
</ul>
</li>
<li>
<h4 data-id="heading-1">浅度对比</h4>
<ul>
<li>
<p>首先入口对比main.js（左边vue3右边vue2.x）;使用了createApp（）</p>
<p><a href="https://imgtu.com/i/6DiUW8" target="_blank" rel="nofollow noopener noreferrer"><img src="https://s3.ax1x.com/2021/03/15/6DiUW8.png" alt="6DiUW8.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</li>
<li>
<p>vue3 的 Template支持多个根标签，但是vue2.x只支持一个</p>
<pre><code class="hljs language-vue copyable" lang="vue">// vue2
<template>
  <div>根元素 示例</div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue">// vue3
<template>
  <div>根元素 示例 0</div>
  <h1>根元素 示例 1</h1>
  <h1>根元素 示例 2</h1>
</template> 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>vue3 使用组合式API</p>
<ul>
<li>
<p>原来vue2.x的data 、computed、watch、mounted等等都要return 出来才能访问到，当我们的组件变得更大时，<strong>逻辑关注点</strong>的列表也会增长。这可能会导致组件难以阅读和理解。（我们还是举个例子吧？我们有个一个审批的表，需要跑南边填一个选项，完了需要北边填一个选项，东边和西边也要，当你拿着这个表跑来跑去，你就会感觉很累，诶当有一天我们有个地方说这个属性可以集中把这些地方都跑了，就不用东西南北各处跑了。这不就清晰省事了 啊 ，那现在vue3中这个地方就是setup）</p>
</li>
<li>
<p>新的 <code>setup</code> 组件选项在创建组件<strong>之前</strong>执行，一旦 <code>props</code> 被解析，就作为组合式 API 的入口点。</p>
</li>
<li>
<p>warning由于在执行 <code>setup</code> 时，组件实例尚未被创建，因此在 <code>setup</code> 选项中没有 <code>this</code>。这意味着，除了 <code>props</code> 之外，你将无法访问组件中声明的任何属性——<strong>本地状态</strong>、<strong>计算属性</strong>或<strong>方法</strong></p>
</li>
<li>
<p>使用ref 使任何响应式变量在任何地方起作用，如下所示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; user &#125; = toRefs(props)
<span class="hljs-keyword">const</span> repositories = ref([])
<span class="hljs-keyword">const</span> getUserRepositories = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-comment">// 更新 `prop.user` 到 `user.value` 访问引用值</span>
  repositories.value = <span class="hljs-keyword">await</span> fetchUserRepositories(user.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>注意ref、reactive、toRef、toRefs的区别</p>
</li>
</ul>
</li>
<li>
<p>vue3中的组件上的v-model 用法已更改，替换v-bind.sync</p>
<pre><code class="hljs language-vue copyable" lang="vue">// 在2.x中 
<ChildComponent v-model="pageTitle" />
<!--是以下的简写：-->
<ChildComponent :value ="pageTitle" @input ="pageTitle=$event" />
<!--如果要将属性或者事件名称改为其他，则需要在ChildComponent组件中添加model选项-->
// childCompnent.vue
<script>
export default &#123;
  model: &#123;
    prop: 'title',
    event: 'change'
  &#125;,
  props: &#123;
      // 这将允许 `value` 属性用于其他用途
      value: String,
      // 使用 `title` 代替 `value` 作为 model 的 prop
      title: &#123;
        type: String,
        default: 'Default title'
      &#125;
    &#125;
  &#125;
  methods:&#123;
    change()&#123;
      this.$emit('cc','我被子组件改变了')
    &#125;
  &#125;
</script>
<!--所以，这个栗子中的v-model是以下的简写-->
<ChildComponent :title="pageTitle" @change="pageTitle = $event" />
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue">//在3.x中 ，自定义组件上的v-model 相当于传递了modelValue prop并接收抛出的update：modelValue事件：
<ChildComponent v-model ="pageTitle" />
<!-- 是以下的简写 -->
<ChildComponent :modelValue ="pageTitle" @update:modelValue="pageTitle=$event" /> 
<!-- 若需要改变model名称，而不是改变组件内的model选项，那么现在我们可以将一个argument 传给model-->
<ChildComponent v-model:title ="pageTitle"/>
<!-- 是以下的简写 -->
<ChildComponent :title="pageTitle" @update:title="pageTitle = $event" />
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>新增context.emit，与this.$emit作用相同 （vue3中只能在methods中使用了，因为vue3的this与vue2的this不同了）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;SetupContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props: Prop, context: SetupContext</span>)</span> &#123;
    <span class="hljs-keyword">const</span> toggle = <span class="hljs-function">() =></span> &#123;
      context.emit(<span class="hljs-string">'input'</span>, !props.value)
    &#125;
    <span class="hljs-keyword">return</span> &#123;toggle&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>computed 计算属性与之前2.x 差不多，只是使用前要先引用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props: Prop, context: SetupContext</span>)</span> &#123;
  <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
 <span class="hljs-keyword">const</span> changCount = computed(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">return</span> count.value ++
  &#125;) 
  <span class="hljs-keyword">return</span> &#123;
    count
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>watchEffect监听</p>
<p>通过ref或者reactive去创建多个响应式的值，当任何一个值发生改变的时候，立即触发这个函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props: Prop, context: SetupContext</span>)</span> &#123;
  <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
  watchEffect(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(count)
  &#125;)
  <span class="hljs-keyword">return</span> &#123;
    count
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>如果有不正确的理解等彻底理解透之后，随时进行更新</p>
</li>
</ul>
</li>
<li>
<h4 data-id="heading-2">深度对比</h4>
<ul>
<li>
<p>在 vue 中， <code>Object.defineProperty</code> 无法监控到数据的下标变化，导致直接通过数组下标给数组设置新值时，无法做到实时响应。目前 vue 只针对数组的变异方法 <code>push/pop/shift/unshift/splice/sort/reverse</code> 做了 hack 处理，存在响应局限。<code>Proxy</code> 是 <code>ES6</code> 中新增的一个特性，翻译过来意思是"代理"，用在这里表示由它来“代理”某些操作。 <code>Proxy</code> 让我们能够以简洁易懂的方式控制外部对对象的访问。其功能非常类似于设计模式中的代理模式。</p>
<p><code>Proxy</code> 可以理解成，在目标对象之前架设一层“拦截”，外界对该对象的访问，都必须先通过这层拦截，因此提供了一种机制，可以对外界的访问进行过滤和改写。</p>
</li>
<li>
<p>其他下一篇进行补充</p>
</li>
</ul>
</li>
</ol></div>  
</div>
            