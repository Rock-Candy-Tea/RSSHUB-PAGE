
---
title: '【Electron】electron-builder打包基础配置介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2f270fb1634a5da580707be0f27b03~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 03:04:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2f270fb1634a5da580707be0f27b03~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与「新人创作礼」活动， 一起开启掘金创作之路。</p>
<h1 data-id="heading-0">一、前言</h1>
<p>本篇主要介绍electron-builder打包的基础配置选项，本文项目基础框架为vue+electron-builder+electron，其中包含打包名称、应用名称、应用icon等配置。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/" ref="nofollow noopener noreferrer">electron-builder官网</a></p>
<h1 data-id="heading-1">二、具体介绍</h1>
<p>这里打包配置写在了vue.config.js中，内容如下</p>
<p>这里我们一个一个的讲一下每个常用配置的作用</p>
<h3 data-id="heading-2">1.<code>productName</code>应用的名称</h3>
<p>这个就是你应用安装完之后的名称，如图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe2f270fb1634a5da580707be0f27b03~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.<code>appId</code>应用id</h3>
<p>这个是你应用的唯一id，，<strong>确认后不要改动了</strong>！不然在更新时候，会被认做为两个应用。这个是在apple那里你申请证书的时候，用生成的那个id就可以，类似这种'com.example.app'。</p>
<h3 data-id="heading-4">3.<code>publish</code>更新配置</h3>
<p>这个主要是用来配置应用的更新地址的，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">publish</span>: [ <span class="hljs-comment">// 更新服务器地址</span>
      &#123;
        <span class="hljs-attr">provider</span>: <span class="hljs-string">'generic'</span>,
        <span class="hljs-attr">url</span>: <span class="hljs-string">'electron应用的更新地址'</span>
      &#125;
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4.<code>directories</code>目录</h3>
<p>这个主要是用来配置打包之后，包的输出文件夹， 默认地址是dist_electron，配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">directories</span>: &#123;
  <span class="hljs-attr">output</span>: <span class="hljs-string">'可自定义文件夹名称'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.<code>asar</code>加密</h3>
