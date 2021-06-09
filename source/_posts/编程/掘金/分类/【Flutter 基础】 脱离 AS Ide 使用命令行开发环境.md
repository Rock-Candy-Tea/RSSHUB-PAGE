
---
title: '【Flutter 基础】 脱离 AS Ide 使用命令行开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe65eafb94b543fd923a39f82350034a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 03:13:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe65eafb94b543fd923a39f82350034a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
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
<p><em>为了搞清楚是否能够脱离 Android Studio Ide 来安装所需环境，我还是下了一个 Android Studio Ide</em></p>
<p>ASI 官方下载：<a href="https://developer.android.google.cn/studio" target="_blank" rel="nofollow noopener noreferrer">android-studio-ide-windows.exe</a></p>
<p>在安装的过程中我把一些重要的安装执行命令记录了下来</p>
<p>最后我把这些信息整理后发现，只需要2个支持环境的 tools 就可以脱离 Android Studio Ide 开发了。<br>
<em>ASI 官网也有提供解压包下载</em></p>
<h3 data-id="heading-1">所需包</h3>
<ul>
<li><a href="https://dl.google.com/android/repository/sdk-tools-windows-4333796.zip" target="_blank" rel="nofollow noopener noreferrer">SDK toots</a></li>
<li><a href="https://dl.google.com/android/repository/platform-tools_r29.0.1-windows.zip" target="_blank" rel="nofollow noopener noreferrer">platform-tools</a></li>
</ul>
<p>首先，将 SDK tools 解压至 你所指定的文件夹\Android SDK 下</p>
<p>然后再将 platform-tools 解压至 你所指定的文件夹\Android SDK 下</p>
<pre><code class="hljs language-text copyable" lang="text">你的文件夹\Android SDK
├─ platform-tools
└─ toots
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">环境变量配置</h3>
<p>然后就需要设置系统环境变量：</p>
<pre><code class="hljs language-text copyable" lang="text">ANDROID_HOME="你的文件夹\Android SDK"
PATH="你的文件夹\Android SDK\tools"
PATH="你的文件夹\Android SDK\tools\bin"
PATH="你的文件夹\Android SDK\platform-tools"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完成后就可以使用与 android 相关的命令了，打开命令行 -> 输入 <code>android</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">android
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe65eafb94b543fd923a39f82350034a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（android 命令）</em></p>
<h2 data-id="heading-3">SDK 管理器</h2>
<p>打开命令行 -> 输入 <code>sdkmanager --list</code></p>
<p>这是 SDK 的管理器 <em>（注意 sdkmanager 严重依赖 jdk 1.8.0 过高或者过低都会报错）</em></p>
<pre><code class="hljs language-shell copyable" lang="shell">sdkmanager --list
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候你会发现，所有的 Android Studio 的支持的各个版本的 SDK、API 都有了</p>
<p>但是如果你想要使用 sdkmanager 来管理这些东西 <strong>对不起！还是不行！</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9434d86c985b4f08a34784989fce85e4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（sdk 的管理器）</em></p>
<h3 data-id="heading-4">缺少 repositories.cfg</h3>
<p>你需要找到 C:\Users\XXX\.android\</p>
<p>然后<strong>创建一个名为 repositories.cfg 的文件</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e5ae6022d7044c79afce498f38fcc0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（创建 repositories.cfg 文件）</em></p>
<p>然后命令行 -> 输入 <code>sdkmanager "platforms;android-29"</code></p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> android-29 为安卓版本</span>
sdkmanager "platforms;android-29"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等待传输下载完成，你就可以使用基本的（非模拟器）的 Android 开发环境了。</p>
<p>如果你喜欢的话还可以顺手更新一下：</p>
<pre><code class="hljs language-shell copyable" lang="shell">sdkmanager --update
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell">android update sdk
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来只要连接上手机，打开开发者模式就可以进行开发了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4665ac84b4349129d598c9ea0e9907f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这里识别出了我使用的手机是 MI 5 - 小米5</strong></p>
<p>然后执行命令 <code>flutter run</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">flutter run
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97d760ea00af47c0b08fb673d0a16191~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（flutter deome）</em></p>
<h2 data-id="heading-5">最后</h2>
<ul>
<li>如果你只想要一个可以连接真机开发环境，那么这篇文章完全可以帮助你。因为这里全部工具完全安装下来只用了 336Mb 空间。</li>
<li>但是如果你想要通过 Android 虚拟机环境开发，那么还是乖乖的照着官方要求来使用 Android Studio Ide 来进行开发。</li>
<li>当然你想要 Geeks 一下，使用命令行创建Android 虚拟机开发环境也是可以的。</li>
</ul></div>  
</div>
            