
---
title: 'Git中 fork, clone,branch之前的区别你真的都了解了吗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05787371b7a04e6eb6ae469f7dd5b052~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 04:54:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05787371b7a04e6eb6ae469f7dd5b052~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、是什么</h2>
<h3 data-id="heading-1">fork</h3>
<p><code>fork</code>，英语翻译过来就是叉子，动词形式则是分叉，如下图，从左到右，一条直线变成多条直线</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05787371b7a04e6eb6ae469f7dd5b052~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>转到<code>git</code>仓库中，<code>fork</code>则可以代表分叉、克隆 出一个（仓库的）新拷贝</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10053f7b6d0e4109a37934dad763bc06~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>包含了原来的仓库（即upstream repository，上游仓库）所有内容，如分支、Tag、提交</p>
<p>如果想将你的修改合并到原项目中时，可以通过的 Pull Request 把你的提交贡献回 原仓库</p>
<h3 data-id="heading-2">clone</h3>
<p><code>clone</code>，译为克隆，它的作用是将文件从远程代码仓下载到本地，从而形成一个本地代码仓</p>
<p>执行<code>clone</code>命令后，会在当前目录下创建一个名为<code>xxx</code>的目录，并在这个目录下初始化一个 <code>.git</code> 文件夹，然后从中读取最新版本的文件的拷贝</p>
<p>默认配置下远程 <code>Git</code> 仓库中的每一个文件的每一个版本都将被拉取下来</p>
<h3 data-id="heading-3">branch</h3>
<p><code>branch</code>，译为分支，其作用简单而言就是开启另一个分支， 使用分支意味着你可以把你的工作从开发主线上分离开来，以免影响开发主线</p>
<p><code>Git</code> 处理分支的方式十分轻量，创建新分支这一操作几乎能在瞬间完成，并且在不同分支之间的切换操作也是一样便捷</p>
<p>在我们开发中，默认只有一条<code>master</code>分支，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33119db9af094ee0a01851da3b37b471~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>git branch</code>可以创建一个分支，但并不会自动切换到新分支中去</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea65ef315b9f42efac61300f4a0b521d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>git checkout</code>可以切换到另一个<code>testing</code>分支</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fad112993f914703973c2d3b238fabb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">二、如何使用</h2>
<h3 data-id="heading-5">fork</h3>
<p>当你在<code>github</code>发现感兴趣开源项目的时候，可以通过点击<code>github</code>仓库中右上角<code>fork</code>标识的按钮，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0fe13cdb5524632b5ae20fd5a0ca5a2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击这个操作后会将这个仓库的文件、提交历史、issues和其余东西的仓库复制到自己的<code>github</code>仓库中，而你本地仓库是不会存在任何更改</p>
<p>然后你就可以通过<code>git clone</code>对你这个复制的远程仓库进行克隆</p>
<p>后续更改任何东西都可以在本地完成，如<code>git add</code>、<code>git commit</code>一系列的操作，然后通过<code>push</code>命令推到自己的远程仓库</p>
<p>如果希望对方接受你的修改，可以通过发送<code>pull requests</code>给对方，如果对方接受。则会将你的修改内容更新到仓库中</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c48b35a1b4a4ba6b900546728b22848~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体流程如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11d58c2479e64363aaf7404388769c1b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">clone</h3>
<p>在<code>github</code>中，开源项目右侧存在<code>code</code>按钮，点击后则会显示开源项目<code>url</code>信息，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a8bb632f78e4db89685b79b583eb7b0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>git clone xxx</code>则能完成远程项目的下载</p>
<h3 data-id="heading-7">branch</h3>
<p>可通过<code>git branch</code>进行查看当前的分支状态，</p>
<p>如果给了<code>--list</code>，或者没有非选项参数，现有的分支将被列出；当前的分支将以绿色突出显示，并标有星号</p>
<p>以及通过<code>git branch</code>创建一个新的分支出来</p>
<h2 data-id="heading-8">三、区别</h2>
<p>其三者区别如下：</p>
<ul>
<li>fork 只能对代码仓进行操作，且 fork 不属于 git 的命令，通常用于代码仓托管平台的一种“操作”</li>
<li>clone 是 git 的一种命令，它的作用是将文件从远程代码仓下载到本地，从而形成一个本地代码仓</li>
<li>branch 特征与 fork 很类似，fork 得到的是一个新的、自己的代码仓，而 branch 得到的是一个代码仓的一个新分支</li>
</ul>
<h2 data-id="heading-9"></h2></div>  
</div>
            