
---
title: """""""""""'iOS Swift5从0到1系列（一）：删除main.storyboard'"""""""""""
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Tue, 23 Feb 2021 01:14:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62b0329912134827a9b0d1f616fba78f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>昨晚和朋友聊天时，聊到了 Swift5.x，虽然现在的项目是混编（OC+Swift），但是想练手个纯 Swift 的项目，考虑过 SwiftUI，但是 iOS 有限制，只支持 iOS13，考虑国内的用户和场景，因此打算开个 Swift5.x + UIKit 的系列。关于该系列，网上杂乱不堪，至于讲的好的呢，还要收费；当然，我不能说别人不对，毕竟人家花了时间、精力；同样，我虽然没那么高尚，一方面自己练手，一方面也想分享给大家，一起交流，一起进步。</p>
<h2 data-id="heading-1">二、新建项目</h2>
<h3 data-id="heading-2">2.1、工欲善其事，必先利其器</h3>
<p>正式创建项目前，大家请升级 macOS 至最新（Big Sur），然后再去 App Store 升级 Xcode，并且安装 xcode 命令行工具：</p>
<pre><code class="copyable">$ xcode-select --install
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.2、创建项目</h3>
<ul>
<li>打开 Xcode，选择『Create a new Xcode project』</li>
</ul>
<p><img alt="create.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62b0329912134827a9b0d1f616fba78f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>选择『iOS - App』</li>
</ul>
<p><img alt="app.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed52ef20419b490b8bb0cca3860a13ea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>选择『Swift + UIKit』，别选择『SwiftUI』了</li>
</ul>
<p><img alt="swift+uikit.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf1c2b695ba497a84582e07439f2011~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>点击『create』就行，至于代码控制可以先无视</li>
</ul>
<p><img alt="succ.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/094574ef03004a0dbbfc200df08c475c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>创建成功如下图</li>
</ul>
<p><img alt="proj.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d2bcf9264d0481681188e16ea200363~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">三、手写UI，删除 Main.storyboard</h2>
<h3 data-id="heading-5">3.1、删除 Main.storyboard 文件</h3>
<ul>
<li>选择『Move to Trash』</li>
</ul>
<p><img alt="delete main-sb.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c5711a5e4444ef81a36d25cc44f20f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3.2、修改『xcodeproject配置』</h3>
<ul>
<li>选择『FirstTrain』</li>
</ul>
<p><img alt="config.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c560f4de99142aea9f94f565a534753~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>删除『Main』，并勾选掉『iPad』、『Landscape Left』、『Landscape Right』</li>
</ul>
<p><img alt="adjust.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0191888500534d6982eff6468b5df6f2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.3、修改『Info.plist』</h3>
<p><img alt="plist.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ab717ca80fb44feb91923a4f5a1f648~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3.4、修改『AppDelegate.swift』</h3>
<p><img alt="simulator.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/629e5ce1eb254f6eb9a4984d0be4abcd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>我的最新的版本，多了『Lifecycle』，需要将其注释掉</li>
</ul>
<p><img alt="modify appdelegate.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1a515f7573441f0accebac4b0655bb2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>注释后如下</li>
</ul>
<p><img alt="mask.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e540816722714e18aacd98a57045d562~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后，快捷键『command + B』编译一下（如果之前有编译，可以先『Product -> Clean Build Folder』一下）。</p>
<h2 data-id="heading-9">四、创建第一个ViewController</h2>
<h3 data-id="heading-10">4.1、修改『AppDelegate.swift』,创建 UIWindow</h3>
<p><img alt="uiwindow.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcab84b58f87409eaa9b27a4baae7ce9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">4.2、修改『ViewController』，添加背景色</h3>
<p><img alt="color.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/881000ee52114268b72dad4a1bc72ae1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">4.3、选择合适的模拟器</h3>
<p><img alt="simulator.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7818455fc0b54ce1b17495e9ec9d5770~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">4.4、编译运行</h3>
<p><img alt="run.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/998a15fb49c64ddab402677e58c62dcb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>OK！大功告成！</p>
<h2 data-id="heading-14">五、总结</h2>
<p>有人会说，现在 storyboard 这么方便，为何还用这么传统老式的手写代码方式？</p>
<p>有这么几个方面原因我想和大家分享一下吧：</p>
<ol>
<li>大学时期，我用过各种开发工具：TurboC、VC6（Win32、MFC）、C++Builder；然后，你会发现，如果你一上手就用各种拖、拉、拽，开发速度确实很快，但你可能会错过很多原理性的东西；相反，如果你手写代码熟练，那么再用工具就会非常的得心应手；</li>
<li>大家都是团队协作，因此，手写代码，文件冲突也非常容易解决，但是用了 storyboard、xib 遇到冲突，解决起来就很麻烦，虽然苹果也一直在改进这块；</li>
<li>本篇重点是练手，顺带分享以及交流，因此，手写代码容易让大家看起来更直观（放心，我会写备注的）</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            