
---
title: 'npm发布公共组件包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4226'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 18:05:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=4226'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1. 修改webpack配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在module.export中加入如下代码</span>
<span class="hljs-comment">// 根据不同的执行环境配置不同的入口</span>
<span class="hljs-attr">entry</span>: NODE_ENV === <span class="hljs-string">'development'</span> ? <span class="hljs-string">'./src/main.js'</span> : <span class="hljs-string">'./src/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./lib'</span>),
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/lib/'</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.js'</span>,
    <span class="hljs-attr">library</span>: <span class="hljs-string">'mu-design'</span>, <span class="hljs-comment">// 指定require时的模块名</span>
    <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>, <span class="hljs-comment">// 指定输出格式</span>
    <span class="hljs-attr">umdNamedDefine</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 会对UMD的构建过程中的AMD模块命名，否则使用匿名的define。</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>library</strong>：指定的就是你使用require时的模块名</p>
<p><strong>libraryTarget</strong>：为了支持多种使用场景，我们需要选择合适的打包格式。常见的打包格式有 CMD、AMD、UMD，CMD只能在 Node 环境执行，AMD 只能在浏览器端执行，UMD 同时支持两种执行环境。显而易见，我们应该选择 UMD 格式。</p>
<p><strong>有时我们想开发一个库，如lodash，underscore这些工具库，这些库既可以用commonjs和amd方式使用也可以用script方式引入。</strong></p>
<p><strong>这时候我们需要借助library和libraryTarget，我们只需要用ES6来编写代码，编译成通用的UMD就交给webpack了</strong></p>
<p><strong>umdNamedDefine</strong>：会对 UMD 的构建过程中的 AMD 模块进行命名。否则就使用匿名的 define</p>
<h4 data-id="heading-1">2. 修改package.json文件 和 index.html，添加readme.md</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 发布开源 因此需要将这个字段改为 false</span>
<span class="hljs-string">"private"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-comment">// 这个指 import demo 的时候它会去检索的路径</span>
<span class="hljs-string">"main"</span>: <span class="hljs-string">"./lib/index.js"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.html中引用地址也要做相应改变</span>
<script src=<span class="hljs-string">"/lib/index.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3. npm发布包</h4>
<ol>
<li>发布新包</li>
</ol>
<p>（1）在npm官网注册账号，地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F%25EF%25BC%258C%25E6%25B3%25A8%25E5%2586%258C%25E5%25A5%25BD%25E4%25B9%258B%25E5%2590%258E%25EF%25BC%259A" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/%EF%BC%8C%E6%B3%A8%E5%86%8C%E5%A5%BD%E4%B9%8B%E5%90%8E%EF%BC%9A" ref="nofollow noopener noreferrer">www.npmjs.com/，注册好之后：</a></p>
<p>　　 注意邮箱要验证，会发送验证链接到你的注册邮箱，没有验证的话是不能发布代码的</p>
<p>　　 看一下package.json 中 author 尽量与 npm 账户一致</p>
<p>（2）切换到需要发包的项目根目录下，登录npm账号，输入用户名、密码、邮箱</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 进入项目根目录，初始化npm包</span>
npm init
<span class="hljs-comment">// 登录</span>
npmnpm login
<span class="hljs-comment">// 执行发布</span>
npm publish
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>更新包</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改包的版本，命令会在原来的版本上自动加1，</span>
<span class="hljs-comment">// 实际上是将package.json文件中的version值修改了</span>
npm version patch 
<span class="hljs-comment">// 重新发布包</span>
npm publish
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>删除包</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 删除指定的版本</span>
npm unpublish 包名@版本号
<span class="hljs-comment">// 删除整个包，会有警告提示</span>
npm unpublish 包名 --force
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4.使用</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 安装</span>
npm install your-npm-page --save

<span class="hljs-comment">//main.js中引入</span>
<span class="hljs-keyword">import</span> demo <span class="hljs-keyword">from</span> <span class="hljs-string">'your-npm-page'</span>
Vue.use(demo)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5.调试</h4>
<p>通过软链接的方式实现，编辑了本地npm代码，在项目中也能使用编码后的代码</p>
<ol>
<li>
<p>确保package.json已经正确配置好</p>
</li>
<li>
<p>在本地npm模块根目录下执行<code>npm link</code>，把本地模块注册到全局</p>
</li>
<li>
<p>在需要引用组件包的项目根目录下执行<code>npm link npm-name</code>,把第2步注册到全局的本地npm模块链接到项目的node_modules下，其中npm-name是指第一步中package.json中配置的模块名</p>
</li>
<li>
<p>正常使用npm包</p>
</li>
</ol>
<h4 data-id="heading-5">6.常见错误</h4>
<ol>
<li>当前不是原始镜像，可能用的是其他镜像，如淘宝镜像</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">no_perms Private mode enable, only admin can publish <span class="hljs-built_in">this</span> <span class="hljs-built_in">module</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改：将npm切回原始镜像</p>
<pre><code class="hljs language-js copyable" lang="js">npm config set registry http:<span class="hljs-comment">//registry.npmjs.org</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用了nrm工具，可以使用命令<code>nrm use npm</code>切换</p>
<ol start="2">
<li>未登录</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm publish failed put <span class="hljs-number">500</span> unexpected status code <span class="hljs-number">401</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改：重新 <code>npm login</code></p>
<ol start="3">
<li>包名被占用</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm ERR! you <span class="hljs-keyword">do</span> not have permission to publish “your <span class="hljs-built_in">module</span> name”. Are you logged <span class="hljs-keyword">in</span> <span class="hljs-keyword">as</span> the correct user?
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改包名</p>
<ol start="4">
<li>邮箱未验证</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">you must verify your email before publishing a <span class="hljs-keyword">new</span> package
<span class="copy-code-btn">复制代码</span></code></pre>
<p>去官网验证一下邮箱
5. 查看npm是否安装成功</p>
<pre><code class="hljs language-js copyable" lang="js">npm who am i
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>包名的限制：不能有大写字母、空格、下划线</li>
<li>由于需要使用Install注册组件，所以一定要注意组件中的name值</li>
</ol></div>  
</div>
            