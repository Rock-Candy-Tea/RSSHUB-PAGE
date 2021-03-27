
---
title: 'vite2+electron12短视频+直播应用_electron+swiper仿制抖音桌面版'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08c8a9952441f18bf0bd0b6a7517ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 03:01:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08c8a9952441f18bf0bd0b6a7517ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上个月有给大家分享一个<a href="https://juejin.cn/post/6933871014937886727/" target="_blank">Electron跨端仿制QQ聊天应用</a>项目。今天带来的是最新开发的Electron+Vite2跨端短视频+直播应用实战。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08c8a9952441f18bf0bd0b6a7517ca~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>vite2-electron-douyin</strong> 基于<code>vite2构建工具整合electron跨平台技术</code>开发的一款仿制抖音短视频+聊天+直播应用exe软件。支持<code>键盘上下键切换效果、新开多个窗口</code>等功能。</p>
</blockquote>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb9de37753c84daab18ca84e13b12adc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">技术栈</h2>
<ul>
<li>构建工具：vite.js</li>
<li>vue3全家桶：vue3.0+vuex4+vue-router@4 </li>
<li>跨端框架：electron12.0.1 </li>
<li>打包工具：vue-cli-plugin-electron-builder </li>
<li>组件库：vant3 (有赞移动端vue3组件库) </li>
<li>弹层组件：v3popup (vue3封装移动端弹窗组件) </li>
<li>滑动组件：swiper6</li>
</ul>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa0fce3c155e485ebf39f21265ce38cb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f8f1dcd2114d9e9e7ab0a2cbec0fd7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/072fc4af8f09443bac97dac1774b451d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c2b33f9efe74a26a8d4bf39f388cf74~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c572137e097d43cea9f3f76be628e0cf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1e4536f39d34a29879a5f8a783fbe91~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46d9061d48bd49c9a6ee2b8737a3119d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfc1f7f3bb046499f1db33492e4f9b2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce10e86399e485b898e09b738803c61~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52e95e0ebf0243209c4484282b45fbae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4528ca6c694e0799db672a9b72a176~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fad55c1bc145447b83cfce7359f974ff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ec4d236552e4a75af4ddea2f8168660~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a47b816570b42f9af2885ef588dec8c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1010858509b24cbd87ff811011aa8184~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb201a4295594ac7b05895264eaa3bbd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9608da77d2d447098c58e1e189e9f342~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e5b54928b4f4a5c9c64b3127be8dc49~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a942d5855284b4f8595c3190d300c82~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/470f51e43d12487ea1a4217438bff247~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">项目结构</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5202e3b83f2e4164bc1424866998739b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>目前electron最新稳定版为v12.0.2，项目中使用的是v12.0.1版。</p>
<p><a href="https://www.electronjs.org/" target="_blank" rel="nofollow noopener noreferrer">www.electronjs.org/</a></p>
<h2 data-id="heading-2">Electron主进程入口配置</h2>
<p>使用electron-builder构建的项目，根目录下有一个background.js配置文件。</p>
<pre><code class="copyable">/**
 * 主进程入口配置background.js
 */
'use strict'
 
import &#123; app, BrowserWindow, globalShortcut &#125; from 'electron'
import &#123; createProtocol &#125; from 'vue-cli-plugin-electron-builder/lib'
 
import Windows from './module/windows'
 
const isDevelopment = process.env.NODE_ENV !== 'production'
 
