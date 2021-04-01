
---
title: 'InheritedWidget的使用和源码分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/537376ec27c34e239dade57609117859~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 01:07:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/537376ec27c34e239dade57609117859~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在用<strong>Flutter</strong>进行界面开发时，我们经常会遇到数据传递的问题。但是由于<strong>Flutter</strong>采用树形结构，造成数据传递的链条有时候会很长，代码写起来也很不方便。</p>
<p><strong>InheritedWidget</strong>可以让它的子节点能访问到它的公开属性，从而实现数据的跨Widget的传递。</p>
<h2 data-id="heading-0"><strong>InheritedWidget</strong>使用</h2>
<p>我们先用一个Demo来看看<strong>InheritedWidget</strong>的使用方法。Demo如下，<strong>InheritedWidget</strong>子类<strong>InfoWidget</strong>的<code>number</code>数值变化后，底下的三个<strong>InfoChildWidget</strong>显示的<code>number</code>也会变化。</p>
<p><img alt="demo" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/537376ec27c34e239dade57609117859~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>接下来我们来写代码。</p>
<ul>
<li>由于<strong>InheritedWidget</strong>是抽象类，我们创建一个继承 自<strong>InheritedWidget</strong>的<strong>InfoWidget</strong>。</li>
</ul>
<pre><code class="copyable">class InfoWidget extends InheritedWidget &#123;
  // 1
  final int number;
    
  // 2    
  InfoWidget(&#123;Key key, @required this.number, @required child&#125;)
      : super(key: key, child: child);
    
  //3    
  @override
  bool updateShouldNotify(InfoWidget oldWidget) &#123;
    return number != oldWidget.number;
  &#125;
  
  // 4
  static InfoWidget of(BuildContext context) &#123;
    return context.dependOnInheritedWidgetOfExactType(); 
  &#125;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码说明：</p>
<ol>
<li><code>number</code>就是定义的共享的数据；</li>
<li><strong>InfoWidget</strong>的构造函数中，有三个参数除了<code>key</code>外，都是必传参数，<code>number</code>是外部传入的给<strong>InfoWidget</strong>共享的数据，<code>child</code>是<strong>子Widget</strong>；</li>
</ol>
<blockquote>
<ul>
<li><strong>InheritedWidget</strong>是<strong>Widget</strong>的子类，但是没有<strong>StatefulWidget</strong>类似的<strong>State</strong>，这样<strong>InheritedWidget</strong>的所有属性都是不可变的，所以数据是需要<strong>父Widget</strong>提供的。</li>
<li><code>child</code>是<strong>InheritedWidget</strong>的必传参数，所以子类也得是必传参数。</li>
</ul>
</blockquote>
<ol start="3">
<li><strong>InheritedWidget</strong>的子类需要重写<code>updateShouldNotify</code>方法，这个方法如果返回<code>true</code>，则会回调<strong>StatefulElement</strong>中<strong>state</strong>的<code>didChangeDependencies</code>方法；</li>
<li><code>of</code>这个静态方法是留给<strong>子Widget</strong>使用的，<strong>子Widget</strong>可以通过它获取到<strong>InheritedWidget</strong>的共享数据。</li>
</ol>
<blockquote>
<p>取<code>of</code>方法名是个约定俗成，当然也可以随便取个合法的方法名。</p>
</blockquote>
<ul>
<li>建一个<strong>Widget</strong>，它可以显示<strong>InfoWidget</strong>共享的数据</li>
</ul>
<pre><code class="copyable">class InfoChildWidget extends StatelessWidget &#123;
  
  // 1
  const InfoChildWidget();

  @override
  Widget build(BuildContext context) &#123;
    // 2
    final int number = InfoWidget.of(context).number;
    return Text("$number", style: TextStyle(color: Colors.amber, fontSize: 40));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>使用<strong>InfoChildWidget</strong>的<strong>常量构造函数</strong>是为了解决不必要的重建和销毁。</li>
<li><code>InfoWidget.of(context)</code>就是上面提到的给<strong>子Widget</strong>使用的<code>of</code>静态方法，然后取到<strong>number</strong>就可以直接显示了。</li>
</ol>
<ul>
<li>使用</li>
</ul>
<pre><code class="copyable">InfoWidget(
    number: _number,
        child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                InfoChildWidget(),
                InfoChildWidget(),
                InfoChildWidget(),
              ],
            ),
        ),
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的时候是将<strong>InfoChildWidget</strong>做为<strong>InfoWidget</strong>的<strong>子Widget</strong>，我这里特意中间加了<strong>Center</strong>和<strong>Column</strong>，就是为了指出<strong>InfoChildWidget</strong>不一定需要是<strong>直接子Widget</strong>。</p>
<ul>
<li>所有代码如下：</li>
</ul>
<pre><code class="copyable">class MyApp extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo'),
    );
  &#125;
