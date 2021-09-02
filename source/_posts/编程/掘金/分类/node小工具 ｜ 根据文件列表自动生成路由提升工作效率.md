
---
title: 'node小工具 ｜ 根据文件列表自动生成路由提升工作效率'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccb1ad725524542b41a9ae0de00be60~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 17:43:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccb1ad725524542b41a9ae0de00be60~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>老话说得好光说不练假把式，要学会学以致用，今天搞了个node小工具方便我们在开发中提升效率</p>
<h2 data-id="heading-0">问题</h2>
<p>我们来分析一下现在存在的问题（小问题🤔）目前在我们的开发工作中如果新建一个可跳转显示的路由页面一般需要下面几步</p>
<blockquote>
<p>1、在当前文件夹下面新建页面或者是<code>.vue</code>或者是<code>.jsx</code><br>2、在路由配置列表中新建对应的路径配置信息<br>3、如果需要像<code>router-link</code>这种跳转方式还需要手动创建一个</p>
</blockquote>
<p>如果是一个新的项目可想而知我们需要重复<code>N</code>次以上步骤，浪费时间是肯定的那么今天我们的目的就是解决以上存在的问题，能让我们有更多的时间去写<code>bug</code>，最后可以做到只要在当前文件夹下建立文件之后，路由配置和<code>router-link</code>会自动生成</p>
<h2 data-id="heading-1">原理</h2>
<p>对于以上功能我们先说原理之后在实现，我觉得这样可能更方便后面的理解，大概有几个步骤</p>
<blockquote>
<p>1、首先监听当前文件夹下文件的变化，如果有变化就执行方法<br>2、监测到变化执行<code>refresh</code>刷新方法<br>3、方法内部会获取文件夹下所有文件名字最后用于生产路由配置<br>4、创建一个<code>compile</code>方法用于读取模版引擎和渲染路由配置<br>5、最后输出<code>log</code></p>
</blockquote>
<h2 data-id="heading-2">准备</h2>
<p>我们需要做几个准备工作<br>
1、创建环境本次选用的是<code>vue</code>的环境使用，<code>vue-cli</code>工具生成<br>
2、创建模版引擎页面，在根目录创建<code>template</code>文件夹在内部放入<code>router.js.hbs</code>和<code>App.vue.hbs</code>，这两个模版引擎使用的是<code>handlebars</code>（如果不了解的同学可以先去看一下）</p>
<p><strong>router.js.hbs</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

Vue.use(Router)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  <span class="hljs-attr">routes</span>: [
    &#123;&#123;#each list&#125;&#125;
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/&#123;&#123;path&#125;&#125;'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'&#123;&#123;path&#125;&#125;'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/&#123;&#123;file&#125;&#125;'</span>)
    &#125;,
    &#123;&#123;/each&#125;&#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>App.vue.hbs</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      &#123;&#123;#each list&#125;&#125;
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/&#123;&#123;path&#125;&#125;"</span>></span>&#123;&#123;path&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
      &#123;&#123;/each&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Avenir'</span>, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok到这里准备工作就已经完成了可以开始操作了，我们先看一下页面的样子，之后自动生成的路由会在后面排队显示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccb1ad725524542b41a9ae0de00be60~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">开始</h2>
<blockquote>
<p>1、在根目录下创建<code>components</code>文件夹之后在下面创建两个页面<code>home.vue</code>和<code>login.vue</code><br>2、更改<code>App.vue</code>和<code>router/index.js</code>让路由先跑起来</p>
</blockquote>
<p><strong>home.vue</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"home"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>home<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<!-- Add <span class="hljs-string">"scoped"</span> attribute to limit CSS to <span class="hljs-built_in">this</span> component only -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>login.vue</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"login"</span>></span>
      login
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>App.vue</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/login"</span>></span>login<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Avenir'</span>, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>router/index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

Vue.use(Router)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home.vue'</span>)
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'login'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/login.vue'</span>)
    &#125;,
  ]
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">在package.json增加启动命令refresh启动命令</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --inline --progress --config build/webpack.dev.conf.js"</span>,
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"npm run dev"</span>,
    <span class="hljs-string">"refresh"</span>: <span class="hljs-string">"node ./lib/server.js"</span>, 
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"node build/build.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">在根目录创建一个lib文件夹在下面创建server.js用来监听components下面的变化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn add -D watch</span>

<span class="hljs-keyword">const</span> watch = <span class="hljs-built_in">require</span>(<span class="hljs-string">'watch'</span>)

