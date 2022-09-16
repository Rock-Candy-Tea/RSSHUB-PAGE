
---
title: 'Swift：巧用module.modulemap，告别Bridging-Header.h'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e99f0a1d3176496d8f1b78763f852ec0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sun, 04 Sep 2022 18:56:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e99f0a1d3176496d8f1b78763f852ec0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
</blockquote>
<h1 data-id="heading-0">前言 项目背景</h1>
<p>项目里面有这么一个需求，在一个App项目中创建多个Static Library，各司其职进行模块与职责划分。</p>
<p>别问为啥没有使用私有库Cocopods进行，反正目前就是为了方便后续各个Static Library，可以随便拖动到其他项目中进行复用。</p>
<p>然后，问题来了。</p>
<h1 data-id="heading-1">问题：在Static Library无法引用友盟的framework</h1>
<p>为了便于说明与演示，我特别创建了一个Demo，通过截图进行讲解。</p>
<p>我有个项目叫做TestUM，里面包含一个SomeSDK，我希望在SomeSDK里面，包含高德地图和友盟统计的功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e99f0a1d3176496d8f1b78763f852ec0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是乎，我在Podfile文件中进行了配置：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">target <span class="hljs-string">'SomeSDK'</span> <span class="hljs-keyword">do</span>

  <span class="hljs-comment"># Comment the next line if you don't want to use dynamic frameworks</span>

  use_frameworks!

  pod <span class="hljs-string">'AMapSearch'</span>, <span class="hljs-string">'= 8.1.0'</span>
  pod <span class="hljs-string">'AMapLocation'</span>, <span class="hljs-string">'= 2.8.0'</span>

  pod <span class="hljs-string">'UMCommon'</span>, <span class="hljs-string">'~> 1.3.4.P'</span>
  pod <span class="hljs-string">'UMSPM'</span>
  pod <span class="hljs-string">'UMCCommonLog'</span>

<span class="hljs-keyword">end</span>

target <span class="hljs-string">'TestUM'</span> <span class="hljs-keyword">do</span>

  <span class="hljs-comment"># Comment the next line if you don't want to use dynamic frameworks</span>

  use_frameworks!

  <span class="hljs-comment"># Pods for TestUM</span>
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，进行Pod的target是<code>SomeSDK</code>而非<code>TestUM</code>，<strong>但是实际上<code>TestUM</code>也是能引用高德与友盟的库。</strong></p>
<p>最后，根据友盟集成的文件，需要添加桥接文件进行处理：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09076dbec0ab4b7bb484fec99856d9a0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在TestUM下，我通过<code>import AMapFoundationKit</code>，我们可以顺利的调用高德的相关API，因为桥接了友盟，我也可以顺利的调用友盟的相关API：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce81d920ef62496b8bbd2294d2a7797c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而，在SomeSDK下，因为可以<code>import AMapFoundationKit</code>，我依旧可以调用高德，但是友盟却怎么也点不出来了：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/022bed40c9344f1784d7befddb4560cb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我尝试在SomeSDK也创建一个类似主工程中<code>Bridging-Header.h</code>的文件，对友盟进行桥接，然而得到的却是编译错误<code>using bridging headers with framework targets is unsupported</code>。</p>
<p>不支持，这条路被堵死了。</p>
<p>如果桥接行不通，SomeSDK就无法使用友盟统计的功能，只能将其相关业务移植到主工程去，这明显不符合公司要求。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3236cbe12a0b4f2daafd4ee020e3496b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="4f9dd5d4aba06d291d7b1e4d05683724.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>领导就一句话：高德可以，友盟为什么不行？</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f41a66d9adc449da92295347f55ecf8b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在回头看看，为何<strong>高德地图的既可以在TestUM又可以在SomeSDK中进行引用——因为它能在工程中的<code>*.swift</code>文件中进行<code>import</code>。</strong></p>
<p>而友盟在通过<code>TestUM-Bridging-Header.h</code>文件进行桥接后，在<code>TestUM</code>主工程的<code>.swift</code>文件中，无需import，直接调用即可，<strong>但是在<code>SomeSDK</code>的子工程中无法调用。</strong></p>
<p><strong>高德与友盟的架包到底有何差异？🤔🤔🤔</strong></p>
<h1 data-id="heading-2">AMapFoundationKit.framework与UMCommon.framework对比</h1>
<p>其实高德与友盟的Pod引用还是非常相似的，因为都是封装的静态库，Pod集成的都是非开源的.framework架包。</p>
<p>这里我们将AMapFoundationKit.framework与UMCommon.framework做一下对比：</p>





















