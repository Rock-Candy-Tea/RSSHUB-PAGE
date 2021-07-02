
---
title: 'Vue：动画原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cn.vuejs.org/images/transition.png'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 05:56:19 GMT
thumbnail: 'https://cn.vuejs.org/images/transition.png'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>Vue 在插入、更新或者移除 DOM 时，提供多种不同方式的应用过渡效果。包括以下工具：</p>
<ul>
<li>在 CSS 过渡和动画中自动应用 class</li>
<li>可以配合使用第三方 CSS 动画库，如 Animate.css</li>
<li>在过渡钩子函数中使用 JavaScript 直接操作 DOM</li>
<li>可以配合使用第三方 JavaScript 动画库，如 Velocity.js</li>
</ul>
<p>在这里，我们只会讲到进入、离开和列表的过渡，你也可以看下一节的<a href="https://cn.vuejs.org/v2/guide/transitioning-state.html" target="_blank" rel="nofollow noopener noreferrer">管理过渡状态</a>。</p>
<h2 data-id="heading-1">单元素 / 组件的过渡</h2>
<p><code>transition</code>的封装组件</p>
<h3 data-id="heading-2">过渡的类名</h3>
<p><img src="https://cn.vuejs.org/images/transition.png" alt="Transition Diagram" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>v-enter</code></li>
<li><code>v-enter-active</code></li>
<li><code>v-enter-to</code></li>
<li><code>v-leave</code></li>
<li><code>v-leave-active</code></li>
<li><code>v-leave-to</code></li>
</ul>
<p>注意：如果<code><transition></code>没有名字，则<code>v-</code>是这些类名的默认前缀。如果像下面示例中，使用<code><transition name="fade"></code>，那么<code>v-enter</code>就会替换为<code>fade-enter</code></p>
<p><a href="https://jsbin.com/gacojod/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">类名示例</a></p>
<p>效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c7ac0e88814150ba65a15f14144971~tplv-k3u1fbpfcp-watermark.image" alt="76.1.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个示例中，<code>.fade-ernter</code>和<code>.fade-enter-active</code>先被添加，随后立即删除<code>.fade-enter</code>，并添加<code>.fade-enter-to</code>，enter进程结束后，一起删除<code>.fade-enter-active</code>和<code>.fade-enter-to</code>。</p>
<h3 data-id="heading-3">CSS过渡</h3>
<p>常用的过渡都是CSS过渡</p>
<p><a href="https://jsbin.com/himeged/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">CSS过渡示例</a></p>
<p>效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec83b01674484dc9be9877fa111699c1~tplv-k3u1fbpfcp-watermark.image" alt="76.1.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">CSS动画</h3>
<p>CSS动画和CSS过渡用法相同，区别是动画中<code>v-enter</code>类名在节点插入DOM后不会立即删除，而是在<code>animationed</code>事件触发时删除</p>
<p><a href="https://jsbin.com/yuyowah/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">CSS动画示例</a></p>
<p>效果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ac1a65ed8b44b34a51c36641c6e91cf~tplv-k3u1fbpfcp-watermark.image" alt="76.1.3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">自定义过渡的类名</h3>
<p>可以通过<code>attribute</code>来自定义过渡类名：</p>
<ul>
<li><code>enter-class</code></li>
<li><code>enter-active-class</code></li>
<li><code>enter-to-class</code></li>
<li><code>leave-class</code></li>
<li><code>leave-active-class</code></li>
<li><code>leave-to-class</code></li>
</ul>
<p>注意，自定义过渡类名，优先级高于普通类名</p>
<p>还可以使用第三方CSS动画库，如<a href="https://animate.style/" target="_blank" rel="nofollow noopener noreferrer">Animate.css</a></p>
<p><a href="https://jsbin.com/kajageg/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">使用Animate.css动画库</a></p>
<p>效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bc80ff508f145be874497a61fe21807~tplv-k3u1fbpfcp-watermark.image" alt="76.3.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">同时使用过渡和动画</h3>
<p>Vue 的事件监听器可以是<code>transitioned</code>或<code>animationed</code>，取决于给元素应用的CSS规则。</p>
<p>但在一些场景中，需要给同一个元素同时设置两种过渡动效。<code>transition</code>和<code>animation</code>结束时间不一样，需要使用<code>type</code> attribute 并设置 <code>animation</code>或<code>transition</code>来声明需要Vue监听的类型。</p>
<h3 data-id="heading-7">显性的过渡持续时间</h3>
<p>在很多情况下，Vue 可以自动得出过渡效果的完成时机。默认情况下，Vue 会等待其在过渡效果的根元素的第一个 <code>transitionend</code> 或 <code>animationend</code> 事件。然而也可以不这样设定——比如，我们可以拥有一个精心编排的一系列过渡效果，其中一些嵌套的内部元素相比于过渡效果的根元素有延迟的或更长的过渡效果。</p>
<p>在这种情况下你可以用 <code><transition></code> 组件上的 <code>duration</code> prop 定制一个显性的过渡持续时间 (以毫秒计)：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:duration</span>=<span class="hljs-string">"1000"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以定制进入和移出的持续时间：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:duration</span>=<span class="hljs-string">"&#123; enter: 500, leave: 800 &#125;"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">JavaScript 钩子</h3>
<p>可在 attribute 中声明 JavaScript 钩子</p>
<h4 data-id="heading-9">钩子函数 结合 CSS</h4>
<p>这些钩子函数可以结合 CSS <code>transitions</code> / <code>animations</code> 使用，也可以单独使用。</p>
<p><a href="https://jsbin.com/zikakiw/edit?html,js,console,output" target="_blank" rel="nofollow noopener noreferrer">JavaScript 函数 结合 transitions 使用示例</a></p>
<p>效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7aa8f04ca814be981c0b1618bcfa24f~tplv-k3u1fbpfcp-watermark.image" alt="76.3.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">JavaScript 过渡</h4>
<p>注意</p>
<ul>
<li>当只用 JavaScript 过渡的时候， 在<code>enter</code>和<code>leave</code>中必须使用<code>done</code>进行回调。否则，它们将被同步调用，过渡会立即完成。</li>
<li>推荐对于仅使用 JavaScript 过渡的元素添加 <code>v-bind:css="false"</code>，Vue会跳过CSS的检测。这也可以避免过渡过程中CSS的影响。</li>
</ul>
<p>Velocity 和 jQuery.animate 的工作方式类似，也可以用来实现 JavaScript 动画</p>
<p><a href="https://jsbin.com/faqejiz/edit?html,js,output" target="_blank" rel="nofollow noopener noreferrer">一个使用 Velocity.js 的简单例子</a></p>
<p>效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ef3769242c4a83bd0d97e014e7b2d8~tplv-k3u1fbpfcp-watermark.image" alt="76.3.3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">多个元素的过渡</h2>
<h3 data-id="heading-12">key</h3>
<p>先看一个<a href="https://jsbin.com/josukuw/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">示例-使用key</a></p>
<p>效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11008e5e01e049d3ba989210ae0e050e~tplv-k3u1fbpfcp-watermark.image" alt="76.4.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>对于多个元素的过渡，可以使用<code>v-if</code> / <code>v-else</code>。</strong></p>
<p>但当有相同标签名的元素切换时，需要通过<code>key</code>设置唯一的值来标记以让Vue区分，否则Vue为了效率只会替换相同标签内部的内容。</p>
<p>上面的示例就正确使用了<code>key</code>，如果不加<code>key</code>的话，就会默认替换标签内部的<code>on</code>为<code>off</code>，效果如下。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eae0d20d68a342178e4ae8fba0e5c3b5~tplv-k3u1fbpfcp-watermark.image" alt="76.4.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>使用多个<code>v-if</code>的多个元素的过渡可以重写为绑定了动态 property 的单个元素过渡。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"docState === 'saved'"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"saved"</span>></span>
    Edit
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"docState === 'edited'"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"edited"</span>></span>
    Save
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"docState === 'editing'"</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"editing"</span>></span>
    Cancel
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以重写为</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-bind:key</span>=<span class="hljs-string">"docState"</span>></span>
    &#123;&#123; buttonMessage &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-attr">computed</span>: &#123;
  <span class="hljs-attr">buttonMessage</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.docState) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'saved'</span>: <span class="hljs-keyword">return</span> <span class="hljs-string">'Edit'</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'edited'</span>: <span class="hljs-keyword">return</span> <span class="hljs-string">'Save'</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'editing'</span>: <span class="hljs-keyword">return</span> <span class="hljs-string">'Cancel'</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">过渡模式</h3>
