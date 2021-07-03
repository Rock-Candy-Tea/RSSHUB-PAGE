
---
title: 'flutter 库_package_ enhance_stepper 封装记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4583'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 06:26:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=4583'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://pub.dev/packages/enhance_stepper" target="_blank" rel="nofollow noopener noreferrer">enhance_stepper </a></p>
<h4 data-id="heading-0">Package 介绍</h4>
<p>使用package可以创建可轻松共享的模块化代码。一个最小的package包括</p>
<ul>
<li>一个<code>pubspec.yaml</code>文件：声明了package的名称、版本、作者等的元数据文件。</li>
<li>一个 <code>lib</code> 文件夹：包括包中公开的(public)代码，最少应有一个<code><package-name>.dart</code>文件</li>
</ul>
<h4 data-id="heading-1">Package 类型</h4>
<p>Packages可以包含多种内容：</p>
<ul>
<li>Dart包：其中一些可能包含Flutter的特定功能，因此对Flutter框架具有依赖性，仅将其用于Flutter，例如<a href="https://pub.dartlang.org/packages/fluro" target="_blank" rel="nofollow noopener noreferrer"><code>fluro</code></a>包。</li>
<li>插件包：一种专用的Dart包，其中包含用Dart代码编写的API，以及针对Android（使用Java或Kotlin）和/或针对iOS（使用ObjC或Swift）平台的特定实现。一个具体的例子是<a href="https://pub.dartlang.org/packages/battery" target="_blank" rel="nofollow noopener noreferrer"><code>battery</code></a>插件包。</li>
</ul>
<hr>
<h2 data-id="heading-2">操作步骤：</h2>
<h4 data-id="heading-3">Step 1：创建 enhance_stepper 本地工程</h4>
<p>flutter create --template=package enhance_stepper</p>
<p>进入 enhance_stepper 文件夹，创建 example 工程
flutter create example</p>
<h4 data-id="heading-4">Step 2: 实现package</h4>
<p>...</p>
<h4 data-id="heading-5">Step 3：关联到 github 并添加文档</h4>
<p>github 上创建同名库，clone 到本地，将本地文件上传同步到 github。</p>
<p>建议将以下文档添加到所有软件包：</p>
<p>README.md:介绍包的文件
CHANGELOG.md 记录每个版本中的更改
LICENSE 包含软件包许可条款的文件
所有公共API的API文档 (详情见下文)</p>
<h4 data-id="heading-6">Step 4：检查是否可发布</h4>
<p>flutter packages pub publish --dry-run --server=<a href="https://pub.dartlang.org/" target="_blank" rel="nofollow noopener noreferrer">pub.dartlang.org</a></p>
<h4 data-id="heading-7">Step 5：发布</h4>
<p>flutter packages pub publish --server=<a href="https://pub.dartlang.org/" target="_blank" rel="nofollow noopener noreferrer">pub.dartlang.org</a></p>
<h4 data-id="heading-8">Step 6：上传成功, 并收到邮件通知</h4>
<p>Successfully uploaded package.</p>
<hr>
<p>如果是发布私有库/package，<strong>Step 3</strong> 结束后不发布即为私有库, 使用如下：</p>
<pre><code class="copyable">dependencies:
  library_name:
   git:
    url: https://github.com/username/library_name.git
    ref: dev    #branch name
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">参考资料：</h4>
<p><a href="https://flutterchina.club/developing-packages/" target="_blank" rel="nofollow noopener noreferrer">flutterchina.club/developing-…</a></p>
<p><a href="https://flutter.cn/docs/development/packages-and-plugins/developing-packages" target="_blank" rel="nofollow noopener noreferrer">flutter.cn/docs/develo…</a></p></div>  
</div>
            