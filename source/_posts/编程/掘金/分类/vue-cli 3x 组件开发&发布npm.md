
---
title: 'vue-cli 3.x 组件开发&发布npm'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b567599c2fa4cc4bec21b96e7bca8f8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 21:59:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b567599c2fa4cc4bec21b96e7bca8f8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、脚手架创建vue项目   vue create project-name
当前的项目目录是这样的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b567599c2fa4cc4bec21b96e7bca8f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先需要创建一个 <strong>packages</strong> 目录，用来存放组件</p>
<p>然后将 src 目录改为 <strong>examples</strong> 用作示例</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78f263afad9e4e8ea4228c40d645c00e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>二、修改配置</strong></p>
<p>启动项目的时候，默认入口文件是 src/main.js</p>
<p>将 src 目录改为 examples 之后，就需要重新配置入口文件</p>
<p>在根目录下创建一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fconfig%2F%23vue-config-js" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/config/#vue-config-js" ref="nofollow noopener noreferrer">vue.config.js</a> 文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.config.js</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 将 examples 目录添加为新的页面</span>
  <span class="hljs-attr">pages</span>: &#123;
    <span class="hljs-attr">index</span>: &#123;
      <span class="hljs-comment">// page 的入口</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'examples/main.js'</span>,
      <span class="hljs-comment">// 模板来源</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span>,
      <span class="hljs-comment">// 输出文件名</span>
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成这一步之后就可以正常启动项目了</p>
<p>vue-cli 3.x  提供了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fbuild-targets.html%23%25E5%25BA%2593" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/build-targets.html#%E5%BA%93" ref="nofollow noopener noreferrer">构建库</a>的命令，所以这里<strong>不需要再为 packages 目录配置 webpack</strong></p>
<p><strong>三、开发组件</strong></p>
<p>之前已经创建了一个 packages 目录，用来存放组件</p>
<p>该目录下存放每个组件单独的开发目录，和一个 index.js 整合所有组件，并对外导出</p>
<p>每个组件都应该归类于单独的目录下，包含其组件源码目录 src，和 index.js 便于外部引用</p>
<p>这里以 textarea 组件为例，完整的 packages 目录结构如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25ad57a3846844838ffab6d4245afe68~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>textarea/src/main.vue</strong> 是组件的开发文件，具体代码这里就不展示了</p>
<p><strong>需要注意的是，组件必须声明 name，这个 name 就是组件的标签</strong></p>
<p><strong>textarea/index.js</strong> 用于导出单个组件，如果要做按需引入，也需要在这里配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// packages/textarea/index.js</span>

<span class="hljs-comment">// 导入组件，组件必须声明 name</span>
<span class="hljs-keyword">import</span> Textarea <span class="hljs-keyword">from</span> <span class="hljs-string">'./main.vue'</span>

<span class="hljs-comment">// 为组件添加 install 方法，用于按需引入</span>
Textarea.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
    Vue.component(Textarea.name, Textarea)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Textarea
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>四、整合并导出组件</strong></p>
<p>编辑 <strong>packages/index.js</strong> 文件，实现组件的全局注册</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// packages / index.js</span>

<span class="hljs-comment">// 导入单个组件</span>
<span class="hljs-keyword">import</span> Textarea <span class="hljs-keyword">from</span> <span class="hljs-string">'./textarea/index'</span>

<span class="hljs-comment">// 以数组的结构保存组件，便于遍历</span>
<span class="hljs-keyword">const</span> components = [
    Textarea
]

