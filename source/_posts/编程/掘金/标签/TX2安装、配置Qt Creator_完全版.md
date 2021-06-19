
---
title: 'TX2安装、配置Qt Creator_完全版'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8896550c304f4b08a79da30ac1af2c41~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 17:22:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8896550c304f4b08a79da30ac1af2c41~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 查看TX2上Qt版本:终端运行</h2>
<pre><code class="hljs language-XML copyable" lang="XML">$ qmake --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出以下结果：
QMake version 3.0
Using Qt version 5.5.1 in /usr/lib/aarch64-linux-gnu</p>
<h2 data-id="heading-1">2. 安装对应版本qtcreator：终端运行</h2>
<pre><code class="hljs language-XML copyable" lang="XML">$ sudo apt-get install qt5-default qtcreator -y
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. 修改Qtcreator启动快捷方式，加载环境变量</h2>
<pre><code class="hljs language-XML copyable" lang="XML">$ cd /usr/share/applications/

$ sudo gedit qtcreator.desktop
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到Exec,加入bash -i -c :</p>
<p><code>Exec=bash -i -c qtcreator %F</code></p>
<p>最后大致如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8896550c304f4b08a79da30ac1af2c41~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">4. 配置Qt Creator on TX2</h2>
<ul>
<li>打开qt creator,依次选择Tools->Options->Build & Run->Compilers</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5255e9ac7c534cf2a5dd421e5b2cd764~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击<code>Add</code>按钮选择<code>GCC</code>。 在<code>Compiler path:’</code>中选择加入路径<code> /usr/bin/gcc</code>。并依次设置<code>ABI</code>的选项如下图所示:（<code>custom – arm – linux – generic – elf – 64 bit</code>）：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14e208eb0aa449f1bef33603baae0593~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>然后点击<code>Apply</code>按钮保存，然后点击<code>Kits</code>:</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc5c0fdc0a5b4f8fbea53db7b0c1ac2b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">- 继续点击<code>Add</code>按钮，按下图填写Name，Qt version, CMake Tool等信息，填好如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1ac96f8d8a1431ca6862e11bb9a8f5b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击<code>Apply</code>,然后点击<code>OK</code>，设置完毕。</li>
</ul>
<h2 data-id="heading-4">5. 简单测试---打开一个ros package:</h2>
<ul>
<li><code>Open Project</code>选中要打开ROS package的CMakeLists.txt文件，点击<code>Open</code>按钮。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/781214bd279a48a08be29bcabbdec282~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">- 然后,点击<code>Browse...</code>选择（或新建）build文件夹。我一般放在package下，也即与src文件夹平级。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/840935525c924e8287181ec7bc2a5a5b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击<code>Next</code>按钮:</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641e2046718747d1a3e3e75462e803c0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击<code>Run CMake</code>:</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4245c689ecf347fda97a3da567832b03~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>等运行完，<code>Finish</code>按钮由灰变成可选状态，点击<code>Finish</code>按钮，成功导入package。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1750c30f420a4d6eaa729a3633b8a553~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>现在，可以愉快的在TX2上与代码共舞啦！<strong><code>注：TX1可以模仿以上方式安装、配置、设置。</code></strong></li>
</ul>
<hr>
<p><strong>END</strong></p></div>  
</div>
            