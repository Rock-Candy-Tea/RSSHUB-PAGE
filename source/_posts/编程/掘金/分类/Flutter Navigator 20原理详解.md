
---
title: 'Flutter Navigator 2.0原理详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd8a3ebc1e144c308ee8b1367a532c7c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 01:37:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd8a3ebc1e144c308ee8b1367a532c7c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>Navigator 2.0</strong>作为新一代的路由提供了<em><strong>申明式</strong></em>的<strong>API</strong>，更加符合<strong>Flutter</strong>的风格。<strong>Navigator 2.0</strong>向前兼容，新增了一些新的<strong>API</strong>，使用的方式和<strong>Navigator 1.0</strong>相比有较大的差别。</p>
<p>本文将详细解析<strong>Navigator 2.0</strong>的底层逻辑，让大家对它有一个深入的了解，这样在使用上会更加的得心应手。</p>
<h2 data-id="heading-0">Navigator 2.0 诞生的背景</h2>
<p><strong>Flutter</strong>官方团队改造路由主要有几点原因：</p>
<ol>
<li><strong>Navigator 1.0</strong> 只提供了一些<code>push()</code>, <code>pushNamed()</code>和 <code>pop()</code>等简单的API。实现压入或者弹出多个页面很困难，更难实现对栈内中间页面的移除，交换等操作；</li>
<li><strong>Flutter</strong>随着<strong>2.0</strong>的到来实现了全平台的支持，这样也就新出现一些使用场景，譬如网页修改URL地址等，这些就需要新的API来支持；</li>
<li><strong>Navigator 2.0</strong>满足了嵌套路由的需求场景，这样开发者在使用时就更加的灵活和方便；</li>
<li><strong>Navigator 2.0</strong>提供的是<em><strong>申明式</strong></em>的<strong>API</strong>，解决了以前路由<em><strong>命令式编程</strong></em>的方式，让编程的风格统一。</li>
</ol>
<p><strong>Navigator 2.0</strong>的<strong>API</strong>虽然比较的多，但是逻辑还是比较清晰的，我们来一个个的进行介绍。</p>
<h2 data-id="heading-1"><code>Page</code></h2>
<p><strong>Page</strong>代表页面不可变的的配置信息，代表一个<em><strong>页面</strong></em>，类似于<strong>Widget</strong>配置信息转换成<strong>Element</strong>, <strong>Page</strong>配置的信息会转换成<strong>Route</strong>。</p>
<pre><code class="copyable">abstract class Page<T> extends RouteSettings &#123;
  
  const Page(&#123;
    this.key,
    String? name,
    Object? arguments,
    this.restorationId,
  &#125;) : super(name: name, arguments: arguments);


  bool canUpdate(Page<dynamic> other) &#123;
    return other.runtimeType == runtimeType &&
           other.key == key;
  &#125;

  @factory
  Route<T> createRoute(BuildContext context);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><code>createRoute</code>就是转换成<strong>Route</strong>的方法；</li>
<li><code>canUpdate</code>的实现方式和<strong>Widget</strong>的一样，也是用于<code>diff</code>算法。</li>
</ol>
</blockquote>
<h2 data-id="heading-2"><code>RouteSettings</code></h2>
<p><strong>Page</strong>的父类<strong>RouteSettings</strong>仅仅用来保存<code>name</code>和<code>arguments</code>这两个值。</p>
<pre><code class="copyable">const RouteSettings(&#123;
    this.name,
    this.arguments,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3"><code>Route</code></h2>
<p><strong>Route</strong>代表一个<em><strong>页面</strong></em>，是<strong>Navigator</strong>栈中真正管理的内容。</p>
<pre><code class="copyable">abstract class Route<T> &#123;
    
    // 1   
    RouteSettings get settings => _settings;
    NavigatorState? get navigator => _navigator;

    // 2
    List<OverlayEntry> get overlayEntries => const <OverlayEntry>[];
    
    // 3
    void install() &#123;&#125;
    TickerFuture didPush() &#123;&#125;
    ...
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><strong>Route</strong>持有了配置对象<code>page</code>和管理它的<code>navigator</code>对象;</li>
<li><strong>Route</strong>还持有一个<strong>OverlayEntry</strong>数组，<strong>OverlayEntry</strong>放置在类似于<strong>Stack</strong>的<strong>Overlay</strong>上，我们写的页面就是放置在一个<strong>OverlayEntry</strong>上的；</li>
<li><strong>Route</strong>还定义了一些协议方法需要子类覆写，这些方法主要是<strong>route</strong>的状态变化后收到的回调函数，这些函数调用主要来自于<code>_RouteEntry</code>。</li>
</ol>
</blockquote>





















































<table><thead><tr><th>方法</th><th>调用时机</th></tr></thead><tbody><tr><td><code>install</code></td><td>被插入<code>navigator</code></td></tr><tr><td><code>didPush</code></td><td>动画进入显示</td></tr><tr><td><code>didAdd</code></td><td>直接显示</td></tr><tr><td><code>didReplace</code></td><td>替换旧的<strong>route</strong></td></tr><tr><td><code>didPop</code></td><td>请求<strong>pop</strong>页面</td></tr><tr><td><code>didComplete</code></td><td><strong>pop</strong>完成后</td></tr><tr><td><code>didPopNext</code></td><td>当前<strong>route</strong>后面的<strong>route</strong>被pop</td></tr><tr><td><code>didChangeNext</code></td><td>当前<strong>route</strong>后面的<strong>route</strong>被替换</td></tr><tr><td><code>didChangePrevious</code></td><td>当前<strong>route</strong>前面的<strong>route</strong>被替换</td></tr><tr><td><code>changedInternalState</code></td><td>当前<strong>route</strong>的<strong>state</strong>变化后</td></tr><tr><td><code>changedExternalState</code></td><td>当前<strong>route</strong>的<code>navigator</code>变化后</td></tr></tbody></table>
<h4 data-id="heading-4"><code>MaterialPage</code> 和 <code>_PageBasedMaterialPageRoute</code></h4>
<p>我们可以直接使用系统给我们提供的<strong>Page</strong>类，也可以自定义继承自<strong>Page</strong>的类。我们来看看官方给我们提供的<strong>MaterialPage</strong>的逻辑。</p>
<p><strong>MaterialPage</strong>的Route是<code>_PageBasedMaterialPageRoute</code>类，它的继承逻辑是：<code>_PageBasedMaterialPageRoute</code> -> <code>PageRoute</code> -> <code>ModalRoute</code> -> <code>TransitionRoute</code> -> <code>OverlayRoute</code> + <code>LocalHistoryRoute</code> -> <code>Route</code>。</p>
<h6 data-id="heading-5"><code>LocalHistoryRoute</code></h6>
<p><strong>LocalHistoryRoute</strong>可以给<strong>Route</strong>添加一些<strong>LocalHistoryEntry</strong>。当<strong>LocalHistoryEntry</strong>不为空时，<code>didPop</code>方法调用的时候会移除最后一个<strong>LocalHistoryEntry</strong>，否则<strong>Route</strong>就要被<code>pop</code>了。</p>
<h6 data-id="heading-6"><code>OverlayRoute</code></h6>
<p><strong>OverlayRoute</strong>主要是持有<strong>Route</strong>对应的<code>OverlayEntry</code>数组，这个数组是子类在被插入<code>navigator</code>的时候对其进行赋值的。</p>
<pre><code class="copyable">abstract class OverlayRoute<T> extends Route<T> &#123;
    @factory
    Iterable<OverlayEntry> createOverlayEntries();
    
    List<OverlayEntry> get overlayEntries => _overlayEntries;
    
    void install() &#123;
        _overlayEntries.addAll(createOverlayEntries());
        super.install();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7"><code>TransitionRoute</code></h6>
<p><strong>TransitionRoute</strong>是主要是负责动画部分。</p>
<pre><code class="copyable">abstract class TransitionRoute<T> extends OverlayRoute<T> &#123;
    
    Animation<double>? get animation => _animation;
    Animation<double>? get secondaryAnimation => _secondaryAnimation;
    
    void install() &#123;
        _animation = createAnimation()
          ..addStatusListener(_handleStatusChanged);
        super.install();
    &#125;
    
    TickerFuture didPush() &#123;
        super.didPush();
        return _controller!.forward();
    &#125;
    
    void didAdd() &#123;
        super.didAdd();
        _controller!.value = _controller!.upperBound;
    &#125;
    
    bool didPop(T? result) &#123;
        _controller!.reverse();
        return super.didPop(result);
    &#125;

    void didPopNext(Route<dynamic> nextRoute) &#123;
        _updateSecondaryAnimation(nextRoute);
        super.didPopNext(nextRoute);
    &#125;

    void didChangeNext(Route<dynamic>? nextRoute) &#123;
        _updateSecondaryAnimation(nextRoute);
        super.didChangeNext(nextRoute);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><strong>TransitionRoute</strong>有<code>_animation</code>和<code>secondaryAnimation</code>两个动画,前者负责当前<strong>Route</strong>的<strong>push</strong>和<strong>pop</strong>动画，后者负责下一个<strong>Route</strong>进行<strong>push</strong>和<strong>pop</strong>时本身这个<strong>Route</strong>的动画。</li>
<li><code>_animation</code>是<code>install</code>就生成了，<code>secondaryAnimation</code>可以大部分情况下就是下一个<strong>Route</strong>的<code>_animation</code>, 所以<code>didPopNext</code>和<code>didChangeNext</code>时需要更新<code>secondaryAnimation</code>。</li>
<li>如果不需要动画时调用的是<code>didAdd</code>方法，<strong>Route</strong>是被动调用的这个方法，其实是<code>_RouteEntry</code>根据(<strong>Navigator确定的</strong>)状态判断调用的这个方法。</li>
</ol>
</blockquote>
<h6 data-id="heading-8"><code>ModalRoute</code></h6>
<p><strong>ModalRoute</strong>主要的作用是阻止除最上层的<strong>Route</strong>之外的<strong>Route</strong>进行用户交互，其中的知识点也是非常丰富的。</p>
<pre><code class="copyable">abstract class ModalRoute<T> extends TransitionRoute<T> with LocalHistoryRoute<T> &#123;
    
  Iterable<OverlayEntry> createOverlayEntries() sync* &#123;
    yield _modalBarrier = OverlayEntry(builder: _buildModalBarrier);
    yield _modalScope = OverlayEntry(builder: _buildModalScope, maintainState: maintainState);
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><strong>ModalRoute</strong>生成了两个非常重要的<code>OverlayEntry</code>---<code>_modalBarrier</code>和<code>_modalScope</code>。</li>
<li><code>_modalBarrier</code>实现了阻止用户对最上层<strong>Route</strong>之外的<strong>Route</strong>进行用户交互的功能；</li>
<li><code>_modalScope</code>会持有<strong>router</strong>自身，<code>_modalScope</code>在构建的时候就会调用<strong>router</strong>的<code>buildTransitions</code>和<code>buildChild</code>方法，参数都包含<strong>router</strong>的<code>animation</code>和<code>secondaryAnimation</code>,也就是<strong>TransitionRoute</strong>中的两个动画属性；</li>
</ol>
</blockquote>
<pre><code class="copyable">Widget _buildModalScope(BuildContext context) &#123;
    return _modalScopeCache ??= Semantics(
      sortKey: const OrdinalSortKey(0.0),
      child: _ModalScope<T>(
        key: _scopeKey,
        route: this,
        // _ModalScope calls buildTransitions() and buildChild(), defined above
      )
    );
&#125;

Widget buildPage(BuildContext context, Animation<double> animation, Animation<double> secondaryAnimation);

Widget buildTransitions(
    BuildContext context,
    Animation<double> animation,
    Animation<double> secondaryAnimation,
    Widget child,
  ) &#123;
    return child;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们接下来看看<code>_ModalScope</code>的<code>_ModalScopeState</code>的内容：</p>
<pre><code class="copyable">class _ModalScopeState<T> extends State<_ModalScope<T>> &#123;
    
    late Listenable _listenable;
    
    final FocusScopeNode focusScopeNode = FocusScopeNode(debugLabel: '$_ModalScopeState Focus Scope');
    
    void initState() &#123;
        super.initState();
        final List<Listenable> animations = <Listenable>[
          if (widget.route.animation != null) widget.route.animation!,
          if (widget.route.secondaryAnimation != null) widget.route.secondaryAnimation!,
        ];
        _listenable = Listenable.merge(animations);
        if (widget.route.isCurrent) &#123;
          widget.route.navigator!.focusScopeNode.setFirstFocus(focusScopeNode);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><code>_listenable</code>是<strong>route</strong>的<code>animation</code>和<code>secondaryAnimation</code>的组合；</li>
<li><code>focusScopeNode</code>是焦点，初始化的时候将<code>navigator</code>的焦点设置为这个焦点，这样就实现了最上层的<strong>Route</strong>才获取到焦点，屏蔽对其他<strong>Route</strong>的焦点获取；</li>
</ol>
</blockquote>
<pre><code class="copyable">  Widget build(BuildContext context) &#123;
    // 1 RestorationScope
    return AnimatedBuilder(
      animation: widget.route.restorationScopeId,
      builder: (BuildContext context, Widget? child) &#123;
        return RestorationScope(
          restorationId: widget.route.restorationScopeId.value,
          child: child!,
        );
      &#125;,
      // 2 _ModalScopeStatus
      child: _ModalScopeStatus(
        route: widget.route,
        isCurrent: widget.route.isCurrent, // _routeSetState is called if this updates
        canPop: widget.route.canPop, // _routeSetState is called if this updates
        child: Offstage(
          offstage: widget.route.offstage, // _routeSetState is called if this updates
          child: PageStorage(
            bucket: widget.route._storageBucket, // immutable
            child: Builder(
              builder: (BuildContext context) &#123;
                return Actions(
                  actions: <Type, Action<Intent>>&#123;
                    DismissIntent: _DismissModalAction(context),
                  &#125;,
                  child: PrimaryScrollController(
                    controller: primaryScrollController,
                    child: FocusScope(
                      node: focusScopeNode, // immutable
                      // 3 RepaintBoundary
                      child: RepaintBoundary(
                        // 4. AnimatedBuilder
                        child: AnimatedBuilder(
                          animation: _listenable, // immutable
                          builder: (BuildContext context, Widget? child) &#123;
                            // 5. buildTransitions
                            return widget.route.buildTransitions(
                              context,
                              widget.route.animation!,
                              widget.route.secondaryAnimation!,
                              AnimatedBuilder(
                                animation: widget.route.navigator?.userGestureInProgressNotifier ?? ValueNotifier<bool>(false),
                                builder: (BuildContext context, Widget? child) &#123;
                                  final bool ignoreEvents = _shouldIgnoreFocusRequest;
                                  focusScopeNode.canRequestFocus = !ignoreEvents;
                                  return IgnorePointer(
                                    ignoring: ignoreEvents,
                                    child: child,
                                  );
                                &#125;,
                                child: child,
                              ),
                            );
                          &#125;,
                          child: _page ??= RepaintBoundary(
                            key: widget.route._subtreeKey, // immutable
                            child: Builder(
                              builder: (BuildContext context) &#123;
                                return widget.route.buildPage(
                                  context,
                                  widget.route.animation!,
                                  widget.route.secondaryAnimation!,
                                );
                              &#125;,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                );
              &#125;,
            ),
          ),
        ),
      ),
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_ModalScopeState</code>的<code>build</code>方法是设计非常精妙的一个方法：</p>
<blockquote>
<ol>
<li><code>RestorationScope</code>负责<strong>Route</strong>用于恢复数据的作用；</li>
<li><code>_ModalScopeStatus</code>是<strong>InheritedWidget</strong>，它保持对<strong>Route</strong>的引用，所以我们在调用<code>ModalRoute.of(contex)</code>获取页面传参时，就是通过获取的这个<code>_ModalScopeStatus</code>，再找到对应的传参。</li>
<li>中间放置了一个<code>RepaintBoundary</code>可以限制重绘的区域，这样可以提高进行动画时绘制的效率；</li>
<li>最底层的<code>AnimatedBuilder</code>这个<strong>Widget</strong>是核心，这个<code>AnimatedBuilder</code>的<code>child</code>是由<code>route.buildPage()</code>这个方法创建的，其实就是我们<strong>Page</strong>的<strong>child</strong>，即开发者写的页面内容；这个<code>AnimatedBuilder</code>的<code>builder</code>方法中调用了<code>route.buildTransitions()</code>,它驱动动画是<code>_listenable</code>，也就是说<code>animation</code>和<code>secondaryAnimation</code>都能驱动它的动画过程。这其实很好理解：当前<strong>Route</strong>的<strong>pop</strong>和<strong>push</strong>和下个<strong>Route</strong>的<strong>pop</strong>和<strong>push</strong>都会触发动画的产生。</li>
</ol>
</blockquote>
<h6 data-id="heading-9"><code>PageRoute</code></h6>
<p><code>PageRoute</code>主要就是让最上层下面的<strong>Route</strong>不可见，点击<code>_modalBarrier</code>不让当前<strong>Route</strong>从<strong>Navigator</strong>栈中弹出。</p>
<pre><code class="copyable">abstract class PageRoute<T> extends ModalRoute<T> &#123;

  @override
  bool get opaque => true;

  @override
  bool get barrierDismissible => false;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10"><code>_PageBasedMaterialPageRoute</code></h6>
<p><code>_PageBasedMaterialPageRoute</code>的作用是覆写了<code>buildPage</code>方法, 返回的是开发者写的界面；</p>
<pre><code class="copyable">class _PageBasedMaterialPageRoute<T> extends PageRoute<T> with MaterialRouteTransitionMixin<T> &#123;
    Widget buildContent(BuildContext context) &#123;
        return _page.child;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方为我们提供了默认的<strong>pop</strong>和<strong>push</strong>动画，它们就在混入的<code>MaterialRouteTransitionMixin</code>中实现的。<code>MaterialRouteTransitionMixin</code>会根据不同的平台有不同的实现，iOS是左后的动画，Android是上下的动画，web也是左右动画。</p>
<p>我们以iOS为例，其最后使用的是<code>CupertinoPageTransition</code>这个类的方法：</p>
<pre><code class="copyable">SlideTransition(
    position: _secondaryPositionAnimation,
    textDirection: textDirection,
    transformHitTests: false,
    child: SlideTransition(
    position: _primaryPositionAnimation,
    textDirection: textDirection,
    child: DecoratedBoxTransition(
        decoration: _primaryShadowAnimation,
        child: child,
    ),
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到<strong>SlideTransition</strong>嵌套到一个<strong>child</strong>上是不是很疑惑？两个动画用在一个<strong>Widget</strong>上？</p>
<p>先解释下其他参数：</p>
<blockquote>
<ol>
<li><code>textDirection</code>决定了滑动的方法，因为有些语言是从右到左排序的；</li>
<li><code>transformHitTests</code>设置为flase,点击事件的响应位置不受动画的影响；</li>
<li><code>_primaryShadowAnimation</code>是设置了一个动画中的阴影。</li>
</ol>
</blockquote>
<p><code>_secondaryPositionAnimation</code>是从<code>Offset.zero</code>到<code>Offset(-1.0/3.0, 0.0)</code>，正常情况下就是从右往左移动1/3的屏幕宽度。</p>
<pre><code class="copyable">final Animatable<Offset> _kMiddleLeftTween = Tween<Offset>(
  begin: Offset.zero,
  end: const Offset(-1.0/3.0, 0.0),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_primaryPositionAnimation</code>是从<code>Offset(1.0, 0.0)</code>到<code>Offset.zero</code>，正常情况下就是从不可见的屏幕右边移动到屏幕最左边，然后占据整个屏幕宽度。</p>
<pre><code class="copyable">final Animatable<Offset> _kRightMiddleTween = Tween<Offset>(
  begin: const Offset(1.0, 0.0),
  end: Offset.zero,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们接下来解释下<strong>pop</strong>一个<strong>Route</strong>时候的动画逻辑, <strong>Animation:0->1</strong></p>
<ol>
<li>新加的<strong>Route</strong>是被<code>_primaryPositionAnimation</code>直接驱动的，也就是执行了从右到左的<code>_kRightMiddleTween</code>动画;</li>
<li><code>_secondaryPositionAnimation</code>只是被修改了值，我们前面<strong>TransitionRoute</strong>的介绍中提到过，新加入<strong>Route</strong>的<code>animation</code>赋值给了前一个<strong>Route</strong>的<code>secondaryAnimation</code>属性。<code>_ModalScopeState</code>中介绍过<code>secondaryAnimation</code>也能驱动<strong>Route</strong>的动画，也就是说前一个<strong>Route</strong>也能产生一个<code>_kMiddleLeftTween</code>动画；</li>
</ol>
<p>概括：</p>
<p>新加的<strong>Route</strong>通过<code>animation</code>驱动从屏幕右边移动到左边的动画，<code>animation</code>赋值给了前一个<strong>Route</strong>的<code>secondaryAnimation</code>驱动前一个<strong>Route</strong>向左移动1/3个屏幕位置。</p>
<p><strong>push</strong>的逻辑类似，只是一个反向的动画<code>reverse</code>。前一个<strong>Route</strong>在<code>secondaryAnimation</code>的驱动下右移了1/3屏幕宽度，当前的<strong>Route</strong>在<code>animation</code>驱动下移出屏幕。</p>
<p>我们可以点击<strong>Flutter DevTools</strong>的<strong>Slow Animations</strong>看看动画的慢放过程：</p>
<p><img alt="动画" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd8a3ebc1e144c308ee8b1367a532c7c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-11">阶段总结</h6>
<p><img alt="总结" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88124413f5804c6494936b6e986093ab~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12"><code>_RouteEntry</code></h2>
<p><strong>Navigator</strong>不是直接操作的<strong>Route</strong>，而是<strong>Route</strong>的封装类<code>_RouteEntry</code>。</p>
<pre><code class="copyable">_RouteEntry(
    this.route, 
    &#123;
      required _RouteLifecycle initialState,
      this.restorationInformation,
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>_RouteEntry</strong>除了持有<code>route</code>外，还持有一个<code>_RouteLifecycle</code>，即路由状态。</p>
<p>函数则主要是修改<code>_RouteLifecycle</code>状态的函数，譬如<code>markForPush</code>,<code>markForAdd</code>,<code>markForPop</code>,<code>markForRemove</code>,<code>markForComplete</code>等。此外还有<code>_RouteLifecycle</code>被标记后对<strong>Route</strong>进行操作函数，譬如<code>handlePush</code>，<code>handleAdd</code>,<code>handlePop</code>,<code>remove</code>等。</p>
<h2 data-id="heading-13"><code>Navigator</code></h2>
<pre><code class="copyable">Navigator(&#123;
    Key? key,
    this.pages = const <Page<dynamic>>[],
    // ...
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Navigator</code>的构造方法中有一个关键的属性<code>pages</code>,<strong>Navigator</strong>会将传入的<code>pages</code>会转换成<strong>Routes</strong>对应的<code>_RouteEntry</code>数组。</p>
<blockquote>
<p>实现<em><strong>申明式</strong></em>编程的逻辑就是修改这个<code>pages</code>中的内容，<strong>Navigator</strong>会自动实现对应的跳转，返回，替换等操作。<code>Navigator.push</code>,<code>Navigator.pop</code>等以前使用的方法就被将不是开发者需要考虑的使用方法了。</p>
</blockquote>
<p>我们接下来分析<strong>NavigatorState</strong>的重要代码。</p>
<pre><code class="copyable">class NavigatorState extends State<Navigator> with TickerProviderStateMixin, RestorationMixin &#123;
    
    List<_RouteEntry> _history = <_RouteEntry>[];
    
    late GlobalKey<OverlayState> _overlayKey;
    OverlayState? get overlay => _overlayKey.currentState;
    
    final FocusScopeNode focusScopeNode = FocusScopeNode(debugLabel: 'Navigator Scope');
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><code>_history</code>就是<code>pages</code>中每个<strong>Page</strong>通过<code>createRoute</code>生成的<code>_RouteEntry</code>数组；</li>
<li><strong>OverlayState</strong><code>overlay</code>代表的就是<strong>OverLay</strong>，它负责摆放每个<strong>Route</strong>的<code>overlayEntries</code>数组；<strong>OverLay</strong>就相当于一个<strong>Stack</strong>，专门用于放置<strong>OverlayEntry</strong>。</li>
</ol>
</blockquote>
<p><strong>NavigatorState</strong>的核心方法是<code>didUpdateWidget</code>方法, 其调用了一个<code>_updatePages()</code>方法：</p>
<pre><code class="copyable">void didUpdateWidget(Navigator oldWidget) &#123;
    _updatePages();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>_updatePages</code>方法的主要作用是对<code>pages</code>进行<strong>diff</strong>比对，更新<code>_history</code>数组中每个<code>_routeEntry</code>的<code>_RouteLifecycle</code>, 最后调用<code>_flushHistoryUpdates()</code>方法。</p>
<blockquote>
<p><code>_routeEntry</code>比对的方法和<code>MultiChildRenderObjectElement</code>的比对方法是一样的，先前往后比对能复用的元素，然后从后往前比对能复用的元素，然后对剩下的元素进行复用或者新建，不能复用的元素进行销毁。</p>
</blockquote>
<pre><code class="copyable">void _flushHistoryUpdates(&#123;bool rearrangeOverlay = true&#125;) &#123;
    final List<_RouteEntry> toBeDisposed = <_RouteEntry>[];
    while (index >= 0) &#123;
      switch (entry!.currentState) &#123;
        case _RouteLifecycle.push:
        case _RouteLifecycle.pushReplace:
        case _RouteLifecycle.replace:
          entry.handlePush(
            navigator: this,
            previous: previous?.route,
            previousPresent: _getRouteBefore(index - 1, _RouteEntry.isPresentPredicate)?.route,
            isNewFirst: next == null,
          );
          if (entry.currentState == _RouteLifecycle.idle) &#123;
            continue;
          &#125;
          break;
        // ...
      &#125;
      index -= 1;
      next = entry;
      entry = previous;
      previous = index > 0 ? _history[index - 1] : null;
    &#125;

    _flushObserverNotifications();

    _flushRouteAnnouncement();

    for (final _RouteEntry entry in toBeDisposed) &#123;
      for (final OverlayEntry overlayEntry in entry.route.overlayEntries)
        overlayEntry.remove();
      entry.dispose();
    &#125;
    
    if (rearrangeOverlay) &#123;
      overlay?.rearrange(_allRouteOverlayEntries);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li>根据每个<code>_RouteEntry</code>的<code>_RouteLifecycle</code>调用对应的方法，例如如果<strong>Route</strong>被标记为<code>_RouteLifecycle.push</code>,则调用<code>handlePush</code>方法，这样此<strong>Route</strong>就会调用<code>install</code>方法插入<strong>Navigator</strong>的树中，然后进行动画；</li>
<li><code>_flushObserverNotifications</code>是对每个<code>_NavigatorObservation</code>监听者进行通知；</li>
<li><code>_flushRouteAnnouncement</code>主要是对每个<strong>Route</strong>的前后关系进行梳理更新，<code>secondaryAnimation</code>的更新就是这个时候进行的；</li>
<li>将不需要的<code>_RouteEntry</code>的<code>overlayEntries</code>从<strong>Overlay</strong>上移除，因为不需要再显示了；</li>
<li>然后将所有的<code>_RouteEntry</code>的<code>overlayEntries</code>更新到<strong>Overlay</strong>上,代码在<code>build</code>方法中可以看到添加的逻辑如下。</li>
</ol>
</blockquote>
<pre><code class="copyable">Widget build(BuildContext context) &#123;
    return HeroControllerScope.none(
      child: Listener(
        onPointerDown: _handlePointerDown,
        onPointerUp: _handlePointerUpOrCancel,
        onPointerCancel: _handlePointerUpOrCancel,
        child: AbsorbPointer(
          absorbing: false, // it's mutated directly by _cancelActivePointers above
          child: FocusScope(
            node: focusScopeNode,
            autofocus: true,
            child: UnmanagedRestorationScope(
              bucket: bucket,
              child: Overlay(
                key: _overlayKey,
                initialEntries: overlay == null ?  _allRouteOverlayEntries.toList(growable: false) : const <OverlayEntry>[],
              ),
            ),
          ),
        ),
      ),
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺便提一下<strong>HeroControllerScope</strong>是负责进行<strong>Hero</strong>动画的的<strong>Widget</strong>，类似于Android中的<em><strong>共享元素动画</strong></em>。</p>
<h6 data-id="heading-14">阶段总结</h6>
<p><img alt="阶段总结" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cad201950edb441b95592d071db6821f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>到目前为止，我们通过切换Navigator的<code>page</code>就能够实现路由切换了，是不是文章就结束了？没有，因为Navigator 2.0是为<strong>Flutter 2.0</strong> 的全平台而生的，目前还没有解决一些问题，例如<strong>编辑浏览器网址</strong>，<strong>网页返回</strong>，<strong>安卓物理键返回</strong>等功能。</p>
<h2 data-id="heading-15"><code>Router</code></h2>
<pre><code class="copyable">Router(&#123;
    Key? key,
    this.routeInformationProvider,
    this.routeInformationParser,
    required this.routerDelegate,
    this.backButtonDispatcher,
  &#125;)
  
final RouteInformationProvider? routeInformationProvider;
final RouteInformationParser<T>? routeInformationParser;
final RouterDelegate<T> routerDelegate;
final BackButtonDispatcher? backButtonDispatcher;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到<strong>Router</strong>有四个属性，<code>RouteInformationProvider</code>路由信息提供者，<code>RouteInformationParser</code>路由信息解析者，<code>RouterDelegate</code>路由信息的处理代理，<code>BackButtonDispatcher</code>返回处理的分发者。他们四个协同作用，共同实现路由的功能。</p>
<h6 data-id="heading-16"><code>RouteInformation</code></h6>
<p>上面说的到路由信息就是指<code>RouteInformation</code>，包括路由的路径<code>location</code>和路由对应的状态<code>state</code>。这里所指的状态就是数据。</p>
<pre><code class="copyable">class RouteInformation &#123;

  final String? location;
  final Object? state;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17"><code>RouteInformationProvider</code></h6>
<p><code>RouteInformationProvider</code>只有一个抽象方法<code>routerReportsNewRouteInformation</code>，这个方法的作用是根据<code>RouteInformation</code>进行一些额外的操作。</p>
<pre><code class="copyable">abstract class RouteInformationProvider extends ValueListenable<RouteInformation?> &#123;
  void routerReportsNewRouteInformation(RouteInformation routeInformation) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>系统默认使用的是<code>PlatformRouteInformationProvider</code>, 它的<code>routerReportsNewRouteInformation</code>方法中回调了系统路由的更新，例如浏览器就会在<strong>History</strong>栈中新增一条历史访问记录:</p>
<pre><code class="copyable">class PlatformRouteInformationProvider extends RouteInformationProvider with WidgetsBindingObserver, ChangeNotifier &#123;

    void routerReportsNewRouteInformation(RouteInformation routeInformation) &#123;
        SystemNavigator.routeInformationUpdated(
          location: routeInformation.location!,
          state: routeInformation.state,
        );
        _value = routeInformation;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18"><code>RouteInformationParser</code></h6>
<p>这个类的作用是对<strong>T</strong>页面模型和<strong>RouteInformation</strong>路由信息进行相互转换：</p>
<pre><code class="copyable">abstract class RouteInformationParser<T> &#123;
  
  Future<T> parseRouteInformation(RouteInformation routeInformation);

  RouteInformation? restoreRouteInformation(T configuration) => null;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>parseRouteInformation</code>这个方法主要是解析初始路由的时候会使用到，例如 根据<code>RouteInformation(location: "/")</code>显示启动页面；</p>
<p><code>restoreRouteInformation</code>这个方法就是根据<strong>T</strong>页面模型生成对应的<code>RouteInformation</code>。</p>
<h6 data-id="heading-19"><code>RouterDelegate</code></h6>
<p><code>RouterDelegate</code>顾名思义就是代替<code>Router</code>工作的类，它包括根据<strong>T</strong>页面模型添加一个页面，<strong>pop</strong>一个页面，提供构建的内容等。</p>
<pre><code class="copyable">abstract class RouterDelegate<T> extends Listenable &#123;
  
  Future<void> setInitialRoutePath(T configuration) &#123;
    return setNewRoutePath(configuration);
  &#125;

  Future<void> setNewRoutePath(T configuration);

  Future<bool> popRoute();

  T? get currentConfiguration => null;

  Widget build(BuildContext context);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以混入<code>PopNavigatorRouterDelegateMixin</code>的<code>popRoute</code>方法，就不用自己去实现了。</p>
</blockquote>
<p>我们从源码角度看看<code>RouteInformationProvider</code>，<code>RouteInformationParser</code>和<code>RouterDelegate</code>他们三者在初始化路由是如何实现的：</p>
<pre><code class="copyable">class _RouterState<T> extends State<Router<T>> &#123;

  void initState() &#123;
    super.initState();
    if (widget.routeInformationProvider != null) &#123;
      _processInitialRoute();
    &#125;
  &#125;

  void _processInitialRoute() &#123;
    _currentRouteInformationParserTransaction = Object();
    _currentRouterDelegateTransaction = Object();
    _lastSeenLocation = widget.routeInformationProvider!.value!.location;
    widget.routeInformationParser!
      .parseRouteInformation(widget.routeInformationProvider!.value!)
      .then<T>(_verifyRouteInformationParserStillCurrent(_currentRouteInformationParserTransaction, widget))
      .then<void>(widget.routerDelegate.setInitialRoutePath)
      .then<void>(_verifyRouterDelegatePushStillCurrent(_currentRouterDelegateTransaction, widget))
      .then<void>(_rebuild);
  &#125;    
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>_processInitialRoute</code>方法中我们看到了，<code>routeInformationParser</code>解析<code>routeInformationProvider</code>的<code>value</code>，然后<code>routerDelegate</code>根据这个解析的结果去调用<code>setNewRoutePath</code>设置路由。</p>
<p><code>routeInformationProvider</code> -> <code>routeInformationParser</code> -> <code>routerDelegate</code> -> (<code>setNewRoutePath</code>)</p>
<p><code>RouterDelegate</code>的覆写案例：</p>
<pre><code class="copyable">class MyRouterDelegate extends RouterDelegate<PageConfiguration>
    with ChangeNotifier, PopNavigatorRouterDelegateMixin<PageConfiguration> &#123;
    
    final List<Page> _pages = [];
    
    final AppState appState;
    final GlobalKey<NavigatorState> navigatorKey;
    
    ShoppingRouterDelegate(this.appState) : navigatorKey = GlobalKey() &#123;
        appState.addListener(() &#123;
          notifyListeners();
        &#125;);
    &#125;

    List<MaterialPage> get pages => List.unmodifiable(_pages);
        
    
    Future<bool> popRoute() &#123;
        _removePage(_pages.last);
        return Future.value(false);
    &#125;
    
    Future<void> setNewRoutePath(PageConfiguration configuration) &#123;
        if (shouldAddPage) &#123;
          _pages.clear();
          addPage(configuration);
        &#125;
        return SynchronousFuture(null);
    &#125;
        
    Widget build(BuildContext context) &#123;
        return Navigator(
          key: navigatorKey,
          onPopPage: _onPopPage,
          pages: buildPages(),
        );
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><code>MyRouterDelegate</code>有<code>_pages</code>属性，这个属性作为<code>Navigator</code>的<code>pages</code>；<code>appState</code>是状态管理的数据，用这个数据去驱动<code>MyRouterDelegate</code>的观察者也就是<code>Router</code>即去重构，这样<code>Navigator</code>也就会重构了。</li>
<li><code>popRoute</code>将<code>_pages</code>的最后一个页面删掉，通知<code>Router</code>即去重构，更新<code>Navigator</code>；</li>
<li><code>setNewRoutePath</code>给<code>_pages</code>添加对应的<strong>Page</strong>，通知<code>Router</code>即去重构<code>Navigator</code>。</li>
</ol>
<h2 data-id="heading-20"><code>BackButtonDispatcher</code></h2>
<p><code>BackButtonDispatcher</code>主要就是解决安卓，网页等物理返回的事件。它有两个子类<code>RootBackButtonDispatcher</code>和<code>ChildBackButtonDispatcher</code>可以解决<strong>Navigator</strong>的嵌套问题。</p>
<p><code>BackButtonDispatcher</code>的返回处理可以直接交给<code>RouterDelegate</code>去处理，例如下面的逻辑：</p>
<pre><code class="copyable">class MyBackButtonDispatcher extends RootBackButtonDispatcher &#123;

  final MyRouterDelegate _routerDelegate;

  MyBackButtonDispatcher(this._routerDelegate)
      : super();

  // 3
  @override
  Future<bool> didPopRoute() &#123;
    return _routerDelegate.popRoute();
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-21">最后总结</h6>
<p><img alt="最后总结" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca589292cbf641d59154ee8aac3660bc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">总结</h2>
<p><strong>Navigator 2.0</strong>的功能更加强大了，使用方式也变得更加<strong>Flutter</strong>了。但是变得更复杂了，这样对学习和使用成本造成了很大的困扰，这方面也是很多人认为<strong>Navigator 2.0</strong>是一个失败的改造的原因。</p>
<p>本文主要从源码角度分析了<strong>Navigator 2.0</strong>的实现逻辑，原理清楚后些代码应该还是很简单的。</p>
<p>如果你需要Demo，可以参阅下面两篇文章的代码，特别是第一篇文章的代码非常具有参考价值：</p>
<p><a href="https://www.raywenderlich.com/19457817-flutter-navigator-2-0-and-deep-links#toc-anchor-001" target="_blank" rel="nofollow noopener noreferrer">Flutter Navigator 2.0 and Deep Links</a></p>
<p><a href="https://medium.com/flutter/learning-flutters-new-navigation-and-routing-system-7c9068155ade" target="_blank" rel="nofollow noopener noreferrer">Learning Flutter’s new navigation and routing system</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            