
---
title: 'Electron 32位+Win7 渲染程序启动时频繁崩溃'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6401'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 01:42:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=6401'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">受影响版本</h3>
<p><code>32位 | >10.3.0  | 11.x.x  |  12.x.x  |  13.x.x</code></p>
<h3 data-id="heading-1">崩溃描述</h3>
<p>在winows7下,频繁重启 <strong>32位</strong> Electron,有一定几率会触发</p>
<p>使用自己打包了node_modules + asar头部解密的包, 触发几率比较高大概10次中会发生1次 , 且忽略asar头部解密功能,直接以读文件夹方式运行,依然存在问题,几率基本不变</p>
<p>一度怀疑是自己改了源码造成的不稳定性</p>
<p>后来测试了Electron官方的包发现也会触发<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnpm.taobao.org%2Fmirrors%2Felectron%2F11.4.9%2Felectron-v11.4.9-win32-ia32.zip" target="_blank" rel="nofollow noopener noreferrer" title="https://npm.taobao.org/mirrors/electron/11.4.9/electron-v11.4.9-win32-ia32.zip" ref="nofollow noopener noreferrer">(下载地址)</a>,只是几率比较小大概100次有1-2次</p>
<p>在windows10下一切正常</p>
<p>使用64位包也一切正常</p>
<p>正常启动Electron,有4个进程,如果发生奔溃只有3个</p>
<p>因为没有头绪,一直搁置,直到有一次在命令行中执行,发现了这个错误</p>
<p><code># Error installing extension 'extensions::SafeBuiltins'. v8_initializer.cc(96)</code></p>
<h3 data-id="heading-2">问题复现</h3>
<p>GitHub上一搜,不得了,哈哈哈</p>
<p>相关问题链接</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fissues%2F28487" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/electron/electron/issues/28487" ref="nofollow noopener noreferrer">github.com/electron/el…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29474" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/electron/electron/pull/29474" ref="nofollow noopener noreferrer">github.com/electron/el…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fissues%2F29177" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/electron/electron/issues/29177" ref="nofollow noopener noreferrer">github.com/electron/el…</a></p>
<p>原因为Electron开发人员为了与chromium保持一致,将x86程序启动时的内存由1.5M改为0.5M</p>
<p>在debug_tools中直接运行以下代码会直接导致渲染程序崩溃</p>
<pre><code class="copyable">try &#123;
function run() &#123;
run();
&#125;;
run();
&#125; catch (e) &#123;
console.error(e);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正常版本的Electron则会提示  <code>RangeError: Maximum call stack size exceeded</code></p>
<h3 data-id="heading-3">解决方案</h3>
<p>1.该BUG修复代码已经有人提交,等待合并后的下一个版本,目前11.4.10暂没有修复</p>
<p>2.直接修改源码重新编译</p>
<pre><code class="copyable">build.gn  1150行左右
 if (current_cpu == "x86") &#123;
        # Set the initial stack size to 0.5MiB, instead of the 1.5MiB needed by
        # Chrome's main thread. This saves significant memory on threads (like
        # those in the Windows thread pool, and others) whose stack size we can
        # only control through this setting. Because Chrome's main thread needs
        # a minimum 1.5 MiB stack, the main thread (in 32-bit builds only) uses
        # fibers to switch to a 1.5 MiB stack before running any other code.
        ldflags += [ "/STACK:0x80000" ]
      &#125; else &#123;
        # Increase the initial stack size. The default is 1MB, this is 8MB.
        ldflags += [ "/STACK:0x800000" ]
      &#125;      
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注释掉 ldflags += [ "/STACK:0x80000" ] </code></p>
<p><code>或者改为和x64一样大 [ "/STACK:0x800000" ]</code></p>
<p>目前我改为和x64一样大,正在测试...后续再报告进度</p></div>  
</div>
            