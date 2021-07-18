
---
title: '让你 vscode 写代码效率更高的技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91c399966f9d472582aadfc0efa09207~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 07:55:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91c399966f9d472582aadfc0efa09207~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>vscode 是我们写代码常用的编辑器，它的功能很多，但其实我们有很多功能都没用到，这篇文章就是想梳理下那些可能你不知道的但是却对效率提高很有帮助的一些技巧。</p>
<p>包括：</p>
<ul>
<li>一键执行 npm scripts</li>
<li>一键 diff、预览</li>
<li>在新页面搜索</li>
<li>git 视图显示目录树</li>
<li>在新编辑器打开文件</li>
<li>编辑时快速删除、复制、移动行</li>
<li>全局搜索文件、跳转到某行</li>
<li>快速切换大小写</li>
</ul>
<h2 data-id="heading-0">一键执行 npm scripts</h2>
<p>执行 npm scripts 需要在命令行？那是你没用过 vscode 自带的这个功能。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91c399966f9d472582aadfc0efa09207~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 会扫描所有的 npm scripts，然后列出来，直接点击 run 就会打开 terminal 来跑，而且高版本 vscode 还可以直接 debug 来跑。</p>
<p>根本不需要自己输入 npm run xxx。</p>
<h2 data-id="heading-1">在侧栏打开文件</h2>
<p>当打开文件的时候，默认会在当前编辑器打开，如果想新开一个编辑器打开呢？这时候可以按住 option 再点击文件，就会新开一个编辑器打开文件了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03f8994d4f0943358e709504db0b0478~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为默认 vscode 都是在当前编辑器打开新文件，如果不知道按住 option 点击可以新开编辑器，还是挺麻烦的事情。</p>
<h2 data-id="heading-2">更强大的搜索</h2>
<p>搜索这个面板有个按钮可能很多同学都没注意到过，点击之后会打开搜索页面来搜索，可以预览的搜索结果更丰富，行数更多。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6028d10b12e9485e881e813ab8acff8b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如我搜索一个 @babel/core：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/965aa3d4d3e546cba03a332aadf5e186~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看，是不是比在左侧那个小框里显示的更多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1807b2f6af094bdeabab5807981e4c4d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对比一下就可以看出来，还是在右边搜索结果更清晰一些，因为会显示多行。</p>
<h2 data-id="heading-3">文件 diff 显示目录信息</h2>
<p>当我们改了多个文件的时候，会列在 source control 面板的列表里，有多个同名文件的时候特别不直观。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a7b063eb23e4c34ad6a528bbd144193~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时候其实可以切换成 tree view 的，显示目录树。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00d465b5f1784974906e8d41eb5eceaa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当有多个同名文件的时候，这样会清晰的多：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a78edc6afa247078a948e93572b867f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">编辑器一键预览 markdown</h2>
<p>markdown 需要安装插件么？不需要，vscode 本身就内置了这个功能。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65d15d78116e45d9891abe123fef6d3a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>右上角有个预览按钮，点击就会打开 markdown 预览界面，按住 option 再点击，则是同个窗口打开预览。</p>
<p>预览之后再点击 show source 按钮就会回去</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3498d358433443e94b603733ebdfe7e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">编辑区一键 diff</h2>
<h3 data-id="heading-6">快速切换 diff 和文件编辑视图</h3>
<p>当改了文件内容的时候，可以点击编辑区右上角的按钮，直接打开 diff，可能很多同学都没注意到这些按钮，但其实是很有用的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ae3b911d8f452dbe933a2d4194ae9f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再次点击就可以回到文件编辑状态</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebab655b9dd94f51807d3625785d1cea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看功能描述 open changes、open files，很明显就是用于 diff 视图和文件编辑视图的切换。</p>
<h3 data-id="heading-7">diff 视图快速在 diff 之间跳转</h3>
<p>当文件内容特别多，比如好几千行的时候，要找 diff 还是比较麻烦的。其实根本不用自己去找，还容易漏，vscode 编辑器提供了上下按钮，可以直接跳到上一个 diff、下一个 diff</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51b5462cd7754fa1a49721933e0d58db~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一键预览、一键 diff，这些都是能提高效率的功能。</p>
<h2 data-id="heading-8">快速搜索功能入口</h2>
<p>知道 vscode 有某个功能但是不知道入口在哪？
直接用 help下面的搜索框，搜索结果会直接标出来在哪个菜单下有什么按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6589a89dc2a14f97af1f4de9e8a208cc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">编辑快捷键</h2>
<p>编辑器最主要的功能还是编辑，但其实有很多 vscode 的请打编辑功能大家可能没有过，我来罗列一下。</p>
<h3 data-id="heading-10">行上下移动/复制</h3>
<p>如果把一行内容上移下移怎么做？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd8e21d9d02b4a2995782009440b34c5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>手动剪切粘贴的效率太低了，不如试下 option + 上/下 的快捷键，快速把一行内容上下移动。</p>
<p>移动的时候想复制呢？再按住 shift 就行了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b6ba5b3cf6404a89a5f9b25e138df5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">快速删除行</h3>
<p>我们知道了如何快速复制行，那快速删除行呢？</p>
<p>按 command + shift + k 就好了。</p>
<p>如果删除多行，那么先选中，再按 command + shift + k。</p>
<h3 data-id="heading-12">多光标同时编辑</h3>
<p>同时修改多个地方的内容？按住 option 点击要修改的地方就可以了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/820c1ea79ba54f189661477789a5aeda~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是上下行的同一位置呢？那就 option + command + 上/下，这样就是添加多行的同一位置的光标。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bd5fcd35b654c50b97ff8a6a8656f46~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">comand + shift + p 相关</h2>
<p>这可能是大家都知道的一个快捷键，输入框中会有一个 > 代表后面是命令，但还有一些大家可能不知道。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae506ef53fd5456e8ca05dccd89c1b96~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如直接 command + p，不按 shift，这时候就是搜索文件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e5615dea1624c1fa5c39cad2b714815~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如直接按 ctrl + g，或者在输入框输入冒号就代表后面是跳转的行号，可以快速跳到某一行</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0ed0456cc4b4e69b28276574b7fca6b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然搜索文件的时候也可以加冒号和行号，快速跳到该文件的那一行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a955081ba30f46c28ad5957e9387076a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">快速切换大小写</h3>
<p>还有一个小功能，有个内置的 upppercase、lowercase 的切换功能，可以快速切换选中内容的大小写。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2249d5102ed046b1ab88a5140fa773cb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16a54b6498694420bfb411864cc2b8d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">总结</h2>
<p>本文梳理了 vscode 中那些可以提效的一些功能，大家可能没有注意到过。</p>
<ul>
<li>一键 diff、预览</li>
<li>在新页面搜索</li>
<li>git 视图显示目录树</li>
<li>一键执行 npm scripts</li>
<li>在新编辑器打开文件</li>
<li>编辑时快速删除、复制、移动行</li>
<li>全局搜索文件、跳转到某行</li>
<li>快速切换大小写</li>
</ul>
<p>熟悉了这些功能的使用，相信会给我们日常开发提升一些效率，学习下每天写代码的工具的使用技巧还是挺有意义的。</p></div>  
</div>
            