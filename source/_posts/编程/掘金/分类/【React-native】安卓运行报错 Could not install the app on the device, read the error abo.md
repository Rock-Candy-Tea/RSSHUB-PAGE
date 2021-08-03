
---
title: '【React-native】安卓运行报错 Could not install the app on the device, read the error abo'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/904f7202baac4f2a92fdd27647069e28~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 00:24:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/904f7202baac4f2a92fdd27647069e28~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>RN在IOS运行一切正常，准备去Android端测试发现报错，但是我设备启着的，于是乎根据提示./gradlew installDebug，却说我Permission denied</p>
</blockquote>
<hr>
<h3 data-id="heading-0">错误截图： </h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/904f7202baac4f2a92fdd27647069e28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6992116749357629448" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-1">可能原因一</h3>
<p><strong>gradlew权限不足导致react-native run-android失败</strong></p>
<h3 data-id="heading-2">解决方案</h3>
<p>执行如下命令：</p>
<pre><code class="copyable">chmod +x gradlew
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6992116749357629448" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-3">可能原因二</h3>
<p>安卓运行后报错，在android/app/src/main/下创建assets文件夹，运行如下脚本即可。</p>
<pre><code class="copyable">react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://juejin.cn/post/6992116749357629448" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-4">可能原因三</h3>
<p>情况： 如果第一次运行（使用 react-native run-android）可以启动，双击R时不显示且报错。</p>
<p>参考：我虚拟机之前由于抓包，设置代理，把代理关掉即可，供参考。</p>
<hr>
<h3 data-id="heading-5">可能原因四</h3>
<p>情况：如果你用 Genymotion 模拟器出现这个情况，进行如下设置：</p>
<p>设置你的 ADB tool 工具为本地 sdk 自带的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1542f5eb5ab482395638251722584e9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img src="https://juejin.cn/post/6992116749357629448" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>不知道你是不是由于以上原因造成，如果能帮到你，就太好了。</p>
<p>如果不是的话，解决完了之后，可以在下方留言，供更多人参考，感谢Thanks♪(･ω･)ﾉ。</p></div>  
</div>
            