&#125;

class MyHomePage extends StatefulWidget &#123;
  MyHomePage(&#123;Key key, this.title&#125;) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
&#125;

class _MyHomePageState extends State<MyHomePage> &#123;
  int _number = 0;
  void _incrementCounter() &#123;
    _number = Random().nextInt(100);
    setState(() &#123;&#125;);
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: InfoWidget(
          number: _number,
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                InfoChildWidget(),
                InfoChildWidget(),
                InfoChildWidget(),
              ],
            ),
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  &#125;
&#125;

<!-- InfoWidget -->
class InfoWidget extends InheritedWidget &#123;
  final int number;

  InfoWidget(&#123;Key key, @required this.number, @required child&#125;)
      : super(key: key, child: child);

  @override
  bool updateShouldNotify(InfoWidget oldWidget) &#123;
    return number != oldWidget.number;
  &#125;

  static InfoWidget of(BuildContext context) &#123;
    return context.dependOnInheritedWidgetOfExactType();
  &#125;
&#125;

<!-- InfoChildWidget -->
class InfoChildWidget extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    final int number = InfoWidget.of(context).number;
    return Text("$number", style: TextStyle(color: Colors.amber, fontSize: 40));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img alt="效果" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63feedb5fe8c4db1b6862495db042356~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><strong>InheritedWidget</strong>源码分析</h2>
<h5 data-id="heading-2">设置inheritedWidgets</h5>
<p>每个<strong>Element</strong>都有一个<strong>key</strong>为<strong>InheritedWidget</strong>类型，值为<strong>InheritedElement</strong>的<strong>Map</strong>属性<code>_inheritedWidgets</code>。</p>
<pre><code class="copyable">Map<Type, InheritedElement>? _inheritedWidgets;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个<strong>Widget</strong>生成的<strong>Element</strong>挂载到<strong>Element Tree</strong>上的时候都会调用<code>mount</code>方法：</p>
<pre><code class="copyable"><!-- Element -->
void mount(Element? parent, dynamic newSlot) &#123;
    _updateInheritance();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mount</code>方法会调用<code>_updateInheritance</code>方法：</p>
<pre><code class="copyable"><!-- Element -->
void _updateInheritance() &#123;
    _inheritedWidgets = _parent?._inheritedWidgets;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不是<strong>InheritedElement</strong>,则<code>_inheritedWidgets</code>都指向父<strong>Element</strong>的<code>_inheritedWidgets</code>。</p>
<pre><code class="copyable"><!-- InheritedElement -->
void _updateInheritance() &#123;
    final Map<Type, InheritedElement>? incomingWidgets = _parent?._inheritedWidgets;
    if (incomingWidgets != null)
      _inheritedWidgets = HashMap<Type, InheritedElement>.from(incomingWidgets);
    else
      _inheritedWidgets = HashMap<Type, InheritedElement>();
    _inheritedWidgets![widget.runtimeType] = this;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是<strong>InheritedElement</strong>,先拷贝一份父节点的<code>_inheritedWidgets</code>, 然后添加或者替换key为<strong>widget.runtimeType</strong>，值为<strong>InheritedElement</strong>的键值对。</p>
<blockquote>
<p>注意：这里如果父类有相同的<strong>widget.runtimeType</strong>，则会被替换，也就是说如果有多个相同的<strong>InheritedWidget</strong>，子节点的<strong>Element</strong>只能找到离它最近的那个。</p>
</blockquote>
<p><img alt="inheritedWidgets" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac49979e388245608e6a27082461858d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3"><strong>子Element</strong>对<strong>InheritedElement</strong>并添加依赖</h5>
<p>我们来看看<code>of</code>类方法调用的<code>dependOnInheritedWidgetOfExactType</code>方法：</p>
<pre><code class="copyable"><!-- Element -->
Set<InheritedElement>? _dependencies;

T? dependOnInheritedWidgetOfExactType<T extends InheritedWidget>(&#123;Object? aspect&#125;) &#123;
    // 1
    final InheritedElement? ancestor = _inheritedWidgets == null ? null : _inheritedWidgets![T];
    if (ancestor != null) &#123;
      // 2
      return dependOnInheritedElement(ancestor, aspect: aspect) as T;
    &#125;
    _hadUnsatisfiedDependencies = true;
    return null;
&#125;

InheritedWidget dependOnInheritedElement(InheritedElement ancestor, &#123; Object? aspect &#125;) &#123;
    _dependencies ??= HashSet<InheritedElement>();
    // 3
    _dependencies!.add(ancestor);
    // 3
    ancestor.updateDependencies(this, aspect);
    return ancestor.widget;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>从<code>_inheritedWidgets</code>这个<strong>Map</strong>中找到类型对应的<strong>InheritedElement</strong>；</li>
<li>如果找到则调用<code>dependOnInheritedElement</code>方法；<code>dependOnInheritedElement</code>方法主要是将<strong>InheritedElement</strong>加入到<code>_dependencies</code>这个<strong>Set</strong>中，然后<strong>InheritedElement</strong>调用<code>updateDependencies</code>方法把<strong>子Element</strong>加入到<code>_dependents</code>中。</li>
</ol>
<pre><code class="copyable"><!-- InheritedElement -->
void updateDependencies(Element dependent, Object? aspect) &#123;
    setDependencies(dependent, null);
&#125;

void setDependencies(Element dependent, Object? value) &#123;
    _dependents[dependent] = value;
&#125;

final Map<Element, Object?> _dependents = HashMap<Element, Object?>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="updateDependencies" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5cff7b71cec418f9e184a4792e981e8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4"><strong>InheritedElement</strong>数据变化调用<strong>StatefulElement</strong>的<code>didChangeDependencies</code>方法：</h5>
<p><strong>InheritedWidget</strong>调用<code>build</code>方法的时候，会调用<code>notifyClients</code>方法：</p>
<pre><code class="copyable">void updated(InheritedWidget oldWidget) &#123;
    if (widget.updateShouldNotify(oldWidget))
      super.updated(oldWidget);
&#125;
  
void updated(covariant ProxyWidget oldWidget) &#123;
    notifyClients(oldWidget);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>notifyClients</code>方法会对<code>_dependents</code>中的每个<strong>子Element</strong>调用<code>notifyDependent</code>方法，<strong>子Element</strong>会调用<code>didChangeDependencies</code>方法：</p>
<pre><code class="copyable">void notifyClients(InheritedWidget oldWidget) &#123;
    for (final Element dependent in _dependents.keys) &#123;
      notifyDependent(oldWidget, dependent);
    &#125;
&#125;

void notifyDependent(covariant InheritedWidget oldWidget, Element dependent) &#123;
    dependent.didChangeDependencies();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>子Element</strong>调用<code>didChangeDependencies</code>最后会重新构建：</p>
<pre><code class="copyable">void didChangeDependencies() &#123;
    markNeedsBuild();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当<strong>子Element</strong>为<strong>StateFulElement</strong>时，会将<code>_didChangeDependencies</code>置为true；</p>
<pre><code class="copyable">void didChangeDependencies() &#123;
    super.didChangeDependencies();
    _didChangeDependencies = true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当重新构建时，<strong>StateFulElement</strong>会调用<strong>state</strong>的<code>didChangeDependencies</code>方法。</p>
<pre><code class="copyable">void performRebuild() &#123;
    if (_didChangeDependencies) &#123;
      state.didChangeDependencies();
      _didChangeDependencies = false;
    &#125;
    super.performRebuild();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="didChangeDependencies" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12ce9975de014d328fa7e8c7399b7d03~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">总结</h2>
<p><strong>InheritedWidget</strong>传递参数的方案只是把传参从<strong>Constructor</strong>变成了<strong>BuildContext</strong>。但是它还是有些的不完善的地方：</p>
<ol>
<li>某个类型的<strong>InheritedWidget</strong>只能获取到最近的那一个；</li>
<li>重新构建没法只重构依赖<strong>InheritedWidget</strong>的<strong>子Widget</strong>，性能上不是太好。</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            