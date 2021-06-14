
---
title: '使用electron将web页面打包为桌面应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2352'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 23:19:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=2352'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Dash是一个非常棒的软件，在里面查询API很方面，但是他没有windows版本...，在mac上也是要收费的...，</p>
<p>好在有<a href="https://devdocs.io/" target="_blank" rel="nofollow noopener noreferrer">DevDocs</a>，功能与Dash一样，界面排版也都差不多，就是没有桌面版本</p>
<p>好，那我们用electron把它做成一个桌面软件~</p>

<h3 data-id="heading-0">从官网上clone一个例子</h3>
<p><code>git clone https://github.com/electron/electron-quick-start</code></p>
<p><code>cd electron-quick-start</code></p>
<p><code>yarn install</code></p>
<p><code>yarn start</code></p>
<p>如果安装失败，可以使用<code>cnpm</code>安装</p>
<p>项目跑起来之后，就会出现electron的桌面页面，提供了本地开发环境，大概看一下入口文件<code>main.js</code> 和<code>package.json</code></p>
<p>修改main.js，注释掉loadFile方法，改用loadURL打包我们的网页</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// and load the index.html of the app.</span>
<span class="hljs-comment">// mainWindow.loadFile('index.html')</span>
<span class="hljs-comment">// and load a webpage URL of the app</span>
   mainWindow.loadURL(<span class="hljs-string">'https://devdocs.io'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// pageage.json</span>
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"start"</span>: <span class="hljs-string">"electron ."</span>
  &#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"electron"</span>: <span class="hljs-string">"^4.1.1"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前目录中的index.html就是入口文件。</p>
<h3 data-id="heading-1">安装依赖，对当前项目进行打包</h3>
<p><code>yarn add electron-packager --save-dev</code></p>
<p><code>electron-packager</code>是打成 exe 文件的插件。<code>执行命令需要额外的目录（比如 dist ），且目录下有 package.json 和入口文件 (如 electron.js )，否则打包会报错</code></p>
<p>1.在当前文件中新建 <code>dist</code> 目录，复制<code>main.js</code>到<code>dist</code>目录下，命名为<code>electron.js</code></p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// main.js</span>
  <span class="hljs-comment">// and load the index.html of the app.</span>
  mainWindow.loadFile(<span class="hljs-string">'../index.html'</span>) <span class="hljs-comment">//修改对应的index.html路径</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.复制<code>package.json</code>到<code>dist </code>文件目录下</p>
<p>修改该文件入口</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
<span class="hljs-string">"main"</span>: <span class="hljs-string">"electron.js"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.在项目的<code>package.json</code>中（注意不是 dist 下的<code>package.json</code>）为之前下载好的<code>electron-packager</code>，增加一条启动命令</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"start"</span>: <span class="hljs-string">"electron ."</span>,
    <span class="hljs-attr">"electron_build"</span>: <span class="hljs-string">"electron-packager ./dist Devdocs --platform=win32 --arch=x64 -icon=./icon/icon.ico --overwrite"</span>   
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>electron-packager <sourcedir> <appname> –platform=<platform> –arch=<arch> [optional flags…]</code></p>
<ul>
<li><code>sourcedir</code>: 资源(dist/package.json)路径，在本例中既是<code>./dist/</code></li>
<li><code>appname</code>:打包出的exe名称,这里取名为<code>Devdocs</code></li>
<li><code>platform</code> :平台名称（ windows 是 win32 ）</li>
<li><code>arch</code>: 版本，本例为x64</li>
<li><code>optional </code>: 额外的配置（选填）</li>
</ul>
<p>本例中选填参数用到了<code>icon</code>自定义图标与<code>overwrite</code>覆盖，其中<code>icon</code>仅支持ico格式图标，且分辨率最好为<code>256X256</code> ，否则会模糊。（PS：这里推荐一个<a href="https://image.online-convert.com/convert-to-ico" target="_blank" rel="nofollow noopener noreferrer">在线图片格式转换网站</a>，实用方便~）</p>
<p>4.生成exe
执行<code>npm run electron_build</code>，可以看到项目目录中多了一个<code>Devdocs-win32-x64</code>文件，找到里面的Devdocs.exe运行即可。</p>

<p>5.修改.exe图标</p>
<p>也可以通过下载安装<a href="https://link.jianshu.com/?t=http%3A%2F%2Fwww.angusj.com%2Fresourcehacker%2F" target="_blank" rel="nofollow noopener noreferrer">Resource Hacker</a>。在.exe文件上鼠标右键，更换图标后保存即可。</p></div>  
</div>
            