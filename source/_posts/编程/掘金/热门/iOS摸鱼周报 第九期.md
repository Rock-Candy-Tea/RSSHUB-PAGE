
---
title: 'iOS摸鱼周报 第九期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6afc277724d4f27a461eafae8028788~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 18:15:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6afc277724d4f27a461eafae8028788~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6afc277724d4f27a461eafae8028788~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享大家开发过程遇到的经验教训及学习内容。虽说是周报，但当前内容的贡献途径还未稳定下来，如果后续的内容不足一期，可能会拖更到下一周再发。所以希望大家可以多分享自己学到的开发小技巧和解bug经历。</p>
<p>周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，可以查看README了解贡献方式；另可关注公众号：iOS成长之路，后台点击进群交流，联系我们。</p>
<h2 data-id="heading-0">开发Tips</h2>
<h3 data-id="heading-1">关于Xcode 12的Tab</h3>
<p>贡献者：<a href="https://www.jianshu.com/u/1e59b1fe9df8" target="_blank" rel="nofollow noopener noreferrer">highway</a></p>
<p>不知道有多少同学困惑于Xcode 12的新tab模式，反正我是觉得这种嵌套的tab形式还不如旧版简洁明了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02ee30ef6fca489da7a72ef47737b320~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>想切回旧版本tab模式的，可以按照此文操作：
<a href="https://www.jessesquires.com/blog/2020/07/24/how-to-fix-the-incomprehensible-tabs-in-xcode-12/" title="How to fix the incomprehensible tabs in Xcode 12" target="_blank" rel="nofollow noopener noreferrer">How to fix the incomprehensible tabs in Xcode 12</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba1ed7f234b34579aa2b3fcdba862301~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过实验发现，Xcode 12下的“子tab”有以下几个特点：</p>
<blockquote>
<p>A.当单击文件打开时，tab将显示为斜体，如果双击，则以普通字体显示。斜体表示为“临时”tab，普通字体表示为“静态”tab；</p>
<p>B.双击tab顶部文件名，或者对“临时”tab编辑后，“临时”tab将切换为“静态”tab；</p>
<p>C.如果当前位于“静态”tab，新打开的文件会新起一个tab，并排在当前tab之后；</p>
<p>D.新打开的“临时”文件会在原有的“临时”tab中打开，而不会新起一个“临时”tab；</p>
<p>E.使用Command + Shift + O打开的是“临时”文件。</p>
</blockquote>
<h3 data-id="heading-2">modalPresentationCapturesStatusBarAppearance</h3>
<p>贡献者：<a href="https://github.com/beatman423" target="_blank" rel="nofollow noopener noreferrer">beatman423</a></p>
<p>这边遇到的问题是非全屏present一个导航控制器的时候，咋也控制不了这个导航控制器以及其子控制器的状态栏的style和hidden。后来找到了UIViewController的这个属性，将其设置为YES就可以了。</p>
<p>该属性的描述是：</p>
<blockquote>
<p>Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller. Defaults to NO.</p>
</blockquote>
<h2 data-id="heading-3">那些Bug</h2>
<h3 data-id="heading-4">fishhook在某些场景下只生效一次</h3>
<p>贡献者：<a href="https://www.jianshu.com/u/739b677928f7" target="_blank" rel="nofollow noopener noreferrer">皮拉夫大王在此</a></p>
<p><strong>问题背景</strong></p>
<p>之前我们监控到钥匙串的API在主线程访问时存在卡死的情况，因此hook 相关API，将访问移到子线程。因此使用到fishook，当时测试并没有发现异常。</p>
<p><strong>问题描述</strong></p>
<p>前段时间在做技术优化时发现我们的hook代码只生效了一次，下次访问API时变成了直接访问系统原方法。</p>
<p><strong>问题原因</strong></p>
<p>由于hook之前没有调用过钥匙串API，因此可能此时并没有做bind，在我们hook后bind信息被替换成我们的函数，因此首次调用hook成功。但是在hook方法中我们又调用了原函数，此时触发了bind，内存中的函数地址又被替换成系统函数，因此第二次调用时hook失败。
解决方案：见<a href="https://github.com/facebook/fishhook/issues/36" target="_blank" rel="nofollow noopener noreferrer">github.com/facebook/fi…</a></p>
<h2 data-id="heading-5">编程概念</h2>
<p>整理编辑：<a href="https://juejin.cn/user/782508012091645" target="_blank">师大小海腾</a>，<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-6">什么是 Homebrew</h3>
<p><a href="https://brew.sh/index_zh-cn" title="Homebrew" target="_blank" rel="nofollow noopener noreferrer">Homebrew</a> 是一款 Mac OS 平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能。简单的一条指令，就可以实现包管理，而不用你关心各种依赖和文件路径的情况，十分方便快捷。</p>
<p>安装方法：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ /bin/bash -c <span class="hljs-string">"<span class="hljs-subst">$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>国内镜像：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ /bin/bash -c <span class="hljs-string">"<span class="hljs-subst">$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">什么是 Ruby</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8fcac70b92949688b24195c4c96aa54~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Ruby 是一种开源的面向对象程序设计的服务器端脚本语言，在 20 世纪 90 年代中期由日本的松本行弘设计并开发。在 Ruby 社区，松本也被称为马茨（Matz）。</p>
<p>Ruby的设计和Objective-C有些类似，都是受Smalltalk的影响。而这也一定程度促进了iOS开发工具较为广泛的使用Ruby写成。</p>
<p>较为知名的几个由Ruby写成的iOS开发工具有：CocoaPods、Fastlane、xcpretty。那这些库为啥使用Ruby开来发呢？</p>
<p>来自CocoaPods的主要作者Eloy Duran的说法：</p>
<blockquote>
<p>Ruby和Objective-C具有很多来自Smalltalk的特性，有一定相似性；使用Ruby可以在Bundler和RubyGem之间分享代码；早期阶段MacRuby提供了很多解析Xcode projects的方法；作为CLI工具，Ruby具有强大的字符串处理能力。</p>
</blockquote>
<p>来自Fastlane工具链的作者之一Felix的说法：</p>
<blockquote>
<p>已经有部分iOS工具选择了Ruby，像是CocoaPods以及给Fastlane的开发带来灵感的nomad-cli。使用Ruby将会更容易与这些工具进行对接。</p>
</blockquote>
<p><a href="https://medium.com/xcblog/a-history-of-ruby-inside-ios-development-427b5a09f91e" title="A History of Ruby inside iOS Development" target="_blank" rel="nofollow noopener noreferrer">参考来源：A History of Ruby inside iOS Development</a></p>
<h3 data-id="heading-8">什么是 Rails</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/773cdb9eabdf41d5910c4d19a0b9fe37~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Rails（也叫Ruby on Rails）框架首次提出是在 2004 年 7 月，它的研发者是 26 岁的丹麦人 David Heinemeier Hansson。Rails 是使用 Ruby 语言编写的 Web 应用开发框架，目的是通过解决快速开发中的共通问题，简化 Web 应用的开发。与其他编程语言和框架相比，使用 Rails 只需编写更少代码就能实现更多功能。有经验的 Rails 程序员常说，Rails 让 Web 应用开发变得更有趣。</p>
<p>Rails的两大哲学是：不要自我重复（DRY），多约定，少配置。</p>
<p>松本行弘说过：Ruby能拥有现在的人气，基本上都是Ruby on Rails所作出的贡献。</p>
<h3 data-id="heading-9">什么是 rbenv</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41fc873281e74cf6bcb33d3b65187eba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/rbenv/rbenv" title="rbenv" target="_blank" rel="nofollow noopener noreferrer">rbenv</a> 和 RVM 都是目前流行的 Ruby 环境管理工具，它们都能提供不同版本的 Ruby 环境管理和切换。</p>
<p>进行 Ruby 版本管理的时候更推荐 rbenv 的方式，你也可以参考 rbenv 官方的 <a href="https://github.com/rbenv/rbenv/wiki/Why-rbenv%3F" title="Why choose rbenv over RVM?" target="_blank" rel="nofollow noopener noreferrer">Why choose rbenv over RVM?</a>，当前 rbenv 有两种安装方式：</p>
<p><strong>手动安装</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/rbenv/rbenv.git ~/.rbenv
<span class="hljs-comment"># 用来编译安装 ruby</span>
git <span class="hljs-built_in">clone</span> https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
<span class="hljs-comment"># 用来管理 gemset, 可选, 因为有 bundler 也没什么必要</span>
git <span class="hljs-built_in">clone</span> git://github.com/jamis/rbenv-gemset.git  ~/.rbenv/plugins/rbenv-gemset
<span class="hljs-comment"># 通过 rbenv update 命令来更新 rbenv 以及所有插件, 推荐</span>
git <span class="hljs-built_in">clone</span> git://github.com/rkh/rbenv-update.git ~/.rbenv/plugins/rbenv-update
<span class="hljs-comment"># 使用 Ruby China 的镜像安装 Ruby, 国内用户推荐</span>
git <span class="hljs-built_in">clone</span> git://github.com/AndorChen/rbenv-china-mirror.git ~/.rbenv/plugins/rbenv-china-mirror
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>homebrew安装</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash">$ brew install rbenv
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置</strong></p>
<p>安装完成后，把以下的设置信息放到你的 Shell 配置文件里面，以保证每次打开终端的时候都会初始化 rbenv。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">export</span> PATH=<span class="hljs-string">"<span class="hljs-variable">$HOME</span>/.rbenv/bin:<span class="hljs-variable">$PATH</span>"</span> 
<span class="hljs-built_in">eval</span> <span class="hljs-string">"<span class="hljs-subst">$(rbenv init -)</span>"</span>
<span class="hljs-comment"># 下面这句选填</span>
<span class="hljs-built_in">export</span> RUBY_BUILD_MIRROR_URL=https://cache.ruby-china.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置Ruby 环境，需重开一个终端。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ rbenv install --list   <span class="hljs-comment"># 列出所有 ruby 版本</span>
$ rbenv install 2.7.3      <span class="hljs-comment"># 安装 2.7.3版本</span>
$ rbenv versions               <span class="hljs-comment"># 列出安装的版本</span>
$ rbenv version                <span class="hljs-comment"># 列出正在使用的版本</span>
<span class="hljs-comment"># 下面三个命令可以根据需求使用</span>
$ rbenv global 2.7.3       <span class="hljs-comment"># 默认使用 1.9.3-p392</span>
$ rbenv shell 2.7.3       <span class="hljs-comment"># 当前的 shell 使用 2.7.3, 会设置一个`RBENV_VERSION` 环境变量</span>
$ rbenv <span class="hljs-built_in">local</span> 2.7.3   <span class="hljs-comment"># 当前目录使用 2.7.3, 会生成一个 `.rbenv-version` 文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">什么是 RubyGems</h3>
<blockquote>
<p>The RubyGems software allows you to easily download, install, and use ruby software packages on your system. The software package is called a “gem” which contains a packaged Ruby application or library.</p>
</blockquote>
<p>RubyGems 是 Ruby 的一个依赖包管理工具，管理着 Gem。用 Ruby 编写的工具或依赖包都称为 Gem。</p>
<p>RubyGems 还提供了 Ruby 组件的托管服务，可以集中式的查找和安装 library 和 apps。当我们使用 gem install 命令安装 Gem 时，会通过 rubygems.org 来查询对应的 Gem Package。而 iOS 日常中的很多工具都是 Gem 提供的，例如 Bundler，fastlane，jazzy，CocoaPods 等。</p>
<p>在默认情况下 Gems 总是下载 library 的最新版本，这无法确保所安装的 library 版本符合我们预期。因此还需要 Gem Bundler 配合。</p>
<p><a href="https://mp.weixin.qq.com/s/s2yJEb2P0_Kk-rIpYBi_9A" target="_blank" rel="nofollow noopener noreferrer">参考：版本管理工具及 Ruby 工具链环境</a></p>
<h3 data-id="heading-11">什么是 Bundler</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1586e0b0aee34292a27392cd9689f393~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://www.bundler.cn/" title="Bundler" target="_blank" rel="nofollow noopener noreferrer">Bundler</a> 是一个管理 Gem 依赖的 Gem，用来检查和安装指定 Gem 的特定版本，它可以隔离不同项目中 Gem 的版本和依赖环境的差异。</p>
<p>你可以执行 <code>gem install bundler</code> 命令安装 Bundler，接着执行 <code>bundle init</code> 就可以生成一个 Gemfile 文件，你可以在该文件中指定 CocoaPods 和 fastlane 等依赖包的特定版本号，比如：</p>
<pre><code class="copyable">source "https://rubygems.org"
gem "cocoapods", "1.10.0"
gem "fastlane", "> 2.174.0"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行 <code>bundle install</code> 来安装 Gem。 Bundler 会自动生成一个 Gemfile.lock 文件来锁定所安装的 Gem 的版本。</p>
<p>这一步只是安装指定版本的 Gem，使用的时候我们需要在 Gem 命令前增加 <code>bundle exec</code>，以保证我们使用的是项目级别的 Gem 版本（也就是 Gemfile.lock 文件中锁定的 Gem 版本），而不是操作系统级别的 Gem 版本。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ bundle <span class="hljs-built_in">exec</span> pod install
$ bundle <span class="hljs-built_in">exec</span> fastlane beta
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://t1.lagounews.com/kR50RoRgcj04C" target="_blank" rel="nofollow noopener noreferrer">参考：iOS开发进阶</a></p>
<h2 data-id="heading-12">优秀博客</h2>
<p>整理编辑：<a href="https://www.jianshu.com/u/739b677928f7" target="_blank" rel="nofollow noopener noreferrer">皮拉夫大王在此</a></p>
<p>1、<a href="https://mp.weixin.qq.com/s/O1haH28cTr0tkhRAnVZQ6g" title="我在Uber亲历的最严重的工程灾难" target="_blank" rel="nofollow noopener noreferrer">我在Uber亲历的最严重的工程灾难</a> -- 来自公众号：infoQ</p>
<p>准备或者已经接入Swfit可以先了解下</p>
<p>2、<a href="https://mp.weixin.qq.com/s/3qcv1NW4-ce87cvAS4Jsxg" title="美团 iOS 工程 zsource 命令背后的那些事儿" target="_blank" rel="nofollow noopener noreferrer">美团 iOS 工程 zsource 命令背后的那些事儿</a> -- 来自公众号： 美团技术团队</p>
<p>美团技术团队历史文章，对DWARF文件的另一种应用。文章还原了作者解决问题的思路历程，除了技术本身外，解决问题的思路历程也是值得借鉴的。</p>
<p>3、<a href="https://juejin.cn/post/6844904000450478087" title="NSObject方法调用过程详细分析" target="_blank">NSObject方法调用过程详细分析</a> -- 来自掘金：maniac_kk</p>
<p>字节跳动maniac_kk同学的一篇优质文章，无论深度还是广度都是非常不错的，很多底层知识融会贯通，值得细细品味</p>
<p>4、<a href="https://www.jianshu.com/p/958d4f109bb0" title="iOS疑难Crash的寄存器赋值追踪排查技术" target="_blank" rel="nofollow noopener noreferrer">iOS疑难Crash的寄存器赋值追踪排查技术</a> -- 来自简书：欧阳大哥</p>
<p>在缺少行号信息时如何通过寄存器赋值推断出具体的问题代码，具有很高的参考价值，在遇到疑难问题时可以考虑是否能借鉴此思路</p>
<p>5、<a href="https://juejin.cn/post/6950454120826765325" title="抖音 iOS 工程架构演进" target="_blank">抖音 iOS 工程架构演进</a> -- 来自掘金：字节跳动技术团队</p>
<p>业务的发展引起工程架构做出调整，文章介绍了抖音的工程架构演进历程。作为日活过亿的产品，其工程架构的演变对多数APP来说都具有一定的借鉴意义。</p>
<p>6、<a href="https://mp.weixin.qq.com/s/yiF0NwXffrkunGOieWbIRA" title="Swift的一次函数式之旅" target="_blank" rel="nofollow noopener noreferrer">Swift的一次函数式之旅</a> -- 来自公众号：搜狐技术产品</p>
<p>编程本身是抽象的，编程范例就是我们如何抽象这个世界的方法，而函数式编程就是其中一个编程范例。在函数式编程的世界里一切皆函数，那如何利用这个思想解决实际问题呢？文中给出了两个有趣的例子，希望可以帮你解决对函数式编程的疑惑。</p>
<p>7、<a href="https://zhangferry.com/2021/04/21/overwrite_system_category/" target="_blank" rel="nofollow noopener noreferrer">Category无法覆写系统方法？</a> -- 来自公众号：iOS成长之路</p>
<p>这是一次非常有趣的解决问题经历，以至于我认为解决方式可能比问题本身更有意思。解决完全没有头绪的问题，我们应该避免陷入不断的猜测和佐证中。深挖问题，找到正确方向才更容易出现转机。</p>
<h2 data-id="heading-13">学习资料</h2>
<p>整理编辑：<a href="https://juejin.cn/user/1433418892590136" target="_blank">Mimosa</a></p>
<p>1、<a href="http://www.cyc2018.xyz/" title="CS-Notes" target="_blank" rel="nofollow noopener noreferrer">CS-Notes</a></p>
<p>该「Notes」包含技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计、Java、Python、C++等内容，知识结构简练，内容扎实。该仓库的内容皆为作者及 Contributors 的原创，目前在 Github 上获 126k Stars。</p>
<p>2、<a href="https://oschina.gitee.io/learn-git-branching/" title="Learn Git Branching" target="_blank" rel="nofollow noopener noreferrer">Learn Git Branching</a></p>
<p>入门级的 Git 使用教程，用图形化的方式来介绍 Git 的各个命令，每一关都有一个小测试来巩固知识点。编者自己过了一遍了，体验很不错，同时填补了我自己一些 Git 知识上的漏洞和误区。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e1e1a7ef5e34751b5f55cf0b4e5ba69~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">开发利器</h2>
<p>整理编辑：<a href="https://juejin.cn/user/307518984425981/posts" target="_blank">brave723</a></p>
<h3 data-id="heading-15">OpenInTerminal</h3>
<p><strong>地址</strong>：<a href="https://github.com/Ji4n1ng/OpenInTerminal" target="_blank" rel="nofollow noopener noreferrer">github.com/Ji4n1ng/Ope…</a></p>
<p><strong>软件状态</strong>：免费，开源</p>
<p><strong>使用介绍</strong></p>
<p>OpenInTerminal 是一款开发辅助工具，可以增强 Finder 工具栏以及右键菜单增加在当前位置打开终端的功能。另外还支持：在编辑器中打开当前目录以及在编辑器中打开选择的文件夹或文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8f21f6dbee0410e94fc2f078b404a93~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-16">核心功能</h5>
<ul>
<li>在终端（或编辑器）中打开目录或文件</li>
<li>打开自定义应用</li>
<li>支持 终端iTerm</li>
</ul>
<h3 data-id="heading-17">SnippetsLib</h3>
<p><strong>地址</strong>：<a href="https://apps.apple.com/cn/app/snippetslab/id1006087419?mt=12" target="_blank" rel="nofollow noopener noreferrer">apps.apple.com/cn/app/snip…</a></p>
<p><strong>软件状态</strong>：$9.99</p>
<p><strong>使用介绍</strong></p>
<p>SnippetsLab是一款mac代码片段管理工具，使用SnippetsLab可以提高工作效率。它可以帮助您收集和组织有价值的代码片段，您可以随时轻松访问它们</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9da3d1b6e894f3daf7bedf624c24716~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">联系我们</h2>
<p><a href="https://zhangferry.com/2021/02/28/iOSWeeklyLearning_5/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第五期</a></p>
<p><a href="https://zhangferry.com/2021/03/14/iOSWeeklyLearning_6/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第六期</a></p>
<p><a href="https://zhangferry.com/2021/03/28/iOSWeeklyLearning_7/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第七期</a></p>
<p><a href="https://zhangferry.com/2021/04/11/iOSWeeklyLearning_8/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第八期</a></p></div>  
</div>
            