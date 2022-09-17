
---
title: '浅析Git Subtree子仓库在实际项目中的应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57bda151986f4548b8a62032643bbccb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 02:48:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57bda151986f4548b8a62032643bbccb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第7篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h2 data-id="heading-0">为什么需要使用Git Subtree</h2>
<p>先说结论：关于子仓库或者说是仓库共用，git 官方推荐的工具是 git subtree。</p>
<p>在我们实际的项目开发过程中，公共的代码或者模块是必定会出现的，为了不重复写相同的代码；普遍的做法就是将其抽取成一个公共模块，这个模块由不同的使用者引用。</p>
<p>作为 Java 工程师，可能会选择将这一部分打包封装成一个jar，并且将其推送到 Maven 的私有仓库，各个使用者将其添加到 pom 文件引用即可。作为前端工程师，可能会选择将这一部分打包封装成一个自定义的 plugin，将其推送至 npm 的私有仓库，团队内各个使用者去安装引用即可。</p>
<p>但是，有没有更好的方式呢？因为使用这种方式，对使用者来说，并不是透明的，假如我们需要修改一个业务，这个业务设计到业务代码和这块公共代码的同步修改，那么使用者是不方便去改这块代码的。</p>
<p>接下来，就一起探讨一种更好的管理方式：git subtree。</p>
<h2 data-id="heading-1">共用代码的需求及处理方式</h2>
<p>1、需求背景：项目A与项目B存在公用模块，在项目A中修改Bug或增加新功能需要同步到项目B中</p>
<p>2、需求分析：A项目中依赖了子项目B，最方便的方式自然是直接在A项目里改B子项目对应的目录里的代码，然后测试通过后，直接提交代码，这个更改也提交到B子项目的 Git仓库里。同时子项目B也可以单独提交到 Git 仓库，再在A项目里把子项目B的代码update。</p>
<p>3、现有方案</p>
<p>（1）Git Submodule：这是Git官方以前的推荐方案</p>
<p>（2）Git Subtree：从 Git1.5.2 开始，Git 新增并推荐使用这个功能来管理子项目</p>
<p>（3）npm 等包管理工具</p>
<p>npm（前端）、maven（后端） 等更侧重于包的依赖管理，虽然能够做到在不同项目中同步同一块代码的，但没法双向同步，修改维护公用代码包也比较麻烦，更适用于子项目代码比较稳定的情形。</p>
<p>Git Submodule 和 Git Subtree 都是官方支持的功能，不具有依赖管理的功能，但能满足我们的要求。Git Subtree相对来说会更好一些，git 官方建议使用 git subtree。</p>
<p>4、Git Subtree 好在哪里？</p>
<p>用一句话来描述 Git Subtree 的优势就是：</p>
<blockquote>
<p>经由 Git Subtree 来维护的子项目代码，对于父项目来说是透明的，所有的开发人员<strong>看到的就是一个普通的目录，原来怎么做现在依旧那么做</strong>，只需要维护这个 Subtree 的人在合适的时候去做同步代码的操作。</p>
</blockquote>
<p>它是怎么做到的呢？后面会通过实操记录简单说下原理。</p>
<h2 data-id="heading-2">什么时候需要 Subtree？</h2>
<p>1、当多个项目共用同一模块代码，而且这块代码跟着项目在快速更新的时候。</p>
<p>2、把一部分代码迁移出去独立为一个新的 git 仓库，但又希望能够保留这部分代码的历史提交记录。</p>
<h2 data-id="heading-3">Git Subtree的原理与实际应用</h2>
<p>首先，你需要2个主项目，我利用之前的demo项目、demo2项目，还要有一个被多个项目共用的subtree项目。我们通过简要讲解使用Subtree来同步代码的过程来解释Subtree的原理</p>
<p>1、初始化子项目subtree</p>
<p>通过我之前的demo项目做下示例</p>
<pre><code class="hljs language-ini copyable" lang="ini">cd demo项目的路径  
git subtree add <span class="hljs-attr">--prefix</span>=用来放subtree项目的相对路径 subtree项目git地址 xxx分支
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">PS D:\demo\vue-button-test> git subtree add --prefix=/subtree https://gitee.com/***/npm_test.git master
git fetch https://gitee.com/goloving/npm_test.git master
From https://gitee.com/goloving/npm_test
 * branch            master     -> FETCH_HEAD
error: Invalid path <span class="hljs-string">'C:/Program Files/Git/subtree/README.md'</span>
error: Invalid path <span class="hljs-string">'C:/Program Files/Git/subtree/index.js'</span>
error: Invalid path <span class="hljs-string">'C:/Program Files/Git/subtree/package.json'</span>
error: Invalid path <span class="hljs-string">'C:/Program Files/Git/subtree/plugins/lib/button.vue'</span>
fatal: C:/Program Files/Git/subtree: <span class="hljs-string">'C:/Program Files/Git/subtree'</span> is outside repository
PS D:\demo\vue-button-test> git subtree add --prefix=subtree https://gitee.com/goloving/npm_test.git master
prefix <span class="hljs-string">'subtree'</span> already exists.
PS D:\demo\vue-button-test> git subtree add --prefix=subtree https://gitee.com/goloving/npm_test.git master
git fetch https://gitee.com/goloving/npm_test.git master
From https://gitee.com/goloving/npm_test
 * branch            master     -> FETCH_HEAD
