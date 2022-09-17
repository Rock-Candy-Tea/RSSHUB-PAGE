
---
title: 'Flutter3.3打包iOS填坑记录'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/722723c225fc44c480ce523068b7eacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 18:46:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/722723c225fc44c480ce523068b7eacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>升级第三方库不可怕，可怕的是附送bug</p>
<p>有bug不可怕，可怕的是第一个吃螃蟹</p>
<p>第一个也不可怕，可怕的是大家都不分享</p>
</blockquote>
<h1 data-id="heading-0">一、 升级Flutter3.3</h1>
<p>太难得了，等了一个半月终于更新了，太期待能有新的性能提升，新的特性加入。使得能有更好的体验，更棒的开发效率。想要的有（1）Android Studio的自动完成，更加智能。（现在每次提示的，都不是我想要的）（2）页面的动画更加的流畅。（很多时间都是没有动画，感觉起来就是H5）（3）性能的优化。（More and More）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/722723c225fc44c480ce523068b7eacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="flutter3.3" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一时间更新到3.3.0，迫不及待的那种。开发（Android开发，然后适配下iOS），一切都是那么地Nice。当沾沾自喜没有附送新bug时，打包iOS提测却一直都是报错，报错的原因有了。但是这个错误好像是有提示，又好像没有。（打包2天才成功，所以值得我记录一下）</p>
<p>之后七天又发布了3.3.1，这个周期是正常合理了。可我有点不敢升级了。</p>
<h1 data-id="heading-1">二、 碰到了BUG</h1>
<p>开始适配iOS的时候，build都是失败的，一直在报错。</p>
<h3 data-id="heading-2">1. 找不到FlutterPluginRegistrant</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3688cc6686fe4f1889c7a63eab0c6f31~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="bug1" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>pod install</code>都是正常的。为啥突然就找不到了<code>FlutterPluginRegistrant</code>，之前一直都是好的。在swift中 <code>import FlutterPluginRegistrant</code>也试了，在<code>xx-Bridging-Header.h</code>中添加<code>#import "FlutterPluginRegistrant,h"</code>也试了，都是报错的。</p>
<h3 data-id="heading-3">2. Flutter的Frameworks为空</h3>
<p>找不到<code>FlutterPluginRegistrant</code>不可能吧。在Pods的Development Pods中找到FlutterPluginRegistant，在的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b89680a3cc3c48b38ed95778cea53c3c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="bug2" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那为啥找不到呢。 尝试着把<code>import FlutterPluginRegistrant</code>删除吧。看看会不会有啥报错。果然报错来了，找不到<code>#import <Flutter/Flutter.h></code>。这真的是一环扣一环啊。在上图中，可以清晰的看到<code>Flutter</code>中的<code>Frameworks</code>空空如也。是不是这个问题啊，是吗？</p>
<h3 data-id="heading-4">3. 怀疑Flutter加了新特性</h3>
<p>打开<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.cn%2Fdocs%2Fdevelopment%2Fadd-to-app%2Fios%2Fproject-setup" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.cn/docs/development/add-to-app/ios/project-setup" ref="nofollow noopener noreferrer">将 Flutter module 集成到 iOS 项目</a>看看吧，不出意外的话，一定是Flutter整了个啥了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f857672b1ed43a4a20f3b134f1baabf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="Flutter3.3新" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增了</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">post_install <span class="hljs-keyword">do</span> |<span class="hljs-params">installer</span>|
  flutter_post_install(installer) <span class="hljs-keyword">if</span> <span class="hljs-keyword">defined</span>?(flutter_post_install)
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大概率是这个原因了。将这句话，加入到Podfile的最下面，然后进行<code>pod install</code>。</p>
<h1 data-id="heading-5">三. 逼近真相</h1>
<h3 data-id="heading-6">1. 找不到targets</h3>
<p>在这个报错前，有一些其他的错误。（这些应该是我环境导致的，升级ruby和cocoapods后消失）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce0b0f0456224907b20206196d589777~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="targets" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在<code>podhelper.rb</code>中，找不到targets。这个看起来好眼熟啊。记得之前在添加<code>IPHONEOS_DEPLOYMENT_TARGET</code>和<code>EXCLUDED_ARCHS[sdk=iphonesimulator*</code>时，也一样用到了。</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">post_install <span class="hljs-keyword">do</span> |<span class="hljs-params">installer</span>|
  flutter_post_install(installer) <span class="hljs-keyword">if</span> <span class="hljs-keyword">defined</span>?(flutter_post_install)
  
  installer.pod_target_subprojects.flat_map &#123; |<span class="hljs-params">p</span>| p.targets &#125;.each <span class="hljs-keyword">do</span> |<span class="hljs-params">target</span>|
    target.build_configurations.each <span class="hljs-keyword">do</span> |<span class="hljs-params">c</span>|
      c.build_settings[<span class="hljs-string">'IPHONEOS_DEPLOYMENT_TARGET'</span>] = <span class="hljs-string">'11.0'</span>
      c.build_settings[<span class="hljs-string">"EXCLUDED_ARCHS[sdk=iphonesimulator*]"</span>] = <span class="hljs-string">"arm64"</span>
    <span class="hljs-keyword">end</span>
  <span class="hljs-keyword">end</span>
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那是不是可以如法炮制，干起来。</p>
<h3 data-id="heading-7">2. 修改podhelper.rb</h3>
<p>找到报错的地方</p>
<p><img src="https://tva1.sinaimg.cn/large/e6c9d24ely1h605m4atpjj20gx054q3g.jpg" alt="podhelper.rb" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将<code>installer.pods_project.targets.each do |target|</code>替换为<code>installer.pod_target_subprojects.flat_map &#123; |p| p.targets &#125;.each **do** |target|</code>.</p>
<p>回到项目目录中，执行<code>pod install</code>。报错消失了。</p>
<h3 data-id="heading-8">3. 成功</h3>
<p>一般就能正常debug和打包了。</p>
<p>如果碰到二般，那还是不行。那只能拿出杀手锏：</p>
<h5 data-id="heading-9">第一步. 清缓存</h5>
<p>（1）shift + commond + k 清理builder文件。
（2）清理DerivedData文件夹。</p>
<h5 data-id="heading-10">第二步. 重装pod</h5>
<p>将<code>Podfile.lock</code>和<code>Pods</code>这2个文件删除。再执行一次<code>pod install</code>。</p>
<hr>
<p>成功了，又没完全成功。正常运行到手机上了，可看着Xcode红红的报错，真的是表示很遗憾，这个锅不背。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fdbd53a6569452b90abd57992f4eade~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="遗憾" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">四. 题外</h1>
<p>开始怀疑是<code>cocoapods</code>不是最新版本，因为之前碰到过。也许是<code>ruby</code>不是最新版本呢。</p>
<p>最后通过升级ruby，重新安装cocoapods</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo gem install  -n /usr/local/bin cocoapods
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>pod</code>引起的问题消失。</p></div>  
</div>
            