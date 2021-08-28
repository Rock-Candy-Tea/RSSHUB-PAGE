
---
title: 'Vue起步'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a99955b35a640e180f25d69831cd651~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 01:39:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a99955b35a640e180f25d69831cd651~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 两个版本的区别</h1>
<p>进行开发时，Vue有两个使用版本：<strong>完整版</strong>与<strong>非完整版</strong>。Vue3较Vue2有一些区别，但总体区别不大。</p>
<p>在Vue 3中，官方推荐的CDN引入方式如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>国内用户可以用bootcdn来操作：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/vue/3.2.0-beta.7/vue.cjs.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但以上两种方式引入CDN引入的都是完整版。在官方文档中还有一种说法是<code>runtime(运行时)</code>版本，它的引入方式如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/vue/3.2.0-beta.7/vue.runtime.global.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>runtime</code>版本即我们所说的<strong>非完整版</strong>，完整版又被称为<code>runtime + complier</code>(即<code>运行时+编译器</code>)。官方文档截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a99955b35a640e180f25d69831cd651~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一句话总结：<code>runtime</code>版本没有编译器(complier)，一旦<code>runtime</code>版本加了编译器之后就是完整版。</p>
<p>更详细的解说：</p>
<p>在<code>runtime</code>中，如果要在视图(view)中创建标签时，需要将标签写到<code>render</code>函数里，并用<code>h</code>来创建标签。例如：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">Vue.createApp(&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> Vue.h(<span class="hljs-string">'div'</span>, &#123;&#125;, <span class="hljs-built_in">this</span>.hi)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是完整版，那么直接作为<code>template</code>选项的参数即可：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">Vue.createApp(&#123;
    <span class="hljs-attr">template</span> : <span class="hljs-string">'<div>&#123;&#123; hi &#125;&#125;</div>'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有编译器的<code>runtime</code>版本可以节省40%左右的空间，并且默认使用<code>runtime</code>版本。</p>
<h1 data-id="heading-1">2. template和render的使用</h1>
<p>Vue组件(即<code>.vue</code>文件)中传统三大部分：</p>
<ul>
<li><code>template</code></li>
<li><code>script</code></li>
<li><code>style</code></li>
</ul>
<p>三大组件中<code>template</code>是重要内容。示例：</p>
<pre><code class="hljs language-Vue copyable" lang="Vue"><template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其作用，官网描述如下：</p>
<blockquote>
<p>一个字符串模板，用作 component 实例的标记。模板将会<strong>替换</strong>所挂载元素的 <code>innerHTML</code>。挂载元素的任何现有标记都将被忽略，除非模板中存在通过插槽分发的内容。
<br>
如果字符串以 <code>#</code> 开始，则它将被用作 <code>querySelector</code>，并使用匹配元素的 innerHTML 作为模板字符串。这允许使用常见的 <code><script type="x-template"></code> 技巧来包含模板。</p>
</blockquote>
<p>而<code>render</code>函数：</p>
<blockquote>
<p>字符串模板之外的另一种选择，允许你充分利用 JavaScript 的编程功能。</p>
</blockquote>
<p>官网示例如下：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">my-title</span> <span class="hljs-attr">blog-title</span>=<span class="hljs-string">"A Perfect Vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其对应的<code>render</code>函数：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> &#123; createApp, h &#125; = Vue
<span class="hljs-keyword">const</span> app = createApp(&#123;&#125;)
app.component(<span class="hljs-string">'my-title'</span>, &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> h(
      <span class="hljs-string">'h1'</span>,           <span class="hljs-comment">// 标签名称</span>
      <span class="hljs-built_in">this</span>.blogTitle  <span class="hljs-comment">// 标签内容</span>
    )
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">blogTitle</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)

app.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. 使用codesandbox（简称csb）编程</h1>
<p>第一步：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a33349d230047bc81e48b97c9a7a91c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6510b7c876db4d189705950c106cc513~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三步：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdec32eca93540aab2d08ca672193678~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>即可开始编码~~</p>
<p>如果要存储：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05df41cb9c08450896bea64426a329cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：<strong>不要登录</strong>！</p></div>  
</div>
            