<p>是否使用Electron的存档格式将应用程序的源代码打包到存档中。这里我们使用webpack的打包就好了，我没有开启这个。</p>
<h3 data-id="heading-7">6.<code>dmg</code>mac安装包的配置项</h3>
<p>这个主要是为了配置dmg格式安装包的，具体内容可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fconfiguration%2Fdmg" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/configuration/dmg" ref="nofollow noopener noreferrer">点击查看</a>。
这里我主要是用来配置macOS系统的安装界面，如下图，里面的拖拽应用到文件夹是图片上的哦。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aee3fffa5bf84fbfb010c19b3575b971~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中标题、应用图标（取决于你设置的应用图标）、应用名称（取决于你设置的应用名称）、背景图以及位置大小都是可以配置，配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">dmg</span>: &#123;
    <span class="hljs-attr">background</span>: <span class="hljs-string">'背景图地址'</span>,
    <span class="hljs-attr">contents</span>: [
        &#123; <span class="hljs-comment">// 这个是右边图标及内容</span>
          <span class="hljs-attr">x</span>: <span class="hljs-number">410</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">190</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'link'</span>,
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/Applications'</span>
        &#125;,
        &#123; <span class="hljs-comment">// 这个是你左边的图标</span>
          <span class="hljs-attr">x</span>: <span class="hljs-number">130</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">190</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-string">'file'</span>
        &#125;
    ],
    <span class="hljs-attr">window</span>: &#123; <span class="hljs-comment">// 这里是整个窗口的大小</span>
        <span class="hljs-attr">height</span>: <span class="hljs-number">380</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-number">540</span>
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">7.<code>mac</code>macOS系统相关打包配置</h3>
<p>这里面的选项适用于任何macOS目标，具体内容可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fconfiguration%2Fmac" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/configuration/mac" ref="nofollow noopener noreferrer">点击查看</a>。例如在mac系统上你应用的图标、打好的mac安装包的名称、mac系统下输出包的格式等，具体配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">mac</span>: &#123;
    <span class="hljs-comment">// 应用程序图标</span>
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'自定义，建议使用png'</span>,
    <span class="hljs-comment">// 应用程序包名 </span>
    <span class="hljs-attr">artifactName</span>: <span class="hljs-string">'$&#123;productName&#125;-$&#123;platform&#125;-$&#123;arch&#125;-$&#123;version&#125;.$&#123;ext&#125;'</span>,
    <span class="hljs-attr">target</span>: [ <span class="hljs-comment">// 要打的包的格式类型设置</span>
        <span class="hljs-string">'dmg'</span>,
        <span class="hljs-string">'zip'</span> <span class="hljs-comment">// 这里注意更新的时候，mac只认zip格式的包</span>
    ], 
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">8.<code>win</code>windows系统相关打包配置</h3>
<p>这里面的选项适用于任何windows目标，具体内容可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fconfiguration%2Fwin" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/configuration/win" ref="nofollow noopener noreferrer">点击查看</a>。例如在windows系统上你应用的图标、打好的win安装包的名称、win系统下输出包的格式等，具体配置如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">win</span>: &#123;
    <span class="hljs-attr">icon</span>: <span class="hljs-string">`256*256的ico格式或png格式文件`</span>,
    <span class="hljs-attr">artifactName</span>: <span class="hljs-string">'$&#123;productName&#125;-$&#123;platform&#125;-$&#123;arch&#125;-$&#123;version&#125;.$&#123;ext&#125;'</span>,
    <span class="hljs-attr">target</span>: [
        &#123;
          <span class="hljs-comment">// 打包成一个独立的 exe 安装程序</span>
          <span class="hljs-attr">target</span>: <span class="hljs-string">'nsis'</span>,
          <span class="hljs-comment">// 这个意思是打出来32 bit + 64 bit的包，但是要注意：这样打包出来的安装包体积比较大，所以建议直接打32的安装包。</span>
          <span class="hljs-attr">arch</span>: [
          <span class="hljs-comment">// 'x64',</span>
            <span class="hljs-string">'ia32'</span>
          ]
        &#125;
    ],
    <span class="hljs-comment">// 打出来的包，自动获取管理员权限，不建议打开</span>
    <span class="hljs-comment">// requestedExecutionLevel: 'highestAvailable',</span>
    <span class="hljs-comment">// ====windows签名公证相关====start--如果没做windows签名，不要开启</span>
    <span class="hljs-comment">// verifyUpdateCodeSignature: false,</span>
    <span class="hljs-comment">// signingHashAlgorithms: [</span>
    <span class="hljs-comment">//     'sha256'</span>
    <span class="hljs-comment">// ],</span>
    <span class="hljs-comment">// signDlls: true,</span>
    <span class="hljs-comment">// rfc3161TimeStampServer: 'http://timestamp.comodoca.com',</span>
    <span class="hljs-comment">// certificateFile: '******.pfx',</span>
    <span class="hljs-comment">// certificatePassword: '******',</span>
    <span class="hljs-comment">// certificateSubjectName: ''</span>
    <span class="hljs-comment">// ====windows签名公证相关====start</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">9.<code>nsis</code>window安装程序配置</h3>
