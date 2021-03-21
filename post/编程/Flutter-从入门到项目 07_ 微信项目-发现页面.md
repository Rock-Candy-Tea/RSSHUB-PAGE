
---
title: Flutter-从入门到项目 07_ 微信项目-发现页面
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Sun, 21 Feb 2021 21:08:14 GMT
thumbnail: https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc810c1365e645c6b0d2f50bfd67e6d1~tplv-k3u1fbpfcp-zoom-1.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><blockquote>
<p><a href="https://juejin.cn/post/6931666501799968782" target="_blank">Flutter 专题目录汇总: </a> 这个目录方便大家快速查询你要学习的内容!!!</p>
</blockquote>
<h3 data-id="heading-0">二: 微信项目发现页面</h3>
<p>这个页面涉及到的可能前面没有讲解 就是关于布局. 在Flutter的世界里更多的是弹性盒子布局</p>
<blockquote>
<p>弹性布局允许子组件按照一定比例来分配父容器空间。弹性布局的概念在其它 <code>UI系统</code> 中也都存在，如<code>H5</code> 中的弹性盒子布局，<code>Android</code> 中的 <code>FlexboxLayout</code> 等。<code>Flutter</code> 中的弹性布局主要通过<code>Flex</code> 和 <code>Expanded</code> 来配合实现。</p>
</blockquote>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc810c1365e645c6b0d2f50bfd67e6d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果大家对这个还不是很理解,可以参考一下 : <a href="https://www.jianshu.com/p/9e69acb20ded" target="_blank" rel="nofollow noopener noreferrer"> Flutter之 Flex 布局</a></p>
<h4 data-id="heading-1">① 发现页面实现</h4>
<p>有上面弹性盒子布局的基础 下面我们开始搭建页面吧</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'package:wecaht/pages/discover/kc_discover_cell.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KCDiscoverPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>{
  <span class="hljs-meta">@override</span>
  _KCDiscoverPageState createState() => _KCDiscoverPageState();
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_KCDiscoverPageState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">KCDiscoverPage</span>> </span>{
  Color _themeColor = Color.fromRGBO(<span class="hljs-number">220</span>, <span class="hljs-number">220</span>, <span class="hljs-number">220</span>, <span class="hljs-number">1.0</span>);
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) {
    <span class="hljs-keyword">return</span> Scaffold(
      appBar: AppBar(
        backgroundColor: _themeColor,
        centerTitle: <span class="hljs-keyword">true</span>,
        elevation: <span class="hljs-number">0.0</span>,
        title: Text(<span class="hljs-string">'发现'</span>),
      ),
      body: Container(
        color: _themeColor,
        child: ListView(
          children: <Widget>[
            KCDiscoverCell(
              imageName: <span class="hljs-string">'images/朋友圈.png'</span>,
              title: <span class="hljs-string">'朋友圈'</span>,
            ),
            SizedBox(height: <span class="hljs-number">10</span>,),
            KCDiscoverCell(
              imageName: <span class="hljs-string">'images/扫一扫.png'</span>,
              title: <span class="hljs-string">'扫一扫'</span>,
            ),
        .....  这里省略一下没有必要的代码, 如果大家想查看详细代码可以移步github: 
        github项目地址 : https:<span class="hljs-comment">//github.com/LGCooci/KCFlutter</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>把这一排的 <code>cell</code> 抽取出来了 <code>KCDiscoverCell </code></li>
<li>状态管理设置 <code>_themeColor </code></li>
<li>整个页面采用 <code>ListView</code> 显示</li>
</ul>
<h4 data-id="heading-2">② 发现页面抽取<code>KCDiscoverCell </code></h4>
<p>这种抽取共用 <code>Cell</code>的方式,想必你已不再迷茫,无论 <code>iOS</code>还是 <code>Android</code> 用的太多了!</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">KCDiscoverCell</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>{
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> title;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> subTitle;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> imageName;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> subImageName;

  KCDiscoverCell({
    <span class="hljs-keyword">this</span>.title,
    <span class="hljs-keyword">this</span>.subTitle,
    <span class="hljs-keyword">this</span>.imageName,
    <span class="hljs-keyword">this</span>.subImageName
  });

  <span class="hljs-meta">@override</span>
  _KCDiscoverCellState createState() => _KCDiscoverCellState();
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_KCDiscoverCellState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">KCDiscoverCell</span>> </span>{

  Color _currentColor = Colors.white;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) {
    <span class="hljs-keyword">return</span> GestureDetector(
      onTap: (){
        Navigator.of(context).push(
            MaterialPageRoute(builder: (BuildContext context) =>
                KCDiscoverChildPage(tittle: widget.title,)));
        setState(() {
          _currentColor = Colors.white;
        });
      },

      onTapDown: (TapDownDetails details){ },

      onTapCancel: (){},

      child: Container(
        color: _currentColor,
        height: <span class="hljs-number">54</span>,
        child: Row(
          <span class="hljs-comment">// 两端排列</span>
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            <span class="hljs-comment">//left</span>
            Container()
            <span class="hljs-comment">// right</span>
            Container()
      ]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>公共方法点击进入子页面 <code>KCDiscoverChildPage </code></li>
<li><code>GestureDetector</code> 给我们的 <code>Cell</code> 添加用户交互能力</li>
<li><code>onTapCancel</code> 、<code>onTapDown </code>、<code>onTap</code> 通过这几个手势设置用户点击效果</li>
<li><code>setState</code> 还是我们非常熟悉的状态管理</li>
<li><code> Navigator.of(context).push</code> 界面跳转</li>
</ul>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e2dced0a13447b28ee4b44574751b3b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>详情代码移步 <a href="https://github.com/LGCooci/KCFlutter" target="_blank" rel="nofollow noopener noreferrer">Github 项目地址</a> 欢迎大家点赞心心 谢谢</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            