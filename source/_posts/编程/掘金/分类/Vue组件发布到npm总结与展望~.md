
---
title: 'Vue组件发布到npm总结与展望~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3300'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 06:43:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=3300'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>昨天发布了自己第一个认认真真写的 Vue 组件，有兴趣的可以看下：<a href="https://juejin.cn/post/6969217825734918152" target="_blank">来动手打造一款自己的大图预览组件~</a>，昨天已经把组件的基本功能(包括放大,缩写,旋转,还原)完成了，今天又加上了下载,虽然下载好像没什么用，右键另存为就可以了，但下载写着写着发现还是不少知识点的，比如要对不同的src地址(httpURL,base64,本地地址)来进行下载文件，一会贴上代码,大家可以看一下~ 然后就是对项目进行一点配置，上传到npm，供其他项目或者有需求的朋友使用(不管你们用不用,反正我自己感觉我的组件挺好用,哈哈哈~)。</p>
</blockquote>
<h2 data-id="heading-0">1. 下载功能实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// utils/index.js</span>

<span class="hljs-comment">// blob下载</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">downFile</span>(<span class="hljs-params">url, fileName = <span class="hljs-string">"download"</span></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">let</span> blob = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">// 本地图片 网络图片 base64图片处理</span>
    <span class="hljs-keyword">if</span> (url.startsWith(<span class="hljs-string">"http"</span>)) &#123;
      blob = <span class="hljs-keyword">await</span> getBlob(url);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (url.startsWith(<span class="hljs-string">"data:image"</span>)) &#123;
      <span class="hljs-keyword">let</span> mime = getBase64Type(url);
      blob = mime ? dataURLtoBlob(url, mime) : dataURLtoBlob(url);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (url.startsWith(<span class="hljs-string">"/"</span>)) &#123;
      blob = <span class="hljs-keyword">await</span> getBlob(<span class="hljs-built_in">window</span>.origin + url);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span>;
    &#125;

    <span class="hljs-keyword">let</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
    a.download = fileName;
    a.href = <span class="hljs-built_in">window</span>.URL.createObjectURL(blob);
    a.click();
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;
&#125;
<span class="hljs-comment">// 将base64转为blob</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dataURLtoBlob</span>(<span class="hljs-params">base64, mimeType = <span class="hljs-string">"image/png"</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> bytes = <span class="hljs-built_in">window</span>.atob(base64.split(<span class="hljs-string">","</span>)[<span class="hljs-number">1</span>]);
  <span class="hljs-keyword">let</span> ab = <span class="hljs-keyword">new</span> <span class="hljs-built_in">ArrayBuffer</span>(bytes.length);
  <span class="hljs-keyword">let</span> ia = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(ab);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < bytes.length; i++) &#123;
    ia[i] = bytes.charCodeAt(i);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Blob([ab], &#123; <span class="hljs-attr">type</span>: mimeType &#125;);
&#125;
<span class="hljs-comment">// 将网络url转为blob</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getBlob</span>(<span class="hljs-params">url</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
    xhr.open(<span class="hljs-string">"GET"</span>, url, <span class="hljs-literal">true</span>);
    xhr.responseType = <span class="hljs-string">"blob"</span>;
    xhr.onload = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (xhr.status == <span class="hljs-number">200</span>) &#123;
        resolve(xhr.response);
      &#125; <span class="hljs-keyword">else</span> &#123;
        reject();
      &#125;
    &#125;;
    xhr.send();
  &#125;);
&#125;
<span class="hljs-comment">// 获取base64文件类型</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getBase64Type</span>(<span class="hljs-params">base64</span>) </span>&#123;
  <span class="hljs-keyword">let</span> index0 = base64.indexOf(<span class="hljs-string">":"</span>);
  <span class="hljs-keyword">let</span> index1 = base64.indexOf(<span class="hljs-string">";"</span>);
  <span class="hljs-keyword">let</span> mime = <span class="hljs-string">""</span>;
  <span class="hljs-keyword">if</span> (index0 !== -<span class="hljs-number">1</span> && index1 !== -<span class="hljs-number">1</span>) &#123;
    mime = base64.slice(index0 + <span class="hljs-number">1</span>, index1);
  &#125;
  <span class="hljs-keyword">return</span> mime;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 组件发布</h2>
<h3 data-id="heading-2">组件注册工具函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入组件</span>
<span class="hljs-keyword">import</span> imgLargeMode <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/img-large-mode"</span>;
<span class="hljs-comment">// install方法,以供Vue.use()注册使用</span>
<span class="hljs-keyword">const</span> install = <span class="hljs-function">(<span class="hljs-params">Vue, option</span>) =></span> &#123;
  <span class="hljs-comment">// 创建构造器,生成一个Vue实例</span>
  <span class="hljs-keyword">const</span> componentInstance = Vue.extend(imgLargeMode);
  <span class="hljs-comment">// 定义实例化对象</span>
  <span class="hljs-keyword">let</span> currentComponent = <span class="hljs-literal">null</span>;
  <span class="hljs-comment">// 对象实例化,将组件挂载到body下</span>
  <span class="hljs-keyword">const</span> initInstance = <span class="hljs-function">() =></span> &#123;
    currentComponent = <span class="hljs-keyword">new</span> componentInstance();
    <span class="hljs-keyword">let</span> componentEL = currentComponent.$mount().$el;
    <span class="hljs-built_in">document</span>.body.appendChild(componentEL);
  &#125;;
  <span class="hljs-comment">// 定义用户使用的方法,挂在到Vue</span>
  Vue.prototype.$_openLargeMode = &#123;
    <span class="hljs-function"><span class="hljs-title">show</span>(<span class="hljs-params">opt</span>)</span> &#123;
      initInstance();
      <span class="hljs-keyword">return</span> currentComponent.show(opt);
    &#125;
  &#125;;
&#125;;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">"undefined"</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
  install(<span class="hljs-built_in">window</span>.Vue);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  install,
  imgLargeMode
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">package.json</h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"img-large-mode"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"./dist/img-large-mode.umd.min.js"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"Tmier"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"基于Vue的大图模式组件"</span>,
  <span class="hljs-attr">"keywords"</span>: [
    <span class="hljs-string">"img-large-mode"</span>,
    <span class="hljs-string">"img-large"</span>,
    <span class="hljs-string">"large-mode"</span>
  ],
  <span class="hljs-attr">"repository"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"git"</span>,
    <span class="hljs-attr">"url"</span>: <span class="hljs-string">"https://github.com/itmier/img-large-mode"</span>
  &#125;,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"files"</span>: [
    <span class="hljs-string">"dist"</span>
  ],
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"vue-cli-service build"</span>,
    <span class="hljs-attr">"package"</span>: <span class="hljs-string">"vue-cli-service build --target lib --name img-large-mode --dest dist ./src/components/index.js"</span>,
    <span class="hljs-attr">"lint"</span>: <span class="hljs-string">"vue-cli-service lint"</span>
  &#125;,
  <span class="hljs-attr">"dependencies"</span>: &#123;
   ...
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
   ...
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件发布的<code>package.json</code>具体说明:</p>
<blockquote>
<p>name: 组件名称,包名,必须有且不能重复</p>
<p>version: 版本号,发布时必填</p>
<p>main: 入口函数,启动项目的文件</p>
<blockquote>
<p>如果包由用户安装,则用户执行<code>require('foo-lib')</code>时,这时<code>require</code>将返回<code>main</code>字段所列出的文件的<code>module.exports</code>属性</p>
</blockquote>
<p>author: 作者</p>
<p>description: 描述</p>
<p>keywords: 关键词</p>
<p>license: 许可证</p>
<p>repository: 记录代码所在的资源库</p>
<p>private: 默认true,发布包时要设置为false,否则npm会拒绝发布它</p>
<p>files: 是一个文件数组,描述了将软件包作为依赖项安装时要包括的条目。如果在数组里面声明了一个文件夹,那么也会包含文件夹中的文件。某些特殊文件和目录也会被包括或者排除在外，无论它们是否存在于文件数组中。</p>
<pre><code class="hljs language-json copyable" lang="json">以下文件无论是否设置，总是包含：
*   `package.json`
*   `README`
*   `CHANGES`/`CHANGELOG`/`HISTORY`
*   `LICENSE`/`LICENCE`
*   `NOTICE`
*   The file in the “main” field

