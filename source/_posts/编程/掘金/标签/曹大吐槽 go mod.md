
---
title: '曹大吐槽 go mod'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f163f511179f49e0b48cf5e7074e5b29~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 23:38:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f163f511179f49e0b48cf5e7074e5b29~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>从 rsc 力排众议设计并将 go mod 集成在 Go 语言中，已经两年过去了，时至今日，广大 Gopher 还是经常被 go mod 相关的问题折磨。</p>
<p>本文会列举一些我和我的同事使用 go mod 时碰到的问题，有些问题是 go mod 本身的问题，有些可能是第三方 goproxy 实现的问题。</p>
<p>如果你做过比较大型的 go 项目开发，相信总会有那么几个让你会心一笑。</p>
<h2 data-id="heading-0">Go 命令的副作用</h2>
<p>从老版本一路升级过来的 gopher 很难理解为什么升级了新版本之后，go fmt 一个文件都变得非常卡顿。</p>
<p>go 的很多子命令都在引入 go mod 后增加了副作用，如 go test，go fmt(ide 常用)，go build，go list(ide 常用)。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f163f511179f49e0b48cf5e7074e5b29~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>例如上面的 <code>go fmt</code>，我只是想格式化一下我的文件，并没有想下载依赖，但还是得耐心等依赖下载完毕。</p>
<p>go test 时会自动修改 go.mod 文件就更令人困惑了：<a href="https://stackoverflow.com/questions/61625796/why-go-mod-keeps-changing-with-go-test" target="_blank" rel="nofollow noopener noreferrer">why go mod keeps changing with go test</a>，<a href="https://github.com/golang/go/issues/30921" target="_blank" rel="nofollow noopener noreferrer">go.mod be modified after go test</a>。</p>
<p>这也是 go.mod 和 go.sum 为什么总是会出现在我们的文件变更列表里。何况这两个文件在大项目开发的时候又尤其容易冲突。</p>
<h2 data-id="heading-1">go.sum git 合并冲突</h2>
<p>当很多同事在同一个 git 仓库中做开发时，即使我们已经划分好了工作职责，在代码合并的时候还是没有办法 auto merge：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/108af304c9264b98a42a48089e97d02b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>类似上面这样的合并冲突，下面躺着 go.sum 的情况相信你也见过很多了。</p>
<h2 data-id="heading-2">形同虚设的 semver 规范</h2>
<p>go mod 的设计认为社区是严格遵守 semver 的规范的：</p>
<blockquote>
<p>Given a version number MAJOR.MINOR.PATCH, increment the:<br>
MAJOR version when you make incompatible API changes,<br>
MINOR version when you add functionality in a backwards compatible manner, and<br>
PATCH version when you make backwards compatible bug fixes.</p>
</blockquote>
<p>小版本升级，如 1.7.4 -> 1.7.5 不应该引入不兼容升级，不过显然 Google 高估了开源社区的节操。不少开源库作者 API 修改起来都比较随便。</p>
<p>即使是 Google 自己的 grpc-go 项目，也在小版本升级中干过不兼容的事情：<a href="https://github.com/grpc/grpc-go/issues/3798" target="_blank" rel="nofollow noopener noreferrer">Update your SemVer Policy Please - Breaking changes in minor versions causing heartache</a>。</p>
<p>何况 grpc-go 的作者还光明正大地承认，他们在 semver 的前提下，依然允许一些不兼容的 <a href="https://github.com/grpc/grpc-go/blob/master/Documentation/versioning.md" target="_blank" rel="nofollow noopener noreferrer">例外</a>。</p>
<p>甚至还有那些从 release notes 中不易察觉的 <a href="https://codeengineered.com/blog/2018/golang-vgo-semver-human-error/" target="_blank" rel="nofollow noopener noreferrer">behavior change</a> 导致依赖 grpc-go 的 helm 项目在生产环境中遇到了 bug，令人大为光火。</p>
<p>好样的，Google 工程师。</p>
<p>除了人的问题之外，在 semver 规范中还存在一种例外情况：</p>
<blockquote>
<p>Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.</p>
</blockquote>
<p>go mod 设计时并未考虑这种情况，mvs 算法在 0.y.z 范围内也会尽量在大版本不变的情况下，无情地帮你升级小版本，搞的百姓怨声载道，苦不堪言。</p>
<p>这两年爆火的云原生领域，有很多项目在 0.x.y 版本一待就是两三年。从业者依赖 0.x 的版本号再正常不过了。如果你问 go mod replace 谁用的最溜？那想必是云原生开发者啦。</p>
<h2 data-id="heading-3">版本信息扩散</h2>
<p>由于 go mod 的设计，如果一个依赖库升级了新版本，我们的 import 路径就会发生变化：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d96e81bebc3141378ab08cfed1d612dc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>chi 项目升级 v5 了，所有引入 chi 下 lib 的代码都需要改 import，开心不开心。我们又要升级兼容新的 API，又要改这些到处散落的 import path。</p>
<p>这绝对不能说是优秀的设计。</p>
<h2 data-id="heading-4">goproxy 的实现各不相同</h2>
<p>因为特殊原因，国内的 gopher 基本都需要配置国内公司 / 个人开发的 goproxy 来加速依赖下载，这些 proxy 没有使用相同的代码，所以实现细节上经常会有差别。</p>
<p>例如，当某个库不存在时，有的 goproxy 返回 404，而有的 goproxy 返回 500(这是笔者使用某司 goproxy 时的真实情况)，匪夷所思。</p>
<p>我们来看一下更加令人诧异的例子，来帮你理解这种匪夷所思。</p>
<h2 data-id="heading-5">删库跑路</h2>
<p>简单做个实验，遵从以下步骤：</p>
<ol>
<li>在 github 上创建仓库 A</li>
<li>通过 goproxy X 来 go build</li>
<li>删除仓库 A</li>
<li>删除 mod cache，并使用 goproxy X/Y/Z 分别执行 go build</li>
</ol>
<table><thead><tr><th>第一次 go build</th><th>删库后 goproxy.cn</th><th>删库后 goproxy.io</th><th>删库后 腾讯 goproxy</th><th>删库后 aliyun goproxy</th></tr></thead><tbody><tr><td>goproxy.cn</td><td>可 build</td><td>不可 build</td><td>不可 build</td><td>不可 build</td></tr><tr><td>goproxy.io</td><td>可 build</td><td>可 build</td><td>不可 build</td><td>不可 build</td></tr><tr><td>腾讯 goproxy</td><td>可 build</td><td>不可 build</td><td>可 build</td><td>不可 build</td></tr><tr><td>aliyun goproxy</td><td>可 build</td><td>不可 build</td><td>不可 build</td><td>可 build</td></tr></tbody></table>
<p>这次选取了国内使用最广泛的四个 goproxy，使用其中之一缓存过一次的外部依赖，在删库后还是可以 build 的。但如果之前未经该 goproxy 缓存的依赖，目前只有 goproxy.cn 依然能够正常地下载依赖。</p>
<p>经过对原作者的咨询，目前 goproxy.cn 在未找到依赖，但 gosumdb 中有值时，会去官方的 index.golang.org 上进行查找，而 gosumdb 中有值时，一般情况下官方的 proxy.golang.org 中会有相应的缓存 (即使你设置的是第三方 goproxy)。这时 goproxy.cn 也会将从官方 goproxy 中拉取，所以用户的 build 还是能成功的。</p>
<p>一个不带 vendor 的项目，理论上就会出现因为 gopher 使用的 GOPROXY 不一样，导致薛定谔的 build 结果。</p>
<p>如果我们细看一下 sum.golang.org，官方对外部库的缓存期限描述也是比较模糊的。</p>
<h2 data-id="heading-6">模糊的存储期限</h2>
<blockquote>
<p>proxy.golang.org does not save all modules forever. There are a number of reasons for this, but one reason is if proxy.golang.org is not able to detect a suitable license. In this case, only a temporarily cached copy of the module will be made available, and may become unavailable if it is removed from the original source and becomes outdated. The checksums will still remain in the checksum database regardless of whether or not they have become unavailable in the mirror.</p>
</blockquote>
<p>上面这段话来自 sum.golang.org，从官方的这种说法来看，依赖库在 goproxy 中的存储并不是永久的，至少在 proxy.golang.org 中不是永久的，官方给出的 a number of reasons 也非常的模糊。</p>
<p>我们没有办法把工作赌在这种虚无缥缈的措辞上，只能认为 goproxy 不会永久缓存我们的仓库。没有办法指望我们的依赖能够永远存在。原仓库从 github 消亡之后，迟早有一天也会在各个 goproxy 上消亡，reproducible build 沦为笑谈。</p>
<p>即使在 go mod 推出的两年后，对于我们来说，把依赖保存在 vendor 中依然是必要的。</p>
<p>多年前，left pad 在 js 社区引起的悲剧，也许并没有给当前的软件设计者提供多少教训：<br>
<a href="https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code/" target="_blank" rel="nofollow noopener noreferrer">how one programmer broke the internet</a>，<a href="https://www.davidhaney.io/npm-left-pad-have-we-forgotten-how-to-program/" target="_blank" rel="nofollow noopener noreferrer">have we forgotten how to program</a>。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            