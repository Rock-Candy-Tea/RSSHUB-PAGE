
---
title: 'KVO原理分析下｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927a8b1651f349338db525e6bc294bb5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 17:48:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927a8b1651f349338db525e6bc294bb5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">KVO探索原理</h4>
<p>通过上一篇我们知道，在添加观察之后，isa指向发生了变化，指向了动态子类<code>NSKVONotifying_Person</code>。该子类有4个方法</p>
<ol>
<li><code>setNickName</code>:观察对象的set方法</li>
<li><code>class</code>：重写class方法</li>
<li><code>dealloc</code>：在该方法中isa指向又重新指回了父类</li>
</ol>
<h4 data-id="heading-1">自定义KVO思路</h4>
<ol>
<li><code>addObserver</code>时确保当前的类<code>(Person)</code>的<code>keyPath</code>有对应的<code>setter</code>方法</li>
<li>动态生成的子类也就是isa_siwziling,给子类添加对应的方法</li>
<li>把isa指向从Person指到<code>NSKVONotifying_Person</code></li>
<li>set方法处理</li>
</ol>
<h4 data-id="heading-2">自定义KVO-<code>addObserver</code></h4>
<p>1.首先从keyPath可以拼凑推导出set方法。eg:(name-> setName)。我们先判断本类中是否存在setName方法，如果不存在就报出异常。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)hb_addObserver:(<span class="hljs-built_in">NSObject</span> *)observer forKeyPath:(<span class="hljs-built_in">NSString</span> *)keyPath options:(<span class="hljs-built_in">NSKeyValueObservingOptions</span>)options context:(<span class="hljs-keyword">nullable</span> <span class="hljs-keyword">void</span> *)context &#123;
    <span class="hljs-comment">//1.确保存在keyPath的set方法</span>
    [<span class="hljs-keyword">self</span> getSetterMethodFromKeyPath:keyPath];
    <span class="hljs-comment">//2.动态生成子类</span>
    Class newClass = [<span class="hljs-keyword">self</span> creatChildClassByKeyPath:keyPath];
    <span class="hljs-comment">//3.isa指向派生的子类</span>
    object_setClass(<span class="hljs-keyword">self</span>, newClass);
    <span class="hljs-comment">//4.保存观察者</span>
    objc_setAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kHBKVOAssiociateKey), observer, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.动态生成子类的时候判断当前的子类是否存在，如果存在直接返回。不存在的话就申请、注册、然后动态添加方法
<code>setName:</code>和<code>class</code></p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> mark - 动态生成子类</span>
-(Class)creatChildClassByKeyPath: (<span class="hljs-built_in">NSString</span> *)keyPath &#123;
    <span class="hljs-comment">// 2.1获取当前的类的名字</span>
    <span class="hljs-built_in">NSString</span> *oldClassName = <span class="hljs-built_in">NSStringFromClass</span>([<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>]);
    <span class="hljs-comment">// 获取当前的类的子类名字</span>
    <span class="hljs-built_in">NSString</span> *newClassName = [<span class="hljs-built_in">NSString</span> stringWithFormat:<span class="hljs-string">@"%@%@"</span>,kHBKVOPrefix,oldClassName];
    Class newClass = <span class="hljs-built_in">NSClassFromString</span>(newClassName);
    <span class="hljs-comment">// 2.2判断是否存在</span>
    <span class="hljs-keyword">if</span> (newClass) <span class="hljs-keyword">return</span> newClass;
    <span class="hljs-comment">// 2.3不存在就创建  申请-注册-添加方法</span>
    objc_allocateClassPair([<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>], newClassName.UTF8String, <span class="hljs-number">0</span>);
    objc_registerClassPair(newClass);
    
    <span class="hljs-comment">// 2.3.1添加方法class方法   class指向的是Person</span>
    SEL classSEL = <span class="hljs-built_in">NSSelectorFromString</span>(<span class="hljs-string">@"class"</span>);
    Method classMethod = class_getInstanceMethod([<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>], classSEL);
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *classTypes = method_getTypeEncoding(classMethod);
    class_addMethod(newClass, classSEL, (IMP)hb_class, classTypes);
    
    <span class="hljs-comment">//2.3.2添加setKeyPath方法</span>
    SEL setterSEL = <span class="hljs-built_in">NSSelectorFromString</span>(setterFromKeyPath(keyPath));
    Method setterMethod = class_getInstanceMethod([<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>], setterSEL);
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *setterTypes = method_getTypeEncoding(setterMethod);
    class_addMethod(newClass, setterSEL, (IMP)hb_setter, setterTypes);
    
    <span class="hljs-comment">// 2.3.3 : 添加dealloc</span>
    SEL deallocSEL = <span class="hljs-built_in">NSSelectorFromString</span>(<span class="hljs-string">@"dealloc"</span>);
    Method deallocMethod = class_getInstanceMethod([<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>], deallocSEL);
    <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *deallocTypes = method_getTypeEncoding(deallocMethod);
    class_addMethod(newClass, deallocSEL, (IMP)hb_dealloc, deallocTypes);
    <span class="hljs-keyword">return</span> newClass;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">自定义KVO-<code>setter方法</code></h4>