以下文件总是被忽略：
*   `.git`
*   `CVS`
*   `.svn`
*   `.hg`
*   `.lock-wscript`
*   `.wafpickle-N`
*   `.*.swp`
*   `.DS_Store`
*   `._*`
*   `npm-debug.log`
*   `.npmrc`
*   `node_modules`
*   `config.gypi`
*   `*.orig`
*   `package-lock.json`(use shrinkwrap instead)
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>在<code>scripts</code>中新添加一条命令,我觉得得记录一下:</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"package"</span>: <span class="hljs-string">"vue-cli-service build --target lib --name img-large-mode --dest dist ./src/components/index.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json">用法：vue-cli-service build [options] [entry|pattern]

选项：

  --mode        指定环境模式 (默认值：production)
  --dest        指定输出目录 (默认值：dist)
  --modern      面向现代浏览器带自动回退地构建应用
  --target      app | lib | wc | wc-async (默认值：app)
  --name        库或 Web Components 模式下的名字 (默认值：package.json 中的 <span class="hljs-string">"name"</span> 字段或入口文件名)
  --no-clean    在构建项目之前不清除目标目录
  --report      生成 report.html 以帮助分析包内容
  --report-json 生成 report.json 以帮助分析包内容
  --watch       监听文件变化
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>索引上面我加的那条命令可以解释为:  构建命令 构建目标 库 名称 img-large-mode 输出目录 dist 函数入口</p>
<p>PS: 这个入口可以是一个 <code>.js</code> 或一个 <code>.vue</code> 文件。如果没有指定入口，则会使用 <code>src/App.vue</code>。</p>
</blockquote>
<p>配置完成,接下来就是npm发布~</p>
<h3 data-id="heading-4">npm发布包</h3>
<pre><code class="hljs language-js copyable" lang="js">npm login <span class="hljs-comment">//输入用户名密码登录npm,没有的话去注册</span>
npm run package(自己定义的scripts打包命令)
npm publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok,发布成功,大功告成~</p>
<p><strong>还差一点,写文章的时候在家里的电脑上安装了一下自己发布的包,然后发现会带着<code>vue</code>,<code>vuex</code>,<code>vue-router</code>,是不是我有地方没有配置好?我安装了一下<code>element-ui</code>,发现它没有安装vue相关库,有没有大佬指点一下~</strong></p>
<h2 data-id="heading-5">3. 展望</h2>
<p>完善组件功能,目前能想到的就下面几个,有看到的可以补充一下:</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" disabled> 支持数组List,图片可以实现上一张下一张查看</li>
<li class="task-list-item"><input type="checkbox" disabled> 像<code>ant design</code> 一样的<code>modal</code> 动画效果,为图片遮罩添加动画</li>
</ul>
<p>参考文章: <a href="https://segmentfault.com/a/1190000022329597" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a></p></div>  
</div>
            