
---
title: 'Flutter ModalBottomSheet 指导'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://ducafecat.tech/2021/05/18/translation/flutter-modalbottomsheet-for-beginners/2021-05-18-09-22-09.png'
author: 掘金
comments: false
date: Mon, 17 May 2021 17:40:08 GMT
thumbnail: 'https://ducafecat.tech/2021/05/18/translation/flutter-modalbottomsheet-for-beginners/2021-05-18-09-22-09.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://ducafecat.tech/2021/05/18/translation/flutter-modalbottomsheet-for-beginners/2021-05-18-09-22-09.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">老铁记得 转发 ，猫哥会呈现更多 Flutter 好文~~~~</h2>
<h2 data-id="heading-1">微信 flutter 研修群 ducafecat</h2>
<h2 data-id="heading-2">原文</h2>
<blockquote>
<p><a href="https://evandrmb.medium.com/flutter-modalbottomsheet-for-beginners-e5f3af271076" target="_blank" rel="nofollow noopener noreferrer">evandrmb.medium.com/flutter-mod…</a></p>
</blockquote>
<h2 data-id="heading-3">代码</h2>
<p><a href="https://github.com/evandrmb/bottom_sheet" target="_blank" rel="nofollow noopener noreferrer">github.com/evandrmb/bo…</a></p>
<h2 data-id="heading-4">参考</h2>
<ul>
<li><a href="https://material.io/components/sheets-bottom" target="_blank" rel="nofollow noopener noreferrer">material.io/components/…</a></li>
</ul>
<h2 data-id="heading-5">正文</h2>
<p>根据材质设计指南，底部表是一个小工具，用于显示锚定在屏幕底部的附加内容。虽然了解使用这个的设计规则很好，但这不是本文的目标。要了解更多关于底板设计原则的详细信息，请参阅“<a href="https://material.io/components/sheets-bottom" target="_blank" rel="nofollow noopener noreferrer">Sheets: bottom — Material Design</a>”。</p>
<p>现在你知道了 BottomSheet，你可能会问自己: 什么是 ModalBottomSheet？我们如何使用他们在 Flutter？</p>
<p>好的，第一个问题，有两种底层表: 模态的和持久的。当用户与屏幕交互时，持久化保持可见。谷歌地图应用就是一个例子。</p>
<p>另一方面，模式化的操作会阻止用户在应用程序中做其他动作。您可以使用它们来确认某些操作，或者请求额外的数据，比如询问用户在电子商务应用程序中订购时需要多少交换，等等。</p>
<p>在本文中，我们将通过创建一个简单的体重跟踪应用程序来展示如何使用它，在这个应用程序中我们可以提交我们的体重并查看我们之前的体重。我们不会输入应用程序的详细信息，而是直接进入 ModalBottomSheet 实现。</p>
<p>要显示它，您需要从具有 Scaffold 的上下文调用 showModalBottomSheet，否则，您将得到一个错误。也就是说，让我们开始构建我们的表格。</p>
<p>首先要知道的是 ModalBottomSheets 的高度默认为屏幕的一半，为了改变它，必须传递 true 给 isScrollControlled 参数，并返回一个与我们期望的大小相匹配的小部件，所以让我们这样做。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> addWeight() &#123;
    showModalBottomSheet(
      isScrollControlled: <span class="hljs-keyword">true</span>,
      context: context,
      builder: (context) &#123;
        <span class="hljs-keyword">var</span> date = <span class="hljs-built_in">DateTime</span>.now();

    <span class="hljs-keyword">return</span> Container(
          height: <span class="hljs-number">302</span>,
          padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">16.0</span>),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [

            ],
          ),
        );
      &#125;,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们需要添加一些东西，以便我们的用户可以输入他们的权重让我们添加一个 TextInput 并给它一个 TextEditingController (这种方式即使我们的工作表意外关闭时，用户再次打开它，它的值仍然存在)。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> addWeight() &#123;
    showModalBottomSheet(
      isScrollControlled: <span class="hljs-keyword">true</span>,
      context: context,
      builder: (context) &#123;
        <span class="hljs-keyword">var</span> date = <span class="hljs-built_in">DateTime</span>.now();

    <span class="hljs-keyword">return</span> Container(
          height: <span class="hljs-number">302</span>,
          padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">16.0</span>),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
      padding: EdgeInsets.only(bottom: <span class="hljs-number">24.0</span>),
                child: Text(
                  <span class="hljs-string">'Register Weight'</span>,
                  style: Styles.titleStyle,
                ),
              ),
              TextField(
                controller: weightInputController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  labelText: <span class="hljs-string">'Weight (KG)'</span>,
                  border: OutlineInputBorder(
                    borderRadius: Styles.borderRadius,
                  ),
                ),
              ),
            ],
          ),
        );
      &#125;,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看起来不错，但现在我们有麻烦了。当用户点击我们的 TextField 键盘在它上面，为什么？当键盘打开时，我们的工作表不会调整位置，我们可以把工作表做得更大，但这不能解决我们的问题，因为我们仍然需要添加一个字段，用户可以在其中输入他们记录重量的日期。那么解决方案是什么呢？这很简单，如果打开键盘，我们让我们的工作表在它上面，我们可以实现这一点，给我们的容器一个边距的边缘。在 viewinset.bottom 中，我们将得到以下结果:</p>