<p>在当前派生子类重写的<code>setName:</code>方法中我们需要做3点
1.判断自动开关是否打开
2.发送到父类Person的set方法中（因为我们set方法最终还是修改掉了父类的set）
3.发送完成之后需要一个回调 也就是给观察者发送通知</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> hb_setter(<span class="hljs-keyword">id</span> <span class="hljs-keyword">self</span>, SEL _cmd, <span class="hljs-keyword">id</span> newValue)&#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"来了:%@"</span>,newValue );
    <span class="hljs-comment">// 消息转发给父类</span>
    <span class="hljs-built_in">NSString</span> *keyPath = getterFromKeyPath(<span class="hljs-built_in">NSStringFromSelector</span>(_cmd));
    <span class="hljs-keyword">id</span> oldValue = [<span class="hljs-keyword">self</span> valueForKey:keyPath];
    
    <span class="hljs-keyword">void</span> (*hb_msgSendSuper)(<span class="hljs-keyword">void</span> *,SEL , <span class="hljs-keyword">id</span>) = (<span class="hljs-keyword">void</span> *)objc_msgSendSuper;
    <span class="hljs-comment">// void /* struct objc_super *super, SEL op, ... */</span>
    <span class="hljs-keyword">struct</span> objc_super superStruct = &#123;
        .receiver = <span class="hljs-keyword">self</span>,
        .super_class = class_getSuperclass(object_getClass(<span class="hljs-keyword">self</span>)),
    &#125;;
    hb_msgSendSuper(&superStruct, _cmd, newValue);
    <span class="hljs-comment">// 1: 拿到观察者</span>
    <span class="hljs-keyword">id</span> observer = objc_getAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kHBKVOAssiociateKey));
    
    <span class="hljs-comment">// 2: 消息发送给观察者</span>
    SEL observerSEL = <span class="hljs-keyword">@selector</span>(observeValueForKeyPath:ofObject:change:context:);
    objc_msgSend(observer,observerSEL,keyPath,<span class="hljs-keyword">self</span>,@&#123;keyPath:newValue&#125;,<span class="hljs-literal">NULL</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">自定义KVO-优化</h4>
<p>观察的数据比较多的话，我们最好弄一个对象来保存观察者，以及keyPath的新值和旧值，所以在最开始的步骤4保存观察者的可以这么写：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">typedef</span> <span class="hljs-built_in">NS_OPTIONS</span>(<span class="hljs-built_in">NSUInteger</span>, HBKeyValueObservingOptions) &#123;

    HBKeyValueObservingOptionNew = <span class="hljs-number">0x01</span>,
    HBKeyValueObservingOptionOld = <span class="hljs-number">0x02</span>,
&#125;;

<span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">HBKVOInfo</span> : <span class="hljs-title">NSObject</span></span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">weak</span>) <span class="hljs-built_in">NSObject</span>  *observer;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">copy</span>) <span class="hljs-built_in">NSString</span>    *keyPath;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) HBKeyValueObservingOptions options;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">    <span class="hljs-comment">// 4: 保存观察者信息</span>
    HBKVOInfo *info = [[HBKVOInfo alloc] initWitObserver:observer forKeyPath:keyPath options:options];
    <span class="hljs-built_in">NSMutableArray</span> *observerArr = objc_getAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kHBKVOAssiociateKey));
    
    <span class="hljs-keyword">if</span> (!observerArr) &#123;
        observerArr = [<span class="hljs-built_in">NSMutableArray</span> arrayWithCapacity:<span class="hljs-number">1</span>];
        [observerArr addObject:info];
        objc_setAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kLGKVOAssiociateKey), observerArr, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在setter方法中给观察者发回调信息的话就遍历</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">    <span class="hljs-built_in">NSMutableArray</span> *observerArr = objc_getAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kHBKVOAssiociateKey));
    <span class="hljs-keyword">for</span> (HBKVOInfo *info <span class="hljs-keyword">in</span> observerArr) &#123;
        <span class="hljs-keyword">if</span> ([info.keyPath isEqualToString:keyPath]) &#123;
            <span class="hljs-built_in">dispatch_async</span>(dispatch_get_global_queue(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>), ^&#123;
                <span class="hljs-built_in">NSMutableDictionary</span><<span class="hljs-built_in">NSKeyValueChangeKey</span>,<span class="hljs-keyword">id</span>> *change = [<span class="hljs-built_in">NSMutableDictionary</span> dictionaryWithCapacity:<span class="hljs-number">1</span>];
                <span class="hljs-comment">// 对新旧值进行处理</span>
                <span class="hljs-keyword">if</span> (info.options & HBKeyValueObservingOptionNew) &#123;
                    [change setObject:newValue forKey:<span class="hljs-built_in">NSKeyValueChangeNewKey</span>];
                &#125;
                <span class="hljs-keyword">if</span> (info.options & HBKeyValueObservingOptionOld) &#123;
                    [change setObject:<span class="hljs-string">@""</span> forKey:<span class="hljs-built_in">NSKeyValueChangeOldKey</span>];
                    <span class="hljs-keyword">if</span> (oldValue) &#123;
                        [change setObject:oldValue forKey:<span class="hljs-built_in">NSKeyValueChangeOldKey</span>];
                    &#125;
                &#125;
                <span class="hljs-comment">// 2: 消息发送给观察者</span>
                SEL observerSEL = <span class="hljs-keyword">@selector</span>(lg_observeValueForKeyPath:ofObject:change:context:);
                objc_msgSend(info.observer,observerSEL,keyPath,<span class="hljs-keyword">self</span>,@&#123;keyPath:newValue&#125;,<span class="hljs-literal">NULL</span>);
            &#125;);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">自定义KVO-<code>removeObserver</code></h4>
<p>在移除观察者的时候首先需要遍历<code>observerArr</code>把observer中的keyPath给移除掉,然后把isa重新指向父类</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"> <span class="hljs-comment">// 指回给父类</span>
        Class superClass = [<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>];
        object_setClass(<span class="hljs-keyword">self</span>, superClass);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">自定义函数式KVO</h4>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">typedef</span> <span class="hljs-keyword">void</span>(^HBKVOBlock)(<span class="hljs-keyword">id</span> observer,<span class="hljs-built_in">NSString</span> *keyPath,<span class="hljs-keyword">id</span> oldValue,<span class="hljs-keyword">id</span> newValue);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么设计的话需要变动的地方有：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)hb_addObserver:(<span class="hljs-built_in">NSObject</span> *)observer forKeyPath:(<span class="hljs-built_in">NSString</span> *)keyPath block:(LGKVOBlock)block;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-class"><span class="hljs-keyword">@interface</span> <span class="hljs-title">HBKVOInfo</span> : <span class="hljs-title">NSObject</span></span>
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">weak</span>) <span class="hljs-built_in">NSObject</span>  *observer;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">copy</span>) <span class="hljs-built_in">NSString</span>    *keyPath;
<span class="hljs-keyword">@property</span> (<span class="hljs-keyword">nonatomic</span>, <span class="hljs-keyword">assign</span>) HBKVOBlock handleBlock;
<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">    <span class="hljs-built_in">NSMutableArray</span> *observerArr = objc_getAssociatedObject(<span class="hljs-keyword">self</span>, (__bridge <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> * _Nonnull)(kHBKVOAssiociateKey));
 <span class="hljs-keyword">for</span> (HBKVOInfo *info <span class="hljs-keyword">in</span> mArray) &#123;
        <span class="hljs-keyword">if</span> ([info.keyPath isEqualToString:keyPath] && info.handleBlock) &#123;
            info.handleBlock(info.observer, keyPath, oldValue, newValue);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">KVO自动销毁机制</h4>
