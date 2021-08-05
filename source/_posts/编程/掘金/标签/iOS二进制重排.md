
---
title: 'iOS二进制重排'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ce91e83ad274f33bd97832149d30dcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 01:00:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ce91e83ad274f33bd97832149d30dcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>一、概念</strong></p>
<p>项目中将启动时需要调用的函数放到一起 ( 比如 <code>前10页</code>中 ) 以尽可能减少 <code>page fault</code> , 达到优化目的 . 而这个做法就叫做 <code>二进制重排</code> </p>
<p>**<br>
**</p>
<p><strong>二、原理</strong></p>
<ul>
<li>首先 , <code>Xcode</code> 是用的链接器叫做 <code>ld</code> , <code>ld</code> 有一个参数叫 <code>Order File</code> , 我们可以通过这个参数配置一个 <code>order</code> 文件的路径 .</li>
<li>在这个 <code>order</code> 文件中 , 将你需要的符号按顺序写在里面 .</li>
<li>当工程 <code>build</code> 的时候 , <code>Xcode</code> 会读取这个文件 , 打的二进制包就会按照这个文件中的符号顺序进行生成对应的 <code>mach-O</code></li>
</ul>
<p>\</p>
<p><strong>三、如何查看自己工程的符号顺序</strong></p>
<p>重排前后我们需要查看自己的符号顺序有没有修改成功 , 这时候就用到了 <code>Link Map</code> </p>
<p>\</p>
<p><code>Link Map</code> 是编译期间产生的产物 , ( ld 的读取二进制文件顺序默认是按照 <code>Compile Sources</code> - <code>GUI</code> 里的顺序 ) , 它记录了二进制文件的布局 .</p>
<p>通过设置 <code>Write Link Map File</code> 来设置输出与否 , 默认是 <code>no</code> .</p>
<p>如下图将 Write Link Map File设置为YES</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ce91e83ad274f33bd97832149d30dcd~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改完毕后 <code>clean</code> 一下 , 运行工程 , <code>Products</code> - <code>show in finder</code>, 如下图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/333a016601324d028b1f44310dc944c4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图找到.txt文件</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6d4f0560c29475f94b9b10479908125~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开上图中的.txt文件如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce22f9c68a44adda70a6eb727aa3ce4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 , 这个符号顺序明显是按照 <code>Compile Sources</code> 的文件顺序来排列的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ec8fd5926b44eb08d6e7163a2a701a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>四、具体如何实现二进制的重排</strong></p>
<p><strong>4.1</strong></p>
<p>来到工程根目录 , 新建一个文件 my_oder.order ， 随便挑选几个启动时就需要加载的方法 (我以ViewController中的方法举例子),</p>
<p>my_oder.order 文件如下图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e83749f46f1a43b0a4311b7b8cf779ce~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ViewController中的方法如下图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1be64b95fa2418d9416b03d84bcc6bf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>4.2 配置oder file文件路径 ，如下图</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93be541e680b4f8aa33ca8f72bc7e041~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>4.3重新运行 , 查看 <strong>工程的符号顺序</strong></strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d15c4c78d0d14744975f41c657f9ad09~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 , 我们所写的这三个方法已经被放到最前面了 , 至此 ,</p>
<p>生成的 <code>macho</code> 中距离首地址偏移量最小的代码就是我们所写的这三个方法 ,</p>
<p>假设这三个方法原本在不同的三页 , 那么我们就已经优化掉了两个 <code>page fault.</code></p>
<p><strong>以上就是二进制重排的实现</strong></p></div>  
</div>
            