async function createWindow() &#123;
  let window = new Windows()
 
  window.listen()
  window.createWin(&#123;isMainWin: true, resize: false&#125;)
  window.createTray()
&#125;
 
// Quit when all windows are closed.
app.on('window-all-closed', () => &#123;
  if (process.platform !== 'darwin') &#123;
    app.quit()
  &#125;
&#125;)
 
app.on('activate', () => &#123;
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
&#125;)
 
// This method will be called when Electron has finished
app.on('ready', async () => &#123;
  createWindow()
&#125;)
 
// Exit cleanly on request from parent process in development mode.
if (isDevelopment) &#123;
  if (process.platform === 'win32') &#123;
    process.on('message', (data) => &#123;
      if (data === 'graceful-exit') &#123;
        app.quit()
      &#125;
    &#125;)
  &#125; else &#123;
    process.on('SIGTERM', () => &#123;
      app.quit()
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Electron+Vue3拖放导航条+TabBar标签栏</h2>
<p>项目整体采用无边框模式<code>frame: false</code>，为了拖动窗口，就需要自定义拖拽区域。</p>
<p>通过设置<code>-webkit-app-region:drag</code>来实现区块拖拽功能。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f52d6ec5e7b14d09b97aae46ac3beb21~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><WinBar bgcolor="transparent" transparent>
    <template #wbtn>
        <a class="wbtn" title="二维码名片" @click="isShowPersonalCard=true"><i class="iconfont icon-erweima"></i></a>
        <a class="wbtn" title="设置" @click="isShowSideMenu=true"><i class="iconfont icon-menu"></i></a>
    </template>
</WinBar>
 
<WinBar bgcolor="linear-gradient(to right, #36384a, #36384a)">
    <template #title>视频预览</template>
    <template #wbtn>
        <a class="wbtn" title="另存为" @click="handleDownLoad"><i class="iconfont icon-down"></i></a>
    </template>
</WinBar>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5029c9ddc6df41ecaa6dc4103ee3e6e8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>底部Tabbar组件采用了镂空背景设计，加上播放进度条功能。</p>
<pre><code class="copyable"><tabbar 
    bgcolor="linear-gradient(to bottom, transparent, rgba(0,0,0,.75))"
    color="rgba(245,255,235,.75)"
    activeColor="#fa367a"
    fixed
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的实现方式，大家感兴趣可以去看看下面这篇分享。</p>
<p><a href="https://www.cnblogs.com/xiaoyan2017/p/14449570.html" target="_blank" rel="nofollow noopener noreferrer">vue3+electron自定义导航条|右上角按钮</a></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab9e5c1493e4b989ef530ed58dd95c1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">vue3+electron自定义弹窗功能</h2>
<p>项目中的弹窗分为vue3自定义组件和electron创建弹窗两种方式。</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6452020fec3f4167a3719fd34555477a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">const handleSendFlower = () => &#123;
    let $el = v3popup(&#123;
        type: 'android',
        content: '<i class="iconfont icon-douzi c-00e077"></i> 确定送TA一颗微信豆吗？',
        btns: [
            &#123;text: '取消', click: () => $el.close()&#125;,
            &#123;text: '确定', style: 'color:#fa367a;', click: handleOk&#125;,
        ]
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c7ef733b5894b6382b2f6404c340349~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cdea0ee783c479eb23c8c76aa670eba~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">const handleAboutWin = () => &#123;
    data.isShowSideMenu= false createWin(&#123;
        title: '关于',
        route: '/about',
        width: 420,
        height: 320,
        resize: false,
        parent: winCfg.window.id,
        modal: true,
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Vite.js+Electron打包参数配置</h2>
<p>@vue/cli构建的项目，可以在vue.config.js中配置electron打包参数。而vite.js构建的项目，没办法在vite.config.js中配置，好在electron提供了一个electron-builder.json配置文件。</p>
<p>在根目录新建一个electron-builder.json配置文件。</p>
<pre><code class="copyable">/**
 * @Desc     vite2+electron打包配置
 * @Time     andy by 2021-03
 * @About    Q：282310962  wx：xy190310
 */
 
&#123;
    "productName": "electron-douyin", //项目名称 打包生成exe的前缀名
    "appId": "com.example.electrondouyin", //包名
    "compression": "maximum", //store|normal|maximum 打包压缩情况(store速度较快)
    "artifactName": "$&#123;productName&#125;-$&#123;version&#125;-$&#123;platform&#125;-$&#123;arch&#125;.$&#123;ext&#125;", //打包后安装包名称
    // "directories": &#123;
    //     "output": "build", //输出文件夹（默认dist_electron）
    // &#125;,
    "asar": false, //asar打包
    // 拷贝静态资源目录到指定位置（如根目录下的static文件夹会拷贝至打包后的dist_electron/win-unpacked/resources/static目录）
    "extraResources": [
        &#123;
            "from": "/static",
            "to": "static"
        &#125;,
    ],
    "nsis": &#123;
        "oneClick": false, //一键安装
        "allowToChangeInstallationDirectory": true, //允许修改安装目录
        "perMachine": true, //是否开启安装时权限设置（此电脑或当前用户）
        "artifactName": "$&#123;productName&#125;-$&#123;version&#125;-$&#123;platform&#125;-$&#123;arch&#125;-setup.$&#123;ext&#125;", //打包后安装包名称
        "deleteAppDataOnUninstall": true, //卸载时删除数据
        "createDesktopShortcut": true, //创建桌面图标
        "createStartMenuShortcut": true, //创建开始菜单图标
        "shortcutName": "ElectronDouYin", //桌面快捷键图标名称
    &#125;,
    "win": &#123;
        "icon": "/static/shortcut.ico", //图标路径
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，运行<code>npm run electron:builder</code>就可以打包了。</p>
<p>ending，使用vite2+electron模仿抖音短视频/直播应用就分享到这里。</p>
<p><a href="https://juejin.cn/post/6933871014937886727/" target="_blank">electron+vue3+antdv跨平台仿QQ聊天室</a></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426751c617454ac3ac37b05ee26e79c4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            