<span class="hljs-comment">// 定义 install 方法</span>
<span class="hljs-keyword">const</span> install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">Vue</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (install.installed) <span class="hljs-keyword">return</span>
    install.installed = <span class="hljs-literal">true</span>
    <span class="hljs-comment">// 遍历并注册全局组件</span>
    components.map(<span class="hljs-function"><span class="hljs-params">component</span> =></span> &#123;
        Vue.component(component.name, component)
    &#125;)
&#125;

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
    install(<span class="hljs-built_in">window</span>.Vue)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-comment">// 导出的对象必须具备一个 install 方法</span>
    install,
    <span class="hljs-comment">// 组件列表</span>
    ...components
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里组件就已经开发完毕</p>
<p>可以在 <strong>examples/main.js</strong> 中引入该组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> TagTextarea <span class="hljs-keyword">from</span> <span class="hljs-string">'../packages/index'</span>
Vue.use(TagTextarea)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就能直接使用刚才开发的 textarea 组件</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b23be0828247fc9802d446089f6143~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>组件的标签就是组件内定义的的 name</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97d7826aef8a4f87a616bad72125f18d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候可以 npm run serve 启动项目，测试一下组件是否有 bug</p>
<p>// 启动前需要确保已经在 vue.config.js 中添加了新入口 examples/main.js</p>
<p><strong>五、打包组件</strong></p>
<p>vue-cli 3.x 提供了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fbuild-targets.html%23%25E5%25BA%2593" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/build-targets.html#%E5%BA%93" ref="nofollow noopener noreferrer">库文件打包命令</a></p>
<p>主要需要四个参数：</p>
<p>1. <strong>target</strong>: 默认为构建应用，改为 <strong>lib</strong> 即可启用构建库模式</p>
<p>2. <strong>name</strong>: 输出文件名</p>
<ol start="3">
<li><strong>dest</strong>: 输出目录，默认为 dist，这里我们改为 <strong>lib</strong></li>
</ol>
<p>4. <strong>entry</strong>: 入口文件路径，默认为 src/App.vue，这里改为 <strong>packages/index.js</strong></p>
<p>基于此，在 package.json 里的 scripts 添加一个 <strong>lib</strong> 命令</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// pageage.json</span>

&#123;
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"lib"</span>: <span class="hljs-string">"vue-cli-service build --target lib --name tag-textarea --dest lib packages/index.js"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行 <strong>npm run lib</strong> 命令，编译组件</p>
<p><strong>六、准备发布</strong></p>
<p>首先需要在 <strong>package.json</strong> 添加组件信息</p>
<p><strong>name:</strong> 包名，该名不能和已有的名称冲突；</p>
<p><strong>version:</strong> 版本号，不能和历史版本号相同；</p>
<p><strong>description:</strong> 简介；</p>
<p><strong>main:</strong> 入口文件，应指向编译后的包文件；</p>
<p><strong>keyword：</strong> 关键字，以空格分割；</p>
<p><strong>author：</strong> 作者；</p>
<p><strong>private：</strong> 是否私有，需要修改为 false 才能发布到 npm；</p>
<p><strong>license：</strong> 开源协议。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e60ac78db6064fd6be50ed248b92799d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后创建  <strong>.npmignore</strong> 文件，设置忽略文件</p>
<p>该文件的语法和 .gitignore 的语法一样，设置发布到 npm 时忽略哪些目录或文件</p>
<pre><code class="hljs language-js copyable" lang="js">.DS_Store
node_modules/
examples/
packages/
public/
vue.config.js
babel.config.js
*.map
*.html

# local env files
.env.local
.env.*.local

# Log files
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Editor directories and files
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw*
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>七、发布到 npm</strong></p>
<p>如果以前改过 npm 的镜像地址，比如使用了淘宝镜像，就先改回来</p>
<pre><code class="copyable">npm config set registry http://registry.npmjs.org 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有 npm 账户，可以通过 <strong>npm adduser</strong> 命令创建一个账户，或者到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com" ref="nofollow noopener noreferrer">npm 官网</a>注册</p>
<p>如果在官网注册的账户，或者以前就有账户，就使用 <strong>npm login</strong> 命令登录</p>
<p>具体流程可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.cn%2Fgetting-started%2Fpublishing-npm-packages%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.cn/getting-started/publishing-npm-packages/" ref="nofollow noopener noreferrer">官方文档</a></p>
<p><strong>在发布之前，一定要确保组件已经编译完毕，而且 package.json 中的入口文件（main）的路径正确</strong></p>
<p>一切就绪，发布组件：</p>
<pre><code class="copyable">npm publish
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            