
---
title: 'flutter中ListView做一个掘金列表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0536166c20c4f0e951843ad73d0839a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 16:06:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0536166c20c4f0e951843ad73d0839a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h4 data-id="heading-0">1.ListView的简单介绍</h4>
<pre><code class="copyable">ListView是最常用的可以滚动组件之一，
它可以沿一个方向进行线性排列所有的子组件。
我们可以把它理解成横向和纵向滚动的组件
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2.ListView的属性值</h4>
<pre><code class="copyable">scrollDirection:列表的滚动方向，
可选值有Axis的horizontal和vertical，
默认是垂直方向上滚动。

controller:控制器，与列表滚动相关，比如监听列表的滚动事件。

physics: 列表滚动至边缘后继续拖动的物理效果，
Android与iOS效果不同。
Android会呈现出一个波纹状（对应ClampingScrollPhysics），
而iOS上有一个回弹的弹性效果（对应BouncingScrollPhysics）。
如果你想不同的平台上呈现各自的效果可以使用AlwaysScrollableScrollPhysics，
它会根据不同平台自动选用各自的物理效果。如果你想禁用在边缘的拖动效果，
那可以使用NeverScrollableScrollPhysics；

shrinkWrap: 该属性将决定列表的长度是否仅包裹其内容的长度。
当ListView嵌在一个无限长的容器组件中时，
shrinkWrap必须为true，否则Flutter会给出警告；

padding: 列表内边距；

itemExtent: 子元素长度。
当列表中的每一项长度是固定的情况下可以指定该值，
有助于提高列表的性能
（因为它可以帮助ListView在未实际渲染子元素之前就计算出每一项元素的位置）；

