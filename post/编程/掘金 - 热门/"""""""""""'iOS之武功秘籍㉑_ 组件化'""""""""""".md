
---
title: """""""""""'iOS之武功秘籍㉑_ 组件化'"""""""""""
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Mon, 08 Mar 2021 07:42:51 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a976d7fe55f14c07a2b3feeba801d616~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://juejin.cn/post/6936173181321347102" target="_blank">iOS之武功秘籍 文章汇总</a></p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>最近在思考团队扩张及项目数量增加的情况下，如何持续保障团队高效产出的问题，很自然的想到了组件化这个话题.以下是个人的梳理和思考.</p>
<p><a href="https://github.com/Tcj1988/objc4-818.2.git" target="_blank" rel="nofollow noopener noreferrer">本节可能用到的秘籍Demo</a></p>
<h2 data-id="heading-1">一、组件化</h2>
<p>谈到组件化，首先想到的是<code>解耦</code>，<code>模块化</code>.其实组件化就是<code>将模块进行抽离、分层</code>，并制定<code>模块间的通讯方式</code>，从而实现<code>解耦</code>的一种方式，<code>主要运用在团队开发</code>.</p>
<h3 data-id="heading-2">为什么需要组件化？</h3>
<p>主要有以下四个原因:</p>
<ul>
<li>1.模块间解耦</li>
<li>2.模块重用</li>
<li>3.提高团队协作开发效率</li>
<li>4.方便进行单元测试</li>
</ul>
<p>当项目因为各种需求，越来越大时，如果此时的各个模块之间是<code>互相调用</code>，即<code>你中有我，我中有你</code>这种情况时，会造成<code>高耦合</code>的情况.一旦我们需要对某一块代码<code>进行修改</code>时，就会<code>牵一发而动全身</code>，导致项目难以维护. 其问题主要体现在以下几个方面:</p>
<ul>
<li>1.修改某个功能时，同时需要修改其他模块的代码，因为在其他模块中有该模块的引用.可以理解为<code>高耦合导致代码修改困难</code></li>
<li>2.模块对外接口不明确，甚至暴露了本不该暴露的私有接口，修改时费时费力.可以理解为<code>接口不固定导致的接口混乱</code></li>
<li>3.高耦合代码产生的后果就是会影响团队其他成员的开发，<code>产生代码冲突</code></li>
<li>4.当模块需要重用到其他项目时，<code>难以单独抽离</code></li>
<li>5.模块间耦合的忌口导致接口和依赖关系混乱，<code>无法进行单元测试</code></li>
</ul>
<p>所以为了解决以上问题，我们需要采用<code>更规范的方式</code>来<code>降低模块间的耦合度</code>，然后组件化就应运而生，<code>组件化</code>也可以理解为<code>模块化</code>.</p>
<h3 data-id="heading-3">组件化的适用说明</h3>
<p>上面说了组件化的好处，但是因为<code>组件化</code>也是<code>需要一定成本的</code>，需要<code>花费时间设计接口</code>、<code>分离代码</code>等，所以<code>并不是所有</code>的项目都需要组件化.如果你的项目有以下<code>3个以上</code>特征就<code>不需要组件化</code>：</p>
<ul>
<li>1.<code>项目较小</code>，模块间交互简单，耦合少</li>
<li>2.项目<code>没有被多个外部模块</code>引用，只是一个单独的小模块</li>
<li>3.模块<code>不需要</code>重用，代码<code>也很少</code>被修改</li>
<li>4.团队<code>规模很小</code></li>
<li>5.<code>不需要编写单元测试</code></li>
</ul>
<p>如果你的项目有以下<code>3个以上</code>特征，说明你就必须要<code>考虑</code>进行组件化了：</p>
<ul>
<li>1.模块<code>逻辑复杂</code>，多个模块之间<code>频繁互相引用</code></li>
<li>2.项目<code>规模逐渐变大</code>，<code>修改代码</code>变的<code>越来越困难</code>（这里可以理解为：修改一处代码，需要同时修改其他多个地方）</li>
<li>3.团队<code>人数变多</code>，提交的代码经常和其他成员<code>冲突</code></li>
<li>4.项目<code>编译耗时较长</code></li>
<li>5.模块的<code>单元测试</code>经常由于<code>其他模块的修改</code>而<code>失败</code></li>
</ul>
<h3 data-id="heading-4">组件化的8条指标</h3>
<p>一个项目经过组件化后如何来评判项目组件化是否彻底或者说是否优秀，可以通过以下几个方面：</p>
<ul>
<li>1.<code>模块之间没有耦合</code>，模块内部的修改<code>不影响</code>其他模块</li>
<li>2.<code>模块可以单独编译</code></li>
<li>3.模块间<code>数据传递明确</code></li>
<li>4.模块可以<code>随时</code>被另一个提供了相同功能的模块<code>替换</code></li>
<li>5.模块对外接口清晰且易维护</li>
<li>6.当<code>模块接口改变</code>时，此<code>模块的外部代码</code>能够被<code>高效重构</code></li>
<li>7.尽量<code>用最少</code>的修改和代码，让现有的项目实现模块化</li>
<li>8.支持<code>OC和Swift</code>，以及混编</li>
</ul>
<p><code>前4条</code>主要用于<code>衡量一个模块是否真正解耦</code>，<code>后4条</code>主要用于<code>衡量在项目实践中的易用程度</code></p>
<h3 data-id="heading-5">组件化原则</h3>
<p>一般一个项目主要分为三层：<code>业务层</code>，<code>通用层</code>，<code>基础层</code>，具体如下图所示：<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a976d7fe55f14c07a2b3feeba801d616~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在进行组件化时，有以下几点需要说明：</p>
<ul>
<li>1.只能<code>上层对下层</code>依赖，不能<code>下层对上层</code>的依赖，因为下层是对上层的抽象</li>
<li>2.项目<code>公共代码资源下沉</code></li>
<li>3.横向的依赖尽量少有，最好下沉至通用模块或者基础模块</li>
</ul>
<h2 data-id="heading-6">二、组件化方案</h2>
<p>目前常用的组件化方案主要有两种：</p>
<ul>
<li>1·<code>本地</code>组件化：主要是通过在<code>工程中创建library</code>，利用<code>cocoapods</code>的<code>workspec</code>进行<code>本地管理</code>，<code>不需要</code>将项目上传<code>git</code>，而是直接在项目中<code>以framework的方式</code>进行调用</li>
<li>2.<code>cocoapods</code>组件化：主要是利用<code>cocoapods</code>来进行<code>模块的远程管理</code>，<code>需要</code>将项目上传<code>git</code>（这里的组件化模块分为<code>公有库</code>和<code>私有库</code>，对<code>公司而言</code>，<code>一般是私有库</code>）</li>
</ul>
<h3 data-id="heading-7">本地组件化</h3>
<h4 data-id="heading-8">1.创建主工程</h4>
<ul>
<li>首先创建主工程<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b790b1966604890b1b0429dab95c84f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>集成<code>cocopods</code>，进行本地管理,执行指令<code>pod init</code></li>
<li>编辑<code>podfile</code>，并执行<code>pod install</code></li>
</ul>
<h4 data-id="heading-9">2.创建组件</h4>
<p>可以创建自己的模块：</p>
<ul>
<li><code>主工程</code>：主要实现表层业务代码</li>
<li><code>Base</code>：基类封装</li>
<li><code>Tools</code>：工具（字符串，颜色，字体等）</li>
<li><code>Service</code>：服务层，封装业务工具类，例如网络层服务、持久化服务等</li>
<li><code>Pods</code>：第三方依赖</li>
</ul>
<p>其中，各个模块间的关系如下所示<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515a8fc8d0cf492c8635c4b2a58587f6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面我们进行简单的模块创建，我们以<code>Service</code>为例：</p>
<ul>
<li>1.选择<code>new -> project -> iOS -> Framework</code>，新建一个<code>模块</code><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da636a26be8a47d3aac1d95b31131b72~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>2.选择正确的<code>Group</code> 和 <code>WorkSpace</code>（这里需要注意一点：创建的<code>library</code>最好<code>放在主工程根目录</code>下，否则后续<code>podfile</code>执行<code>pod install</code>时会报错）<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b3dde887f5040da9483b327fb937730~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>3.将创建的<code>library</code>的<code>Build Settings -> Mach-O Type</code>修改为静态库<code>Static Library</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb5fd3f278c84902bbbd569260134510~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<h4 data-id="heading-10">3.主工程调用library</h4>
<p>在<code>TCJService</code>中新建一个文件，并添加如下代码<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402cc2c38a014837bafff1bd87bf5bd0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>在<code>Build Phases -> Headers -> Public</code>中将新建的文件添加为<code>public</code>，这样<code>主工程才能访问该文件</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/683fa7b6dbe941dfb03d838f5abdf8fd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>在主工程中，选择<code>target -> Linked Binary With Libraries</code>中添加<code>TCJService</code>，只需要<code>build</code>主工程，<code>library</code>能够自动联编<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3938f2f7499d4e36bde14c55a1b36afd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bae83a7d46234fd3b9f24e5a7759ba5f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>主项目调用:首先<code>import TCJService</code>，然后使用<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3301d428b5d84da7aa6ae7e84e9f1e81~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>这里需要注意的是，<code>子library</code>之间的<code>互相调用</code>，与<code>主工程调用library类似</code>，需要添<code>加依赖</code>、<code>暴露header</code>即可.</p>
<h4 data-id="heading-11">4.使用cocoapods管理三方依赖</h4>
<p>假设我们需要在<code>TCJService</code>中封装网络层代码，需要用到三方库<code>Alamofire</code>，在<code>podfile</code>中进行如下修改<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad387e4190dc4f0293af561208bbc7cb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96fcc6b16fc34f1cae4f76da636dfc69~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>到此，一个本地组件化的模块就配置完成了</p>
<h3 data-id="heading-12">cocoapods组件化</h3>
<p>除了本地组件化，还可以使用<code>cocoapods</code>，其原理如下图所示<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/159a7450f7814fbf9032677423d14f6a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这里还是以本地组件化中的结构为例</p>
<h4 data-id="heading-13">1、创建私有仓库 -- 创建私有Spec Repo</h4>
<p>私有库当然要用私有<code>Spec Repo</code>，当然可以使用官方的<code>Repo</code>，但如果只想添加自己的<code>Pods</code>，那还是使用私有的<code>Repo</code>把.打开：<code>~/.cocoapods/repos</code>.你会看到一个<code>master</code>文件夹，这个是 <code>Cocoapods</code> 官方的 <code>Spec Repo</code>.</p>
<ul>
<li>在<code>github</code>上创建一个<code>TCJDemoSpecs</code>仓库来作为私有的<code>Repo</code></li>
</ul>
<p>具体步骤：登录<code>github</code>-->点击<code>右上角“+”</code>-->选择 <code>new repository</code>-->输入<code>Repository name</code>为<code>TCJDemoSpecs</code>，选择仓库类型为 <code>private</code>，点击<code>Create repository</code>.</p>
<ul>
<li>执行<code>repo</code>命令添加私有<code>Repo</code>,将私有仓库添加至本地<code>~/.cocoapods/repos</code>目录</li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc">pod repo add TCJDemoSpecs https:<span class="hljs-comment">//github.com/Tcj1988/TCJDemoSpecs.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时如果成功的话，到：~/.cocoapods/repos 目录可以看到<code>TCJDemoSpecs</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79aea2c5d6074a0bb23d2da541d138eb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">2、Using Pod Lib Create创建pods工程，即组件化工程:组件库</h4>
<ul>
<li>创建一个<code>TCJDemoSpecs</code>项目.<code>cd到</code>想要创建项目的目录然后使用终端执行 -- <code>pod lib create TCJDemoSpecs</code></li>
<li>根据提示依次选择<code>iOS，Objc，Yes，None，No,TCJ</code></li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d19c2bde24b54f75901d947a13184871~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>进入模块目录，将需要的文件<code>拷贝</code>到<code>TCJDemoSpecs -> Classes</code>中<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fdd39fe79fb47f6b2f9c6f3e9bf6a0f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><code>cd</code>到<code>Example文件夹</code>执行<code>pod install</code>,会将<code>Classes</code>更新至pods中<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fc75956fdbb462c870a2fbe1344af06~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h4 data-id="heading-15">3、配置pods工程</h4>
<p>修改模块的配置文件，即<code>TCJDemoSpecs.podspec</code></p>
<ul>
<li>如果需要依赖第三方库，需要配置<code>s.dependency</code></li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc">s.dependency <span class="hljs-string">'AFNetworking'</span> # 依赖AFNetworking
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果模块间需要相互引用，同样需要配置<code>s.dependency</code>，以<code>TCJBase</code>为例，需要引用<code>TCJDemoSpecs</code></li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">//********1、修改 podspec 文件</span>
s.dependency <span class="hljs-string">'TCJDemoSpecs'</span>

