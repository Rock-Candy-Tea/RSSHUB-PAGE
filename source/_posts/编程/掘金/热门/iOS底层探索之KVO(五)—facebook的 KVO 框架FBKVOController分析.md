
---
title: 'iOS底层探索之KVO(五)—facebook的 KVO 框架FBKVOController分析'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f1c9bc492e94426918e8fbab32b1ba2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 21:04:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f1c9bc492e94426918e8fbab32b1ba2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">回顾</h2>
<p>在前面的几篇博客中，已经介绍了<code>KVO</code>的基本使用，如何自定义 <code>KVO</code>，那么本篇博客将分析一下<code>FBKVOController</code>这个优秀的<code> KVO</code>三方库。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzjpjay%2Farticle%2Fdetails%2F119343205%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zjpjay/article/details/119343205?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">iOS底层探索之KVO(一)—KVO简介</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzjpjay%2Farticle%2Fdetails%2F119376021%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zjpjay/article/details/119376021?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">iOS底层探索之KVO(二)—KVO原理分析</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzjpjay%2Farticle%2Fdetails%2F119417380%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zjpjay/article/details/119417380?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">iOS底层探索之KVO(三)—自定义KVO</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzjpjay%2Farticle%2Fdetails%2F119442712%3Fspm%3D1001.2014.3001.5501" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zjpjay/article/details/119442712?spm=1001.2014.3001.5501" ref="nofollow noopener noreferrer">iOS底层探索之KVO(四)—自定义KVO</a></p>
<blockquote>
<p><code>FBKVOController</code>是一个函数式编程实现，不用移除观察者者。</p>
</blockquote>
<h2 data-id="heading-1">1. FBKVOController简单介绍</h2>
<p><code>FBKVOController</code>是<code>Facebook</code>开源的一个基于系统<code>KVO</code>实现的框架。支持<code>Objective-C</code>和<code>Swift</code>语言。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebookarchive%2FKVOController" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebookarchive/KVOController" ref="nofollow noopener noreferrer">GitHub地址</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f1c9bc492e94426918e8fbab32b1ba2~tplv-k3u1fbpfcp-watermark.image" alt="KVOController" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>键值观察是一种特别有用的技术，用于在模型-视图-控制器应用程序中的层之间进行通信。<code>KVOController</code> 建立在 <code>Cocoa </code>久经考验的键值观察实现之上。它提供了一个简单、现代的 <code>API</code>，这也是<code>线程安全</code>的。</p>
<blockquote>
<p><code>KVOController</code>优点如下：</p>
</blockquote>
</blockquote>
<h3 data-id="heading-2">1.1 KVOController优点</h3>
<ul>
<li>使用blocks、自定义操作或<code> NSKeyValueObserving</code> 回调通知。</li>
<li>不需要额外的移除观察者</li>
<li>在控制器 dealloc 的时候隐式的把观察者移除。</li>
<li>具有防止观察者复活的特殊线程安全的保护机制</li>
<li>有关 KVO 的更多信息，请参阅 Apple 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Flibrary%2Farchive%2Fdocumentation%2FCocoa%2FConceptual%2FKeyValueObserving%2FKeyValueObserving.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html" ref="nofollow noopener noreferrer">键值观察简介</a>。</li>
</ul>
<h3 data-id="heading-3">1.2 <strong>FBKVOController</strong> 使用</h3>
<p><code>FBKVOController</code>的使用起来非常的简单，代码很少，<code>FBKVOController</code>简单使用如下代码所示：</p>
<ul>
<li><code>FBKVOController</code> 使用</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"> <span class="hljs-keyword">self</span>.person = [[JPPerson alloc] init];
    <span class="hljs-keyword">self</span>.person.name = <span class="hljs-string">@"RENO"</span>;
    <span class="hljs-keyword">self</span>.person.age = <span class="hljs-number">18</span>;
    <span class="hljs-keyword">self</span>.person.mArray = [<span class="hljs-built_in">NSMutableArray</span> arrayWithObject:<span class="hljs-string">@"1"</span>];

    [<span class="hljs-keyword">self</span>.kvoCtrl observe:<span class="hljs-keyword">self</span>.person keyPath:<span class="hljs-string">@"age"</span> options:<span class="hljs-number">0</span> action:<span class="hljs-keyword">@selector</span>(jp_observerAge)];
    [<span class="hljs-keyword">self</span>.kvoCtrl observe:<span class="hljs-keyword">self</span>.person keyPath:<span class="hljs-string">@"name"</span> options:(<span class="hljs-built_in">NSKeyValueObservingOptionNew</span>) block:^(<span class="hljs-keyword">id</span>  _Nullable observer, <span class="hljs-keyword">id</span>  _Nonnull object, <span class="hljs-built_in">NSDictionary</span><<span class="hljs-built_in">NSString</span> *,<span class="hljs-keyword">id</span>> * _Nonnull change) &#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"****%@****"</span>,change);
    &#125;];
    [<span class="hljs-keyword">self</span>.kvoCtrl observe:<span class="hljs-keyword">self</span>.person keyPath:<span class="hljs-string">@"mArray"</span> options:(<span class="hljs-built_in">NSKeyValueObservingOptionNew</span>) block:^(<span class="hljs-keyword">id</span>  _Nullable observer, <span class="hljs-keyword">id</span>  _Nonnull object, <span class="hljs-built_in">NSDictionary</span><<span class="hljs-built_in">NSString</span> *,<span class="hljs-keyword">id</span>> * _Nonnull change) &#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"****%@****"</span>,change);
    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码非常的简洁，不用向我们之前使用系统的 <code>KVO</code>那样在<code> dealloc</code> 里面移除观察者，这一波使用就很爽啊！</p>
<ul>
<li>懒加载初始化</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> mark - lazy</span>
- (FBKVOController *)kvoCtrl&#123;
    <span class="hljs-keyword">if</span> (!_kvoCtrl) &#123;
        _kvoCtrl = [FBKVOController controllerWithObserver:<span class="hljs-keyword">self</span>];
    &#125;
    <span class="hljs-keyword">return</span> _kvoCtrl;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2. KVOController 实现分析</h2>
<h3 data-id="heading-5">2.1 中介者模式</h3>
<blockquote>
<p>我们平时买房、租房都会找中介，通过中介可以更快更高效的找到合适的房子，也就很多事情中介帮我们去做了，不用我们自己去找房源。</p>
<blockquote>
<p><code>KVOController</code>主要是使用了中介者模式，官方<code>kvo</code>使用麻烦的点在于使用需要三部曲。<code>KVOController</code>核心就是将三部曲进行了底层封装，上层只需要关心业务逻辑。</p>
</blockquote>
<blockquote>
<p><code>FBKVOController</code>会进行注册、移除以及回调的处理（回调包括<code>block</code>、<code>action</code>以及兼容系统的<code>observe</code>回调）。是对外暴露的交互类。使用<code>FBKVOController</code>分为两步：</p>
</blockquote>
</blockquote>
<ul>
<li>使用 <code>controllerWithObserver</code> 初始化<code>FBKVOController</code>实例。</li>
<li>使用<code>observe:</code>进行注册。</li>
</ul>
<h3 data-id="heading-6">2.2 FBKVOController 初始化</h3>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">instancetype</span>)initWithObserver:(<span class="hljs-keyword">nullable</span> <span class="hljs-keyword">id</span>)observer retainObserved:(<span class="hljs-built_in">BOOL</span>)retainObserved
&#123;
  <span class="hljs-keyword">self</span> = [<span class="hljs-keyword">super</span> init];
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> != <span class="hljs-keyword">self</span>) &#123;
    _observer = observer;
    <span class="hljs-built_in">NSPointerFunctionsOptions</span> keyOptions = retainObserved ? <span class="hljs-built_in">NSPointerFunctionsStrongMemory</span>|<span class="hljs-built_in">NSPointerFunctionsObjectPointerPersonality</span> : <span class="hljs-built_in">NSPointerFunctionsWeakMemory</span>|<span class="hljs-built_in">NSPointerFunctionsObjectPointerPersonality</span>;
    _objectInfosMap = [[<span class="hljs-built_in">NSMapTable</span> alloc] initWithKeyOptions:keyOptions valueOptions:<span class="hljs-built_in">NSPointerFunctionsStrongMemory</span>|<span class="hljs-built_in">NSPointerFunctionsObjectPersonality</span> capacity:<span class="hljs-number">0</span>];
    pthread_mutex_init(&_lock, <span class="hljs-literal">NULL</span>);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_observer</code>是观察者，是<code>FBKVOController</code>的属性，用 weak来修饰</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nullable</span>, <span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">weak</span>, <span class="hljs-keyword">readonly</span>) <span class="hljs-keyword">id</span> observer;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>因为<code>FBKVOController</code>本身被观察者持有了，所以是<code>weak</code>类型的修饰。</p>
</blockquote>
<p><code>_objectInfosMap</code>根据<code>retainObserved</code>进行<code>NSMapTable</code>内存管理/初始化配置，<code>FBKVOController</code>的成员变量。其中保存的是一个被观察者对应多个<code>_FBKVOInfo</code>（也就是被观察对象对应多个<code>keyPath</code>）：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">  <span class="hljs-built_in">NSMapTable</span><<span class="hljs-keyword">id</span>, <span class="hljs-built_in">NSMutableSet</span><_FBKVOInfo *> *> *_objectInfosMap;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_FBKVOInfo</code>是放在<code>NSMutableSet</code>中的，说明是去重的。</p>
<h3 data-id="heading-7">2.3 FBKVOController 注册</h3>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)observe:(<span class="hljs-keyword">nullable</span> <span class="hljs-keyword">id</span>)object keyPath:(<span class="hljs-built_in">NSString</span> *)keyPath options:(<span class="hljs-built_in">NSKeyValueObservingOptions</span>)options block:(FBKVONotificationBlock)block
&#123;
  <span class="hljs-built_in">NSAssert</span>(<span class="hljs-number">0</span> != keyPath.length && <span class="hljs-literal">NULL</span> != block, <span class="hljs-string">@"missing required parameters observe:%@ keyPath:%@ block:%p"</span>, object, keyPath, block);
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> == object || <span class="hljs-number">0</span> == keyPath.length || <span class="hljs-literal">NULL</span> == block) &#123;
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-comment">// create info</span>
  _FBKVOInfo *info = [[_FBKVOInfo alloc] initWithController:<span class="hljs-keyword">self</span> keyPath:keyPath options:options block:block];

  <span class="hljs-comment">// observe object with info</span>
  [<span class="hljs-keyword">self</span> _observe:object info:info];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>首先第一步就是做一些判断，容错判断。</p>
