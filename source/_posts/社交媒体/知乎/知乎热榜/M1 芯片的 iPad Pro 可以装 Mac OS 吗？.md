
---
title: 'M1 芯片的 iPad Pro 可以装 Mac OS 吗？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=538'
author: 知乎
comments: false
date: Wed, 21 Apr 2021 17:45:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=538'
---

<div>   
不减肥成功不改名的回答<br><br><p>我猜测Apple可能会在WWDC宣布iPadOS 15可以通过虚拟机的形式运行macOS。这应该</p><ul><li>比网上流传的双启动方案，对用户方便很多。</li><li>把iPadOS和macOS深度整合，让iPadOS跑Mac app，工程量很大。</li><li>也可以避免给macOS加入复杂的系统级触摸支持。</li></ul><p>说几个擦边的证据：</p><ul><li>M1芯片是支持硬件虚拟化的。之前我猜测A14X会直接砍掉这些东西，结果全保留了。</li><li>iPad Pro内存从6G直接飞跃到16GB。</li><li>之前有人发现<a href="http://link.zhihu.com/?target=https%3A//passthroughpo.st/mac-os-adds-early-support-for-virtio-qemu/" class=" wrap external" target="_blank" rel="nofollow noreferrer">Apple在macOS Mojave里测试虚拟机里面用的驱动</a>。目前的macOS是不能合法虚拟化的，所以用处何在？</li><li><a href="http://link.zhihu.com/?target=https%3A//9to5mac.com/2020/11/06/ios-14-2-brings-jit-compilation-support-which-enables-emulation-apps-at-full-performance/" class=" wrap external" target="_blank" rel="nofollow noreferrer">iOS 14.2允许第三方app JIT</a>。JIT是指程序在运行时动态生成原生代码，提高性能。桌面浏览器解释JavaScript都有用JIT；iOS上只有Safari/和WebKit进程支持。14.2之后普通app也可以了，但还不能上架App Store。</li></ul><p>这些加起来，iPadOS 15或许是可以跑macOS虚拟机的。不知道是作为系统功能，还是第三方app也可以，比如Parallels iPad？</p><ul><li>如果是前者的话，可能在连接外接显示器的时候可以用起来。也不需要给macOS加复杂的触摸支持了。</li><li>或者类似Sidecar，用Apple Pencil代替鼠标。</li><li>后者的话，如果谁都能拿到虚拟机的entitlement，或许开放JIT也就可以理解了。</li><li>放开JIT的话，苹果或许也会允许移动的Chrome/Edge，以应付反垄断官司。</li></ul><p>如果成真，iPad Pro作为轻中级Mac替代品会很棒，在星巴克想看书/Netflix也行，写码勉强也够——就是不知道续航能不能扛住——回家里插上Pro Display XDR，可以做严肃的开发。</p><p>一切静候六月。</p>  
</div>
            