<p>希望达到的效果是不用用户调用，自动释放。我们看到上面的<code>removeObserver</code>我们在这里面释放，但是如果用户不调用这个方法的话，是永远不会释放的。同时在上面的自定义的setter方法中，我们派生的子类还有一个<code>dealloc</code>方法没有实现。把<code>dealloc</code>的方法实现指定为下面的函数</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> hb_dealloc(<span class="hljs-keyword">id</span> <span class="hljs-keyword">self</span>,SEL _cmd)&#123;
  Class superClass = [<span class="hljs-keyword">self</span> <span class="hljs-keyword">class</span>];
   object_setClass(<span class="hljs-keyword">self</span>, superClass);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工程中验证一下，在这个方法调用之前self.person指向的是派生类，这个之后指向的是Person类
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927a8b1651f349338db525e6bc294bb5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">FaceBook的<code>FBKVOController</code>思考</h4>
<p>KVO的麻烦的地方在于每次移除比较麻烦，观察和回调的代码段不是连续的比较分散，看起来写起来都比较费劲。而<code>FBKVOController</code>利用了中介者模式，函数响应式调用、不需要手动销毁，vc不需要关注释放，它下层已经做好了相关的工作。
self-> _kvoCtrl -> FB单例 -> self.person</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (FBKVOController *)kvoCtrl&#123;
    <span class="hljs-keyword">if</span> (!_kvoCtrl) &#123;
        _kvoCtrl = [FBKVOController controllerWithObserver:<span class="hljs-keyword">self</span>];
    &#125;
    <span class="hljs-keyword">return</span> _kvoCtrl;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">    [<span class="hljs-keyword">self</span>.kvoCtrl observe:<span class="hljs-keyword">self</span>.person keyPath:<span class="hljs-string">@"name"</span> options:(<span class="hljs-built_in">NSKeyValueObservingOptionNew</span>) block:^(<span class="hljs-keyword">id</span>  _Nullable observer, <span class="hljs-keyword">id</span>  _Nonnull object, <span class="hljs-built_in">NSDictionary</span><<span class="hljs-built_in">NSString</span> *,<span class="hljs-keyword">id</span>> * _Nonnull change) &#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"****%@****"</span>,change);
    &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.创建一个info来接收<code>keyPath</code>、<code>option</code>、<code>block</code>
