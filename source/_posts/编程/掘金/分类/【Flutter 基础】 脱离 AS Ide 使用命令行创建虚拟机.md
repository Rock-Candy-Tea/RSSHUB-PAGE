
---
title: '【Flutter 基础】 脱离 AS Ide 使用命令行创建虚拟机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab6836c2bf944dd6ad74540ee20e4126~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:18:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab6836c2bf944dd6ad74540ee20e4126~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><em>注：本文从个人公众号（岛前屿端）中迁移重新发布</em></p>
<blockquote>
<p>Flutter 是谷歌的移动 UI 框架，可以快速在 iOS 和 Android 上构建高质量的原生用户界面。 Flutter 可以与现有的代码一起工作。</p>
</blockquote>
<hr>
<h2 data-id="heading-0">为什么要脱离 Android Studio Ide？</h2>
<p><strong>为什么我想着要脱离 Android Studio Ide 来写 Flutter？</strong></p>
<blockquote>
<p>因为，当所有 Android Studio Ide 的所需环境以及 SDK 安装完成后大概占用 <strong>6~8Gb</strong> 磁盘空间。<br>
这对我来说，实在是 <strong>太！恐！怖！了！</strong><br>
所以我就开始尝试脱离 Android Studio Ide 只使用 VS Code 来开发 Flutter。<br>
好在 <strong>Flutter 官方是支持 VS Code 的</strong>。<br>
具体配置和插件详见：<a href="https://flutterchina.club/" target="_blank" rel="nofollow noopener noreferrer">flutterchina.club</a></p>
</blockquote>
<h2 data-id="heading-1">如何用命令行创建 Android 虚拟机？</h2>
<p><strong>首先要保证 Android 命令是可用的</strong>，相关配置、命令、环境问题参考：<a href="https://juejin.cn/post/6971750152784576525" target="_blank">【Flutter 基础】 脱离 AS Ide 使用命令行开发环境</a></p>
<p>但如果你要用<strong>命令行创建 Android 虚拟机</strong>的话，那就需要使用 <code>sdkmanager</code> 更新一下所需的支持包</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> emulator 和 build-tools;29.0.0 （这里我以 29 为安卓版本为例）</span>
sdkmanager "emulator" "build-tools;29.0.0"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果熟悉使用命令行的不会有太大问题，这里照顾一下<strong>不熟悉使用命令行又想装逼的朋友</strong>，简单解释一下</p>
<h3 data-id="heading-2">旧版本命令</h3>
<p>创建一个 avd 虚拟机 <em>（旧版本命令）</em></p>
<pre><code class="hljs language-shaell copyable" lang="shaell"># -n 虚拟机名称
# -t targetID
android create avd -n tAndroid -t 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何得到 targetID？ 命令行 -> 输入 <code>android list target</code> 就会列出已下载在本地的 <strong>Android API</strong> 版本了</p>
<pre><code class="hljs language-shell copyable" lang="shell">android list target
<span class="copy-code-btn">复制代码</span></code></pre>
<p>旧版本的命令，如果执行的话就会报错了。并且告诉你 <code>flag '-t' is not valid for 'create avd'.</code> -t 的标记对创建 avd 无效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab6836c2bf944dd6ad74540ee20e4126~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（旧版本命令-执行错误）</em></p>
<h3 data-id="heading-3">现版本命令</h3>
<p>那新命令要如何使用呢？基本上未变更太多
<em>-t 标记变更为 -k 标记</em>，-k 的标记就是说，将要使用哪个版本的系统镜像包和API</p>
<pre><code class="hljs language-shell copyable" lang="shell">android create avd -n tAndroid -k 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">创建虚拟机</h3>
<p>如果之前你有下载了对应的系统 API <em>（platforms;android-29）</em> 的话，那么这条命令执行后会告诉你</p>
<p>需要：<strong>system-images;android-29;google_apis;x86_64</strong>，即安卓系统镜像以及相关 API</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b73d435be2e46e2a944d4f9c101f59f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（命令提示缺少相关的镜像）</em></p>
<p>那么就来下载这个包</p>
<pre><code class="hljs language-shell copyable" lang="shell">sdkmanager "system-images;android-29;google_apis;x86_64"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载完成后，再次执行命令，此时 -k 的参数为下载的镜像全名，<strong>别忘了双引号</strong></p>
<pre><code class="hljs language-shell copyable" lang="shell">android create avd -n tAndroid -k "system-images;android-29;google_apis;x86_64"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候会问你是否需要创建自定义的硬件配置？默认是 <strong>[no]</strong> 直接回车就好，稍等一下虚拟机就配置完成了。
默认创建的虚拟机是全 API 支持，但是 <strong>屏幕宽度为 320px</strong> 且 <strong>dpr 为 1</strong>。</p>
<p>稍等过后，虚拟机就创建完成了。</p>
<h2 data-id="heading-5">如何启动虚拟机</h2>
<p>还记得一开始就要下载的支持包 <strong>emulator</strong> 吗？启动 <strong>Android 虚拟机</strong> 的话就需要使用它了。</p>
<p>不知道如何使用？OK，没问题。命令行 -> 输入 <strong>emulator</strong>，结果会告诉你使用 @虚拟机名称 或者 -avd 虚拟机名称。</p>
<pre><code class="hljs language-shell copyable" lang="shell">emulator @tAndroid 
<span class="hljs-meta">#</span><span class="bash"> or</span>
emulator -avd tAndroid
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次启动大概率会遇到如下错误</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8456939a3874966947a476dd1e4f98a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过不要着急，这时候还需要做一件事：</p>
<ol>
<li>进入你配置的 <strong>SDK 文件夹的位置</strong>，找到 emulator 文件夹下的 <strong>emulator.exe</strong>，右键创建快捷方式。</li>
<li>然后剪切一下，在 SDK 文件夹下找到 tools 文件夹，进入右键粘贴。</li>
</ol>
<p>然后你会发现这里也有一个 <strong>emulator.exe</strong> ！！！这是什么情况？真假孙悟空？！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a2befb83f904cfaab841065139e0da4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不要慌！！！只需要把<strong>原 emulator.exe 改名</strong>，<strong>新 emulator.exe 快捷方式去掉</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aef37f8e3d294d2ba1f2337e7e4addab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后重新执行</p>
<pre><code class="hljs language-shell copyable" lang="shell">emulator -avd tAndroid
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>一定会遇到如下错误</strong>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6306bea9db1848638e3a206fda9c5a03~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">WHPX & HAXM</h3>
<p><strong>大兄弟，你怎么又报错了？</strong></p>
<p><strong>WHPX 是什么？</strong></p>
<p><strong>HAXM 又是什么？</strong></p>
<p>不要着急，仔细看提示：</p>
<blockquote>
<p>使用 <strong>仿真</strong> <em>（虚拟机）</em> <strong>需要硬件加速</strong><br>
请确保 Windows <strong>虚拟机监控程序平台</strong> <em>（WHPX）</em> 已正确安装并可用<br>
CPU加速状态：此计算机上未安装 <strong>硬件加速执行管理器</strong> <em>（HAXM）</em>
如果您使用的是 Intel CPU：请检查BIOS中是否启用了<strong>虚拟化</strong>，以及 <strong>HAXM</strong> 是否已安装并可用<br>
如果您使用 <strong>AMD CPU</strong> 或需要与基于 <strong>Hyper-V-based</strong> 的应用程序（如Docker）一起运行，我们建议您使用 Windows 系统管理程序平台</p>
</blockquote>
<p><strong>So，看完之后知道 WHPX & HAXM 是什么了么？</strong></p>
<p>这时候只要下载 HAXM 支持包，以及在 BIOS 中开启主板虚拟化支持就可以解决问题啦！</p>
<blockquote>
<p><strong>google/bing/百度</strong> 一下你自己主板的虚拟化支持的选项在哪里，然后开启就 OK！</p>
</blockquote>
<h3 data-id="heading-7">下载 HAXM 支持包</h3>
<pre><code class="hljs language-shell copyable" lang="shell">sdkmanager "extras;intel;Hardware_Accelerated_Execution_Manager"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开启完成后，在你的SDK文件夹下找到 <strong>extras\intel\Hardware_Accelerated_Execution_Manager</strong></p>
<p>双击安装即可 <code>如果安装失败则是因为虚拟化支持未开启成功）</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72878df61d8d46c6a21f744f265481a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408307b617ca4ea8b4c5392a498e47ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装成功后，再次执行 -> <strong>emulator @tAndroid</strong> 稍作等待</p>
<pre><code class="hljs language-shell copyable" lang="shell">emulator -avd tAndroid
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ab8e441b6bc4dcba20dfa8ec467e841~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（启动虚拟机中）</em></p>
<h2 data-id="heading-8">激动人心的时刻就要到来了！</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe5bf0586e2c4f729525b967446f40db~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不要激动！虽然只是成功创建并启动了虚拟机而已。</p>
<p>但是，能否建立与开发项目的连接还是个问题。</p>
<p>执行如下设备检查命令</p>
<pre><code class="hljs language-shell copyable" lang="shell">adb devices
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell">flutter devices
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfb74dd315324c13b00f0c8a0399e236~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>两个都可以识别出来是 Android 虚拟机了，那么就可以使用虚拟机进行开发了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ca25e7b9bf54acba084de31d42f9258~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结</h2>
<ul>
<li>踩了坑就要一步一步记录下来，以便之后用来复盘过程。</li>
<li>在出现问题的时候，千万不要惊慌，错误提示大多数时候都会明确告诉你发生了什么。</li>
<li>学会并且合理使用搜索工具，能让你减少看到垃圾文章的几率。</li>
</ul>
<p>前置阅读：<a href="https://juejin.cn/post/6971750152784576525" target="_blank">【Flutter 基础】 脱离 AS Ide 使用命令行开发环境</a></p></div>  
</div>
            