
---
title: 'rollup+vue3开发个人的组件库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7a57a9b0004f28bdead6bc082ba3e4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 01:18:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7a57a9b0004f28bdead6bc082ba3e4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先我们需要知道rollup是干嘛的</p>
<h2 data-id="heading-0">rollup是做什么的？</h2>
<p>rollup是一个JavaScript打包模块器，可以将小代码编译成大块复杂的代码，例如 library 或应用程序。
Rollup 对代码模块使用新的标准化格式，这些标准都包含在 JavaScript 的 ES6 版本中，而不是以前的特殊解决方案，如 CommonJS 和 AMD。ES6 模块可以使你自由、无缝地使用你最喜爱的 library 中那些最有用独立函数，而你的项目不必携带其他未使用的代码。ES6 模块最终还是要由浏览器原生实现，但当前 Rollup 可以使你提前体验。 <br></p>
<p>参考文档： <br>
<a href="https://www.rollupjs.com/guide/tutorial" target="_blank" rel="nofollow noopener noreferrer">rollup中文文档</a> <br>
<a href="https://github.com/rollup/awesome" target="_blank" rel="nofollow noopener noreferrer">rollup插件集合</a></p>
<h2 data-id="heading-1">安装rollup</h2>
<ol>
<li>首选安装<code>node.js</code></li>
<li>使用如下命令进行全局安装</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm install rollup --<span class="hljs-built_in">global</span> <span class="hljs-comment">// or npm i rollup -g</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>查看是否安装成功只需要在终端输入：rollup</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f7a57a9b0004f28bdead6bc082ba3e4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如上则表明全局的<code>rollup</code>安装成功</p>
<h2 data-id="heading-2">实现一个简单的hello world</h2>
<ol>
<li>创建一个文件夹，在文件夹下创建<code>index.js</code>,<code>hello.js</code></li>
</ol>
<p>hello.js代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'hello'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">world</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'world'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;hello, world&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./hello.js'</span>
<span class="hljs-keyword">const</span> result = hello() + world()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>编译，在终端输入如下指令：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npx rollup index.js --file dist/bundle.js --format iife
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现打包了一个dist文件夹如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47bdcc23c7b2433e83123931c5b18469~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
接下来我们看看打包的内容：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c5bd363b02c42c1a47a11d13c6e8402~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个时候我们就会很疑惑了，说好的hello，world呢？其实这个是因为tree-shaking的作用，是不是感觉和webpack类似了。那我们在做一下变形：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;hello, world&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./hello.js'</span>
<span class="hljs-keyword">const</span> result = hello() + world()
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>).innerHTML = result
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在打包看看输出的代码</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b287560cac9841f68f2cec46d7d3a838~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个时候就有了hello，world了，对比发现rollup打包后的代码比webpack更加的清晰，这个我们接下来探讨webpack和rollup的区别。</p>
<h2 data-id="heading-3">webpack和rollup</h2>
<h3 data-id="heading-4">webpack</h3>
<p><strong>大型SPA项目的构建</strong>，也就是我们常说的web应用。</p>
<ul>
<li>通过各种Loader处理各种各样的资源文件</li>
<li>通过各种插件Plugins对整体文件进行一些处理</li>
<li>code spliting对公共模块进行提取</li>
<li>提供一个webpack-dev-server对本地进行开发</li>
<li>支持HMR模块进行热替换</li>
</ul>
<h3 data-id="heading-5">rollup</h3>
<ul>
<li>rollup设计之初就是面向ES module的构建出结构扁平，性能出众的类库</li>
<li>目的是将ES module打包生成特定的JS模块文件，并减少它的体积</li>
<li>编译出来的代码可读性更好，内容小，执行效率更高</li>
<li>配置更加简单</li>
</ul>
<p><strong>顺带说一下ES module规则</strong></p>
<ul>
<li>import语句只能作为模块的顶层出现，不能出现在function if里面这点和commonJS不一样</li>
<li>ES module的模块名只能是字符串常量</li>
<li>不管import的语句位置出现在哪，在模块初始化的时候所有的import都必须是导入完成的</li>
</ul>
<h3 data-id="heading-6">webpack VS rollup</h3>
<p>通过以上我们可以知道构建App应用时选用webpack适合，构建类库rollup更加适合。</p>
<p>接下来开始尝试配置rolluop吧</p>
<h2 data-id="heading-7">rolluop配置</h2>
<ol>
<li>新建一个文件夹<code>rolluplearn</code>目录下执行<code>npm init -y</code></li>
<li>安装rollup</li>
<li>创建如下目录结构，并新建文件<code>rollup.config.js</code></li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8766aed88ea64697857921f4b7a985f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3. 编写rollup配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 读取json文件</span>
<span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">'main.js'</span>,
    <span class="hljs-attr">input</span>: <span class="hljs-string">'main.js'</span>, <span class="hljs-comment">// 入口文件</span>
    <span class="hljs-attr">output</span>: &#123;        
        <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/bundle.js'</span>, <span class="hljs-comment">//打包文件地址</span>
        <span class="hljs-attr">format</span>: <span class="hljs-string">'esm'</span>,          <span class="hljs-comment">// 打包格式为esmodule</span>
    &#125;
    <span class="hljs-attr">plugins</span>: [json()]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>在<code>package.json</code>中编辑打包脚本：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"rollup --config rollup.config.js"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>开始编写main.j和src/test.js文件</li>
