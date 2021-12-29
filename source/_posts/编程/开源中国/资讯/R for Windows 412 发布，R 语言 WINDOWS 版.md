
---
title: 'R for Windows 4.1.2 发布，R 语言 WINDOWS 版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7758'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7758'
---

<div>   
<div class="content">
                                                                                            <p><span>R 是用于统计计算和图形的语言和环境，是一个类似于 S 语言和环境的 GNU 项目。该项目为 R 语言在 WINDOWS 系列操作系统上的版本。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span style="background-color:#ffffff">R for Windows 4.1.2 版本的更新如下：</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>C-LEVEL FACILITIES</strong></p> 
<ul> 
 <li>Oracle Developer Studio 编译器的头文件 'R.h' 和 'Rmath.h'（使用命名空间 std;）中的解决方法现在不再需要 C++11了，所以已经被删除。在 Solaris 上报告了一些带有 int 参数的 log()（应该是 std::log()）的使用情况。</li> 
 <li>对于来自 S-compatibility macros PROBLEM 和 MESSAGE 的信息，现在已经有了 4095 字节的限制，更长的信息将被默默地截断，而不是可能导致 segfaults。</li> 
 <li>如果<code>R_NO_SEGV_HANDLER</code>环境变量非空，则不会设置 SEGV/ILL/BUS 信号（提供恢复用户界面）的信号处理程序。这允许更可靠地调试涉及控制台的崩溃。</li> 
</ul> 
<p style="text-align:start"><strong>DEPRECATED AND DEFUNCT</strong></p> 
<ul> 
 <li>旧的 S-compatibility macros PROBLEM、MESSAGE、ERROR、WARN、WARNING、RECOVER...已被废弃，并将在 R 4.2.0 中被隐藏。Rf_error 和 Rf_warning 的 native interface 长期以来一直是首选。</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#000000">BUG 修复</span></strong></p> 
<ul> 
 <li>.mapply(F, dots, .) 当 dots 不是一个列表时，不再出现 segfaults，并一如既往地使用 match.fun(F) 的记录。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18164" target="_blank">PR#18164</a></li> 
 <li> <p>hist(<Date>, ...) 和 hist(<POSIXt>, ...) 不再将 rect() 的参数（如 col 和 density）传递给 axis() 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18171" target="_blank">PR#18171</a></p> </li> 
 <li> <p><code>\Sexpr&#123;ch&#125;</code>现在保留<code>Encoding(ch)</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18152" target="_blank">PR#18152</a></p> </li> 
 <li> <p>将 RNG 设置为<code>"Marsaglia-Multicarry"</code>，例如 by <code>RNGkind()</code>，现在在更多地方发出警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18168" target="_blank">PR#18168</a></p> </li> 
 <li> <p><code>gray(numeric(), alpha=1/2)</code>不再出现 segfaults，修复了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18183" target="_blank">PR#18183</a></p> </li> 
 <li> <p>修复<code>dnbinom(x, size=<very_small>, .., log=TRUE)</code> 回归</p> </li> 
 <li> <p><code>as.Date.POSIXlt(x)</code>现在保留<code>names(x)</code>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18188" target="_blank">PR#18188</a></p> </li> 
 <li> <p><code>model.response()</code>现在通常会剥离一个<code>"AsIs"</code>类。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18190" target="_blank">PR#18190 </a></p> </li> 
 <li> <p><code>try()</code>在出现错误和长时间调用的情况下要快得多，例如从一些<code>do.call()</code>中</p> </li> 
 <li> <p><code>qqline(y = <object>)</code>例如<code>y=I(.)</code>，现在可以使用，另请参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18190" target="_blank">PR#18190</a></p> </li> 
 <li> <p>Non-integer mgp par() settings 现在可以在<code>axis()</code>和<code>mtext()</code>中正确处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.r-project.org%2Fshow_bug.cgi%3Fid%3D18194" target="_blank">PR#18194</a></p> </li> 
 <li> <p><code>formatC(x)</code>现在返回长度为零的<code>character()</code>，而不是当<code>x</code>长度为零时的<code>""</code></p> </li> 
 <li> <p><code>removeSource(fn)</code>现在保留了 (other) <code>attributes(fn)</code>。</p> </li> 
</ul> 
<p style="text-align:start">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcran.r-project.org%2Fbin%2Fwindows%2Fbase%2FNEWS.R-4.1.2.html" target="_blank">https://cran.r-project.org/bin/windows/base/NEWS.R-4.1.2.html</a></p>
                                        </div>
                                      
</div>
            