</li>
<li>
<p>构造<code>_FBKVOInfo</code>，保存<code>FBKVOController</code>、keyPath、<code>options</code>以及<code>block</code>。</p>
</li>
<li>
<p>调用<code>_observe:(id)object info:(_FBKVOInfo *)info</code></p>
</li>
<li>
<p><strong>_FBKVOInfo</strong></p>
</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">_FBKVOInfo</span></span>
&#123;
<span class="hljs-keyword">@public</span>
  __<span class="hljs-keyword">weak</span> FBKVOController *_controller;
  <span class="hljs-built_in">NSString</span> *_keyPath;
  <span class="hljs-built_in">NSKeyValueObservingOptions</span> _options;
  SEL _action;
  <span class="hljs-keyword">void</span> *_context;
  FBKVONotificationBlock _block;
  _FBKVOInfoState _state;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>_FBKVOInfo</code>中保存了一些相关的数据信息</p>
<ul>
<li>重写<code>isEqual</code>与<code>hash</code>方法</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-built_in">NSUInteger</span>)hash
&#123;
  <span class="hljs-keyword">return</span> [_keyPath hash];
&#125;

- (<span class="hljs-built_in">BOOL</span>)isEqual:(<span class="hljs-keyword">id</span>)object
&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> == object) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">NO</span>;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">self</span> == object) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">YES</span>;
  &#125;
  <span class="hljs-keyword">if</span> (![object isKindOfClass:[<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>]]) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">NO</span>;
  &#125;
  <span class="hljs-keyword">return</span> [_keyPath isEqualToString:((_FBKVOInfo *)object)->_keyPath];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>只要<code>_keyPath</code>相同就认为是同一对象</p>
