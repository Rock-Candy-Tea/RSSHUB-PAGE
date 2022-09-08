
---
title: 'React18 - 在React中编写CSS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2173'
author: 掘金
comments: false
date: Tue, 06 Sep 2022 17:06:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=2173'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第5篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<p>目前，前端最流行的开发方式是组件化，而CSS的设计本身就不是为组件化而生的，所以在目前组件化的框架中都在需要一种合适的CSS解决方案</p>
<p>在组件化开发环境下的CSS，应该满足如下需求:</p>
<ol>
<li>可以编写局部css:  css具备自己的具备作用域，不会随意污染其他组件内的元素</li>
<li>可以编写动态的css:  可以获取当前组件的一些状态，根据状态的变化生成不同的css样式</li>
<li>支持所有的css特性:伪类、动画、媒体查询等</li>
<li>编写起来简洁方便、最好符合一贯的css风格特点</li>
<li>等等 。。。。</li>
</ol>
<p>Vue在CSS上虽然不能称之为完美，但是已经足够简洁、自然、方便了，至少统一的样式风格不会出现多个开发人员、多个项目 采用不一样的样式风格</p>
<p>相比而言，React官方并没有给出在React中统一的样式风格</p>
<p>由此，从普通的css，到css modules，再到css in js，有几十种不同的解决方案，上百个不同的库</p>
<p>大家一致在寻找最好的或者说最适合自己的CSS方案，但是到目前为止也没有统一的方案</p>
<h2 data-id="heading-0">内联样式</h2>
<p>内联样式是官方推荐的一种css样式的写法:</p>
<ol>
<li>style 接受一个采用小驼峰命名属性的 JavaScript 对象，而不支持 CSS 字符串形式写法</li>
<li>并且可以引用state中的状态来设置相关的样式</li>
</ol>
<p><code>优点</code></p>
<ol>
<li>内联样式, 样式之间不会有冲突</li>
<li>可以动态获取当前state中的状态</li>
</ol>
<p><code>缺点</code></p>
<ol>
<li>
<p>写法上都需要使用驼峰标识</p>
</li>
<li>
<p>某些样式没有提示</p>
</li>
<li>
<p>大量的样式, 代码混乱</p>
</li>
<li>
<p>某些样式无法编写(比如伪类/伪元素)</p>
</li>
</ol>
<p>所以官方依然是希望内联合适和普通的css来结合编写</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
    <span class="hljs-variable language_">super</span>(props)

    <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
      <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>
    &#125;
  &#125;


  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">colot:</span> <span class="hljs-attr">this.state.color</span>, <span class="hljs-attr">backgroundColor:</span> '<span class="hljs-attr">skyblue</span>' &#125;&#125;></span>App<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">普通的CSS</h2>
<p>普通的css我们通常会编写到一个单独的文件，之后再进行引入</p>
<p>这样的编写方式和普通的网页开发中编写方式是一致的</p>
<p>但是使用这种方式编写我们的css有一个致命缺点，即没有自己的样式作用域</p>
<p>默认引入的样式都是全局样式</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./style.css'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
    <span class="hljs-variable language_">super</span>(props)

    <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
      <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>
    &#125;
  &#125;


  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>App<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">css modules</h2>
<p>css modules并不是React特有的解决方案，而是所有使用了类似于webpack配置的环境下都可以使用的</p>
<p>如果在其他项目中使用它，那么我们需要自己来进行配置，比如配置webpack.config.js中的modules: true等</p>
<p>如果使用React脚手架，其内部已经内置了css modules的配置</p>
<p>.css/.less/.scss 等样式文件都需要修改成 .module.css/.module.less/.module.scss 等 之后就可以引用并且进行使用了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 引入css modules - 实际会将对应的css文件编译为一个JS对象</span>
<span class="hljs-comment">// 当我们将一个样式文件的后缀名修改为 .module.css的时候，对应样式文件就变成了css样式模块</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">AppStyle</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./style.module.css'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
    <span class="hljs-variable language_">super</span>(props)

    <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
      <span class="hljs-attr">color</span>: <span class="hljs-string">'red'</span>
    &#125;
  &#125;


  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
