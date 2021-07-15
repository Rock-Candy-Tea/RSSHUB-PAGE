
---
title: 'Vue3+Vite2+typescript的基础用法(1)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d67d212a80f74d79b2035eeefe7f1553~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 19:10:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d67d212a80f74d79b2035eeefe7f1553~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>虽然已经2021.7月了，但是靓仔还是没有项目真正用到vue3+vite2。所以在<a href="https://juejin.cn/post/6981734584568250376" target="_blank" title="https://juejin.cn/post/6981734584568250376">Vue3 + SSR + Vite</a>中承诺的出项目实战只能延后了。</p>
<p>之所以想写这篇文章，是因为靓仔自己也不怎么会Vue3+Vite2+Typesctripts（主要公司项目没用上这些东西）。所以就当给自己和大家查漏补缺吧。</p>
<h2 data-id="heading-1">主要内容</h2>
<ol>
<li>搭建vue3+vite2+ts的项目</li>
<li>vue3 composition api各种写法</li>
<li>vue3生命周期展示</li>
<li>集成 vuex@4和vue-router@4</li>
<li>集成axios</li>
<li>...（大家想到有什么想要了解的可以留言，我会在后续文章中去更新它）</li>
</ol>
<h3 data-id="heading-2">项目搭建</h3>
<p>大家可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2F%23scaffolding-your-first-vite-project" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/#scaffolding-your-first-vite-project" ref="nofollow noopener noreferrer">vite官方文档</a></p>
<p>由于我们项目中要使用到ts所以我们用<code>vue-ts</code>这个模板</p>
<pre><code class="copyable">npm init vite@latest my-vue-app --template vue-ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令运行完成后我们进入到项目<code>cd my-vue-app</code>执行<code>npm i && npm run dev</code> 然后打开浏览器，在url中输入<code>http://localhost:3000/</code>就能看到效果了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d67d212a80f74d79b2035eeefe7f1553~tplv-k3u1fbpfcp-watermark.image" alt="Image 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">composition api 各种写法演示</h3>
<p>我们使用<code>vscode</code>打开项目，打开<code>src/App.vue</code>后可以看到</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> HelloWorld <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/HelloWorld.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
    HelloWorld
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这个写法还是<code>vue2</code>的但是<code>vue3</code>去做了兼容。接下来把它改造成<code>vue3</code>的<code>setup</code>写法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> HelloWorld <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/HelloWorld.vue'</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>少了很多代码，但是项目还是可以运行，没有报错。细心的小伙伴可能会发现<code>name: 'App'</code>这个字段没有了。这就是其中的坑，一些自定义组件其他字段还是只能用<code>export default defineComponent(&#123;&#125;)</code>这个写法</p>
<p>然后打开<code>src/components/HelloWorld.vue</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-attr">setup</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> &#123; count &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改造后</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span> <span class="hljs-attr">setup</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
defineProps(&#123;
  <span class="hljs-attr">msg</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里多了两个在vue2中没见过的东西<code>ref, defineProps</code></p>
<h4 data-id="heading-4">props</h4>
<p><code>defineprops</code>可以看的出来是替代<code>props</code>的，<code>ref</code>可以看出来是替代<code>data</code>的。</p>
<p>我们先来说说<code>defineprops</code>的另外几种用法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
type Props = &#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
&#125;
defineProps<Props>()
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应该还有一种，但是这样运行起来会报错</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span>=<span class="hljs-string">"props"</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, toRefs, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> &#123; msg &#125; = toRefs(props)
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, toRefs, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-comment">// 这样写就没问题，很奇怪</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent( &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props: any</span>)</span> &#123; <span class="hljs-comment">// 这应该是(props: Props) 但是这个Props找不到引用的地方，就写了any</span>
    <span class="hljs-keyword">const</span> &#123;msg&#125; = toRefs(props);
    
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">return</span> &#123;msg, count&#125;
  &#125;,
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">ref, toRef, toRefs, reactive 用法跟区别</h4>
<p>首先我们先来看<code>ref</code>和<code>reactive</code>的几种写法用法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; state.msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.msg"</span>></span>
    &#123;&#123; item.msg &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClick"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, defineProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
type Props = &#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>;
&#125;;
defineProps<Props>();
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> state = ref<Props>(&#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"123"</span> &#125;);
<span class="hljs-keyword">const</span> list = ref<Props[]>();
<span class="hljs-built_in">console</span>.log(count.value);
<span class="hljs-built_in">console</span>.log(count);
list.value = [
  &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"item 1"</span> &#125;,
  &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"item 2"</span> &#125;,
  &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"item 3"</span> &#125;,
  &#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">"item 4"</span> &#125;,
];
<span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
  count.value++;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code><scripts></scripts></code>中你要访问<code>count</code>的变量的话必须要通过<code>count.value</code>，而在<code><template></template></code>中不需要</p>
<p>下面我们来看<code>reactive toRef toRefs</code>几种用法</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in data1.todoList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>></span>
      &#123;&#123; item &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClick"</span>></span>
      count is: &#123;&#123; data2.count &#125;&#125; double count is: &#123;&#123; data2.double &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>tempCount is &#123;&#123; tempCount &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>count is &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>double is &#123;&#123; double &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">setup</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive, onMounted, computed, toRef, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
type Todo = &#123;
  <span class="hljs-attr">id</span>: number;
  message: string;
  completed: boolean;
  time: string;
&#125;;
type State = &#123;
  <span class="hljs-attr">count</span>: number;
  double: number;
&#125;;
<span class="hljs-keyword">const</span> data1 = reactive(&#123;
  <span class="hljs-attr">todoList</span>: [] <span class="hljs-keyword">as</span> Todo[],
&#125;);
<span class="hljs-keyword">const</span> data2: State = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">double</span>: computed(<span class="hljs-function">() =></span> data2.count * <span class="hljs-number">2</span>),
&#125;);
<span class="hljs-keyword">const</span> tempCount = toRef(data2, <span class="hljs-string">"count"</span>);
<span class="hljs-keyword">const</span> &#123; count, double &#125; = toRefs(data2);
<span class="hljs-keyword">const</span> handleClick = <span class="hljs-function">() =></span> &#123;
  data2.count++;
&#125;;
onMounted(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> todos: Todo[] = [
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">"todo1"</span>,
      <span class="hljs-attr">completed</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">time</span>: <span class="hljs-string">"2021-7-15 07:00"</span>,
    &#125;,
    &#123;
      <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">"todo2"</span>,
      <span class="hljs-attr">completed</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">time</span>: <span class="hljs-string">"2021-7-15 07:00"</span>,
    &#125;,
  ];
  data1.todoList = todos;
  data1.todoList.push(&#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">"todo3"</span>,
    <span class="hljs-attr">completed</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">time</span>: <span class="hljs-string">"2021-7-15 07:00"</span>,
  &#125;);
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>reactive</code>和<code>ref</code>给我主观的感觉就是<code>reactive</code>声明响应式对象会比较方便，<code>ref</code>声明简单的变量比较方便。他们有很多异曲同工之处</p>
<h2 data-id="heading-6">结尾</h2>
<p>这次文章先写到这里（主要开头废话太多，怕篇幅太长，看的让人厌烦），现在就写了1和2两点。下篇文章我会更新<code>watch</code> <code>watchEffect</code> <code>context</code> <code>vue生命周期</code>的相关内容。</p>
<p>新人作者希望大家多多点赞👍</p>
<p>有什么意见、建议、写错的地方或者其他用法希望大家可以留言，大家互相学习一起进步</p>
<h2 data-id="heading-7">项目地址</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcxyxxx0924%2Fvue3-vite2-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cxyxxx0924/vue3-vite2-demo" ref="nofollow noopener noreferrer">github</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fchen-xinyou%2Fvue3-vite2-ts-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/chen-xinyou/vue3-vite2-ts-demo" ref="nofollow noopener noreferrer">gitee</a></li>
</ol></div>  
</div>
            