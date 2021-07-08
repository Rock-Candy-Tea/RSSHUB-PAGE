
---
title: '由美团文章_一款可以让大型iOS工程编译速度提升50%的工具_引出的.hmap文件（下）hmap落地'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d0647fe29b42f683338e55004d2677~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 07:59:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d0647fe29b42f683338e55004d2677~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>系列文章：<a href="https://juejin.im/post/6871441300521304077" target="_blank" title="https://juejin.im/post/6871441300521304077">OC底层原理系列</a>，<a href="https://juejin.im/post/6889028196704976910" target="_blank" title="https://juejin.im/post/6889028196704976910">OC基础知识系列</a>，<a href="https://juejin.cn/post/6914837339353120775" target="_blank" title="https://juejin.cn/post/6914837339353120775">Swift底层探索系列</a>，<a href="https://juejin.cn/post/6923957462714286093" target="_blank" title="https://juejin.cn/post/6923957462714286093">iOS高级进阶系列</a></strong></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>距离上篇文章写出来已经有一个多月的时间了，上面文章<a href="https://juejin.cn/post/6958842510042988581" target="_blank" title="https://juejin.cn/post/6958842510042988581">由美团文章“一款可以让大型iOS工程编译速度提升50%的工具”引出的.hmap文件探索</a>介绍了什么是hmap，有什么用！文章结尾我说会进行落地，然后就比较坑了，感觉不落地，这以后都没法交代，没法继续写文章了！后面不再写这样的话了，坑！</p>
<h2 data-id="heading-1">结果展示</h2>
<ul>
<li>1.创建个项目工程，如下图所示，红框为<code>自己写的组件</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d0647fe29b42f683338e55004d2677~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>2.<code>Pod目录</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be790726d47044eb9866029bc2c2f0c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>3.使用写的<code>插件</code>，<code>生成</code>我们需要的<code>hmap</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5c899fed846415c88bc565e166e5a76~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.<code>文件变化</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/774a09d374a1493f8bf1f40f2e3ec03f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>发现<code>pod</code>的<code>xcconfig</code>的<code>HEADER_SEARCH_PATHS添加了hmap路径</code></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d99ca76d5f5e4558b025383431505c10~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>此时我们的<code>文件目录</code>也发生了变化，在Headers文件中<code>多生成了一个Hmap</code>，在<code>Hmap文件夹</code>下，我们根据Cocoapods引入不同的库而<code>生成</code>了相应的<code>.hmap文件</code></p>
</blockquote>
<ul>
<li>5.<code>读取</code>一下<code>hmap</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8255d56ededd4b2489ac80279a7409a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这个和我们上面文章<code>读系统自动生成的格式是一样</code>的</p>
</blockquote>
<ul>
<li>6.<code>优化结果</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/745a18a0b8f348c5beef949792893b97~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2770cf5827c54136b7181b0d36a52736~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>上面</code>为<code>没有使用hmap的编译时间</code>，<code>下面</code>是<code>使用了hmap的编译时间</code>，可以明显感觉到<code>编译速度提升</code>了！说明我们做的没错</p>
</blockquote>
<h2 data-id="heading-2">分析</h2>
<p>上面我们也看到了，我们是<code>通过pod命令</code>来实现<code>生成的hmap</code>的，那么我们就需要使用<code>ruby语言</code>来<code>实现</code>这个<code>功能</code></p>
<ul>
<li>1.看下这个插件</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bfabf36ac804eaeb0dc228fafac6847~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>红框就是<code>实现代码文件</code>，通过文件我们可以感觉它特别<code>像组件</code></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cc53219dc7d4b6b916f3df143b5716d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>上图是项目的组件，而<code>ruby</code>写的其实<code>ruby的组件</code>，<code>cocoapods</code>其实就是<code>用ruby写的</code></p>
</blockquote>
<ul>
<li>2.<code>更新bundle</code>，因为在<code>写ruby</code>，也会<code>引入依赖库</code>，就和<code>项目引入第三方库类似</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38956cdaa7244e3f878fc6053e410c2f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>引入的依赖</code></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d63fec09b934a32ae0dab88eabf7092~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff1c6bad9be4d7a9d59cb72b7844c9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>到这一步，意味着<code>更新完成</code></p>
</blockquote>
<ul>
<li>3.生成插件</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2a1faef6d2a409197cb9c8cf9f584a8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>通过rake install:local命令将写的组件生成我们要用的插件</p>
</blockquote>
<ul>
<li>4.查看插件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1320cd962a4cd08b503bf901c117d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>上面的红框就是我现在使用的cocoapods，下面的就是我们刚生成的</p>
</blockquote>
<h2 data-id="heading-3">代码分析</h2>
<p>代码也没啥分析的，因为我的ruby学的也不怎么样，就粗略的说一下</p>
<h3 data-id="heading-4">hmap创建</h3>
<ul>
<li>1.<code>通过pod获取相关信息</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bab822ab6a84f53953fd902aea8004e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>因为cocoapods也是ruby写的，所以我们可以引入cocoapods，通过cocoapods获取podfile</p>
</blockquote>
<ul>
<li>2.<code>获取将要生成的Header路径</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c299d81a57a4929aabb00f6edc457b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>3.<code>获取pod所有的Target，通过Target名称生成相应的文件</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06d50b1e570048f8b671c23484150c98~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>调用了<code>create方法</code>，<code>生成hmap</code></p>
</blockquote>
<ul>
<li>4.<code>将hmap路径生成好</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6c957d44b6b4715ad5050f268d7a8c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>5.<code>将生成的hmap路径导入xcconfig中</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaeb3a6c40b6426ab006df1f713a7bf8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">hmap写入</h3>
<p>上面说了<code>hmap创建</code>并<code>将路径写入到xcconfig中</code>，下面说下怎么写入的</p>
<ul>
<li>1.<code>生成Header</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1154b2eca96344d1bc9cfd664b786cc2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>就是<code>生成HMapHeader</code>，这部分内容在上面文章中讲过了</p>
</blockquote>
<ul>
<li>2.<code>生成Bucket</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4b676ef0224d67959d63fc608a783c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>3.<code>生成String</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e88beb2bc6d4b6b9fb081cbb7cf7402~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">最后</h2>
<p>今天总算写完了，代码没有细讲，就是粗略的说了下，会ruby的看看就知道啥意思，不会ruby讲的细也不知道啥意思，只需要会用就好了，后面我会放出代码，明天还需要再自己项目中验证一下，没什么问题就会放出代码</p>
<h2 data-id="heading-7">后续</h2>
<p>测试没啥问题，优化了其中的一切代码，完善了一些功能。贴出来插件链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCat1237%2Fcocoapods-hmap" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Cat1237/cocoapods-hmap" ref="nofollow noopener noreferrer">hmap落地</a>。最后补充这个hmap插件对组件化项目效果明显</p></div>  
</div>
            