
---
title: '7x0 精读Vue官方文档 - 全局配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5522'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 17:46:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=5522'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<hr>
<p>以下都是 <code>Vue.config</code> 的配置项。</p>
<h2 data-id="heading-1">config.silent</h2>
<p>取消 Vue 的日志与警告输出。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.config.silent = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">config.optionMergeStrategies</h2>
<p>自定义组件选项的合并策略。
主要作用与：</p>
<ul>
<li><code>Vue.extend(&#123;...&#125;)</code></li>
<li>Vue 的 <code>mixin</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">Vue.config.optionMergeStrategies.custom_option = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">parent, value, vm</span>) </span>&#123;
   <span class="hljs-comment">/*
    * parent 父级实例
    * value 当前选项的值
    * vm 实例上下文
    */</span>
    <span class="hljs-keyword">return</span> value + <span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">config.devtools</h2>
<p>配置是否允许 <code>vue-devtools</code> 工具检查代码。开发版本默认为 <code>true</code>，生产版本默认为 <code>false</code></p>
<h2 data-id="heading-4">config.errorHandler</h2>
<p>Vue 运行时的错误信息捕获处理函数，可以用于结合错误追踪服务 <code>Sentry</code> 一起使用。</p>
<h2 data-id="heading-5">config.warnHandler</h2>
<p>Vue 运行时的警告信息捕获处理函数。</p>
<blockquote>
<p>只用于开发版本。</p>
</blockquote>
<h2 data-id="heading-6">config.ignoredElements</h2>
<p>用来忽略未知元素产生的警告提示 —— <code>Unknown custom element</code>。
可能会产生的原因有：</p>
<ol>
<li>使用了基于 Web Components APIs 的自定义标签元素。</li>
<li>忘记了组件的注册。</li>
<li>组件的元素名称拼写错误。</li>
</ol>
<h2 data-id="heading-7">config.keyCodes</h2>
<p>为按键码自定义别名。</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.config.keyCodes = &#123;
    <span class="hljs-string">'media-play-pause'</span>: <span class="hljs-number">179</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：<code>key</code> 名只支持 <code>kebab-case</code> 并不支持 <code>camelCase</code> 或 <code>PascalCase</code></p>
</blockquote>
<h2 data-id="heading-8">config.performance</h2>
<p>适用于开发模式和支持 <code>performance.mark</code> API 的浏览器上。
通过 <code>vue-devtools</code> 的 <code>performance</code> 工具可以启用对组件初始化、编译、渲染和打补丁的性能追踪。</p>
<h2 data-id="heading-9">config.productTip</h2>
<p>用于控制开发环境的提示信息。</p>
<pre><code class="hljs language-text copyable" lang="text">You are running Vue in development mode.
Make sure to turn on production mode when deploying for production.
See more tips at https://vuejs.org/guide/deployment.html
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            