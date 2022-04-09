
---
title: 'Crystal 1.4.0 发布，语法类似 Ruby 的编译型编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=297'
author: 开源中国
comments: false
date: Sat, 09 Apr 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=297'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Crystal 是一种通用的、面向对象的编程语言，由 Ary Borenszweig、Juan Wajnerman、Brian Cardiff 和 300 多名贡献者设计开发。Crystal 的语法受到 Ruby 的启发，属于编译语言，具有静态类型检查功能，但一般不需要指定变量或方法参数的类型，可实现接近 C/C++ 的性能。它的类型由一个先进的全局类型推理算法来解决。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最新发布的 1.4.0 版本包含错误修复和功能改进，涉及到语法、标准库、集合、加密、文件、语法宏、网络、运行时和规范等，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Freleases%2Ftag%2F1.4.0" target="_blank">详情查看 release note</a>。</p> 
<p>值得关注的变化</p> 
<p><strong>初步支持 WebAssembly</strong></p> 
<p>1.4.0 版本提供了对 WebAssembly 支持的 MVP 实现（最小可行<span style="background-color:#ffffff; color:#333333">性产品</span>），目前只支持将 Crystal 程序编译为 WebAssembly，以及与基于 WASI 的 LibC 连接，尚未支持浏览器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F10870" target="_blank">更多技术细节查看此 PR</a>。</p> 
<p><strong>对实例和类变量提供更好的类型推断</strong></p> 
<p>在此版本之前，像下面的简单程序无法推断出实例变量的类型：</p> 
<pre><code>class DisplayHello
  DELAY = 10.milliseconds

  @timer_countdown = DELAY
end</code></pre> 
<p>在新版本中可正常编译，正确推断出<code class="language-crystal"><span>@timer_countdown</span></code><span style="background-color:#ffffff; color:#000000">变量的类型为</span><code class="language-crystal"><span>Time</span><span>::</span><span>Span</span></code><span style="background-color:#ffffff; color:#000000">。</span></p> 
<pre><code>class DisplayHello

  def initialize(delay : Time::Span)
    @timer_countdown = delay + 10.seconds
  end
end</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11812" target="_blank">点此查看更多技术细节</a>。</p> 
<p>其他重要变更</p> 
<ul> 
 <li>支持 <span style="background-color:#ffffff; color:#000000">LLVM 14 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11905" target="_blank">#11905</a><span style="background-color:#ffffff; color:#000000">)</span></li> 
 <li>面向<code class="language-crystal"><span>Int128</span></code><span style="background-color:#ffffff; color:#000000">提供完整的编译器支持 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11576" target="_blank">#11576</a><span style="background-color:#ffffff; color:#000000">)</span></li> 
 <li><span style="background-color:#ffffff; color:#000000"><span>在</span></span><code class="language-crystal"><span>BigFloat</span><span>#to_s</span></code>中提供对科学计数法的支持<span style="background-color:#ffffff; color:#000000"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F10632" target="_blank">#10632</a><span style="background-color:#ffffff; color:#000000">)</span></li> 
 <li>不再支持无文档<span style="background-color:#ffffff; color:#000000"><span> </span>flag</span><code class="language-crystal"><span>skip_abstract_def_check</span></code><span style="background-color:#ffffff; color:#000000"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F9217" target="_blank">#9217</a><span style="background-color:#ffffff; color:#000000">)</span></li> 
 <li><span style="background-color:#ffffff; color:#000000">……</span></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2F2022%2F04%2F06%2F1.4.0-released.html" target="_blank">点此查看详细更新说明</a>。</p>
                                        </div>
                                      
</div>
            