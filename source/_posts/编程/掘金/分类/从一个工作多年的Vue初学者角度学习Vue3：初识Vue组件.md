
---
title: '从一个工作多年的Vue初学者角度学习Vue3：初识Vue组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/222251fe505a411f8f1c9a190f828b57~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 05:19:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/222251fe505a411f8f1c9a190f828b57~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文字数：4708，阅读完全文大约要花费30分钟。</p>
<p>一直觉得框架只是工具，工作中用不上就没必要去学，要用的时候再去学习即可。</p>
<p>所以对国内非常火爆的Vue框架也只有一个初浅的印象：</p>
<ul>
<li>Vue是一个渐进式的JavaScript框架</li>
<li>Vue2通过defineProperty拦截对象实现响应式，而Vue3则改成了Proxy实现响应式</li>
<li>Vue3增加了Composite API以解决代码复用和可维护性问题</li>
</ul>
<p>为了拓展DevUI的生态，让DevUI的最佳实践能够服务更多的开发者，今年3月份我们在社区正式发起了<a href="https://juejin.cn/post/6992233443585163300" target="_blank" title="https://juejin.cn/post/6992233443585163300">Vue DevUI开源项目</a>，吸引了很多社区小伙伴们的加入。</p>
<blockquote>
<p>目前已经有<code>35+</code>位组件田主认领了<code>60+</code>个组件👏🎉🥳</p>
</blockquote>
<p>以下是贡献者花名册：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui%2Fwikis%2F%25E8%25B4%25A1%25E7%258C%25AE%25E8%2580%2585%25E8%258A%25B1%25E5%2590%258D%25E5%2586%258C" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui/wikis/%E8%B4%A1%E7%8C%AE%E8%80%85%E8%8A%B1%E5%90%8D%E5%86%8C" ref="nofollow noopener noreferrer">gitee.com/devui/vue-d…</a></p>
<p>我正好也利用这个契机，系统地学习了一遍Vue3，趁着刚学完，从初学者的角度总结Vue3的关键特性（只是从我个人的角度，不一定完全按照文档来）。</p>
<p>本文从以下技术栈的角度进行阐述：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Freleases%2Ftag%2Fv2.4.4" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/releases/tag/v2.4.4" ref="nofollow noopener noreferrer">vite@2.4.4</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Freleases%2Ftag%2Fv3.1.5" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/releases/tag/v3.1.5" ref="nofollow noopener noreferrer">vue@3.1.5</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Freleases%2Ftag%2Fv4.3.5" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/TypeScript/releases/tag/v4.3.5" ref="nofollow noopener noreferrer">typescript@4.3.5</a></li>
</ul>
<p>💡提示：截止到2021年8月7日，以上库/框架的版本都是最新版本。</p>
<p>文章较长，如果想直接看小结，可以跳转到以下章节：
<a href="https://juejin.cn/post/6993676123385102373#heading-17" target="_blank" title="https://juejin.cn/post/6993676123385102373#heading-17">6 小结</a></p>
<h1 data-id="heading-0">1 先跑起来再说</h1>
<p>对于一个小白来说，要学习一门新技术，最快的方式就是：</p>
<blockquote>
<p>先跑起来再说</p>
</blockquote>
<p>跑起来之后，我们会对这门新技术有一个直观的印象，后续看文档也会更清晰。</p>
<p>另外就是要多思考，带着问题去学习，记忆会更深刻，也更容易理解其中的原理。</p>
<p>后续我们学习过程中学到的新知识点，我都会加上官网的链接，不过这些官网资料只是一个进一步学习的参考，关键是我们自己要有思考，并带着问题去学习。</p>
<p>Vite是尤大大比较推荐的开发Vue3的工具，听说非常丝滑，所以第一步先建一个Vite的工程跑起来。</p>
<p>直接参考官网的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/" ref="nofollow noopener noreferrer">开始</a>章节，一个命令就搞定啦：</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn create vite learning-vue3 --template vue-ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>--template</code>这个参数是选择一个工程模板，我们选择的是<code>vue-ts</code>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Ftree%2Fmain%2Fpackages%2Fcreate-vite%2Ftemplate-vue-ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/tree/main/packages/create-vite/template-vue-ts" ref="nofollow noopener noreferrer">Vue 3 + Typescript + Vite</a></p>
<p>Vite除了创建Vue的工程，还可以创建React/Preact/Svelte等多种框架的工程。</p>
<p>Vite果然非常快，不到3s就创建了一个基本的脚手架工程。</p>
<pre><code class="copyable">$ yarn create vite learning-vue3 --template vue-ts
yarn create v1.22.10
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 🔨  Building fresh packages...

