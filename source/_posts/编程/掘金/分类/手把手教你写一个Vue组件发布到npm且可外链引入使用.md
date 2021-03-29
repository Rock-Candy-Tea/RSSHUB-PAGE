
---
title: '手把手教你写一个Vue组件发布到npm且可外链引入使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2b20b215853416f9e5823a577973610~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 19:04:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2b20b215853416f9e5823a577973610~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">前言</h2>
<p>我们为什么要写个组件上传到<code>npm</code>镜像上呢，我们肯定遇到过这样一个场景，项目中有很多地方与某个功能相似，你想到的肯定是把该功能封装成<code>Component</code>组件，后续方便我们调用。但是过了一段时间，你的<code>Leader</code>让你去开发另一个项目，结果你在哪个项目中又看见了类似的功能，你这时会怎么做?   你也可以使用<code>Ctrl + c + v</code>大法，拿过来上一个项目封装好的代码，但是如果需求有些变动，你得维护两套项目的代码，甚至以后更多的项目....，这时你就可以封装一个功能上传到你们公司内网的<code>npm</code>上(或者自己的账号上)，这样每次遇到类似的功能直接<code>npm install</code> 安装<code>import</code>导入进来使用就可以，需求有变动时完全可以改动一处代码。</p>
<h2 data-id="heading-1">配置环境</h2>
<p>笔者这里使用的是<code>Webpack</code>配置(有点菜，不要介意)，也可以安装一个<code>Vue-cli</code>简单版的，它那里面有暴露<code>Webpack</code>的配置(也得修改自行配置)，我们来配置一下打包组件环境，一般开发组件库都是使用的<code>umd</code>格式，这种格式支持<code>Es Module</code>、<code>CommonJs</code>、<code>AMD</code>三种引入方式使用，主要就是<code>Webpack</code>里的<code>library</code>和<code>libraryTarget</code>，如果不明白的看这里<a href="https://blog.csdn.net/frank_yll/article/details/78992778" target="_blank" rel="nofollow noopener noreferrer">详解webpack的out.libraryTarget属性</a></p>
<blockquote>
<p>我这里的Webpack版本为4,  最好跟着本章里的插件版本号进行安装，避免出现版本兼容问题</p>
</blockquote>
<h3 data-id="heading-2">项目结构</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">|- /node_modules
|- /src
   |- Tag.vue
   |- main.js
|- index.html
|- webpack.config.js
|- package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">初始化Package.json</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">安装Webpack && Loader && Plugin</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i webpack webpack-cli -D
cnpm i css-loader style-loader -D
cnpm i file-loader -D
cnpm i vue-loader@<span class="hljs-number">15.7</span><span class="hljs-number">.0</span> vue vue-template-compiler -D
cnpm i html-webpack-plugin@<span class="hljs-number">3.2</span><span class="hljs-number">.0</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css-loader style-loader 配置<code>.css</code>文件及样式使用</li>
<li>file-loader 配置特殊字体和图片使用</li>
<li>vue-loader 处理<code>.vue</code>文件后缀</li>
<li>vue 使用Vue语法</li>
<li>vue-template-compiler 处理<code>.vue</code>文件里的<code>template</code>模板语法</li>
</ul>
<h3 data-id="heading-5">webpack.config.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/main.js"</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">"index.js"</span>
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>]  
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(ttf|eot|woff|svg|woff2)/</span>,
                use: <span class="hljs-string">"file-loader"</span>
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
                use: <span class="hljs-string">"vue-loader"</span>
            &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> VueLoaderPlugin(),
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">index.html</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上我们基本环境就搭建完啦，可以在终端使用<code>npx webpack</code>运行看看哦。</p>
<h2 data-id="heading-7">封装组件</h2>
<p>我这里只做一个示例哈，代码就不写那么复杂，大家知道怎么打包使用就行，具体封装成啥样看你们公司需求啦~。笔者这里使用<code>Element Ui</code>组件来做一个示例，相信大部分小伙伴公司也在使用<code>Element Ui</code>。假如我们项目中有以下类似的功能就可以单独封装起来。</p>
<p><img alt="示例" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2b20b215853416f9e5823a577973610~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">main.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Tag &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/tag.css'</span>;
Vue.component(Tag.name, Tag)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Tag
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Tag.vue</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Tag"</span>></span>
    &#123;&#123; msg &#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">el-tag</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success"</span>></span>标签二<span class="hljs-tag"></<span class="hljs-name">el-tag</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'Tag'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">msg</span>: <span class="hljs-string">"hello 蛙人"</span>,
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;&#125;,
  <span class="hljs-attr">watch</span>: &#123;&#125;,
  <span class="hljs-attr">methods</span>: &#123;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Webpack.config.js</h3>
<p>将<code>webpack.config.js</code>里的<code>output</code>修改为如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">output: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">"index.js"</span>,
    <span class="hljs-attr">library</span>: <span class="hljs-string">"Modal"</span>,
    <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">"umd"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完之后就可以使用<code>npx webpack</code>打包，可以看到有一个<code>dist</code>目录，该目录下存在一个<code>index.js</code>,  这个文件就是我们封装的<code>Tag.vue</code>文件, 你可以将它引入到你的项目中，进行调用，该文件支持<code>Es Module</code>、<code>CommonJs</code>、<code>AMD</code>三种方式引入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Tag &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/tag.css'</span>;