<p>还有一个问题，上面使用了<code>key</code>的示例，在<code>on</code>按钮和<code>off</code>按钮的过渡中，两个按钮都被重绘了，一个离开过渡的时候，另一个开始进入过渡。这是<code><transition></code>的默认行为——进入和离开同时发生。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61115cafca9143a9a06896db261132f7~tplv-k3u1fbpfcp-watermark.image" alt="76.4.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此提供了过渡模式：</p>
<ul>
<li><code>in-out</code>：新元素过渡 => 当前元素过渡离开</li>
<li><code>out-in</code>：当前元素过渡 => 新元素过渡进入</li>
</ul>
<p>现在用<code>out-in</code>重写之前的开关按钮过渡：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"fade"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span>></span>
  <span class="hljs-comment"><!-- ... the buttons ... --></span>
<span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72e2f2dcbaaf4b8b95c3689e1ad61ad2~tplv-k3u1fbpfcp-watermark.image" alt="76.4.3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://jsbin.com/poniboj/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">用<code>in-out</code>实现轮播效果</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be23e6ad57614b2cbb6a05d87ded9728~tplv-k3u1fbpfcp-watermark.image" alt="76.4.4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">多个组件的过渡</h2>
<p>多个组件的过渡更简单，不需要<code>key</code>，相反，只需要使用<a href="https://cn.vuejs.org/v2/guide/components.html#%E5%8A%A8%E6%80%81%E7%BB%84%E4%BB%B6" target="_blank" rel="nofollow noopener noreferrer">动态组件</a></p>
<p><a href="https://jsbin.com/kulocor/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">示例-组件过渡</a></p>
<p>效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/365d6edae666457aa9b85a2ffe3253f5~tplv-k3u1fbpfcp-watermark.image" alt="76.4.5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">列表过渡</h2>
<p>使用<code><transition-group></code>组件，同时渲染整个列表。</p>
<p>组件特点：</p>
<ul>
<li>不同于<code><transition></code>，它会以一个真实元素呈现：默认为一个<code><span></code>。也可以通过<code>tag</code>更换为其他元素。</li>
<li><strong>过渡模式</strong>不可用，因为不再相互切换特有的元素。</li>
<li>内部元素总是需要提供唯一的<code>key</code>值。</li>
<li>CSS过渡的类将会应用在内部的元素中，而不是这个组 / 容器本身。</li>
</ul>
<h3 data-id="heading-16">列表的进入 / 离开过渡</h3>
<p><a href="https://jsbin.com/weyaxex/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">示例</a></p>
<p>效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad92503cb9164f29835665629fb2977a~tplv-k3u1fbpfcp-watermark.image" alt="76.5.1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个例子中，当添加和移除元素的时候，周围的元素会瞬间移动到他们的新布局的位置，而不是平滑的过渡，下面来解决这个问题。</p>
<h3 data-id="heading-17">列表的排序过渡</h3>
<p><a href="https://jsbin.com/yasagim/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">示例</a></p>
<p>效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48bf755010554bb4b6f4d435715e38fe~tplv-k3u1fbpfcp-watermark.image" alt="76.5.2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><transition-group></code>组件不仅可以进入和离开动画，还可以改变定位。</p>
<p>Vue使用了一个叫<a href="https://aerotwist.com/blog/flip-your-animations/" target="_blank" rel="nofollow noopener noreferrer">FLIP</a>简单的动画队列，使用<code>transforms</code>将元素从之前的位置平滑过渡到新的位置。</p>
<p>现在将这个技术和之前的示例结合，使列表的一切变动都有动画过渡。</p>
<p><a href="https://jsbin.com/mefaman/1/edit?html,css,js,output" target="_blank" rel="nofollow noopener noreferrer">示例</a></p>
<p>效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a09df7b83de3453e9180bc7e37827ba8~tplv-k3u1fbpfcp-watermark.image" alt="76.5.3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意！使用FLIP过渡的元素不能设置为<code>display: inline</code>，作为替代方案，可以设置为<code>display: inline-block</code>，或放置于flex中。</p></div>  
</div>
            