children: 容纳子元素的组件数组。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3.ListTile 属性简介</h4>
<pre><code class="copyable">this.leading,              // 内容的==>前置图标
this.title,                // 内容的==>标题
this.subtitle,             // 内容的==>副标题
this.trailing,             // 内容的==>后置图标
this.isThreeLine = false,  // 内容的==>是否三行显示
this.dense,                // 内容的==>直观感受是整体大小
this.contentPadding,       // 内容的==>内容内边距
this.enabled = true,       // 内容 是否禁用
this.onTap,                // item onTap 点击事件
this.onLongPress,          // item onLongPress 长按事件
this.selected = false,     // item 是否选中状态
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4.ListView的基本使用</h4>
<pre><code class="copyable">我们做一个新闻列表；
结构非常的简单：有主标题和副标题
title(主标题)和subtitle(subtitle)
我们一起来看看长成什么样子。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: <Widget>[
      ListTile(
        // 主标题
        title: Text('Flutter 由 Google 的工程师团队打造，用于创建高性能、跨平台的移动应用',
            //文字左对齐
            textAlign: TextAlign.left, 
            //超出显示省略号
            overflow: TextOverflow.ellipsis, 
            style: TextStyle(
              //数字必须是Double类型的
              fontSize: 20.0, 
              //  设置字体的颜色
              color: Color.fromARGB(200, 100, 100, 8)
            )
        ),
        // 副标题
        subtitle: Text('你好flutter'),
      ),
      ListTile(
        title: Text('Flutter 由 Google 的工程师团队打造，用于创建高性能、跨平台的移动应用'),
        subtitle: Text('你好flutter'),
      ),
    ]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0536166c20c4f0e951843ad73d0839a~tplv-k3u1fbpfcp-watermark.image" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">5.listView列表设置前置图标</h4>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: <Widget>[
      ListTile(
        // 主标题
        // 在前面设置图标
        leading: Icon(
          //设置图标类型
          Icons.settings, 
          //0x后面开始 两位FF表示透明度16进制，
          color: Color(0xFFFFB6C1), 
          //这是图标的大小
          size: 30.0
        ),
        // 在后面设置图标
        // trailing: Icon(Icons.accessible),
        title: Text('flutter教程_2021 Dart Flutter入门实战视频教程132讲',
          //文字左对齐
          textAlign: TextAlign.left, 
          //超出显示省略号
          overflow: TextOverflow.ellipsis, 
          style: TextStyle(
            fontSize: 20.0, //数字必须是Double类型的
            //  设置字体的颜色
            color: Color(0xFFFFB6C1)
          )
        ),
        subtitle: Text('不管是Ios还是Android开发都可以在flutter官网上查到安装及使用步骤，这里我就不累述太多'),
      ),
    ]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f28949f0e1e4d6882c64994f1136c80~tplv-k3u1fbpfcp-watermark.image" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">6.设置前置图片</h4>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: <Widget>[
      ListTile(
        // 主标题
        // 通过leading可以将图片放在前面
        leading: Image.network(
          "https://giidu.c/ster/src=http%3A%2F%2Ft14.npg"),
          title: Text(
            'flutter教程_2021 Dart Flutter入门实战视频教程132讲',
            textAlign: TextAlign.left, //文字左对齐
            overflow: TextOverflow.ellipsis, //超出显示省略号
            style: TextStyle(
              fontSize: 20.0, //数字必须是Double类型的
              //  设置字体的颜色
              color: Color(0xFFFFB6C1)
            )
          ),
        subtitle: Text('不管是Ios还是Android开发都可以在flutter官网上查到安装及使用步骤，这里我就不累述太多'),
      ),
    ]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca58301c4c1349378f803a8467926bf9~tplv-k3u1fbpfcp-watermark.image" alt="03.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">7.垂直列表</h4>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: <Widget>[
      Container(
        width: 750.0,
        height: 200.0,
        color:Color(0xFFFFB6C1),
        // 外边距 左上右下，跟css不一样哈
        margin: EdgeInsets.fromLTRB(10, 10, 10, 0),
      ),
      Container(
        width: 750.0,
        height: 200.0,
        color: Color(0xFFFFB6C1),
        // 外边距 左上右下，跟css不一样哈
        margin: EdgeInsets.fromLTRB(10, 10, 10, 0),
      )
    ]);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cefa2d472125473e93cdc3e78528a298~tplv-k3u1fbpfcp-watermark.image" alt="04.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">8.水平排列</h4>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return Container(
      height: 200.0,
      child:new ListView(
        // 水平排列 
        scrollDirection: Axis.horizontal, children: <Widget>[
          Container(
            width: 220.0,
            height: 200.0,
            color: Color(0xFFFFB6C1),
            // 外边距 左上右下，跟css不一样哈
            margin: EdgeInsets.fromLTRB(10, 10, 10, 0),
          ),
          Container(
            width: 220.0,
            height: 200.0,
            color: Color(0xFFFFB6C1),
            // 外边距 左上右下，跟css不一样哈
            margin: EdgeInsets.fromLTRB(10, 10, 10, 0),
          ),
          Container(
            width: 220.0,
            height: 200.0,
            color: Color(0xFFFFB6C1),
            // 外边距 左上右下，跟css不一样哈
            margin: EdgeInsets.fromLTRB(10, 10, 10, 0),
          ),
        ]
      )
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/077f97d6da444eb5b528db8801d83a72~tplv-k3u1fbpfcp-watermark.image" alt="05.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">9.动态列表</h4>
<pre><code class="copyable">在项目的实际开发过程中；
我们会有很多的列表；
我们想将ListView中children中的代码封装成为一个函数。
方便后期的管理
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class MyApp extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return MaterialApp(
      home: Scaffold(appBar: AppBar(title: Text('首页')), body: MyCont()),
      //设置顶部的颜色
      theme: ThemeData(primarySwatch: Colors.yellow),
    );
  &#125;
&#125;

class MyCont extends StatelessWidget &#123;
  // Lis里面的数据必须是Widget组件；
  // _backDataList方法下划线开头，表示当前这个类私有的。
  List<Widget> _backDataList() &#123;
    return [
      ListTile(
        title: Text('我是新闻标题1'),
      ),
      ListTile(
        title: Text('我是新闻标题2'),
      ),
      ListTile(
        title: Text('我是新闻标题3'),
      ),
      ListTile(
        title: Text('我是新闻标题4'),
      )
    ];
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: this._backDataList());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/793976c62b9b4333b46bb860cb8a20b2~tplv-k3u1fbpfcp-watermark.image" alt="06.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">10.往数组中添加数据进行循环</h4>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  // Lis里面的数据必须是Widget组件；
  // _backDataList方法下划线开头，表示当前这个类私有的。
  List<Widget>_backDataList() &#123;
    // 声明了一个数组，里面的数据类型是Widget
    List<Widget> list = []; 
    for (var i = 0; i < 10; i++) &#123;
      list.add(ListTile(
        title: Text('我是新闻标题$i'),
      ));
    &#125;
    return list;
  &#125;
  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: this._backDataList());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">11.为什么要使用ListView.builder</h4>
<pre><code class="copyable">ListView.builder下的两个属性值
itemCount：指定被循环数组的长度
itemBuilder:它有2个参数。
itemBuilder(contText, index) &#123;
    contText表示的循环的内容
    index表示循环的索引值
&#125;

