
---
title: 'Rubick 的 star 数破 1k 的心路历程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef9b1f8fc6d4f949d5e9a0bdb76efc3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 02:59:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef9b1f8fc6d4f949d5e9a0bdb76efc3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前几个月在 github 上开源了一款基于 <code>electron</code> 实现的工具箱：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FclouDr-f2e%2Frubick" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/clouDr-f2e/rubick" ref="nofollow noopener noreferrer">Rubick</a> 。出发点是为了解决公司内部插件无法发布到 <code>uTools</code> 生态但又需要类似 <code>uTools</code> 那样的插件化能力。同时开源社区也希望了解当前社区内是否也有这样的诉求，或许可以帮助我们更好的完善和改进。在开源的过程中还是遇到了不少问题和挑战，谨以此文记录与 <code>Rubick</code> 有关的我的心路历程。</p>
<h2 data-id="heading-0">项目体验安装</h2>
<p>github 项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FclouDr-f2e%2Frubick" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/clouDr-f2e/rubick" ref="nofollow noopener noreferrer">Rubick</a></p>
<p>工具下载链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FclouDr-f2e%2Frubick%23%25E5%25AE%2589%25E8%25A3%2585%25E5%258C%2585" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/clouDr-f2e/rubick#%E5%AE%89%E8%A3%85%E5%8C%85" ref="nofollow noopener noreferrer">下载体验</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef9b1f8fc6d4f949d5e9a0bdb76efc3~tplv-k3u1fbpfcp-watermark.image" alt="demo" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">项目孵化</h2>
<h3 data-id="heading-2">启蒙</h3>
<p>Electron 是 GitHub 开源的一个框架。它通过 Node.js 和 Chromium 的渲染引擎完成跨平台的桌面 GUI 应用程序的开发。我起初没有接触过 Electron，最开始接触 <code>electron</code> 是因为看到了 <code>PicGo</code> 作者在掘金上推广他的图床工具。他的一个核心功能非常吸引我，就是 <code>macos</code> 下可以直接拖拽图片进入任务托盘上传图片：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6052407ab720424ebfacb4029a8a4570~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当时正好我们团队也需要搞一个内部的 cdn 图片资源管理图床，用于项目图片资源压缩并直接上传到 cdn 上，之前我们做了个网页版。而这里我深刻的感受到了 <code>electron</code> 的强大，可以极大的提高工作效率，参考 <code>PicGo</code>，我尝试做了第一个 <code>electron</code> 项目，完成了基于 <code>tinypng</code> 的图片压缩上传到内部 cdn 的桌面端应用。</p>
<h3 data-id="heading-3">演化</h3>
<p>之后公司内部因为开发需要，需要和后端进行接口联调，测试环境的时候，经常会涉及到一些状态改变要看交互样式的问题。比如测试需要测商品的待支付、支付中、支付完成等各种节点的交互样式是否符合预期，这种情况测试一般会去造数据或者让后端改数据库接口。有的小伙伴可能会用 <code>Charles</code> 修改返回数据进行测试。但是 <code>Charles</code> 的抓包体验和配置体验感觉有点麻烦，对新人不是很友好，所以我们自己做了个非常易用 <code>抓包&mock</code> 工具：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe19cfe19ff4fb099202c7a87addc7f%7Etplv-k3u1fbpfcp-watermark.image" alt="抓包" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>这也是 <code>Rubick</code> 最早的雏形。</strong> 随后，我们发现，当页面发布线上的时候，没有办法在微信环境内对线上页面进行调试，所以开发了一个基于 <code>winner</code> 的远程调试功能：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5add0779932746da9364ca754759f829~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>随着 <code>Rubick</code> 在内部不断推广和使用，所需功能也越来越多。我们需要 <code>需求管理</code>、<code>一键VPN</code>、<code>性能评估</code>、<code>埋点检测</code> 等等工具。这些工具的增加一方面导致我们的 <code>Rubick</code> 体积暴增，一方面又导致了用户需要不断更新软件，导致用户体验非常差。</p>
<p>其次，我们在推广给测试、UI同学使用的时候，发现他们其实并不关注前面的页面调试、性能测评等功能，可能只是用到其中某一项，所以整个项目对他们来说就显得很臃肿。</p>
<h3 data-id="heading-4">灵感</h3>
<p>直到有一天，我在掘金上看到这样一个沸点：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/966854586d0a47e7aa17e751058ba275~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面有个评论提到了 uTools 这是我第一次和 uTools 产生了交集，在体验了 uTools 功能后，我长吸一口气：这不就是我想要的嘛！然后就去 GitHub 上找 uTools 的源码，发现它并没有开源。</p>
<p>所以就想把上面提到的那些工具， 发布到 uTools 市场在 uTools 里通过插件的方式使用他们。但我发现发布插件只能发布到公网，但这又涉及到数据安全的问题。</p>
<p>无奈，难道真的要自己做一个这样的工具吗？真的是有点头大。不过想想也挺有意思的。至此，我萌生了要开发一个媲美 uTools 的开源工具箱的念头。</p>
<h2 data-id="heading-5">研发</h2>
<p>开篇第一步，按照我之前的套路都是先取好名字先占个坑，之前写了一本《从0开始可视化搭建》的小册，里面基于 dota 取了个 <code>coco</code> 的名字。这次我取名的是 <code>rubick</code> 即 <code>拉比克</code>。Rubick(拉比克) 是 dota 里面的英雄之一，其核心技能是插件化使用其他英雄的技能，用完即走。非常符合本工具的设计理念，所以取名 <code>Rubick</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33a4e360a4044315a719910131f56bd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">支持插件化</h3>
<p>我们的核心目标就是需要让 <code>Rubick</code> 支持插件化，解决前面提到的问题。当复制 <code>plugin.json</code> 进入搜索框时，变可直接出现 2个选项，一个新建插件，一个复制路径的功能：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a22b242ba7046e790f45595bd255d4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">运行插件</h3>
<p>运行插件是比较有意思的一个环节，接下来我会稍微介绍一下实现原理：</p>
<p>运行插件需要容器，electron 提供了一个 <code>webview</code> 的容器来加载外部网页。所以我们可以借助 <code>webview</code> 的能力实现动态网页渲染，这里所谓的网页就是插件。但是网页无法使用<code>node</code>的能力，而且我们做插件的目的就是为了开放与约束，需要对插件开放一些内置的 <code>API</code> 能力。好在 <code>webview</code> 提供了一个 <code>preload</code> 的能力，可以在页面加载的时候去预置一个脚本来执行。</p>
<p>也就是说我们可以给自己的插件写一个 <code>preload.js</code> 来加载。但这里需要注意我们既要保持插件的个性又得向插件内注入全局 <code>API</code> 供插件使用，所以可以直接加载 <code>rubick</code> 内置 <code>preload.js</code>，<code>preload.js</code> 内再加载个性化的 <code>preload.js</code>:</p>
<pre><code class="hljs language-html copyable" lang="html">// webview plugin.vue
<span class="hljs-tag"><<span class="hljs-name">webview</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"webview"</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"path"</span> <span class="hljs-attr">:preload</span>=<span class="hljs-string">"preload"</span>></span><span class="hljs-tag"></<span class="hljs-name">webview</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"index.vue"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">`File://<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.$route.query.sourceFile&#125;</span>`</span>,
      <span class="hljs-comment">// 加载当前 static 目录中的 preload.js</span>
      <span class="hljs-attr">preload</span>: <span class="hljs-string">`File://<span class="hljs-subst">$&#123;path.join(__static, <span class="hljs-string">'./preload.js'</span>)&#125;</span>`</span>,
      <span class="hljs-attr">webview</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">query</span>: <span class="hljs-built_in">this</span>.$route.query,
      <span class="hljs-attr">config</span>: &#123;&#125;,
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <code>preload.js</code> 我们就可以这么用啦：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (location.href.indexOf(<span class="hljs-string">'targetFile'</span>) > -<span class="hljs-number">1</span>) &#123;
  filePath = <span class="hljs-built_in">decodeURIComponent</span>(getQueryVariable(<span class="hljs-string">'targetFile'</span>));
