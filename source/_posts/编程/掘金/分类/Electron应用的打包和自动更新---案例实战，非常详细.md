
---
title: 'Electron应用的打包和自动更新---案例实战，非常详细'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55e1a0e45ca47c0a34e14bc5de5f74f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 16:02:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55e1a0e45ca47c0a34e14bc5de5f74f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在上一篇文章中，我们介绍了electron的一些基础知识， <a href="https://juejin.cn/post/6974192432443293726" target="_blank">入门Electron，手把手教你编写完整实用案例</a>，在这里我们将基于这个项目继续介绍Electron的打包和自动更新。</p>
<h1 data-id="heading-0">生成图标</h1>
<p>在打包应用之前，要为应用准备一个图标，作为安装包图标。不同的操作系统所需图标的格式不同，Mac对应的格式为<code>icns</code>，Windows对应的格式为<code>ico</code>。</p>
<p>图标的生成可以借助 <code>electron-icon-builder</code>。</p>
<ul>
<li>首先，准备一张<code>1024*1024的png</code>图片，将图片放在项目文件夹中，我们这里选择放在<code>tasky/public文件夹</code>中。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55e1a0e45ca47c0a34e14bc5de5f74f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>安装 electron-icon-builder：</p>
<p><code>npm i electron-icon-builder --D</code></p>
</li>
<li>
<p>在<code>package.json</code>的<code>scripts</code>添加指令：</p>
<p><code>"build-icon": "electron-icon-builder --input=./public/icon.png --output=build --flatten"</code></p>
</li>
<li>
<p>运行<code>npm run build-icon</code>，就会在<code>build</code>文件夹中生成一系列打包所需的图标文件。</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c40e4e274db46c9bd3db008a4d7937c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">打包应用</h1>
<p>Electron生态下常用的打包工具有两个：<code>electron-builder</code> 和 <code>electron-packager</code>。</p>
<p><code>electron-builder</code>配置更灵活，使用也更广泛。下面，我们使用<code>electron-builder</code>来进行打包。</p>
<h2 data-id="heading-2">安装</h2>
<pre><code class="copyable">npm i electron-builder --D
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">配置</h2>
<p>使用<code>electron-builder</code>打包主要是各种配置，它支持两种配置方式：</p>
<ol>
<li>在<code>package.json</code>中添加<code>build</code>字段：</li>
</ol>
<pre><code class="copyable">"build": &#123;
  "appId": "your.app.id"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>指定配置文件，在其中写入配置项。默认是项目根目录下的electron-builder.yml。</li>
