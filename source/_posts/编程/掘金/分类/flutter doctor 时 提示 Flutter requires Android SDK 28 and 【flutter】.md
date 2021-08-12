
---
title: 'flutter doctor 时 提示 Flutter requires Android SDK 28 and ...【flutter】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9429'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 18:49:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=9429'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、基本的一些环境变量已经配置</h2>
<ul>
<li>
<p>之前的若干步骤参见官网</p>
</li>
<li>
<p>先安装 <code>Android Studio</code></p>
</li>
<li>
<p>安装好后再运行<code>Android Studio</code></p>
</li>
<li>
<p>使用<code>SDK Manager</code> 安装<code>Android SDK 28</code></p>
</li>
<li>
<p>配置好 <code>ANDROID_HOME</code> 和 <code>PATH</code></p>
<p>export ANDROID_HOME=/Users/【当前用户】/Library/Android/sdk
export PATH=<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mi>A</mi><mi>T</mi><mi>H</mi><mo>:</mo></mrow><annotation encoding="application/x-tex">PATH:</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">P</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal" style="margin-right:0.08125em;">H</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span></span></span></span>&#123;ANDROID_HOME&#125;/tools
export PATH=<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>P</mi><mi>A</mi><mi>T</mi><mi>H</mi><mo>:</mo></mrow><annotation encoding="application/x-tex">PATH:</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">P</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal" style="margin-right:0.08125em;">H</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span></span></span></span>&#123;ANDROID_HOME&#125;/platform-tools</p>
</li>
</ul>
<p>上述操作完成之后 执行<code>flutter doctor</code>发现提示还有问题</p>
<pre><code class="copyable">Flutter requires Android SDK 28 and the Android BuildTools 28.0.3
1- Android SDK version 28
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、原因</h2>
<p>已安装的版本没有正确匹配 <code>Flutter</code>指定需要的版本</p>
<h2 data-id="heading-2">三、解决方法</h2>
<p>1、安装<code>Android 9.0 Pie</code><br>
操作步骤与路径：</p>
<pre><code class="copyable">Android Studio => SDK Manager => SDK Platforms tab => 选择 Android 9.0 Pie
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、安装<code>Android BuildTools version 28.0.3</code><br>
操作步骤与路径：</p>
<pre><code class="copyable">Android Studio => SDK Manager => SDK Tools tab => 选择右下角 Show Package Details => 在 Android SDK Build-Tools 里选择 28.0.3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、勾选完成之后点击<code>ok</code>进行安装</p>
<p>4、安装完成后重启<code>Android studio</code>，</p>
<p>5、此时再去命令行执行<code>flutter doctor</code>，应该没有这个问题了</p></div>  
</div>
            