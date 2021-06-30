
---
title: 'Python 3.9.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4853'
author: 开源中国
comments: false
date: Wed, 30 Jun 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4853'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Python 3.9.6 正式发布，该版本更新内容如下：</p> 
<h3>安全</h3> 
<ul> 
 <li>mod: <code>http.client</code> 现在可以避免在服务器发出 <code>100 Continue</code> 状态响应后无限地读取潜在的HTTP headers 信息；</li> 
</ul> 
<h3>核心和内置程序</h3> 
<ul> 
 <li>修复标记生成器初始化时引发的标记生成器错误的错误位置信息；</li> 
 <li>改进了 Oracle Solaris 上非 UTF 语言环境中的 Unicode 支持，此问题不会影响其他 Solaris 系统；</li> 
 <li>修复解析器中涉及带有无效表达式的关键字参数的错误消息；</li> 
 <li>修复了 C 代码中不正确的 dictkeys_reversed 和 dictitems_reversed 函数签名，这会破坏 webassembly 构建；</li> 
 <li>不再急切地使导入文件名绝对化，除了在 3.9.5 中引入的扩展模块。</li> 
 <li>修正 <code>str.format()</code> 中一个令人困惑的错误信息；</li> 
 <li>当通过 <code>compile()</code> 编译带有递归引用的 <code>ast.AST</code> 对象时，解释器不再崩溃，而是引发 <code>RecursionError</code>。</li> 
</ul> 
<h3>库</h3> 
<ul> 
 <li>将 vendored pip 更新为 21.1.3；</li> 
 <li>修复在其他 Python 实现中非常不可能发生的 glob 资源泄漏；</li> 
 <li>修正在 <code>bz2.BZ2File.write()</code> / <code>lzma.LZMAFile.write()</code> 方法中，当输入数据是支持缓冲区协议的对象时，文件长度可能是错误的问题。</li> 
 <li>修正 <code>as_string()</code> 函数，以正确传递 unixfrom；</li> 
 <li>在使一个枚举类成为 unpicklable 之前，要更稳健地搜索 pickle 支持；</li> 
 <li>允许多个数据类型混合，如果它们都是一样的；</li> 
 <li>在 Mac 上，给 turtledemo 按钮文本一个颜色，在浅色或深色背景下都可以使用；</li> 
 <li>修正当线程对象从未被加入时的引用泄露问题；</li> 
 <li>修正前一版本中用 <code>pathlib.Path</code> 对象的列表调用 <code>pkgutil.iter_modules()</code> 时的回归问题；</li> 
 <li>当为 ARM 平台编译时， <code>hashlib</code> 模块不再进行未对齐的内存访问；</li> 
 <li>将 <code>IO</code>、 <code>BinaryIO</code>、 <code>TextIO</code>、 <code>Match</code> 和 <code>Pattern</code> 加入 <code>typing._**all_</code>；**</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue43972" target="_blank">bpo-43972</a>: When <code>[http.server.SimpleHTTPRequestHandler](<https://docs.python.org/release/3.9.6/library/http.server.html#http.server.SimpleHTTPRequestHandler>)</code> sends a <code>301 (Moved Permanently)</code> for a directory path not ending with <code>/</code>, add a <code>Content-Length: 0</code> header. This improves the behavior for certain clients.</li> 
 <li>修正 <code>pdb</code> 中 <code>checkline()</code> 如果在 <code>reset()</code> 之后被调用会引发 <code>AttributeError</code> 的错误；</li> 
</ul> 
<h3>构建</h3> 
<ul> 
 <li>bpo-44381: Windows 版现在可以接受 EnableControlFlowGuard 设置为 guard 来启用 CFG。</li> 
</ul> 
<h3>Windows</h3> 
<ul> 
 <li>修正在 <code>threading</code> 中使用超时时，例如使用 <code>threading.Lock.acquisition()</code> 或 <code>threading.Condition.wait()</code> 时的 16ms 抖动；</li> 
</ul> 
<h3>macOS</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue43568" target="_blank">bpo-43568</a>：在为 macOS 构建扩展模块时放宽不必要的限制性 MACOSX_DEPLOYMENT_TARGET 检查；</li> 
 <li>允许 –with-lto 配置选项与 Apple 提供的 Xcode 或命令行工具一起使用；</li> 
</ul> 
<h3>IDLE</h3> 
<ul> 
 <li>将缩进空间设置从“字体”选项卡移动到新的 Windows 选项卡；</li> 
 <li>将设置对话框 General 选项卡拆分为 Windows 和 Shell/ED 选项卡。将扩展帮助菜单的帮助源移动到扩展选项卡。为新选项腾出空间并缩短对话框；</li> 
 <li>避免 <code>AutoCompleteWindow.winconfig_event()</code> 中未捕获的异常；</li> 
 <li>修正 IDLE 在 macOS 上完成标签时有时会冻结的问题；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.9.6%2Fwhatsnew%2Fchangelog.html" target="_blank">https://docs.python.org/release/3.9.6/whatsnew/changelog.html</a></p>
                                        </div>
                                      
</div>
            