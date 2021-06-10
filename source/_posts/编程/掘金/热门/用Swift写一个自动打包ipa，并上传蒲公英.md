
---
title: '用Swift写一个自动打包ipa，并上传蒲公英'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e844f956a1304ac19d939bf8a506ad29~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 00:00:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e844f956a1304ac19d939bf8a506ad29~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">在项目中看到以前同事写的自动打包并上传蒲公英脚本，就萌发了用原生swift或者OC可不可以编写脚本的想法。查阅相关资料后发现是可行的。</h5>
<h2 data-id="heading-1">1、Process是一个可以执行终端命令的类</h2>
<p>我们给<code>Process</code>扩展一个便捷方法执行终端命令</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">Process</span> </span>&#123;
    
    <span class="hljs-comment">/// 执行命令</span>
    <span class="hljs-comment">/// - Parameters:</span>
    <span class="hljs-comment">///   - launchPath: 命令路径</span>
    <span class="hljs-comment">///   - arguments: 命令参数</span>
    <span class="hljs-comment">///   - currentDirectoryPath: 命令执行目录</span>
    <span class="hljs-comment">///   - environment: 环境变量</span>
    <span class="hljs-comment">/// - Returns: 返回执行结果</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">executable</span>(<span class="hljs-params">launchPath</span>:<span class="hljs-type">String</span>,
                           <span class="hljs-params">arguments</span>:[<span class="hljs-type">String</span>],
                           <span class="hljs-params">currentDirectoryPath</span>:<span class="hljs-type">String</span>? <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>,
                           <span class="hljs-params">environment</span>:[<span class="hljs-params">String</span>:<span class="hljs-type">String</span>]<span class="hljs-operator">?</span> <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>)</span>-><span class="hljs-type">Pipe</span>&#123;
        <span class="hljs-keyword">let</span> process <span class="hljs-operator">=</span> <span class="hljs-type">Process</span>()
        process.launchPath <span class="hljs-operator">=</span> launchPath
        process.arguments <span class="hljs-operator">=</span> arguments
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> environment <span class="hljs-operator">=</span> environment &#123;
            process.environment <span class="hljs-operator">=</span> environment
        &#125;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">let</span> currentDirectoryPath <span class="hljs-operator">=</span> currentDirectoryPath &#123;
            process.currentDirectoryPath <span class="hljs-operator">=</span> currentDirectoryPath
        &#125;
        <span class="hljs-keyword">let</span> pipe <span class="hljs-operator">=</span> <span class="hljs-type">Pipe</span>()
        process.standardOutput <span class="hljs-operator">=</span> pipe
        process.launch()
        <span class="hljs-keyword">return</span> pipe
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2、xcodebuild命令</h2>
<ol>
<li>
<h4 data-id="heading-3"><strong>Clean</strong></h4>
<pre><code class="copyable">xcodebuild clean
           -workspace <workspaceName>
           -scheme <schemeName>
           -configuration <Debug|Release>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-4"><strong>Archive</strong></h4>
<pre><code class="copyable">xcodebuild archive 
           -archivePath <archivePath>
           -project <projectName>
           -workspace <workspaceName>
           -scheme <schemeName> 
           -configuration <Debug|Release>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 data-id="heading-5"><strong>Export</strong></h4>
<pre><code class="copyable">xcodebuild -exportArchive
           -archivePath <xcarchivepath>
           -exportPath <destinationpath>
           -exportOptionsPlist <plistpath>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>参考文章：<a href="https://www.cnblogs.com/liuluoxing/p/8622108.html" target="_blank" rel="nofollow noopener noreferrer">xcodebuild命令介绍</a></p>
