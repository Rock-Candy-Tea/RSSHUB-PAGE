
---
title: 'LockSupport都不知道，怎么拿offer？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<p>LockSupport是一个编程工具类，主要是为了阻塞和唤醒线程用的。使用它我们可以实现很多功能，今天主要就是对这个工具类的讲解，希望对你有帮助：</p>
<p><strong>一、LockSupport简介</strong></p>
<p><strong>1、LockSupport是什么</strong></p>
<p>刚刚开头提到过，LockSupport是一个线程工具类，所有的方法都是静态方法，可以让线程在任意位置阻塞，也可以在任意位置唤醒。</p>
<p>它的内部其实两类主要的方法：park（停车阻塞线程）和unpark（启动唤醒线程）。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="476" data-height="281"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-a57f503a359d0323" data-original-width="476" data-original-height="281" data-original-format="image/jpeg" data-original-filesize="28116" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>注意上面的123方法，都有一个blocker，这个blocker是用来记录线程被阻塞时被谁阻塞的。用于线程监控和分析工具来定位原因的。</p>
<p>现在我们知道了LockSupport是用来阻塞和唤醒线程的，而且之前相信我们都知道wait/notify也是用来阻塞和唤醒线程的，那么它相比，LockSupport有什么优点呢？</p>
<p><strong>2、与wait/notify对比</strong></p>
<p>这里假设你已经了解了wait/notify的机制，如果不了解，可以在网上一搜，很简单。相信你既然学到了这个LockSupport，相信你已经提前已经学了wait/notify。</p>
<p>我们先来举一个使用案例：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="476" data-height="316"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-3572175f0b5dd3e3" data-original-width="476" data-original-height="316" data-original-format="image/jpeg" data-original-filesize="24901" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>上面这段代码的意思是，我们定义一个线程，但是在内部进行了park，因此需要unpark才能唤醒继续执行，不过上面，我们在MyThread进行的park，在main线程进行的unpark。</p>
<p>这样来看，好像和wait/notify没有什么区别。那他的区别到底是什么呢？这个就需要仔细的观察了。这里主要有两点：</p>
<p>（1）wait和notify都是Object中的方法,在调用这两个方法前必须先获得锁对象，但是park不需要获取某个对象的锁就可以锁住线程。</p>
<p>（2）notify只能随机选择一个线程唤醒，无法唤醒指定的线程，unpark却可以唤醒一个指定的线程。</p>
<p>区别就是这俩，还是主要从park和unpark的角度来解释的。既然这个LockSupport这么强，我们就深入一下他的源码看看。</p>
<p><strong>二、源码分析（基于jdk1.8）</strong></p>
<p><strong>1、park方法</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="336" data-height="120"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-402c1ddd08c8bca0" data-original-width="336" data-original-height="120" data-original-format="image/jpeg" data-original-filesize="8712" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>blocker是用来记录线程被阻塞时被谁阻塞的。用于线程监控和分析工具来定位原因的。setBlocker(t, blocker)方法的作用是记录t线程是被broker阻塞的。因此我们只关注最核心的方法，也就是UNSAFE.park(false, 0L)。</p>
<p>UNSAFE是一个非常强大的类，他的的操作是基于底层的，也就是可以直接操作内存，因此我们从JVM的角度来分析一下：</p>
<p>每个java线程都有一个Parker实例：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="411" data-height="281"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-d1bb6b7f565d804b" data-original-width="411" data-original-height="281" data-original-format="image/jpeg" data-original-filesize="14259" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>我们换一种角度来理解一下park和unpark，可以想一下，unpark其实就相当于一个许可，告诉特定线程你可以停车，特定线程想要park停车的时候一看到有许可，就可以立马停车继续运行了。因此其执行顺序可以颠倒。</p>
<p>现在有了这个概念，我们体会一下上面JVM层面park的方法，这里面counter字段，就是用来记录所谓的“许可”的。</p>
<p>本文部分总结来源于：<a href="https://www.jianshu.com/p/1f16b838ccd8" target="_blank">https://www.jianshu.com/p/1f16b838ccd8</a></p>
<p>当调用park时，先尝试直接能否直接拿到“许可”，即_counter>0时，如果成功，则把_counter设置为0,并返回。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="490" data-height="154"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-1dd6fe9bb3251c3d" data-original-width="490" data-original-height="154" data-original-format="image/jpeg" data-original-filesize="14872" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>如果不成功，则构造一个ThreadBlockInVM，然后检查_counter是不是>0，如果是，则把_counter设置为0，unlock mutex并返回:</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="332" data-height="105"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-82557b274473ed3f" data-original-width="332" data-original-height="105" data-original-format="image/jpeg" data-original-filesize="6836" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>否则，再判断等待的时间，然后再调用pthread_cond_wait函数等待，如果等待返回，则把_counter设置为0，unlock mutex并返回：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="389" data-height="140"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-50917d32cbc83ffa" data-original-width="389" data-original-height="140" data-original-format="image/jpeg" data-original-filesize="10884" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>这就是整个park的过程，总结来说就是消耗“许可”的过程。</p>
<p><strong>2、unpark</strong></p>
<p>还是先来看一下JDK源码：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="557" data-height="279"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-eae3b8eac3a4da08" data-original-width="557" data-original-height="279" data-original-format="image/jpeg" data-original-filesize="20893" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>上面注释的意思是给线程生产许可证。</p>
<p>当unpark时，则简单多了，直接设置_counter为1，再unlock mutext返回。如果_counter之前的值是0，则还要调用pthread_cond_signal唤醒在park中等待的线程：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="425" data-height="423"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-989e9ba488e9d926" data-original-width="425" data-original-height="423" data-original-format="image/jpeg" data-original-filesize="28800" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>ok，现在我们已经对源码进行了分析，整个过程其实就是生产许可和消费许可的过程。而且这个生产过程可以反过来。也就是先生产再消费。下面我们使用几个例子验证一波。</p>
<p><strong>三、LockSupport使用</strong></p>
<p><strong>1、先interrupt再park</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="640" data-height="324"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-a73dc77f0a77bbdc" data-original-width="640" data-original-height="324" data-original-format="image/jpeg" data-original-filesize="27030" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>我们看一下结果：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="457" data-height="175"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-1ff1aee3ad0431b7" data-original-width="457" data-original-height="175" data-original-format="image/jpeg" data-original-filesize="20716" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><strong>2、先unpark再park</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="435" data-height="248"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-e81e970063c51e6b" data-original-width="435" data-original-height="248" data-original-format="image/jpeg" data-original-filesize="14997" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>我们只需在park之前先休眠1秒钟，这样可以确保unpark先执行。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="428" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/4153190-33a57115dc5448e1" data-original-width="428" data-original-height="200" data-original-format="image/jpeg" data-original-filesize="21457" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>OK，今天的文章先写到这，如有问题，还请批评指正。</p>
  
</div>
            