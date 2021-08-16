
---
title: 'Swift 照片_视频选择器'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a90e141a7c148cd973ff0568d1f47ef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 01:09:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a90e141a7c148cd973ff0568d1f47ef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a90e141a7c148cd973ff0568d1f47ef~tplv-k3u1fbpfcp-watermark.image" alt="界面快照" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker" ref="nofollow noopener noreferrer">项目链接</a></p>
<h2 data-id="heading-0">功能</h2>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> UI 外观支持浅色/深色/自动/自定义</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持多选/混合内容选择</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持的媒体类型：</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Photo</li>
<li class="task-list-item"><input type="checkbox" checked disabled> GIF</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Live Photo</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Video</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持的本地资源类型：</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Photo</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Video</li>
<li class="task-list-item"><input type="checkbox" checked disabled> GIF</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持的网络资源类型：</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Photo</li>
<li class="task-list-item"><input type="checkbox" checked disabled> Video</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持下载iCloud上的资源</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持手势返回</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 支持滑动选择</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 编辑图片（支持动图、网络资源）</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 涂鸦</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 贴纸</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 文字</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 裁剪</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 马赛克</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 滤镜</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 编辑视频（支持网络资源）</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 配乐</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 裁剪</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 相册展现方式</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 单独列表</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 弹窗</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 多平台支持</li>
<li class="task-list-item"><input type="checkbox" checked disabled> iOS</li>
<li class="task-list-item"><input type="checkbox" checked disabled> iPadOS</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 国际化支持</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 英文 (en)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 简体中文 (zh-Hans)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 繁体中文 (zh-Hant)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 日语 (ja)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 韩语 (ko)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 泰语 (th)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 印尼语 (id)</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 自定义语言 (custom)</li>
</ul>
<h2 data-id="heading-1">要求</h2>
<ul>
<li>iOS 10.0+</li>
<li>Xcode 12.0+</li>
<li>Swift 5.3+</li>
</ul>
<h2 data-id="heading-2">安装</h2>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswift.org%2Fpackage-manager%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swift.org/package-manager/" ref="nofollow noopener noreferrer">Swift Package Manager</a></h3>
<p>⚠️ 需要 Xcode 12.0 及以上版本来支持资源文件/本地化文件的添加。</p>
<pre><code class="hljs language-swift copyable" lang="swift">dependencies: [
    .package(url: <span class="hljs-string">"https://github.com/SilenceLove/HXPHPicker.git"</span>, .upToNextMajor(from: <span class="hljs-string">"1.1.7"</span>))
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fguides.cocoapods.org%2Fusing%2Fusing-cocoapods.html" target="_blank" rel="nofollow noopener noreferrer" title="https://guides.cocoapods.org/using/using-cocoapods.html" ref="nofollow noopener noreferrer">CocoaPods</a></h3>
<p>将下面内容添加到 <code>Podfile</code>，并执行依赖更新。</p>
<pre><code class="hljs language-swift copyable" lang="swift">pod '<span class="hljs-type">HXPHPicker</span>'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCarthage%2FCarthage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Carthage/Carthage" ref="nofollow noopener noreferrer">Carthage</a></h3>
<p>将下面内容添加到 <code>Cartfile</code>，并执行依赖更新。</p>
<pre><code class="hljs language-swift copyable" lang="swift">github <span class="hljs-string">"SilenceLove/HXPHPicker"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">使用方法</h2>
<blockquote>
<p>我们在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fwiki" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/wiki" ref="nofollow noopener noreferrer">Wiki</a> 中提供了更详细的使用说明。</p>
</blockquote>
<h3 data-id="heading-7">准备工作</h3>
<p>按需在你的 Info.plist 中添加以下键值:</p>





























<table><thead><tr><th>Key</th><th>备注</th></tr></thead><tbody><tr><td>NSPhotoLibraryUsageDescription</td><td>允许访问相册</td></tr><tr><td>NSPhotoLibraryAddUsageDescription</td><td>允许保存图片至相册</td></tr><tr><td>PHPhotoLibraryPreventAutomaticLimitedAccessAlert</td><td>设置为 <code>YES</code> iOS 14+ 以禁用自动弹出添加更多照片的弹框(已适配 Limited 功能，可由用户主动触发，提升用户体验)</td></tr><tr><td>NSCameraUsageDescription</td><td>允许使用相机</td></tr><tr><td>NSMicrophoneUsageDescription</td><td>允许使用麦克风</td></tr></tbody></table>
<h3 data-id="heading-8">快速上手</h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">import</span> HXPHPicker

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">presentPickerController</span>()</span> &#123;
        <span class="hljs-comment">// 设置与微信主题一致的配置</span>
        <span class="hljs-keyword">let</span> config <span class="hljs-operator">=</span> <span class="hljs-type">PhotoTools</span>.getWXPickerConfig()
        <span class="hljs-keyword">let</span> pickerController <span class="hljs-operator">=</span> <span class="hljs-type">PhotoPickerController</span>.<span class="hljs-keyword">init</span>(picker: config)
        pickerController.pickerDelegate <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>
        <span class="hljs-comment">// 当前被选择的资源对应的 PhotoAsset 对象数组</span>
        pickerController.selectedAssetArray <span class="hljs-operator">=</span> selectedAssets 
        <span class="hljs-comment">// 是否选中原图</span>
        pickerController.isOriginal <span class="hljs-operator">=</span> isOriginal
        present(pickerController, animated: <span class="hljs-literal">true</span>, completion: <span class="hljs-literal">nil</span>)
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">PhotoPickerControllerDelegate</span> </span>&#123;
    
    <span class="hljs-comment">/// 选择完成之后调用</span>
    <span class="hljs-comment">/// - Parameters:</span>
    <span class="hljs-comment">///   - pickerController: 对应的 PhotoPickerController</span>
    <span class="hljs-comment">///   - result: 选择的结果</span>
    <span class="hljs-comment">///     result.photoAssets  选择的资源数组</span>
    <span class="hljs-comment">///     result.isOriginal   是否选中原图</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">pickerController</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">pickerController</span>: <span class="hljs-type">PhotoPickerController</span>, 
                            <span class="hljs-params">didFinishSelection</span> <span class="hljs-params">result</span>: <span class="hljs-type">PickerResult</span>)</span> &#123;
        result.getImage &#123; (image, photoAsset, index) <span class="hljs-keyword">in</span>
            <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> image <span class="hljs-operator">=</span> image &#123;
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"success"</span>, image)
            &#125;<span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"failed"</span>)
            &#125;
        &#125; completionHandler: &#123; (images) <span class="hljs-keyword">in</span>
            <span class="hljs-built_in">print</span>(images)
        &#125;
    &#125;
    
    <span class="hljs-comment">/// 点击取消时调用</span>
    <span class="hljs-comment">/// - Parameter pickerController: 对应的 PhotoPickerController</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">pickerController</span>(<span class="hljs-params">didCancel</span> <span class="hljs-params">pickerController</span>: <span class="hljs-type">PhotoPickerController</span>)</span> &#123;
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">更新日志</h2>















































