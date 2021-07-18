
---
title: '4x0 精读Vue官方文档 -  单文件组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9642'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 17:31:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=9642'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<h2 data-id="heading-1">使用方式对比</h2>
<p>使用 <code>Vue.js</code> 有两种方式 ：</p>
<ol>
<li><strong>纯JavaScrit驱动</strong>：模板的编译、Vdom 的创建、视图渲染都在浏览器端完成。</li>
<li>使用 Vue 官方提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/" ref="nofollow noopener noreferrer"><strong>标准化工具</strong></a>：通过构建工具的支持，可以使用扩展名为 <code>.vue</code> 的单文件组件的形式来使用 Vue。</li>
</ol>
<blockquote>
<p>采用 Vue 标准化工具，开发者只需要在单文件组件 (SFC) 中进行功能编码，其它额外的工作都将交由构建工具进行编译输出。构建工具自带了诸如 <code>babel</code>、<code>Typescript</code>、<code>SCSS</code>、<code>PostCSS</code> 等预处理器，集成了专为 Vue 开发环境服务的插件，例如 <code>eslint-plugin-vue</code>、<code>eslint-plugin-prettier</code>、<code>@vue/cli-plugin-*</code> 等，并搭配 <code>vue-loader</code> 来对单文件组件进行编译输出处理。</p>
</blockquote>
<p>下面是两种方式的对比：</p>





























<table><thead><tr><th>标准开发工具</th><th>纯JavaScript驱动</th></tr></thead><tbody><tr><td>组件可以模块化引入</td><td>不支持模块化，组件需要全局定义，并且组件名称不得重复</td></tr><tr><td>HTML 风格模板、支持语法高亮</td><td>HTML 字符串形式的模板、换行困难且不支持语法高亮</td></tr><tr><td>支持 CSS Module，可以使用多种 CSS 预处理器编写 CSS</td><td>不支持 CSS Module，不支持 CSS 预处理器</td></tr><tr><td>组件化更完整，会将 HTML、CSS、JavaScript 内聚在一个单文件组件中</td><td>只有 HTML、JavaScript 会被组件化，CSS 被遗漏</td></tr><tr><td>支持构建工具、编译阶段由构建工具完成，并且支持对代码优化，性能大大提高</td><td>不支持构建工具，浏览器端完成模板编译</td></tr></tbody></table>
<blockquote>
<p>在 <code>Vue1.x</code> 版本早期，<code>Vue-cli</code> 还未面世，人们会依赖构建工具例如 <code>webpack</code> 的模块化系统实现局部组件模块的导入导出与注册。它可以被视为 纯 JavaScript 驱动到现代 Vue 标准化工具开发的过渡阶段。</p>
</blockquote>
<h2 data-id="heading-2">单文件组件</h2>
<p><strong>SFC</strong>（Single-File Components) 单文件组件。
一个模块对应一个组件，每个模块同时包含了 <code>template</code>、<code>style</code>、<code>script </code> 三个部分，通过将这些不同的内容内聚在一个模块中，从而让组件更集中、更易于开发与管理。</p>
<ul>
<li><code>template</code> : 组件的模板部分、语法全面拥抱 HTML WebComponent 规范，上手简单易于使用。</li>
<li><code>script</code> : 组件的逻辑部分，采用 <code>optionsAPI</code> 方式编写，直观易懂。</li>
<li><code>style</code> : 组件的样式部分，支持 CSS Module。</li>
</ul>
<p>Vue 的单文件组件也可以使用较为松散形式的内聚：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- my-component.vue --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>This will be pre-compiled<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./my-component.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./my-component.css"</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，你也可以基于构建工具的模块化系统，将逻辑与样式作为独立的模块 <code>import/require</code> 进来。</p>
<blockquote>
<p>由此我们可以看出 Vue 的单文件组件非常类似于 HTML 文件性质，例如组件的样式与逻辑既可以内联也可以外链。</p>
</blockquote>
<h2 data-id="heading-3">关注点分离</h2>
<p>首先，<strong>关注点分离并不等于文件类型分离</strong>。相比于把代码库分离成三个大的层次并将其相互交织起来实现产品或功能，而是把它们划分为松散耦合的组件再将其组合起来更为合理一些。在一个组件里，其模板、逻辑和样式是内部耦合的，并且把他们搭配在一起实际上使得组件更加内聚且更可维护。</p>
<blockquote>
<p>其实二者在我看来并不冲突，因为对于传统应用来说，其代码库是基于语言类型层面来进行的划分，而对于现代应用的开发，特别是以 Vue 的视角来看，一个应用或功能都是由一个一个组件进行堆砌而成，然后在组件内部进行关注点的分离。因此二者的差异在于看待应用开发模式上的不同。</p>
</blockquote>
<h2 data-id="heading-4">自定义构建工具</h2>
<p><code>webpack</code> + <code>vue-loader</code> 可以实现针对 Vue 项目的自定义构建。</p>
<h2 data-id="heading-5">Vue With Vscode</h2>
<h3 data-id="heading-6">Vetur</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.github.io%2Fvetur%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.github.io/vetur/" ref="nofollow noopener noreferrer"><code>Vetur</code></a>是 Vue 社区专门打造的一款 VScdoe 插件，目的于完善在 Vscode 中开发 Vue 的体验，解决自定义的 <code>.vue</code> 文件类型不能被识别的问题。</p>
<p>它主要提供了以下功能：</p>
<ul>
<li>基于 <code>prettier</code> 格式化模板、CSS、JS。</li>
<li>语法高亮</li>
<li>Emmet 自动生成模板中的 HTML 标签</li>
<li>错误检查与质量检查</li>
<li>代码提示与补全
<ul>
<li>例如一些内置组件 <code>transition</code>，<code>component</code> 等。</li>
<li>内置组件的一些属性提示</li>
<li>Vue 组件实例上的方法与属性提示</li>
</ul>
</li>
<li>代码片段 - Snippet
<ul>
<li>快速创建 <code>template</code> 标签</li>
<li>快速创建基于不同css预处理器的 style 标签</li>
<li>快速创建基于 composition-api、typescript 或者传统 javascript 的 script 标签。</li>
</ul>
</li>
</ul>
<p>需要注意的是 <code>Vetur</code> 内置了对模板、逻辑与样式的的错误检查，但是代码质量检查是基于 <code>Eslint</code> 实现，因此要确保 VScode 已经安装了 <code>Eslint</code> 插件。</p>
<blockquote>
<p>如果存在 <code>ESlint</code> 与 <code>Prettier</code> 格式化规则冲突时，则需要在 <code>.eslintrc.js</code> 中覆盖 <code>prettier</code> 规则即可。</p>
</blockquote></div>  
</div>
            