<span class="hljs-comment">//********2、修改 podfile 文件</span>
pod <span class="hljs-string">'TCJDemoSpecs'</span>, :path => <span class="hljs-string">'../../TCJServices'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果需要加载资源，例如<code>图片、json、bundle</code>文件等
<ul>
<li>创建Images.xcassets用来存放TCJServices组件的图片</li>
<li>2.在<code>specs</code>里配置资源路径（必须配置！！否则无法读取资源）</li>
<li>3.访问时需要指定资源文件路径</li>
</ul>
</li>
</ul>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a0312dc50734d518d3500d965b0d18d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么怎样获取图片呢?
在前面我们添加的<code>TCJUtils</code>类里面写了一个类方法:<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d73ccb326fd49ea8774e970dd4ea3a3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a5e666334d746179acb3af7a1dfc4e5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用示例：在<code>Example</code>工程的<code>ViewController</code>中直接导入<code>TCJUtils</code><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56a6b93412844f95bbd2c384aa04e1fa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>运行结果:<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65edd813de234464a34ef41e3f9d44cd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>同理，模块中的<code>xib</code>，<code>json</code>文件的获取方式也是一样的</p>
<h4 data-id="heading-16">4、提交至git</h4>
<p>这里提交至<code>git</code>的模块是<code>pods</code>工程才可以，以<code>TCJDemoSpecs</code>为例, 我们刚才在<code>git</code>建了一个私有库：<code>TCJDemoSpecs</code>.</p>
<ul>
<li>执行以下终端命令<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93969a8a8b7741f4a76d2071902fc084~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a39ec6bf9e4c118d9d644d53055338~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<h4 data-id="heading-17">5、验证podspec文件</h4>
<p>执行终端命令 <code>pod spec lint --allow-warnings</code>,加上 <code>--allow-warnings</code>为了移除警告</p>
<blockquote>
<p><code>pod spec</code>相对于<code>pod lib</code>会更为精确
<code>pod lib</code>相当于<code>只验证</code>一个<code>本地仓库</code>
<code>pod spec</code>会<code>同时验证本地仓库和远程仓库</code></p>
</blockquote>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d1714fe3b354cafb67f398b53b7c9ed~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">6、提交到私有仓库</h4>
<p>执行以下命令：<code>pod repo push [本地Spec Repo名称][podspec文件路径]</code>
<code>pod repo push TCJDemoSpecs TCJDemoSpecs.podspec --allow-warnings</code><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55ce7a59057c42bb80706a997412fcd9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">7、使用</h4>
<ul>
<li>
<p>新建一个工程<code>PodsTest</code>，在项目的<code>podfile</code>里添加<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76ff287b32f646d5817cd2e3ddb81b87~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>执行<code>pod install</code>即可<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fb7147a6a7d40e58964fee497a2a2b5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>执行成功后打开项目：</p>
</li>
</ul>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbb0bf7369b44def97499f36cfd23d98~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>在 <code>PodsTest</code> 中的 <code>ViewController</code> 使用组件的东西：</li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbde5b7c5c74439aac1ba1cac5dab34f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>至此我们对<code>cocoapods</code>组件化已经完成，下面我们要介绍下组件化之间的通信.</p>
<h2 data-id="heading-20">三、组件化通讯方案</h2>
<p>目前主流的主要有以下三种方式：</p>
<ul>
<li>1.<code>URL</code>路由</li>
<li>2.<code>target-action</code></li>
<li>3.<code>protocol</code>匹配</li>
</ul>
<h3 data-id="heading-21">协议试编程</h3>
<p>在<code>编译层面使用协议定义规范</code>，<code>实现在不同地方</code>，从而达到<code>分布管理</code>和<code>维护组件的目的</code>.这种方式也遵循了<code>依赖反转</code>原则，是一种很好的<code>面向对象编程</code>的实践.</p>
<p>但是方案也很明显：</p>
<ul>
<li>由于<code>协议式编程缺少统一调度层</code>，导致<code>难于集中管理</code>，特别是<code>项目规模变大</code>、<code>团队人数变多</code>的情况下，<code>架构管控就会显得越来越重要</code></li>
<li><code>协议式编程接口</code>定义模式<code>过于规范</code>，从而使得架构的<code>灵活性不够高</code>.当需要引入一个<code>新的设计模式来开发</code>时，我们就会发现<code>很难融入到当前架构中</code>，<code>缺乏架构的统一性</code>.</li>
</ul>
<h3 data-id="heading-22">中间者</h3>
<p>它采用<code>中间者统一管理</code>的方式，来控制<code>App的整个生命周期中组件间的调用关系</code>.同时<code>iOS对于组件接口的设计</code>也需要<code>保持一致性</code>，方便中间者统一调用.</p>
<p><code>拆分的组件</code>都会<code>依赖于中间者</code>，但是<code>组间之间</code>就<code>不存在相互依赖的关系</code>了.由于<code>其他组件</code>都会<code>依赖</code>于这个<code>中间者</code>，<code>相互间的通信</code>都会<code>通过中间者统一调度</code>，所以<code>组件间的通信</code>也就<code>更容易管理</code>了.在中间者上也<code>能够轻松添加新的设计模式</code>，从而使得架构<code>更容易扩展</code></p>
<p><strong>好的架构一定是健壮的、灵活的</strong>.<code>中间者架构</code>的<code>易管控带来的架构更稳固</code>，<code>易扩展带来的灵活性</code>.</p>
<h3 data-id="heading-23">URL路由</h3>
<p>这也是很多<code>iOS</code>项目使用的<code>通信方案</code>，它就是基于<code>路由匹配</code>，或者<code>根据命名约定</code>，用<code>runtime方法进行动态调用</code>，<code>URL路由思路</code>采用了<code>中间者模式</code>.</p>
<p>这些<code>动态化的方案</code>的<code>优点是实现简单</code>，<code>缺点</code>是需要<code>维护字符串表</code>，或者<code>依赖于命名约定</code>，<code>无法在编译时</code>暴露出所有问题，<code>需要在运行时</code>才能发现错误.</p>
<h4 data-id="heading-24">URL路由的优缺点</h4>
<p><strong>【优点】</strong></p>
<ul>
<li><code>极高的动态性</code>，适合<code>经常</code>展开运营活动的<code>app</code>.例如：电商类</li>
<li><code>方便统一管理</code>多平台的路由规则</li>
<li><code>易于适配URL Scheme</code></li>
</ul>
<p><strong>【缺点】</strong></p>
<ul>
<li><code>传参方式有限</code>，<code>并且无法利用编译期进行参数类型检查</code>（所有的参数都是通过字符串转换而来）</li>
<li><code>只适用于界面模块</code>，<code>不适用于通用模块</code></li>
<li><code>参数格式不明确</code>，是个灵活的<code>dictionary</code>，还需要有个地方查看参数格式</li>
<li><code>不支持storyboard</code></li>
<li><code>依赖于字符串硬编码</code>，难以管理，<code>蘑菇街为此专门</code>做了一个后台管理这部分</li>
<li><code>无法保证所有使用的模块一定存在</code></li>
<li><code>解耦能力有限</code>，<code>URL</code>的"注册"，"实现"，"使用"必须使用<code>相同的字符串规则</code>，一旦任何一方做出修改都会导致其他地方的代码失效，并且<code>重构难度大</code></li>
</ul>
<p><code>URL路由方式</code>主要是<code>以蘑菇街</code>为代表的<a href="https://github.com/meili/MGJRouter" target="_blank" rel="nofollow noopener noreferrer">MGJRouter</a></p>
<h4 data-id="heading-25">MGJRouter</h4>
<p>其实现思路是：</p>
<ul>
<li><code>App启动时</code>实例化各组件模块，然后这些<code>组件向MGJRouter注册URL</code>，有时候<code>不需要实例化</code>，使<code>用Class注册</code>.<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/295d78e2ebad42a09c8823b1945c23a2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>当<code>组件A</code>需要调用<code>组件B</code>时，向<code>ModuleManager传递URL</code>，参数跟随<code>URL</code>以<code>GET</code>方式传递，类似<code>openURL</code>.然后由<code>ModuleManager</code>负责调度<code>组件B</code>，最后完成任务.<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88e41b32a6d3484b9cc98dadee4f51d1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p>除了上面的<code>MGJRouter</code>，还有以下三方框架</p>
<ul>
<li><a href="https://github.com/clayallsopp/routable-ios" target="_blank" rel="nofollow noopener noreferrer">routable-ios</a></li>
<li><a href="https://github.com/joeldev/JLRoutes" target="_blank" rel="nofollow noopener noreferrer">JLRoutes</a></li>
<li><a href="https://github.com/lightory/HHRouter" target="_blank" rel="nofollow noopener noreferrer">HHRouter</a></li>
</ul>
<h3 data-id="heading-26">target-action</h3>
<p>这个方案是基于<code>OC</code>的<code>runtime</code>、<code>category</code>特性<code>动态获取模块</code>，例如通过<code>NSClassFromString</code>获取类并创建实例，通过<code>performSelector+NSInvocation</code>动态调用方法</p>
<p>这种方式主要是以<code>casatwy</code>的<a href="https://github.com/casatwy/CTMediator" target="_blank" rel="nofollow noopener noreferrer">CTMediator</a>为代表,其实现思路是：</p>
<ul>
<li>1.<code>利用分类</code>为<code>路由添加新的接口</code>，在<code>接口</code>通过<code>字符串获取对应的类</code></li>
<li>2.通过<code>runtime</code>创建实例，<code>动态调用实例的方法</code></li>
</ul>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">//******* 1、分类定义新接口</span>
public extension <span class="hljs-built_in">CTMediator</span>&#123;
    @objc func A_showHome()-><span class="hljs-built_in">UIViewController</span>?&#123;
        let params = [
            kCTMediatorParamsKeySwiftTargetModuleName: <span class="hljs-string">"TCJLHome"</span>
        ]
        
        <span class="hljs-keyword">if</span> let vc = <span class="hljs-keyword">self</span>.performTarget(<span class="hljs-string">"A"</span>, action: <span class="hljs-string">"Extension_HomeViewController"</span>, params: params, shouldCacheTarget: <span class="hljs-literal">false</span>) as? <span class="hljs-built_in">UIViewController</span>&#123;
            <span class="hljs-keyword">return</span> vc
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>
    &#125;