&#123;/*
css modules 会将css文件编译为js对象，所以需要向属性那样使用
同理 如果使用了一个样式模块中不存在的样式，对应值就是undefined
实际表现为对应元素样式不生效, 页面并不会报错
*/&#125;
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;AppStyle.title&#125;</span>></span>title<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
&#123;/*
对应的样式会被编译w为 style_content__O3F7P
也就是 [样式文件名]_[样式名]__[hash值]
从而避免出现样式冲突
*/&#125;
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;AppStyle.content&#125;</span>></span>content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是CSS modules依旧存在自己的缺点</p>
<ol>
<li>引用的类名，不能直接使用连接符(.home-title)，需要使用中括号语法，因为连字符在JavaScript中是不识别的</li>
<li>所有的className都必须使用&#123;style.className&#125; 的形式来编写</li>
<li>不方便动态来修改某些样式，依然需要使用内联样式的方式</li>
</ol>
<h2 data-id="heading-3">css in js</h2>
<p>“CSS-in-JS” 是指一种模式，其中 CSS 由 JavaScript 生成而不是在外部文件中定义</p>
<p>注意此功能并不是 React 的一部分，而是由第三方库提供</p>
<p>React的思想中认为逻辑本身和UI是无法分离的，所以才会有了JSX的语法</p>
<p>事实上CSS-in-JS的模式就是一种将样式(CSS)也写入到JavaScript中的方式，并且可以方便的使用JavaScript的状态</p>
<p>所以React有被人称之为 All in JS</p>
<p>CSS-in-JS通过JavaScript来为CSS赋予一些能力，包括类似于CSS预处理器一样的样式嵌套、函数定义、逻辑复用、动态修 改状态等等</p>
<p>所以，目前可以说CSS-in-JS是React编写CSS最为受欢迎的一种解决方案</p>
<p>目前最为常用的css-in-js库是 <code>styled-components</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install styled-components
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>组件</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 使用css in js后，对应的样式直接编写在js文件中即可</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">AppWrapper</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./style.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AppWrapper</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"title"</span>></span>title<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"content"</span>></span>content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">AppWrapper</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>样式</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-comment">// styled.div本质上是一个函数  需要通过标签模板字符串进行调用 并返回一个新的有对应样式的组件</span>
<span class="hljs-comment">// ps: 默认情况下对应样式是不会高亮的，需要高亮可以安装vscode-styled-components插件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
/* 对应样式会被编译为 .jaGVDq */
/* 即一个唯一的hash值 */
/* 所以使用styled-components编写对应的样式会存在自己的样式作用域 */
/* 组件和组件之间的样式是不会冲突的 */
/* 
但因为编译后的样式类似于 .jaGVDq .content
所以在实际使用过程中，对于后代选择器仍然可能出现样式冲突的情况
  */
background-color: #f5f5f5;

/* .jaGVDq .title */
.title &#123;
color: red;

&:hover &#123;
background-color: gray;
&#125;
&#125;

/* .jaGVDq .content */
.content &#123;
color: skyblue
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">样式组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
background-color: #f5f5f5;

.content &#123;
color: skyblue
&#125;
`</span>

<span class="hljs-comment">// 如果某一块的样式比较多，可以将对应的样式进行单独抽离</span>
<span class="hljs-comment">// 形成一个独立的样式组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">TitleWrapper</span> = styled.<span class="hljs-property">h2</span><span class="hljs-string">`
color: red;

&:hover &#123;
background-color: gray;
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">引入外部变量</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">AppWrapper</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./style.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
<span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
<span class="hljs-variable language_">super</span>(props)

<span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
<span class="hljs-attr">color</span>: <span class="hljs-string">'skyblue'</span>
&#125;
&#125;


  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
<span class="hljs-comment">// AppWrapper本质上是一个组件</span>
<span class="hljs-comment">// 所以对应的样式直接以props的形式进行传入即可</span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AppWrapper</span> <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">this.state.color</span> &#125;></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"title"</span>></span>title<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"content"</span>></span>content<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">AppWrapper</span>></span></span>
    )
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
.title &#123;
/*
如果直接使用props.color 在js中 会沿着作用域链去查找对应的props
所以直接使用props 在css in js中是不合适的
所以在styled-components中引入外部变量的时候，需要传入一个回调函数
该回调函数的参数为外部传入的props，返回值是所需要设置的对应样式值
*/
color: <span class="hljs-subst">$&#123; props => props.color &#125;</span>;

