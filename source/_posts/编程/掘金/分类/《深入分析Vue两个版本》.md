
---
title: '《深入分析Vue两个版本》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00883df9084475899c6edc1253766ca~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:18:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00883df9084475899c6edc1253766ca~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Vue的两个版本</h1>
<p>Vue有两个版本，分别是完整版和非完整版，</p>
<h2 data-id="heading-1">1.1 完整版</h2>
<p>完整版同时包括编译器(compiler) 和 运行时(runtime)</p>
<p>编译器的功能是将模板字符串编译为 JavaScript 渲染函数(render函数)的代码</p>
<p>运行时的功能包括创建 Vue 实例、渲染并处理虚拟 DOM 等，它包括除了编译器的其他所有功能</p>
<h2 data-id="heading-2">1.2 只包含运行时版</h2>
<p>只包含运行时版就只有运行时，没有编译器</p>
<h1 data-id="heading-3">二、两个版本的区别</h1>



































<table><thead><tr><th></th><th>Vue完整版</th><th>Vue只包含运行时版</th></tr></thead><tbody><tr><td>特点</td><td>有compiler</td><td>没有compiler</td></tr><tr><td>视图</td><td>写在HTML里，或者写在template选项里</td><td>写在render函数里，用h创建标签</td></tr><tr><td>cdn引入</td><td>vue.js</td><td>vue.runtime.js</td></tr><tr><td>webpack引入</td><td>需要配置alias</td><td>默认使用</td></tr><tr><td>vue@cli引入</td><td>需要额外配置</td><td>默认使用</td></tr></tbody></table>
<p>那究竟应该使用哪一个版本呢？</p>
<p>最佳实践是使用 非完整版，然后用vue-loader引入compiler</p>
<p>整个流程思路如下：</p>
<ol>
<li>
<p>对于用户来说，非完整版 （即runtime版）体积小，用户体验好，但只支持h函数</p>
</li>
<li>
<p>对于程序员来说，只能写h函数的话，开发体验不好，如果有compiler, 开发者就能写更直观更语义化的HTML标签和template, 所以我们需要一个compiler</p>
</li>
<li>
<p>vue-loader就可以引入compiler, 把vue文件里的HTML标签和template 会在构建时预编译成 h函数，这样用户和开发者都高兴</p>
</li>
</ol>
<h1 data-id="heading-4">三、template 和 render 的用法</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 需要编译器</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>&#123;&#123; hi &#125;&#125;</div>'</span>
&#125;)

<span class="hljs-comment">// 不需要编译器</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  render (h) &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, <span class="hljs-built_in">this</span>.hi)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>template标签和JS里的template</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vue文件中的template标签</span>
  <template>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>      
          &#123;&#123;n&#125;&#125;
          <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>   
     <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> 
  </template>

<span class="hljs-comment">//js中的template</span>
    template : <span class="hljs-string">`
        <div id="app">      
          &#123;&#123;n&#125;&#125;
          <button @click="add">+1</button>   
        </div> 
    `</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>render函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//不完整版在js中构建视图</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span>&#123; 
       <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, [<span class="hljs-built_in">this</span>.n,h（<span class="hljs-string">'&#123;on:&#123;click:this.add&#125;’,'</span>+<span class="hljs-number">1</span><span class="hljs-string">'])
   &#125;

//不完整版使用vue-loader

//先创建一个demo.vue文件，在里面构建视图
    import demo from "./demo.vue"
     new Vue(&#123;
       el: "#app",
       render(h) &#123;
         return h(demo)
       &#125;
     &#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">三、快速在线上手Vue的神器</h1>
<p>我们可以在codesandbox里在线写Vue的代码，不用任何本地的安装依赖</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fboring-sanderson-7ozng%3Ffile%3D%2Fsrc%2Fmain.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/boring-sanderson-7ozng?file=/src/main.js" ref="nofollow noopener noreferrer">codesandbox.io/s/boring-sa…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00883df9084475899c6edc1253766ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>本文为fjl的原创文章，著作权归本人和饥人谷所有，转载务必注明来源</em></p></div>  
</div>
            