<table><thead><tr><th>高德</th><th>友盟</th></tr></thead><tbody><tr><td><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49c97420326e440c8030ed7a174595ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35112d12f0894350ac76b0c46350e250~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94c4ac66755a44a899cef384c31c70bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Snip20220905_6.png" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94c4ac66755a44a899cef384c31c70bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Snip20220905_6.png" loading="lazy" referrerpolicy="no-referrer"></td></tr><tr><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30bc2deebaa147eea47fdb915d468d0c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a996e2e5a5134053b307496869b1940e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Snip20220824_21.png" loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<ol>
<li>通过Xcode展开工程看，Pod中，<code>AMapFoundationKit.framework</code>不仅展示了Frameworks文件夹，同时暴露的.h文件也显示了，而<code>UMCommon.framework</code>没有显示.h文件。</li>
<li>通过<code>AMapFoundationKit.podspec.json</code>与<code>UMCommon.podspec.json</code>，我们会发现虽然两者都是<code>.framework</code>的pod集成方式，但是在配置参数的差异方式决定了显示不同。</li>
<li>看.framework的文件结构，<strong>很明显的发现<code>AMapFoundationKit.framework</code>比<code>UMCommon.framework</code>多一个Module文件夹！</strong></li>
</ol>
<p>就让我们看看，这个Module文件夹下面吧。</p>
<p>里面就只有一个<code>module.modulemap</code>文件，里面长这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43cc67a6b32e4ebabf1c91e473a6d555~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>关于<code>umbrella header</code>大家可以看看参考文档<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F31238761%2Fwhat-is-an-umbrella-header" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/31238761/what-is-an-umbrella-header" ref="nofollow noopener noreferrer">What is an umbrella header?</a>，它的功能就是将<code>AMapFoundationKit.h</code>里面暴露的<code>.h</code>文件，通过循环都暴露出来。</strong></p>
<p><code>AMapFoundationKit.h</code>里面长这样：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e427107f4a974582bffc0620b058c8f9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>回想一下，我们可以在<code>*.swift</code>文件中可以<code>import AMapFoundationKit</code>是不是因为有<code>module.modulemap</code>中的配置缘故？</p>
<p>带着这个问题，我去搜索了一下<code>module.modulemap</code>的相关资料。</p>
<p>在一篇文章中我找到相关的信息与灵感：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/920c6c76d58a4a05b6afdc14bfba3e35~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>As <strong>Bridging-Header</strong> can help us in <strong>App Target</strong> and <strong>App Test Target</strong>, <strong>not in static library or dynamic libraries</strong> to use the Objective C / C APIs into Swift classes, <strong>modulemap</strong> can help us here.</p>
</blockquote>
<p><strong>通过理解，Pod这种<code>.framework</code>的静态库，在主工程的应用可以通过桥接解决，而在主工程的的static library则需要通过modulemap来进行解决。</strong></p>
<h1 data-id="heading-3">为UMCommon.framework手搓一个<code>module.modulemap</code></h1>
<p>本着死马当活马医的想法，我想为UMCommon.framework手搓一个<code>module.modulemap</code>。</p>
<p>首先我特地看了一下UMCommon.framework中Headers里面的文件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0a1ea2938ed4d7fa0b2fc87c6505149~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>抱着试一试的态度，我新建了Modules一个文件夹，并写了这样一个文件，<strong>注意我并没添加所有的.h文件,只是为了方便测试。</strong></p>
<pre><code class="hljs language-arduino copyable" lang="arduino">framework <span class="hljs-keyword">module</span> UMCommon &#123;

   header <span class="hljs-string">"MobClick.h"</span>

   header <span class="hljs-string">"UMConfigure.h"</span>

   header <span class="hljs-string">"UMCommon.h"</span>
   
   <span class="hljs-keyword">export</span> *

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后将其放到对应的UMCommon.framework。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06eb4858e0984981861833737dd79dcc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>见证结果的时刻来了，编译，试着import，成功了！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/758010c3e50c48d0a5eb8a179347c676~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们甚至可以，点击看看这个<code>import UMCommon</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91caafe82fa6479f9541c3b5f007f4ef~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>MobClick</code>类已经完美通过Swift表示了。</p>
<p>而且此时，我们可以把主工程里面的<code>Bridging-Header.h</code>里面桥接文件注释掉（甚至将这个<code>.h</code>文件删除），在<code>*.swift</code>中<code>import</code>对应的类，即可成功引入与调用！</p>
<h1 data-id="heading-4">总结</h1>
<ul>
<li>
<p>将Pod中的某些需要桥接的库，通过手搓一个<code>module.modulemap</code>，我们完全有能力<strong>抹去桥接操作</strong>，但是同时这样有一个问题，一旦Pod的库，升级或者文件进行了变更，自行写的<code>module.modulemap</code>可能也需要更改。</p>
<p>而且更改Pod下的库的文件，也不太符合操作规则。</p>
<p>另外，大家可以尝试把<code>AlipaySDK.framework</code>通过这种方式去除桥接试试，原理都是一样的，就当练手。</p>
</li>
<li>
<p>还有一种方式就是自己创建一个私有的Spec，自己添加<code>module.modulemap</code>后，进行pod库管理，但是这样还是避免不了上游更新，私有库也要同步更新的问题。</p>
</li>
</ul>
<p><strong>最好的Pod集成方式，就像高德的库，官方将<code>podspec</code>配置好，使用者直接傻瓜<code>pod install</code>就好了。</strong></p>
<h1 data-id="heading-5">参考文档</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F31238761%2Fwhat-is-an-umbrella-header" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/31238761/what-is-an-umbrella-header" ref="nofollow noopener noreferrer">What is an umbrella header?</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40mail2ashislaha%2Fswift-objective-c-interoperability-static-libraries-modulemap-etc-39caa77ce1fc" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@mail2ashislaha/swift-objective-c-interoperability-static-libraries-modulemap-etc-39caa77ce1fc" ref="nofollow noopener noreferrer">Swift Objective C interoperability, Static Libraries, Modulemap etc…</a></p>
<h1 data-id="heading-6">自己写的项目，欢迎大家star⭐️</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FseasonZhu%2FRxStudy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seasonZhu/RxStudy" ref="nofollow noopener noreferrer">RxStudy</a>：RxSwift/RxCocoa框架，MVVM模式编写wanandroid客户端。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FseasonZhu%2FGetXStudy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seasonZhu/GetXStudy" ref="nofollow noopener noreferrer">GetXStudy</a>：使用GetX，重构了Flutter wanandroid客户端。</p></div>  
</div>
            