</blockquote>
<ul>
<li><strong>_observe: info:</strong></li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)_observe:(<span class="hljs-keyword">id</span>)object info:(_FBKVOInfo *)info
&#123;
  <span class="hljs-comment">// lock</span>
  pthread_mutex_lock(&_lock);

  <span class="hljs-comment">//从TableMap中获取 object（被观察者） 对应的 set</span>
  <span class="hljs-built_in">NSMutableSet</span> *infos = [_objectInfosMap objectForKey:object];

  <span class="hljs-comment">// check for info existence</span>
  <span class="hljs-comment">//判断对应的keypath info 是否存在</span>
  _FBKVOInfo *existingInfo = [infos member:info];
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> != existingInfo) &#123;
    <span class="hljs-comment">//存在直接返回，这里就相当于对于同一个观察者排除了相同的keypath</span>
    <span class="hljs-comment">// observation info already exists; do not observe it again</span>

    <span class="hljs-comment">// unlock and return</span>
    pthread_mutex_unlock(&_lock);
    <span class="hljs-keyword">return</span>;
  &#125;

  <span class="hljs-comment">// lazilly create set of infos</span>
  <span class="hljs-comment">//TableMap数据为空进行创建设置</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> == infos) &#123;
    infos = [<span class="hljs-built_in">NSMutableSet</span> set];
    <span class="hljs-comment">//<被观察者 - keypaths info></span>
    [_objectInfosMap setObject:infos forKey:object];
  &#125;

  <span class="hljs-comment">// add info and oberve</span>
  <span class="hljs-comment">//keypaths info添加 keypath info</span>
  [infos addObject:info];

  <span class="hljs-comment">// unlock prior to callout</span>
  pthread_mutex_unlock(&_lock);
  <span class="hljs-comment">//注册</span>
  [[_FBKVOSharedController sharedController] observe:object info:info];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先判断<code>kayPath</code>是否已经被注册了，注册了直接返回，这里也就是进行了去重的处理，这一波操作就非常细节。</li>
