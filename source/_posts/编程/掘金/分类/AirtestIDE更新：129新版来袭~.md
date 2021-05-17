
---
title: 'AirtestIDE更新：1.2.9新版来袭~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f7b8d7231eb42d2aa70168c088bcc29~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 18:05:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f7b8d7231eb42d2aa70168c088bcc29~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>此文章来源于项目官方公众号：“AirtestProject”<br>
版权声明：允许转载，但转载必须保留原链接；请勿用作商业或者非法用途</p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p>本次更新为AirtestIDE更新，版本提升至1.2.9版本，另外airtest更新至1.1.11版本。更新详情如下：</p>
<h3 data-id="heading-1">更新详情</h3>
<h5 data-id="heading-2">1. 恢复查看iOS的unity-poco树的功能</h5>
<p>恢复了在IDE上查看iOS设备的unity-poco树的功能，mac或者是Windows平台上的IDE都支持。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f7b8d7231eb42d2aa70168c088bcc29~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是需要注意的是，目前 <strong>仅支持用USB线与本地相连的iOS设备</strong> 。</p>
<p>另外，如同学们的IDE使用了本地Python环境，则需要把本地Python环境里面的airtest库和pocoui库都更新到最新版本。</p>
<pre><code class="copyable">pip install -U airtest
pip install -U pocoui
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2.新手机初始化不需要再装RotationWatcher.apk</h5>
<p>之前同学们使用旧版的IDE连接新的安卓设备，初始化时会自动给设备安装上2个apk：</p>
<ul>
<li>Yosemite.apk</li>
<li>RotationWatcher.apk</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88a032206d24b5fa0977047547a8c40~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1.2.9版本的IDE初始化新设备时，将不再需要安装RotationWatcher.apk，仅需要装上Yosemite.apk即可：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81063984455b4d7ea678e2e2acdb54ba~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">3.支持使用rgb=True开启彩色识别</h5>
<p>新版IDE的airtest识别算法有所改进，能更好地识别指定了 <code>rgb=True</code> 这个参数的情况。我们可以直接双击IDE上的截图脚本，进入图片编辑器后勾上rgb选项：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8004bff1cfa94cca911b9ec2f7be9b2c~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者在IDE的脚本编辑窗口空白处单击右键，选择 <code>图片/代码模式切换</code> ，在 <code>Template</code> 里面添加 <code>rgb=True</code> 的参数：</p>
<pre><code class="copyable">touch(Template(r"tpl1619590322520.png", rgb=True, record_pos=(-0.118, 0.189), resolution=(1080, 1920)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>特别注意：使用旧版IDE的同学，尽管脚本中添加了 <code>rgb=True</code> 的参数，实际上是不生效的；代码放在新版IDE执行的话，<code>rgb=True</code> 的参数生效，识别结果会与旧版识别的结果相差比较大，请同学们根据自己脚本的实际情况修改参数。</p>
<h5 data-id="heading-5">4.poco辅助窗的UI树更新时间改成实时更新</h5>
<p>1.2.9版本IDE的poco辅助窗，UI树更新时间改成实时刷新，方便同学们查看当前的连接是否断开：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a8e3e5875c4ca8b44dd6ae6964125b~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-6">5.新版IDE截图时使用高清图片</h5>
<p>1.2.8版本截图时使用的图片比较模糊，但1.2.9版本使用高清图片截图。</p>
<h5 data-id="heading-7">6.修复部分情况下安卓10无法点击手机屏幕的问题</h5>
<p>修复了当安卓10手机开启了IDE自动录制功能时，关掉录制功能后，会再也无法点击手机屏幕，报错是主机终止了一个连接的问题。</p>
<p>还修复了在安卓10以上手机连接出画面的瞬间，立刻用鼠标去点屏幕，也非常容易出现无法用鼠标操作屏幕，必须重连才能成功初始化手机并进行点击操作的问题。</p>
<h5 data-id="heading-8">7.修复使用poco的inspector模式偶现报错的问题</h5>
<h5 data-id="heading-9">8.修复部分情况下IDE容易卡死的问题</h5>
<p>目前IDE的安卓手机如果在连接时直接拔掉，不再会卡死IDE了。</p>
<h3 data-id="heading-10">如何更新</h3>
<h5 data-id="heading-11">1. 官网下载</h5>
<p>同学们可以直接在我们的AirtestIDE官网上下载最新版本到本地电脑使用：<a href="http://airtest.netease.com/" target="_blank" rel="nofollow noopener noreferrer">airtest.netease.com/</a> 。</p>
<p>（部分Mac用户启动IDE时，如未收到新版本的更新弹窗，可以直接到我们官网上手动下载最新版本）</p>
<h5 data-id="heading-12">2. 旧版IDE检查更新</h5>
<p>对于使用1.2.5版本或者以上版本IDE的同学，重新打开IDE时即可看到更新消息，按指示更新即可。或者在IDE顶部菜单栏中，依次打开 <code>帮助--检查更新</code> 也可以获取最新本IDE的更新消息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e479556349c483dbd57c7f2c6fbc950~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>特别注意：Mac用户在覆盖更新版本之前，<strong>需要检查自己的脚本保存路径是否在AirtestIDE的路径之内</strong> ，如在的话，请备份脚本之后再进行覆盖更新；否则覆盖更新过程中，所有IDE路径之内的脚本都会丢失！！</p>
<hr>
<p><a href="https://juejin.cn/post/airtest.netease.com/">AirtestIDE下载</a>：airtest.netease.com/<br>
<a href="https://juejin.cn/post/airtest.doc.io.netease.com/">Airtest 教程官网</a>：airtest.doc.io.netease.com/<br>
<a href="https://juejin.cn/post/airlab.163.com/b2b">搭建企业私有云服务</a>：airlab.163.com/b2b</p>
<p>官方答疑 Q 群：654700783</p>
<p>呀，这么认真都看到这里啦，帮忙在文章左侧点一下点赞和收藏，给我一个支持把，灰常感谢~</p></div>  
</div>
            