Vue.component(Tag.name, Tag)
<span class="hljs-keyword">import</span> CustomTag <span class="hljs-keyword">from</span> <span class="hljs-string">"./index"</span> <span class="hljs-comment">// 打包完的，直接引入进来</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(CustomTag)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">Npm发布</h2>
<p>如果没有<code>npm</code>账号呢，先去官网注册一个<code>npm</code>账号<a href="https://www.npmjs.com/signup" target="_blank" rel="nofollow noopener noreferrer">这里</a></p>
<h3 data-id="heading-12">新建一个发布包项目文件夹</h3>
<p>在终端执行<code>npm init -y</code> ，进行初始<code>package.json</code>文件，主要信息就是name和main字段，前者是这个包的名称(也就是npm instal xxx)，后者则是我们打包好的文件<code>Tag</code>文件，默认<code>main</code>就去找这个入口文件。</p>
<blockquote>
<p>注意：包名称不能包含大写，包名称不能包含大写，包名称不能包含大写，重要的事情说三遍</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"custom-tag-waren"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"这是xxxx"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"WaRen"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果淘宝镜像之前被更改，先改回来执行以下命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm config set registry http:<span class="hljs-comment">//registry.npmjs.org</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注册完之后，执行<code>npm login</code>, 依次填写你的<code>用户名</code>、<code>密码</code>、<code>邮箱</code></p>
<p>执行<code>npm publish</code>发布，然后等待进度条完成即可。</p>
<h3 data-id="heading-13">整理一些常见的发布错误</h3>
<p>这是因为镜像设置成淘宝镜像了，设置回来即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">no_perms Private mode enable, only admin can publish <span class="hljs-built_in">this</span> <span class="hljs-built_in">module</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般是没有登录，重新登录一下 <code>npm login</code> 即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm publish failed put <span class="hljs-number">500</span> unexpected status code <span class="hljs-number">401</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>包名被占用，改个包名即可，最好在官网查一下是否有包名被占用，之后再重命名</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm ERR! you <span class="hljs-keyword">do</span> not have permission to publish “your <span class="hljs-built_in">module</span> name”. Are you logged <span class="hljs-keyword">in</span> <span class="hljs-keyword">as</span> the correct user?
<span class="copy-code-btn">复制代码</span></code></pre>
<p>邮箱未验证，去官网验证一下邮箱</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">you must verify your email before publishing a <span class="hljs-keyword">new</span> package
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">npm安装使用</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">cnpm i custom-tag-waren -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">main.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Tag &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/tag.css'</span>;
<span class="hljs-keyword">import</span> customTagWaren <span class="hljs-keyword">from</span> <span class="hljs-string">"custom-tag-waren"</span>  <span class="hljs-comment">// 下载完引入进来</span>
Vue.component(Tag.name, Tag)
<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(customTagWaren)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止就完成了一个组件的打包上传下载，这样我们在每个项目需要的时候直接<code>npm install</code>安装就行，当需求改动的时候只改一个文件然后再次发布就行。是不是很方便啦。</p>
<h2 data-id="heading-16">外链引入</h2>
<p>我们也不上传<code>npm</code>上，直接使用外链的形式使用，下面我们来看看</p>
<h3 data-id="heading-17">import引入</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Tag"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">TagEl</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> TagEl <span class="hljs-keyword">from</span> <span class="hljs-string">"./index"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-string">'Tag'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
       
    &#125;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
      TagEl
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面<code>example</code>中，我们看到直接引入了<code>index.js</code>文件并进行注册组件，直接就可以使用啦。</p>
<h3 data-id="heading-18">script引入</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Tag</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/vue/2.6.9/vue.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-attr">Tag</span>: Tag.default
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面<code>example</code>中，直接使用<code>script</code>标签引入进来，也是注册完使用就可以。那么我们怎么知道他名字是Tag，这个你在封装组件的使用，必须指定Name名称。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"Tag"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">感谢</h2>
<p>谢谢你读完本篇文章，希望对你能有所帮助，如有问题欢迎各位指正。</p>
<p>我是蛙人(✿◡‿◡)，如果觉得写得可以的话，请点个赞吧❤。</p>
<p>感兴趣的小伙伴可以加入 <a href="https://qinzhiying.github.io/" target="_blank" rel="nofollow noopener noreferrer">[ 前端娱乐圈交流群 ]</a> 欢迎大家一起来交流讨论</p>
<p>写作不易，<strong>「点赞」+「在看」+「转发」</strong> 谢谢支持❤</p>
<h2 data-id="heading-20">往期好文</h2>
<p><a href="https://juejin.cn/post/6942322281913778206" target="_blank">《分享12个Webpack中常用的Loader》</a></p>
<p><a href="https://juejin.cn/post/6938581764432461854" target="_blank">《聊聊什么是CommonJs和Es Module及它们的区别》</a></p>
<p><a href="https://juejin.cn/post/6937855370220011551" target="_blank">《带你轻松理解数据结构之Map》</a></p>
<p><a href="https://juejin.cn/post/6937092511508725774" target="_blank">《这些工作中用到的JavaScript小技巧你都知道吗？》</a></p>
<p><a href="https://juejin.cn/post/6934487656873082887" target="_blank">《【建议收藏】分享一些工作中常用的Git命令及特殊问题场景怎么解决》</a></p>
<p><a href="https://juejin.cn/post/6930428551091109896" target="_blank">《你真的了解ES6中的函数特性么？》</a></p>
<h2 data-id="heading-21">参考</h2>
<p><a href="https://blog.csdn.net/weixin_43606158/article/details/1068086" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/weixin_4360…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            