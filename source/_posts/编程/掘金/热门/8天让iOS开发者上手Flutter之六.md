
---
title: '8天让iOS开发者上手Flutter之六'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3c12fb3b244575ac6b794168d93675~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 00:45:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3c12fb3b244575ac6b794168d93675~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>发现了一个宝藏网址，这里讲解的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/" ref="nofollow noopener noreferrer">flutter实战</a>比我写的靠谱多了。</p>
<h1 data-id="heading-0">准备网络数据</h1>
<p>这一步不是很重要，提供一些假数据而已，不是重点嫌麻烦的可以跳过。</p>
<p>先介绍一个网址：<a href="https://link.juejin.cn/?target=http%3A%2F%2Frap2.taobao.org%2Faccount%2Flogin" target="_blank" rel="nofollow noopener noreferrer" title="http://rap2.taobao.org/account/login" ref="nofollow noopener noreferrer">rap2.taobao.org/account/log…</a> 这个网址用来搭建我们需要的网络数据，注册账号非常简单，这里就不多说了。</p>
<p>注册完成之后，新建一个仓库，简简单单取个名字就够了：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3c12fb3b244575ac6b794168d93675~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后点击进入仓库，可以看到下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfd2860cb5c64f4b947d45551aba9d93~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>会默认生成以一个示例接口，可以看一看示例接口的生成规则。看不懂也没关系，我们直接直接上手自己新建一个接口，如图所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0af92d6af9b14eae865b69d5beb874c4~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击右上角的编辑按钮进入编辑模式，新建一个响应chatlist，类型为Array。然后生成chatlist的数据，imageUrl表示每条聊天数据的用户头像。其中用户头像的初始值里面有一段@natural(20,99)，这个是Mock.js代码。这里是相关介绍<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmockjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://mockjs.com/" ref="nofollow noopener noreferrer">mockjs.com/</a>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b21769272134c4ea316f9289a9d945d~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每条聊天数据，除了imageUrl还需要有用户名name和消息的内容message。@cname用来生成随机的中文名，@cparagraph用来生成随机的中文段落来表示聊天内容。我们这里只是简单的构造一下这个聊天列表所需要的数据，真正的聊天列表的数据肯定是不会这么简单的。。。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1a42755454d455d9d2be30c80fd6e62~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_15.png" loading="lazy" referrerpolicy="no-referrer">
编辑的差不多的时候，记得点击保存,保存之后点击红圈中的图标就可以获取到数据
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1db20c16414845bc45ce901e244a66~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">聊天页面导航条</h1>
<h2 data-id="heading-2">准备工作</h2>
<p>默认展示页面改为<code>_currentIndex</code>改为0,新建chat目录，将相关文件放在这里。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0213b262930d4066b6f26e34993011cc~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210808_17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">添加加号按钮</h2>
<p>加号按钮这个东西，我们之前已经添加过类似的了，appBar的actions就是我们需要添加代码的地方。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336b5de10dc2451bbb989516bd66049c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果我们按照这个思路写下去的话，就需要自己再去实现一个弹出菜单的类。其实flutter提供了我们一些现成的类可以做到类似的效果。</p>
<h2 data-id="heading-4"><code>PopupMenuButton</code></h2>
<p><code>PopupMenuButton</code>类用来弹出一个菜单，必传参数为<code>itemBuilder</code>，用来实现它需要展示的内容。<code>PopupMenuItem</code>就是用来展示内容的类。这里有一个细节说一下，<code>PopupMenuButton</code>有一个<code>onSelected</code>属性，这个属性是个闭包，意思是选中某个<code>PopupMenuItem</code>的时候，会调用这个闭包。但是有一个前提就是每个<code>PopupMenuItem</code>的<code>value</code>必须不为null的时候，才会执行<code>onSelected</code>闭包，我在这里卡了半天，网上找了半天资料也没有明确讲到这里。其他就没什么好讲的了，都比较简单。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b9d82deec2e46e881aa084e25d9bb7d~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210812_19.png" loading="lazy" referrerpolicy="no-referrer">
其中<code>_buildMenuItem</code>的实现如下，注意<code>value</code>要赋值就好了，不为空就行，不然<code>PopupMenuButton</code>的<code>onSelected</code>不执行：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f6f5da2ff794264afbf256c95e307a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
还有一个小细节，如何设置<code>PopupMenuButton</code>的颜色，可以直接设置它的颜色
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0548c31d2ba248e9b8bdeb375031c487~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
还可以设置APP的主题的<code>cardColor</code>，不过这个优先级没有直接设置<code>PopupMenuButton</code>颜色高。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c19742492944488ba13249b31db685b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">请求网络数据</h1>
<h2 data-id="heading-6"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.flutter-io.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.flutter-io.cn/" ref="nofollow noopener noreferrer">pub.flutter-io.cn/</a></h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04224929590b47528f1a1ea05dbe8ab9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个网站可以搜索flutter使用的包packages。我们使用http这个包来请求我们的网络数据。这个包是flutter官方提供的。实际项目开发的时候可能并不会使用http这个包，大部分是使用dio来请求网络数据。这里只介绍官方的http包如何使用。</p>
<h2 data-id="heading-7">导入http包</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32044f0faafd4673bc0a0e5cc22ae858~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dfb3991238d4f77927c2728ef210d6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
粘贴完成之后需要更新一下，就是获取一下包对应的代码。可以通过上方的<code>Pub get</code>,也可以在终端中输入<code>flutter packages get</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfeb775cd3ae4e96ba22440e706d33d3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
命令执行完之后，就可以使用这个包了。</p>
<h2 data-id="heading-8">导入http头文件并取别名</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9539435380ef4dd38aa8af4eaa119b38~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">发送请求</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df206f11e0b1474e8086c80ff222d5cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
请求的发送写在<code>initState</code>里面。<code>getData()</code>后面跟了一个async表示的是异步执行。async需要搭配await使用，await后面跟着的是耗时的代码。所以上面的程序会先打印来了，然后再输出请求的状态码；
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9e9b0f789c4471492caccb982daa03d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
点击其他的页面，再次回到当前页面会发现initState方法重新走了一遍，这是因为我们还没有保存住状态，后面会讲到如何保持Widget的状态。</p>
<h2 data-id="heading-10">处理返回的数据</h2>
<p>首先介绍一下，在flutter中如何将请求返回的JSON数据转为Map，在我们iOS开发中是转为字典，而flutter中没有字典这个类型，对应的类型是Map。以及如果将Map转为JSON。在iOS中我们知道会使用一个<code>NSJSONSerialization</code>的类用来处理JSON数据。同样的，在flutter中也会有一个专门的类<code>JsonCodec</code>来处理。</p>
<h3 data-id="heading-11">JSON和Map互相转</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd897b4dbfd54af1941972b4360d3159~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
其中的json就是<code>JsonCodec</code>的实例。需要导入<code>'dart:convert'</code>头文件。flutter中还可以通过<code>is</code>来判断是不是某个类型。</p>
<h3 data-id="heading-12">新建聊天模型</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3017a15c3cbe4d3ab67d82bafdb385f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
除了红框内的方法之外，其他没什么新鲜事物。红框内的方法应该说是一个工厂方法，是设计模式的一种，用来初始化对象的。除了默认的初始化方法，还可以使用这个工厂方法来实例化一个Chat对象。模型建立好了之后就可以处理响应的数据了</p>
<h3 data-id="heading-13">处理响应的数据</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bf33bb810d64e51873ad84fb15bf76d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里用到了Future，关于Future的讲解可以看官方文档<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.cn%2Ftutorials%2Flanguage%2Ffutures" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.cn/tutorials/language/futures" ref="nofollow noopener noreferrer">dart.cn/tutorials/l…</a></p>
<h1 data-id="heading-14">使用FutureBuilder显示界面</h1>
<p>很多时候我们会依赖一些异步数据来动态更新UI，比如在打开一个页面时我们需要先从互联网上获取数据，在获取数据的过程中我们显示一个加载框，等获取到数据时我们再渲染页面；当然，通过StatefulWidget我们完全可以实现上述这些功能。但由于在实际开发中依赖异步数据更新UI的这种场景非常常见，因此Flutter专门提供了<code>FutureBuilder</code>来快速实现这种功能。<code>FutureBuilder</code>会依赖一个<code>future</code>，它会根据所依赖的<code>future</code>的状态来动态构建自身。这个<code>future</code>我们刚刚已经准备好了。关于<code>FutureBuilder</code>的介绍<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2Fchapter7%2Ffuturebuilder_and_streambuilder.html%23_7-5-1-futurebuilder" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/chapter7/futurebuilder_and_streambuilder.html#_7-5-1-futurebuilder" ref="nofollow noopener noreferrer">这篇文章</a>讲解的很详细。
最后完整代码如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/320e21f3548744db88a59b289094e80b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-15">不使用FutureBuilder的方式</h1>
<p>刚刚说了，我们可以使用FutureBuilder来快速实现展示异步网络数据，也可以自己实现，现在我们自己实现一下。使用一个私有变量_chatList记录请求下来的数据，再根据_chatList的值来展示不同的页面。代码如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57600afd73aa4a3c8178bc07be97a375~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22da31c383294f85ae5af4ad182b2ab1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
因为getData的返回值是Future的原因，getData()后面可以跟<code>then</code>方法，还可以跟错误捕获<code>catchError</code>,完成时的回调<code>whenComplete</code>，超时设置<code>timeOut</code>等等，这种写法挺有意思，一路点下去就完了...</p>
<h2 data-id="heading-16">实现超时取消刷新功能</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b865f3d6e0434e74a1e1a3324da786f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在每次请求的时候，重置<code>_cancelConnect</code>的值。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07c8ba9d07b446f9a6684241fc5f31bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-17">保持Widget的状态</h1>
<p>我们来回点击通讯录页面和聊天页面，会发现每次点击进入当前的页面，都会重新的载入，<code>initState()</code>会被重新调用。将通讯录页面滑动到底部，再次点击进入会发现又默认回到了顶部。为什么会出现这样的问题。正是因为我们的Widget的状态没有保持，每次展示都重新创建了。</p>
<p>Dart语言中有一个Mixins的概念：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.cn%2Fsamples%23mixins" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.cn/samples#mixins" ref="nofollow noopener noreferrer">官方的解释是这样</a>，可以给类A Mixins 一个B，那么A就拥有了B的属性和方法。有点像OC的类扩展的意思。保持Widget的状态就需要用到这个语言特性。一共有三个步骤：</p>
<ol>
<li>Mixins 类<code>AutomaticKeepAliveClientMixin</code></li>
<li>重写<code>wantKeepAlive</code>方法</li>
<li>调用父类Builder方法</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3d29b34ea3746b9a9cc7ec0ca19a9d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样把通讯录页面也实现上面的步骤。然后再次来回点击发现还是没有保持住状态？？？这里有一个最大的问题就是我们的根Widget都没有保持住状态，那还谈什么保持子Widget的状态呢。。。</p>
<h2 data-id="heading-18">使用PageView</h2>
<p>来到rootPage.dart文件，我们会看到body里面直接取了数组的某个元素作为根Widget展示。这样是无法保持住状态的，使用PageView才可以保持住状态。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/275398750bb34835b5fa1a593e30bbc4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
使用PageView，代码如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adc5cc5e8c1046909d27097107c9f590~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
点击跳转到其他页面就可以直接通过_pageController来完成。使用了PageView之后会发现，不同的页面之间可以直接通过手势左右滑到就能切换了。这样的效果我们一般是不需要的，可以设置直接关闭。如果需要的话，在滑动的方法里面重新设置底部导航条的正确位置也是没有问题的。</p>
<h3 data-id="heading-19">使用滑动切换，解决bug</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44cb9bc186724397b471136abbcc44ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">禁用滑动切换</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9d533514d734781bd6a13e6c43e738a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            