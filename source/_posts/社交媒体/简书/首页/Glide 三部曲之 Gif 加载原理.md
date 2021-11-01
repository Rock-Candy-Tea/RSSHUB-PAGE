
---
title: 'Glide 三部曲之 Gif 加载原理'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/6038844-4b98652e31d227d0.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/6038844-4b98652e31d227d0.png'
---

<div>   
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FgSQbKLp_T4PBGHFsgX8ATw" target="_blank">本篇文章已授权微信公众号 guolin_blog （郭霖）独家发布</a></p>
<ul>
<li>本文章所使用的 Glide 源码版本：4.11.0</li>
</ul>
<h4>上一篇：<a href="https://www.jianshu.com/p/9f5d95632120" target="_blank">Glide 三部曲之图片加载流程</a>
</h4>
<h4>开胃菜</h4>
<ul>
<li>在讲之前，我们先补充一点基础知识，安卓 ImageView 支不支持加载 Gif 动图呢？其实是不支持的，因为 ImageView 本身就是一个 View，View 的绘制需要用 Canvas，而 Canvas 只支持 canvas.drawBitmap，也就是同一时间只能绘制一张位图，而 Gif 是由多帧图片组成，那么 Glide 是如何让 ImageView 实现播放 Gif 动图呢？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1282" data-height="172"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-4b98652e31d227d0.png" data-original-width="1282" data-original-height="172" data-original-format="image/png" data-original-filesize="134814" src="https://upload-images.jianshu.io/upload_images/6038844-4b98652e31d227d0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>还是从 Glide 给我们提供的写法来入手这块的源码</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1212" data-height="394"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-dbc48ff0667f8c90.png" data-original-width="1212" data-original-height="394" data-original-format="image/png" data-original-filesize="226251" src="https://upload-images.jianshu.io/upload_images/6038844-dbc48ff0667f8c90.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>一上来就发现了今天的主角：GifDrawable</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2324" data-height="448"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-bae46ce413e18cd7.png" data-original-width="2324" data-original-height="448" data-original-format="image/png" data-original-filesize="375595" src="https://upload-images.jianshu.io/upload_images/6038844-bae46ce413e18cd7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>确认过眼神，是想要的类</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1706" data-height="1428"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-a3ab422bd3329ae0.png" data-original-width="1706" data-original-height="1428" data-original-format="image/png" data-original-filesize="1082284" src="https://upload-images.jianshu.io/upload_images/6038844-a3ab422bd3329ae0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>那么问题来了，这个类有将近 500 多行代码，我们该从哪里看起？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2730" data-height="1618"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-99f5e844331c253d.png" data-original-width="2730" data-original-height="1618" data-original-format="image/png" data-original-filesize="1965153" src="https://upload-images.jianshu.io/upload_images/6038844-99f5e844331c253d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>这就跟看书类似，我们可以先看目录，在源码中也差不多，只不过它叫代码结构</li>
</ul>
<h4>源码解析</h4>
<ul>
<li>通过查看代码结构，我们发现了一个方法，从方法名上理解，它是开始播放第一帧的方法，那么我们就从这个方法入手</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1902" data-height="1590"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-40501062799d8a6a.png" data-original-width="1902" data-original-height="1590" data-original-format="image/png" data-original-filesize="1087256" src="https://upload-images.jianshu.io/upload_images/6038844-40501062799d8a6a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>我们可以看到当 Gif 只有一帧的时候，会直接调用绘制方法，而 Gif 不止一帧的时候，那么它就开启了订阅，接下来让我们看看这个订阅的方法里面做了什么事情</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1550" data-height="648"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-f1450f4172682780.png" data-original-width="1550" data-original-height="648" data-original-format="image/png" data-original-filesize="473352" src="https://upload-images.jianshu.io/upload_images/6038844-f1450f4172682780.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="746" data-height="440"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-612717127fb72c46.png" data-original-width="746" data-original-height="440" data-original-format="image/png" data-original-filesize="177366" src="https://upload-images.jianshu.io/upload_images/6038844-612717127fb72c46.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2092" data-height="1176"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-41faa351daf2b317.png" data-original-width="2092" data-original-height="1176" data-original-format="image/png" data-original-filesize="999347" src="https://upload-images.jianshu.io/upload_images/6038844-41faa351daf2b317.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>接下来让我们重点看一下这三句代码分别做了什么事</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1090" data-height="328"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-97d3f0d874c90809.png" data-original-width="1090" data-original-height="328" data-original-format="image/png" data-original-filesize="173039" src="https://upload-images.jianshu.io/upload_images/6038844-97d3f0d874c90809.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1542" data-height="276"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-21e7a7de01211e84.png" data-original-width="1542" data-original-height="276" data-original-format="image/png" data-original-filesize="172823" src="https://upload-images.jianshu.io/upload_images/6038844-21e7a7de01211e84.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>看到这里我们大概明白了，这个方法是用来递增帧位置的，从它的算法来看，这还是一个无限轮播的算法</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2106" data-height="1182"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-1b87da4a75486f31.png" data-original-width="2106" data-original-height="1182" data-original-format="image/png" data-original-filesize="1008930" src="https://upload-images.jianshu.io/upload_images/6038844-1b87da4a75486f31.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>看完了 advance 的作用，我们回去接着看剩下的两句代码</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1604" data-height="1292"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-d17f5c2a4198edc5.png" data-original-width="1604" data-original-height="1292" data-original-format="image/png" data-original-filesize="1002727" src="https://upload-images.jianshu.io/upload_images/6038844-d17f5c2a4198edc5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>是不是忽然有点蒙，这个类是什么，我们先看一下它的父类</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1792" data-height="1556"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-98892fd5abef00ba.png" data-original-width="1792" data-original-height="1556" data-original-format="image/png" data-original-filesize="1638885" src="https://upload-images.jianshu.io/upload_images/6038844-98892fd5abef00ba.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>是不是有点似曾相识，但就是怎么也说不出来什么，让我们先看看它的父类</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="3228" data-height="912"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-3a4eb4ad437cbb50.png" data-original-width="3228" data-original-height="912" data-original-format="image/png" data-original-filesize="1674217" src="https://upload-images.jianshu.io/upload_images/6038844-3a4eb4ad437cbb50.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>这个 Target 就是我们上篇讲到图片加载流程提到过的接口</p></li>
<li><p>这个接口的作用就是回调一些加载监听，这个接口前面三个方法分别是：加载开始、加载失败、加载成功读取资源的回调</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1628" data-height="1286"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-63e92fb8f97b2b8e.png" data-original-width="1628" data-original-height="1286" data-original-format="image/png" data-original-filesize="1005682" src="https://upload-images.jianshu.io/upload_images/6038844-63e92fb8f97b2b8e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>现在我们知道了这个是加载资源的回调，那么它又是从哪里调用的？</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2098" data-height="1188"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-cfc2cca16d632e07.png" data-original-width="2098" data-original-height="1188" data-original-format="image/png" data-original-filesize="993481" src="https://upload-images.jianshu.io/upload_images/6038844-cfc2cca16d632e07.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>就是在我们后面要讲的第三句代码里面调用的，真是让人意想不到</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1636" data-height="1258"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-7d8b8e088bfeeb9e.png" data-original-width="1636" data-original-height="1258" data-original-format="image/png" data-original-filesize="980723" src="https://upload-images.jianshu.io/upload_images/6038844-7d8b8e088bfeeb9e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>我们看到在加载资源的回调中发送了一个消息，那么这个消息最终是去了哪里，接下来让我们根据这个消息的 what 参数进行跟踪</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1300" data-height="942"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-9df4a2630f920b83.png" data-original-width="1300" data-original-height="942" data-original-format="image/png" data-original-filesize="689997" src="https://upload-images.jianshu.io/upload_images/6038844-9df4a2630f920b83.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>看到 handleMessage 忽然有了一种熟悉的味道，我们看到这里主要处理了两种消息，一种是延迟消息，一种是清理消息。接下来让我们先看看，如果这是一个延迟消息会发生什么事</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1756" data-height="1604"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-1cb6f1d4d8f5af91.png" data-original-width="1756" data-original-height="1604" data-original-format="image/png" data-original-filesize="1094055" src="https://upload-images.jianshu.io/upload_images/6038844-1cb6f1d4d8f5af91.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="798" data-height="240"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-bbd40d6d6fc8f5e0.png" data-original-width="798" data-original-height="240" data-original-format="image/png" data-original-filesize="115372" src="https://upload-images.jianshu.io/upload_images/6038844-bbd40d6d6fc8f5e0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1342" data-height="874"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-5ee0e87663106c06.png" data-original-width="1342" data-original-height="874" data-original-format="image/png" data-original-filesize="454269" src="https://upload-images.jianshu.io/upload_images/6038844-5ee0e87663106c06.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1790" data-height="698"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-d21134d8fac7d270.png" data-original-width="1790" data-original-height="698" data-original-format="image/png" data-original-filesize="478778" src="https://upload-images.jianshu.io/upload_images/6038844-d21134d8fac7d270.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>在这里我们看到，它会先获取当前帧数据，然后再通过 Canvas.drawBitmap 到 ImageView 上面，接下来我们回去刚刚那个方法里面，看看它还做了些什么</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1744" data-height="1598"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-eac3d94d580a4be1.png" data-original-width="1744" data-original-height="1598" data-original-format="image/png" data-original-filesize="1112567" src="https://upload-images.jianshu.io/upload_images/6038844-eac3d94d580a4be1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1346" data-height="906"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-a27beb617e0dfeb4.png" data-original-width="1346" data-original-height="906" data-original-format="image/png" data-original-filesize="678257" src="https://upload-images.jianshu.io/upload_images/6038844-a27beb617e0dfeb4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p>原来如此，它在刷新新的一帧数据到 ImageView 之后，会对旧的一帧数据进行清除</p></li>
<li><p>然后再回去继续看，它还做了什么事</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1756" data-height="1606"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-c6916c986b99ebc6.png" data-original-width="1756" data-original-height="1606" data-original-format="image/png" data-original-filesize="1115128" src="https://upload-images.jianshu.io/upload_images/6038844-c6916c986b99ebc6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2092" data-height="1210"><img data-original-src="//upload-images.jianshu.io/upload_images/6038844-82d8c8c5fd051adb.png" data-original-width="2092" data-original-height="1210" data-original-format="image/png" data-original-filesize="990990" src="https://upload-images.jianshu.io/upload_images/6038844-82d8c8c5fd051adb.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>还是原来的方法，还是熟悉的三句代码</li>
</ul>
<h4>总结</h4>
<ul>
<li>Glide 加载 Gif 的原理比较简单，就是将 Gif 解码成多张图片进行无限轮播，每帧切换都是一次图片加载请求，再加载到新的一帧数据之后会对旧的一帧数据进行清除，然后再继续下一帧数据的加载请求，以此类推，使用 Handler 发送消息实现循环播放。</li>
</ul>
<h4>下一篇：<a href="https://www.jianshu.com/p/03b6e71e9025" target="_blank">Glide 番外篇之判断图片的类型</a>
</h4>
<h4>Android技术讨论Q群：78797078</h4>
  
</div>
            