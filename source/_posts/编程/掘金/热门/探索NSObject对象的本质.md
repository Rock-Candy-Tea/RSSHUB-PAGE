
---
title: '探索NSObject对象的本质'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b65e7cb9d0e042bb83edba02ff29947f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 14 Mar 2021 04:21:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b65e7cb9d0e042bb83edba02ff29947f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家在iOS面试的时候，是否遇到这样的面试题：一个NSObject对象占用多少内存？（我们知道不同的平台支持的代码肯定是不一样的，这里是讨论iOS下64bit （arm64））。</p>
<p>首先这个Objective-C的底层是C或者C++，然后是汇编语言，再然后是机器语言！</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b65e7cb9d0e042bb83edba02ff29947f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>首先我们用malloc_size函数来获取一下分配的内存大小</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2df3edd8416448abae194a31f4452a5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>答案是：16字节</p>
<p><strong>但是这个答案是怎么来的呢？我们来探究一下！</strong></p>
<p>首先底层既然是c++,我们把代码转换一下c++代码看一下底层实现</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50bb3d375369463b99c18a7909162fe8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里是代码实现，下面的main.arm64.cpp是main.m的c++底层实现，大家可以用终端执行下面的参照，2条红线的2条命令</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0659944c18364d9b9f337a75ec987214~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfac81497dd641839d20cbf04cf327c8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面用的代码</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4185365c5a7d4c89971331b8301aea2b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面我们用class_getInstanceSize这个函数来获取一下NSObject类的实例对象的大小</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d3d4f12734a46a7ab0a3f9f9ac246a2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从这里可以看出，实际NSObject对象实例大小只有8bit，但是分配了却是16bit。这是为什么呢？</p>
<h2 data-id="heading-0">二、利用lldb下的View Memory来佐证，实例大小是8bit，分配却是16bit</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7d90ad14f134c52b0c598bc760ee054~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">三、从开源源码上查看class_getInstanceSize</h2>
<p>首先我们可以从：<a href="https://opensource.apple.com/tarballs/" target="_blank" rel="nofollow noopener noreferrer">opensource.apple.com/tarballs/</a> 下载object的最新源码</p>
<p>下载下来打开搜索 class_getInstanceSize，然后打开项目</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b90550ac9b074f04b14decf4ea441bbd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b653ea90fc46435a84413e868fff5c69~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里就很明显可以看出，class_getInstanceSize是返回类的成员变量的大小，而nsobject只有一个isa指针，大小是8bit，所以class_getInstanceSize的打印是8bit</p>
<h2 data-id="heading-2">四、探索一下NSObject对象占用16bit是如何来的</h2>
<p>NSObject *obj = [[NSObject alloc]init]; 在objc上面搜索alloc的实现，其实alloc实现是调用allocWithZone，所以搜索一下,查找到最后</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac1117ffcda9416b8ed2b64a7163914b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从这里可以看出，只要size传的值小于16，就会返回16，我们这个对象的值是8，返回的是16，所以malloc_size的大小是16bit</p>
<h2 data-id="heading-3">结论：</h2>
<p>所以这道面试的答案，我认为这么写合适：</p>
<p>系统分配了16个字节给NSObject的对象（通过malloc_size函数获得）；</p>
<p>但是NSObject对象内部只使用了8个字节的空间（64bit环境下，可以通过class_getInstanceSize函数获得）</p>
<h1 data-id="heading-4">扩展提问：假如如下这三种情况，内存是如何分配呢？</h1>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372d98337b6e429fa6e9d2baeb19db8e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>请大家自己尝试😄！</p>
<p>附件代码下载链接：<a href="https://github.com/1084493818/NSObejc--day01" target="_blank" rel="nofollow noopener noreferrer">github.com/1084493818/…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            