&:hover &#123;
background-color: gray;
&#125;
&#125;

.content &#123;
color: gray
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">默认值</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-comment">// 因为styled-components 本质上就是css in js</span>
<span class="hljs-comment">// 所以我们也可以通过如下方式来使用styled-components</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
.title &#123;
// 解构语法
color: <span class="hljs-subst">$&#123; (&#123; color &#125;) => color &#125;</span>;

&:hover &#123;
  // 解构的时候 设置对应的默认值
background-color: <span class="hljs-subst">$&#123; (&#123; bgColor = <span class="hljs-string">'yellow'</span> &#125;) => bgColor &#125;</span>;
&#125;
&#125;

.content &#123;
 // 空值合并操作符
color: <span class="hljs-subst">$&#123; (&#123; contentColor &#125;) => contentColor ?? <span class="hljs-string">'orange'</span> &#125;</span>
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有的时候，我们希望在外部没有传入对应props的时候，可以存在对应的默认值</p>
<p>但是使用上述写法，每使用一次就需要单独设置一次对应的默认值，这必然是十分麻烦的</p>
<p>所以styled-components提供了attrs方法，专门用于设置默认值</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-comment">// attrs方法会返回对应的含有样式的样式组件</span>
<span class="hljs-comment">// 所以在这里可以链式调用</span>
<span class="hljs-comment">// 在attrs中可以传入一个回调函数，用于设置对应的默认值</span>
<span class="hljs-comment">// 回调函数在被调用的时候会将对应的props传递过来</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span>.<span class="hljs-title function_">attrs</span>(<span class="hljs-function"><span class="hljs-params">props</span> =></span> (&#123;
<span class="hljs-attr">contentColor</span>: props.<span class="hljs-property">contentColor</span> ?? <span class="hljs-string">'purple'</span>
&#125;))<span class="hljs-string">`
.title &#123;
color: <span class="hljs-subst">$&#123; props => props.color &#125;</span>;

&:hover &#123;
background-color: gray;
&#125;
&#125;

.content &#123;
color: <span class="hljs-subst">$&#123; props => props.contentColor &#125;</span>
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">引入全局样式</h3>
<p><code>/style/theme.js --- 全局的主题样式文件</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> primaryColor = <span class="hljs-string">'#409eff'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> warnColor = <span class="hljs-string">'#e6a23c'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> successColor = <span class="hljs-string">'#67c23a'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>样式组件</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>
<span class="hljs-keyword">import</span> &#123;
primaryColor,
successColor
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../style/theme'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
.title &#123;
color: <span class="hljs-subst">$&#123; successColor &#125;</span>;

&:hover &#123;
background-color: gray;
&#125;
&#125;

.content &#123;
color: <span class="hljs-subst">$&#123; primaryColor &#125;</span>
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">provider</h3>
<p><code>app.jsx</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/client'</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">StrictMode</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">ThemeProvider</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>;

<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">createRoot</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelector</span>(<span class="hljs-string">'#root'</span>)).<span class="hljs-title function_">render</span>(
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">StrictMode</span>></span>
&#123;/*
ThemeProvider 是 styled-components中 导出的 context
通过theme属性来设置对应的全局变量值
*/&#125;
<span class="hljs-tag"><<span class="hljs-name">ThemeProvider</span> <span class="hljs-attr">theme</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">skyblue</span>' &#125;&#125;></span>
<span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">ThemeProvider</span>></span>
<span class="hljs-tag"></<span class="hljs-name">StrictMode</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> styled <span class="hljs-keyword">from</span> <span class="hljs-string">'styled-components'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> styled.<span class="hljs-property">div</span><span class="hljs-string">`
.title &#123;
/* ThemeContext中提供的全局样式值会被传入到 props.theme中 */
color: <span class="hljs-subst">$&#123; props => props.theme.color &#125;</span>;
&#125;

.content &#123;
color: red
&#125;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">样式继承</h3>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> <span class="hljs-title class_">OriginButton</span> = styled.<span class="hljs-property">button</span><span class="hljs-string">`
border-radius: 5px;
`</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title class_">PrimaryButton</span> = <span class="hljs-title function_">styled</span>(<span class="hljs-title class_">OriginButton</span>)<span class="hljs-string">`
color: #fff;
background-color: #409eff;
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">动态添加class</h2>
<p><code>写法一 --- 使用三元运算符</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
<span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
<span class="hljs-variable language_">super</span>(props)

