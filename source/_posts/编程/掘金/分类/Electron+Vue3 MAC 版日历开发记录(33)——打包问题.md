
---
title: 'Electron+Vue3 MAC 版日历开发记录(33)——打包问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bda4c24da0b147988ec74034af56dcc5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 07:24:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bda4c24da0b147988ec74034af56dcc5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Mac APP 打包的问题汇总和整理。通过简单的配置，提交 Github：</p>
<pre><code class="copyable">const now = new Date;
const buildVersion = `$&#123;now.getFullYear() - 2020&#125;.$&#123;now.getMonth() - 6&#125;.$&#123;now.getDate()&#125;`;
const id = 'cn.coding01.fanlycalendar';
/**
 * @type &#123;import('electron-builder').Configuration&#125;
 * @see https://www.electron.build/configuration/configuration
 */
const config = &#123;
  appId: id,
  directories: &#123;
    output: 'dist',
    buildResources: 'buildResources',
  &#125;,
  files: [
    'packages/**/dist/**',
  ],
  extraMetadata: &#123;
    version: buildVersion,
  &#125;,
  mac: &#123;
    target: 'mas',
    extendInfo: &#123;
      CFBundlePackageType: 'APPL',
      CFBundleIdentifier: id,
      CFBundleShortVersionString: buildVersion,
    &#125;,
  &#125;,
&#125;;

module.exports = config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自动打包出 <code>pkg</code> 安装包：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bda4c24da0b147988ec74034af56dcc5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>直接提交 Transporter：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c95207e157645adb4e7fbd2cf72420f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>额，果然不会很顺利～ 出现问题了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef503acb72ca4f0097e3dd410d327d3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">ICNS 图标问题</h2>
<p>第一个问题，关于 icon 的，这个之前使用线上工具制作的，估计缺少 icon，后来找了一个 workflow，特别好用，直接集成到右键菜单栏了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fdb435a8d0f4368b1103d304b9df111~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一键生成，完美，具体代码查看：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmolcik%2FPNG-to-ICNS-right-click-converter%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/molcik/PNG-to-ICNS-right-click-converter/releases" ref="nofollow noopener noreferrer">github.com/molcik/PNG-…</a></p>
<h2 data-id="heading-1">3rd Party Mac Developer Installer 证书问题</h2>
<p>第二个问题，我们在线打包是使用的 <code>Developer ID Application: *** (***)</code>，在提交到服务器上的，需要重新使用 <code>3rd Party Mac Developer Installer: *** (***)</code> code sign：</p>
<pre><code class="copyable">Productsign --sign "3rd Party Mac Developer Installer: *** (***)" "/Users/yemeishu/Downloads/FanlyCalendar-1.0.23.pkg" "/Users/yemeishu/Downloads/FanlyCalendar-1.0.23_sign.pkg"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决以上两个问题后，我们看看提交效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1660fea08b4855b7bab5706f8f5794~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">app-sandbox 问题</h2>
<pre><code class="copyable">ERROR ITMS-90296: "App sandbox not enabled. The following executables must include the "com.apple.security.app-sandbox" entitlement with a Boolean value of true in the entitlements property list: [( "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Electron Framework.framework/Versions/A/Helpers/chrome_crashpad_handler", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/FanlyCalendar Helper (GPU).app/Contents/MacOS/FanlyCalendar Helper (GPU)", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/FanlyCalendar Helper (Plugin).app/Contents/MacOS/FanlyCalendar Helper (Plugin)", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/FanlyCalendar Helper (Renderer).app/Contents/MacOS/FanlyCalendar Helper (Renderer)", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/FanlyCalendar Helper.app/Contents/MacOS/FanlyCalendar Helper", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Squirrel.framework/Versions/A/Resources/ShipIt", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/MacOS/FanlyCalendar", "cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Resources/app.asar.unpacked/node_modules/esbuild/bin/esbuild" )] Refer to App Sandbox page at https://developer.apple.com/documentation/security/app_sandbox for more information on sandboxing your app."
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个主要是没使用 <code>entitlements</code>，配置：</p>
<pre><code class="copyable">    <key>com.apple.security.app-sandbox</key>
    <true/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我们需要引入 <code>entitlements.mas.plist</code>：</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.application-groups</key>
    <string>***</string>
    <key>com.apple.security.files.user-selected.read-write</key>
    <true/>
    <key>com.apple.security.network.client</key>
    <true/>
  </dict>
</plist>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和 <code>entitlements.mas.inherit.plist</code>：</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.inherit</key>
    <true/>
  </dict>
</plist>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入后，出现新的问题：</p>
<pre><code class="copyable">Dear Developer,

We identified one or more issues with a recent delivery for your app, "FanlyCalendar" 1.0.23 (1.0.23). Please correct the following issues, then upload again.

