
---
title: '提升你工作效率的内置git客户端'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253625260cbc42bb97a1fe750130dc09~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:18:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253625260cbc42bb97a1fe750130dc09~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>webstorm中集成了一个很好用的git管理工具，它可以大大提升我们的工作效率，本文就跟大家分享下工作中几个常用操作，欢迎各位感兴趣的开发者阅读本文。</p>
<h2 data-id="heading-1">Git管理面板</h2>
<p>我们通过webstorm左下角的Git来打开这套集成工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253625260cbc42bb97a1fe750130dc09~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724172051880" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开后的界面如下所示：</p>
<ul>
<li>Local Changes 展示你当前已修改但未提交的文件</li>
<li>Log: master 你当前所在的分支
<ul>
<li>左侧区域展示的是所有分支列表
<ul>
<li>Local 本地的分支列表</li>
<li>Remote 远程仓库的分支列表</li>
</ul>
</li>
<li>右侧区域展示的是当前选中分支的提交记录
<ul>
<li>选中一个提交记录，最右侧会展示当前提交记录所修改的文件</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc73d66eacae4bb7962594eac81eb959~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724172729171" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果你看不到左下角的Git，可能是因为你隐藏了<code>Tool Window Bars</code>，在菜单栏<code>View -Appearance - Tool Window Bars</code>将其勾选即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed5b5ed54eea4c0fa21333be48373eab~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724180744707" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>如果你对webstorm不是很熟悉，请移步我的另一篇文章：<a href="https://juejin.cn/post/6987411282274025485" target="_blank" title="https://juejin.cn/post/6987411282274025485">合理使用WebStorm-环境配置篇</a>。</p>
<h2 data-id="heading-2">常用的操作</h2>
<p>接下来跟大家分享下，工作中一些常用的git操作，如何在这套内置工具上实现。</p>
<h3 data-id="heading-3">创建分支</h3>
<p>当项目需求明确后，我们要做的第一件事就是创建一个新分支来做这个需求，在这套内置git工具中，我们只需在我们需要基于的分支上右键选择<code>New Branch from Selected...</code>即可。</p>
<p>例如：我们想基于<code>master</code>分支创建一个新的分支</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a12b6f07ede4b95a648ad1709a39661~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724201805387" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在弹出框中输入新的分支名，点<code>CREATE</code>即可，如下图所示，我们给新分支起名为<code>AddMenu</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a444349cd24c47859ac9d1f4f62cb615~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724202217151" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照上述步骤操作即可完成一个新分支的创建。</p>
<blockquote>
<p>注意：在弹出框中默认是创建并选中当前创建的分支的，如果你只想创建不想选中，取消弹出框里面的<code>Checkout branch</code>选中即可。</p>
</blockquote>
<p>创建完车后，我们可能还需要将这个分支推到远程仓库，我们在创建好的分支上右键选择<code>Push...</code>即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47524bec5cef4af28e345a61e145b622~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724210234782" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">拉取分支</h3>
<p>当我们想选中同事的分支，帮同事改bug时，则需要将这个分支拉到本地，在这套内置git工具中我们只需在<code>Remote</code>中找到这个分支，右键选择<code>Checkout</code>即可。</p>
<p>例如，我们想选中<code>github_page</code>分支：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/632ead0065c1461bac9abdf28fee7881~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724203856360" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择后，你会看到如下图所示的提示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8562cb60aa1446a0bad4da2a3fb3bc4a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724204040261" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">合并分支</h3>
<p>当我们将需求开发完成，测试通过后，就需要将分支合并到dev去了，在这套内置工具中，我们只需要切换分支到dev，然后再需要合并的分支上右键选择<code>Merge into Current</code>即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0321e4197a41417ba07c45d542a68e8b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724234453128" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果有冲突的文件，则需要解决下冲突，如下所示：</p>
<ul>
<li>选中一个冲突的文件
<ul>
<li>序号1标注 使用当前所在分支(dev)的文件</li>
<li>序号2标注 使用合并分支的文件</li>
<li>序号3标注 比对两个版本的文件差异，解决冲突</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ef67de38d5140fda0ada7b6ee4d3b17~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724234718134" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你选择了序号3标注的按钮，将看到如下所示的界面：</p>
<ul>
<li>左侧为dev分支的代码，中间为最终结果区域，右侧为合并分支的代码</li>
<li>序号1、2、3标注的地方为应用此处更改到最终结果区域</li>
<li><code>X</code>的意思是舍弃此处的更改</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee9dfba88b2b4a6d908bf939c7858314~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210724235117407" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">删除分支</h3>
<p>当我们将某个分支合并到dev后，此时这个分支就不需要了，需要将其删除。</p>
<p>在webstorm中，我们只需在远程分支列表中找到这个分支，右键选择<code>Delete</code>即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e386e0536ed4e609002e7cff8e3df87~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725003634683" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">提交代码</h3>
<p>当我们修复了一个bug，或者完成了一个模块的开发时，需要将代码提交到本地，然后再推送远程仓库，在webstorm中只需要点击<code>Toolbar</code>中的<code>commit</code>图标和<code>push</code>图标即可。</p>
<p>如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f37fda83034514aef7fbd5127ac525~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725000121578" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在弹出的窗口中，填写提交信息即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8d7cc960ed6472b8a9c039274fd4d69~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725000233787" loading="lazy" referrerpolicy="no-referrer"></p>
<p>提交完成后，点击推送按钮即可将本次提交推送到远程仓库。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc1058e1185344eda9a14470093ada20~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725000436434" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在弹出的窗口中点<code>push</code>即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94995d512e3743bebc853f2676f08358~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725000529092" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：如果你看不到<code>Toolbar</code>，则需要在菜单栏: <code>view - Appearance - ToolBar</code>将其开启。</p>
<p>除此之外，你还可以在菜单栏的<code>Git</code>子菜单中去提交/推送，或者按快捷键<code>command K / command shift K</code>。</p>
</blockquote>
<h3 data-id="heading-8">拉取代码</h3>
<p>当需要获取某个分支上同事修改的最新代码时，此时就需要进行<code>pull</code>操作，我们只需在webstorm菜单栏的<code>git</code>子菜单下选择pull即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e25256f63554d168caa5e9477d0d916~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725001609640" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">暂存与取出</h3>
<p>当我们在某个分支上开发需求时，突然来一个加急需求需要你在别的分支改，此时你的更改又不适宜提交，那么就需要将当前更改暂存起来。</p>
<p>我们只需在项目树上右键，选择<code>Git - Stash Changes...</code>即可将更改暂存，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/383a7e94048d499293ddc587c8540791~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725002140382" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在弹出的窗口中填写保存信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ae6741117d4663b4891629ac990560~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725002254573" loading="lazy" referrerpolicy="no-referrer"></p>
<p>紧急任务开发完成后，我们切回分支，在项目根目录右键，选择<code>Git - Unstash Change...</code>即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0996bb764654fa18d7a78909b17999a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725002450616" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">版本回退</h3>
<p>当我们提交了代码后，测试那边测出了很多问题，此时我们就会觉得本次提交无意义，需要将其撤销。</p>
<p>我们只需在<code>Git</code>面板中，选中要回退的git版本，右键选择<code>Reset Current Branch to Here...</code>即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1e41ddbe5941629c9e7b2beb3d6114~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725002931454" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在弹出的菜单中选择<code>Mixed</code>选项即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4956bf71fa4c4880d5bfd32e6f8be8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725003002381" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：如果你的提交已经推到了远程仓库，你想删除远程仓库的记录，在本地回退后还需要在终端执行<code>git push --force</code>命令进行强推。</p>
<p>强推是危险命令，如果你回退的版本之后还有别的同事提交的代码，那么此命令将会删除别的同事提交的代码。</p>
</blockquote>
<h3 data-id="heading-11">合并部分提交记录</h3>
<p>当我们需要将某个分支的部分提交合并到<code>dev</code>分支时，我们需要用到<code>git cherry-pick</code>命令。</p>
<p>在webstorm中，我们只需切换分支到dev，然后在<code>Git</code>面板中选中需要合并提交的分支，选择需要合并的记录，点击<code>樱桃</code>图标即可完成合并。</p>
<p>如下所示，我们需要将<code>AddMenu</code>分支的两个提交合并到<code>dev</code>分支：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f430c21d09141d5b7e4575d2be5d9fc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725004742222" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，我们切换到dev分支即可看到合并过来的两个提交，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffd0f72ad9c442fa927b2cc2c97ac554~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210725004916220" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">写在最后</h2>
<p>至此，文章就分享完毕了。</p>
<p>我是<strong>神奇的程序员</strong>，一位前端开发工程师。</p>
<p>如果你对我感兴趣，请移步我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.kaisir.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.kaisir.cn/" ref="nofollow noopener noreferrer">个人网站</a>，进一步了解。</p></div>  
</div>
            