<span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
<span class="hljs-attr">isActive</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">isCurrent</span>: <span class="hljs-literal">true</span>
&#125;
&#125;

<span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
<span class="hljs-keyword">const</span> &#123; isActive, isCurrent &#125; = <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span>

<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span> `$&#123;<span class="hljs-attr">isActive</span> ? '<span class="hljs-attr">active</span>' <span class="hljs-attr">:</span> '' &#125; $&#123; <span class="hljs-attr">isCurrent</span> ? '<span class="hljs-attr">current</span>' <span class="hljs-attr">:</span> '' &#125;` &#125;></span>active<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)
&#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>写法二 --- 使用join方法</code></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">PureComponent</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">PureComponent</span> &#123;
<span class="hljs-title function_">constructor</span>(<span class="hljs-params">props</span>) &#123;
<span class="hljs-variable language_">super</span>(props)

<span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
<span class="hljs-attr">isActive</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">isCurrent</span>: <span class="hljs-literal">true</span>
&#125;
&#125;

<span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
<span class="hljs-keyword">const</span> &#123; isActive, isCurrent &#125; = <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span>

<span class="hljs-keyword">const</span> activeClass = []

<span class="hljs-keyword">if</span> (isActive) &#123;
activeClass.<span class="hljs-title function_">push</span>(<span class="hljs-string">'active'</span>)
&#125;

<span class="hljs-keyword">if</span> (isCurrent) &#123;
activeClass.<span class="hljs-title function_">push</span>(<span class="hljs-string">'current'</span>)
&#125;

<span class="hljs-keyword">return</span> (
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">activeClass.join</span>(' ') &#125;></span>active<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)
&#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>写法三 --- 使用第三方库 classnames</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install classnames
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-title function_">classNames</span>(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>); <span class="hljs-comment">// => 'foo bar'</span>
<span class="hljs-title function_">classNames</span>(<span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>
<span class="hljs-title function_">classNames</span>(&#123; <span class="hljs-string">'foo-bar'</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo-bar'</span>
<span class="hljs-title function_">classNames</span>(&#123; <span class="hljs-string">'foo-bar'</span>: <span class="hljs-literal">false</span> &#125;); <span class="hljs-comment">// => ''</span>
<span class="hljs-title function_">classNames</span>(&#123; <span class="hljs-attr">foo</span>: <span class="hljs-literal">true</span> &#125;, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>
<span class="hljs-title function_">classNames</span>(&#123; <span class="hljs-attr">foo</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar'</span>

<span class="hljs-comment">// classnames 支持多种编写方式 混合使用</span>
<span class="hljs-title function_">classNames</span>(<span class="hljs-string">'foo'</span>, &#123; <span class="hljs-attr">bar</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">duck</span>: <span class="hljs-literal">false</span> &#125;, <span class="hljs-string">'baz'</span>, &#123; <span class="hljs-attr">quux</span>: <span class="hljs-literal">true</span> &#125;); <span class="hljs-comment">// => 'foo bar baz quux'</span>

<span class="hljs-comment">// 只要是falsy值的结果 全部都会被忽略</span>
<span class="hljs-title function_">classNames</span>(<span class="hljs-literal">null</span>, <span class="hljs-literal">false</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-literal">undefined</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, &#123; <span class="hljs-attr">baz</span>: <span class="hljs-literal">null</span> &#125;, <span class="hljs-string">''</span>); <span class="hljs-comment">// => 'bar 1'</span>

<span class="hljs-comment">// classnames 支持 数组写法 和 计算属性名</span>
className=&#123; <span class="hljs-title function_">classnames</span>([&#123; [activeClass]: isActive &#125;, &#123; <span class="hljs-attr">current</span>: isCurrent &#125;])
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            