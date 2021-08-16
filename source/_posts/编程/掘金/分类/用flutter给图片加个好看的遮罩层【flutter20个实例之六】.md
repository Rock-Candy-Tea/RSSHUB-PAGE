
---
title: '用flutter给图片加个好看的遮罩层【flutter20个实例之六】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff77689d13324ec7996aadcf0b4e29b7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 19:20:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff77689d13324ec7996aadcf0b4e29b7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、老套路，先看样式</h2>
<p>图一是我业务中的样式，图二、三是下方源码展示样式（复制可直接运行，无额外组件引入）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff77689d13324ec7996aadcf0b4e29b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40d22748626748cc8709f42d9c2ce0fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/356ec66dd3b44aaf8519efb19dd159ae~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">二、讲解</h2>
<h3 data-id="heading-2">1.结构拆分</h3>
<p>我们先看下页面布局结构，首先肯定是有个GridView滚动组件来容纳内容</p>
<p>其次顶部有个日期的选择，点击后底部弹出下拉选择，可以选择不同年份</p>
<p>年份选择后，进行内容刷新，数据重新加载</p>
<p>每个图片底部有个一定高度的遮罩层，用来放一些文字</p>
<h3 data-id="heading-3">2.看看这个布局的主内容</h3>
<p>body里面的列表内容</p>
<p>右上角点击后调用了bottomModal组件</p>
<pre><code class="copyable">  @override
  Widget build(BuildContext context) &#123;
    return Scaffold(
        appBar: AppBar(
          title: Text('备忘录' + _dropValue),
          centerTitle: true,
          elevation: 0.0,
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.date_range),
              tooltip: "编辑",
              onPressed: () &#123;
                return bottomModal();
              &#125;,
            ),
          ],
        ), //这个是顶部tab样式，如果不需要可以去掉
        body: monthList());
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.底部弹框其实就是个showModalBottomSheet组件</h3>
<p>isDismissible：false //点击空白区域不可关闭</p>
<p>row：底部的三个样式进行mainAxisAlignment: MainAxisAlignment.spaceBetween的布局排列</p>
<p>InkWell：为每个图标增加个点击事件</p>
<p>由于底部弹框也相当于一个页面，所以想要里面的select选择后内容跟着变动，就需要重定义setState()</p>
<h3 data-id="heading-5">4.核心内容列表就是一个GridView</h3>
<p>一行显示4个</p>
<pre><code class="copyable">crossAxisCount: 4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>左右间距</p>
<pre><code class="copyable">crossAxisSpacing: 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上下间距</p>
<pre><code class="copyable">mainAxisSpacing: 10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>宽高比</p>
<pre><code class="copyable">childAspectRatio: 0.6

    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: SafeArea(
        child: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 4,
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              childAspectRatio: 0.6),
          itemBuilder: (context, index) &#123;
            return _itemGrid(index);
          &#125;,
          itemCount: _list.length,
        ),
      ),
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">5.主要是遮罩层的讲解</h3>
<p>这里是一个stack，通过两个组件的堆叠实现，外层要设一个颜色透明度</p>
<p>属性要设置自动撑满，这样组件的遮罩层才会自动撑满父组件宽度</p>
<pre><code class="copyable">fit: StackFit.expand
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后要设置一个颜色透明度</p>
<pre><code class="copyable">decoration: BoxDecoration(color: Color(0x72000000)),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是flutter的所有颜色透明</p>
<p>比如完全不透明：0xFF000000 需要将第3第4两个字母，替换为下方列表的右侧两个字符即可</p>
<pre><code class="copyable">00%=FF（不透明） 
5%=F2 
10%=E5 
15%=D8 
20%=CC 
25%=BF 
30%=B2 
35%=A5 
40%=99 
45%=8c 
50%=7F 
55%=72 
60%=66 
65%=59 
70%=4c 
75%=3F 
80%=33 
85%=21 
90%=19 
95%=0c 
100%=00（全透明）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">三、源码（可直接运行调试）</h2>
<pre><code class="copyable">import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Mytest extends StatefulWidget &#123;
  @override
  _MytestState createState() => _MytestState();