</ol>
<p>src/test.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hell = <span class="hljs-function">()=></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hell'</span>)
&#125;
<span class="hljs-keyword">const</span> fn = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fn'</span>)
&#125;

<span class="hljs-keyword">export</span> &#123;
    hell,
    fn 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; fn, hell &#125;<span class="hljs-keyword">from</span> <span class="hljs-string">'./src/test'</span>
<span class="hljs-keyword">import</span> &#123; version &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./package.json'</span>
<span class="hljs-built_in">console</span>.log(version)
fn()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>执行 <code>npm run build</code>，结果如下：</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f492b5a569d2471c8e9a2f0172889ac4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
rollup相对来说比较简单，没有weebpack的配置那么复杂，接下来我们介绍下vue3的插件开发。</p>
<h2 data-id="heading-8">vue3插件系统开发</h2>
<p>给vue3应用添加全局功能，一般是Object有一个<code>install</code>方法或者是直接使用<code>function</code>，它们没有严格的限制，一般有如下几个功能：</p>
<ul>
<li>添加全局方法和属性</li>
<li>添加全局资源和指令</li>
<li>通过全局混入添加一些组件选项</li>
<li>通过config.globalProperties来添加app的实例方法</li>
</ul>
<h3 data-id="heading-9">开发一个插件</h3>
<h4 data-id="heading-10">全局方法</h4>
<p>使用vue-cli创建一个项目，在<code>components</code>下创建<code>test.plugin.ts</code>文件，代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;App&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> plugins = &#123;
    <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">app: App</span>)</span> &#123;
        app.config.globalProperties.$echo = <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'echo plugin'</span>)
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> plugins

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在<code>main.ts</code>中使用进行全局使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> testPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/test.plugin'</span>
createApp(App)
.use(store)
.use(router)
.use(testPlugin)
.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们就注册成功了一个全局方法<code>$echo</code>，接下来我们调用试试看能否成功，
在<code>App.vue</code>写入以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
<span class="hljs-keyword">import</span> &#123; defineComponent, getCurrentInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// getCurrentInstance 返回当前组件的实例对象</span>
    getCurrentInstance()?.appContext.config.globalProperties.$echo()
  &#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看浏览器控制台</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0af48da1d7c64b90980f26cfd09c407d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
说明我们的全局方法已经添加成功，接下来我们看看如何添加全局组件。</p>
<h4 data-id="heading-11">全局组件</h4>
<p>还是在<code>mian.ts</code>中进行一些修改</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;App&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> plugins = &#123;
    <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">app: App</span>)</span> &#123;
        app.config.globalProperties.$echo = <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'echo plugin'</span>)
        &#125;
        app.component(HelloWord.name, HelloWord)
    &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> plugins
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在全局方法的使用中我们已经在<code>main.ts</code>中使用了<code>use</code>方法进行了全局注册，接下来我们只需要在App.vue中进行使用即可，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">HelloWorld</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"Welcome to Your Vue.js + TypeScript App"</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看浏览器发现全局组件已经注册成功
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0275f977d804e2ab6c2217b61fe70a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体来看其实是和vue2差不多的，主要的区别就是：</p>
<ul>
<li>vue2全局方法是挂载在vue的原型对象上的，vue3挂载在<code>app.config.globalProperties</code>方法上</li>
<li>调用的时候vue2可以直接使用this.xxx进行调用，vue3需要<code>getCurrentInstance()?.appContext.config.globalProperties</code>进行调用</li>
</ul>
<p>到这里使用vue3开发一个插件基本算是完成了，接下来我们需要了解一个组件库入口应该如何开发。</p>
<h3 data-id="heading-12">组件库入口问价设计</h3>
<p>我们使用一个组件库的时候一般会有两种引入方式，一个是全局引入，一个是按需加载。所以在导出的时候应该有这样一个index.ts文件:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> componentA <span class="hljs-keyword">from</span> <span class="hljs-string">'./a'</span>
<span class="hljs-keyword">const</span> componentList = [
    componentA
]
<span class="hljs-keyword">const</span> install = (app: App) &#123;
      ...
