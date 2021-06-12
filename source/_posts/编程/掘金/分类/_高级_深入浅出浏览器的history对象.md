
---
title: '_高级_深入浅出浏览器的history对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e23a4127c7c2480289e51de413fd5c3b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 03:28:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e23a4127c7c2480289e51de413fd5c3b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、history简介</h1>
<p>History 对象包含用户（在浏览器窗口中）访问过的 URL，它是 window 对象的一部分，可通过 window.history 属性对其进行访问。history对象在前端应用中至关重要，所有单页应用的路由都是基于history对象。</p>
<h1 data-id="heading-1">二、导读</h1>
<p>本文会先简单介绍history对象的一些属性，然后会重点介绍history对象的一些实际应用，以此来帮助我们加深对history对象的理解。</p>
<h1 data-id="heading-2">三、属性介绍</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e23a4127c7c2480289e51de413fd5c3b~tplv-k3u1fbpfcp-zoom-1.image" alt="history的属性" loading="lazy" referrerpolicy="no-referrer">
上图是我在控制台打印的history对象，下面我们简单介绍一下这些属性。</p>
<h3 data-id="heading-3">3.1 属性值</h3>
<ul>
<li>length：返回浏览器历史列表中的 URL 数量。</li>
<li>scrollRestoration: 滚动恢复属性允许web应用程序在历史导航上显式地设置默认滚动恢复行为。该属性有两个可选值，默认为auto，将恢复用户已滚动到的页面上的位置。另一个值为：manual，不还原页上的位置，用户必须手动滚动到该位置。</li>
<li>state：返回一个表示历史堆栈顶部的状态的值，这是一种可以不必等待popstate事件而查看状态的方式。</li>
</ul>
<h3 data-id="heading-4">3.2 方法</h3>
<ul>
<li>history.pushState(object, title, url)方法接受三个参数，object 为随着状态保存的一个对象，title为新页面的标题，url为新的网址。</li>
<li>replaceState(object, title, url) 与pushState的唯一区别在于该方法是替换掉history栈顶元素。</li>
<li>history.go(x) 去到对应的url历史记录。</li>
<li>history.back() 相当于浏览器的后退按钮。</li>
<li>history.forward() 相当于浏览器的前进按钮。</li>
</ul>
<h3 data-id="heading-5">3.3 事件</h3>
<ul>
<li>popstate事件：popstate事件会在以下的情况触发：</li>
</ul>
<p>同一个文档的浏览历史发生变化时触发。调用history.pushState()和history.replaceState()方法不会触发。而用户点击浏览器的前进/后退按钮时会触发，调用history对象的back()、forward()、go()方法时，也会触发。popstate事件的回调函数的参数为event对象，该对象的state属性为随状态保存的那个对象。</p>
<h3 data-id="heading-6">3.4 理解</h3>
<h4 data-id="heading-7">3.4.1问题</h4>
<p>介绍了history对象，我们先抛出几个小问题：</p>
<p>1.history对象可变吗？
2.history.length既然代表浏览器历史列表中的URL数量，那么这个数量可以无限多吗？
3.location.href与history.pushState有什么区别？
4.如果我从A域名跳转到了B域名，那么history.back()会回到哪里？
5.popstate事件的触发条件是什么？</p>
<h4 data-id="heading-8">3.4.2 解答</h4>
<p>下面我们来依次解答这几个问题，初步加深对history对象的理解。</p>
<h5 data-id="heading-9">问题1</h5>
<p>history对象可变吗？</p>
<h6 data-id="heading-10">探索</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7096e83496044f1bb6ad3b9d22ea716~tplv-k3u1fbpfcp-zoom-1.image" alt="给history赋值" loading="lazy" referrerpolicy="no-referrer">
我们给history赋值为空对象，然后打印一下history，可以看到history不为空对象。</p>
<h6 data-id="heading-11">结论</h6>
<p>window.history对象是不可变的</p>
<h5 data-id="heading-12">问题2</h5>
<p>history.length既然代表浏览器历史列表中的URL数量，那么这个数量可以无限多吗？</p>
<h6 data-id="heading-13">探索</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee1780f0d2f1463899d4ea5eab8f9ae3~tplv-k3u1fbpfcp-zoom-1.image" alt="探索history.length" loading="lazy" referrerpolicy="no-referrer">
我们首先打印出history.length，发现结果为3；然后我们添加100条记录，再次打印history.length，发现值为50。</p>
<h6 data-id="heading-14">结论</h6>
<p>history.length并不会无限大</p>
<h5 data-id="heading-15">问题3</h5>
<p>location.href与history.pushState有什么区别？</p>
<h6 data-id="heading-16">探索</h6>
<p>[图片上传中...(image.png-a52ee3-1609847856284-0)]</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/534b8a42a0ad444dad5f921bd9263009~tplv-k3u1fbpfcp-zoom-1.image" alt="打印history.length" loading="lazy" referrerpolicy="no-referrer">
我们以百度h5页面来举例，首先我们进入http:<a href="http://www.baidu.xn--com,history,length2-j673avgw2bf09f7bduv2eur8agsum29v./" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com，同时打印一下history对象，length为2。</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29311260e6544157a42a07c69f8e2840~tplv-k3u1fbpfcp-zoom-1.image" alt="知乎页面" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7711c0e47f7643c2ab56856a5a38e8b0~tplv-k3u1fbpfcp-zoom-1.image" alt="打印history.length" loading="lazy" referrerpolicy="no-referrer">
接下来我们使用location.href = '<a href="https://www.zhihu.xn--com',,history,length3-bl07aih95b1n30cta25zw93aupeu4lr6cra8v2238b76bd60djnld41bkm3ewa7236bvn0ld82bda254oea434c875i3hl./" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com'来进行跳转，发现页面跳转到了知乎，此时我们再打印一下history，发现length变为了3。</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baf25d4569fa45a7ac3e0b1d9c6b47a3~tplv-k3u1fbpfcp-zoom-1.image" alt="百度h5页面" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae616f3d19b9472a8ed22db7b8f69c7d~tplv-k3u1fbpfcp-zoom-1.image" alt="打印history.length" loading="lazy" referrerpolicy="no-referrer">
此时我们点击浏览器的返回，再次回到百度h5页面，打印一下history，依然为3。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36ceb54ab4644f128428966157e2c8d4~tplv-k3u1fbpfcp-zoom-1.image" alt="pushState跳转其他域名" loading="lazy" referrerpolicy="no-referrer">
此时我们使用history.pushState(null, ' ', <a href="https://www.zhihu.xn--com'),,pushstate-0l9y8ga28cxw116drvj5lbza187rineo71b40xojgvmnyz2aja556hok6ilcldimtk4h0g9dp4qwho261d2yh./" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com')，发现抛出一个错误，意思就是pushState是不能用来在不同域名之间跳转的。</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529a3eefbe0b4678a70b4833d44264b6~tplv-k3u1fbpfcp-zoom-1.image" alt="pushState跳转当前域名" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b8192a120394350aa5e9d1aca4c2250~tplv-k3u1fbpfcp-zoom-1.image" alt="百度h5页面" loading="lazy" referrerpolicy="no-referrer">
接下来我们使用history.pushState(null, ' ', /a')，发现页面的url后面添加了一个'/a'路径，但是观察控制台，发现并没有往服务器再发送任何请求。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fb8c8f9362b49bc9d481fbc68ed1161~tplv-k3u1fbpfcp-zoom-1.image" alt="location.href跳转" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d5b786951cb4e02b1e134faa9d1c02d~tplv-k3u1fbpfcp-zoom-1.image" alt="跳转后效果" loading="lazy" referrerpolicy="no-referrer">
我们再使用一下location.href = '/a'，发现浏览器再次发起了文档请求，页面变为了Not Found</p>
<h6 data-id="heading-17">结论</h6>
<p>1.使用location.href跳转后页面会发起新的文档请求，而history.pushState不会。
2.location.href可以跳转到其他域名，而history不能。
3.location.href与history都会往历史列表中添加一条记录。</p>
<h5 data-id="heading-18">问题4</h5>
<p>如果我从A域名跳转到了B域名，那么history.back()会回到哪里？</p>
<h6 data-id="heading-19">探索</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54b928def5e0430baf04a5239f58ea09~tplv-k3u1fbpfcp-zoom-1.image" alt="百度h5页面" loading="lazy" referrerpolicy="no-referrer">
还是以百度h5页面为例
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c0ac95913674d33905e08781e997016~tplv-k3u1fbpfcp-zoom-1.image" alt="location.href跳转知乎" loading="lazy" referrerpolicy="no-referrer">
我们使用location.href = '<a href="https://www.zhihu.xn--com'-o55l73zotckza/" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com'进行跳转</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a85056c54e474d6ba6170e807e5f222b~tplv-k3u1fbpfcp-zoom-1.image" alt="history.back回退" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e044e3a540d402aaec9407d2e0b8378~tplv-k3u1fbpfcp-zoom-1.image" alt="百度页面" loading="lazy" referrerpolicy="no-referrer">
接着，使用history.back()方法，页面又回到了www.baidu.com页面</p>
<h6 data-id="heading-20">结论</h6>
<p>从A域名跳转到了B域名，那么调用history.back()会回到A域名</p>
<h5 data-id="heading-21">问题5</h5>
<p>popstate事件的触发条件是什么？</p>
<h6 data-id="heading-22">探索</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c3559f855834a099e1e8da84e49a221~tplv-k3u1fbpfcp-zoom-1.image" alt="监听popstate事件" loading="lazy" referrerpolicy="no-referrer">
首先我们监听一下popstate事件，然后我依次调用了location.href，location.hash，history.go，history.back，history.forward，history.pushState，history.replaceState方法，得出结果如下</p>
<h6 data-id="heading-23">结论</h6>
<p>1.因为location.href是刷新式的跳转，所以这个打印信息是肯定打印不出来的，在刷新的时候这个监听函数就已经失效了，所以这里不讨论location.href会不会触发popstate事件。跟location.href类似的还有history.go(0)，因为history.go(0)也会直接刷新页面，所以这个监听函数也会失效，也不会打印出信息。
2.location.hash是会触发popstate事件的，同样会触发popstate的还有history.back，history.forward，history.go。
3.history.pushState，history.replaceState都不会触发popstate事件。</p>
<h1 data-id="heading-24">四、应用</h1>
<p>通过以上几个问题，我们初步了解了history对象，下面我们来看一下它的一些实际应用</p>
<h3 data-id="heading-25">4.1 单页应用</h3>
<p>history最常见的使用就是搭建前端单页应用
使用history.pushState方法可以改变地址栏的路径而不用刷新页面，所以这使得我们只需要在第一次进入页面的时候去请求一次html，后续的页面呈现则交由js来控制，根据不同url路径来加载不同的js模块。
使用history路由需要注意的是服务器需要做好处理 URL 的准备，因为当用户在url为'/a/b/c'的页面进行刷新操作，服务器很有可能会因为匹配不到路径而返回404状态码，应当对这样的路径也都返回html文件。</p>
<h3 data-id="heading-26">4.2 交互操作</h3>
<h5 data-id="heading-27">问题</h5>
<p>另一类比较常见的，就是一些交互实现类。比如说以下交互：
1.在创建/编辑页面，用户修改了表单以后，如果退出的时候，给出二次弹窗确认。
2.在移动端的列表页，点击筛选框会弹出一个浮层，当用户点击app的后退按钮时，把浮层关闭掉，而不是回退页面。
3.当前处在页面A，点击跳转到页面B，由页面B内请求发现当前用户无权限，于是跳转到错误页C，如果避免用户在C页面点击浏览器的回退按钮再次回到B页面。</p>
<h5 data-id="heading-28">解答</h5>
<h6 data-id="heading-29">分析</h6>
<p>1.交互1与交互2是同一类问题，原理都是点击浏览器的前进与后退按钮都会触发popstate事件，监听这个popstate事件，一旦触发，便给出一个弹窗。需要注意的是，当popstate事件触发的时候，历史地址记录就已经被回退了，我们无法阻止这个回退，所以在回退之前，我们需要使用history.pushState(null,null,document.URL)方法去主动再添加一条当前url的记录，当popstate事件触发的时候，虽然回退了一条记录，但是url并不会改变，也就达到了停留在当前页面的目的。
2.关于交互3，我们要学会使用history.replace方法，如果我们一直使用pushState或者location.href进行跳转的话，那么此时历史记录是这样的A—B—C，但是如果我们从B到C跳转的时候使用history.replace的话，B记录就会被替换为C记录，那么历史记录就会变为A—C，此时从C页面点击返回按钮就可以直接返回A页面。</p>
<h6 data-id="heading-30">实例</h6>
<p>下面我给出一个点击浏览器的后按钮后弹窗的效果，供大家参考。
还是以百度h5页面举例，在'/a'页面，我点击返回的时候，会弹出禁止返回的弹窗。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2375742fc334c2291ddfac8fbcd6ed7~tplv-k3u1fbpfcp-zoom-1.image" alt="弹窗提示" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体代码如下，可在控制台使用</p>
<pre><code class="copyable">   history.pushState(null, null, '/a')
   window.addEventListener('popstate', () => &#123;
     alert('禁止返回')
   &#125;)
   history.pushState(null, null, document.URL)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">4.3 各种路由框架的基础</h3>
<p>路由框架通常都有三种模式：browserHistory，hashHistory，memoryHistory，其中browserHistory的实现就是依赖于window.history对象，下面我们先来想两个问题，然后接着来实现一个简单的前端单页路由。</p>
<h5 data-id="heading-32">问题</h5>
<p>1.用window.history.pushState和路由框架的pushState有什么区别？
2.既然使用history.pushState无法触发popstate事件，那么路由框架又是如何在pushState的时候加载不同组件的呢？
3.为什么使用pushState跳转以后，history对象的state里都有一个属性key？</p>
<h5 data-id="heading-33">解答</h5>
<p>下面咱们来分析一下这几个问题。</p>
<h6 data-id="heading-34">实验</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7319e1f15fcc4f9bb665dc0929e8671e~tplv-k3u1fbpfcp-zoom-1.image" alt="掘金前端板块" loading="lazy" referrerpolicy="no-referrer">
首先我们掘金的首页，点击前端板块，发现在进入'/frontend'路径时，并没有发送html请求，说明这是一个单页应用，下面我们再返回首页，使用history.pushState(null, null, '/frontend')来进入前端板块，看看会发生什么。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0985a7b24e644ec0af887106c1c47b53~tplv-k3u1fbpfcp-zoom-1.image" alt="pushState以后的页面" loading="lazy" referrerpolicy="no-referrer">
可以看到，此时url已经变了，但是页面并没有渲染出前端模块。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5cd1058d5c044ddb9371ab2cff4c7aa~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-router-push函数" loading="lazy" referrerpolicy="no-referrer">
我们顺势来看一看vue-router的源码，我们可以看到它调用了一个pushState函数，我们来看看这个函数
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61784eb2ee8f45eaa8b44fddd3a4a8a7~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-router-pushState函数" loading="lazy" referrerpolicy="no-referrer">
并没有看出什么特别的地方，这儿的pushState就是调用了history.pushState函数。不过从这里我们看出了问题3的答案，vue-router在使用push函数的时候调用了history.pushState方法，而这里在使用history.pushState函数时往里面加了一个key。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0b4503975074e858949c6b6baa26cd2~tplv-k3u1fbpfcp-zoom-1.image" alt="key属性" loading="lazy" referrerpolicy="no-referrer">
我们可以看到这个key的值就是一个时间，有什么特殊含义吗？后来查阅官方文档，得出了这样的解释：
<code>当一个 history 通过应用程序的 push 或 replace 跳转时，它可以在新的 location 中存储 “location state” 而不显示在 URL 中，这就像是在一个 HTML 中 post 的表单数据。 在 DOM API 中，这些 hash history 通过 window.location.hash = newHash 很简单地被用于跳转，且不用存储它们的location state。但我们想全部的 history 都能够使用location state，因此我们要为每一个 location 创建一个唯一的 key，并把它们的状态存储在 session storage 中。当访客点击“后退”和“前进”时，我们就会有一个机制去恢复这些 location state。</code>
我们再回到之前的问题一与问题二，既然这个pushState没有什么特别的，我们再来看一看这个transitionTo函数。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0135538512c04c7d8b3eb59c76059b2f~tplv-k3u1fbpfcp-zoom-1.image" alt="vue-router-transitionTo函数" loading="lazy" referrerpolicy="no-referrer">
我发现了这段代码，这里调用了该路由的回调函数。众所周知，我们注册一个路由一般是采用这种形式<code>router.route('/111', state => &#123; contentDOM.innerHTML = '111';&#125;);</code>这里就是执行了<code>state => &#123; contentDOM.innerHTML = '111'; &#125;</code>这个回调函数，所以问题就清楚了，路由框架的pushState不仅调用了history.pushState方法，还调用了该路由对应的回调函数来渲染了对应的组件。</p>
<h6 data-id="heading-35">结论</h6>
<p>所以我们得出结论，路由框架的pushState与history.pushState是不一样的，路由框架的pushState不仅调用了history.pushState改变了url，更重要的是它还多了一步操作，即根据这个url销毁了旧组件，渲染了新组件；至于state里面的key值，则是为了兼容hashHistory。</p>
<h3 data-id="heading-36">4.4 前端路由demo</h3>
<p>下面我们来实现一个前端路由的demo，现在已经有一个html，我们需要为它写一个Router，实现如下效果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b37906a00074951b9afe0aecdc1fc77~tplv-k3u1fbpfcp-zoom-1.image" alt="前端路由demo" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>前端路由实现</title>
  <style>
    .link &#123;
      color: #999;
      cursor: pointer;
    &#125;
    .link:hover &#123;
      text-decoration: underline;
    &#125;
  </style>
</head>
<body>
<ul>
  <li><a class="link" data-href="/A">A</a></li>
  <li><a class="link" data-href="/B">B</a></li>
  <li><a class="link" data-href="/C">C</a></li>
  <li><a class="link" data-href="/D">D</a></li>
</ul>

<div id="wrapper"></div>


<script>
  // 创建实例
  const router = new Router();
  const contentDOM = document.querySelector('#wrapper');
  // 注册路由
  router.route('/A', state => &#123;
    contentDOM.innerHTML = 'A';
  &#125;);
  router.route('/B', state => &#123;
    contentDOM.innerHTML = 'B';
  &#125;);
  router.route('/C', state => &#123;
    contentDOM.innerHTML = 'C';
  &#125;);
  router.route('/D', state => &#123;
    contentDOM.innerHTML = 'D';
  &#125;);
</script>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单分析一下:
1.首先发布订阅模式肯定少不了，注册路由的时候，需要将每个路由所对应的回调函数存储起来，在路由变化的时候执行对应的回调函数。
2.只监听popSate是不够的，页面初始化的时候，以及pushState的时候，都需要执行对应的回调函数去主动更新一下组件。
3.还有一个问题，就是需要阻止这几个a标签的默认事件。
经过以上对history的理解，这个简单的Router已经不难实现了，下面直接给出完整代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>前端路由实现</title>
  <style>
    .link &#123;
      color: #999;
      cursor: pointer;
    &#125;
    .link:hover &#123;
      text-decoration: underline;
    &#125;
  </style>
  <script>

    const noop = () => undefined;

    class Router &#123;
      constructor() &#123;
        this.init();
      &#125;

      // 初始化
      init() &#123;
        this.routes = &#123;&#125;;
        this.doListen();
        this.makeLink();
      &#125;
      // 监听
      doListen() &#123;
        window.addEventListener('DOMContentLoaded', this.listenEventInstance.bind(this));
        window.addEventListener('popstate', this.listenEventInstance.bind(this));
      &#125;

      // 监听事件后，触发路由的回调
      listenEventInstance() &#123;
        this.callbackCenter(window.location.pathname);
      &#125;;

      // 注册路由，将回调函数存储下来
      route(pathname, callback = noop) &#123;
        this.routes[pathname] = callback;
      &#125;

      // 回调
      callbackCenter(pathname) &#123;
        if (!this.routes[pathname]) &#123;
          return;
        &#125;
        const &#123;state&#125; = window.history;
        this.routes[pathname](state);
      &#125;

      // 绑定 a 标签，阻止默认行为
      makeLink() &#123;
        document.addEventListener('click', e => &#123;
          const &#123;target&#125; = e;
          const &#123;nodeName, dataset: &#123;href&#125;&#125; = target;
          if (!(nodeName === 'A') || !href) &#123;
            return;
          &#125;
          e.preventDefault();
          window.history.pushState(null, '', href);
          this.callbackCenter(href);
        &#125;);
      &#125;
    &#125;

  </script>
</head>
<body>
<ul>
  <li><a class="link" data-href="/A">A</a></li>
  <li><a class="link" data-href="/B">B</a></li>
  <li><a class="link" data-href="/C">C</a></li>
  <li><a class="link" data-href="/D">D</a></li>
</ul>

<div id="wrapper"></div>


<script>
  // 创建实例
  const router = new Router();
  const contentDOM = document.querySelector('#wrapper');
  // 注册路由
  router.route('/A', state => &#123;
    contentDOM.innerHTML = 'A';
  &#125;);
  router.route('/B', state => &#123;
    contentDOM.innerHTML = 'B';
  &#125;);
  router.route('/C', state => &#123;
    contentDOM.innerHTML = 'C';
  &#125;);
  router.route('/D', state => &#123;
    contentDOM.innerHTML = 'D';
  &#125;);
</script>
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-37">五、总结</h1>
<p>本文首先介绍了history对象的各个属性，然后介绍了它的一些应用，希望本文能在实际工作中对大家有所帮助。在前端路由这块儿除了window.history以外，其他知识点以及相关应用还有很多。对于location对象、搭建多页应用等其他知识，大家感兴趣的话可以去深入探究。</p>
<h1 data-id="heading-38">六、参考</h1>
<ul>
<li>jqhtml.com: <a href="https://www.jqhtml.com/43510.html" target="_blank" rel="nofollow noopener noreferrer">单页应用的部署方案</a></li>
<li>掘金:<a href="https://juejin.cn/post/6844903773266001933#heading-4" target="_blank"> 性能 & 集成 —— History API</a></li>
<li>react-router: <a href="http://react-guide.github.io/react-router-cn/docs/guides/basics/Histories.html#hashHistory" target="_blank" rel="nofollow noopener noreferrer">react-router文档</a></li>
<li>vue: <a href="https://github.com/vuejs/vue-router/blob/ca80c4442c85329b950de483a596aae0d91e7ca8/dist/vue-router.js#L2190" target="_blank" rel="nofollow noopener noreferrer">vue源码</a></li>
<li>MDN: <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/History" target="_blank" rel="nofollow noopener noreferrer">history对象</a></li>
</ul></div>  
</div>
            