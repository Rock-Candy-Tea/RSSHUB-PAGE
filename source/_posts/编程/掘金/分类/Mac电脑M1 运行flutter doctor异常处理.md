
---
title: 'Mac电脑M1 运行flutter doctor异常处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/165f08bc109a4f26a64a1f1c1c8770da~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 21:54:57 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/165f08bc109a4f26a64a1f1c1c8770da~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本人硬件设备：Mac电脑是M1芯片，
本人安装的Android studio 版本：4.2.2；
本人安装的flutter版本：1.17.1，由于开发需要，安装的是旧的flutter版本</p>
<ul>
<li>1、运行结果如下</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/165f08bc109a4f26a64a1f1c1c8770da~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-24 上午11.57.10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>2、Android license status unknow 问题解决如下</p>
<ul>
<li>
<p>终端运行flutter doctor --android-licenses命令：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b75a3351ea0457280d882aae4fe7892~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>解决报错如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/445e8f8d911346c6bfdeacc1a21620c7~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_4.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>再次运行结果如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83dc7856db81425cb09c920f0348a8ed~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_6.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>3、解决实际上已经在安装了Flutter和Dart插件，运行flutter doctor事却报插件未安装的错误，</p>
<ul>
<li>
<p>这个错误是Android studio 4.1以后的版本插件的插件位置改变了，而我装的旧版本的flutter仍然按照旧版本的Android studio插件路径去查找，因此找不到报未安装，解决这个问题需要将我们安装的plugins文件按照旧的路径创建拷贝，可以自己手动去拷贝，也可以执行以下终端命令 ,注意将对应的AndroidStudio4.2,AndroidStudio4.1等版本替换成你自己安装的版本</p>
</li>
<li>
<p>终端命令：<strong>ln -s ~/Library/Application\ Support/Google/AndroidStudio4.2/plugins ~/Library/Application\ Support/AndroidStudio4.2</strong></p>
</li>
<li>
<p><em>4.1后的新版本插件位置</em>：<strong>~/Library/Application\ Support/Google/AndroidStudio4.1/plugins</strong></p>
</li>
<li>
<p><em>老版本插件路径</em>：<strong>~/Library/Application\ Support/AndroidStudio4.1</strong></p>
</li>
<li>
<p>再次运行flutter doctor 结果如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062d3006bc0549d5af9654e052363083~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_7.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>4、解决 No devices available问题
解决：手动打开Xcode的模拟器，或者执行终端命令：open -a Simulator，打开模拟器即可</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b94a68981164400b2da0609f8ae7a3e~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>重新运行lutter doctor 结果如下</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2bca9ddf1e451aacb67f5a2828a522~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210724_10.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
</ul></div>  
</div>
            