
---
title: 'vue3改动和使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807f8c42bbce4745a60ab866b091031a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 21:54:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807f8c42bbce4745a60ab866b091031a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue3带来的新变化</h1>
<h2 data-id="heading-1">优化</h2>
<ol>
<li>
<p>性能提升（零成本：从vue2切到vue3就享受到）</p>
<p>首次渲染更快，diff算法更快，内存占用更少，打包体积更小，....</p>
</li>
<li>
<p>更好的Typescript支持（在vue下写TS更方便了）</p>
</li>
<li>
<p>提供新的写代码的方式：Composition API <strong>（需要学习成本）</strong></p>
</li>
</ol>
<p>相关阅读： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/" ref="nofollow noopener noreferrer">Vue3 中文文档</a>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fvue-composition%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/vue-composition/" ref="nofollow noopener noreferrer">Vue3 设计理念</a></p>
<p>支持 vue3 的UI组件库: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fantdv.com%2Fdocs%2Fvue%2Fintroduce-cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://antdv.com/docs/vue/introduce-cn/" ref="nofollow noopener noreferrer">ant-design-vue</a>, <a href="https://link.juejin.cn/?target=https%3A%2F%2Felement-plus.gitee.io%2F%23%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://element-plus.gitee.io/#/zh-CN" ref="nofollow noopener noreferrer">element-plus</a>, <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvant-contrib.gitee.io%2Fvant%2Fv3%2F%23%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://vant-contrib.gitee.io/vant/v3/#/zh-CN" ref="nofollow noopener noreferrer">vant</a></strong></p>
<p>基于composition组合api的常用集合 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/" ref="nofollow noopener noreferrer">VueUse</a></p>
<h2 data-id="heading-2">Vue2在Vue3中被废弃的部分</h2>
<p>vue3.0对于2.0版本的大部分语法都是可以兼容的（之前是怎么写的，现在也正常写），但是也有一些破坏性的语法更新，这个大家要格外注意</p>
<ol>
<li>移除了$on方法 （eventBus现有实现模式不再支持，可以使用三方插件替代）</li>
<li>移除过滤器选项 （插值表达式里不能再使用过滤器filter， 可以使用methods替代）</li>
<li>移除 .sync语法（v-bind时不能使用.sync修饰符了，现在它v-model语法合并了）</li>
</ol>
<p>更多阅读，参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Fmigration%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/migration/introduction.html" ref="nofollow noopener noreferrer">官网</a></p>
<h1 data-id="heading-3">开发环境搭建</h1>
<h2 data-id="heading-4">创建项目</h2>
<p>命令：Vue create 项目名</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807f8c42bbce4745a60ab866b091031a~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-07-13_12-12-42.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选中 Vue3 Preview</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11d9067a96b447fdb7a2264e4be900d1~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-07-13_12-11-51.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">版本报错</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51fab98741ca408aad48f6f14ba7e1e9~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-07-13_13-46-07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>手动下载版本 : npm i vue-loader-v16</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f77df4253cf84b3dbfacfc859d841d1f~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-07-13_13-48-34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">目录分析</h1>
<p>主要看三个位置：</p>
<ol>
<li>package.json</li>
<li>main.js</li>
<li>app.vue</li>
</ol>
<h2 data-id="heading-7">package.json</h2>
<p>首先我们可以看一下<code>package.json</code>文件，在dependencies配置项中显示，我们当前使用的版本为3.0.0</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"core-js"</span>: <span class="hljs-string">"^3.6.5"</span>,
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^3.0.0"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">main.js</h2>
<p>然后打开<code>main.js</code> 入口文件，发现Vue的实例化发生了一些变化，由先前的new关键词实例化，转变为createApp方法的调用形式 。</p>
<p>vue2.x中的写法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue3.x的写法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span> <span class="hljs-comment">// 根组件</span>
createApp(App).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">app.vue</h2>
<p>打开app.vue发现：vue3.0的单文件组件中不再强制要求必须有唯一根元素</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"Vue logo"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./assets/logo.png"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Welcome to Your Vue.js App"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            