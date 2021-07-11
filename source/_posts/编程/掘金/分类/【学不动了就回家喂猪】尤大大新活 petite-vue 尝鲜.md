
---
title: '【学不动了就回家喂猪】尤大大新活 petite-vue 尝鲜'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c8e67c799a9491694e9ee948e486654~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 08:03:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c8e67c799a9491694e9ee948e486654~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与好文召集令活动，点击查看<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c8e67c799a9491694e9ee948e486654~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开尤大大的GitHub，发现多了个叫 <strong>petite-vue</strong> 的东西，好家伙，Vue3 和 Vite 还没学完呢，又开始整新东西了？本着学不死就往死里学的态度，咱还是来瞅瞅这到底是个啥东西吧，谁让他是咱的祖师爷呢！</p>
<h3 data-id="heading-1">简介</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b778696a4a20430a97e5ffe22125dcd1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从名字来看可以知道 petite-vue 是一个 mini 版的vue，大小只有5.8kb，可以说是非常小了。据尤大大介绍，petite-vue 是 Vue 的可替代发行版，针对渐进式增强进行了优化。它提供了与标准 Vue 相同的模板语法和响应式模型：</p>
<ul>
<li>大小只有5.8kb</li>
<li>Vue 兼容模版语法</li>
<li>基于DOM，就地转换</li>
<li>响应式驱动</li>
</ul>
<h3 data-id="heading-2">上活</h3>
<p>下面对 petite-vue 的使用做一些介绍。</p>
<h4 data-id="heading-3">简单使用</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/petite-vue"</span> <span class="hljs-attr">defer</span> <span class="hljs-attr">init</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"&#123; count: 0 &#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count--"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 script 标签引入同时添加 init ，接着就可以使用 v-scope 绑定数据，这样一个简单的计数器就实现了。</p>
<blockquote>
<p>了解过 Alpine.js 这个框架的同学看到这里可能有点眼熟了，两者语法之间是很像的。</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--  Alpine.js  --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">x-data</span>=<span class="hljs-string">"&#123; open: false &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"open = true"</span>></span>Open Dropdown<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">x-show</span>=<span class="hljs-string">"open"</span> @<span class="hljs-attr">click.away</span>=<span class="hljs-string">"open = false"</span>></span>
    Dropdown Body
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了用 init 的方式之外，也可以用下面的方式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"&#123; count: 0 &#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count--"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-comment"><!--  放在body底部  --></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/petite-vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span>
    PetiteVue.createApp().mount()
  <span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或使用 ES module 的方式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    createApp().mount()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"&#123; count: 0 &#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count--"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">根作用域</h4>
<p>createApp 函数可以接受一个对象，类似于我们平时使用 data 和 methods 一样，这时 v-scope 不需要绑定值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    createApp(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
      <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.count++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.count--
      &#125;
    &#125;).mount()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">指定挂载元素</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    createApp(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;).mount(<span class="hljs-string">'#app'</span>)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123; count &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">生命周期</h4>
<p>可以监听每个元素的生命周期事件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    createApp(&#123;
      <span class="hljs-function"><span class="hljs-title">onMounted1</span>(<span class="hljs-params">el</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(el) <span class="hljs-comment">// <span>1</span></span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">onMounted2</span>(<span class="hljs-params">el</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(el) <span class="hljs-comment">// <span>2</span></span>
      &#125;
    &#125;).mount(<span class="hljs-string">'#app'</span>)
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mounted</span>=<span class="hljs-string">"onMounted1($el)"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> @<span class="hljs-attr">mounted</span>=<span class="hljs-string">"onMounted2($el)"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">组件</h4>
<p>在 petite-vue 里，组件可以使用函数的方式创建，通过template可以实现复用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">$template</span>: <span class="hljs-string">'#counter-template'</span>,
      <span class="hljs-attr">count</span>: props.initialCount,
      <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.count++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.count++
      &#125;
    &#125;
  &#125;

  createApp(&#123;
    Counter
  &#125;).mount()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"counter-template"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-comment"><!-- 复用 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"Counter(&#123; initialCount: 1 &#125;)"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>=<span class="hljs-string">"Counter(&#123; initialCount: 2 &#125;)"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">全局状态管理</h4>
<p>借助 reactive 响应式 API 可以很轻松的创建全局状态管理</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>

    <span class="hljs-keyword">const</span> store = reactive(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
      <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.count++
      &#125;
    &#125;)
    <span class="hljs-comment">// 将count加1</span>
    store.increment()
    createApp(&#123;
      store
    &#125;).mount()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
    <span class="hljs-comment"><!-- 输出1 --></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; store.count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"store.increment"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">自定义指令</h4>
<p>这里来简单实现一个输入框自动聚焦的指令。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    
    <span class="hljs-keyword">const</span> autoFocus = <span class="hljs-function">(<span class="hljs-params">ctx</span>) =></span> &#123;
      ctx.el.focus()
    &#125;

    createApp().directive(<span class="hljs-string">'auto-focus'</span>, autoFocus).mount()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-auto-focus</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">内置指令</h4>
<ul>
<li>v-model</li>
<li>v-if / v-else / v-else-if</li>
<li>v-for</li>
<li>v-show</li>
<li>v-html</li>
<li>v-text</li>
<li>v-pre</li>
<li>v-once</li>
<li>v-cloak</li>
</ul>
<blockquote>
<p>注意：v-for 不需要key，另外 v-for 不支持 深度解构</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
    <span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'https://unpkg.com/petite-vue?module'</span>
    
    createApp(&#123;
      <span class="hljs-attr">userList</span>: [
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">age</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">23</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">24</span> &#125; &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'李四'</span>, <span class="hljs-attr">age</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">23</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">24</span> &#125; &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'王五'</span>, <span class="hljs-attr">age</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">23</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">24</span> &#125; &#125;
      ]
    &#125;).mount()
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-scope</span>></span>
    <span class="hljs-comment"><!-- 支持 --></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"&#123; age &#125; in userList"</span>></span>
      &#123;&#123; age.a &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-comment"><!-- 不支持 --></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"&#123; age: &#123; a &#125; &#125; in userList"</span>></span>
      &#123;&#123; a &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">不支持</h4>
<p>为了更轻量小巧，petite-vue 不支持以下特性：</p>
<ul>
<li>ref()、computed</li>
<li>render函数，因为petite-vue 没有虚拟DOM</li>
<li>不支持Map、Set等响应类型</li>
<li>Transition, KeepAlive, Teleport, Suspense</li>
<li>v-on="object"</li>
<li>v-is & </li>
<li>v-bind:style auto-prefixing</li>
</ul>
<h3 data-id="heading-12">总结</h3>
<p>以上就是对 petite-vue 的一些简单介绍和使用，抛砖引玉，更多新的探索就由你们去发现了。</p>
<p>总的来说，prtite-vue 保留了 Vue 的一些基础特性，这使得 Vue 开发者可以无成本使用，在以往，当我们在开发一些小而简单的页面想要引用 Vue 但又常常因为包体积带来的考虑而放弃，现在，petite-vue 的出现或许可以拯救这种情况了，毕竟它真的很小，大小只有 5.8kb，大约只是 Alpine.js 的一半。</p>
<h3 data-id="heading-13">写在最后</h3>
<p>码字不易，如果本文对你有什么帮助或收获，欢迎<strong>点赞</strong>，你的点赞是我创作的动力！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cbf986b527f42e19c93a75e6902c590~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            