<p><img src="https://ducafecat.tech/2021/05/18/translation/flutter-modalbottomsheet-for-beginners/2021-05-18-08-58-03.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>它开始看起来很漂亮，但是你不认为如果我们在纸上加一些半径会更平滑吗？让我们通过添加如下所示的 shapeproperty 来实现。</p>
<pre><code class="hljs language-dart copyable" lang="dart">showModalBottomSheet(
      isScrollControlled: <span class="hljs-keyword">true</span>,
      context: context,
      shape: <span class="hljs-keyword">const</span> RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(<span class="hljs-number">8</span>),
            topRight: Radius.circular(<span class="hljs-number">8</span>),
          )),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>酷，现在让我们做我们的小工具来选择一个日期。通常，您会创建一个小部件来处理这个逻辑，并使用 ValueChanged 函数公开选定的值，但是为了说明您将来可能面临的问题，让我们在工作表本身内部创建所有逻辑。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> addWeight() &#123;
    showModalBottomSheet(
      isScrollControlled: <span class="hljs-keyword">true</span>,
      context: context,
      shape: <span class="hljs-keyword">const</span> RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
        topLeft: Radius.circular(<span class="hljs-number">8</span>),
        topRight: Radius.circular(<span class="hljs-number">8</span>),
      )),
      builder: (context) &#123;
        <span class="hljs-keyword">return</span> Container(
          height: <span class="hljs-number">360</span>,
          width: MediaQuery.of(context).size.width,
          margin:
              EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom),
          padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">16.0</span>),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(<span class="hljs-number">20</span>),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              <span class="hljs-keyword">const</span> Padding(
                padding: EdgeInsets.only(bottom: <span class="hljs-number">24.0</span>),
                child: Text(
                  <span class="hljs-string">'Register Weight'</span>,
                  style: Styles.titleStyle,
                ),
              ),
              TextField(
                controller: weightInputController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  labelText: <span class="hljs-string">'Weight (KG)'</span>,
                  border: OutlineInputBorder(
                    borderRadius: Styles.borderRadius,
                  ),
                ),
              ),
              Padding(
                padding: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(vertical: <span class="hljs-number">8.0</span>),
                child: Row(
                  children: [
                    Expanded(
                      child: Text(
                        <span class="hljs-string">'Select a date'</span>,
                        style: TextStyle(
                          fontSize: <span class="hljs-number">14</span>,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                    Container(
                      padding: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(horizontal: <span class="hljs-number">4</span>),
                      margin: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(vertical: <span class="hljs-number">8.0</span>),
                      height: <span class="hljs-number">36</span>,
                      decoration: BoxDecoration(
                        borderRadius: Styles.borderRadius,
                      ),
                      child: OutlinedButton(
                        onPressed: () <span class="hljs-keyword">async</span> &#123;
                          <span class="hljs-keyword">final</span> now = <span class="hljs-built_in">DateTime</span>.now();

                          <span class="hljs-keyword">final</span> result = <span class="hljs-keyword">await</span> showDatePicker(
                              context: context,
                              initialDate: now,
                              firstDate: now.subtract(
                                <span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(
                                  days: <span class="hljs-number">90</span>,
                                ),
                              ),
                              lastDate: now);

                          <span class="hljs-keyword">if</span> (result != <span class="hljs-keyword">null</span>) &#123;
                            setState(() &#123;
                              selectedDate = result;
                            &#125;);
                          &#125;
                        &#125;,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Padding(
                              padding: <span class="hljs-keyword">const</span> EdgeInsets.only(right: <span class="hljs-number">16.0</span>),
                              child:
                                  Text(<span class="hljs-string">'<span class="hljs-subst">$&#123;formatDateToString(selectedDate)&#125;</span>'</span>),
                            ),
                            Icon(Icons.calendar_today_outlined),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              )

            ],
          ),
        );
      &#125;,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，我已经在我们的主页中添加了 selectedDatevariable，你可以在我最后提供的存储库链接中看到这一点。但是现在我们遇到了一个问题，尽管我们正在使用 setstateoutlinebutton 更新 selectedDate 的值，但是在重新打开工作表之前，仍然会显示旧的值，如下所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ebcde4b7e34aa3b9e2053ca26a267f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了解决这个问题，我们需要将 OutlinedButton 传递给 StatefulBuilder (或者您可以创建一个新的小部件并使用回调公开更改，正如我前面所说的，顺便说一下，这是更正确的方法)。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> addWeight() &#123;
    showModalBottomSheet(
      isScrollControlled: <span class="hljs-keyword">true</span>,
      context: context,
      shape: <span class="hljs-keyword">const</span> RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
        topLeft: Radius.circular(<span class="hljs-number">8</span>),
        topRight: Radius.circular(<span class="hljs-number">8</span>),
      )),
      builder: (context) &#123;
        <span class="hljs-keyword">return</span> Container(
          height: <span class="hljs-number">360</span>,
          width: MediaQuery.of(context).size.width,
          margin:
              EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom),
          padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">16.0</span>),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(<span class="hljs-number">20</span>),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              <span class="hljs-keyword">const</span> Padding(
                padding: EdgeInsets.only(bottom: <span class="hljs-number">24.0</span>),
                child: Text(
                  <span class="hljs-string">'Register Weight'</span>,
                  style: Styles.titleStyle,
                ),
              ),
              TextField(
                controller: weightInputController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  labelText: <span class="hljs-string">'Weight (KG)'</span>,
                  border: OutlineInputBorder(
                    borderRadius: Styles.borderRadius,
                  ),
                ),
              ),
              Padding(
                padding: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(vertical: <span class="hljs-number">8.0</span>),
                child: Row(
                  children: [
                    Expanded(
                      child: Text(
                        <span class="hljs-string">'Select a date'</span>,
                        style: TextStyle(
                          fontSize: <span class="hljs-number">14</span>,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                    Container(
                        padding: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(horizontal: <span class="hljs-number">4</span>),
                        margin: <span class="hljs-keyword">const</span> EdgeInsets.symmetric(vertical: <span class="hljs-number">8.0</span>),
                        height: <span class="hljs-number">36</span>,
                        decoration: BoxDecoration(
                          borderRadius: Styles.borderRadius,
                        ),
                        child: StatefulBuilder(
                          builder: (context, setState) &#123;
                            <span class="hljs-keyword">return</span> OutlinedButton(
                              onPressed: () <span class="hljs-keyword">async</span> &#123;
                                <span class="hljs-keyword">final</span> now = <span class="hljs-built_in">DateTime</span>.now();

                                <span class="hljs-keyword">final</span> result = <span class="hljs-keyword">await</span> showDatePicker(
                                    context: context,
                                    initialDate: now,
                                    firstDate: now.subtract(
                                      <span class="hljs-keyword">const</span> <span class="hljs-built_in">Duration</span>(
                                        days: <span class="hljs-number">90</span>,
                                      ),
                                    ),
                                    lastDate: now);

                                <span class="hljs-keyword">if</span> (result != <span class="hljs-keyword">null</span>) &#123;
                                  setState(() &#123;
                                    selectedDate = result;
                                  &#125;);
                                &#125;
                              &#125;,
                              child: Row(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceBetween,
                                children: [
                                  Padding(
                                    padding: <span class="hljs-keyword">const</span> EdgeInsets.only(right: <span class="hljs-number">16.0</span>),
                                    child: Text(
                                        <span class="hljs-string">'<span class="hljs-subst">$&#123;formatDateToString(selectedDate)&#125;</span>'</span>),
                                  ),
                                  Icon(Icons.calendar_today_outlined),
                                ],
                              ),
                            );
                          &#125;,
                        )),
                  ],
                ),
              ),
              Expanded(child: Container()),
              ButtonBar(
                children: [
                  ElevatedButton(
                    onPressed: () => Navigator.pop(context),
                    child: Text(<span class="hljs-string">'Cancel'</span>,
                        style: TextStyle(
                          color: Theme.of(context).primaryColor,
                        )),
                    style: ElevatedButton.styleFrom(
                      primary: Colors.white,
                      <span class="hljs-comment">// minimumSize: Size(96, 48),</span>
                    ),
                  ),
                  ElevatedButton(
                      onPressed: () &#123;
                        setState(() &#123;
                          weights.insert(
                              <span class="hljs-number">0</span>,
                              WeightModel(
                                value: <span class="hljs-built_in">double</span>.parse(weightInputController.text),
                                date: selectedDate,
                              ));
                        &#125;);
                        Navigator.pop(context);
                      &#125;,
                      child: <span class="hljs-keyword">const</span> Text(<span class="hljs-string">'Register'</span>)),
                ],
              ),
            ],
          ),
        );
      &#125;,
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我们的 ModalBottomSheet 的最终版本！</p>
<p><a href="https://github.com/evandrmb/bottom_sheet" target="_blank" rel="nofollow noopener noreferrer">github.com/evandrmb/bo…</a></p>
<hr>
<p>© 猫哥</p>
<p><a href="https://ducafecat.tech/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/</a></p>
<p><a href="https://github.com/ducafecat" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat</a></p>
<h2 data-id="heading-6">往期</h2>
<h3 data-id="heading-7">开源</h3>
<h4 data-id="heading-8">GetX Quick Start</h4>
<p><a href="https://github.com/ducafecat/getx_quick_start" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/g…</a></p>
<h4 data-id="heading-9">新闻客户端</h4>
<p><a href="https://github.com/ducafecat/flutter_learn_news" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/f…</a></p>
<h3 data-id="heading-10">strapi 手册译文</h3>
<p><a href="https://getstrapi.cn/" target="_blank" rel="nofollow noopener noreferrer">getstrapi.cn</a></p>
<h3 data-id="heading-11">微信讨论群 ducafecat</h3>
<h3 data-id="heading-12">系列集合</h3>
<h4 data-id="heading-13">译文</h4>
<p><a href="https://ducafecat.tech/categories/%E8%AF%91%E6%96%87/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-14">开源项目</h4>
<p><a href="https://ducafecat.tech/categories/%E5%BC%80%E6%BA%90/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-15">Dart 编程语言基础</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=111585" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-16">Flutter 零基础入门</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=123470" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-17">Flutter 实战从零开始 新闻客户端</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=106755" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-18">Flutter 组件开发</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=144262" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-19">Flutter Bloc</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177519" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-20">Flutter Getx4</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177514" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-21">Docker Yapi</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=130578" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p></div>  
</div>
            