ITMS-90238: Invalid Signature - The nested app bundle Mantle at path FanlyCalendar.app/Contents/Frameworks/Mantle.framework has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Mantle.framework/Versions/A: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The nested app bundle ReactiveObjC at path FanlyCalendar.app/Contents/Frameworks/ReactiveObjC.framework has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/ReactiveObjC.framework/Versions/A: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The nested app bundle Squirrel at path FanlyCalendar.app/Contents/Frameworks/Squirrel.framework has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Squirrel.framework/Versions/A: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The executable at path FanlyCalendar.app/Contents/Frameworks/Electron Framework.framework/Versions/A/Helpers/chrome_crashpad_handler has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Electron Framework.framework/Versions/A/Helpers/chrome_crashpad_handler: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The executable at path FanlyCalendar.app/Contents/Frameworks/Squirrel.framework/Versions/A/Resources/ShipIt has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Frameworks/Squirrel.framework/Versions/A/Resources/ShipIt: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The executable at path FanlyCalendar.app/Contents/Resources/app/node_modules/esbuild/bin/esbuild has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Resources/app/node_modules/esbuild/bin/esbuild: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

ITMS-90238: Invalid Signature - The executable at path FanlyCalendar.app/Contents/Resources/app/node_modules/fsevents/fsevents.node has following signing error(s): valid on disk /Volumes/data01/app_data/awf/mz_17116261486138838905dir/mz_4007830068208133740dir/cn.coding01.fanlycalendar.pkg/Payload/FanlyCalendar.app/Contents/Resources/app/node_modules/fsevents/fsevents.node: satisfies its Designated Requirement test-requirement: code failed to satisfy specified code requirement(s) . Refer to the Code Signing and Application Sandboxing Guide at http://developer.apple.com/library/mac/#documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html and Technical Note 2206 at https://developer.apple.com/library/mac/technotes/tn2206/_index.html for more information.

Best regards,

The App Store Team
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">code sign 问题</h2>
<p>类似这样的问题，基本都是 code sign 打包的问题，我们尝试在本地 <code>npm run compile</code>，打包成 <code>.app</code> 格式，然后再使用 <code>codesign</code> 对 app 和引用的所有第三方插件进行 code sign：</p>
<pre><code class="copyable">#!/bin/bash

# 应用名称
APP="FanlyCalendar"
# 应用路径
APP_PATH="/***/fanlymenu2/dist/Mac/FanlyCalendar.app"
# 生成安装包路径
RESULT_PATH="./$APP.pkg"
# 开发者应用签名证书
APP_KEY="3rd Party Mac Developer Application: *** (***)"
INSTALLER_KEY="3rd Party Mac Developer Installer: *** (***)"
# 授权文件路径
CHILD_PLIST="/***/fanlymenu2/buildResources/entitlements.mas.inherit.plist"
PARENT_PLIST="/***/buildResources/entitlements.mas.plist"

FRAMEWORKS_PATH="$APP_PATH/Contents/Frameworks"

codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Electron Framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Helpers/chrome_crashpad_handler"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libEGL.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libffmpeg.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libGLESv2.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libswiftshader_libEGL.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libswiftshader_libGLESv2.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libvk_swiftshader.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Mantle.framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/ReactiveObjC.framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Squirrel.framework/Versions/A/Resources/ShipIt"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Squirrel.framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper.app/Contents/MacOS/$APP Helper"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper.app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (Renderer).app/Contents/MacOS/$APP Helper (Renderer)"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (Renderer).app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (GPU).app/Contents/MacOS/$APP Helper (GPU)"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (GPU).app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (Plugin).app/Contents/MacOS/$APP Helper (Plugin)"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper (Plugin).app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$APP_PATH/Contents/Resources/app/node_modules/esbuild/bin/esbuild"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$APP_PATH/Contents/Resources/app/node_modules/fsevents/fsevents.node"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$APP_PATH/Contents/MacOS/$APP"
codesign -s "$APP_KEY" -f --entitlements "$PARENT_PLIST" "$APP_PATH"

productbuild --component "$APP_PATH" /Applications --sign "$INSTALLER_KEY" "$RESULT_PATH"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过程效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfefbe50d0024bb59b0727889f008642~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后再利用 <code>Transporter</code> 上传我们打包好的 <code>FanlyCalendar.pkg</code>，同时也可以在服务器后台看到我们得构建版本了。</p>
<p>如果不出问题，我们就可以补充介绍和信息，提交审核了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c0693c2158427a8c946b6795cecbbd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Mark 下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/850f15739dff48358afae169c6e8e3a3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">总结</h2>
<p>无论审核结果怎么样，至少到目前为止，完成了第一阶段的开发了，接近两个月的自学，再加上晚上工作之余的时间，给自己打 80 分！</p>
<p>未完待续！</p></div>  
</div>
            