&#125; <span class="hljs-keyword">else</span> &#123;
  filePath = location.pathname.replace(<span class="hljs-string">'file://'</span>, <span class="hljs-string">''</span>);
&#125;


<span class="hljs-built_in">window</span>.utools = &#123;
  <span class="hljs-comment">// utools 所有的 api 实现</span>
&#125;
<span class="hljs-comment">// 加载插件 preload.js</span>
<span class="hljs-built_in">require</span>(path.join(filePath, <span class="hljs-string">'../preload.js'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里就已经实现了一个最基础的插件加载，我们来看看效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33b05667411441b7b8a65b58dc20f6f7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">支持更多体验能力</h3>
<p>随后为了更加贴近 uTools 的体验，我又开始着手让 Rubick 支持更多原生体验增强的特性：超级面板、模板、系统命令、全局快捷键等</p>
<h4 data-id="heading-9">超级面板</h4>
<p>长按鼠标右键，即可呼起超级面板，可以根据当前鼠标选择内容，匹配对应插件能力。比如当前选择图片后长按右击，则会呼起上传图床插件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1706cc730f1f46078cb700a445211317~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">模板</h4>
<p>为了更贴合 <code>uTools</code> 的插件能力，需要实现模板功能，模板即是一个内置 UI 样式的功能插件。</p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b113ad547974699b9c73c28bc09b9b1~tplv-k3u1fbpfcp-watermark.image" width="500" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-11">系统命令</h4>
<h5 data-id="heading-12">取色</h5>
<p>基于 <code>robot.js</code> 以及 <code>iohook</code> 实现。未使用 C++ 扩展。输入框内输入 <code>取色</code> 或者 <code>colorpocker</code> 唤起</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3036ae85bf3549fc8bbbe2926ecbad55~tplv-k3u1fbpfcp-watermark.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">截屏</h5>
<p>输入框内输入 <code>shortcut</code> 或者 <code>截屏</code> 唤起</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18023dab52e1420c9e87362cefddb2a1~tplv-k3u1fbpfcp-watermark.image" width="500" loading="lazy" referrerpolicy="no-referrer">
<h4 data-id="heading-14">全局快捷键</h4>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62cc424eacac4c9eb178f0e055e87d9a~tplv-k3u1fbpfcp-watermark.image" width="500" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-15">最后</h2>
<p>再次致敬 uTools！如果没有它就没有 Rubick，我做 Rubick 旨在技术分享，并不以商业化为目的。</p>
<p>以上就是我和 Rubick 的故事，如果 Rubick 对您有帮助，那么就请给个 Star ✨ 鼓励一下：</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FclouDr-f2e%2Frubick" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/clouDr-f2e/rubick" ref="nofollow noopener noreferrer">github.com/clouDr-f2e/…</a></p>
</blockquote>
<hr>
<p>机缘巧合我发现了 <strong>HelloGitHub 一个推荐开源项目的平台</strong>，了解到卤蛋也是喜欢打 Dota，我想那他应该能感受到 Rubick 的魅力，所以我就抱着试一试的心态投稿了。也有幸入选了月刊<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA5MzYyNzQ0MQ%3D%3D%26mid%3D2247508947%26idx%3D1%26sn%3D370a95b6142c5645eb585c55a8bffa6a%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzA5MzYyNzQ0MQ==&mid=2247508947&idx=1&sn=370a95b6142c5645eb585c55a8bffa6a&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">第 64 期</a></p>
<p>最后，感谢 HelloGitHub 让 Rubick 被更多人发现和喜欢，特别感谢卤蛋对文章的润色和修改，让本文增色不少。</p></div>  
</div>
            