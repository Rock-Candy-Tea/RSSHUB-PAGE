
---
title: 'Glide 三部曲之请求生命周期管控'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/6038844-01b421aa796c0e33.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/6038844-01b421aa796c0e33.png'
---

<div>   
<ul>
<li>本文章所使用的 Glide 源码版本：4.11.0</li>
</ul>
<h4>源码解析</h4>
<ul>
<li>在讲源码之前，我们先复习一下 Glide 的用法</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="996" data-height="140"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-01b421aa796c0e33.png" data-original-width="996" data-original-height="140" data-original-format="image/png" data-original-filesize="89917" src="https://upload-images.jianshu.io/upload_images/6038844-01b421aa796c0e33.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>主要分成三部曲：传入 Activity 或者 Fragment、传入图片地址、传入目标的 ImageView</p></li>
<li><p>我们先讲讲 Glide 的生命周期控制，也就是 Glide.with 方法，让我们简单看一下里面的源码</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2924" data-height="1686"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-f7aee827c180c4ee.png" data-original-width="2924" data-original-height="1686" data-original-format="image/png" data-original-filesize="2603050" src="https://upload-images.jianshu.io/upload_images/6038844-f7aee827c180c4ee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>我们可以看到，Glide.with 复写了多个不同参的方法，那么问题来了，这些方法有什么不一样，Glide 又拿它们做了什么事？</p></li>
<li><p>带着这个疑问，我们先进入 Glide.with(FragmentActivity activity) 的源码里面看看</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1724" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-b12e052e8daebd71.png" data-original-width="1724" data-original-height="600" data-original-format="image/png" data-original-filesize="593404" src="https://upload-images.jianshu.io/upload_images/6038844-b12e052e8daebd71.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1828" data-height="584"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-a6d2a5e8f42b6867.png" data-original-width="1828" data-original-height="584" data-original-format="image/png" data-original-filesize="542587" src="https://upload-images.jianshu.io/upload_images/6038844-a6d2a5e8f42b6867.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1932" data-height="514"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-5de110a1e2d9dc04.png" data-original-width="1932" data-original-height="514" data-original-format="image/png" data-original-filesize="404325" src="https://upload-images.jianshu.io/upload_images/6038844-5de110a1e2d9dc04.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1742" data-height="896"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-a16cb873f7835b50.png" data-original-width="1742" data-original-height="896" data-original-format="image/png" data-original-filesize="731553" src="https://upload-images.jianshu.io/upload_images/6038844-a16cb873f7835b50.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>通过查看这几段源码，我们可以得出一个结论，Glide 拿到 FragmentActivity 的用处是为了在 Activity 里面创建一个 Fragment，那么问题又来了，它创建 Fragment 是要做什么事？接下来让我们继续追踪一下源码。</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2544" data-height="1630"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-2e407cfddebef84f.png" data-original-width="2544" data-original-height="1630" data-original-format="image/png" data-original-filesize="2666607" src="https://upload-images.jianshu.io/upload_images/6038844-2e407cfddebef84f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>看到这里，我想大多数人的想法跟我一样，想看这个 Fragment 到底长啥样？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2622" data-height="1570"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-9229ef5d1440c9ca.png" data-original-width="2622" data-original-height="1570" data-original-format="image/png" data-original-filesize="2524642" src="https://upload-images.jianshu.io/upload_images/6038844-9229ef5d1440c9ca.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2568" data-height="1614"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-dbb777b1b8351bf7.png" data-original-width="2568" data-original-height="1614" data-original-format="image/png" data-original-filesize="2545620" src="https://upload-images.jianshu.io/upload_images/6038844-dbb777b1b8351bf7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>通过搜索关键字，我们基本可以断定这个是一个无界面的 Fragment，也可以认为是一个透明的 Fragment，那么 Glide 到底是想做什么？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2542" data-height="1620"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-359242cbcbc666a8.png" data-original-width="2542" data-original-height="1620" data-original-format="image/png" data-original-filesize="2405539" src="https://upload-images.jianshu.io/upload_images/6038844-359242cbcbc666a8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>接下来让我们把目光放到一个类上面，ActivityFragmentLifecycle，光看名字就知道这个是我们要讲的主角之一：生命周期管理，接下来我们看看这个类在 Fragment 里面做了什么事</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1428" data-height="940"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-65314e6c40c919bc.png" data-original-width="1428" data-original-height="940" data-original-format="image/png" data-original-filesize="504614" src="https://upload-images.jianshu.io/upload_images/6038844-65314e6c40c919bc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2796" data-height="1640"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-f226a972d56a358e.png" data-original-width="2796" data-original-height="1640" data-original-format="image/png" data-original-filesize="1422458" src="https://upload-images.jianshu.io/upload_images/6038844-f226a972d56a358e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>那么问题又来了，Glide 这样做的目的又是什么？是为了解决什么问题而做的？</p></li>
<li><p>这个问题非常值得我们去思考，首先我们要知道，Glide 是通过网络请求获取图片的资源，网络请求是异步的，也就是必须在子线程中，而 Activity 是运行在主线程中，正常的情况是 Glide 请求完毕之后 Activity 再销毁，但是这个并不能代表所有的请求都会按照这个逻辑来执行，往往是 Glide 还没有请求完毕 Activity 已经销毁了这种情况也非常常见，为了避免这种情况，我们必须知道 Activity 什么时候销毁，然后赶在 Activity 销毁之前把网络请求取消。</p></li>
<li><p>这个时候 Fragment 发挥了很大的作用，我们都知道 Fragment 是依附于 Activity，同时这两者的生命周期是绑定在一起的，Glide 通过 Fragment 的生命周期就能知道 Activity 的生命周期。</p></li>
<li><p>那么问题又来了，刚刚 Glide.with 有很多重载方法，万一它传入的不是 FragmentActivity，而是其他类型的对象，那么 Glide 又会怎么处理呢？</p></li>
<li><p>我就是不给你传入 FragmentActivity，而是直接传入 Activity，让 Glide 创建不了 Fragment 对象，这样它就监听不到 Activity 的生命周期了</p></li>
<li><p>接下来让我们看看 Glide 应对 Activity 对象会做什么不一样的处理？</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1790" data-height="542"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-1867f4b86b3cc26b.png" data-original-width="1790" data-original-height="542" data-original-format="image/png" data-original-filesize="469670" src="https://upload-images.jianshu.io/upload_images/6038844-1867f4b86b3cc26b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1790" data-height="602"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-ce932aa2f3f10e75.png" data-original-width="1790" data-original-height="602" data-original-format="image/png" data-original-filesize="459763" src="https://upload-images.jianshu.io/upload_images/6038844-ce932aa2f3f10e75.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1736" data-height="914"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-467fc15e941119c6.png" data-original-width="1736" data-original-height="914" data-original-format="image/png" data-original-filesize="757386" src="https://upload-images.jianshu.io/upload_images/6038844-467fc15e941119c6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>看到这里，我们要纠正一个误区，不是一定要 FragmentActivity 才能创建 Fragment，其实 Activity 对象也是可以的，只不过这个是 Android 3.0 之后的特性</p></li>
<li><p>app.Fragment、support.Fragment 的思想和用法和 Activity 和 Fragment Activity 大同小异，这里直接略过</p></li>
<li><p>再来跟大家讲讲 Fragment，它又是怎么监听生命周期的</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1766" data-height="544"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-43425478345bbe50.png" data-original-width="1766" data-original-height="544" data-original-format="image/png" data-original-filesize="489519" src="https://upload-images.jianshu.io/upload_images/6038844-43425478345bbe50.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1866" data-height="590"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-e3beede449adeb09.png" data-original-width="1866" data-original-height="590" data-original-format="image/png" data-original-filesize="544710" src="https://upload-images.jianshu.io/upload_images/6038844-e3beede449adeb09.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>看到这里，我们没必须要继续往下看了，还是原来的配方，还是熟悉的味道</p></li>
<li><p>接下来让我们看看 Context 参数的 Glide.with 方法</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1792" data-height="1174"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-fb7cd5a26f82d35e.png" data-original-width="1792" data-original-height="1174" data-original-format="image/png" data-original-filesize="1528526" src="https://upload-images.jianshu.io/upload_images/6038844-fb7cd5a26f82d35e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1744" data-height="946"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-d1689084d9cd140b.png" data-original-width="1744" data-original-height="946" data-original-format="image/png" data-original-filesize="853685" src="https://upload-images.jianshu.io/upload_images/6038844-d1689084d9cd140b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>分析上面的源码，我们可以知道，你如果给 Glide 传入的是一个 Context 对象，它会自动推导 Context 的类型，究竟是 FragmentActivity 呢还是 Activity 呢，如果两种都不是呢？万一是 Application 的 Context 呢？接下来继续看源码</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1778" data-height="1168"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-caafe189871da4e1.png" data-original-width="1778" data-original-height="1168" data-original-format="image/png" data-original-filesize="728014" src="https://upload-images.jianshu.io/upload_images/6038844-caafe189871da4e1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>看到这段源码，我们又发现了一个 Lifecycle 类，只不过这次跟我们之前看到的 ActivityFragmentLifecycle 类不一样，因为它换了一个马甲：ApplicationLifecycle</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1760" data-height="946"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-64bbb58513266d76.png" data-original-width="1760" data-original-height="946" data-original-format="image/png" data-original-filesize="821123" src="https://upload-images.jianshu.io/upload_images/6038844-64bbb58513266d76.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="746" data-height="332"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-0048cb09038a33d7.png" data-original-width="746" data-original-height="332" data-original-format="image/png" data-original-filesize="148355" src="https://upload-images.jianshu.io/upload_images/6038844-0048cb09038a33d7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>那么又问题来了，它和 ActivityFragmentLifecycle 有什么区别？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1768" data-height="1630"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-50e02d5890eb1407.png" data-original-width="1768" data-original-height="1630" data-original-format="image/png" data-original-filesize="1093990" src="https://upload-images.jianshu.io/upload_images/6038844-50e02d5890eb1407.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>让我们再回顾一下这个类，经过比对不难发现，ApplicationLifecycle 类没有生命周期之类的方法回调</p></li>
<li><p>所以到这里，我们也不难断定，当我们传入的 Context 对象经过推导之后不是 Activity 或者 FragmentActivity 对象，那么 Glide 会把这个请求当做一个全局请求，何为全局请求，请求的生命周期和应用的生命周期保持一致，只要应用不被杀死，那么这个网络请求在请求完毕之前就不会消失。</p></li>
</ul>
<h4>总结</h4>
<ul>
<li>Glide 请求生命周期主要利用一个无界面的 Fragment，然后绑定到 Activity / Fragment 上面，由此来感知 Activity / Fragment 的生命周期，从而赶在 Activity / Fragment 对象销毁之前把网络请求移除掉，另外如果我们传入的 Context 对象不是 Activity / Fragment，Glide 会默认将这个网络请求作为一个全局请求，这样就完成了 Glide 对网络请求的生命周期控制。</li>
</ul>
<h4>下一篇：<a href="https://www.jianshu.com/p/9f5d95632120" target="_blank">Glide 三部曲之图片加载流程</a>
</h4>
<h4>Android 技术讨论 Q 群：10047167</h4>
  
</div>
            