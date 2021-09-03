
---
title: 'vue 开发谷歌浏览器插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e17d8f8a36475b9512b88323315bcb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 18:03:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e17d8f8a36475b9512b88323315bcb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.什么是谷歌浏览器</h2>
<p>谷歌浏览器插件由**<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Fmv3%2Fbackground_pages%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/docs/extensions/mv3/background_pages/" ref="nofollow noopener noreferrer"><strong>background scripts</strong></a> <strong>,</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Fmv3%2Fcontent_scripts%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/docs/extensions/mv3/content_scripts/" ref="nofollow noopener noreferrer"><strong>content scripts</strong></a> <strong>,</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Fmv3%2Foptions%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/docs/extensions/mv3/options/" ref="nofollow noopener noreferrer"><strong>page</strong></a> <strong>,</strong> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Fmv3%2Fuser_interface%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/docs/extensions/mv3/user_interface/" ref="nofollow noopener noreferrer"><strong>UI elements</strong></a> **和各种逻辑文件,manifest.json组成。扩展组件是使用 Web 开发技术创建的：HTML、CSS 和 JavaScript和图片等资源组成的一个压缩包。扩展的组件将取决于其功能，并且可能不需要每个选项。</p>
<h2 data-id="heading-1">2.谷歌浏览器插件能力</h2>
<p>谷歌浏览器插件提供了很多实用API供我们使用：</p>
<ul>
<li>
<p>  书签控制；</p>
</li>
<li>
<p>  下载控制；</p>
</li>
<li>
<p>  窗口控制；</p>
</li>
<li>
<p>  标签控制；</p>
</li>
<li>
<p>  网络请求控制、事件监听；</p>
</li>
<li>
<p>  自定义原生菜单；</p>
</li>
<li>
<p>  通信机制；</p>
</li>
<li>
<p> 等等；</p>
</li>
</ul>
<h2 data-id="heading-2">3.配置文件（manifest.json）</h2>
<p>manifest.json 是一个谷歌浏览器插件必须要有的配置文件，用来配置所有和插件相关的配置，且必须在根目录下面。其中manifest_version、name、version是必须配置的。</p>
<pre><code class="copyable">&#123;

 // 清单文件的版本，这个必须写，而且必须是2

 "manifest_version": 2,

 // 插件的名称

 "name": "demo",

 // 插件的版本

 "version": "1.0.0",

 // 插件描述

 "description": "简单的Chrome扩展demo",

 // 图标，一般偷懒全部用一个尺寸的也没问题

 "icons":

 &#123;

 "16": "img/icon.png",

 "48": "img/icon.png",

 "128": "img/icon.png"

 &#125;,

 // 会一直常驻的后台JS或后台页面

 "background":

 &#123;

 // 2种指定方式，如果指定JS，那么会自动生成一个背景页

 "page": "background.html"

 //"scripts": ["js/background.js"]

 &#125;,

 // 浏览器右上角图标设置，browser_action、page_action、app必须三选一

 "browser_action": 

 &#123;

 "default_icon": "img/icon.png",

 // 图标悬停时的标题，可选

 "default_title": "这是一个示例Chrome插件",

 "default_popup": "popup.html"

 &#125;,

 // 当某些特定页面打开才显示的图标

 /*"page_action":

 &#123;

 "default_icon": "img/icon.png",

 "default_title": "我是pageAction",

 "default_popup": "popup.html"

 &#125;,*/

 // 需要直接注入页面的JS

 "content_scripts": 

 [

 &#123;

 //"matches": ["http://*/*", "https://*/*"],

 // "<all_urls>" 表示匹配所有地址

 "matches": ["<all_urls>"],

 // 多个JS按顺序注入

 "js": ["js/jquery-1.8.3.js", "js/content-script.js"],

 // JS的注入可以随便一点，但是CSS的注意就要千万小心了，因为一不小心就可能影响全局样式

 "css": ["css/custom.css"],

 // 代码注入的时间，可选值： "document_start", "document_end", or "document_idle"，最后一个表示页面空闲时，默认document_idle

 "run_at": "document_start"

 &#125;,

 // 这里仅仅是为了演示content-script可以配置多个规则

 &#123;

 "matches": ["*://*/*.png", "*://*/*.jpg", "*://*/*.gif", "*://*/*.bmp"],

 "js": ["js/show-image-content-size.js"]

 &#125;

 ],

 // 权限申请

 "permissions":

 [

 "contextMenus", // 右键菜单

 "tabs", // 标签

 "notifications", // 通知

 "webRequest", // web请求

 "webRequestBlocking",

 "storage", // 插件本地存储

 "http://*/*", // 可以通过executeScript或者insertCSS访问的网站

 "https://*/*" // 可以通过executeScript或者insertCSS访问的网站

 ],

 // 普通页面能够直接访问的插件资源列表，如果不设置是无法直接访问的

 "web_accessible_resources": ["js/inject.js"],

 // 插件主页，这个很重要，不要浪费了这个免费广告位

 "homepage_url": "https://www.baidu.com",

 // 覆盖浏览器默认页面

 "chrome_url_overrides":

 &#123;

 // 覆盖浏览器默认的新标签页

 "newtab": "newtab.html"

 &#125;,

 // Chrome40以前的插件配置页写法

 "options_page": "options.html",

 // Chrome40以后的插件配置页写法，如果2个都写，新版Chrome只认后面这一个

 "options_ui":

 &#123;

 "page": "options.html",

 // 添加一些默认的样式，推荐使用

 "chrome_style": true

 &#125;,

 // 向地址栏注册一个关键字以提供搜索建议，只能设置一个关键字

 "omnibox": &#123; "keyword" : "go" &#125;,

 // 默认语言

 "default_locale": "zh_CN",

 // devtools页面入口，注意只能指向一个HTML文件，不能是JS文件

 "devtools_page": "devtools.html"

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.vue-cli3开发谷歌浏览器插件实践</h2>
<p>搭建环境</p>
<ul>
<li>用vue-cli3创建一个项目： vue create vue-extension。</li>
<li>进入创建好的项目cd vue-extension</li>
<li>安装插件 vue-cli-plugin-chrome-ext：npm ivue-cli-plugin-chrome-ext </li>
<li>删除跟<strong>谷歌浏览器</strong>无用的文件夹：src/main.js、src/components</li>
</ul>
<p>运行项目
npm run build-watch 运行开发环境，对修改文件进行实时编译并自动在根目录下生成dist文件夹，然后在浏览器上加载dist文件夹完成插件安装
npm run build，运行生产环境，编译打包，将所有文件进行打包生成dist文件夹。</p>
<p>实时刷新插件
单纯地通过vue-cli3更新代码并不能使插件的background.js、content.js也跟着更新，因为代码已经加载到浏览器了，浏览器并不会监听这些文件的变化。** <a href="https://link.juejin.im/?target=https%3A%2F%2Fgithub.com%2Fxpl%2Fcrx-hotreload" target="_blank" title="https://link.juejin.im/?target=https%3A%2F%2Fgithub.com%2Fxpl%2Fcrx-hotreload"><strong>crx-hotreload</strong></a>**可以完美实现实时刷新功能，而不用重新手动加载。代码还简单易用，在这里我们直接将代码复制到src/utils/hot-reload.js文件：</p>
<pre><code class="copyable">// https://github.com/xpl/crx-hotreload/edit/master/hot-reload.js

