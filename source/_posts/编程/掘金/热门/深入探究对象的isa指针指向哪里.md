
---
title: '深入探究对象的isa指针指向哪里'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93379f12361f4dc784313666d41df553~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 14 Mar 2021 04:28:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93379f12361f4dc784313666d41df553~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">首先我们之前知道isa的指针的指向结论是：</h2>
<h4 data-id="heading-1">1.instance对象的isa指向class对象</h4>
<h4 data-id="heading-2">2.clsaa对象的isa指向meta-class</h4>
<h4 data-id="heading-3">3.meta-class对象的isa指向基类的meta-class对象</h4>
<p>（<a href="https://www.jianshu.com/p/ce64c9429426" target="_blank" rel="nofollow noopener noreferrer">NSObject的isa和superclass区别</a>）</p>
<h4 data-id="heading-4">这篇博客，我们将探究isa指针指向哪里？并且会从代码层的内存地址证明isa指针的指向。</h4>
<p>首先instance对象的isa指针指向class对象，我们就可以创建一个instance对象</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93379f12361f4dc784313666d41df553~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面的截图运行结果可以看出stu的isa的0x001d8001000084e9 和GDStudent的isa的0x00000001000084e8并不一样，跟我们之前说的结果不一致？</p>
<p>其实啊，在arm64之前，也就是iPhone 5s之前其实是一致的，而在arm64以后它需要一个&位运算操作，需要stu的isa与ISA_MASK这个常量位运算一次，也就是</p>
<p>0x001d8001000084e9 & ISA_MASK ，现在我们苹果源码看一下ISA_MASK是什么东西，请看下面的截图</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/749b0fb74d0d4911915bf5325b70dda8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>需要这份源码的，请移步下载：<a href="https://opensource.apple.com/tarballs/" target="_blank" rel="nofollow noopener noreferrer">苹果源码下载地址</a></p>
<p>因为我们创建的是mac程序，所以我们复制下面的ISA_MASK位运算操作一次，请看下面的结果：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e549dc4abb34a04949466cd0c4f4e7a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从红色的结果是不是一摸一样，正好验证了instance对象的isa指针指向class对象！</p>
<p>此时是不是666！😄</p>
<h2 data-id="heading-5">2.clsaa对象的isa指向meta-class</h2>
<p>细心的同学可能可能发现我们无法输出classStu的isa，就像上面的绿色不是structure，我们点一下class的jump to Definition查看它的源码定义</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1ed4e86c0834c97a7822024c8acec99~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15cdee74c9194598a5a0e7ad680c509d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样我们看最后那种红色部分，确实是有个isa，此时怎么处理呢？我们可以定义一个一摸一样的结构体来替换一下class就行了如下代码：</p>
<p><strong>struct gd</strong>_objc_class &#123;</p>
<p>Class isa;</p>
<p>Class superclass;</p>
<p>&#125;;</p>
<p>objc_class前面加gd是防止重名，编译不通过，所以随便写啥都行</p>
<p>现在就可以验证了</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0db43f12e324170ae5aef61a088998b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样结果就是一摸一样可以验证了！</p>
<p>这样也是从代码层验证了</p>
<h2 data-id="heading-6">1.instance对象的isa指向class对象</h2>
<h2 data-id="heading-7">2.clsaa对象的isa指向meta-class</h2>
<h2 data-id="heading-8">3.meta-class对象的isa指向基类的meta-class对象</h2>
<p>接下来我将用代码证明</p>
<p>1.对象方法、属性、成员变量、协议信息存放在class对象中</p>
<p>2.类方法存放在meta-class对象中</p>
<p>3.成员变量的具体值是存放在instance对象中</p>
<h2 data-id="heading-9">如果觉得我写得对您有所帮助，请关注我，我会持续更新😄</h2></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            