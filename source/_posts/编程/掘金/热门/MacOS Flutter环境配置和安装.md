
---
title: 'MacOS Flutter环境配置和安装'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e75dcdbe0eea4a3b96a88b0430351fbc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 02:04:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e75dcdbe0eea4a3b96a88b0430351fbc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>由于本人是一名iOS开发，所以本文主要讲的就是在MacOS环境下Flutter的安装流程，中间也踩了一部分坑，现在把我亲身来配置的步骤贴出来
​</p>
<h4 data-id="heading-0">1. 下载Flutter SDK包</h4>
<p>直接打开<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2Fdocs%2Fget-started%2Finstall%2Fmacos" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/docs/get-started/install/macos" ref="nofollow noopener noreferrer">官网iOS下载地址</a>，找到这个下载，我下载的版本是macos_2.2.3
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e75dcdbe0eea4a3b96a88b0430351fbc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">2.解压SDK</h4>
<p>我是下载下来之后直接解压，没有用命令，感觉双击一下就能解决的问题，搞这么复杂，奇奇怪怪。我双击解压之后直接拖到我的用户下面。当然啦，有的确实喜欢用命令行，使用命令的话, 可以直接复制。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">cd /Users/DaGongRen
unzip ~/Downloads/flutter_macos_2<span class="hljs-number">.2</span><span class="hljs-number">.3</span>-stable.zip
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3.配置环境变量</h4>
<p>刚开始的时候我是按照教程一步步来的。首先打开终端，进入存放Flutter的路径</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">cd /Users/DaGongRen/flutter
vim ~/.bash_profile
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用vim打开这个<code>.bash_profile</code>的文件，在这个文件里面添加配置，这个文件其实是个隐藏文件，我们可以使用<code>shift + command + .</code>打开隐藏文件，我的flutter放在和这个<code>.bash_profile</code>在同一级目录之下。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61484c784d97410b9efa2130ca12d623~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我是不太喜欢使用命令行，我就直接打开这个文件，在这个文件里面添加上<code>PATH</code></p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">export</span> PATH=/Users/DaGongRen/flutter/bin:$PATH
<span class="hljs-keyword">export</span> PATH=/Users/DaGongRen/flutter/bin/cache/dart-sdk/bin:$PATH
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后关闭，接着重新打开终端</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">cd /Users/DaGongRen/flutter
flutter -h
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着出现如下界面，说明环境配置成功了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67f86cf943c74a64b26a039f245134b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">4.检查是否安装成功</h4>
<p>打开终端，检查是否安装成功</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">cd /Users/DaGongRen/flutter
flutter --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果显示如下，则表明安装成功
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a290fbe2bf54f78a21de133037865e8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我这里是提示：<code>command not found</code>,最后怎么解决的呢？最后我是在<code>.zshrc</code>这个隐藏文件中配置的<code>PATH</code> 而不是步骤3的<code>.bash_profile</code>文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9e10d24f795468c961f1a6117d3fe93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着，来验证下是否所有的依赖都已经安装完毕！
​</p>
<h4 data-id="heading-4">5.安装诊断</h4>
<p>通过运行<code>flutter doctor</code>命令来诊断是否存在未安装或者未安装成功的<code>Flutter</code>开发所需要的依赖选项。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ef3c932f2c54341bb8e29010bb28f25~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行我们可以看到<code>Unable to locate Android SDK.</code>那我们就去下载吧<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.google.cn%2Fstudio" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.google.cn/studio" ref="nofollow noopener noreferrer">Android Studio 下载地址</a>，温馨提示下载完成之后打开，然后会提示你下载一堆资源，你要选择同意，内容比较大，需要等待一段时间。
完了之后，继续<code>flutter doctor</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9e010f2b3284f09aa6b7f2229c679f8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>报红的地方意思说的是没有Java运行环境，接续下载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.java.com%2Fzh-CN%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.java.com/zh-CN/download/" ref="nofollow noopener noreferrer">java 下载地址</a>
下载完成之后，继续<code>flutter doctor</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38052b657ab342d993ba3b96ddc26e37~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照提示的要求继续<code>flutter doctor --android-licenses</code>，接下来就出现了好多次这个提示，直接输入y</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76fbc73cb3b94c7d8d3f5a620fc4aa82~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一顿操作之后继续<code>flutter doctor</code>继续提示我</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb5600e6c5504763873772786a8aabf1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我又接着继续<code>flutter doctor --android-licenses</code>结果出现了这个玩意</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b97582c4df347a4a99189d040efc793~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后找到了一个大佬的回答<a href="https://link.juejin.cn/?target=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2021%2F05%2F31%2Fflutter-cn-doctor-android-license-java-erro%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://clay-atlas.com/blog/2021/05/31/flutter-cn-doctor-android-license-java-erro/" ref="nofollow noopener noreferrer">直达大佬的心底</a>
步骤我借花献佛贴一下，大致是，首先打开<code>Android Studio</code>找到<code>Preferences</code>,把这个选项勾选上应用，然后会下载，需要等待一会时间，下载完成之后关闭。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a83869128244e61925a25cb8c34559b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着最后来执行一次<code>flutter doctor</code>,ok，终于搞定了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdf06a4a76494accb2fdd4c9830a423d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            