<li>将构造的<code>_FBKVOInfo</code>信息添加进<code>_objectInfosMap</code>中。</li>
<li>调用<code>_FBKVOSharedController</code>进行真正的注册。</li>
<li><code>member:</code>说明</li>
</ul>
<p><code>member</code>会调用到<code>_FBKVOInfo中的hash</code>以及<code>isEqual</code>进行判断对象是否存在，也就是判断<code>keyPath</code>对应的对象是否存在。</p>
<blockquote>
<p>这里注册 <code>[[_FBKVOSharedController sharedController]  observe:object info:info] </code>是使用了单例</p>
<blockquote>
<p>为什么这里使用<code>单例</code>呢？而不是在外面的调用初始化的时候使用单例呢？
这方法里面使用单例，下次再次使用就不会重复创建了，就是相当于保活了，我们在<code>VC</code> 中使用的是 <code>FBKVOController</code>的实例对象，会随着<code>VC</code>的销毁而销毁，这个单例观察者会在内部移除，移除不是销毁的意思，只是告诉这个单例，移除对某个对象的观察，例如观察了<code>self.person</code>的属性，最后的<code>dealloc</code>是移除对<code>self.person</code>的观察的意思。这一波操作，又是非常的细节，厉害了！</p>
</blockquote>
</blockquote>
<p>这里的<code>object</code>参数传入的是什么呢？是 <code>self</code>吗？</p>
<p>不是 <code>self</code>是<code>self.person</code>，why ？小朋友，你现在是否有很多问号？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/187fc87bcc804e17af13fac9d03cc440~tplv-k3u1fbpfcp-watermark.image" alt="问号脸" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在我们的印象中，使用<code> KVO</code>添加观察者传入的都是 <code>self </code>啊！但是靓仔，我们这里不是哦！</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d172f65062c47479f2c20477a938bd6~tplv-k3u1fbpfcp-watermark.image" alt="使用案例" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们的<code> VC</code>需要的是<code>block</code>的回调，添加观察者是观察<code>self.person</code>的属性变化，所以传入<code>self.person</code>就好了。你内部怎么操作，我<code> VC</code>不管，你只要把改变之后结果告诉我就好了，丢个<code> block</code> 的回调通知我<code> VC</code>就 <code>OK </code>了！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a0b8377311d48c38e5ba3281fdf9c22~tplv-k3u1fbpfcp-watermark.image" alt="observe:(id)object info:" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图这里的<code> self</code>是指前面的那个<code>单例</code>，就是为了复用，就是:只要添加属性的观察都是使用这个单例，这里通过 <code>keyPath </code>来区分，观察的是不同的属性。</p>
<h3 data-id="heading-8">2. 4 KVOController销毁</h3>
<blockquote>
<p><code>KVOController</code>的销毁，其实是内部帮我们实现了，所以不用我们手动去销毁。</p>
</blockquote>
<ul>
<li>dealloc</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a76dcf8e9e1e41929e0a663e5a7837bd~tplv-k3u1fbpfcp-watermark.image" alt="KVOController的dealloc" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>unobserveAll</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)unobserveAll
&#123;
  [<span class="hljs-keyword">self</span> _unobserveAll];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>_unobserveAll</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fbad7ad8b1c42cb84a2d5e70d14fc0a~tplv-k3u1fbpfcp-watermark.image" alt="_unobserveAll" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>_unobserve:(id)object info:</li>