&#125;

<span class="hljs-comment">//******* 2、模块提供者提供target-action的调用方式（对外需要加上public关键字）</span>
<span class="hljs-keyword">class</span> Target_A: <span class="hljs-built_in">NSObject</span> &#123;
    
    @objc public func Action_Extension_HomeViewController(_ params: [String: Any])-><span class="hljs-built_in">UIViewController</span>&#123;
         
        let home = HomeViewController()
        <span class="hljs-keyword">return</span> home
    &#125;

&#125;

<span class="hljs-comment">//******* 3、使用</span>
<span class="hljs-keyword">if</span> let vc = <span class="hljs-built_in">CTMediator</span>.sharedInstance().A_showHome() &#123;
            <span class="hljs-keyword">self</span>.navigationController?.pushViewController(vc, animated: <span class="hljs-literal">true</span>)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模块间的引用关系如下：<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb1cf96eab1342398854186c36483844~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>【优点】：</strong></p>
<ul>
<li>利用<code>分类</code>可以<code>声明接口</code>，进行<code>编译检查</code></li>
<li>实现方式<code>轻量级</code></li>
</ul>
<p><strong>【缺点】:</strong></p>
<ul>
<li>需要在<code>mediator</code>和<code>target</code>中<code>重新添加</code>每一个<code>接口</code>，<code>模块化时代码较为繁琐</code></li>
<li>在<code>category</code>中仍然要<code>引入字符串硬编码</code>，内部使用<code>字典传参</code>，一定程度上也存在和<code>URL路由相同的问题</code></li>
<li><code>无法保证使用的模块一定存在</code>，<code>target在修改后</code>，使用者只能在<code>运行时才能发现错误</code></li>
<li>创建<code>过多的target</code>类，导致<code>target类泛滥</code></li>
</ul>
<h4 data-id="heading-27">CTMediator源码分析</h4>
<ul>
<li>
<p><code>CTMediator</code>使用<code>URL路由处理</code>:这个方法主要是针对远程<code>APP</code>的互相调起,通过<code>openURL</code>实现<code>APP</code>之间的跳转,通过<code>URL</code>进行数据传递<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2273f2d0ea344a3d92e10c2e8e17ae42~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><code>CTMediator</code>使用的是<code>运行时解耦</code>，解耦核心方法如下所示：<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e92589f5b64b8fa25a5bcb790f4373~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><code>performTarget:action:params:shouldCacheTarget:</code>方法主要是对 <code>targetName</code>和<code>actionName</code>进行容错处理，也就是对调用方法无响应的处理.</li>
<li>这个方法封装了<code>safePerformAction:target:params</code> 方法，入参<code>targetName</code>就是调用接口的对象，<code>actionName</code>是调用的方法名，<code>params</code>是参数.</li>
<li>并且代码中同时还能看出只有满足<code>Target_ 前缀的类的对象</code>和<code>Action_的方法才能被CTMediator使用</code>.这时，我们可以看出中间者架构的优势，也就是利于统一管理，可以轻松管控制定的规则.</li>
</ul>
</li>
<li>
<p>进入<code>safePerformAction:target:params:</code>实现，主要是通过<code>invocation</code>进行<code>参数传递+消息转发</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94e692636a15454ba78997f45b2606d9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-28">protocol class</h3>
<p><code>protocol</code>匹配的<code>实现思路</code>是：</p>
<ul>
<li>1.将<code>protocol</code>和对应的<code>类</code>进行<code>字典匹配</code></li>
<li>2.通过用<code>protocol</code>获取<code>class</code>，再<code>动态创建实例</code></li>
</ul>
<p><code>protocol</code>比较典型的三方框架就是<a href="https://github.com/alibaba/BeeHive" target="_blank" rel="nofollow noopener noreferrer">阿里的BeeHive</a>.<code>BeeHive</code>借鉴了<code>Spring Service、Apache DSO</code>的架构理念，<code>采用AOP+扩展App生命周期API</code>形式，将<code>业务功能</code>、<code>基础功能</code>模块以模块方式解决大型应用中的复杂问题，并让<code>模块之间以Service形式调用</code>，将复杂问题切分，<code>以AOP方式模块化服务</code>.</p>
<h4 data-id="heading-29">BeeHive 核心思想</h4>
<ul>
<li>1.<code>各个模块间调用</code>从<code>直接调用对应模块</code>，变成<code>调用Service的形式</code>，<code>避免直接依赖</code></li>
<li>2.<code>App</code>生命周期的分发，<code>将耦合在AppDelegate中逻辑拆分</code>，每个模块以<code>微应用</code>的形式独立存在</li>
</ul>
<p><strong>【优点】</strong></p>
<ul>
<li>1.<code>利用接口调用</code>，实现参数传递时的<code>类型安全</code></li>
<li>2.直接使用模块的<code>protocol</code>接口，<code>无需再重复封装</code></li>
</ul>
<p><strong>【缺点】</strong></p>
<ul>
<li>1.用<code>框架来创建所有对象</code>，创建方式不同，即不支持外部传参</li>
<li>2.用<code>OC</code>的<code>runtime</code>创建对象，<code>不支持Swift</code></li>
<li>3.只做了<code>protocol</code>和<code>class</code>的匹配，<code>不支持更复杂的创建方式和依赖注入</code></li>
<li>4.<code>无法保证所以使用的protocol一定存在对应的模块</code>，也<code>无法直接判断</code>某个<code>protocol</code>是否能用于获取模块.</li>
</ul>
<p>除了<code>BeeHive</code>还有<a href="https://github.com/Swinject/Swinject" target="_blank" rel="nofollow noopener noreferrer">Swinject</a></p>
<h4 data-id="heading-30">BeeHive 模块注册</h4>
<p>在<code>BeeHive</code>中主要是通过<code>BHModuleManager</code>来管理各个模块的.<code>BHModuleManager</code>中只会管理<code>已经被注册过的模块</code></p>
<p><code>BeeHive</code>提供了<code>三种</code>不同的调用形式，<code>静态plist</code>，<code>动态注册</code>，<code>annotation</code>.<code>Module</code>、<code>Service</code>之间<code>没有关联</code>，<code>每个业务模块</code>可以<code>单独实现Module</code>或者<code>Service的功能</code>.</p>
<h5 data-id="heading-31">Annotation方式注册</h5>
<p>这种方式主要是通过<code>BeeHiveMod</code>宏进行<code>Annotation</code>标记<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d030031d9104e448ff732889a1390bd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这里针对<code>__attribute</code>需要说明以下几点</p>
<ul>
<li>第一个参数<code>used</code>：用来<code>修饰函数</code>，被<code>used</code>修饰以后，即使函数没有被引用，在<code>Release</code>下也不会被优化.如果<code>不加这个修饰</code>，那么<code>Release环境链接器下会去掉没有被引用的段</code>.</li>
<li>通过使用<code>__attribute__((section("name")))</code>来<code>指明哪个段</code>.数据则用<code>__attribute__((used))</code>来标记，<code>防止链接器会优化删除未被使用的段</code>，然后将模块注入到<code>__DATA</code>中.</li>
</ul>
<p>此时<code>Module</code>已经被存储到<code>Mach-O</code>文件的特殊段中，那么如何取呢？</p>
<ul>
<li>进入<code>BHReadConfiguration</code>方法，主要是通过<code>Mach-O</code>找到存储的数据段，<code>取出放入数组中</code><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fdc766443634bba88bc17dc0a0291ef~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<h5 data-id="heading-32">读取本地Pilst文件</h5>
<ul>
<li>
<p>首先，需要设置好路径<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5cd709a3177405e95de515332035e20~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>创建<code>plist</code>文件，<code>plist</code>文件的格式也是数组中包含多个字典.字典里面有<code>两个key</code>，一个是<code>"moduleLevel"</code>，另一个是<code>"moduleClass"</code>.注意<code>根的数组的名字</code>叫<code>"moduleClasses"</code>.<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a4199e5df684bc08195bceb03d05828~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>进入<code>loadLocalModules</code>方法，主要是从<code>plist</code>里面取出数组，然后把数组加入到<code>BHModuleInfos</code>数组里<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55f7719f61f7427f82d664ce1628ba0c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8debed2eb643b28e76ef3a45d8f14b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h5 data-id="heading-33">动态注册 -- load方法注册</h5>
<ul>
<li>
<p>该方法注册<code>Module</code>就是在<code>load</code>方法里面注册<code>Module</code>的类<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b41bfaf93242ae94557f9467cee3b0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>进入<code>registerDynamicModule</code>实现<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a39ad5274c44a76970aabcc80784dd1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6941d06cbc994275ac7cdb1a41f9f274~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>其底层还是同第一种方式一样，最终会走到<code>addModuleFromObject:shouldTriggerInitEvent:</code>方法中</p>
<ul>
<li><code>load</code>方法，还可以使用<code>BH_EXPORT_MODULE</code>宏代替<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c396bbfbc81d4bf7a0f59f3ddd4415c0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p><code>BH_EXPORT_MODULE</code>宏里面可以传入一个参数，代表<code>是否异步加载Module模块</code>，如果是<code>YES</code>就是<code>异步加载</code>，如果是<code>NO</code>就是<code>同步加载</code>.</p>
<h4 data-id="heading-34">BeeHive模块事件</h4>
<p><code>BeeHive</code>会给每个模块提供生命周期事件<code>，用于与</code>BeeHive<code>宿主环境进行必要</code>信息交互<code>，</code>感知模块生命周期的变化`.</p>
<p><code>BeeHive</code>各个模块会收到一些事件.在<code>BHModuleManager</code>中，所有的事件被定义成了<code>BHModuleEventType</code>枚举.如下所示，其中有<code>2个事件很特殊</code>，一个是<code>BHMInitEvent</code>，一个是<code>BHMTearDownEvent</code>. <img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/753648f55a5140ad9204d4203f76b60d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>主要分三种事件:</strong></p>
<ul>
<li>1.<code>系统事件</code>：主要是指<code>Application</code>生命周期事件<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3692e5b249964a37a275864a6de954b6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p>一般的做法是<code>AppDelegate</code>改为继承自<code>BHAppDelegate</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7cccd952e274d63a06788b92aa84122~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>2.<code>应用事件</code>：官方给出的流程图，其中<code>modSetup</code>、<code>modInit</code>等，可以用于<code>编码实现各插件模块的设置与初始化</code>.<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bce5ca65f6ad428c8224f0d098b647b9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>3.自定义事件</p>
</li>
</ul>
<p>以上所有的事件都可以通过调用<code>BHModuleManager</code>的<code>triggerEvent:</code>来处理.<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b13a637c93245caaa7c5c797a348d5c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/366b663aafe54879b1e614407cef5750~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的代码中可以发现，除去<code>BHMInitEvent</code>初始化事件和<code>BHMTearDownEvent</code>拆除<code>Module</code>事件这两个特殊事件以外，所有的事件都是调用的<code>handleModuleEvent:forTarget:withSeletorStr:andCustomParam:</code>方法，其内部实现主要是遍历 <code>moduleInstances</code> 实例数组，调用<code>performSelector:withObject:</code>方法实现对应方法调用<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e55aa7ca06d44f88f873b9d693c0c21~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
注意:这里所有的<code>Module</code>必须是遵循<code>BHModuleProtocol</code>的，否则无法接收到这些事件的消息</p>
<h4 data-id="heading-35">BeeHive模块调用</h4>
<p>在<code>BeeHive</code>中是通过<code>BHServiceManager</code>来管理各个<code>Protocol</code>的.<code>BHServiceManager</code>中只会管理<code>已经被注册</code>过的<code>Protocol</code>.</p>
<p>注册<code>Protocol</code>的方式总共有三种，和注册<code>Module</code>是一样一一对应的.</p>
<h5 data-id="heading-36">Annotation方式注册</h5>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">//****** 1、通过BeeHiveService宏进行Annotation标记</span>
BeeHiveService(HomeServiceProtocol,BHViewController)

<span class="hljs-comment">//****** 2、宏定义</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">define</span> BeeHiveService(servicename,impl) \
class BeeHive; char * k##servicename##_service BeeHiveDATA(BeehiveServices) = <span class="hljs-meta-string">"&#123; \""</span>#servicename<span class="hljs-meta-string">"\" : \""</span>#impl<span class="hljs-meta-string">"\"&#125;"</span>;</span>

<span class="hljs-comment">//****** 3、转换后的格式，也是将其存储到特殊的段</span>
<span class="hljs-keyword">char</span> * kHomeServiceProtocol_service __attribute((used, section(<span class="hljs-string">"__DATA,"</span><span class="hljs-string">"BeehiveServices"</span><span class="hljs-string">" "</span>))) = <span class="hljs-string">"&#123; \""</span><span class="hljs-string">"HomeServiceProtocol"</span><span class="hljs-string">"\" : \""</span><span class="hljs-string">"BHViewController"</span><span class="hljs-string">"\"&#125;"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-37">读取本地plist文件</h5>
<ul>
<li>
<p>首先同<code>Module</code>一样，需要先设置好路径<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b328761c7147288b3212dda7697585~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>设置plist文件<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8ec1b8908841559194b6e61bd80361~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>同样也是在<code>setContext</code>时注册<code>services</code><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e3a7ace484240dea70eb01b6fa1196c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2231fbaa002494f9b167ef017d97c9c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dced596c0c34ded8fddcae60d83a00e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h5 data-id="heading-38">protocol注册</h5>
<p>主要是调用<code>BeeHive</code>里面的<code>createService:</code>完成<code>protocol</code>的注册<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a2b40d069014bbf852a1ff6fd7294aa~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d900e1feba34081bd755c94d3ad5b8e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40ed9ae40544710a95507ea3ac7a672~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>createService</code>会先检查<code>Protocol</code>协议是否是注册过的.然后接着取出字典里面对应的<code>Class</code>，如果实现了<code>shareInstance</code>方法，那么就创建一个单例对象，如果没有，那么就创建一个实例对象.如果还实现了<code>singleton</code>，就能进一步的把<code>implInstance</code>和<code>serviceStr</code>对应的加到<code>BHContext</code>的<code>servicesByName</code>字典里面<code>缓存起来</code>.这样就可以随着上下文传递了</p>
<p>进入<code>serviceImplClass</code>实现，从这里可以看出<code>protocol</code>和<code>类</code>是通过<code>字典</code>绑定的，<code>protocol作为key</code>，<code>serviceImp（类的名字）作为value</code>.<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b4c4ab98be4f2dafc1d28628960c4e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-39">Module & Protocol</h4>
<p>简单的总结一下:</p>
<ul>
<li>对于<code>Module</code>：数组存储</li>
<li>对于<code>Protocol</code>：通过<code>字典</code>将<code>protocol与类进行绑定</code>，<code>key为protocol</code>，<code>value为 serviceImp</code>即类名.</li>
</ul>
<h4 data-id="heading-40">辅助类说明</h4>
<ul>
<li>
<p><code>BHConfig</code>类：是一个<code>单例</code>，其内部有一个<code>NSMutableDictionary</code>类型的<code>config</code>属性，该属性维护了一些动态的环境变量，作为<code>BHContext</code>的补充存在</p>
</li>
<li>
<p><code>BHContext</code>类：是一个<code>单例</code>，其内部有两个<code>NSMutableDictionary</code>的属性，分别是<code>modulesByName</code> 和 <code>servicesByName</code>.这个类主要用来保存上下文信息的.例如在<code>application:didFinishLaunchingWithOptions:</code>的时候，就可以初始化大量的上下文信息<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4291c77eed2143a4b63e76c88f2b6cad~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><code>BHTimeProfiler</code>类：用来进行<code>计算时间性能</code>方面的<code>Profiler</code></p>
</li>
<li>
<p><code>BHWatchDog</code>类：用来<code>开一个线程</code>，<code>监听主线程是否堵塞</code>.</p>
</li>
</ul>
<h2 data-id="heading-41">写在后面</h2>
<p>和谐学习,不急不躁.我还是我,颜色不一样的烟火.</p>
<p><strong>参考链接</strong></p>
<p><a href="https://juejin.cn/post/6844903583356305421" target="_blank">BeeHive —— 一个优雅但还在完善中的解耦框架</a></p>
<p><a href="https://www.zybuluo.com/pockry/note/657651" target="_blank" rel="nofollow noopener noreferrer">BeeHive，一次iOS模块化解耦实践</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            