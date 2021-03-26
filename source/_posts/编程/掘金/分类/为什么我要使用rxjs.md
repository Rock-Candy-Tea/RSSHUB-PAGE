
---
title: '为什么我要使用rxjs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7e9105d4dbd4c29a40ec1190bb6e3ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 19:15:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7e9105d4dbd4c29a40ec1190bb6e3ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>文章差点从 为什么我要用rxjs 变成了 为什么我要用rxjs，短短一句话体现出了中文的博大精深。最开始接触rxjs大概是在18年学习angular版本更新的时候（angular永远滴神！）。当时还买了程墨大神的书（深入浅出rxjs），并且认真地读完了。现在它还在我旁边躺着，以防不知道这篇文章怎么写了，还能去抄一点。</p>
<h1 data-id="heading-1">开始</h1>
<p>rxjs主要是一套兼具函数式和响应式编程特点，并擅长处理异步的解决方案（程墨大神书里抄的）。在rxjs中，我们习惯把它的实例称作数据流。形象一点的话，异步操作就像是没有拧紧的水龙头，不知道什么时候会滴出下一滴水。等到数据来了，rxjs就把它推出去。当数据传递过来时，我们可能需要做很多的数据处理，包括对数据的整合，筛选以及转换，而rxjs就可以用它的api来帮助我们分离并简化这些操作。</p>
<h2 data-id="heading-2">简介</h2>
<p>rxjs是可以处理同步数据的，但是现在的map,filter这些api的组合完全可以达到它的效果，也就不是很有必要使用它了。为了简单了解一下rxjs，写一个比较简单的例子。</p>
<p><img alt="1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7e9105d4dbd4c29a40ec1190bb6e3ca~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>interval是一个创建操作符，每隔1000ms就会往下游推送一个数据（0,1,2），而take是一个过滤操作符，take(3)表示只去上游推送下来的前3个数据。
subcrible表示订阅这个数据流，有3个参数，分别是next，error和complete触发时相应的处理函数。这是一个简单的操作符之间的组合，而下面，就是见证我瞎哔哔的时刻了。
另外，下面的许多例子中为了简化代码，都使用了interval操作符来替代真实的数据流，而实际使用中，我们大多会Subject实例来进行数据的推送。</p>
<h2 data-id="heading-3">原来我以为rxjs很行的用法</h2>
<p>有许多的功能，使用rxjs可以实现，而且看起来很炫酷，但我们在实际开发中可能并不需要去使用它，刻意地在项目中使用可能会起到反效果，可以先举几个例子。</p>
<h5 data-id="heading-4">1.竞速问题</h5>
<p>在我们使用部分手机号进行模糊查找的时候，由于客户输入过快，导致请求之间间隔极短，服务器返回数据的前后顺序稍有偏差，就会导致呈现的内容与预期的不一致。</p>
<p><img alt="2.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c1e8de133e3414aaa7e2e2168e842d9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图的例子中，我们用request来模拟http请求，用interval来模拟数据流，可以发现最后打印出来的是1(interval的值从0开始递增)，说明第一个request被忽略了。因为switchMap在上游产生新的数据时，会取消对上一次数据的订阅，即在我们收到1时，500ms前的0已经被取消订阅了，而它发出的request也就不会我们的结果造成影响了。
但是，现在一般为了保证服务器性能，大家都会用节流防抖来避免竞速问题的产生，这个看似方便的东西。说实话，挺鸡肋的。</p>
<h5 data-id="heading-5">2.节流防抖</h5>
<p>刚说完就到这了。Rxjs也提供了节流和防抖的解决方案，用防抖举一个小例子，使用fromEvent监听输入框的input事件，然后使用debounceTime操作符进行一个防抖的操作，在input停止变更500ms后，将值打印出来。</p>
<p><img alt="3.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7319cae94def4bf2bb8638fcdfa0bf5a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="4.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3716263386144d368094841e66ea267a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>乍一看，感觉挺简单的，去掉调试的这些console，写法也很优雅，是不是有一种情不自禁想去尝试一下的冲动。
但是这只是在原生中，如果在react，vue或者是angular中，我们一般都会使用框架的语法绑定input，难道都要改成使用fromEvent，显然是不会的。而且，自己写一个防抖并不是什么很麻烦的事情。</p>
<p><img alt="5.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54bd4a0adc1400e89ad4f779b003dbf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="6.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7543e3858614ec4b7aa2f91270df623~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>不仅实现了相同的功能，在于框架的结合使用上也没有什么问题。</p>
<h5 data-id="heading-6">3.状态管理</h5>
<p>确实，我们可以用rxjs中的Subject实例来实现状态管理。但是对于我来说，我用惯了redux和vuex，为什么我要自己再去整一套rxjs来实现状态管理呢，并且，我还要去说服其他的组员一起来做这个至少是看起来吃力不讨好的事情。可以用来写demo倒是没问题，但是用进生产，应该是遥遥无期了。</p>
<h3 data-id="heading-7">rxjs确实很行的用法</h3>
<p>虽然上面举了几个小例子，但是写作讲究先抑后扬。于是，不得不说，rxjs在有些方面，是真的让我感受到了简单和便捷！</p>
<h5 data-id="heading-8">1.Websocket</h5>
<p>例子中，页面中有2个按钮，点击按钮1打开websocket，单击按钮2关闭websocket</p>
<p><img alt="7.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84f0fb32cfb24591813ba1047a6eeded~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="8.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b360abc5dd04ee7a813c3d7c1fda48f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从代码层面来看，使用rx来实现websocket还是十分方便的，而且，当你有多处代码订阅了websocket流的时候，rxjs会在你所有代码都取消订阅后才断开连接，并不需要我们自己去做判断，或者也可以调用unSubscribe.complete()直接结束这个数据流。</p>
<h5 data-id="heading-9">2. 异步数据的筛选和处理</h5>
<p>这才是我真正觉得我会需要rxjs的地方，也是它真正的强项所在。</p>
<p>1.比如我想做个需求，在获取5个有效数据（比如大于3）以后，停止对数据的读取，在实际操作中，我们需要先判断数据是否有效，然后再进行一个计数操作，并且在次数达到5次以后，进行一次取消，而在rxjs中，就简单很多。</p>
<p><img alt="9.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/707f3b9953c149789e75f8ebf20c3149~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="10.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55e2c6b75bcd49afb69663aeee7c69c6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2.再比如，我想筛选出每1秒中内，传递过来的数据流中，不重复的数据，在原来的操作中，我们需要设置一个定时器，并设置一个存储数据的数组，然后判断新的数据和数组内的数据有没有重复的值，而使用rxjs的话，同样也会简单很多。</p>
<p><img alt="11.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c4630f7ab434137b3879069b1b3448c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="12.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f80fc07f03a4244b2030f6959a0082e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>1000ms中的间隔应该输出10个值，但是由于值重复，每1000ms中只会出现1，2，3，4这四个值，完成了对重复数据的筛选。</p>
<p>类似的api还有很多，在异步数据处理方面，使用各种api的组合，确实可以让我们的业务代码变得更加优雅易读。</p>
<h5 data-id="heading-10">3.发布订阅</h5>
<p>我在实际业务中，需要管理许多桌位的状态，但是如果放在vuex中的obj中，用id对应状态的，在每个桌位组件中引用state的话，一旦有桌位发生状态改变，就会导致obj发生变化，使所有的桌位组件update，在安卓pad上，严重影响了渲染性能，所以我们改用发布订阅的模式，单独控制每个桌位的状态，来减少组件的更新，提升性能。
代码简化一下大致是这样，数据流的来源(websocket)和组件卸载时删除的逻辑就省略了。</p>
<p><img alt="13.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a39f26fb144a5387b8b3b6511d7536~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>相当于写了一个中间层，来维系和推送信息桌位状态。但在不断地迭代和与业务结合中，这个中间层的代码，显得越来越不纯粹和难以维护（大部分原因是自己写的不够好）。于是，我想到了可能可以用rxjs来重新梳理下这一段逻辑。</p>
<p><img alt="14.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/739d5b4db2c346129eb91271ed5a93e2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从websocket获取数据，经过筛选和处理，传递给Subject，而组件只需订阅output$就可以获得传递过来的值，直接可以省略了搭建中间层的代码。但也有不足之处，原来的发布订阅模式，可以根据id指定需要运行的回调函数，但是使用了Subject后，所有的组件都会接到数据推送，需要在组件层面做一层数据筛选，但因为只需要判断是否是当前桌位的有效数据，对性能几乎没有影响。而从代码层面来说，明显会比之前清楚易读很多，业务逻辑也都可以回归到组件中，而不用写在中间层中了。</p>
<h1 data-id="heading-11">总结</h1>
<p>虽然rx已经学习了挺久了，书和文档来来回回也翻了好几遍，但是在实际项目中用的还是比较少，有写的不对的地方，或者理解不足的地方也希望大家能够指正。包括写文章前也看了群里程青松大佬写的rxjs的文章，也学习借鉴了一下。
学习一门新的技术或者库，确实不是一个很容易的事情，但是在使用的时候，我们也需要考虑到具体使用场景和整个团队的情况，太过刻意地去使用新的技术栈反而可能会事倍功半。</p>
<p>如果这篇文章对你有帮助的话，麻烦关注下我的公众号，懒狗小前端，谢谢~</p>
<p><img alt="qrcode_for_gh_0a0d3527dc75_258.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aff3a79c8534ce1a16e445ae2c00ca9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            