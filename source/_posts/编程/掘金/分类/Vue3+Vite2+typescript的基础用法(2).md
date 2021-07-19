
---
title: 'Vue3+Vite2+typescript的基础用法(2)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1880'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:52:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=1880'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>发布完<a href="https://juejin.cn/post/6984985230012579853#heading-1" target="_blank" title="https://juejin.cn/post/6984985230012579853#heading-1">Vue3+Vite2+typescript的基础用法(1)</a> 后我自己也仔细的看了一边，发现写的内容跟我一开始想的有很大的区别。比如一开始我想的是先挨个展示<code>vue2</code>和<code>vue3</code>的代码区别，比如<code>vue2 data</code>和<code>vue3 setup 中的data</code>，但是我只写了<code>vue3</code>的。而且我也只用了<code>vite脚手架</code>去创建了一个项目，在文章的内容中也没有再次提到<code>vite</code>。既然已经跑偏了，那就先按跑偏了的来吧😂</p>
</blockquote>
<h2 data-id="heading-1">主要内容</h2>
<ol>
<li>搭建vue3+vite2+ts的项目</li>
<li>⭐⭐vue3 setup语法糖与composition api各种写法</li>
<li>⭐⭐vue3生命周期展示</li>
<li>⭐⭐集成 vuex@4和axios</li>
<li>集成vue-router@4</li>
<li>ts介绍和配置</li>
<li>vite介绍与配置</li>
</ol>
<p>...（大家想到有什么想要了解的可以留言，我会在后续文章中去更新它）</p>
<p>上篇已经把如何搭建项目简单的写了一下，也介绍了<code>props</code>、<code>ref</code>、<code>reactive</code>、<code>toRef</code>、<code>toRefs</code>。这次要给大家展示的是<code>computed</code>、<code>watch</code>、<code>watchEffect</code>、<code>vue</code>的生命周期和项目集成<code>vuex</code>和<code>vue-router</code></p>
<h2 data-id="heading-2">setup 语法糖与composition api各种写法</h2>
<h3 data-id="heading-3">computed</h3>
<p><code>vue2</code> <code>computed</code>的使用方法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">plusOne</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.count++
    &#125;
  &#125;,
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>目前我知道<code>computed</code>在<code>vue3</code>中的用法有2种。在<code>setup</code>中可以把<code>computed</code>写在<code>reactive</code>上，还可以通过<code>set</code> <code>get</code>方法对<code>computed</code>赋值，总的来说比<code>vue2</code>更加的灵活多变了</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleAdd"</span>></span>Add count<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count: &#123;&#123; count1.count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>double: &#123;&#123; count1.double &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count1.count++"</span>></span>Add count1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>plusOne -> &#123;&#123; plusOne &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count2 &#123;&#123; count2 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>plusOne2 &#123;&#123; plusOne2 &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count2++"</span>></span>count2++</button
    ><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"plusOne2 = 0"</span>></span>count2 init<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, reactive, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
type Count = &#123;
  <span class="hljs-attr">count</span>: number;
  double: number;