</ul>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)_unobserve:(<span class="hljs-keyword">id</span>)object info:(_FBKVOInfo *)info
&#123;
  <span class="hljs-comment">// lock</span>
  pthread_mutex_lock(&_lock);

  <span class="hljs-comment">// get observation infos</span>
  <span class="hljs-built_in">NSMutableSet</span> *infos = [_objectInfosMap objectForKey:object];

  <span class="hljs-comment">// lookup registered info instance</span>
  _FBKVOInfo *registeredInfo = [infos member:info];

  <span class="hljs-keyword">if</span> (<span class="hljs-literal">nil</span> != registeredInfo) &#123;
    [infos removeObject:registeredInfo];

    <span class="hljs-comment">// remove no longer used infos</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-number">0</span> == infos.count) &#123;
      [_objectInfosMap removeObjectForKey:object];
    &#125;
  &#125;

  <span class="hljs-comment">// unlock</span>
  pthread_mutex_unlock(&_lock);

  <span class="hljs-comment">// unobserve</span>
  [[_FBKVOSharedController sharedController] unobserve:object info:registeredInfo];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>单例去调用内部的方法去移除观察者</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8bc320281d34164a27ee8cab227bb1a~tplv-k3u1fbpfcp-watermark.image" alt="unobserve:(id)object info:" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中红色框起来的代码，其实就是调用的系统的移除观察者的方法<code>removeObserver: forKeyPath :</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53dcddcc57d94840bd38864a50b3f663~tplv-k3u1fbpfcp-watermark.image" alt="removeObserver: forKeyPath :" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>由于<code>FBKVOController</code>的实例是VC持有的，所以我们的 VC被<code>dealloc</code>销毁的时候<code>FBKVOController</code>实例也就<code>dealloc</code>了。在这里调用就相当于在 VC 中<code>dealloc</code>中调用了移除是一样的。</p>
<blockquote>
<p>就是移除单例对 <code>object</code>观察这个动作，而不是移除观察者本身，就是说 老铁 我不需要观察了，后续别给我发送消息了。</p>
</blockquote>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ce53d5753d5403db7407baf963c1a08~tplv-k3u1fbpfcp-watermark.image" alt="KVO" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">3. 通过gnustep探索KVO</h2>
<p><code>kvo</code>与<code>kvc</code>是属于<code>Foundation</code>框架里面的，由于<code>Foundation</code>相关的代码苹果并没有开源，对于它们的探索可以通过<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.gnustep.org%2Fresources%2Fdownloads.php" target="_blank" rel="nofollow noopener noreferrer" title="http://www.gnustep.org/resources/downloads.php" ref="nofollow noopener noreferrer">gnustep</a>查看原理，<code>gnustep</code>中有一些苹果早期底层的实现。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e06966a4d8740f9b51858c9b53f87de~tplv-k3u1fbpfcp-watermark.image" alt="gnustep官网首页" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么<code>FBKVOController</code>分析就介绍到这了。</p>
<p>通过【<code>gnustep</code>】具体的探索，这里就不过多的描述了，感兴趣的老铁，可以自行去下载<code>Foundation</code>的源码，看看里面的实现，思路都是差不多的！</p>
<h2 data-id="heading-10">4. 总结</h2>
<ul>
<li><code>FBKVOController</code>使用了<code>中介者</code>模式，通过<code>函数式编程</code>的思想，把对属性的变化的观察，使用 <code>block</code>通知回调</li>
<li><code>FBKVOController</code> 注册，内部使用了单例，进行复用，通过 <code>keyPath </code>来区分，观察的是不同的属性。</li>
<li>在控制器 <code>dealloc</code> 的时候隐式的把观察者移除，其实内部还是调用了系统的移除方法。</li>
</ul>
<p><strong>更多内容持续更新</strong></p>
<p>🌹 喜欢就点个赞吧👍🌹</p>
<p>🌹 觉得有收获的，可以来一波，收藏+关注，评论 + 转发，以免你下次找不到我😁🌹</p>
<p>🌹欢迎大家留言交流，批评指正，互相学习😁，提升自我🌹</p></div>  
</div>
            