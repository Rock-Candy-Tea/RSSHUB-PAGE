
---
title: 'Vue： 构造选项学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a6401cc2754d399807ad5ac91d7973~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 09:30:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a6401cc2754d399807ad5ac91d7973~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Vue的选项式API包含以下部分：Data、DOM、生命周期钩子，资源、组合、杂项。本篇主要用来记录学习的，主要涉及这些API的类型、限制条件，并且举一些例子来更好理解。</p>
</blockquote>
<p>先甩一个<a href="https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE" target="_blank" rel="nofollow noopener noreferrer">文档</a></p>
<h2 data-id="heading-0">数据</h2>
<h3 data-id="heading-1">data-内部数据</h3>
<ul>
<li>
<p>类型：<code>Object | Function</code></p>
</li>
<li>
<p>限制：<strong>组件的定义只接受<code>function</code></strong></p>
<p>因为组件引入调用data，如果data为对象，那么连续两次引入，第二次就会覆盖掉第一次。当data为Function时，组件调用函数，函数会生成一个全新的对象，所以两次引入会得到两个全新的对象，互不干扰。</p>
<p>注意，是<strong>调用data</strong></p>
</li>
<li>
<p>详细：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.js完整版为例</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.Vue)

<span class="hljs-keyword">const</span> Vue = <span class="hljs-built_in">window</span>.Vue

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-comment">// data是对象</span>
  <span class="hljs-attr">data</span>:&#123;
    <span class="hljs-attr">n</span>:<span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-comment">// 函数可缩写为 data()&#123;&#125;</span>
  <span class="hljs-comment">// 或函数</span>
  <span class="hljs-attr">data</span>:<span class="hljs-function"><span class="hljs-keyword">function</span></span>&#123;
    <span class="hljs-keyword">return</span>&#123;
      <span class="hljs-attr">n</span>:<span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-attr">template</span>:<span class="hljs-string">`
    <div>
    &#123;&#123; n &#125;&#125;
    <button @click="add">+1</button>
    </div>
  `</span>,
  <span class="hljs-attr">methods</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-built_in">this</span>.n += <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">props-外部数据</h3>
<ul>
<li>
<p>类型：<code>Array<string> | Object</code></p>
</li>
<li>
<p>详情：props 可以是数组或对象，用于接收来自父组件的数据。props 可以是简单的数组，或者使用对象作为替代，对象允许配置高级选项，如类型检测、自定义验证和设置默认值</p>
</li>
<li>
<p>例子：</p>
<p>传字符串</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a6401cc2754d399807ad5ac91d7973~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608013454399.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当使用<code>:</code>时，引号内是<code>JS</code>，比如下面，就可以将<code>n:0</code>传入<code>demo.vue</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2108e6cfb7ec4d47bb206b54e8d81091~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608014056045.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果需要再<code>JS</code>里传字符串，则需要再加引号</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23501cd95af544a0b8a13547ecf6e511~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608014235103.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>让儿子<code>call</code>父亲里的函数<code>add</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92deef18c61a49febe44c395bb406268~tplv-k3u1fbpfcp-watermark.image" alt="69.5.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更高级一点的，儿子<code>call</code>父亲的<code>add</code>，父亲的n发生变化，再将<code>n</code>传给儿子</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bad0d9c8f604d49971726b06b4a8d10~tplv-k3u1fbpfcp-watermark.image" alt="69.5.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">propsData</h3>
<h3 data-id="heading-4">computed</h3>
<h3 data-id="heading-5">methods-方法</h3>
<ul>
<li>
<p>类型：<code>&#123;[key: string]: Function&#125;</code></p>
</li>
<li>
<p>详细：事件处理函数或者是普通函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 事件处理函数</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span>&#123;
      <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>   
    &#125;
  &#125;,
  <span class="hljs-attr">template</span>:<span class="hljs-string">`
    <div>
    &#123;&#123; n &#125;&#125;
    <button @click="add">+1</button>
    </div>
  `</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 方法中的this自动绑定为Vue实例</span>
      <span class="hljs-built_in">this</span>.n += <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 普通函数，可以代替filter</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span>&#123;
      <span class="hljs-attr">n</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">array</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]
    &#125;
  &#125;,
  <span class="hljs-attr">template</span>:<span class="hljs-string">`
    <div>
    &#123;&#123; n &#125;&#125;
    <button @click="add">+1</button>
    <hr>
    &#123;&#123;filter()&#125;&#125;
    </div>
  `</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 方法中的this自动绑定为Vue实例</span>
      <span class="hljs-built_in">this</span>.n += <span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">filter</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.array.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>)
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：不应该使用箭头函数来定义method函数，因为箭头函数绑定了父级作用域的上下文，所以this将不会按照期望指向Vue实例，<code>this.n</code>将是undefined。</p>
</li>
</ul>
<h3 data-id="heading-6">watch</h3>
<h2 data-id="heading-7">DOM</h2>
<h3 data-id="heading-8">el-挂载点</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d6bc3d4d0fb401eac82b1aa69f034f0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607205608637.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>类型：<code>string | Element</code></p>
</li>
<li>
<p>限制：只在用<code>new</code>创建实例时生效</p>
</li>
<li>
<p>详细：与<code>$mount</code>有替换关系。</p>
<p>提供一个在页面上已存在的 DOM 元素作为 Vue 实例的挂载目标。可以是 CSS 选择器，也可以是一个 HTMLElement 实例。</p>
<p>在实例挂载之后，元素可以用 <code>vm.$el</code> 访问。</p>
<p>如果在实例化时存在这个选项，实例将立即进入编译过程，否则，需要显式调用 <code>vm.$mount()</code> 手动开启编译。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b9bbf59195470da346749a8406d6a2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607210105125.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">template</h3>
<h3 data-id="heading-10">render</h3>
<h3 data-id="heading-11">renderError</h3>
<h2 data-id="heading-12">生命周期钩子</h2>
<p>生命周期图示</p>
<p><img src="https://cn.vuejs.org/images/lifecycle.png" alt="Vue 实例生命周期" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">beforeCreate</h3>
<h3 data-id="heading-14">created-实例出现在内存中</h3>
<ul>
<li>
<p>类型：<code>Function</code></p>
</li>
<li>
<p>例子</p>
<p>代码如下</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9d7bfb060e64022b14030bf72b1676c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608005514707.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>debugger<code>created</code>，可以知道<code>created()&#123;&#125;</code>运行时，实例出现在内存中，不出现在页面中</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04144b959fed44b283fedc0fb3d6fb64~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608010046136.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>debugger<code>mounted</code>，可以知道<code>mounted()&#123;&#125;</code>运行时，实例出现在页面中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b976f5d46c9f4dd3af7c7b6b05dd52d6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210608010115827.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实例每次更新，<code>updated()&#123;&#125;</code>运行</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4784988a08804702a6c279237b6b0b72~tplv-k3u1fbpfcp-watermark.image" alt="69.4.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而每次点击<code>toggle</code>，使实例消失时，<code>destory()&#123;&#125;</code>就会运行，并且再次调出实例时，n还原为0，表示<strong>实例从页面和内存中消失</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70097523939345f3b9c96c62c4280432~tplv-k3u1fbpfcp-watermark.image" alt="69.4.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">beforeMount</h3>
<h3 data-id="heading-16">mounted-实例出现在页面中</h3>
<ul>
<li>
<p>类型：<code>Function</code></p>
</li>
<li>
<p>例子：参见created中的例子</p>
</li>
</ul>
<h3 data-id="heading-17">beforeUpdate</h3>
<h3 data-id="heading-18">updated-实例更新了</h3>
<ul>
<li>
<p>类型：<code>Function</code></p>
</li>
<li>
<p>例子：参见created中的例子</p>
</li>
</ul>
<h3 data-id="heading-19">activated</h3>
<h3 data-id="heading-20">deactivated</h3>
<h3 data-id="heading-21">beforeDestroy</h3>
<h3 data-id="heading-22">destroyed-实例从页面和内存中消亡了</h3>
<ul>
<li>
<p>类型：<code>Function</code></p>
</li>
<li>
<p>例子：参见created中的例子</p>
</li>
</ul>
<h3 data-id="heading-23">errorCaptured</h3>
<h2 data-id="heading-24">资源</h2>
<h3 data-id="heading-25">directives</h3>
<h3 data-id="heading-26">filters</h3>
<h3 data-id="heading-27">components-组件</h3>
<ul>
<li>
<p>类型：<code>Object</code></p>
</li>
<li>
<p>三种引入方式</p>
<p>考虑模块化，优先使用第一种方法</p>
<p>方法一：</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e96da4ee9bc47aa80d2844982139bb6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607232146182.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a973b7f86f41469f043ec2bf5267c3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607231957845.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>方法二：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a4b5c8918c4d959639cf26ff527119~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607234858239.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb7afbb996e4de7b0ab65a06e37bbe4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607234758730.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>方法三：</p>
<p>结合前两种方法</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2a13ff6aa5842c8947a3ca967848015~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607235641662.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb338bfa19e48aab636cdd50f852ea6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210607235627510.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>命名规则：组件名推荐大写开头，与原生标签区分。文件名推荐小写，因为有的系统识别不了大小写，比如win10。</li>
</ul>
<h2 data-id="heading-28">组合</h2>
<h3 data-id="heading-29">parent</h3>
<h3 data-id="heading-30">mixins</h3>
<h3 data-id="heading-31">extends</h3>
<h3 data-id="heading-32">provide</h3>
<h3 data-id="heading-33">inject</h3></div>  
</div>
            