如果itemBuilder下是一个封装的函数，
不要添加括号，因为括号表示调用；
直接itemBuilder:this.youFunc就可以了

使用ListView.builder的优势：
ListView.builder适合列表项比较多（或者无限）的情况，
只有当子组件真正显示的时候列表才会被创建，
也就说通过该构造函数创建的ListView是支持基于Sliver的懒加载模型的。
也就是说使用ListView.builder可以提升性能。
下面我们将会使用ListView.builder来创建一个列表
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">在lib目录下创建一个res
在res目录下创建demo.dart
demo.dart文件下有数据的哈
import 'res/demo.dart';
List listData = [
  &#123;
    'title': 'Python 创作季，秀出你的 Python 文章
  &#125;
]
后面使用listData就可以直接获取数据了哈

class MyCont extends StatelessWidget &#123;
  @override
  Widget build(BuildContext context) &#123;
    return ListView.builder(
      // itemCount:指定该数组的长度
      itemCount: listData.length,
      //itemBuilder 会进行循环遍历
      itemBuilder: (contText, index) &#123;
        return ListTile(
          title: Text(listData[index]['title']),
          //还有很多的属性xxxx........
        );
      &#125;,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">前面我们说了，使用ListView.builder可以提高性能；
但是我们发现了itemBuilder下如果有很多属性的话；
那么就会变得非常的臃肿的；
后期是不利于我们维护；
那么我们能不能将 itemBuilder中的抽离出去了？
经过我的查询文档发现是可以的
请看下面：
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">12.将itemBuilder中的属性抽离出去</h4>
<pre><code class="copyable">我们可以将原来itemBuilder下的代码
封装成为一个方法放置在自定义的_getListData下；
方便我们后期的维护以及修改
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">class MyCont extends StatelessWidget &#123;
  //自定义的方法
  Widget _getListData(contText, index)&#123;
    return ListTile(
      title: Text(listData[index]['title']),
    );
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return ListView.builder(
      // itemCount:指定该数组的长度
      itemCount: listData.length,
      //this._getListData是不需要加括号的；
      // 我们这里表示的复制该方法
      // this._getListData()表示的是直接去调用这个方法
      itemBuilder:this._getListData
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">13.ListView children与ListView.builder的区别</h4>
<pre><code class="copyable">通过前面的例子，
我们可以发现ListView有默认构造函数。
ListView默认构造函数有一个children参数，
children接受一个Widget列表[List],

通过children参数的形式接受的子组件列表。
这种方式需要将所有的children都提前创建好；
因此需要提前做大量的工作；
所以:这种形式只适合少量的子组件的情况

ListView.builder
ListView.builder适合列表项比较多（或者无限）的情况，
只有当子组件真正显示的时候列表才会被创建，
也就说通过该构造函数创建的ListView是支持基于Sliver的懒加载模型的。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">14.制作一个掘金列表</h4>
<pre><code class="copyable">我们将使用后置图标trailing这个属性来完成图片后置。
同时我们将给一个容器组件Container；
容器组件的宽高来限制图片的大小；
我们将会对图片进行裁剪，
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">在lib目录下创建一个res
在res目录下创建demo.dart
demo.dart文件下有数据的哈
import 'res/demo.dart';
List listData = [
  &#123;
    'title': 'Python 创作季，秀出你的 Python 文章
  &#125;
]

class MyCont extends StatelessWidget &#123;
  // Lis里面的数据必须是Widget组件；
  // _backDataList方法下划线开头，表示当前这个类私有的。
  List<Widget> _backDataList() &#123;
    var temtepleList = listData.map((value) &#123;
      return ListTile(
          title: Text(
            value['title'],
            // 超出显示省略号
            overflow: TextOverflow.ellipsis,
            style: TextStyle(fontSize: 16.0, color: Color(0xFF86909c)),
          ),
          subtitle: Text(
            value['cont'],
            overflow: TextOverflow.ellipsis,
            style: TextStyle(fontSize: 13.0, color: Color(0xFF86909c)),
          ),
          trailing: Container(
              width: 90.0, //容器宽
              height: 70.0, //容器高
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(4.0),
                image: DecorationImage(
                  image: NetworkImage(
                    value['img'],
                  ),
                  alignment: Alignment.topLeft, //左上角居中
                  fit: BoxFit.cover, //裁剪，充满整个容器。不会变形
                ) 
              )
          )
      );
    &#125;);
    // 转化成为一个数组
    return temtepleList.toList();
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return ListView(children: this._backDataList());
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c5d8cd6ce6440cc9dc3ccd9bdc51a0a~tplv-k3u1fbpfcp-watermark.image" alt="07.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            