<h1 data-id="heading-6">3、使用 SPM 搭建开发或者直接使用xcode的创建一个命令行程序项目</h1>
<pre><code class="copyable">$ mkdir SwiftCommandLineTool
$ cd SwiftCommandLineTool
$ swift package init --type executable
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一行的 <code>type executable</code> 参数将告诉 SPM，我们想创建一个 CLI，而不是一个 Framework。</p>
<ol>
<li>
<p>封装一个打包上传相关的工具</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">String</span></span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">appPath</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">value</span>:<span class="hljs-type">String</span>)</span> -> <span class="hljs-type">String</span> &#123;
        <span class="hljs-keyword">if</span> <span class="hljs-keyword">self</span>.hasSuffix(<span class="hljs-string">"/"</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span> <span class="hljs-operator">+</span> value
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">self</span> <span class="hljs-operator">+</span> <span class="hljs-string">"/"</span> <span class="hljs-operator">+</span> value
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">IpaTool</span> </span>&#123;
    
    <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Output</span> </span>&#123;
        <span class="hljs-keyword">var</span> pipe:<span class="hljs-type">Pipe</span>
        <span class="hljs-keyword">var</span> readData:<span class="hljs-type">String</span>
        <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">pipe</span>:<span class="hljs-type">Pipe</span>)</span> &#123;
            <span class="hljs-keyword">self</span>.pipe <span class="hljs-operator">=</span> pipe
            <span class="hljs-keyword">self</span>.readData <span class="hljs-operator">=</span> <span class="hljs-type">String</span>(data: pipe.fileHandleForReading.readDataToEndOfFile(), encoding: <span class="hljs-type">String</span>.<span class="hljs-type">Encoding</span>.utf8) <span class="hljs-operator">??</span> <span class="hljs-string">""</span>
        &#125;
    &#125;
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Configuration</span>:<span class="hljs-title">String</span> </span>&#123;
        <span class="hljs-keyword">case</span> debug <span class="hljs-operator">=</span> <span class="hljs-string">"Debug"</span>
        <span class="hljs-keyword">case</span> release <span class="hljs-operator">=</span> <span class="hljs-string">"Release"</span>
    &#125;
    
    <span class="hljs-keyword">var</span> workspace:<span class="hljs-type">String</span>&#123;
        projectPath.appPath(<span class="hljs-string">"<span class="hljs-subst">\(projectName)</span>.xcworkspace"</span>)
    &#125;
    <span class="hljs-comment">///scheme</span>
    <span class="hljs-keyword">var</span> scheme:<span class="hljs-type">String</span>
    <span class="hljs-comment">///Debug|Release</span>
    <span class="hljs-keyword">var</span> configuration:<span class="hljs-type">Configuration</span>
    <span class="hljs-comment">///编译产物路径</span>
    <span class="hljs-keyword">var</span> xcarchive:<span class="hljs-type">String</span>&#123;
        exportIpaPath.appPath(<span class="hljs-string">"<span class="hljs-subst">\(projectName)</span>.xcarchive"</span>)
    &#125;
    <span class="hljs-comment">///配置文件路径</span>
    <span class="hljs-keyword">var</span> exportOptionsPlist:<span class="hljs-type">String</span>
    <span class="hljs-comment">///导出ipa包的路径</span>
    <span class="hljs-keyword">var</span> exportIpaPath:<span class="hljs-type">String</span>
    <span class="hljs-comment">///项目路径</span>
    <span class="hljs-keyword">let</span> projectPath:<span class="hljs-type">String</span>
    <span class="hljs-comment">///项目名称</span>
    <span class="hljs-keyword">let</span> projectName:<span class="hljs-type">String</span>
    <span class="hljs-comment">///存放打包目录</span>
    <span class="hljs-keyword">let</span> packageDirectory:<span class="hljs-type">String</span>
    <span class="hljs-comment">///蒲公英_api_key</span>
    <span class="hljs-keyword">let</span> pgyerKey:<span class="hljs-type">String</span>
    
    <span class="hljs-comment">///</span>
    <span class="hljs-comment">/// - Parameters:</span>
    <span class="hljs-comment">///   - projectPath: 项目路径</span>
    <span class="hljs-comment">///   - configuration: Debug|Release</span>
    <span class="hljs-comment">///   - exportOptionsPlist: 配置文件Plist的路径</span>
    <span class="hljs-comment">///   - pgyerKey: 上传蒲公英的key</span>
    <span class="hljs-comment">/// - Throws: 抛出错误</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">projectPath</span>:<span class="hljs-type">String</span>,
      <span class="hljs-params">configuration</span>:<span class="hljs-type">Configuration</span>,
      <span class="hljs-params">exportOptionsPlist</span>:<span class="hljs-type">String</span>,
      <span class="hljs-params">pgyerKey</span>:<span class="hljs-type">String</span>)</span> <span class="hljs-keyword">throws</span> &#123;
     <span class="hljs-keyword">self</span>.projectPath <span class="hljs-operator">=</span> projectPath
     <span class="hljs-keyword">self</span>.configuration <span class="hljs-operator">=</span> configuration
     <span class="hljs-keyword">self</span>.exportOptionsPlist <span class="hljs-operator">=</span> exportOptionsPlist
     <span class="hljs-keyword">self</span>.pgyerKey <span class="hljs-operator">=</span> pgyerKey
     <span class="hljs-keyword">let</span> manager <span class="hljs-operator">=</span> <span class="hljs-type">FileManager</span>.default
     <span class="hljs-keyword">var</span> allFiles <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> manager.contentsOfDirectory(atPath: projectPath)
     projectName <span class="hljs-operator">=</span> allFiles.first(where: &#123; <span class="hljs-variable">$0</span>.hasSuffix(<span class="hljs-string">".xcodeproj"</span>)  &#125;)<span class="hljs-operator">?</span>.components(separatedBy: <span class="hljs-string">"."</span>).first <span class="hljs-operator">??</span> <span class="hljs-string">""</span>
     packageDirectory <span class="hljs-operator">=</span> <span class="hljs-type">NSHomeDirectory</span>()
         .appPath(<span class="hljs-string">"Desktop/<span class="hljs-subst">\(projectName)</span>_ipa"</span>)
     
     allFiles <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> manager.contentsOfDirectory(atPath: projectPath.appPath(<span class="hljs-string">"<span class="hljs-subst">\(projectName)</span>.xcodeproj/xcshareddata/xcschemes"</span>)
     )
     scheme <span class="hljs-operator">=</span> allFiles[<span class="hljs-number">0</span>].components(separatedBy: <span class="hljs-string">"."</span>).first <span class="hljs-operator">??</span> <span class="hljs-string">""</span>
     <span class="hljs-keyword">let</span> formatter <span class="hljs-operator">=</span> <span class="hljs-type">DateFormatter</span>()
     formatter.dateFormat <span class="hljs-operator">=</span> <span class="hljs-string">"yyyy-MM-dd HH:mm:ss"</span>
     exportIpaPath <span class="hljs-operator">=</span> packageDirectory.appPath(formatter.string(from: <span class="hljs-type">Date</span>()))
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>封装执行clean，archive，exportArchive</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">IpaTool</span></span>&#123;
    <span class="hljs-comment">/// 执行 xcodebuild clean</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">clean</span>()</span>-><span class="hljs-type">Output</span>&#123;
        <span class="hljs-keyword">let</span> arguments <span class="hljs-operator">=</span> [<span class="hljs-string">"clean"</span>,
                         <span class="hljs-string">"-workspace"</span>,
                         workspace,
                         <span class="hljs-string">"-scheme"</span>,
                         scheme,
                         <span class="hljs-string">"-configuration"</span>,
                         configuration.rawValue,
                         <span class="hljs-string">"-quiet"</span>,
                        ]
        <span class="hljs-keyword">return</span> <span class="hljs-type">Output</span>(pipe: <span class="hljs-type">Process</span>.executable(launchPath: <span class="hljs-string">"/usr/bin/xcodebuild"</span>, arguments: arguments))
    &#125;
    <span class="hljs-comment">/// 执行 xcodebuild archive</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">archive</span>()</span>-><span class="hljs-type">Output</span>&#123;
        <span class="hljs-keyword">let</span> arguments <span class="hljs-operator">=</span> [<span class="hljs-string">"archive"</span>,
                         <span class="hljs-string">"-workspace"</span>,
                         workspace,
                         <span class="hljs-string">"-scheme"</span>,
                         scheme,
                         <span class="hljs-string">"-configuration"</span>,
                         configuration.rawValue,
                         <span class="hljs-string">"-archivePath"</span>,
                         xcarchive,
                         <span class="hljs-string">"-quiet"</span>,
                        ]
        <span class="hljs-keyword">return</span> <span class="hljs-type">Output</span>(pipe: <span class="hljs-type">Process</span>.executable(launchPath: <span class="hljs-string">"/usr/bin/xcodebuild"</span>, arguments: arguments))
    &#125;
    <span class="hljs-comment">/// 执行 xcodebuild exportArchive</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">exportArchive</span>()</span>-><span class="hljs-type">Output</span>&#123;
        <span class="hljs-keyword">let</span> arguments <span class="hljs-operator">=</span> [<span class="hljs-string">"-exportArchive"</span>,
                         <span class="hljs-string">"-archivePath"</span>,
                         xcarchive,
                         <span class="hljs-string">"-configuration"</span>,
                         configuration.rawValue,
                         <span class="hljs-string">"-exportPath"</span>,
                         exportIpaPath,
                         <span class="hljs-string">"-exportOptionsPlist"</span>,
                         exportOptionsPlist,
                         <span class="hljs-string">"-quiet"</span>,
                        ]
        <span class="hljs-keyword">return</span> <span class="hljs-type">Output</span>(pipe: <span class="hljs-type">Process</span>.executable(launchPath: <span class="hljs-string">"/usr/bin/xcodebuild"</span>, arguments: arguments))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>准备工作完成，我们现在来编写打包代码</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">do</span>&#123;
    <span class="hljs-keyword">let</span> ipaTool <span class="hljs-operator">=</span> <span class="hljs-keyword">try</span> <span class="hljs-type">IpaTool</span>(projectPath: <span class="hljs-string">"/Users/gree/gmall_ios"</span>,
                          configuration: .debug,
                          exportOptionsPlist: <span class="hljs-string">"/Users/gree/Desktop/greeMall_ipa/2021-06-03 09:48:40/ExportOptions.plist"</span>,
                          pgyerKey: <span class="hljs-string">"xxxxxx"</span>)
    
    <span class="hljs-built_in">print</span>(ipaTool)
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行clean"</span>)
    <span class="hljs-keyword">var</span> output <span class="hljs-operator">=</span> ipaTool.clean()
    <span class="hljs-keyword">if</span> output.readData.count <span class="hljs-operator">></span> <span class="hljs-number">0</span> &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行失败clean error = <span class="hljs-subst">\(output.readData)</span>"</span>)
        exit(<span class="hljs-operator">-</span><span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行archive"</span>)
    output <span class="hljs-operator">=</span> ipaTool.archive()
    <span class="hljs-keyword">if</span> <span class="hljs-operator">!</span><span class="hljs-type">FileManager</span>.default.fileExists(atPath: ipaTool.xcarchive) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行失败archive error = <span class="hljs-subst">\(output.readData)</span>"</span>)
        exit(<span class="hljs-operator">-</span><span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行exportArchive"</span>)
    output <span class="hljs-operator">=</span> ipaTool.exportArchive()
    
    <span class="hljs-keyword">if</span> <span class="hljs-operator">!</span><span class="hljs-type">FileManager</span>.default.fileExists(atPath: ipaTool.exportIpaPath.appPath(<span class="hljs-string">"<span class="hljs-subst">\(ipaTool.scheme)</span>.ipa"</span>)) &#123;
        <span class="hljs-built_in">print</span>(<span class="hljs-string">"执行失败exportArchive error =<span class="hljs-subst">\(output.readData)</span>"</span>)
        exit(<span class="hljs-operator">-</span><span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"导出ipa成功<span class="hljs-subst">\(ipaTool.exportIpaPath)</span>"</span>)
&#125;<span class="hljs-keyword">catch</span>&#123;
    <span class="hljs-built_in">print</span>(error)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意projectPath使用自己项目路径，exportOptionsPlist建议先手动打一次包来获取</p>
</li>
<li>
<p>运行结果</p>
<pre><code class="copyable">IpaTool(scheme: "greeMall", configuration: SwiftCommandLineTool.IpaTool.Configuration.debug, exportOptionsPlist: "/Users/gree/Desktop/greeMall_ipa/2021-06-03 09:48:40/ExportOptions.plist", exportIpaPath: "/Users/gree/Desktop/greeMall_ipa/2021-06-07 13:59:21", projectPath: "/Users/gree/gmall_ios", projectName: "greeMall", packageDirectory: "/Users/gree/Desktop/greeMall_ipa", pgyerKey: "51895949ad44dcc3934f47c17aa0c0e5")
执行clean
执行archive
执行exportArchive
导出ipa成功/Users/gree/Desktop/greeMall_ipa/2021-06-07 13:59:21
Program ended with exit code: 0
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h1 data-id="heading-7">4、把ipa包上传蒲公英</h1>
<p>我这里上传文件使用<code>Alamofire</code>，如果你们熟悉<code>URLSession</code>用它也行</p>
<ol>
<li>
<p>在Package.swift</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> package <span class="hljs-operator">=</span> <span class="hljs-type">Package</span>(
    name: <span class="hljs-string">"SwiftCommandLineTool"</span>,
    platforms: [.macOS(<span class="hljs-string">"10.12"</span>)],
    dependencies: [
        .package(name: <span class="hljs-string">"Alamofire"</span>,
                 url: <span class="hljs-string">"https://github.com/Alamofire/Alamofire.git"</span>,
                 from: <span class="hljs-string">"5.4.3"</span>)
    ],
    targets: [
        .target(
            name: <span class="hljs-string">"SwiftCommandLineTool"</span>,
            dependencies: [<span class="hljs-string">"Alamofire"</span>]),
        .testTarget(
            name: <span class="hljs-string">"SwiftCommandLineToolTests"</span>,
            dependencies: [<span class="hljs-string">"SwiftCommandLineTool"</span>,<span class="hljs-string">"Alamofire"</span>]),
    ]
)

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>给IpaTool添加一个上传ipa的函数</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">//上传蒲公英</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">update</span>()</span>&#123;
       
        <span class="hljs-keyword">let</span> ipaPath <span class="hljs-operator">=</span> exportIpaPath.appPath(<span class="hljs-string">"<span class="hljs-subst">\(scheme)</span>.ipa"</span>)
        
        <span class="hljs-keyword">let</span> upload <span class="hljs-operator">=</span> <span class="hljs-type">AF</span>.upload(multipartFormData: &#123; formdata <span class="hljs-keyword">in</span>
            formdata.append(pgyerKey.data(using: .utf8)<span class="hljs-operator">!</span>, withName: <span class="hljs-string">"_api_key"</span>)
            formdata.append(<span class="hljs-type">URL</span>(fileURLWithPath: ipaPath), withName: <span class="hljs-string">"file"</span>)
        &#125;, to: <span class="hljs-type">URL</span>(string: <span class="hljs-string">"https://www.pgyer.com/apiv2/app/upload"</span>)<span class="hljs-operator">!</span>)
        
        <span class="hljs-keyword">var</span> isExit <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">let</span> queue <span class="hljs-operator">=</span> <span class="hljs-type">DispatchQueue</span>(label: <span class="hljs-string">"queue"</span>)
        upload.uploadProgress(queue: queue) &#123; progress <span class="hljs-keyword">in</span>
            <span class="hljs-keyword">let</span> p <span class="hljs-operator">=</span> <span class="hljs-type">Int</span>((<span class="hljs-type">Double</span>(progress.completedUnitCount) <span class="hljs-operator">/</span> <span class="hljs-type">Double</span>(progress.totalUnitCount)) <span class="hljs-operator">*</span> <span class="hljs-number">100</span>)
            <span class="hljs-built_in">print</span>(<span class="hljs-string">"上传进度:<span class="hljs-subst">\(p)</span>%"</span>)
        &#125;
        upload.responseData(queue:queue) &#123; dataResponse <span class="hljs-keyword">in</span>
            <span class="hljs-keyword">switch</span> dataResponse.result &#123;
            <span class="hljs-keyword">case</span> .success(<span class="hljs-keyword">let</span> data):
                <span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> <span class="hljs-type">String</span>(data: data, encoding: .utf8) <span class="hljs-operator">??</span> <span class="hljs-string">""</span>
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"上传成功:<span class="hljs-subst">\(result)</span>"</span>)
            <span class="hljs-keyword">case</span> .failure(<span class="hljs-keyword">let</span> error):
                <span class="hljs-built_in">print</span>(<span class="hljs-string">"上传失败: <span class="hljs-subst">\(error)</span>"</span>)
            &#125;
            isExit <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
        &#125;
        <span class="hljs-comment">//使用循环换保证命令行程序,不会死掉</span>
        <span class="hljs-keyword">while</span> isExit &#123;
            <span class="hljs-type">Thread</span>.sleep(forTimeInterval: <span class="hljs-number">1</span>)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-built_in">print</span>(<span class="hljs-string">"导出ipa成功<span class="hljs-subst">\(ipaTool.exportIpaPath)</span>"</span>)
<span class="hljs-built_in">print</span>(<span class="hljs-string">"开始上传蒲公英"</span>)
ipaTool.update()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上传文件的时候使用DispatchQueue.main命令行程序还是会死掉，所以加了一个while循环来保证程序不死。大家有其他方法告送我一下。</p>
</li>
</ol>
<h1 data-id="heading-8">5、打代码打包成一个CLl工具（命令行程序）</h1>
<p>我这里就不提供教程了，大家可以参考这篇文章：<a href="https://mp.weixin.qq.com/s/tX8LPjmGLEV9IT1_smMQBw" target="_blank" rel="nofollow noopener noreferrer">使用 Swift 编写 CLI 工具的入门教程</a></p>
<p>我不喜欢使用终端所以使用SwiftUI写了一个简单的macOS App</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e844f956a1304ac19d939bf8a506ad29~tplv-k3u1fbpfcp-watermark.image" alt="1623050858375.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">6、一般我们的项目中用了<code>CocoaPods</code>我们打包的时候要执行一下pod相关的命令</h1>
<pre><code class="hljs language-swift copyable" lang="swift"> <span class="hljs-comment">// pod install</span>
    <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">podInstall</span>()</span>-><span class="hljs-type">Output</span>&#123;
        <span class="hljs-keyword">var</span> environment <span class="hljs-operator">=</span> [<span class="hljs-type">String</span>:<span class="hljs-type">String</span>]()
        <span class="hljs-comment">/*
         添加环境变量LANG = en_US.UTF-8
         否则这个错误
         [33mWARNING: CocoaPods requires your terminal to be using UTF-8 encoding.
         Consider adding the following to ~/.profile:
         export LANG=en_US.UTF-8
         */</span>
        environment[<span class="hljs-string">"LANG"</span>] <span class="hljs-operator">=</span> <span class="hljs-string">"en_US.UTF-8"</span>
        <span class="hljs-comment">/*
         添加环境变量PATH = /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/gree/.rvm/bin
         终端运行 echo $PATH 获取
         否则这个错误
         [1mTraceback[m (most recent call last):
         9: from /usr/local/bin/pod:23:in `<main>'
         8: from /usr/local/bin/pod:23:in `load'
         7: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/bin/pod:55:in `<top (required)>'
         6: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/command.rb:49:in `run'
         5: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/command.rb:140:in `verify_minimum_git_version!'
         4: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/command.rb:126:in `git_version'
         3: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/executable.rb:143:in `capture_command'
         2: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/executable.rb:117:in `which!'
         1: from /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/executable.rb:117:in `tap'
     /Library/Ruby/Gems/2.6.0/gems/cocoapods-1.10.1/lib/cocoapods/executable.rb:118:in `block in which!': [1m[31m[!] Unable to locate the executable `git`[0m ([1;4mPod::Informative[m[1m)[m
         */</span>
        environment[<span class="hljs-string">"PATH"</span>] <span class="hljs-operator">=</span> <span class="hljs-string">"/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/gree/.rvm/bin"</span>
        <span class="hljs-comment">/*
         添加环境变量CP_HOME_DIR = NSHomeDirectory().appending("/.cocoapods")
         我的cocoapods安装在home目录所以使用这个,
         你们可以在访达->前往文件夹...-> ~/.cocoapods,来获取路径
         否则这个错误
         Analyzing dependencies
         Cloning spec repo `cocoapods` from `https://github.com/CocoaPods/Specs.git`
         [!] Unable to add a source with url `https://github.com/CocoaPods/Specs.git` named `cocoapods`.
         You can try adding it manually in `/var/root/.cocoapods/repos` or via `pod repo add`.
         */</span>
        environment[<span class="hljs-string">"CP_HOME_DIR"</span>] <span class="hljs-operator">=</span> <span class="hljs-type">NSHomeDirectory</span>().appending(<span class="hljs-string">"/.cocoapods"</span>)
        <span class="hljs-keyword">let</span> pipe <span class="hljs-operator">=</span> <span class="hljs-type">Process</span>.executable(launchPath: <span class="hljs-string">"/usr/local/bin/pod"</span>,
                                    arguments: [<span class="hljs-string">"install"</span>],
                                    currentDirectoryPath: projectPath,
                                    environment: environment)
        <span class="hljs-keyword">return</span> <span class="hljs-type">Output</span>(pipe: pipe)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            