2.创建一个单例来把<code>object</code>这里指的是<code>self.person</code>和info关联起来
3.调用系统自身的kvo
4.在回调时拿到对应的<code>block</code>然后执行
​</p>
<p>FB自动销毁
我们控制器释放的时候，_kvoCtrl也会同步释放。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)dealloc
&#123;
  [<span class="hljs-keyword">self</span> unobserveAll];
  pthread_mutex_destroy(&_lock);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)unobserveAll
&#123;
  [<span class="hljs-keyword">self</span> _unobserveAll];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>释放的时候，拿到objectInfo的哈希map表一个一个移除，同时也移除所有的对象和信息。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)_unobserveAll
&#123;
  <span class="hljs-comment">// lock</span>
  pthread_mutex_lock(&_lock);

  <span class="hljs-built_in">NSMapTable</span> *objectInfoMaps = [_objectInfosMap <span class="hljs-keyword">copy</span>];

  <span class="hljs-comment">// clear table and map</span>
  [_objectInfosMap removeAllObjects];

  <span class="hljs-comment">// unlock</span>
  pthread_mutex_unlock(&_lock);

  _FBKVOSharedController *shareController = [_FBKVOSharedController sharedController];

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">id</span> object <span class="hljs-keyword">in</span> objectInfoMaps) &#123;
    <span class="hljs-comment">// unobserve each registered object and infos</span>
    <span class="hljs-built_in">NSSet</span> *infos = [objectInfoMaps objectForKey:object];
    [shareController unobserve:object infos:infos];
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<h4 data-id="heading-9"><code>GNUstep Base Library</code></h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgnustep%2Flibs-base" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/gnustep/libs-base" ref="nofollow noopener noreferrer">GNU</a>​
苹果开源的代码，可以看到KVO的内部实现跟本篇的自定义大致思想是一致的。</p></div>  
</div>
            