&#125;

class _MytestState extends State<Mytest> &#123;
  var _dropValue = '2020';
  List _list = [
    &#123;
      'id': '1',
      'num': '0',
      'cover':
          'https://daybili.oss-cn-beijing.aliyuncs.com/image/202008/1m.jpg',
      'name': '1月'
    &#125;
  ];

  @override
  Widget build(BuildContext context) &#123;
    return Scaffold(
        appBar: AppBar(
          title: Text('备忘录' + _dropValue),
          centerTitle: true,
          elevation: 0.0,
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.date_range),
              tooltip: "编辑",
              onPressed: () &#123;
                return bottomModal();
              &#125;,
            ),
          ],
        ), //这个是顶部tab样式，如果不需要可以去掉
        body: monthList());
  &#125;

  //核心的内容列表数据
  Widget monthList() &#123;
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: SafeArea(
        child: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 4,
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              childAspectRatio: 0.6),
          itemBuilder: (context, index) &#123;
            return _itemGrid(index);
          &#125;,
          itemCount: _list.length,
        ),
      ),
    );
  &#125;

  Widget _itemGrid(index) &#123;
    return InkWell(
      child: Container(
        color: Colors.black,
        height: 120,
        padding: EdgeInsets.all(0),
        child: Stack(
          fit: StackFit.expand,
          children: <Widget>[
            Container(
              height: 150,
              child: Image.network(
                _list[index]['cover'],
                fit: BoxFit.fill,
              ),
            ),
            Align(
              alignment: Alignment.bottomCenter,
              child: Container(
                width: double.infinity,
                child: RichText(
                  text: TextSpan(
                      style: DefaultTextStyle.of(context).style,
                      children: <InlineSpan>[
                        TextSpan(
                          text: _list[index]['name'],
                          style: TextStyle(
                              fontSize: 11,
                              decoration: TextDecoration.none,
                              color: Colors.white),
                        ),
                        TextSpan(
                          text: _list[index]['num'] + '条',
                          style: TextStyle(
                              color: Colors.red,
                              fontSize: 13,
                              decoration: TextDecoration.none),
                        ),
                        TextSpan(
                          text: '提醒',
                          style: TextStyle(
                              fontSize: 11,
                              color: Colors.white,
                              decoration: TextDecoration.none),
                        ),
                      ]),
                ),
                decoration: BoxDecoration(color: Color(0x72000000)),
              ),
            ),
          ],
        ),
      ),
    );
  &#125;

  //底部日期选择框
  Widget bottomModal() &#123;
    showModalBottomSheet(
        isDismissible: false,
        context: context,
        builder: (BuildContext context) &#123;
          return StatefulBuilder(builder: (context1, state) &#123;
            ///这里的state就是setState
            return Container(
              height: 60,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: <Widget>[
                  InkWell(
                      onTap: () &#123;
                        Navigator.of(context).pop();
                      &#125;,
                      child: Padding(
                        padding: const EdgeInsets.only(left: 10),
                        child: Icon(Icons.close),
                      )),
                  selectYear(context1, state),
                  InkWell(
                      onTap: () &#123;
                        Navigator.of(context).pop();
                      &#125;,
                      child: Padding(
                        padding: const EdgeInsets.only(right: 10),
                        child: Icon(Icons.done),
                      ))
                ],
              ),
            );
          &#125;);
        &#125;);
  &#125;

  Widget selectYear(context1, state) &#123;
    return DropdownButtonHideUnderline(
      child: DropdownButton(
        iconSize: 20.0, //设置三角标icon的大小
        value: _dropValue,
        items: [
          DropdownMenuItem(
            child: Text('2020年'),
            value: '2020',
          ),
          DropdownMenuItem(child: Text('2021年'), value: '2021'),
          DropdownMenuItem(child: Text('2022年'), value: '2022'),
        ],
        onChanged: (value) &#123;
          state(() &#123;
            _dropValue = value;
          &#125;);
          setState(() &#123;
            _dropValue = value;
          &#125;);
        &#125;,
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            