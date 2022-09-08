
---
title: '比pnpm的更快的模块管理方案，提效竟有6倍？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82243201168f42d1baaf9b3e8b3990a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Mon, 05 Sep 2022 02:10:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82243201168f42d1baaf9b3e8b3990a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在大前端世界发展到繁荣时代的今天，前端从业者们不得不面对如今纷繁复杂的模块环境带给研发和维护工作的烦恼：它安装的实在太慢了。在研发效能的大赛道上，依赖管理性能已经成了我们避无可避的绊脚石。</p>
<p>我们关注到蚂蚁集团的优秀同行们提出的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F511006062%2Fanswer%2F2307564054" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/511006062/answer/2307564054" ref="nofollow noopener noreferrer">tnpm rapid</a>思路和探索，使用底层技术手段，解决上层业务问题，成功从文件系统层面解决前端基建问题。为前端领域的先行者们点赞👍！</p>
<p>我们根据这套方案还原了相对完整的FUSE版模块管理器，并且在团队日常开发中实装测试。本文将分享成果数据并且分析实践中的痛点与难点，给出我们团队的解决方案，希望能对大家有所启发。</p>
<p>也欢迎大家提出用底层技术”破圈“前端基建的想法和建议。</p>
<h2 data-id="heading-0">成果先行</h2>
<p>我们使用Rust编写了FUSE守护进程和模块下载、解压的模块，使用node实现了上层命令行程序以覆盖script hook等需要npm库支持的情况，并且在团队内的osx的开发环境实装测试。</p>
<p>看一下基于整体思路实现的模块安装程序的性能数据</p>
<blockquote>
<p>MacBook Pro (macOS Big Sur)</p>
<p>处理器: 2.8 GHz 四核Intel Core i7</p>
<p>内存: 16 GB 2133 MHz LPDDR3</p>
<p>测试项目: 团队内中台项目 (包含1709个模块、69450个子文件)</p>
<p>网络环境: < 300Mbps</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82243201168f42d1baaf9b3e8b3990a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="截屏2022-09-05 18.59.12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到在包含lock文件的情况下，安装速度有明显的提升。在含有缓存文件的情况，npm由于要处理大量的文件写入，性能表现很低下。对比而看，FUSE的优化效果非常明显，符合预期情况。由于我们的方案没有设计优化lock生成性能，依旧使用npm本身的方案，所以就先不在此列出无lock的情况的性能数据了。</p>
<p>综合结果数据来看，FUSE在模块管理的领域大有可为。尤为重要的是，这种把上层问题使用底层方案解决的做法是非常有突破性的，可以说拓宽了前端基建的上限，带给我们很深的启发。</p>
<h2 data-id="heading-1">FUSE是什么</h2>
<p>FUSE (Filesystem in Userspace) 即用户态文件系统，是指一种在用户态实现的文件系统。Linux通过FUSE内核模块对此进行支持，osx中可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fosxfuse.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://osxfuse.github.io/" ref="nofollow noopener noreferrer">macfuse</a>实现相同的能力。FUSE的核心思想是允许使用用户态程序控制文件系统的相关逻辑，避免了内核态代码难以调试的尴尬处境，又能实现不同的灵活的业务需求。</p>
<p>放眼前端领域，我们是否可以设想一个场景，node读取模块的目录node_modules由FUSE承载，相关的目录结构由文件系统守护进程虚拟构造。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49b67abdcd3d42959c79cf00c97fee94~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="截屏2022-09-05 18.59.19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以简单构思一个工作流程，即用户看到的node_modules目录由FUSE守护进程通过模块依赖图（即lock文件）生成，上端的node程序读取模块文件的请求被无差别转发到守护进程，由其返回真实文件内容。</p>
<p>在具体设计程序之前，为了保证ROI合理，我们先要找到目前模块管理领域效率优化问题的核心痛点，来确认FUSE的引入是否值得。</p>
<h2 data-id="heading-2">解决什么问题</h2>
<p>我们来关注下目前npm的工作流程，从中找到最需要优化的核心问题。</p>
<ol>
<li>递归获取依赖版本、压缩包、子依赖信息，整合成lock图</li>
<li>下载tgz压缩包，构建本地缓存</li>
<li>创建项目node_modules目录，从归档包写入文件</li>
</ol>
<h3 data-id="heading-3">npm、yarn的扁平化方案</h3>
<p>npm@3、yarn等从过程第一步出发，提出扁平化优化，将子依赖优先提升到顶层node_modules目录，解决了大量重复的依赖问题，同时层级在一般情况下不会太深。</p>
<p>但是这种模式有一个根深蒂固的性能问题，前端依赖包中通常包含大量的小文件，同时依赖之间还存在复杂的关联。最后的结果就是我们在业务中使用的模版项目都很“臃肿”，其node_modules通常都包含上万个文件。写入依赖包内大量的小文件的I/O，严重限制了这种模式的安装速度，导致在lock和cache都存在的情况也要消耗大量的时间在I/O上。</p>
<p>于此同时，npm为每一个项目创建一个node_modules目录，无法共用存储空间，产生了硬盘空间的巨额损耗。</p>
<h3 data-id="heading-4">pnpm的方案</h3>
<p>为了解决上述的问题，pnpm提出了硬链接 + 软链接的方式解决模块管理问题。官网的介绍图很好的描述了这种模式：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8478819518254eb78dbbf5d7813fcf86~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="截屏2022-09-05 18.59.27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>pnpm从全局store中通过软、硬链接文件的方式引入到项目node_modules目录中，减少文件复制的同时，可以共用磁盘空间。</p>
<p>但是pnpm依然存在一些限制：</p>
<ul>
<li>项目的node_modules无法独立，对系统某一个项目内的模块进行调试会污染全局存储</li>
<li>软链的创建依旧存在磁盘损耗</li>
</ul>
<h3 data-id="heading-5">其他的思路</h3>
<p>yarn在之前提出了Plug'n'Play特性，其核心思想在于生成静态映射表直接把模块文件关联到缓存中的具体位置，不生成node_modules目录。但是相应的，必须实现一套resolver来改变node的require默认行为，没办法兼容目前的node生态。</p>
<h3 data-id="heading-6">总结下问题</h3>
<p>不难看出，pnpm、yarn等提出的优化策略都是从减少文件I/O出发，加速模块安装速度。但是目前市面的方案或多或少都存在其限制和不足。</p>
<p>现在来回想下上节介绍的FUSE，FUSE可以从根本上避免文件I/O问题，而且其灵活的特性可以弥补pnpm现存的不足之处。FUSE的思路让我们可以从更底层的视角出发，尝试缓解安装模块时带来的大量写入时间，最大化增速安装过程。</p>
<h2 data-id="heading-7">实现方案</h2>
<p>设计一下需求的功能：</p>
<ol>
<li>支持FUSE守护进程生成虚拟node_modules目录</li>
<li>支持项目模块的隔离，弥补pnpm的不足</li>
<li>支持多项目同时使用，也就是说要同时支持多个node_modules目录</li>
</ol>
<h3 data-id="heading-8">虚拟node_modules目录</h3>
<p>在不考虑自行处理lock文件生成的情况下，我们可以用npm提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40npmcli%2Farborist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@npmcli/arborist" ref="nofollow noopener noreferrer">解析库</a>将lock文件处理成依赖树，然后提取出我们需要的内容。在这种场景下，我们提取出模块tgz文件下载路径之后，处理下载、解压的逻辑，最后的储存形式是tar归档文件，然后把依赖树信息传递给守护进程进行分析。守护进程可以根据依赖结构生成相应的虚拟模块目录，目录下面的具体模块文件内容可以根据文件大小、偏移量数据直接从tar归档文件读取返回。</p>
<p>需要特别注意的有几点</p>
<ol>
<li>单独处理@xxx格式的私有文件夹前缀，生成其下相应模块的虚拟目录。其余普通格式的模块直接在根node_modules底下生成目录。</li>
<li>由于npm的扁平化方案依然存在不同版本的子依赖无法提升，需要由依赖本身维护在自己的node_modules底下，所以我们需要在依赖目录下确认是否需要维护下一级node_modules。</li>
<li>.bin目录需要根据依赖package.json内的bin段确认，并且生成对应的软链接文件。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31132032fa334ba98b2b17296fe10f3b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="截屏2022-09-05 18.59.34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">项目隔离</h3>
<p>我们期望的场景是修改项目里的node_modules模块进行调试，不会影响使用相同依赖的其他项目，也就是不会污染全局存储。如果接触过docker的同学，会对这个概念很熟悉。docker利用UnionFS（联合文件系统）进行镜像分层，启动容器的时候，docker会在下层只读镜像的顶部加一层可写层，这就是容器层的由来。对上层容器进行文件写入不会影响底层镜像。</p>
<p>这种镜像系统UnionFS在linux内有内核级的实现，我们为了兼容osx环境，在这里使用其<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frpodgorny%2Funionfs-fuse" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rpodgorny/unionfs-fuse" ref="nofollow noopener noreferrer">FUSE版的实现</a>。大体的示意图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1128741b8984521823e244509be7f0e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="截屏2022-09-05 18.59.40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们为每个项目的node_modules挂载一层单独的叠加镜像，由上层的项目独立并且可写入的UpperDir和底层FUSE实现的只可读的原始node_modules目录合并而成。在某程序进行node_modules的写入时，UnionFS会将改动复制到上层文件夹中，不会影响底层目录。这样不同的项目之间node_modules的修改就不会互相影响了。</p>
<h3 data-id="heading-10">多项目支持</h3>
<p>在我们日常的开发中，当然需要多个项目并行开发，支持多个node_modules同时挂载是非常有必要的。那么底层守护进程怎么为不同项目输出不同的node_modules目录呢？</p>
<p>结合UnionFS来看，每个项目的UnionFS是独立的，而且其合并镜像层时自然需要请求底层的目录，这个request内是有进程信息的。也就是说我们可以使用UnionFS的进程信息来确认目录来源。</p>
<p>换句话说，我们只需要为不同项目的依赖树增加进程信息作为索引，再提交给底层守护进程，底层守护进程就可以在接收到文件相关的request时，使用进程pid找到指定的依赖树，并生成虚拟目录。</p>
<p>至此，一套完整的基于FUSE的模块管理器就设计完成了。</p>
<h2 data-id="heading-11">展望</h2>
<p>传统前端基建的瓶颈已经愈发明显，利用rust等语言工具、系统底层技术的方案越来越多。如何在这个以变化为核心的大环境中找到合适团队的方向，如何在技术门槛成本与效能提升目标之间找到平衡点，都是我们一直在思考的命题。希望本篇文章能带给前端同仁们一些启发，也为大前端良性健康的发展做出我们团队的一点微末贡献。</p></div>  
</div>
            