success Installed "create-vite@2.5.4" with binaries:
      - create-vite
      - cva
[###########################################################################################################################################################################################################] 232/232
Scaffolding project in /devui/kagol/learning-vue3...

Done. Now run:

  cd learning-vue3
  yarn
  yarn dev

✨  Done in 2.69s.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且非常友好地提示我们下一步要执行的命令：</p>
<pre><code class="copyable">Done. Now run:

  cd learning-vue3
  yarn
  yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照提示操作，我们很快就能将项目跑起来了！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/222251fe505a411f8f1c9a190f828b57~tplv-k3u1fbpfcp-watermark.image" alt="vite.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">2 Vue组件初步印象</h1>
<p>启动画面最底下，有一个指引，让我们编辑<code>components/HelloWorld.vue</code>这个文件，测试下热更新（HMR）的功能。</p>
<p>我们找到这个文件<code>HelloWorld.vue</code>，不着急修改它，先来观察下它的结构。</p>
<p>这个文件是以<code>.vue</code>为文件后缀的，代表这是一个<code>Vue组件</code>。</p>
<p>一个Vue组件包含三个部分：</p>
<ul>
<li>最顶部是一个<code><template></code>标签</li>
<li>中间是一个<code><script lang="ts"></code>标签</li>
<li>最下面是一个<code><style scoped></code>标签</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71aae96d8b8648a1ab1a8578330fbc6b~tplv-k3u1fbpfcp-watermark.image" alt="HelloWorld.vue.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这和我们最早学习前端编写html页面的结构是一样的，将<code>HTML</code>/<code>CSS</code>/<code>JavaScript</code>分成三个区块。</p>
<p>不过我们还是注意到一点不同：</p>
<ul>
<li>HTML部分是用<code><template></code>这个特殊的标签包裹起来的；</li>
<li><code><script></code>部分多了一个<code>lang="ts"</code>属性，代表支持<code>TypeScript</code>；</li>
<li><code><style></code>部分多了一个<code>scoped</code>属性，代表局部样式，即：这里面写的样式只针对当前这个Vue组件。</li>
</ul>
<p>以上就是目前观察到的Vue组件的基本特点。</p>
<h1 data-id="heading-2">3 <template>分析</h1>
<p>我们把<code><template></code>/<code><script></code>/<code><style></code>三个标签展开，看下里面的结构。</p>
<p>先看下<code><template></code>，里面元素比较多，先都收起来，看下大致结构。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/180766c7c7e74374a4d34aaa58976b8f~tplv-k3u1fbpfcp-watermark.image" alt="template.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们注意到里面就是一些html元素，似乎和写html没什么区别，不过仔细一看，还有会有些不同：</p>
<ul>
<li>首先就是第2行的双大括号包裹的部分<code>&#123;&#123; msg &#125;&#125;</code>，这和我们之前写的html有点不一样，这是一种Vue的模板语法，叫<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Ftemplate-syntax.html%23%25E6%2596%2587%25E6%259C%25AC" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/template-syntax.html#%E6%96%87%E6%9C%AC" ref="nofollow noopener noreferrer">文本插值</a>，里面的msg是组件的变量，变量的值会被渲染到<code><h1></code>标签里面。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第30行是一个<code><button></code>标签，我们很熟悉它是一个按钮，里面也有一个<code>文本插值</code>，绑定的是<code>count</code>变量，还有一个<code>@click</code>属性我们没见过，这是Vue<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fevents.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/events.html" ref="nofollow noopener noreferrer">事件绑定</a>的语法，绑定了button的点击事件。</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++"</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Vite热更新 - template</h2>
<p>我们尝试修改下<code>template</code>里面的内容，比如将最后一行的：</p>
<pre><code class="copyable">hot module replacement.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改成</p>
<pre><code class="copyable">hot module replacement(HMR).
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看下页面会有什么变化。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c69ce5d853e642e8b678fceb4b57a65e~tplv-k3u1fbpfcp-watermark.image" alt="Vite热更新-template.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从以上动图可以看出，修改完<code>template</code>中的内容，一保存文件，页面内容立马刷新，几乎没有任何延迟，页面也没有刷新，开发体验非常丝滑。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae4f6d311fd54fb79d1240b7c00c6766~tplv-k3u1fbpfcp-watermark.image" alt="猫猫震惊.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">4 <script>分析</h1>
<p>这部分是全文的核心部分，内容较长，如果想直接看本章节的小结，可以点击直通车链接：
<a href="https://juejin.cn/post/6993676123385102373#heading-13" target="_blank" title="https://juejin.cn/post/6993676123385102373#heading-13">4.9 小结</a></p>
<p>模板部分我们已经有了一个初步的了解，再来看看脚本部分。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b444d74ec64d4c319978642036a587a8~tplv-k3u1fbpfcp-watermark.image" alt="script.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">4.1 导入Vue方法</h2>
<p>脚本的第一行从<code>vue</code>导入了两个方法：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fapi%2Frefs-api.html%23ref" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/api/refs-api.html#ref" ref="nofollow noopener noreferrer">ref</a>：返回一个响应式且可变的ref对象；</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fapi%2Fglobal-api.html%23definecomponent" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/api/global-api.html#definecomponent" ref="nofollow noopener noreferrer">defineComponent</a>：用来定义一个同步的Vue组件。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个方法是高频方法，必须牢牢记住。</p>
<h2 data-id="heading-6">4.2 导出Vue组件</h2>
<p>第39行导出了一个Vue组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-attr">setup</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> &#123; count &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue组件通过<code>defineComponent</code>方法来定义，该方法的参数是一个对象，该对象有3个属性：</p>
<ul>
<li>name：一个字符串，代表组件的名字；</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fcomponent-props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/component-props.html" ref="nofollow noopener noreferrer">props</a>：一个对象，代表组件的入参，也就是组件与外部进行交互的一个口子，外部使用组件时，可以通过<code>props</code>往组件内部传递数据；</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fcomposition-api-setup.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/composition-api-setup.html" ref="nofollow noopener noreferrer">setup</a>：一个箭头函数，这是Vue3新推出的<code>Composite API</code>的入口，会在组件创建之前、props被解析之后执行。</li>
</ul>
<h2 data-id="heading-7">4.3 组件入参</h2>
<p>第42行定义了一个msg变量，之前我们在<code>template</code>中已经见过它，可是它的值是什么呢？</p>
<pre><code class="copyable">  props: &#123;
    msg: &#123;
      type: String,
      required: true
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们注意到msg是嵌套在props里面的，代表它是组件的一个入参，是组件与外部交互的API，那么它的值就应该是从外部传进来的。</p>
<p>从哪儿传进来的呢？使用组件是通过它的名字<code>name</code>来使用的，所以我们在源代码里面搜索组件的名字：<code>HelloWorld</code>，发现是在<code>App.vue</code>中使用的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Hello Vue 3 + TypeScript + Vite"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4.4 使用Vue组件</h2>
<p>使用一个组件和使用一个普通的html标签（比如div）几乎是一样的，唯一不同的是使用组件之前需要先导入并声明该组件。</p>
<p>使用组件的方式很简单，只需要3步：</p>
<ul>
<li>导入组件</li>
<li>声明组件</li>
<li>使用组件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d825aca830c4721a6f007e56628934d~tplv-k3u1fbpfcp-watermark.image" alt="使用组件.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">4.5 Vite热更新 - script</h2>
<p>我们尝试修改下这个msg的值（比如改成：<code>Hello everyone! I'm learning Vue 3 + TypeScript + Vite</code>），看下页面会有什么变化。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ae6f87201cc43d1848f796ca258dcfa~tplv-k3u1fbpfcp-watermark.image" alt="Vite热更新-script.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从以上动图可以看出，与修改<code>template</code>的效果一样，修改完msg的值，一保存文件，页面内容立马刷新，之前的：</p>
<pre><code class="copyable">Hello Vue 3 + TypeScript + Vite
<span class="copy-code-btn">复制代码</span></code></pre>
<p>立马变成了：</p>
<pre><code class="copyable">Hello everyone! I'm learning Vue 3 + TypeScript + Vite
<span class="copy-code-btn">复制代码</span></code></pre>
<p>几乎没有任何延迟，页面也没有刷新，开发体验非常丝滑。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75cb63de090f4c6caf97ebc306e61520~tplv-k3u1fbpfcp-watermark.image" alt="猫猫震惊2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">4.6 响应式的ref对象</h2>
<p>第48行定义了一个<code>count</code>变量：</p>
<pre><code class="copyable">  setup: () => &#123;
    const count = ref(0)
    return &#123; count &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前我们在<code>template</code>中也见过这个变量，它的值就是这里定义的<code>count</code>，我们注意到这个<code>count</code>的值是调用<code>ref</code>函数之后返回的，函数的参数是数字<code>0</code>。为什么要包一层ref，而不是直接将0赋值给count变量呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接赋值不是更简洁吗？</p>
<p>我们先来看下官网对ref的介绍：</p>
<pre><code class="copyable">接受一个内部值并返回一个响应式且可变的 ref 对象。ref 对象具有指向内部值的单个 property `.value`。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了理解ref函数的作用，我们先尝试在页面里点击一下这个<code>count is: 0</code>的按钮。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc8004b4c6014c668f5226d629751759~tplv-k3u1fbpfcp-watermark.image" alt="button.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击完发现里面的值立马变成：</p>
<pre><code class="copyable">count is: 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们将：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改成：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次点击button按钮，发现值没有变。</p>
<p>我们大致能理解ref函数返回<code>响应式ref对象</code>的含义：</p>
<blockquote>
<p>响应式的意思就是这个变量的值是动态的，某些动作（点击按钮）改变了它的值，模板里面的文本插值立马也会跟着变化，从而页面里面的内容也会跟着刷新。</p>
</blockquote>
<p>如果count没有被ref函数包裹，那它就不是响应式的，点击按钮改变它的值之后，模板的内容不会跟着变化。</p>
<p>有一个需要注意的点：</p>
<blockquote>
<p>setup中定义的变量必须返回，才能在template中使用，否则插值不会被渲染，并且会在浏览器控制台警告提示这个变量没有在实例中定义。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84253ee22b094d038969e0f3ca723aa2~tplv-k3u1fbpfcp-watermark.image" alt="warn.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">[Vue warn]: Property "count" was accessed during render but is not defined on instance.
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">4.7 TypeScript支持</h2>
<p>前面提到<code><script></code>中的<code>lang="ts"</code>属性是用来支持TypeScript的，我们来试试看吧。</p>
<p>先定义一个type类型：</p>
<pre><code class="hljs language-js copyable" lang="js">type Size = <span class="hljs-string">'sm'</span> | <span class="hljs-string">'md'</span> | <span class="hljs-string">'lg'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在setup方法中定义一个变量用来使用这个类型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> size = ref<Size>(<span class="hljs-string">'md'</span>)

<span class="hljs-keyword">return</span> &#123; size &#125; <span class="hljs-comment">// 记得返回哦</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在template通过文本插值使用该变量：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; size &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们在<code><script></code>中加了<code>lang="ts"</code>，所以页面能正常显示<code>md</code>。</p>
<p>这时我们把<code>lang="ts"</code>去掉，保存文件并刷新页面，页面变成白页，并且浏览器控制台也报错：</p>
<pre><code class="copyable">Uncaught SyntaxError: unexpected token: identifier
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面定义的<code>Size</code>类型也出现了红色的波浪下划线。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbde8365faca418a8f78122b590f965e~tplv-k3u1fbpfcp-watermark.image" alt="Size.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>提示type类型声明必须在TypeScript文件中使用：</p>
<pre><code class="copyable">Type aliases can only be used in TypeScript files.
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">4.8 TypeScript类型错误高亮提示</h2>
<p>这样似乎看不出TypeScript的优势，我们丰富下这个demo，来看看TypeScript的好处。</p>
<p>我们加一个<code>addSize</code>方法，用来增加尺寸：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> addSize = <span class="hljs-function">() =></span> &#123;
  size.value = <span class="hljs-string">'lg'</span> <span class="hljs-comment">// 给size变量赋值为Size类型中定义好的值是没问题的</span>
&#125;

<span class="hljs-keyword">return</span> &#123; addSize &#125; <span class="hljs-comment">// 记得返回哦</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>template</code>中使用该方法：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addSize"</span>></span>Add size<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果将size赋值为Size类型定义的值，比如：<code>large</code>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.github.io%2Fvetur%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.github.io/vetur/" ref="nofollow noopener noreferrer">Vetur</a>类型检查马上就会提示，相应的赋值代码也会出现红色波浪下划线：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93aa431338b74f2083cebfaa3686a293~tplv-k3u1fbpfcp-watermark.image" alt="ts.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时我们能够立即警觉：</p>
<blockquote>
<p>这里的代码可能写得有问题</p>
</blockquote>
<p>💡提示：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Doctref.vetur" target="_blank" rel="nofollow noopener noreferrer" title="https://marketplace.visualstudio.com/items?itemName=octref.vetur" ref="nofollow noopener noreferrer">Vetur</a>是一款VSCode插件，用来做<code>.vue</code>文件的语法高亮和TypeScript类型检查等。</p>
<p>非常感谢你能阅读到这里，还有最后5分钟就阅读完了，通过小结巩固下学到的知识，然后喝杯水放松下吧😋</p>
<h2 data-id="heading-13">4.9 小结</h2>
<p><code><script></code>部分基本就是这些，我们做一个简单的小结：</p>
<ol>
<li>defineComponent方法用于定义Vue组件</li>
<li>Vue组件的名字通过name属性来定义，名字可以用来唯一区分一个组件</li>
<li>Vue组件通过props属性来与外界进行数据交互</li>
<li>setup方法是Vue3 Composite API的入口</li>
<li>使用Vue组件和使用html元素差不多，只是需要先导入、声明组件才能使用</li>
<li>ref用于返回一个响应式对象</li>
<li><code>lang="ts"</code>用来支持TypeScript</li>
</ol>
<h1 data-id="heading-14">5 <style>分析</h1>
<p>最后再来看下<code><style></code>部分。</p>
<pre><code class="copyable"><style scoped>
a &#123;
  color: #42b983;
&#125;

label &#123;
  margin: 0 0.5em;
  font-weight: bold;
&#125;

code &#123;
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看着和写CSS没什么区别，只是有一点不一样（前面也提到过），就是<code><style></code>标签中增加了一个<code>scoped</code>属性，这个属性用来定义局部样式，里面写的样式只针对当前组件生效。</p>
<h2 data-id="heading-15">5.1 局部样式</h2>
<p>为了理解局部样式的含义，我们在其他组件中也写一个<code><code></code>标签，看下它的样式是不是和HelloWorld组件中的一样，HelloWorld组件中，code标签样式是这样的（有一个灰色的背景色）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33af2073ba4b4ec2b56986cc9c90d435~tplv-k3u1fbpfcp-watermark.image" alt="code.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">code &#123;
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在App.vue中也写一个code标签：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">code</span>></span>Vue DevUI<span class="hljs-tag"></<span class="hljs-name">code</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31adf601d7bf424cb668f4a50fcced1f~tplv-k3u1fbpfcp-watermark.image" alt="App.vue.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现在HelloWorld组件的style中写的样式并不会影响App组件中的code，这就是局部样式。</p>
<p>通过对比两者的html元素，发现HelloWorld组件中的元素都加上了一个<code>data-v-</code>开头的特殊属性，相应的css规则也加上了这个选择器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e63dd660150492b8dfe39225e3ee177~tplv-k3u1fbpfcp-watermark.image" alt="scoped.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一点和Angular中的<code>encapsulation</code>属性非常类似。</p>
<h2 data-id="heading-16">5.2 Vite热更新 - style</h2>
<p>除了<code>template</code>和<code>script</code>的热更新，Vite也支持<code>style</code>样式的热更新，一样的丝滑，就不再赘述。</p>
<h1 data-id="heading-17">6 小结</h1>
<p>通过本文，我们使用Vite启动了一个初始的项目工程，并且对Vue组件有了一个初步的认识，现在做个简单的小结巩固下吧。</p>
<ol>
<li>先是搭建了一个Vue3+TypeScript+Vite的工程</li>
<li>然后了解了一下Vue组件的整体结构（<code>.vue</code>文件，template+script+style）</li>
<li>接着对template、script、style区块进行了单独的分析</li>
<li>template和html很类似，只是增加了一些Vue特有的<code>模板语法</code>，如<code>文本插值</code>、事件绑定等</li>
<li>script是定义组件逻辑的地方，可以通过<code>lang="ts"</code>支持TypeScript</li>
<li><code>defineComponent</code>和<code>ref</code>是Vue提供的两个非常常用的方法，defineComponent用来定义Vue组件，ref用来生成一个响应式的ref对象</li>
<li>defineComponent方法的参数是一个对象，其中的<code>name</code>属性用来定义Vue组件的名字，使用组件时通过名字引用</li>
<li>使用Vue组件和使用html标签很类似，只是需要先导入和声明组件</li>
<li><code>props</code>属性用来定义组件与外部交互的API，是组件设计的关键</li>
<li><code>setup</code>方法是Vue3 <code>Composite API</code>的入口，它会在组件生成之前、props解析之后执行</li>
<li>style用来编写组件的样式，可以通过<code>scoped</code>支持只对当前组件生效的局部样式</li>
</ol>
<p>本篇文章到这里就结束了，以下是Vue DevUI开源项目的介绍，如果感兴趣可以选择继续阅读。</p>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui" ref="nofollow noopener noreferrer">Vue DevUI</a>正在火热🔥开发中，欢迎大家踊跃参与进来，一起共建一个基于DevUI设计理念的Vue开源组件库。</p>
<p>和社区其他组件库相比，我们主要有以下优势：</p>
<ol>
<li>vue devui是基于devui沉浸、至简、灵活的设计价值观进行设计和开发的，这是经受过devcloud众多商用项目考验的，确保质量和体验</li>
<li>vue devui的定位是一个跨端组件库，确保满足pc/mobile多端用户的需求</li>
<li>devui是一个专注于用户体验的团队，背后有50+优秀的设计师和工程师，确保产品的优秀体验和技术的先进性</li>
<li>我们有多个特色组件，比如甘特图、分类搜索、精灵导航、同时支持自定义字体图标和自定义svg的图标组件等</li>
<li>我们支持按需加载、自定义主题、国际化等组件库标配特性。</li>
</ol>
<p>以下是该项目的源码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui" ref="nofollow noopener noreferrer">gitee.com/devui/vue-d…</a></p>
<p>参与贡献可以加小助手微信：devui-official，拉你进Vue DevUI核心成员小组～😋😋</p>
<p>欢迎关注我们<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2F%2522" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/%22" ref="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/devcloudfe/ng-devui" ref="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/admin-page/home" ref="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-18">再次预告：DevUI 12 和 DevUI Admin 2.0 马上就要来了！</h1>
<blockquote>
<p>DevUI 将于本月10日发布 DevUI 12 版本，除了升级 Angular 12 之外，更有超多有趣的新特性，尽情期待！</p>
</blockquote>
<blockquote>
<p>DevUI Admin 2.0 版本也将在本月17号重磅发布，提供了一项神奇的黑科技，让我们拭目以待吧！</p>
</blockquote>
<p>参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/introduction.html" ref="nofollow noopener noreferrer">Vue3中文文档</a></p></div>  
</div>
            