
---
title: 'iOS之武功秘籍㉒_ AFNetworking最新源码解析与面试考点延伸'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1f9afbfca94a38819aa9fcec77585b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 13 Mar 2021 01:32:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1f9afbfca94a38819aa9fcec77585b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://juejin.cn/post/6936173181321347102" target="_blank">iOS之武功秘籍 文章汇总</a></p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>最近重读了AFNetworking 4.x的源码，算是温故而知新吧.也梳理了一些优秀的代码细节和面试考点，罗列下来，发现这个库小而精致，简直初学者的宝藏库.</p>
<p><a href="https://github.com/AFNetworking/AFNetworking" target="_blank" rel="nofollow noopener noreferrer">AFN在GitHub中的地址</a>
<a href="https://github.com/Tcj1988/objc4-818.2.git" target="_blank" rel="nofollow noopener noreferrer">本节可能用到的秘籍Demo</a></p>
<h2 data-id="heading-1">一、开源库怎么看？</h2>
<p>先说个题外话，阅读优质的开源代码库，绝对是程序员们快速提升自我的有效途径，而怎样高效率的去阅读源码同样也是一个问题，不知道有没有人和我之前一样，碰到过读倒是读了，但总感觉收获不大的情况.</p>
<p>这里分享一下我的一些读码经验：</p>
<ol>
<li>
<p>多思考，多抛出问题，比如说</p>
<ul>
<li>整体的代码结构是怎样的？类与类之间的关系是怎样的？为什么要这么设计？</li>
<li>代码有没有涉及到多线程，其线程模型是怎样的？哪类问题可以适用这种多线程的方案？</li>
<li>代码中使用了哪些设计模式？具体是怎么实现的？</li>
</ul>
</li>
<li>
<p>也可以关注代码细节，遇到不熟悉的用法不要放过，多刨根究底才能夯实基础</p>
<p>关于<code>AFNetworking</code>的一些优秀代码细节，我这里也整理了一部分，可以查阅后文</p>
</li>
<li>
<p>一定要记笔记和总结，能分享更好</p>
<p>参考费曼学习法，我认为这一点是最好的加深理解和强化记忆的手段.随着年龄的增大，记忆力会有所衰退，有个笔记能够回顾，能节约大把再次记忆的时间.此外，多与人分享，与人交流验证，也能够为自己查缺补漏.</p>
</li>
</ol>
<h2 data-id="heading-2">二、AFNetworking 4.x的代码结构</h2>
<p>还是说回到<code>AFNetworking</code>这里，<code>AF</code>的代码结构大部分人应该都了解，这里我先简单介绍下.<code>AFNetworking 4.x</code>的代码结构比<code>2.x</code>要简单许多，主要也得益于苹果优化了网络相关的<code>api</code>，整体代码有这么几部分：</p>
<p><img alt="16152774422553.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1f9afbfca94a38819aa9fcec77585b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从<code>AF3.x</code>版本开始剔除了<code>NSURLConnection</code></p>
</blockquote>
<p><img alt="16152807855121.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c285f304e4af44b58f805f9c0d63f163~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>AFURLSessionManager/AFHTTPSessionManager</strong></p>
<p>这里就是<code>AF</code>代码的核心了，主要负责网络请求的发起，回调处理，是在系统网络相关<code>API</code>上的一层封装.大部分逻辑是在<code>AFURLSessionManager</code>里面处理的，<code>AFHTTPSessionManager</code>则是专为<code>HTTP</code>请求提供了一些便利方法.如果需要扩展其他协议的功能（比如<code>FTP</code>协议），可以考虑从<code>AFURLSessionManager</code>创建一个子类.</p>
</li>
<li>
<p><strong>AFURLRequestSerialization/AFURLResponseSerialization</strong></p>
<p>这两兄弟主要处理一些参数序列化相关的工作.<code>AFURLRequestSerialization</code>是将传入的参数构造成<code>NSURLRequest</code>，比如自定义的<code>header</code>，一些<code>post</code>或者<code>get</code>参数等等. <code>AFURLResponseSerialization</code>主要是将系统返回的<code>NSURLResponse</code>处理成我们需要的<code>responseObject</code>，比如<code>json、xml、image</code>等等.</p>
</li>
<li>
<p><strong>AFSecurityPolicy</strong></p>
<p>处理<code>https</code>相关的公钥和验证逻辑.目前由于苹果<code>ATS</code>的开启，基本<code>HTTPS</code>已经成为标配.虽然通常直接使用<code>CA</code>来验证服务器公钥的情况下，不需要我们额外做什么配置.但是从这里出发，顺便考察一下<code>HTTPS</code>相关的知识点，感觉也比较常见，具体面试题可看下文</p>
</li>
<li>
<p><strong>AFNetworkReachabilityManager</strong></p>
<p>这个其实是比较独立的一个模块了，提供获取当前网络状态的功能.</p>
</li>
<li>
<p><strong>UIKit+AFNetworking</strong></p>
<p>这里主要是通过<code>Category</code>来提供了一下<code>UIkit</code>的便利方法</p>
</li>
</ul>
<h3 data-id="heading-3">AFURLSessionManager/AFHTTPSessionManager</h3>
<h4 data-id="heading-4">① manager初始化</h4>
<p>说到<code>manager</code>的初始化.我想问问大家<code>manager</code>的设计模式是什么呢?
我猜想肯定有一大部分人会说是<code>单例模式</code>,哈哈,如果你在面试的时候这样说,那面试官可能会叫你回去等消息吧.
<strong>其实<code>manager</code>所用到的设计模式是<code>工厂设计模式</code></strong>.</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/333661c1f40b4245988377ef8ed40f7d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dc843382acc4a9485af12d4110d6a94~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
查看父类<code>AFURLSessionManager</code>的<code>initWithSessionConfiguration</code>方法
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86e1e99486da432782439d4725f423a6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这其中,又有一个考点哦.即<code>self.operationQueue.maxConcurrentOperationCount = 1;</code>为什么要这样呢?能不能多开几个线程呢?---<code>答案是不能</code>,鉴于一些多线程数据访问的安全性考虑.同时苹果官方也告诉我们不能
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7947f0d0825b45d7ae58f887b358ddeb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">② request方法封装</h4>
<p>我们都知道一个完整的请求 <code>request</code> 应该包括 <code>请求行+请求头+请求体</code>.
<code>请求行</code>我们后面再讲,先讲讲<code>AF</code>是如何封装<code>请求头</code>和<code>请求体</code>的.</p>
<p>以<code>get</code>请求为例来看看,进入到<code>AF</code>中<code>get</code>请求实现的方法<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83ab149310144d1197a79ff47321d5eb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这里主要是返回一个<code>dataTask</code>和<code>开始网络请求</code>,并没有告诉我们是如何封装请求头的,我们继续进入<code>dataTaskWithHTTPMethod:</code>方法<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33b320e0f9554627a160077aff613817~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这个方法作用主要是:</p>
<ul>
<li>① <code>生成request</code></li>
<li>② 通过<code>request</code>生成<code>dataTask</code>.</li>
</ul>
<p>那么它是如何封装生成request的呢?快跟上我的车队,继续进入<code>requestWithMethod:</code>方法<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06963851c02847d1be8f30113078898e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在<code>requestWithMethod</code>方法中，做了三件事情：</p>
<ul>
<li>① 创建<code>mutableRequest</code>并设置其请求方法；</li>
<li>② 把当前类设置的一些属性设置给<code>mutableRequest</code> -- <code>请求头的配置</code>;<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1b34de4b99046fa82d2fb3e86d80633~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a2e45ccce034144b487418712671cae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<pre><code class="hljs language-! copyable" lang="!">如果我们没有设置超时时间,那就是使用默认的超时时间为60s...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要利用<code>KVO</code>的响应式编程技术
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b00dcfad327a4db78ac5e519bc0450de~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/877278f0d0fa45e4b15eb57ddcfce703~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>③ 把需要传递的参数进行编码并且设置到<code>mutableRequest</code>当中 -- <code>请求参数封装</code>,调用<code>requestBySerializingRequest:</code>方法<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed78de3196ae4ddf84782ae0863de2b0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p>这个方法中主要做了以下几件事:</p>
<ul>
<li>① 从当前请求队列中拿到<code>self.HTTPRequestHeaders</code>的参数，赋值到要请求的<code>request</code>中.</li>
<li>② 把<code>网络请求的参数</code>转换为<code>NSString</code>类型，这一步是对<code>参数进行转码</code>-- 这是我们的重点,主要是调用<code>AFQueryStringFromParameters</code>方法.</li>
<li>③ 将请求方法拼接到<code>url</code>中:<code>GET、HEAD、DELETE</code>这几个<code>method</code>的<code>query</code>是拼接到<code>url</code>后面的,而<code>POST、PUT</code>是把<code>query</code>拼接到<code>http body</code>中的.</li>
</ul>
<p>接下来我们着重来看看,<code>AF</code>是怎么把我们传入的参数字典转成字符串的.进入<code>AFQueryStringFromParameters</code>方法<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96244f7385d94197a583a9e2a03de4d8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
通过递归调用并解析，直到解析的除了<code>array，dic，set</code>以外的元素，然后将最终得到的参数返回,接着③的步骤继续处理.</p>
<h4 data-id="heading-6">③ task与代理的关系</h4>
<p>接着上面的分析,我们刚刚讲了<code>AF</code>如何把<code>网络请求的参数</code>转换为<code>NSString</code>类型,现在我们来看看<code>AF</code>又是如何把请求方法拼接到<code>url</code>中的---这就来到了我们的重点<code>task</code>与<code>代理</code>的关系.进入<code>dataTaskWithRequest:</code>方法
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18807a1b2a14abd9807599db44ae63c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fb113fc582f4e55992a8fa509bdd191~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这里要注意一点这个方法是由<code>AFURLSessionManager</code>管理的,而不是<code>AFURLSessionManagerTaskDelegate</code><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22040e3803d64594a90a9258716345a3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么最后他们为什么要关联以及关联在一起呢?想知道吗?想的话我们继续<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270ef61d5c034c38985611a8573db1b3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
结合前面我们有这时的持有关系为<code>manager-->session-->task--->delegate--->manager</code>,那这不就构成了循环引用了吗?那AF是怎么解决这个问题的呢??<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f9d09c02384f569502264b6173680a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/745c22665e9f4195aa3a80dac75ffd9b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c1a5c58ee734bc380d50e770c081100~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
之后又回到我们的<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d4fb92d6aad4bbcb60a9429754f3a29~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>经过上面的过程,接下来就是调用<code>[dataTask resume];</code>方法了.这个<code>resume</code>是有问题的,老铁,<code>AF</code>在底层有给它做了一些骚操作..这里我将揭露他的秘密之处.
其实他在这里做了一个内部类<code>_AFURLSessionTaskSwizzling</code>,在这个类里面将<code>resume</code>和<code>af_resume</code>进行了交换.
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6b51e61a9d42db9c7e6acefa5f74c0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ab9fe45daf345efb275e76293d83d3e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们在来看看<code>AF</code>搞的骚操作的<code>af_resume</code>的实现<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfffc26e07a445ecb6f755bbf60a95d3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
其实在这个<code>AF</code>框架里面,我们都能拿到<code>task</code>状态.那么这个通知是给谁的呢?来一起来瞧瞧<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4c9dbe420df4152b2e9cbe28619e36a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
竟然给了<code>AFURLSessionManager</code>.因为它一个大管家,权限大.哈哈.</p>
<p>最后来总结一下这部分的整个流程,如下所示
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f00ece55fca447d2a8bd1198cb9966ba~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">AFURLRequestSerialization/AFURLResponseSerialization</h3>
<h4 data-id="heading-8">① NSObject, NSSecureCoding, NSCopying协议</h4>
<p>来到<code>AFURLRequestSerialization</code>类声明的地址,我们会发现它遵循了<code>NSObject, NSSecureCoding, NSCopying</code>这个三个协议.<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27d7b16263694feeb87b07b163d61fce~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
主要是让<code>AFURLRequestSerialization</code>具备<code>copy</code>和<code>归档</code>等一系列功能.</p>
<h4 data-id="heading-9">② 多表单对数据的封装</h4>
<p>对于多表单是怎么处理的呢?来直接看源码<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e78c5c2032045eda9481ff980142d0f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
通过上面的方法(在上传图片或断点续传的时候调用)进入<code>multipartFormRequestWithMethod:</code>方法<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a4e7c95bb04e2fb610a7203c1ea837~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们先来看下生产<code>formData</code>的<code>initWithURLRequest:</code>方法<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce7b33f5f6a46d883cbb50583b68d26~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着在来看看<code>AFCreateMultipartFormBoundary</code>这个分隔符<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69009ae90ac5400d85694c27e2d51cb7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着我们返回来,继续看<code>AF</code>是如何处理<code>parameters</code>的,它将进行一系列的格式化,生成相应的<code>AFQueryStringPair</code>对,最后进行拼接调用<code>appendPartWithFormData</code>方法
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b792692f56c043f2aac0c6b9575ddf4b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07e3114e091f4788adf491a46c1e9ab7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其整体流程就是
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e319089d0eb94acf9ecf73e71c7c67fb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8803a0149a340aab5dff0cec62f7360~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里要注意<code>多表单</code>的<code>Content-Type</code>和普通<code>post</code>表单的是不同的,普通的<code>Content-Type</code>是<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aeca69c073f94120836f6d15346800c8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
而<code>多表单</code>的则是
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474ecb381bc04899ac291c561306a309~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90a3701a53554e428f2c4b7ea963ef91~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着来看看<code>contentLength</code>是怎么拼接的
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80533c739ad4e7b959816024c763777~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4d839b069324f39b78d506550fca5ea~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">② Stream流程</h4>
<p>那么拼接后的数据又是如何处理的呢?回顾前面说的<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70b0fcf4279f480d855dbeaaecfaa32b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这个方法中就设置了<code>stream</code>.先来看看<code>HTTPBodyStream</code>属性<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20bd7600f3124bc08d5dca9ffa8da784~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
源码告诉我们<code>stream</code>默认是关闭的,我们要先开启,在去读它.之后在调用<code>NSInputStream</code>相关的代理.<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61934030e44340648e9a717ccd50de2b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
且<code>HTTPBodyStream</code>和<code>HTTPBody</code>是相冲的,只能设置一个.</p>
<p>在调用<code>resume</code>方法之前,会先进行下面的方法.
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f12f28108f74bff99da1b5a50a6692e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这方法里面主要是调用<code>bodypart</code>的接口方法:<code>read:...maxLength</code><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ec7774bd7c4e6eb7f1fe00b2013969~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着进入<code>transitionToNextPhase</code>,在这个方法里面就开启了我们的<code>stream</code><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6560469c3c04e4e904eb99ee37acda0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
那么<code>transitionToNextPhase</code>这个方法又是什么时候调用的呢?其实它在<code>init</code>初始化的时候就调用了<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96d157990d614d13bd4f196748a53bc7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">③ AFURLResponse</h4>
<p>那么什么时候会来<code>AFURLResponse</code>呢? <code>manager -- task --请求完成</code>的时候,后台有了返回的时候.回到<code>NSURLSessionTaskDelegate</code>代理方法中的<code>if(error)else</code>部分<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8034732e9f8d4d3eb150d57accb8d70e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这其中包含了我们开发中的各种序列化<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2bf607a55245dbabcbbc65d15c4bf3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
来看我们常用的<code>[AFJSONResponseSerializer responseObjectForResponse:data:error:]</code>方法<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1e1445465d449f91b63245a1af6a30~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>①先看验证请求判断这块,他是为了验证什么呢?<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c706cdab162f4406b064e65e7ce8acf0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>② 如果验证通过之后就进行<code>JSON</code>数据序列化,这其中有一点需要说一下<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72f567ceff9d4f4dacf85e7ed86f0a1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<p>就是移除返回为<code>null的数据</code>.</p>
<p>这部分内容的流程大概如下所示<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea8b5040686c4f3b8fb9c28193efa160~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">AFSecurityPolicy</h3>
<h4 data-id="heading-13">① http简介</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/015942b2d0514ec89b3baed01691f20d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">② https</h4>
<h5 data-id="heading-15">HTTPS和HTTP的区别</h5>
<p>HTTPS协议 = HTTP协议 + SSL/TLS协议
SSL的全称是Secure Sockets Layer，即安全套接层协议，是为网络通信提供安全及数据完整性的一种安全协议.TLS的全称是Transport Layer Security，即安全传输层协议.
即HTTPS是安全的HTTP.</p>
<h5 data-id="heading-16">HTTPS的连接建立流程</h5>
<p>HTTPS为了兼顾安全与效率，同时使用了对称加密和非对称加密。在传输的过程中会涉及到三个密钥：</p>
<ul>
<li>
<p>服务器端的公钥和私钥，用来进行<code>非对称加密</code></p>
</li>
<li>
<p>客户端生成的随机密钥，用来进行<code>对称加密</code></p>
</li>
</ul>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/977ffee5497346c693208efc70e4172a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如上图，HTTPS连接过程大致可分为八步:
<strong>1、客户端访问HTTPS连接</strong></p>
<p>客户端会把<code>安全协议版本号</code>、客户端支持的加密算法列表、<code>随机数C</code>发给服务端。</p>
<p><strong>2、服务端发送证书给客户端</strong></p>
<p>服务端接收密钥算法配件后，会和自己支持的加密算法列表进行比对，如果不符合，则断开连接。否则，服务端会在该算法列表中，选择一种对称算法（如AES）、一种公钥算法（如具有特定秘钥长度的RSA）和一种MAC算法发给客户端.
服务器端有一个密钥对，即<code>公钥</code>和<code>私钥</code>，是用来进行<code>非对称加密</code>使用的，服务器端保存着<code>私钥</code>，不能将其泄露，<code>公钥</code>可以发送给任何人。
在发送加密算法的同时还会把<code>数字证书</code>和<code>随机数S</code>发送给客户端</p>
<p><strong>3、客户端验证server证书</strong></p>
<p>会对server公钥进行检查，验证其合法性，如果发现公钥有问题，那么HTTPS传输就无法继续。</p>
<p><strong>4、客户端组装会话秘钥</strong></p>
<p>如果公钥合格，那么客户端会用服务器公钥来生成一个<code>前主秘钥</code>(Pre-Master Secret，PMS)，并通过该<code>前主秘钥</code>和随机数C、S来组装成<code>会话秘钥</code></p>
<p><strong>5、客户端将前主秘钥加密发送给服务端</strong></p>
<p>是通过服务端的公钥来对前主秘钥进行非对称加密，发送给服务端</p>
<p><strong>6、服务端通过私钥解密得到前主秘钥</strong></p>
<p>服务端接收到加密信息后，用私钥解密得到主秘钥.</p>
<p><strong>7、服务端组装会话秘钥</strong></p>
<p>服务端通过<code>前主秘钥</code>和随机数C、S来组装<code>会话秘钥</code>.
至此，服务端和客户端都已经知道了用于此次会话的主秘钥.</p>
<p><strong>8、数据传输</strong></p>
<p>客户端收到服务器发送来的密文，用客户端密钥对其进行对称解密，得到服务器发送的数据。
同理，服务端收到客户端发送来的密文，用服务端密钥对其进行对称解密，得到客户端发送的数据.</p>
<p><strong>总结：</strong></p>
<p><code>会话秘钥</code> = random S + random C + <code>前主秘钥</code></p>
<ul>
<li>
<p>HTTPS连接建立过程使用<code>非对称加密</code>，而<code>非对称加密</code>是很耗时的一种加密方式</p>
</li>
<li>
<p>后续通信过程使用<code>对称加密</code>，减少耗时所带来的性能损耗</p>
</li>
<li>
<p>其中，<code>对称加密</code>加密的是实际的数据，<code>非对称加密</code>加密的是对称加密所需要的客户端的密钥.</p>
</li>
</ul>
<h5 data-id="heading-17">对称加密和非对称加密</h5>
<p><strong>1、对称加密</strong></p>
<p>用同一套密钥来进行加密解密.
对称加密通常有 DES,IDEA,3DES 加密算法.</p>
<p><strong>2、非对称加密</strong></p>
<p>用公钥和私钥来加解密的算法。
<code>公钥</code>（Public Key）与<code>私钥</code>（Private Key）是通过一种算法得到的一个密钥对（即一个<code>公钥</code>和一个<code>私钥</code>），<code>公钥</code>是密钥对中公开的部分，<code>私钥</code>则是非公开的部分,<code>私钥</code>通常是保存在本地。</p>
<ul>
<li>
<p>用<code>公钥</code>进行加密，就要用<code>私钥</code>进行解密；反之，用<code>私钥</code>加密，就要用<code>公钥</code>进行解密（数字签名）.</p>
</li>
<li>
<p>由于私钥是保存在本地的，所以<code>非对称加密</code>相对与<code>对称加密</code>是安全的.</p>
</li>
</ul>
<p>但<code>非对称加密</code>比<code>对称加密</code>耗时(100倍以上),所以通常要结合<code>对称加密</code>来使用.</p>
<p>常见的非对称加密算法有：RSA、ECC（移动设备用）、Diffie-Hellman、El Gamal、DSA（数字签名用）</p>
<p>而为了确保客户端能够确认公钥就是想要访问的网站的公钥，引入了数字证书的概念，由于证书存在一级一级的签发过程，所以就出现了证书链，在证书链中的顶端的就是根CA.</p>
<h4 data-id="heading-18">③ AFSecurityPolicy</h4>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd330873f1a48e6b4da2da7e7527826~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
来看看<code>AF</code>的源码
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18403ca41b504c748b11694f54e6b75a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/369bb4ae6e8d4801a5f6372a6d3f96de~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那么它是如何取出公钥的呢?继续跟进<code>setPinnedCertificates</code>方法<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/887dd559e60a4970a07bb5bf5d037c41~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在取公钥的过程可能有两种验证方式,单向验证(服务端)和双向验证(客服端和服务端):
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20356e0336a54171818b6ac61af63412~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab431c52e9e64c7981861b4a8eeffad0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aa3a3f24977493181c65026865e783a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在取出公钥传输的过程中会验证所有证书的信息.
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce89933d31564540a3482f480d10c40b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eb2d5e0679d4651bd1077c4d6032601~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eea3e6955ce4063b7c403f7a6044e66~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在后面这个代理方法里面会进入<code>evaluateServerTrust:forDomain:</code>方法,用来验证服务端是否值得信任.<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d14c69c2eea48309e0f155f526e87b0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
假如你的证书是不受信任的话(即自签证书),那他会进入
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a0a07387aed48f8ae4c0a64a2a795d8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
也就是说如果你的证书是<code>CA</code>的就不需要处理,是自签的话就需要设置为根证书.</p>
<h3 data-id="heading-19">AFNetworkReachabilityManager</h3>
<p>先上个流程图<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b4f4f5f90ee465f93f5d8b64279c0e1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
话不多说来上源码,这个类主要用要到了全局单例的设计模式<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec04b710287d4e5885aae05ec9959a74~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着调用<code>manager</code>方法<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ef693b93aa40ce9df4b419cbc327d7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
跟进<code>managerForAddress</code>方法
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02819ed72a204151a5a8a79d10d04510~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0ad7256e9a14169bd056388c56b6b04~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>返回<code>ReachabilityManager</code>对象后调用<code>startMonitoring</code>方法
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b010eb4546004db3a642f08c222bf397~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32ac211541344399ab11826a4f640c5c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着根据网络<code>flag</code>转成我们开发中常用的网络状态调用<code>AFNetworkReachabilityStatus()</code>
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b1cedf31365487b945dbd19e1a68f0d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">UIKit+AFNetworking</h3>
<h4 data-id="heading-21">AFAutoPurgingImageCache</h4>
<p>该类是用来管理内存中的缓存图片的，它提供了最大内存容量和首选内存容量，当达到最大容量时，会依次删除（<code>Purging</code>）最久未使用的缓存图片，直到降到首选内存容量以下.让我们看一下这个功能是如何实现的？</p>
<h5 data-id="heading-22">AFImageCache协议</h5>
<p>这个协议定义了针对缓存图片的<code>增删改查</code>的方法，这些方法都是同步并安全的:</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">AFImageCache</span> <<span class="hljs-title">NSObject</span>></span>
- (<span class="hljs-keyword">void</span>)addImage:(<span class="hljs-built_in">UIImage</span> *)image withIdentifier:(<span class="hljs-built_in">NSString</span> *)identifier;
- (<span class="hljs-built_in">BOOL</span>)removeImageWithIdentifier:(<span class="hljs-built_in">NSString</span> *)identifier;
- (<span class="hljs-built_in">BOOL</span>)removeAllImages;
- (<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">UIImage</span> *)imageWithIdentifier:(<span class="hljs-built_in">NSString</span> *)identifier;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些方法中涉及到入参<code>identifier</code>，这个值可以作为<code>图片id</code>用来查找图片，一般可以用图片名来表示，当然网络图片也可以用<code>url</code>来表示，针对这一点，<code>AF</code>对这个协议进行了扩展.</p>
<h5 data-id="heading-23">AFImageRequestCache</h5>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@protocol</span> <span class="hljs-title">AFImageRequestCache</span> <<span class="hljs-title">AFImageCache</span>></span>
<span class="hljs-comment">// 是否应该缓存，默认实现是YES</span>
- (<span class="hljs-built_in">BOOL</span>)shouldCacheImage:(<span class="hljs-built_in">UIImage</span> *)image forRequest:(<span class="hljs-built_in">NSURLRequest</span> *)request withAdditionalIdentifier:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSString</span> *)identifier;
<span class="hljs-comment">// 增删查方法，支持了传入一个request对象，并以request.URL.absoluteString为图片identifier，同时也可以在默认identifier后拼接AdditionalIdentifier</span>
- (<span class="hljs-keyword">void</span>)addImage:(<span class="hljs-built_in">UIImage</span> *)image forRequest:(<span class="hljs-built_in">NSURLRequest</span> *)request withAdditionalIdentifier:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSString</span> *)identifier;
- (<span class="hljs-built_in">BOOL</span>)removeImageforRequest:(<span class="hljs-built_in">NSURLRequest</span> *)request withAdditionalIdentifier:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSString</span> *)identifier;
- (<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">UIImage</span> *)imageforRequest:(<span class="hljs-built_in">NSURLRequest</span> *)request withAdditionalIdentifier:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSString</span> *)identifier;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完协议的定义后，我们继续看一下这个协议的主要实现<code>AFAutoPurgingImageCache</code>类</p>
<h5 data-id="heading-24">AFAutoPurgingImageCache</h5>
<p>这个类中除了实现<code>AFImageCache</code>协议相关方法，还增加了内存控制的属性：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">// 最大内存</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) <span class="hljs-built_in">UInt64</span> memoryCapacity;
<span class="hljs-comment">// 首选内存</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) <span class="hljs-built_in">UInt64</span> preferredMemoryUsageAfterPurge;
<span class="hljs-comment">// 当前内存用量</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>, <span class="hljs-keyword">readonly</span>) <span class="hljs-built_in">UInt64</span> memoryUsage;
<span class="hljs-comment">// init</span>
- (<span class="hljs-keyword">instancetype</span>)initWithMemoryCapacity:(<span class="hljs-built_in">UInt64</span>)memoryCapacity preferredMemoryCapacity:(<span class="hljs-built_in">UInt64</span>)preferredMemoryCapacity;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>属性都很好理解，这些属性是如何使用的要看具体的实现了：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">AFAutoPurgingImageCache</span> ()</span>
<span class="hljs-comment">// 用来管理缓存图片的字典</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">strong</span>) <span class="hljs-built_in">NSMutableDictionary</span> <<span class="hljs-built_in">NSString</span>* , AFCachedImage*> *cachedImages;
<span class="hljs-comment">// 当前使用的内存</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) <span class="hljs-built_in">UInt64</span> currentMemoryUsage;
<span class="hljs-comment">// 保证安全性的队列</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">strong</span>) <span class="hljs-built_in">dispatch_queue_t</span> synchronizationQueue;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这个类的内部有一个用来管理<code>缓存图片的字典</code>，这个字典的<code>key</code>为图片的<code>identifier</code>，<code>value</code>为<code>AFCachedImage</code>对象，对于这个对象，我们看下它的实现：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">AFCachedImage</span> : <span class="hljs-title">NSObject</span></span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">strong</span>) <span class="hljs-built_in">UIImage</span> *image;<span class="hljs-comment">//持有image</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">copy</span>) <span class="hljs-built_in">NSString</span> *identifier;<span class="hljs-comment">//唯一标识</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) <span class="hljs-built_in">UInt64</span> totalBytes;<span class="hljs-comment">//图片占用的总字节数</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">strong</span>) <span class="hljs-built_in">NSDate</span> *lastAccessDate;<span class="hljs-comment">//上次获取的时间</span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) <span class="hljs-built_in">UInt64</span> currentMemoryUsage;<span class="hljs-comment">//当前使用的内存</span>
<span class="hljs-keyword">@end</span>

<span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">AFCachedImage</span></span>
- (<span class="hljs-keyword">instancetype</span>)initWithImage:(<span class="hljs-built_in">UIImage</span> *)image identifier:(<span class="hljs-built_in">NSString</span> *)identifier &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">self</span> = [<span class="hljs-keyword">self</span> init]) &#123;
        <span class="hljs-keyword">self</span>.image = image;
        <span class="hljs-keyword">self</span>.identifier = identifier;
        <span class="hljs-comment">// 计算当前的图片总字节数</span>
        <span class="hljs-built_in">CGSize</span> imageSize = <span class="hljs-built_in">CGSizeMake</span>(image.size.width * image.scale, image.size.height * image.scale);
        <span class="hljs-built_in">CGFloat</span> bytesPerPixel = <span class="hljs-number">4.0</span>;
        <span class="hljs-built_in">CGFloat</span> bytesPerSize = imageSize.width * imageSize.height;
        <span class="hljs-keyword">self</span>.totalBytes = (<span class="hljs-built_in">UInt64</span>)bytesPerPixel * (<span class="hljs-built_in">UInt64</span>)bytesPerSize;
        <span class="hljs-keyword">self</span>.lastAccessDate = [<span class="hljs-built_in">NSDate</span> date];
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span>;
&#125;

- (<span class="hljs-built_in">UIImage</span> *)accessImage &#123;
    <span class="hljs-comment">// 每次获取图片都会刷新时间</span>
    <span class="hljs-keyword">self</span>.lastAccessDate = [<span class="hljs-built_in">NSDate</span> date];
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span>.image;
&#125;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到<code>AFCachedImage</code>类相当于对<code>UIImage</code>进行了包装，添加了一些标识类的属性而已，现在我们回到<code>AFAutoPurgingImageCache</code>中继续往下看它的方法实现：
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c748271ea7947109f5b171e3e6ff211~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/983c58468aed41399bb1b73248767264~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
以上就是<code>AF</code>的图片缓存,大致的流程为
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbee6368035c40a9ad61ec161d2c61c8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">AFImageDownloader</h4>
<p>下载图片类，这个类会并行下载图片任务，下载后的图片会缓存到内存中.
说到这我们用的最多的就是给<code>UIimageView</code>设置图片了,这其中又需要用到<code>AF</code>的<code>UIImageView+AFNetworking</code>分类了.
例如<code>[cell.imageView setImageWithURL:[NSURL URLWithString:model.imageUrl]];</code></p>
<p>这时候会来到<code>AF</code>的<code>UIImageView+AFNetworking</code>分类中的<code>setImageWithURL:</code>方法<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4db677c4894346e6bbc48fcc0ce247d6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
为什么<code>AFImageDownloader *downloader = [[self class] sharedImageDownloader];</code>中用<code>sharedImageDownloader</code>呢?意味着我所有的下载用一个下载器下载就行了.这个下载器关联到<code>AF</code>的分类里面,所以用关联属性进行设置.<img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26b1bdaa3ae44846b14bcc5293be1e99~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
接着会初始化一个下载凭证<code>AFImageDownloadReceipt *receipt;</code>,下载凭证会调用<code>downloadImageForURLRequest:</code>方法<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b09fe70b2086488a8d69ec7db3525c21~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
梳理下大致逻辑，当遇到需要加载网络图片的情况下时，我们调用<code>downloadImageForURLRequest</code>方法创建任务，并生成<code>receipt</code>返回给我们，方便我们随时取消.加载过程会优先根据缓存策略，选择是否去缓存中查找，请求成功后会把当前图片放到内存中方便下次使用.</p>
<p><code>AF</code>下载图片的大致流程如下
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db2077868ef3488da99f301e57969e20~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26">三、AF的一些优质代码细节</h2>
<p>仔细瞅瞅代码之后，发现常见的<code>OC基础知识</code>在<code>AF</code>里面都有具体应用，挺多还是面试题考点，这里也是做个记录和梳理.</p>
<ul>
<li><strong>单例的创建方法</strong></li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86d81072451d489998bb5be1dbaa7e35~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
通过<code>dispatch_once</code>来保证多线程调用时，只有一个实例被创建.</p>
<ul>
<li><strong>dispatch_sync与dispatch_barrier_sync配合解决并行读串行写问题</strong></li>
</ul>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cdd970651fe44f4a060bfbfe5738bc1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa099c8a87d41959f72d270c259b65b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<code>GCD</code>使用<code>barrier</code>来处理<code>并行读串行写</code>问题的具体用法</p>
<ul>
<li><strong>weakSelf与strongSelf的用法</strong> -- 强弱共舞</li>
</ul>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2af77ff84b2144009c0a83fd09459463~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
必知必会，<code>weakSelf</code>避免循环引用，<code>strongSelf</code>保证<code>block</code>内部执行过程中<code>self</code>不会被释放.</p>
<h2 data-id="heading-27">四、AFNetworking的可能面试考点</h2>
<p>前面提到阅读开源库时，要多思考多提问题，这里也结合一些面试考题来梳理下</p>
<h3 data-id="heading-28">AFNetworking 2.x怎么开启常驻子线程？为何需要常驻子线程？</h3>
<p>这个知识点应该是<code>AF2.x</code>版本面试官比较喜欢问的了，<code>AF2.x</code>版本有个细节，通过<code>runloop</code>开启了一个常驻子线程，具体代码是这样的：</p>
<pre><code class="hljs language-objc copyable" lang="objc">+ (<span class="hljs-keyword">void</span>)networkRequestThreadEntryPoint:(<span class="hljs-keyword">id</span>)__unused object &#123;
    <span class="hljs-keyword">@autoreleasepool</span> &#123;
        [[<span class="hljs-built_in">NSThread</span> currentThread] setName:<span class="hljs-string">@"AFNetworking"</span>];

        <span class="hljs-built_in">NSRunLoop</span> *runLoop = [<span class="hljs-built_in">NSRunLoop</span> currentRunLoop];
        [runLoop addPort:[<span class="hljs-built_in">NSMachPort</span> port] forMode:<span class="hljs-built_in">NSDefaultRunLoopMode</span>];
        [runLoop run];
    &#125;
&#125;

+ (<span class="hljs-built_in">NSThread</span> *)networkRequestThread &#123;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">NSThread</span> *_networkRequestThread = <span class="hljs-literal">nil</span>;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">dispatch_once_t</span> oncePredicate;
    <span class="hljs-built_in">dispatch_once</span>(&oncePredicate, ^&#123;
        _networkRequestThread = [[<span class="hljs-built_in">NSThread</span> alloc] initWithTarget:<span class="hljs-keyword">self</span> selector:<span class="hljs-keyword">@selector</span>(networkRequestThreadEntryPoint:) object:<span class="hljs-literal">nil</span>];
        [_networkRequestThread start];
    &#125;);

    <span class="hljs-keyword">return</span> _networkRequestThread;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，我们要了解为何要开启<strong>常驻子线程</strong>？</p>
<p><code>NSURLConnection</code>的接口是<code>异步</code>的，然后会再发起线程的回调.而一个子线程，在同步代码执行完成之后，一般情况下，线程就退出了.那么想要接收到<code>NSURLConnection</code>的回调，就必须让子线程至少存活到回调的时机.而<code>AF</code>让线程常驻的原因是，<code>当发起多个http请求的时候，会统一在这个子线程进行回调的处理</code>，所以干脆就让其一直存活下来.</p>
<p>上面说的一般情况，<code>子线程执行完任务就会退出</code>，那么什么情况下，子线程能够继续存活呢？这就涉及到第二个问题了，<code>AF</code>是如何开启常驻线程的，这里实际上考察的是<code>runloop</code>的基础知识.</p>
<p>关于<code>runloop</code>，可以看下我的<a href="https://juejin.cn/post/6937300616184070174" target="_blank">iOS之武功秘籍⑲: 内存管理与NSRunLoop
</a>.这里简单来说，当<code>runloop</code>发现还有<code>source/timer/observer</code>的时候，<code>runloop</code>就不会退出.所以<code>AF</code>这里就通过给当前<code>runloop</code>添加一个<code>NSMachPort</code>，这个<code>port</code>实际上相当于添加了一个<code>source</code>事件源，这样子线程的<code>runloop</code>就会一直处于循环状态，等待别的线程向这个<code>port</code>发送消息，而实际上<code>AF</code>这里是没有消息发送到这个<code>port</code>的.</p>
<p>除了<code>AF</code>的这种处理方式，实际上苹果也提供了回调线程的解决方案：</p>
<pre><code class="hljs language-objc copyable" lang="objc"><span class="hljs-comment">// NSURLConnection</span>
- (<span class="hljs-keyword">void</span>)setDelegateQueue:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSOperationQueue</span>*) queue

<span class="hljs-comment">// NSURLSession</span>
+ (<span class="hljs-built_in">NSURLSession</span> *)sessionWithConfiguration:(<span class="hljs-built_in">NSURLSessionConfiguration</span> *)configuration delegate:(<span class="hljs-keyword">nullable</span> <span class="hljs-keyword">id</span> <<span class="hljs-built_in">NSURLSessionDelegate</span>>)delegate delegateQueue:(<span class="hljs-keyword">nullable</span> <span class="hljs-built_in">NSOperationQueue</span> *)queue;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>苹果提供了接口，可以让你制定一个<code>operationQueue</code>供回调执行.所以从<code>AF3.x</code>版本开始，就直接创建了一个<code>并发度为1</code>的队列，来处理回调.
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b123216bf64f5dae1f0cedbf3123eb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cee66bdaaa864a3a8a346ea66341d292~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>扩展一:</strong></p>
<p><strong>面试官可能会问你：为什么从<code>AF3.x</code>开始需要设置<code>maxConcurrentOperationCount = 1</code>,而<code>AF2.x</code>却不需要？</strong></p>
<p>这个问题不难，但是却可以帮助面试官判断面试者是否真的认真研读了<code>AF</code>的两个大版本的源码.
解答：功能不一样：<code>AF3.x</code>开始的<code>operationQueue</code>是用来接收<code>NSURLSessionDelegate</code>回调的，鉴于一些多线程数据访问的安全性考虑，设置了<code>maxConcurrentOperationCount = 1</code>来达到<code>串行回调的效果</code>.
而<code>AF2.x</code>的<code>operationQueue</code>是用来添加<code>operation</code>并进行并发请求的，所以不要设置为1.</p>
<h3 data-id="heading-29">AFURLSessionManager与NSURLSession的关系，每次都需要新建mananger吗？</h3>
<p>我们如果仔细查看代码，应该就能得出这样的结论：<code>manager</code>与<code>session</code>是<code>1对1</code>的关系，<code>AF</code>会在<code>manager</code>初始化的时候创建对应的<code>NSURLSession</code>.</p>
<p>那么复用<code>manager</code>实际上就是复用了<code>session</code>，而复用<code>session</code>可以带来什么好处呢？</p>
<p>其实<code>iOS9</code>之后，<code>session</code>就开始支持<code>http2.0</code>.而<code>http2.0</code>的一个特点就是<code>多路复用</code>。所以这里复用<code>session</code>其实就是在利用<code>http2.0</code>的多路复用特点，减少访问同一个服务器时，重新建立<code>tcp</code>连接的耗时和资源.</p>
<p>官方文档也推荐在不同的功能场景下，使用不同的<code>session</code>.比如：一个<code>session</code>处理普通的请求，一个<code>session</code>处理<code>background</code>请求；1个<code>session</code>处理浏览器公开的请求，一个<code>session</code>专门处理隐私请求等等场景.</p>
<h3 data-id="heading-30">AFSecurityPolicy如何避免中间人攻击？</h3>
<p>现在，由于苹果<code>ATS</code>的策略，基本都切到<code>HTTPS</code>了，<code>HTTPS</code>的基本原理还是需要了解一下的，这里不做介绍，需要的可以<code>google</code>查阅一下相关文章.</p>
<p>通常，首先我们要了解中间人攻击，大体就是黑客通过截获服务器返回的证书，并伪造成自己的证书，通常我们使用的<code>Charles/Fiddler</code>等工具实际上就可以看成中间人攻击.</p>
<p>解决方案其实也很简单，就是<code>SSL Pinning</code>.<code>AFSecurityPolicy</code>的<code>AFSSLPinningMode</code>就是相关设置项.</p>
<p><code>SSL Pinning</code>的原理就是需要将服务器的公钥打包到客户端中，<code>tls</code>验证时，会将服务器的证书和本地的证书做一个对比，一致的话才允许验证通过.<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e021cedc8fd64c858ef988e46b0232cf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
由于数字证书存在有效期，内置到客户端后就存在失效后导致验证失败的问题，所以可以考虑设置为<code>AFSSLPinningModePublicKey</code>的模式，这样的话，只要保证证书续期后，证书中的公钥不变，就能够通过验证了.</p>
<h2 data-id="heading-31">写在后面</h2>
<p>和谐学习,不急不躁.我还是我,颜色不一样的烟火.</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            