<table><thead><tr><th>版本</th><th>发布时间</th><th>Xcode</th><th>Swift</th><th>iOS</th></tr></thead><tbody><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fblob%2Fmain%2FDocumentation%2FRELEASE_NOTE.md%23117" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/blob/main/Documentation/RELEASE_NOTE.md#117" ref="nofollow noopener noreferrer">v1.1.7</a></td><td>2021-08-06</td><td>12.5.1</td><td>5.3</td><td>10.0+</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fblob%2Fmain%2FDocumentation%2FRELEASE_NOTE.md%23116" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/blob/main/Documentation/RELEASE_NOTE.md#116" ref="nofollow noopener noreferrer">v1.1.6</a></td><td>2021-08-02</td><td>12.5.1</td><td>5.3</td><td>10.0+</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fblob%2Fmain%2FDocumentation%2FRELEASE_NOTE.md%23115" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/blob/main/Documentation/RELEASE_NOTE.md#115" ref="nofollow noopener noreferrer">v1.1.5</a></td><td>2021-07-28</td><td>12.5.1</td><td>5.3</td><td>10.0+</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fblob%2Fmain%2FDocumentation%2FRELEASE_NOTE.md%23114" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/blob/main/Documentation/RELEASE_NOTE.md#114" ref="nofollow noopener noreferrer">v1.1.4</a></td><td>2021-07-16</td><td>12.5.1</td><td>5.3</td><td>10.0+</td></tr><tr><td><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSilenceLove%2FHXPHPicker%2Fblob%2Fmain%2FDocumentation%2FRELEASE_NOTE.md%23113" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SilenceLove/HXPHPicker/blob/main/Documentation/RELEASE_NOTE.md#113" ref="nofollow noopener noreferrer">v1.1.3</a></td><td>2021-07-14</td><td>12.5.1</td><td>5.3</td><td>10.0+</td></tr></tbody></table>
<h2 data-id="heading-10">版权协议</h2>
<p>HXPHPicker 基于 MIT 协议进行分发和使用，更多信息参见<a href="https://link.juejin.cn/?target=.%2FLICENSE" target="_blank" title="./LICENSE" ref="nofollow noopener noreferrer">协议文件</a>。</p></div>  
</div>
            