<span class="hljs-keyword">let</span> isRefresh = <span class="hljs-literal">false</span>
watch.watchTree(<span class="hljs-string">'./src/components'</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">//监听到文件变化</span>
    <span class="hljs-keyword">if</span> (!isRefresh) &#123;
        isRefresh = <span class="hljs-literal">true</span>
        <span class="hljs-comment">//执行刷新路由文件</span>
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">require</span>(<span class="hljs-string">'./refresh'</span>)()
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            isRefresh = <span class="hljs-literal">false</span>
        &#125;, <span class="hljs-number">500</span>)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">创建refresh.js用来刷新路由并且展示日志</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn add -D handlebars figlet chalk clear</span>
 
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> handelBarse = <span class="hljs-built_in">require</span>(<span class="hljs-string">'handlebars'</span>)
<span class="hljs-keyword">const</span> &#123; promisify &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'util'</span>)
<span class="hljs-keyword">const</span> figlet = promisify(<span class="hljs-built_in">require</span>(<span class="hljs-string">'figlet'</span>)) <span class="hljs-comment">//获取设置终端logo方式</span>
<span class="hljs-keyword">const</span> clear = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clear'</span>)
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>)
<span class="hljs-keyword">const</span> logGreen = <span class="hljs-function"><span class="hljs-params">content</span> =></span> <span class="hljs-built_in">console</span>.log(chalk.green(content))
<span class="hljs-keyword">const</span> logRed = <span class="hljs-function"><span class="hljs-params">content</span> =></span> <span class="hljs-built_in">console</span>.log(chalk.red(content))

<span class="hljs-keyword">let</span> prevList = [] <span class="hljs-comment">//存储上一次的更新记录</span>
   
<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">//读取文件目录</span>
    <span class="hljs-keyword">const</span> list = fs.readdirSync(<span class="hljs-string">'./src/components'</span>).map(<span class="hljs-function"><span class="hljs-params">file</span> =></span> (&#123;
        <span class="hljs-attr">path</span>: file.replace(<span class="hljs-string">'.vue'</span>, <span class="hljs-string">''</span>).toLocaleLowerCase(),
        file
    &#125;))
    
    <span class="hljs-comment">//创建编译更新函数</span>
    <span class="hljs-keyword">const</span> compile = <span class="hljs-keyword">async</span> (meta, filepath, templatePath) => &#123;
        <span class="hljs-keyword">if</span> (fs.existsSync(templatePath)) &#123;
            <span class="hljs-keyword">const</span> content = fs.readFileSync(templatePath).toString()
            <span class="hljs-comment">//执行模版引擎传入参数</span>
            <span class="hljs-keyword">const</span> result = handelBarse.compile(content)(meta)
            <span class="hljs-comment">//写入文件</span>
            fs.writeFileSync(filepath, result)
        &#125;
    &#125;
    
    <span class="hljs-comment">//覆盖router/index.js</span>
    compile(&#123; list &#125;, <span class="hljs-string">'./src/router/index.js'</span>, <span class="hljs-string">'./template/router.js.hbs'</span>)
    <span class="hljs-comment">//覆盖App.vue</span>
    compile(&#123; list &#125;, <span class="hljs-string">'./src/App.vue'</span>, <span class="hljs-string">'./template/App.vue.hbs'</span>)
    clear()
    <span class="hljs-comment">//输出更新日志</span>
    inputLog(list, prevList)
    prevList = list
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>inputLog</strong></p>
<pre><code class="hljs language-hs copyable" lang="hs"><span class="hljs-title">const</span> inputLog = async (currList, prevList) => &#123;

    <span class="hljs-keyword">if</span> (prevList.length !== <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">let</span> file = ''
        <span class="hljs-keyword">let</span> prevListPath = prevList.map(item => item.path)
        <span class="hljs-keyword">let</span> currListPath = currList.map(item => item.path)

        <span class="hljs-keyword">if</span> (prevListPath.length > currList.length) &#123;
            file = prevList.find(item => !currListPath.includes(item.path))?.file || ''
            <span class="hljs-keyword">if</span> (file) logRed(`删除$&#123;file&#125;🚀🚀🚀`)
        &#125; <span class="hljs-keyword">else</span> &#123;
            file = currList.find(item => !prevListPath.includes(item.path))?.file || ''
            <span class="hljs-keyword">if</span> (file) logGreen(`新增$&#123;file&#125;🚀🚀🚀`)
            <span class="hljs-keyword">else</span> logGreen(`更新完成🚀🚀🚀`)
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        const tips = await figlet(`start success`)
        logGreen(tips)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">试验</h2>
<blockquote>
<p>执行<code>npm run server</code>启动监听</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/820e0c1a541f45b0ae77d1ad47deb54b~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>之后在components下面创建一个test3.vue文件</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5391d2a7063e4d748e76a5360ad6f402~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>接下来在删除test3.vue文件</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7029c83a04ba47efb151d2215a460559~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以在控制台中看出都是能监听到的，这样的话我们在创建新页面的时候就只需要在当前目录下创建文件即可，不需要在考虑其他配置路由路径的情况</p>
<h2 data-id="heading-8">总结</h2>
<p>写作的话对自己有个加深的印象，而且以后复盘起来也比较方便同时又是学习一遍的过程，如果大家觉得有用的话留个赞呗☕️</p></div>  
</div>
            