&#125;;
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> count1: Count = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">double</span>: computed(<span class="hljs-function">() =></span> count1.count * <span class="hljs-number">2</span>),
&#125;);
<span class="hljs-keyword">const</span> plusOne = computed(<span class="hljs-function">() =></span> count.value + count1.count);
<span class="hljs-keyword">const</span> count2 = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> plusOne2 = computed(&#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> count2.value + <span class="hljs-number">1</span>,
  <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
    count2.value = val;
  &#125;,
&#125;);
<span class="hljs-keyword">const</span> handleAdd = <span class="hljs-function">() =></span> &#123;
  count.value++;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">watch</h3>
<p><code>watch</code>在<code>vue3</code>和<code>vue2</code>中区别不是很大，用法也是非常的像</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count -> &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>add one<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count1.count -> &#123;&#123; count1.count.count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count1.count.count++"</span>></span>add one<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive, ref, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
watch(
  <span class="hljs-function">() =></span> count.value,
  <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"count"</span>, count);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"prevCount"</span>, prevCount);
  &#125;
);
<span class="hljs-keyword">const</span> count1 = reactive(&#123; <span class="hljs-attr">count</span>: &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125; &#125;);
<span class="hljs-comment">// 跟vue2一样，层次比较深的话没办法直接被watch到，需要加上deep:true</span>
watch(<span class="hljs-function">() =></span> count1.count, <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"count"</span>, count);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"prevCount"</span>, prevCount);
&#125;, &#123;
  <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">immediate</span>: <span class="hljs-literal">false</span>
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">watchEffect</h3>
<p><code>watchEffect</code>在<code>vue2</code>和<code>vue3</code>中区别也不大</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-comment">/**
* 1.不需要手动传入依赖
* 2.不是lazy初始化执行分析依赖
* 3.无法获取原始值
* 4.一些异步操作放里面更加的合适
* 5.wacth第三个参数处理副作用的第一个参数
*/</span>
<span class="hljs-keyword">import</span> &#123; ref, defineProps, watchEffect, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
defineProps(&#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
&#125;);
<span class="hljs-keyword">const</span> num = ref(<span class="hljs-number">0</span>);
onMounted(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onMounted"</span>)
&#125;);
<span class="hljs-keyword">const</span> stop = watchEffect(<span class="hljs-function">(<span class="hljs-params">onInvalidate</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"watchEffed之前调用"</span>, num.value);
  onInvalidate(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">/** 清楚副作用 */</span>
  &#125;)
&#125;, &#123;
  <span class="hljs-attr">flush</span>:<span class="hljs-string">"sync"</span>,
  <span class="hljs-function"><span class="hljs-title">onTrigger</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-comment">//debugger;</span>
  &#125;
&#125;)
<span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
  num.value++;
  <span class="hljs-keyword">if</span>(num.value === <span class="hljs-number">10</span>) &#123;
    <span class="hljs-comment">//停用监听</span>
    stop()
    <span class="hljs-built_in">clearInterval</span>(interval)
  &#125;
&#125;, <span class="hljs-number">1000</span>);

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">vue3生命周期</h2>
<p><code>vue3</code>的生命周期和<code>vue2</code>的生命周期基本一样，就名字改了一下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-comment">// 开发 Hooks</span>
<span class="hljs-comment">/*   2.x与 3.x对比
 beforeCreate -> use setup()
 created -> use setup()
 beforeMount -> onBeforeMount
 mounted -> onMounted
 beforeUpdate -> onBeforeUpdate
 updated -> onUpdated
 beforeDestroy -> onBeforeUnmount
 destroyed -> onUnmounted
 errorCaptured -> onErrorCaptured
*/</span>
<span class="hljs-keyword">import</span> &#123;
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted,
  onErrorCaptured,
  defineProps
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

defineProps(&#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
&#125;);
onBeforeMount(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onBeforeMount"</span>);
&#125;);
onMounted(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onMounted!"</span>);
&#125;);
onBeforeUpdate(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onBeforeUpdate!"</span>);
&#125;);
onUpdated(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onUpdated!"</span>);
&#125;);
onBeforeUnmount(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onBeforeUnmount!"</span>);
&#125;);
onUnmounted(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onUnmounted!"</span>);
&#125;);
onErrorCaptured(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"onErrorCaptured!"</span>);
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">集成 <code>vuex@4</code>和<code>axios</code></h2>
<p><code>vuex</code>和<code>axios</code>应该不用介绍它们是什么吧😂</p>
<p>下面还是给大家分享它们在<code>composition api</code>中的使用方法</p>
<h3 data-id="heading-8">vuex@4</h3>
<p><code>vue3</code>中<code>vuex</code>的版本已经是V4了，首先我们按照<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.vuex.vuejs.org%2Fzh%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.vuex.vuejs.org/zh/index.html" ref="nofollow noopener noreferrer">官方文档</a>来安装依赖</p>
<pre><code class="hljs language-npm copyable" lang="npm">npm install vuex@next --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先创建<code>store/index.ts</code>，这里把<code>state</code>,<code>mutations</code>,<code>actions</code>,<code>getters</code>, <code>modules</code>的使用方法全部演示一边。</p>
<p>首先是<code>src/store/index.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> &#123; Counter, Person &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./module'</span>
<span class="hljs-keyword">const</span> store = createStore(&#123;
  <span class="hljs-attr">modules</span>: &#123;
    Counter,
    Person
  &#125;
&#125;)
<span class="hljs-keyword">export</span> &#123; store  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>src/store/</code>创建<code>StateType.d.ts</code>用来声明变量类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Commit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">interface</span> TPerson &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
&#125;

<span class="hljs-keyword">interface</span> TCount &#123;
  <span class="hljs-attr">count</span>: <span class="hljs-built_in">number</span>,
  <span class="hljs-attr">double</span>: <span class="hljs-built_in">number</span>,
&#125;

<span class="hljs-keyword">interface</span> ActionType &#123;
  <span class="hljs-attr">state</span>: TPerson,
  <span class="hljs-attr">commit</span>: Commit,
  <span class="hljs-attr">rootState</span>: TPerson
&#125;

<span class="hljs-keyword">export</span> &#123; TPerson, TCount, ActionType &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>src/store/</code>下创建<code>module/index.ts</code>、<code>Counter.ts</code>、<code>Person.ts</code></p>
<p><code>module/index.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Counter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./Counter'</span>
<span class="hljs-keyword">import</span> &#123; Person &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./Person'</span>

<span class="hljs-keyword">export</span> &#123;
  Counter,
  Person,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>module/Counter.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; TCount, ActionType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../StateType"</span>
<span class="hljs-keyword">const</span> Counter = &#123;
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">double</span>: <span class="hljs-number">0</span>
  &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">plusOne</span>(<span class="hljs-params">state: TCount</span>)</span> &#123;
      state.count++
      state.double = state.count * <span class="hljs-number">2</span>
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">delayPlus</span>(<span class="hljs-params">&#123; commit &#125;: ActionType</span>)</span> &#123;
      <span class="hljs-comment">// commit('plusOne')</span>
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        commit(<span class="hljs-string">'plusOne'</span>)
      &#125;, <span class="hljs-number">1000</span>);
    &#125;
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">composeNum</span>(<span class="hljs-params">state: TCount</span>)</span> &#123;
      <span class="hljs-keyword">return</span> state.count + state.double
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">export</span> &#123; Counter &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>module/Person.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; TPerson, ActionType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../StateType'</span>
<span class="hljs-keyword">const</span> Person = &#123;
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">0</span>
  &#125;),
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">setInfo</span>(<span class="hljs-params">state: TPerson, info: TPerson</span>)</span> &#123;
      state.name = info.name
      state.age = info.age
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">getPersonInfo</span>(<span class="hljs-params">&#123; state, commit, rootState &#125;: ActionType</span>)</span> &#123;
      <span class="hljs-comment">// if((state))</span>
      <span class="hljs-built_in">console</span>.log(state);
      <span class="hljs-built_in">console</span>.log(rootState);
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> info: TPerson = &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'XiaoMing'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>,
        &#125;
        commit(<span class="hljs-string">'setInfo'</span>, info)
      &#125;, <span class="hljs-number">1000</span>);
    &#125;
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params">state: TPerson</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">`my name is <span class="hljs-subst">$&#123;state.name&#125;</span> I'm <span class="hljs-subst">$&#123;state.age&#125;</span> years old`</span>
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">export</span> &#123; Person &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在<code>src/mian.ts</code>下把<code>store</code>加进去就好了</p>
<p><code>src/main.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> &#123; store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

<span class="hljs-keyword">const</span> app = createApp(App)
app.use(store);
app.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样整个<code>store</code>的配置就算完成了。接下来给大家展示一下怎么使用</p>
<p>⭐需要注意的是，在<code>setup()</code>中无法使用<code>this.$store</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.vuex.vuejs.org%2Fzh%2Fguide%2Fcomposition-api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.vuex.vuejs.org/zh/guide/composition-api.html" ref="nofollow noopener noreferrer">官网文档</a>上是</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> store = useStore()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而我的使用方法如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>count: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>double: &#123;&#123; double &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>composeNum: &#123;&#123; composeNum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handlePlusOne"</span>></span>plusOne<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handlePlusDelayOne"</span>></span>plusOne<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../store"</span>;

<span class="hljs-built_in">console</span>.log(store);
<span class="hljs-keyword">const</span> composeNum = computed(<span class="hljs-function">() =></span> store.getters[<span class="hljs-string">"Counter/composeNum"</span>]);
<span class="hljs-keyword">const</span> &#123; count, double &#125; = toRefs(store.state.Counter);
<span class="hljs-keyword">const</span> handlePlusOne = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(store.getters[<span class="hljs-string">"Counter/composeNum"</span>]);
  store.commit(<span class="hljs-string">"Counter/plusOne"</span>);
&#125;;
<span class="hljs-keyword">const</span> handlePlusDelayOne = <span class="hljs-function">() =></span> &#123;
  store.dispatch(<span class="hljs-string">"Counter/delayPlus"</span>);
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本来还想把<code>mapState, mapGetters, mapActions, mapMutations</code>这几个方法挨个演示一遍的，但是一直没弄出来，后续有实现的话我会在仓库中把这块内容给加上的。到这<code>vuex</code>的演示就结束了。接下来我们进入<code>vue-router</code></p>
<h3 data-id="heading-9">axios集成</h3>
<blockquote>
<p>本来这里是想写<code>vue-router@4</code>的，但是发现内容实在太多了，放这里的话篇幅又太长，而<code>axios</code>的话就简单配置一下，这样下次文章写<code>vue-router</code>和介绍<code>ts</code>就刚好了</p>
</blockquote>
<p>接下来我们来说一下<code>axios</code>的安装和配置，<code>axios</code>跟<code>vue</code>的版本没有关系，就装最新的就可以了</p>
<pre><code class="hljs language-npm copyable" lang="npm">npm i axios -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为<code>Axios</code>属于工具，所以我放到了<code>src/utils/axios.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">const</span> baseURL = <span class="hljs-string">'https://api.github.com'</span>

<span class="hljs-keyword">const</span> axios = Axios.create(&#123;
  baseURL,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">20000</span> <span class="hljs-comment">// 请求超时 20s</span>
&#125;)
<span class="hljs-comment">// 前置拦截器（发起请求之前的拦截）</span>
axios.interceptors.request.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
    <span class="hljs-comment">/**
     * 根据你的项目实际情况来对 config 做处理
     * 这里对 config 不做任何处理，直接返回
     */</span>
    <span class="hljs-keyword">return</span> response
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
)
<span class="hljs-comment">// 后置拦截器（获取到响应时的拦截）</span>
axios.interceptors.response.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
    <span class="hljs-comment">/**
     * 根据你的项目实际情况来对 response 和 error 做处理
     * 这里对 response 和 error 不做任何处理，直接返回
     */</span>
    <span class="hljs-keyword">return</span> response
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (error.response && error.response.data) &#123;
      <span class="hljs-keyword">const</span> code = error.response.status
      <span class="hljs-keyword">const</span> msg = error.response.data.message
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`Code: <span class="hljs-subst">$&#123;code&#125;</span>, Message: <span class="hljs-subst">$&#123;msg&#125;</span>`</span>)
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[Axios Error]`</span>, error.response)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`<span class="hljs-subst">$&#123;error&#125;</span>`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在需要使用<code>Axios</code>文件里，引入<code>Axios</code>配置文件，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>axios<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"../utils/axios"</span>;
axios
  .get(<span class="hljs-string">"/users/cxyxxx0924"</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"res: "</span>, res);
  &#125;)
  .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"err: "</span>, err);
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">总结</h2>
<blockquote>
<p>种一棵树最好是十年前其次是现在</p>
</blockquote>
<p>虽然<code>vue3</code>和<code>vite</code>发布已经是很长的一段时间了，但是很多大框架还是没有适配上<code>vue3</code>和<code>vite</code>。所以现在学起来，等<code>vue3</code>的生态跟<code>vue2</code>完全重合的时候，那我们就可以在公司的项目上or自己的项目上大展手脚。学习不怕晚，就怕你轻易放弃</p>
<p>下篇文章主要会写一下<code>vite</code>, <code>ts</code>的配置, <code>vue-router@4</code>的使用。希望各位靓仔，靓女们多多关注，多多点赞。有问题可以留言，我会第一时间回复你们的</p>
<h2 data-id="heading-11">项目地址&友情链接</h2>
<ol>
<li><a href="https://juejin.cn/post/6984985230012579853#heading-0" target="_blank" title="https://juejin.cn/post/6984985230012579853#heading-0">Vue3+Vite2+typescript的基础用法(1)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcxyxxx0924%2Fvue3-vite2-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cxyxxx0924/vue3-vite2-demo" ref="nofollow noopener noreferrer">项目源代码：github</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fchen-xinyou%2Fvue3-vite2-ts-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/chen-xinyou/vue3-vite2-ts-demo" ref="nofollow noopener noreferrer">项目源代码：gitee</a></li>
</ol>
<h2 data-id="heading-12">学习资料：</h2>
<ol>
<li><a href="https://juejin.cn/post/6951649464637636622" target="_blank" title="https://juejin.cn/post/6951649464637636622">从 0 开始手把手带你搭建一套规范的 Vue3.x 项目工程环境</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Rb4y1C7p3" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1Rb4y1C7p3" ref="nofollow noopener noreferrer">【阿崔cxr】vue3 的 script setup 语法糖定稿啦 快来看看香不香！！！</a></li>
</ol></div>  
</div>
            