&#125;
<span class="hljs-comment">// 导出单个</span>
expoert &#123;
...
&#125;
<span class="hljs-comment">// 导出所有</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    install
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>componentA</code>也应该有一个<code>install</code>方法，那么应该如何实现呢？🤔️
在原有的vue-cli下载下来的项目进行一些改造，目录如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7bcb74287ab492cb0a9a743a01b4437~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
现在主要实现<code>components/TText/index.ts</code>和<code>index.ts</code>
components/TText/index.ts</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; App &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 随便写一个组件就行</span>
<span class="hljs-keyword">import</span> TText <span class="hljs-keyword">from</span> <span class="hljs-string">'./TText.vue'</span>

<span class="hljs-comment">// 在组件上添加install方法，方便直接使用单个组件</span>
TText.install = <span class="hljs-function">(<span class="hljs-params">app: App</span>)=></span> &#123;
    app.component(TText.name, TText)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> TText
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.ts</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; App &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> TText <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/TText'</span>
<span class="hljs-comment">// 组件列表</span>
<span class="hljs-keyword">const</span> components = [
  TText
] 
<span class="hljs-comment">// 使用所有组件</span>
<span class="hljs-keyword">const</span> install = <span class="hljs-function">(<span class="hljs-params">app: App</span>)=></span> &#123;
    components.forEach(<span class="hljs-function"><span class="hljs-params">component</span> =></span> &#123;
      app.component(component.name, component)
    &#125;)
  &#125;
<span class="hljs-keyword">export</span> &#123;
  TText,
  install
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; install &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里我们就完成组件入口文件的开发，其他的基本就是按照这个模式直接造轮子就好了，接下来我们就使用rollup来打包成umd和esmodule格式的文件。</p>
<h3 data-id="heading-13">添加tollup配置并打包</h3>
<p>根目录创建<code>build</code>文件夹，并依此创建</p>
<ol>
<li><code>rollup.config.js</code>：公共基础配置</li>
<li><code>rollup.esm.config.js</code>：打包esmodule文件配置</li>
<li><code>rollup.umd.config.js</code>打包umd文件配置</li>
</ol>
<p>因为都是配置就直接写了，可以看后面的备注
rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 处理vue文件插件</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-vue'</span>
<span class="hljs-comment">// 处理css文件插件</span>
<span class="hljs-keyword">import</span> css <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-css-only'</span>
<span class="hljs-comment">// 处理ts插件</span>
<span class="hljs-keyword">import</span> typescript <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-typescript2'</span>
<span class="hljs-comment">// 用于在节点单元模块中使用第三方模块</span>
<span class="hljs-keyword">import</span> &#123; nodeResolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span>
<span class="hljs-keyword">import</span> &#123; name &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../package.json'</span>
<span class="hljs-comment">// 输出打包后的文件名称type 1.esm 2.umd</span>
<span class="hljs-keyword">const</span> file = <span class="hljs-function"><span class="hljs-params">type</span> =></span> <span class="hljs-string">`dist/<span class="hljs-subst">$&#123;name&#125;</span>.<span class="hljs-subst">$&#123;type&#125;</span>.js`</span>
<span class="hljs-keyword">const</span> overrides = &#123;
  <span class="hljs-attr">compilerOptions</span>: &#123; <span class="hljs-attr">declaration</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-comment">// 生成.d.ts的文件</span>
  <span class="hljs-attr">exclude</span>: [<span class="hljs-string">"tests/**/*.ts"</span>, <span class="hljs-string">"tests/**/*.tsx"</span>] 
&#125;
<span class="hljs-keyword">export</span> &#123; name, file &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/index.ts'</span>,
  <span class="hljs-attr">output</span>: &#123;
    name,
    <span class="hljs-attr">file</span>: file(<span class="hljs-string">'esm'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    nodeResolve(),
    typescript(&#123; <span class="hljs-attr">tsconfigOverride</span>: overrides &#125;),
    vue(),
    css(&#123; <span class="hljs-attr">output</span>: <span class="hljs-string">'bundle.css'</span> &#125;) <span class="hljs-comment">// 可自行修改output文件名</span>
  ],
  <span class="hljs-attr">external</span>: [<span class="hljs-string">'vue'</span>, <span class="hljs-string">'lodash-es'</span>] <span class="hljs-comment">// 规定哪些是外部引用的模块</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rollup.esm.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> basicConfig, &#123;file, name&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./rollup.config'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    ...basicConfig,
  <span class="hljs-attr">output</span>: &#123;
    name,
    <span class="hljs-attr">file</span>: file(<span class="hljs-string">'esm'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rollup.umd.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> basicConfig, &#123; name, file &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./rollup.config'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  ...basicConfig,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'thComponents'</span>,
    <span class="hljs-attr">file</span>: file(<span class="hljs-string">'umd'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,
    <span class="hljs-attr">globals</span>: &#123; <span class="hljs-comment">// 设定全局变量的名称</span>
      <span class="hljs-string">'vue'</span>: <span class="hljs-string">'Vue'</span>,
      <span class="hljs-string">'lodash-es'</span>: <span class="hljs-string">'_'</span>
    &#125;,
    <span class="hljs-attr">exports</span>: <span class="hljs-string">'named'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写打包脚本</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"npm run clean && npm run build:esm && npm run build:umd"</span>, <span class="hljs-comment">// 整体打包指令</span>
    <span class="hljs-attr">"build:esm"</span>: <span class="hljs-string">"rollup --config ./build/rollup.esm.config.js"</span>, <span class="hljs-comment">// 打包esmodule</span>
    <span class="hljs-attr">"build:umd"</span>: <span class="hljs-string">"rollup --config ./build/rollup.umd.config.js"</span>, <span class="hljs-comment">// 打包umd格式</span>
    <span class="hljs-attr">"clean"</span>: <span class="hljs-string">"rimraf ./dist"</span> <span class="hljs-comment">// 清除dist</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>npm run build</code></p>
<p>查看结果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7f7c316c14e422891149c739284321a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>组件已经打包完成，接下来我们进行在本地使用 npm link进行测试</p>
<h3 data-id="heading-14">发布组件</h3>
<h4 data-id="heading-15">使用npm link进行组件库测试</h4>
<ol>
<li>配置package.json</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"th-bricks"</span>,
    <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
    <span class="hljs-string">"private"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"author"</span>: <span class="hljs-string">"linlei"</span>,
    <span class="hljs-string">"main"</span>: <span class="hljs-string">"dist/th-bricks.umd.js"</span>,
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"dist/th-bricks.esm.js"</span>,
    <span class="hljs-string">"types"</span>: <span class="hljs-string">"dist/index.d.ts"</span>
    ...
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>根目录下执行：<code>npm link</code></li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd02720af9ae4139a540d92f756476be~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3. 在项目中使用</p>
<ul>
<li>配置</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"dependencies"</span>: &#123;
    ...
    <span class="hljs-string">"th-bricks"</span>: <span class="hljs-string">"0.1.0"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>执行 <code>npm link th-bricks</code></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7176bf42f5214c23bd9e7a2d68d5d76a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>在项目的main.ts中引入，并在App.vue中使用</li>
</ol>
<p>main.ts</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> thBricks <span class="hljs-keyword">from</span> <span class="hljs-string">'th-bricks'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'th-bricks/dist/bundle.css'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
createApp(App)
.use(store)
.use(router)
.use(thBricks)
.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>App.vue</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
    <span class="hljs-comment"><!-- 使用 --></span>
    <span class="hljs-tag"><<span class="hljs-name">t-text</span> <span class="hljs-attr">text</span>=<span class="hljs-string">"hello"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"h2"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>查看结果</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31612dedaada43678dd8367b6d4d3bf8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到已经渲染出了组件
<strong>坑：如果出现可以打印thBricks无法使用的情况，可以重启电脑试试。</strong></p>
<h4 data-id="heading-16">发布npm</h4>
<ol>
<li>首先查看是否登录 <code>npm whami</code></li>
<li>如果已经登录就直接跳过，否则使用<code>npm login</code>进行登录，没有npm账号的就需要注册一个了</li>
<li>发布<code>npm publish</code></li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b13ef20367b4220b066b2877ed023cb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71e3efc3aa7940b8aee98f404141ad6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到已经发布成功了。</p>
<p>🤔我们每次执行<code>npm publish</code>的时候并不能保证我们一定执行了<code>npm run build</code>，那么有什么方法可以处理呢？
经过查看各种资料发现了可以这样处理：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cf7a56bbd3c488a94fb08d1af3387b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"npm run clean && npm run build:esm && npm run build:umd"</span>,
    <span class="hljs-string">"build:esm"</span>: <span class="hljs-string">"rollup --config ./build/rollup.esm.config.js"</span>,
    <span class="hljs-string">"build:umd"</span>: <span class="hljs-string">"rollup --config ./build/rollup.umd.config.js"</span>,
    <span class="hljs-string">"clean"</span>: <span class="hljs-string">"rimraf ./dist"</span>,
    <span class="hljs-string">"prepublishOnly"</span>: <span class="hljs-string">"npm run build"</span> <span class="hljs-comment">// npm publish的时候先执行npm run build</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">写在最后</h3>
<ul>
<li>基本的组件库的流程基本上已经完成了，但是离真正的一个完善组件库还有很远的距离，需要不断的丰富组件库，例如：tree，table，message，还有各种项目特定的组件等等</li>
<li><a href="https://github.com/linlei0/th-component.git/" target="_blank" rel="nofollow noopener noreferrer">组件库代码</a></li>
</ul></div>  
</div>
            