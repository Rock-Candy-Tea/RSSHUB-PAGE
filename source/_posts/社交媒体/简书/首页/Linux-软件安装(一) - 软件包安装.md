
---
title: 'Linux-软件安装(一) - 软件包安装'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/11344802-5467e4912d4f9623.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/11344802-5467e4912d4f9623.png'
---

<div>   
<h2>1. 软件包分类</h2>
<ul>
<li>源码包</li>
<li>二进制包</li>
</ul>
<h2>2. 源码包</h2>
<h3>2.1 源码结构</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2187" data-height="1213"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-5467e4912d4f9623.png" data-original-width="2187" data-original-height="1213" data-original-format="image/png" data-original-filesize="216723" src="https://upload-images.jianshu.io/upload_images/11344802-5467e4912d4f9623.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">源码结构</div>
</div>
<h3>2.2 源码包特点</h3>
<p>源码包的优点是：</p>
<ul>
<li>开源，如果有足够的能力，可以修改源代码</li>
<li>可以自由选择所需的功能</li>
<li>软件是编译安装，所以更加适合自己的系统，更加稳定也效率更高</li>
<li>卸载方便</li>
</ul>
<p>源码包的缺点</p>
<ul>
<li>安装过程步骤较多，尤其安装较大的软件集合时（如 LAMP 环境搭建），容易出现拼写错误</li>
<li>编译过程时间较长，安装比二进制安装时间长</li>
<li>因为是编译安装，安装过程中一旦报错新手很难解决</li>
</ul>
<h3>2.3 二进制包</h3>
<h4>1.二进制包分类</h4>
<ul>
<li>DPKG 包：是由 Debian Linux 所开发出来的包管理机制，通过 DPKG 包，Debian Linux就可以进行软件包管理。主要应用在 Debian 和 unbuntu 中。</li>
<li>RPM 包：是由 Red Hat 公司所开发的包管理系统。功能强大，安装、升级、查询和卸载都非常简单和方便。目前很多 Linux 都在使用这种包管理方式，包括 Fedora、CentOS、SuSE 等。我们学习的是 CentOS 6.3，所以我们将要学习 RPM 包管理系统</li>
</ul>
<h4>2. 特点</h4>
<p><strong>RPM 包的优点:</strong></p>
<ul>
<li>包管理系统简单，只通过几个命令就可以实现包的安装、升级、查询和卸载</li>
<li>安装速度比源码包安装快的多</li>
</ul>
<p><strong>RPM 包的缺点:</strong></p>
<ul>
<li>经过编译，不再可以看到源代码</li>
<li>功能选择不如源码包灵活</li>
<li>依赖性。有时我们会发现需要安装软件包 a 时需要先安装 b 和 c，而安装 b 时需要安装d 和 e。这是需要先安装 d 和 e，再安装 b 和 c，最后才能安装 a 包。比如说，我买了个漂亮的灯具，打算安装到我们家客厅，可是在安装灯具之前我们家客厅总要有顶棚吧，顶棚总要是做好了防水和刷好油漆了吧，这个装修和安装软件其实类似总要有一定的顺序的。可是有时依赖性会非常繁琐</li>
</ul>
<h4>3. RPM 包依赖</h4>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="827" data-height="810"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-a23ffaa4399a4347.png" data-original-width="827" data-original-height="810" data-original-format="image/png" data-original-filesize="33443" src="https://upload-images.jianshu.io/upload_images/11344802-a23ffaa4399a4347.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>1）树形依赖      a---->b---->c<br>
2）环形依赖      a---->b---->c---->a<br>
3）函数库依赖<br>
<strong>模块依赖:</strong><br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2327" data-height="111"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-da2581c23b7cef35.png" data-original-width="2327" data-original-height="111" data-original-format="image/png" data-original-filesize="28762" src="https://upload-images.jianshu.io/upload_images/11344802-da2581c23b7cef35.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">模块依赖</div>
</div><p></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2376" data-height="289"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-6246ece612ccc57d.png" data-original-width="2376" data-original-height="289" data-original-format="image/png" data-original-filesize="81124" src="https://upload-images.jianshu.io/upload_images/11344802-6246ece612ccc57d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">模块依赖</div>
</div>
<p>发现报错，需要安装“<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flibodbc.so.2" target="_blank">libodbc.so.2</a>”函数库文件，这时会发现在光盘中根本找不到这个文件。那是因为函数库没有单独成包，是包含在某一个软件包中的。而如果要知道在哪个软件包中，需要查询网站<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fwww.rpmfind.net" target="_blank">www.rpmfind.net</a></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="820" data-height="407"><img data-original-src="//upload-images.jianshu.io/upload_images/11344802-b6e4cd696ccc15e4.png" data-original-width="820" data-original-height="407" data-original-format="image/png" data-original-filesize="169867" src="https://upload-images.jianshu.io/upload_images/11344802-b6e4cd696ccc15e4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
  
</div>
            