const filesInDirectory = dir => new Promise(resolve =>

    dir.createReader().readEntries(entries =>

        Promise.all(entries.filter(e => e.name[0] !== '.').map(e =>

            e.isDirectory ?

            filesInDirectory(e) :

            new Promise(resolve => e.file(resolve))

        ))

        .then(files => [].concat(...files))

        .then(resolve)

    )

)

const timestampForFilesInDirectory = dir =>

    filesInDirectory(dir).then(files =>

        files.map(f => f.name + f.lastModifiedDate).join())

const reload = () => &#123;

    window.chrome.tabs.query(&#123;

        active: true,

        currentWindow: true

    &#125;, tabs => &#123; // NB: see https://github.com/xpl/crx-hotreload/issues/5

        if (tabs[0]) &#123;

            window.chrome.tabs.reload(tabs[0].id)

        &#125;

        window.chrome.runtime.reload()

    &#125;)

&#125;

const watchChanges = (dir, lastTimestamp) => &#123;

    timestampForFilesInDirectory(dir).then(timestamp => &#123;

        if (!lastTimestamp || (lastTimestamp === timestamp)) &#123;

            setTimeout(() => watchChanges(dir, timestamp), 1000) // retry after 1s

        &#125; else &#123;

            reload()

        &#125;

    &#125;)

&#125;

window.chrome.management.getSelf(self => &#123;

    if (self.installType === 'development') &#123;

        window.chrome.runtime.getPackageDirectoryEntry(dir => watchChanges(dir))

    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在vue.config.js对热刷新代码进行处理，如果是开发环境的话就将其复制到assets文件夹里面：</p>
<pre><code class="copyable">// vue.config.js
const plugins = [

  CopyWebpackPlugin([

    manifest

  ])

]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// 开发环境将热加载文件复制到dist文件夹</p>
<pre><code class="copyable">if (process.env.NODE_ENV !== 'production') &#123;

  plugins.push(

    CopyWebpackPlugin([&#123;

      from: path.resolve("src/utils/hot-reload.js"),

      to: path.resolve("dist")

    &#125;])

  )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5.开发</h2>
<p>谷歌历览器插件没有严格的项目结构要求，只需要有manifest.json即可，也不需要专门的开发环境和编辑器，普通的前端开发工具就可以。首先点击谷歌浏览器右上角菜单->更多工具->扩展程序进入 扩展程序管理页面,打开开发者模式，然后加载你打包好的文件，就可以加载你的插件了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e17d8f8a36475b9512b88323315bcb~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0486d8037a5e4cab8e440e58006e6e52~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b865581b554e4170b2ae7b11b66eb0c0~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG39.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            