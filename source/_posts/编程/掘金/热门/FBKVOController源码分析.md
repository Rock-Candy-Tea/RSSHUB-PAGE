
---
title: 'FBKVOController源码分析'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2b3531e99d4197b8ec02103a5be2a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 02:01:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2b3531e99d4197b8ec02103a5be2a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">源码</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2FKVOController" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/KVOController" ref="nofollow noopener noreferrer">FBKVOController</a></p>
<p><code>KVO</code>一种非常有用的技术，用于在模型-视图-控制器应用程序中的层之间进行通信，<code>FBKVOController</code>在系统的<code>KVO</code>的基础上做了一层封装，它提供了一个简单、现代的API，也是线程安全的。好处包括</p>
<ul>
<li>使用了block回调，自定义actions，原有的NSKeyValueObserving 回调</li>
<li>实现了自动移除observer，无需开发则手动移除</li>
<li>线程安全</li>
<li>使用block的形式，是代码更加集中。</li>
</ul>
<h1 data-id="heading-1">API使用</h1>
<p>第一步：先定义一个中介者，kvo控制器，
第二步：添加观察</p>
<pre><code class="hljs language-js copyable" lang="js">- (FBKVOController *)kvoCtrl&#123;
    <span class="hljs-keyword">if</span> (!_kvoCtrl) &#123;
        _kvoCtrl = [FBKVOController controllerWithObserver:self];
    &#125;
    <span class="hljs-keyword">return</span> _kvoCtrl;
&#125;

[self.kvoCtrl observe:self.person keyPath:@<span class="hljs-string">"name"</span> options:(NSKeyValueObservingOptionNew) block:^(id  _Nullable** observer, id _Nonnull object, NSDictionary<NSString *,id> * _Nonnull change) &#123;

        NSLog(@<span class="hljs-string">"%@"</span>,change);

    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">源码分析</h1>
<h2 data-id="heading-3">中介者初始化方法：</h2>
<p><code>FBKVOController controllerWithObserver:self]</code></p>
<ol>
<li>弱引用持有self</li>
<li>初始化一个<code>NSMapTable</code>表，这个表主要存储了<code>object</code> 和<code>kvo infos</code>对应的信息</li>
</ol>
<h2 data-id="heading-4">添加观察者</h2>
<p>下面以<code>block</code>的这种方式为例，其他的几种方式流程一样</p>
<ol>
<li>先创建一个<code>_FBKVOInfo</code>实例，让后判断<code>objectInfosMap</code>之前是否存在，这个<code>info</code>实例，如果不存在则添加进去</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2b3531e99d4197b8ec02103a5be2a1~tplv-k3u1fbpfcp-watermark.image" alt="添加到表中.png" loading="lazy" referrerpolicy="no-referrer">
2.单列注册系统的observer</p>
<p><code>[[_FBKVOSharedController sharedController] observe:object info:info]</code>
其中做了一些状态的判断，如果状态为没有注册，就会移除。</p>
<h2 data-id="heading-5">回调处理</h2>
<p>在系统的方法里面做如下处理：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d670b276c184e348d144f4dda6a07fe~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-29 下午5.40.41.png" loading="lazy" referrerpolicy="no-referrer">
如果是<code>block</code>方式，则<code>block</code>回调，如果是自定义<code>actions</code>，则调用自定义的action，如果实现了系统的回调方法，则调用系统的。</p>
<h2 data-id="heading-6">移除观察</h2>
<p><code>vc</code> 持有 <code>FBKVOController</code> 对象，<code>vc</code>控制释放的时候会调用vc的dealloc，也会调用，<code>FBKVOController</code> 对象的dealloc，如果在这个里面移除观察者，这不需要在每个控制器里面移除。</p>
<pre><code class="hljs language-js copyable" lang="js">- (<span class="hljs-keyword">void</span>)dealloc
&#123;
  [self unobserveAll];
  pthread_mutex_destroy(&_lock);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如我们所料，在<code>FBKVOController</code>做了移除观察者的处理。</p>
<h1 data-id="heading-7">总结</h1>
<p>通过阅读<code>FBKVOController</code>源码，我们主要可以了解一种设计模式，对我们的业务开发会设计会有一些启发。</p></div>  
</div>
            