
---
title: 'AOSP 源码导入 Android Studio'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51abb6b44dd4068a303f3680430df10~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 02:11:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51abb6b44dd4068a303f3680430df10~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>前一篇文章<a href="https://juejin.cn/post/6969209217760624670" target="_blank">AOSP 源码环境搭建</a>我们已经将AOSP整个源码down到了我们硬盘。接下来我们就要Read The Fucking Source Code !</p>

<h2 data-id="heading-1">准备工作</h2>
<p>原理</p>
<p>idegen专门为IDE环境调试源码而设计的工具，所以我们要将工程导入AS需要下面三个步骤</p>
<ol>
<li>获取到idegen.jar</li>
<li>获取idegen.sh 执行生成android.ipr/android.iml</li>
<li>Android sutdio 选择android.ipr导入</li>
</ol>
<p>不想编译整个AOSP源码的，对于idegen.jar以及idegen.sh 获取可以参考<a href="https://lingdage.com/posts/ca9841f5.html" target="_blank" rel="nofollow noopener noreferrer">AOSP frameworks 源码环境搭建</a></p>
<p>下面讲下完整版的</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">cd</span> ～/aosp //具体的源码根目录

//用于初始化环境变量
<span class="hljs-built_in">source</span> build/envsetup.sh  

//生成文件out/host/linux-x86/framework/idegen.jar 注意要在bash下 zsh会有问题
mmm development/tools/idegen/  

//源码根目录生成文件android.ipr(工程相关设置), android.iml(模块相关配置)
./development/tools/idegen/idegen.sh  

//改成可读可写，否则，在更改一些项目配置的时候可能会出现无法保存的情况
sudo chmod 777 android.iml
sudo chmod 777 android.ipr
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>m/mm/mmm/make 相关参考<a href="https://blog.csdn.net/Luoshengyang/article/details/19023609" target="_blank" rel="nofollow noopener noreferrer">Android源代码编译命令m/mm/mmm/make分析</a></p>
</blockquote>
<p>todo</p>
<p><a href="https://blog.csdn.net/mcryeasy/article/details/60466837" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/mcryeasy/ar…</a></p>
<p>如何阅读 <a href="https://wiki.lineageos.org/import-android-studio-howto.html" target="_blank" rel="nofollow noopener noreferrer">wiki.lineageos.org/import-andr…</a></p>
<h2 data-id="heading-2">导入源码</h2>
<p>打开Android Studio， 点击<code>File</code> -> <code>Open</code>，选中前面生成的<strong>android.ipr</strong>文件即可， 该过程较耗时</p>
<h3 data-id="heading-3">加载前配置文件提速</h3>
<p>打开<code>android.iml</code>文件，有大量excludeFolder，是指不会导入到AS的模块，默认除了以下14个文件夹之外的所有文件都会导致到AS工程， 这显然还会非常庞大的，那么我们可以有选择的导入 如下：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">excludeFolder</span> <span class="hljs-attr">url</span>=<span class="hljs-string">"file://$MODULE_DIR$/.repo"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">excludeFolder</span> <span class="hljs-attr">url</span>=<span class="hljs-string">"file://$MODULE_DIR$/external/bluetooth"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">excludeFolder</span> <span class="hljs-attr">url</span>=<span class="hljs-string">"file://$MODULE_DIR$/frameworks/base/docs"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">excludeFolder</span> <span class="hljs-attr">url</span>=<span class="hljs-string">"file://$MODULE_DIR$/out/host"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">excludeFolder</span> <span class="hljs-attr">url</span>=<span class="hljs-string">"file://$MODULE_DIR$/prebuilt"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">加载后提速</h3>
<p>如果已经把全部项目导入到Android Studio，又想删除怎么办，其实有一个简单的方法就是进入目录<code>Project Structure</code> -> <code>Modules</code>， 可快速去除某些模块, 其中红色代码Exclueded选项(即代表已删除的目录), 如下图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f51abb6b44dd4068a303f3680430df10~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">配置源码正确跳转</h3>
<p>这里的配置JDK/SDK，是用于解决在分析和调试源码的过程，能正确地跳转到目标源码，而非SDK中的代码。 点击<code>File</code>菜单下的<code>Project Structure</code>.</p>
<h4 data-id="heading-6">新建JDK(No Libraries)</h4>
<ol>
<li>新建JDK(No Libraries),路径可选择之前的一样的</li>
<li>删除JDK(No Libraries)中的ClassPath和SourcePath</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a122273a75864da2bb13bb163fef9013~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">配置SDK</h4>
<p>Project Structure -> SDKs, 选中<code>Android API 28 Platform</code>, 然后选择其Java SDK为前面新建的<code>JDK(No Libraries)</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2647821b8bc548f095add51f29945437~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">选择SDK</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b880867e704ed3bf4f5b435ad49fa9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">建立依赖</h4>
<p>Project Structure -> Modules -> android -> Dependencies: 先删除Android API 25 Platform之外的所有依赖, 然后点击下图绿色的<code>+</code>号来选择<code>Jars or directories</code>，将frameworks添加进来, 也可添加其他所关注的源码；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5247fe824b9741b4bf17c67ee0f24246~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">调试</h2>
<p>前面已搭建好了Android的源码调试环境, 接下来可以在线调试源码. 首先,需要一台具有debug版的手机, 打开开发者选项, 允许USB调试.</p>
<p>frameworks各大核心服务运行在system_server进程, 在调试器上名字为system_process,通过attach到我们要调试的目标进程, 同理, 要调试其他app进程也是这个方式.</p>
<h2 data-id="heading-11">参考</h2>
<p><a href="http://gityuan.com/2016/08/13/android-os-env" target="_blank" rel="nofollow noopener noreferrer">AndroidStudio源码开发环境搭建</a></p></div>  
</div>
            