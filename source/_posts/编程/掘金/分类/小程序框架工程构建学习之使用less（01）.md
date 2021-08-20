
---
title: '小程序框架工程构建学习之使用less（01）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62db785fd042406b98d7608176d5b62b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 01:48:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62db785fd042406b98d7608176d5b62b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>最近在探索学习前端工程化的知识，发现了Vue mini小程序框架项目。从GitHub star数来看，了解Vue mini框架的人可能不多，它是一个可以用vue3 Composition API编写小程序的框架，与众多小程序开发框架（taro，wepy等）不同的是，它的底层直接依赖于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Ftree%2Fmaster%2Fpackages%2Freactivity" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/tree/master/packages/reactivity" ref="nofollow noopener noreferrer">@vue/reactivity</a>， 强调轻量的运行时，它既不依赖任何编译步骤，也不涉及任何 Virtual DOM。详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuemini.org%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuemini.org/guide/" ref="nofollow noopener noreferrer">官方文档</a>。不过目前要介绍的并不是该框架如何使用或者它的实现原理，而是由于该框架初始化的构建文件build.js代码量少，非常适合入门学习工程构建，接下来将分多篇文章输出相关知识。</p>
</blockquote>
<p>首先，我们新建一个小程序项目，它的结构目录如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62db785fd042406b98d7608176d5b62b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于习惯了web开发的我们来说，先从最简单的一个痛点需求出发：原生wxss写样式太不方便了，我要用less编写样式代码，如何做？</p>
<h3 data-id="heading-0">项目准备</h3>
<p>新建一个文件夹，比如就叫mini-demo，我们先将上面新建的初始化小程序的代码中所有的样式文件wxss后缀改为less，然后拷贝到mini-demo -> src的目录下，并在根目录下npm init创建一个package.json文件，后面会安装各种构建依赖包。</p>
<p>通常来说，使用less都会创建variables.less及mixins.less文件，目前我想将这两个less样式文件约定，统一放到src目录下叫做styles的文件夹中，然后在工程构建中将这两个文件内容逐一添加进各个样式文件中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57dc1553e580469e91249e75053ae4fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此，项目准备工作已经完成，接下来我们要做的就是构建工程代码实现：</p>
<ol>
<li>监听src目录下的less样式文件改动，实时将less文件编译成css，并将文件后缀名重新改为wxss</li>
<li>将src文件整体输出到dist目录</li>
</ol>
<h3 data-id="heading-1">创建build.js</h3>
<p>在根目录下创建build.js，并在package.json script中添加脚本</p>
<pre><code class="copyable">"dev": "node build.js",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后续我们通过npm run dev方式启动运行构建代码</p>
<h3 data-id="heading-2">编写build.js构建脚本</h3>
<p>首先，启动npm run dev后，我们要实现：</p>
<ol>
<li>文件监听功能，npm包：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fchokidar" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/chokidar" ref="nofollow noopener noreferrer">chokidar</a></li>
<li>文件操作的功能（如将src目录下文件移动到dist目录），npm包：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Ffs-extra" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/fs-extra" ref="nofollow noopener noreferrer">fs-extra</a></li>
<li>less编译：npm包：less</li>
<li>处理样式，npm包：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fpostcss" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/postcss" ref="nofollow noopener noreferrer">postcss</a></li>
</ol>
<p>以上相关包的用法请自行查阅文档，下面直接上代码，配合注释不难阅读：</p>
<p>build.js</p>
<pre><code class="copyable">const chokidar = require('chokidar');
const fs = require('fs-extra');
const postcss = require('postcss');
const less = require('less');
const path = require('path'); // node 自带的，无需安装依赖包，直接引入即可

async function dev() &#123;
  // 对不同文件进行不同的处理，这里暂时只实现对样式文件的处理 
  const cb = (filePath) => &#123;
     if (/\.less$/.test(filePath)) &#123;
      processStyle(filePath);
      return;
    &#125;
    // 将文件拷贝到dist目录
    fs.copy(filePath, filePath.replace('src', 'dist'));
  &#125;
  
  chokidar
    .watch(['src'], &#123;
      ignored: ['**/.&#123;gitkeep,DS_Store&#125;'],
    &#125;)
    .on('add', (filePath) => &#123;
      // 监听到有新的文件添加进来执行的逻辑
      
      // styles 文件夹下的less样式文件不会打包进dist目录
      if (filePath.includes(path.join('src', 'styles'))) return;
      cb(filePath);
    &#125;)
    .on('change', (filePath) => &#123;
      // 文件内容改变触发的逻辑
      console.log('change file: ' + filePath)

      if (filePath.includes(path.join('src', 'styles'))) &#123;
        // 重新编译样式文件
        recompileStyles();
        return;
      &#125;

      cb(filePath);
    &#125;);
&#125;

// 样式文件处理
async function processStyle(filePath,) &#123;
  let source = await fs.readFile(filePath, 'utf8');
  // 在pages文件下的各个样式文件中注入variables和mixins定义的内容
  source =
    `@import '$&#123;path.resolve('src/styles/variables.less')&#125;';\n` +
    `@import '$&#123;path.resolve('src/styles/mixins.less')&#125;';\n` +
    source;

  // 将less编译为css  
  const &#123; css &#125; = await less.render(source, &#123;
    filename: path.resolve(filePath),
  &#125;);

  // postcss可以利用各种插件对css内容进行处理，这里先暂时不用
  const &#123; css: wxss &#125; = await postcss().process(css, &#123; map: false, from: undefined &#125;);

  // 修改less后缀为wxss并且将文件输出到dist目录
  const destination = filePath.replace('src', 'dist').replace(/\.less$/, '.wxss');
  
  await fs.copy(filePath, destination);
  fs.writeFile(destination, wxss);
&#125;

// 由于styles目录下的文件修改可能影响多个文件，所以重新遍历编译一遍所有页面样式文件
function recompileStyles() &#123;
    const watcher = chokidar.watch(['src/**/*.less', '!src/styles/**/*']);
    watcher.on('add', (filePath) => &#123;
      processStyle(filePath);
    &#125;);
    watcher.on('ready', () => watcher.close());
&#125;

dev()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们往styles目录的文件中增加测试数据</p>
<p>variables.less</p>
<pre><code class="copyable">@blue: blue;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mixins.less</p>
<pre><code class="copyable">.backgroundBlue() &#123;
  background: @blue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开src -> page -> index.less,我们往里面添加</p>
<pre><code class="copyable">.test &#123;
  .testone &#123;
    .backgroundBlue()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后运行npm run dev，可以看到dist目录成功生成：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a52b74867243fc8af09ed9730a2b92~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点开index.wxss,可以看到less文件成功编译：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33c4428aec6e444496ac9d093abe0521~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpengjinlong%2Frebuild-miniprogram" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pengjinlong/rebuild-miniprogram" ref="nofollow noopener noreferrer">源码地址</a></h3>
<p>仓库源码以序号对应每篇文章源码</p></div>  
</div>
            