Added <span class="hljs-built_in">dir</span> <span class="hljs-string">'subtree'</span>
PS D:\demo\vue-button-test>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遇到3个报错：</p>
<p>（1）<code>Working tree has modifications. Cannot add. </code>实际上工作树没有更改，解决：关闭终端，重新开启终端即可</p>
<p>（2）--prefix=/subtree 应该是相对路径，不是绝对路径，所以写 /subtree 匹配到 C:/Program Files/Git/ 去了</p>
<p>（3）--prefix=subtree 刚开始以为必须新建这个目录，发现不是的，新建会报错，删除即可</p>
<p>这样的命令，把subtree即npm_test项目的代码下载到--prefix所指定的subtree目录中，并在demo项目里自动产生一个commit（就是把npm_test目录的内容提交到demo项目里）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57bda151986f4548b8a62032643bbccb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们再用一个demo2项目做同样的操作</p>
<p>2、像往常一样更新代码</p>
<p>大家在demo项目里各种提交commit，其中有些commit会涉及到subtree目录的更改，正如前面提到的，这是没任何关系的，大家也不会感受到有任何不一样。</p>
<p>比如我们在 npm-test 项目里button按钮后随便加个文字：subtree，看下图 demo 项目生效了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a390e1df0944919a8c659622ba65037~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们把更改的所有内容 git 提交到 demo 项目仓库，我们可以看到下面全部的 commit 记录</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8e3bf9da3594fc39713d954c92a1ef0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e08e5a97f1a42e58427ef6c3c5c2000~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、提交更改到子项目的Git服务器</p>
<p>关键的地方来了：当维护这个demo项目 subtree 的人希望把最近这段时间对demo项目subtree目录的更改提交到subtree对应的npm_test项目的 Git 服务器上时，他执行一段类似于这样的命令：</p>
<pre><code class="hljs language-ini copyable" lang="ini">cd demo项目的路径  
git subtree push <span class="hljs-attr">--prefix</span>=用来放subtree项目的相对路径 subtree项目git地址 xxx分支
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">PS D:\demo\vue-button-test> git subtree push --prefix=subtree https://gitee.com/***/npm_test.git master
git push using:  https://gitee.com/goloving/npm_test.git master
Counting objects: 5, <span class="hljs-keyword">done</span>.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), <span class="hljs-keyword">done</span>.
Writing objects: 100% (5/5), 384 bytes | 384.00 KiB/s, <span class="hljs-keyword">done</span>.
Total 5 (delta 2), reused 0 (delta 0)
remote: Powered by GITEE.COM [GNK-6.3]
To https://gitee.com/goloving/npm_test.git
   adbf133..bbe8c7b  bbe8c7b22181acc371c7118f6392fafa9448ce4f -> master
PS D:\demo\vue-button-test>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Git 会遍历所有的commit，从中找出针对subtree目录的更改，然后把这些更改记录提交到subtree对应的npm_test项目的Git服务器上。</p>
<p>然后我们就可以看到 npm_test 项目上多个对button更改的记录</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab88366a71de4e91bfb284d97188e95f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4、更新子项目新的代码到父项目</p>
<p>现在subtree npm_test项目有新代码了，demo2项目也想使用这些新代码，维护demo2项目这个Subtree的人只要执行</p>
<pre><code class="hljs language-ini copyable" lang="ini">cd demo2项目路径
git subtree pull <span class="hljs-attr">--prefix</span>=subtree项目的路径 subtree项目git地址 xxx分支
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">PS D:\其他\big-data-view1>  git subtree pull --prefix=subtree https://gitee.com/goloving/npm_test.git master
Working tree has modifications.  Cannot add.
PS D:\其他\big-data-view1>  git subtree pull --prefix=subtree https://gitee.com/goloving/npm_test.git master
remote: Enumerating objects: 9, <span class="hljs-keyword">done</span>.
remote: Counting objects: 100% (9/9), <span class="hljs-keyword">done</span>.
remote: Compressing objects: 100% (3/3), <span class="hljs-keyword">done</span>.
remote: Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), <span class="hljs-keyword">done</span>.
From https://gitee.com/goloving/npm_test
 * branch            master     -> FETCH_HEAD
Merge made by the <span class="hljs-string">'recursive'</span> strategy.
 subtree/plugins/lib/button.vue | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
PS D:\其他\big-data-view1>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当有未提交记录时会报这个错误：Working tree has modifications. Cannot add. 解决：将未提交记录全部提交即可</p>
<p>接下来我们就可以看到 demo2 项目里的 button 按钮就更新为最新的了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d8e1745fbcf44e1810b8bda25d7e03a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就可以将demo2项目里subtree目录里的内容更新为npm_test项目xxx分支的最新代码了。</p></div>  
</div>
            