
---
title: 'Vue v3.1.0 Pluto 发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d92d356d2214da5a2e9e27d9b504cfd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 22:49:13 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d92d356d2214da5a2e9e27d9b504cfd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着 Vue 3 生态的逐步稳定，Vue 3 的迁移版本也提上了日程。</p>
<p>就在今天早些时候，Vue 官方团队正式发布了 v3.1.0 版本。</p>
<p>后续版本都会致力于让你更轻松地从 Vue 2 迁移至 Vue 3。</p>
<p>为此，官方团队做了很多努力。</p>
<h2 data-id="heading-0">文档更新</h2>
<p>官方团队针对迁移文档进行了进一步的完善 <a href="https://github.com/vuejs/docs-next/pull/1033/files" title="PR 1033" target="_blank" rel="nofollow noopener noreferrer">PR 1033</a></p>
<p>其中尤大在 <a href="https://vue.w3ctech.com/" title="Vue Conf China 2021" target="_blank" rel="nofollow noopener noreferrer">Vue Conf China 2021</a> 上提到的 <a href="https://github.com/vuejs/vue-next/tree/master/packages/vue-compat" title="Vue Compat" target="_blank" rel="nofollow noopener noreferrer">Vue Compat</a> 仓库的文档，也一并合并到了官方文档中，其连接为 <a href="https://v3.vuejs.org/guide/migration/migration-build.html" title="迁移构建" target="_blank" rel="nofollow noopener noreferrer">迁移构建</a>。</p>
<h2 data-id="heading-1">破坏性更改</h2>
<p>本次更新中存在两个小的破坏性更改，</p>
<h3 data-id="heading-2">1. props 中声明的 key，将一直存在。不管父组件是否传递该 key。</h3>
<p>源码中的核心代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ensure all declared prop keys are present</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> instance.propsOptions[<span class="hljs-number">0</span>]) &#123;
  <span class="hljs-keyword">if</span> (!(key <span class="hljs-keyword">in</span> props)) &#123;
    props[key] = <span class="hljs-literal">undefined</span> <span class="hljs-comment">// 如果 key 不存在 props 中，将默认在 props 中进行声明</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这会导致一些行为的变化，比如(issues 中的案例)：</p>
<p>因为字段一直存在，所以在使用 <code>hasOwnProperty</code> 时，就会出现异常情况。</p>
<p>Old:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> propsToAdd = &#123;
  <span class="hljs-string">'value'</span>: props.hasOwnProperty(<span class="hljs-string">'modelValue'</span>) ? props.modelValue : props.value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>New:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> propsToAdd = &#123;
  <span class="hljs-string">'value'</span>: props.hasOwnProperty(<span class="hljs-string">'modelValue'</span>) && props.modelValue !== <span class="hljs-literal">undefined</span> ? props.modelValue : props.value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方文档给出了相应解释：</p>
<blockquote>
<p>Similar to <code>this.$props</code> when using Options API, the <code>props</code> object will only contain explicitly declared props. Also, all declared prop keys will be present on the <code>props</code> object, regardless of whether it was passed by the parent component or not. Absent optional props will have a value of <code>undefined</code>.</p>
<p>If you need to check the absence of an optional prop, you can give it a Symbol as its default value:</p>
</blockquote>
<p>如果你遇到了这方面的问题，可以按照如下方式修改：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isAbsent = <span class="hljs-built_in">Symbol</span>()

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">foo</span>: &#123; <span class="hljs-attr">default</span>: isAbsent &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (props.foo === isAbsent) &#123;
      <span class="hljs-comment">// foo is absent</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关链接：</p>
<ul>
<li><a href="https://github.com/vuejs/vue-next/issues/3288" title="issue 3288" target="_blank" rel="nofollow noopener noreferrer">issue 3288</a></li>
<li><a href="https://github.com/vuejs/vue-next/issues/3889" title="issue 3889" target="_blank" rel="nofollow noopener noreferrer">issue 3889</a></li>
<li><a href="https://github.com/vuejs/vue-next/commit/4fe4de0a49ffc2461b0394e74674af38ff5e2a20" title="commit" target="_blank" rel="nofollow noopener noreferrer">commit</a></li>
<li><a href="https://github.com/vuejs/docs-next/commit/e41f44167f637bbff1f7c3ee041e8e7b37d56e22" title="文档更新" target="_blank" rel="nofollow noopener noreferrer">文档更新</a></li>
</ul>
<h3 data-id="heading-3">2. <code>optionsMergeStrategies</code> 不再接收组件实例作为第三个参数</h3>
<p>这个对大家影响不大，主要用于生成警告。</p>
<h2 data-id="heading-4">弃用</h2>
<ul>
<li><code>app.config.isCustomElement</code> 已被废弃，应使用 <code>app.config.compilerOptions</code> 下的 <code>isCustomElement</code> 选项。<a href="https://v3.vuejs.org/api/application-config.html#compileroptions" title="文档" target="_blank" rel="nofollow noopener noreferrer">文档</a></li>
<li><code>delimiters</code> 组件选项已被废弃，请使用 <code>compilerOptions</code> 下的 <code>delimiters</code> 选项。<a href="https://v3.vuejs.org/api/options-misc.html#compileroptions" title="文档" target="_blank" rel="nofollow noopener noreferrer">文档</a></li>
<li><code>v-is</code> 已弃用，请使用 <code>is="vue:xxx"</code> 代替。<a href="https://v3.vuejs.org/api/special-attributes.html#is" title="文档" target="_blank" rel="nofollow noopener noreferrer">文档</a></li>
</ul>
<h2 data-id="heading-5">总结</h2>
<p>其他更新，可以参阅我们编写的 <a href="https://juejin.cn/post/6960322464471744542" target="_blank">Vue 3.1.0 beta 版本发布</a>。</p>
<p>最后附上尤大在 Vue Conf 上的演讲，可以帮助大家更进一步的理解。</p>
<p><a href="https://www.bilibili.com/video/BV1JK4y1G7bf?p=1&share_medium=iphone&share_plat=ios&share_source=WEIXIN_MONMENT&share_tag=s_i&timestamp=1622670442&unique_k=qryf5g&share_times=1" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d92d356d2214da5a2e9e27d9b504cfd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></a></p></div>  
</div>
            