</ol>
<pre><code class="copyable">appId："your.app.id"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在日常开发中，<code>package.json</code>这种配置方式比较常用，我们也以这种方式为主。</p>
<h3 data-id="heading-4">基础配置</h3>
<pre><code class="copyable">"build": &#123;
    "appId": "this.is.tasky", 
    "productName": "Tasky",
    "copyright": "Copyright © 2021 Alaso",
    "directories": &#123;
      "buildResources": "build",   //指定打包需要的静态资源，默认是build
      "output": "dist",  //打包生成的目录，默认是dist
    &#125;
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>build文件夹放置的是，<code>electron-builder</code>默认的在打包过程中需要的静态文件，比如我们上面生成的图标文件；dist文件夹放置的是打包生成的各种文件。</p>
<ol>
<li>在<code>package.json</code>的<code>scripts</code>添加指令：<code>"pack": "electron-builder"</code></li>
<li>运行<code>npm run pack</code></li>
</ol>
<p>基于以上的配置，<code>electron-builder</code>会根据当前的操作系统打包出默认的文件。比如，在windows平台下，打包结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b4ea351569240b18c2d84fdf3fef80e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">平台相关的配置</h3>
<p><strong><code>electron-builder</code>会自动识别当前的操作系统，打出系统对应的安装包。</strong> 这也意味着，如果要生成exe\msi，需要在Windows操作系统，如果是dmg，则需要在Mac操作系统。</p>
<p><code>electron-builder</code>的配置选项中，有很多跟操作系统相关的配置，可以对不同平台的打包做一些定制效果。下面以Windows和Mac为例，介绍一些常用的平台相关的配置。</p>
<ol>
<li>Windows</li>
</ol>
<pre><code class="copyable">"build": &#123;
  ...
  "win": &#123;
    "target": ["msi","nsis"],        //安装包的格式，默认是"nsis"
    "icon": "build/icons/icon.ico"   //安装包的图标
  &#125;,
  
  //"target"值"nsis"打包出来的就是exe文件
  //nsis是windows系统安装包的制作程序，它提供了安装、卸载、系统设置等功能
  //关于"nsis"的一些配置
  "nsis": &#123;                          
    "oneClick": false,               //是否一键安装，默认为true
    "language": "2052",              //安装语言，2052对应中文
    "perMachine": true,              //为当前系统的所有用户安装该应用程序
    "allowToChangeInstallationDirectory": true   //允许用户选择安装目录
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aae055ad0ea7465d97478f286c12fc36~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
2. Mac</p>
<pre><code class="copyable">...
"build": &#123;
  "mac": &#123;
     "target": ["dmg", "zip"],       //安装包的格式，默认是"dmg"和"zip"
     "category": "public.app-category.utilities"  //应用程序安装到哪个分类下，具体有哪些分类可以在苹果官网上找
  &#125;,
  "dmg": &#123;
     "background": "build/background.jfif",   //安装窗口背景图
     "icon": "build/icons/icon.icns",         //安装图标
     "iconSize": 100,                         //图标的尺寸
     "contents": [                            //安装图标在安装窗口中的坐标信息
        &#123;
          "x": 380,
          "y": 180,
          "type": "link",
          "path": "/Applications"
        &#125;,
        &#123;
          "x": 130,
          "y": 180,
          "type": "file"
        &#125;
     ],
     "window": &#123;                             //安装窗口的大小
        "width": 540,
        "height": 380
     &#125;
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/147d20ccf4134748b566336c7a4d3082~tplv-k3u1fbpfcp-watermark.image" alt="&#123;B92F643C-E8F2-183F-C7DE-E0C24E347CFC&#125;.jpg" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/436beba53e1f45a4887a3ba5fb82ed3b~tplv-k3u1fbpfcp-watermark.image" alt="&#123;552B6FD3-6150-4409-662B-0916EBC574D3&#125;.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">会将哪些文件pack到安装包</h2>
<p>在打包生成的文件夹中，会有一个<code>app.asar</code>，它是Electron应用程序的主业务文件压缩包，要知道项目中哪些文件被pack到安装包，可以通过解压<code>app.asar</code>进行查看。</p>
<p>解压<code>app.asar</code>需要借助asar工具，首先来安装：<code>npm i asar -g</code>。</p>
<p>然后切换到<code>app.asar</code>所在目录，执行：<code>asar extract app.asar ./app-folder</code>。</p>
<p>以windows为例，<code>app.asar</code>位于<code>tasky\dist\win-unpacked\resources</code>目录中，解压后，可以看到app-folder中的内容如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84ce48d6f2144d28711a3090845dc77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，基本上就是项目所有文件了（除了<code>package-lock.json</code>\ <code>.gitignore</code> \ <code>build</code>文件夹），并且还有<code>node_modules</code>。</p>
<p>对于<code>node_modules</code>，<strong>并不是所有<code>node_modules</code>中的内容都会被打包进安装包，只有<code>package.json</code>中<code>dependencies</code>字段中的依赖会被打包，<code>devDependencies</code>字段中的依赖则不会。</strong> 这是唯一规则，跟项目实际是否使用依赖没有关系。</p>
<p>所以，为了减小安装包体积，建议在渲染进程中使用的外部包，都安装在<code>devDependencies</code>中，然后使用webpack将外部包的代码和业务代码打包到一起，在后面的文章中会详细介绍。</p>
<p>当然，<strong>可以通过配置files字段，来指定将哪些内容进行打包</strong>。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74d5fb7dbcb42e68d8a33f225b18c56~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如，我们只打包<code>src文件夹</code>、<code>index.js</code>和<code>package.json</code>，可以这样配置：</p>
<pre><code class="copyable">"build": &#123;
  "files": [
    "package.json",
    "index.js",
    "src/**/*"
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">自动更新</h1>
<p>要自动更新，应用程序的安装包应该存放在互联网的某台服务器上，每次打开应用的时候，进行自动检测，根据当前应用程序的<code>version</code>和线上版本进行匹配，当发现有新的<code>version</code>的时候，就自动下载，下载完成后，询问用户是否安装新版本。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1147929e115d40ee93009f4f62305d87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">打包不同版本</h2>
<p>在<code>package.json</code>中，有个<code>"version"</code>字段，用于决定当前版本。</p>
<ul>
<li>step1: 设置<code>"version": "1.0.0"</code>，运行<code>npm run pack</code></li>
<li>step2: 设置<code>"version": "1.0.1"</code>, 运行<code>npm run pack</code></li>
</ul>
<p>虽然，我们没有改变应用程序的内容，但是会被识别成"1.0.0"和"1.0.1"两个版本。</p>
<h2 data-id="heading-9">搭建一个服务器放安装包</h2>
<p>我们在本地启动一个服务器，放最新版本的安装包资源。</p>
<ul>
<li>1、初始化</li>
</ul>
<pre><code class="copyable">mkdir tasky-server
cd tasky-server
npm init -y
npm install koa koa-static --save
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2、在tasky-server目录下新建<code>index.js</code>，内容如下:</li>
</ul>
<pre><code class="copyable">const Koa = require('koa')
const app = new Koa()

const static = require('koa-static')
const path = require('path')

app.use(static(path.join(__dirname,'./static')));

app.listen(9005)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3、在创建一个<code>static</code>文件夹，放入最新版本的安装包set。具体包含哪些文件呢？假如最新版本是"1.0.1"。</li>
</ul>
<p><strong>Mac平台：</strong> <code>latest-mac.yml</code>、 <code>Tasky-1.0.1-mac.zip</code>、<code>Tasky-1.0.1.dmg</code>、<code>Tasky-1.0.1.dmg.blockmap</code></p>
<p><strong>Windows平台：</strong> <code>latest.yml</code>、<code>Tasky 1.0.1.msi</code>、<code>Tasky Setup 1.0.1.exe</code>、<code>Tasky Setup 1.0.1.exe.blockmap</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8adfcfeff5e4a8d80d245249bf79593~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4、启动服务器。<code>node index.js</code></li>
</ul>
<h2 data-id="heading-10">检测更新</h2>
<p>检测更新可以借助<code>electron-updater</code>来实现。它结合<code>electron-builder</code>，实现起来非常简单。直接上代码。</p>
<ul>
<li>第一步、在build中配置<code>"publish"</code>字段：</li>
</ul>
<pre><code class="copyable">"build": &#123;
    ...
    "publish": [
      &#123;
         "provider": "generic",
         "url": "http://127.0.0.1:9005/" 
      &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步、在应用程序主进程中调用<code>electron-updater</code>模块检测更新。</p>
<pre><code class="copyable">const &#123; autoUpdater &#125; = require('electron-updater')
function checkUpdate()&#123;
  if(process.platform == 'darwin')&#123;  
  
    //我们使用koa-static将静态目录设置成了static文件夹，
    //所以访问http://127.0.0.1:9005/darwin，就相当于访问了static/darwin文件夹，win32同理
    autoUpdater.setFeedURL('http://127.0.0.1:9005/darwin')  //设置要检测更新的路径
    
  &#125;else&#123;
    autoUpdater.setFeedURL('http://127.0.0.1:9005/win32')
  &#125;
  
  //检测更新
  autoUpdater.checkForUpdates()
  
  //监听'error'事件
  autoUpdater.on('error', (err) => &#123;
    console.log(err)
  &#125;)
  
  //监听'update-available'事件，发现有新版本时触发
  autoUpdater.on('update-available', () => &#123;
    console.log('found new version')
  &#125;)
  
  //默认会自动下载新版本，如果不想自动下载，设置autoUpdater.autoDownload = false
  
  //监听'update-downloaded'事件，新版本下载完成时触发
  autoUpdater.on('update-downloaded', () => &#123;
    dialog.showMessageBox(&#123;
      type: 'info',
      title: '应用更新',
      message: '发现新版本，是否更新？',
      buttons: ['是', '否']
    &#125;).then((buttonIndex) => &#123;
      if(buttonIndex.response == 0) &#123;  //选择是，则退出程序，安装新版本
        autoUpdater.quitAndInstall() 
        app.quit()
      &#125;
    &#125;)
  &#125;)
&#125;

app.on('ready', () => &#123;
  //每次启动程序，就检查更新
  checkUpdate()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ba57ae1611447d8fdd07408c32be9a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>是否需要更新是根据什么判断的呢？</strong></p>
<p>electron-updater会根据上面setFeedURL指定路径下的<code>latest.yml</code>中的<code>version</code>来判断是否需要更新，大于当前版本的<code>version</code>则需要更新，否则不更新。<code>.yml</code>也是一种配置文件，有点类似于我们常用的<code>.json</code>配置文件，两者写法不一样。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/285b87b8761741b391b8faaa2b251123~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">基于github的方案</h2>
<p>如果你不想搭建自己的服务器，也可以借助github。使用github自动发布，不用每次手动上传最新安装包资源。</p>
<h3 data-id="heading-12">自动发布</h3>
<p>第一步，依然是配置<code>"publish"</code>字段。</p>
<pre><code class="copyable">"build": &#123;
    ...
    "publish": ['github']
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步、在<code>"scripts"</code>中配置新的指令，由于github权限控制，需要GH_TOKEN，可以在 <a href="https://github.com/settings/tokens" target="_blank" rel="nofollow noopener noreferrer">github.com/settings/to…</a> 中生成GH_TOKEN。</p>
<pre><code class="copyable">"scripts": &#123;
    ...
    "release": "cross-env GH_TOKEN=ghp_KmVD3.......W2k3Pd4vV electron-builder"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步、<code>npm run release</code>，就会在打包后，将资源上传到github，生成release draft，你在github项目中，找到这个draft，publish release就可以了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea2270f6e76840eb8a4e1c6a6c652cae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e69581269316471597535bfaecd8e190~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">检测更新</h3>
<p>和上面类似，以Windows为例，代码如下。</p>
<pre><code class="copyable">const &#123; autoUpdater &#125; = require('electron-updater')
function checkUpdate()&#123;
  //检测更新
  autoUpdater.checkForUpdates()
  
  //监听'error'事件
  autoUpdater.on('error', (err) => &#123;
    console.log(err)
  &#125;)
  
  //监听'update-available'事件，发现有新版本时触发
  autoUpdater.on('update-available', () => &#123;
    console.log('found new version')
  &#125;)
  
  //默认会自动下载新版本，如果不想自动下载，设置autoUpdater.autoDownload = false
  
  //监听'update-downloaded'事件，新版本下载完成时触发
  autoUpdater.on('update-downloaded', () => &#123;
    dialog.showMessageBox(&#123;
      type: 'info',
      title: '应用更新',
      message: '发现新版本，是否更新？',
      buttons: ['是', '否']
    &#125;).then((buttonIndex) => &#123;
      if(buttonIndex.response == 0) &#123;  //选择是，则退出程序，安装新版本
        autoUpdater.quitAndInstall() 
        app.quit()
      &#125;
    &#125;)
  &#125;)
&#125;

app.on('ready', () => &#123;
  //每次启动程序，就检查更新
  checkUpdate()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">结语</h1>
<p>我们上面的例子中，是将页面的web资源都打包到了安装包，还有一种情况就是，web资源和“app壳子”分离，web资源放在服务器，每次都通过网络动态加载，像下面这样：</p>
<pre><code class="copyable">mainWindow.loadURL('https://juejin.cn')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在业务需要频繁更新的场景中，可以使用这种方式，快速无障碍地实现更新。在这种情况下，我们可以按照上述方式打包和更新“壳子”，也就是主进程相关；而页面资源的打包和普通的前端项目打包无异，这里不再赘述。</p>
<p>这篇文章主要讲解了使用<code>electron-builder</code>打包应用和自动更新，在下一篇文章中，我们将探讨Electron和Vue的结合使用。</p></div>  
</div>
            