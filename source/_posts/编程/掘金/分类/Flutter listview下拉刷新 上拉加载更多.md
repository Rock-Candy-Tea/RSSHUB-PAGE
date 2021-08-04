
---
title: 'Flutter listview下拉刷新 上拉加载更多'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6fd34fd6d094a1dad0fb91f9d5e292e~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 02:03:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6fd34fd6d094a1dad0fb91f9d5e292e~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">下拉刷新</h1>
<p>在Flutter中系统已经为我们提供了google material design的刷新功能 , 样式与原生Android一样.
我们可以使用RefreshIndicator组件来实现Flutter中的下拉刷新，下面们还是先来看下如何使用吧</p>
<h2 data-id="heading-1">RefreshIndicator</h2>
<p>构造方法:</p>
<pre><code class="copyable"> const RefreshIndicator(&#123;
    Key key,
    @required this.child,
    this.displacement: 40.0,      //触发下拉刷新的距离
    @required this.onRefresh,     //下拉回调方法
    this.color,                   //进度指示器前景色 默认为系统主题色
    this.backgroundColor,         //背景色
    this.notificationPredicate: defaultScrollNotificationPredicate,
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们看一下效果以及实现方式:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6fd34fd6d094a1dad0fb91f9d5e292e~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们看一下代码:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_MyHomePageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">MyHomePage</span>> </span>&#123;
  <span class="hljs-built_in">List</span> list = <span class="hljs-keyword">new</span> <span class="hljs-built_in">List</span>(); <span class="hljs-comment">//列表要展示的数据</span>
 

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> initState() &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement initState</span>
    <span class="hljs-keyword">super</span>.initState();
    getData();
  &#125;

  <span class="hljs-comment"><span class="markdown">/<span class="hljs-strong">**
   <span class="hljs-emphasis">* 初始化list数据 加延时模仿网络请求
   *</span>/</span></span></span>
  Future getData() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">2</span>), () &#123;
      setState(() &#123;
        list = <span class="hljs-built_in">List</span>.generate(<span class="hljs-number">15</span>, (i) => <span class="hljs-string">'哈喽,我是原始数据 <span class="hljs-subst">$i</span>'</span>);
      &#125;);
    &#125;);
  &#125;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Scaffold(
      appBar: <span class="hljs-keyword">new</span> AppBar(
        <span class="hljs-comment">// Here we take the value from the MyHomePage object that was created by</span>
        <span class="hljs-comment">// the App.build method, and use it to set our appbar title.</span>
        title: <span class="hljs-keyword">new</span> Text(widget.title),
      ),
      body: RefreshIndicator(
        onRefresh: _onRefresh,
        child: ListView.builder(
          itemBuilder: _renderRow,
          itemCount: list.length,
        ),
      ),
    );
  &#125;

  Widget _renderRow(BuildContext context, <span class="hljs-built_in">int</span> index) &#123;
    <span class="hljs-keyword">return</span> ListTile(
      title: Text(list[index]),
    );
  &#125;

  <span class="hljs-comment"><span class="markdown"><span class="hljs-strong">/**</span>
<span class="hljs-bullet">   *</span> 下拉刷新方法,为list重新赋值
   <span class="hljs-emphasis">*/</span></span></span>
  Future<<span class="hljs-built_in">Null</span>> _onRefresh() <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">await</span> Future.delayed(<span class="hljs-built_in">Duration</span>(seconds: <span class="hljs-number">3</span>), () &#123;
      <span class="hljs-built_in">print</span>(<span class="hljs-string">'refresh'</span>);
      setState(() &#123;
        list = <span class="hljs-built_in">List</span>.generate(<span class="hljs-number">20</span>, (i) => <span class="hljs-string">'哈喽,我是新刷新的 <span class="hljs-subst">$i</span>'</span>);
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码不复杂,我们一步步分析:
MyHomePage 只是返回一个State,这里省略了.
首先body里我们返回了一个RefreshIndicator,这个组件自带下拉回调,然后里面我们包裹了一个listview,
然后使用List.generate（）方法来创建了一个长度为15的List，并把List里的值赋值给ListView Item中的ListTile。
下拉回调onRefresh 我们返回了一个改变list的方法 .
在上面的代码中我们使用_onRefresh()方法来处理下拉刷新的回调</p>
<pre><code class="copyable">/**
   * 下拉刷新方法,为list重新赋值
   */
  Future<Null> _onRefresh() async &#123;
    await Future.delayed(Duration(seconds: 3), () &#123;
      print('refresh');
      setState(() &#123;
        list = List.generate(20, (i) => '哈喽,我是新刷新的 $i');
      &#125;);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 Future.delayed（）方法可以选择延迟处理任务，这里我们假设网络的延迟是3秒.
这样一个简单的下拉刷新就实现了.</p>
<h1 data-id="heading-2">上拉加载更多</h1>
<p>对于加载更多的组件在Flutter中是没有提供的，所以在这里我们就需要考虑如何实现的。</p>
<p>在ListView中有一个ScrollController属性，它就是专门来控制ListView滑动事件，在这里我们可以根据ListView的位置来判断是否滑动到了底部来做加载更多的处理。</p>
<p>在这里我们可以使用如下代码来判断ListView 是否滑动到了底部</p>
<pre><code class="copyable">  @override
  void initState() &#123;
    // TODO: implement initState
    super.initState();
    getData();
    _scrollController.addListener(() &#123;
      if (_scrollController.position.pixels ==
          _scrollController.position.maxScrollExtent) &#123;
        print('滑动到了最底部');
        _getMore();
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_scrollController是我们初始化的ScrollController对象，通过监听我们可以判断现在的位置是否是最大的下滑位置来判断是否下滑到了底部。</p>
<p>看一下代码和效果:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f589f331726c4a2a9f429e25fd314378~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">class _MyHomePageState extends State<MyHomePage> &#123;
  List list = new List(); //列表要展示的数据
  ScrollController _scrollController = ScrollController(); //listview的控制器
  int _page = 1; //加载的页数
  bool isLoading = false; //是否正在加载数据

  @override
  void initState() &#123;
    // TODO: implement initState
    super.initState();
    getData();
    _scrollController.addListener(() &#123;
      if (_scrollController.position.pixels ==
          _scrollController.position.maxScrollExtent) &#123;
        print('滑动到了最底部');
        _getMore();
      &#125;
    &#125;);
  &#125;

  /**
   * 初始化list数据 加延时模仿网络请求
   */
  Future getData() async &#123;
    await Future.delayed(Duration(seconds: 2), () &#123;
      setState(() &#123;
        list = List.generate(15, (i) => '哈喽,我是原始数据 $i');
      &#125;);
    &#125;);
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return new Scaffold(
      appBar: new AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: new Text(widget.title),
      ),
      body: RefreshIndicator(
        onRefresh: _onRefresh,
        child: ListView.builder(
          itemBuilder: _renderRow,
          itemCount: list.length,
          controller: _scrollController,
        ),
      ),
      // This trailing comma makes auto-formatting nicer for build methods.
    );
  &#125;

  Widget _renderRow(BuildContext context, int index) &#123;
    return ListTile(
      title: Text(list[index]),
    );
  &#125;

  /**
   * 下拉刷新方法,为list重新赋值
   */
  Future<Null> _onRefresh() async &#123;
    await Future.delayed(Duration(seconds: 3), () &#123;
      print('refresh');
      setState(() &#123;
        list = List.generate(20, (i) => '哈喽,我是新刷新的 $i');
      &#125;);
    &#125;);
  &#125;

  /**
   * 上拉加载更多
   */
  Future _getMore() async &#123;
    if (!isLoading) &#123;
      setState(() &#123;
        isLoading = true;
      &#125;);
      await Future.delayed(Duration(seconds: 1), () &#123;
        print('加载更多');
        setState(() &#123;
          list.addAll(List.generate(5, (i) => '第$_page次上拉来的数据'));
          _page++;
          isLoading = false;
        &#125;);
      &#125;);
    &#125;
  &#125;

  @override
  void dispose() &#123;
    // TODO: implement dispose
    super.dispose();
    _scrollController.dispose();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滑动到底部的时候,我们执行加载更多的方法,给list数据多加5条,这次我们把延迟改到了1秒:</p>
<pre><code class="copyable">/**
   * 上拉加载更多
   */
  Future _getMore() async &#123;
    if (!isLoading) &#123;
      setState(() &#123;
        isLoading = true;
      &#125;);
      await Future.delayed(Duration(seconds: 1), () &#123;
        print('加载更多');
        setState(() &#123;
          list.addAll(List.generate(5, (i) => '第$_page次上拉来的数据'));
          _page++;
          isLoading = false;
        &#125;);
      &#125;);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，看着上面的效果我们已经实现了下拉加载更多，但是因为我们是滑动到底部触发的,如果在正在请求的过程中多次下拉就会造成多次加载更多的情况，所以我们还得对这个做下处理为了避免多次触发,我们加了一个isLoading,在上拉方法执行的过程中不会再次执行.
可以看到，我们仅仅在上面代码的基础上加上了一个isLoading的变量，当这个变量的值为true时，就不会触发加载更多的操作。</p>
<p>而因为是网络请求,可能需要分页,所以我们加了个page参数来查看是第几次触发上拉加载.</p>
<p>因为我们加了个监听,在组件卸载掉的时候记得移除这个监听,所以:</p>
<pre><code class="copyable">  @override
  void dispose() &#123;
    // TODO: implement dispose
    super.dispose();
    _scrollController.dispose();
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个一定不要忘记,养成好习惯,每次加了监听都跑到这个方法里移除掉.</p>
<p>这样,我们一个简单的上拉加载更多的功能就实现了.
但是还有个问题,没有用户交互啊,加载的时候要有个提示,于是我们尝试上拉的时候展示一个加载中的组件给用户:
首先我们创建加载更多时显示的Vidget</p>
<pre><code class="copyable">/**
   * 加载更多时显示的组件,给用户提示
   */
  Widget _getMoreWidget() &#123;
    return Center(
      child: Padding(
        padding: EdgeInsets.all(10.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Text(
              '加载中...     ',
              style: TextStyle(fontSize: 16.0),
            ),
            CircularProgressIndicator(strokeWidth: 1.0,)
          ],
        ),
      ),
    );
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在listview的itemcount那里把count+1,相当于我们给listview加了个尾部的组件.</p>
<pre><code class="copyable"> body: RefreshIndicator(
        onRefresh: _onRefresh,
        child: ListView.builder(
          itemBuilder: _renderRow,
          itemCount: list.length + 1,   //这里!这里!这里!
          controller: _scrollController,
        ),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下效果是否满意:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c26a5db7a4d4c1b9b0203ff72f81755~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="这里写图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>嗯,基本符合要求,感觉那个刷新图标加的有点丑,画蛇添足了,不过功能都是ok了的.
当然， 大家可以根据自己的需要去自己实现想要的样式
看一下全部的代码:</p>
<pre><code class="copyable">/*
 * Created by 李卓原 on 2018/9/13.
 * email: zhuoyuan93@gmail.com
 *
 */
 
class MyHomePage extends StatefulWidget &#123;
  MyHomePage(&#123;Key key, this.title&#125;) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => new _MyHomePageState();
&#125;

class _MyHomePageState extends State<MyHomePage> &#123;
  List list = new List(); //列表要展示的数据
  ScrollController _scrollController = ScrollController(); //listview的控制器
  int _page = 1; //加载的页数
  bool isLoading = false; //是否正在加载数据

  @override
  void initState() &#123;
    // TODO: implement initState
    super.initState();
    getData();
    _scrollController.addListener(() &#123;
      if (_scrollController.position.pixels ==
          _scrollController.position.maxScrollExtent) &#123;
        print('滑动到了最底部');
        _getMore();
      &#125;
    &#125;);
  &#125;

  /**
   * 初始化list数据 加延时模仿网络请求
   */
  Future getData() async &#123;
    await Future.delayed(Duration(seconds: 2), () &#123;
      setState(() &#123;
        list = List.generate(15, (i) => '哈喽,我是原始数据 $i');
      &#125;);
    &#125;);
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return new Scaffold(
      appBar: new AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: new Text(widget.title),
      ),
      body: RefreshIndicator(
        onRefresh: _onRefresh,
        child: ListView.builder(
          itemBuilder: _renderRow,
          itemCount: list.length + 1,
          controller: _scrollController,
        ),
      ),
      // This trailing comma makes auto-formatting nicer for build methods.
    );
  &#125;

  Widget _renderRow(BuildContext context, int index) &#123;
    if (index < list.length) &#123;
      return ListTile(
        title: Text(list[index]),
      );
    &#125;
    return _getMoreWidget();
  &#125;

  /**
   * 下拉刷新方法,为list重新赋值
   */
  Future<Null> _onRefresh() async &#123;
    await Future.delayed(Duration(seconds: 3), () &#123;
      print('refresh');
      setState(() &#123;
        list = List.generate(20, (i) => '哈喽,我是新刷新的 $i');
      &#125;);
    &#125;);
  &#125;

  /**
   * 上拉加载更多
   */
  Future _getMore() async &#123;
    if (!isLoading) &#123;
      setState(() &#123;
        isLoading = true;
      &#125;);
      await Future.delayed(Duration(seconds: 1), () &#123;
        print('加载更多');
        setState(() &#123;
          list.addAll(List.generate(5, (i) => '第$_page次上拉来的数据'));
          _page++;
          isLoading = false;
        &#125;);
      &#125;);
    &#125;
  &#125;

  /**
   * 加载更多时显示的组件,给用户提示
   */
  Widget _getMoreWidget() &#123;
    return Center(
      child: Padding(
        padding: EdgeInsets.all(10.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Text(
              '加载中...',
              style: TextStyle(fontSize: 16.0),
            ),
            CircularProgressIndicator(
              strokeWidth: 1.0,
            )
          ],
        ),
      ),
    );
  &#125;

  @override
  void dispose() &#123;
    // TODO: implement dispose
    super.dispose();
    _scrollController.dispose();
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结:</h2>
<ul>
<li>
<p>RefreshIndicator可以显示下拉刷新</p>
</li>
<li>
<p>使用ScrollController可以监听滑动事件，判断当前view所处的位置</p>
</li>
<li>
<p>可以根据item所处的位置来处理加载更多显示效果</p>
</li>
</ul></div>  
</div>
            