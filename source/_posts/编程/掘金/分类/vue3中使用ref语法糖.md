
---
title: 'vue3中使用ref语法糖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9871'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 06:44:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=9871'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>自从引入组合式 API 的概念以来，一个主要的未解决的问题就是 ref 和响应式对象到底用哪个。响应式对象存在解构丢失响应性的问题，而 ref 需要到处使用 .value 则感觉很繁琐，并且在没有类型系统的帮助时很容易漏掉 .value</p>
</blockquote>
<p>以上是官方原话,大概就是新的语法糖,可以让我们更方便的使用ref,而不用每次都写.value,大概就是把这样的代码,简化成这样</p>
<pre><code class="hljs language-vue copyable" lang="vue">
<script setup lang="ts">
import &#123; ref &#125; from 'vue'

const count = ref(0)

console.log(count.value)

function increment() &#123;
  count.value++
&#125;
</script>

<template>
  <button @click="increment">&#123;&#123; count &#125;&#125;</button>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简化成这样</p>
<pre><code class="hljs language-vue copyable" lang="vue"><script setup lang="ts">
let count = $ref(0)

console.log(count)

function increment() &#123;
  count++
&#125;
</script>

<template>
  <button @click="increment">&#123;&#123; count &#125;&#125;</button>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每一个会返回 ref 的响应式 API 都有一个相对应的、以 $ 为前缀的宏函数。包括以下这些 API：</p>
<ol>
<li>ref -> $ref</li>
<li>computed -> $computed</li>
<li>shallowRef -> $shallowRef</li>
<li>customRef -> $customRef</li>
<li>toRef -> $toRef</li>
</ol>
<p>多余的不再赘述,大家可以自行查看官方文档,接下来我们来看看这个语法糖的具体使用,在项目中怎么配置</p>
<h4 data-id="heading-0">第一步(必须),在vite中启用语法糖开关</h4>
<p>打开vite.config.ts,添加如下代码</p>
<pre><code class="hljs language-ts copyable" lang="ts">    <span class="hljs-title function_">vue</span>(&#123;
      <span class="hljs-attr">reactivityTransform</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用响应式语法糖$ref $computed $toRef</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">第二步(可选),配置tsconfig.json</h4>
<p>在compilerOptions下添加vue/ref-macros,
不然会报错<code>TS2304: Cannot find name '$ref'</code>.虽然不影响使用,但是会影响开发体验</p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-attr">"compilerOptions"</span><span class="hljs-punctuation">:</span><span class="hljs-punctuation">&#123;</span>
    ...
    <span class="hljs-attr">"types"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"vue/ref-macros"</span><span class="hljs-punctuation">]</span> 
  <span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">第三步(可选),配置eslint</h4>
<p>在eslintrc.cjs中加上global,不然会提示<code>ESLint: '$ref' is not defined.(no-undef)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  ...
  <span class="hljs-attr">globals</span>: &#123;
    <span class="hljs-attr">$ref</span>: <span class="hljs-string">"readonly"</span>,
    <span class="hljs-attr">$computed</span>: <span class="hljs-string">"readonly"</span>,
    <span class="hljs-attr">$shallowRef</span>: <span class="hljs-string">"readonly"</span>,
    <span class="hljs-attr">$customRef</span>: <span class="hljs-string">"readonly"</span>,
    <span class="hljs-attr">$toRef</span>: <span class="hljs-string">"readonly"</span>,
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">如果不嫌麻烦,又不想代码中总是有误报错误的行为,可以直接在vue代码中引入<code>vue/ref-macros</code>,这样就不用配置<code>tsconfig.json</code>和<code>eslint</code>了,也就是刚刚写的第二,第三步</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><script setup lang="ts">
import &#123; $ref &#125; from "vue/macros";
let count = $ref(0)

console.log(count)

function increment() &#123;
  count++
&#125;
</script>

<template>
  <button @click="increment">&#123;&#123; count &#125;&#125;</button>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs copyable"><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            