<p>这里是定义windows系统的安装程序相关的配置，具体内容可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fconfiguration%2Fnsis" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/configuration/nsis" ref="nofollow noopener noreferrer">点击查看</a>。配置内容如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-attr">nsis</span>: &#123;
      <span class="hljs-comment">// NSIS的路径包括自定义安装程序的脚本。默认为build/installer.nsh</span>
      <span class="hljs-attr">include</span>: <span class="hljs-string">'build/installer.nsh'</span>,
      <span class="hljs-comment">// 是否一键安装，建议为 false，可以让用户点击下一步、下一步、下一步的形式安装程序，如果为true，当用户双击构建好的程序，自动安装程序并打开，即：一键安装（one-click installer）</span>
      <span class="hljs-attr">oneClick</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-comment">// 是否开启安装时权限限制（此电脑或当前用户）</span>
      <span class="hljs-attr">perMachine</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 允许请求提升。 如果为false，则用户必须使用提升的权限重新启动安装程序。</span>
      <span class="hljs-attr">allowElevation</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-comment">// 允许修改安装目录，建议为 true，是否允许用户改变安装目录，默认是不允许</span>
      <span class="hljs-attr">allowToChangeInstallationDirectory</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 卸载时删除用户数据</span>
      <span class="hljs-attr">deleteAppDataOnUninstall</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 安装图标</span>
      <span class="hljs-comment">// installerIcon: 'build/installerIcon_120.ico',</span>
      <span class="hljs-comment">// 卸载图标</span>
      <span class="hljs-comment">// uninstallerIcon: 'build/uninstallerIcon_120.ico',</span>
      <span class="hljs-comment">// 安装时头部图标</span>
      <span class="hljs-comment">// installerHeaderIcon: 'build/installerHeaderIcon_120.ico',</span>
      <span class="hljs-comment">// 创建桌面图标</span>
      <span class="hljs-attr">createDesktopShortcut</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-comment">// 创建开始菜单图标</span>
      <span class="hljs-attr">createStartMenuShortcut</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后这是全部的配置代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue.config.js</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-attr">pluginOptions</span>: &#123;
        <span class="hljs-attr">electronBuilder</span>: &#123;
          <span class="hljs-attr">builderOptions</span>: &#123;
            <span class="hljs-attr">productName</span>: <span class="hljs-string">'这里填写应用名称'</span>,
            <span class="hljs-attr">appId</span>: <span class="hljs-string">'com.example.app'</span>, 
            <span class="hljs-attr">publish</span>: [ <span class="hljs-comment">// 更新服务器地址</span>
              &#123;
                <span class="hljs-attr">provider</span>: <span class="hljs-string">'generic'</span>,
                <span class="hljs-attr">url</span>: <span class="hljs-string">'electron应用的更新地址'</span>
              &#125;
            ],
            <span class="hljs-attr">directories</span>: &#123; <span class="hljs-comment">// 打包之后，包的输出文件夹, 默认地址是dist_electron</span>
              <span class="hljs-attr">output</span>: <span class="hljs-string">'outputFile'</span>
            &#125;,
            <span class="hljs-comment">// asar打包</span>
            <span class="hljs-attr">asar</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">dmg</span>: &#123;
              <span class="hljs-attr">background</span>: <span class="hljs-string">'背景图地址'</span>,
              <span class="hljs-attr">contents</span>: [
                &#123;
                  <span class="hljs-attr">x</span>: <span class="hljs-number">410</span>,
                  <span class="hljs-attr">y</span>: <span class="hljs-number">190</span>,
                  <span class="hljs-attr">type</span>: <span class="hljs-string">'link'</span>,
                  <span class="hljs-attr">path</span>: <span class="hljs-string">'/Applications'</span>
                &#125;,
                &#123;
                  <span class="hljs-attr">x</span>: <span class="hljs-number">130</span>,
                  <span class="hljs-attr">y</span>: <span class="hljs-number">190</span>,
                  <span class="hljs-attr">type</span>: <span class="hljs-string">'file'</span>
                &#125;
              ],
              <span class="hljs-attr">window</span>: &#123;
                <span class="hljs-attr">height</span>: <span class="hljs-number">380</span>,
                <span class="hljs-attr">width</span>: <span class="hljs-number">540</span>
              &#125;,
            &#125;,
            <span class="hljs-attr">mac</span>: &#123;
                <span class="hljs-comment">// 应用程序图标</span>
                <span class="hljs-attr">icon</span>: <span class="hljs-string">'自定义，建议使用png'</span>,
                <span class="hljs-comment">// 应用程序包名 </span>
                <span class="hljs-attr">artifactName</span>: <span class="hljs-string">'$&#123;productName&#125;-$&#123;platform&#125;-$&#123;arch&#125;-$&#123;version&#125;.$&#123;ext&#125;'</span>,
                <span class="hljs-attr">target</span>: [ <span class="hljs-comment">// 要打的包的格式类型设置</span>
                    <span class="hljs-string">'dmg'</span>,
                    <span class="hljs-string">'zip'</span> <span class="hljs-comment">// 这里注意更新的时候，mac只认zip格式的包</span>
                ], 
            &#125;,
            <span class="hljs-attr">win</span>: &#123;
                <span class="hljs-attr">icon</span>: <span class="hljs-string">`256*256的ico格式或png格式文件`</span>,
                <span class="hljs-attr">artifactName</span>: <span class="hljs-string">'$&#123;productName&#125;-$&#123;platform&#125;-$&#123;arch&#125;-$&#123;version&#125;.$&#123;ext&#125;'</span>,
                <span class="hljs-attr">target</span>: [
                    &#123;
                      <span class="hljs-comment">// 打包成一个独立的 exe 安装程序</span>
                      <span class="hljs-attr">target</span>: <span class="hljs-string">'nsis'</span>,
                      <span class="hljs-comment">// 这个意思是打出来32 bit + 64 bit的包，但是要注意：这样打包出来的安装包体积比较大，所以建议直接打32的安装包。</span>
                      <span class="hljs-attr">arch</span>: [
                      <span class="hljs-comment">// 'x64',</span>
                        <span class="hljs-string">'ia32'</span>
                      ]
                    &#125;
                ],
                <span class="hljs-comment">// 打出来的包，自动获取管理员权限，不建议打开</span>
                <span class="hljs-comment">// requestedExecutionLevel: 'highestAvailable',</span>
            &#125;,
            <span class="hljs-attr">nsis</span>: &#123;
              <span class="hljs-comment">// NSIS的路径包括自定义安装程序的脚本。默认为build/installer.nsh</span>
              <span class="hljs-attr">include</span>: <span class="hljs-string">'build/installer.nsh'</span>,
              <span class="hljs-comment">// 是否一键安装，建议为 false，可以让用户点击下一步、下一步、下一步的形式安装程序，如果为true，当用户双击构建好的程序，自动安装程序并打开，即：一键安装（one-click installer）</span>
              <span class="hljs-attr">oneClick</span>: <span class="hljs-literal">false</span>,
              <span class="hljs-comment">// 是否开启安装时权限限制（此电脑或当前用户）</span>
              <span class="hljs-attr">perMachine</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-comment">// 允许请求提升。 如果为false，则用户必须使用提升的权限重新启动安装程序。</span>
              <span class="hljs-attr">allowElevation</span>: <span class="hljs-literal">false</span>,
              <span class="hljs-comment">// 允许修改安装目录，建议为 true，是否允许用户改变安装目录，默认是不允许</span>
              <span class="hljs-attr">allowToChangeInstallationDirectory</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-comment">// 卸载时删除用户数据</span>
              <span class="hljs-attr">deleteAppDataOnUninstall</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-comment">// 安装图标</span>
              <span class="hljs-comment">// installerIcon: 'build/installerIcon_120.ico',</span>
              <span class="hljs-comment">// 卸载图标</span>
              <span class="hljs-comment">// uninstallerIcon: 'build/uninstallerIcon_120.ico',</span>
              <span class="hljs-comment">// 安装时头部图标</span>
              <span class="hljs-comment">// installerHeaderIcon: 'build/installerHeaderIcon_120.ico',</span>
              <span class="hljs-comment">// 创建桌面图标</span>
              <span class="hljs-attr">createDesktopShortcut</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-comment">// 创建开始菜单图标</span>
              <span class="hljs-attr">createStartMenuShortcut</span>: <span class="hljs-literal">true</span>
            &#125;
          &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是关于electron-builder的一些基础配置，大家可以直接复制，修改下文件地址、名称可直接使用。关于electron-builder中的配置还有很多，在做mac签证和公证的时候或者引入一些node文件时候，也需要在这里面进行配置，后续会逐步的给大家完善讲解。</p>
<h1 data-id="heading-11">三、后记</h1>
<p>这里再给大家分享一段关于nsis的自定义配置，可以实现指定路径安装的。</p>
<pre><code class="hljs language-nsh copyable" lang="nsh">// installer.nsh
!macro preInit
    SetRegView 64
    ReadRegStr $0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\&#123;GUID&#125;" "UninstallString"
    $&#123;If&#125; $0 == ''
        WriteRegStr HKLM "$&#123;INSTALL_REGISTRY_KEY&#125;" InstallLocation "C:\Program Files (x86)\hello"
    $&#123;Endif&#125;
    SetRegView 32
    ReadRegStr $0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\&#123;GUID&#125;" "UninstallString"
    $&#123;If&#125; $0 == ''
        WriteRegStr HKLM "$&#123;INSTALL_REGISTRY_KEY&#125;" InstallLocation "C:\Program Files (x86)\hello"
    $&#123;Endif&#125;
!macroend
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接在<code>nsis.include</code>配置对应路径引入就好了。</p>
<p>本篇完结！ 撒花！ 感谢观看！ 希望能帮助到你！</p></div>  
</div>
            