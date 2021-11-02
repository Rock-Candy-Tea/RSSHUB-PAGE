
---
title: 'Rust 1.56.1 发布，解决 Unicode 安全漏洞问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4863'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4863'
---

<div>   
<div class="content">
                                                                                            <p>Rust 1.56.1 现已发布。此版本引入了两个新的 lints，以减轻最近披露的一个安全问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-42574" target="_blank">CVE-2021-42574 </a>的影响：</p> 
<blockquote> 
 <p>在 Unicode Specification through 14.0 的双向算法中发现了一个问题。它允许通过控制序列对字符进行视觉重新排序，可用于制作源代码，呈现与编译器和解释器摄取的标记的逻辑顺序不同的逻辑。攻击者可以利用这一点对接受 Unicode 的编译器的源代码进行编码，从而将目标漏洞引入人类审查者不可见的地方。</p> 
</blockquote> 
<p>Rust 官方<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rust-lang.org%2F2021%2F11%2F01%2Fcve-2021-42574.html" target="_blank">表示</a>，他们于今年 7 月 25 号<span style="background-color:#ffffff; color:#000000">收到了报告并开始</span><span style="color:#000000"><span style="background-color:#ffffff">着手修复。虽然这问题本身不是 rustc 的缺陷，但他们正在采取积极措施来减轻其对 Rust 开发人员的影响。其</span>建议所有用户立即升级，以确保他们的代码库不受该安全问题的影响。</span></p> 
<p><span style="color:#000000">Rust 1.56.1 引入了两个新的 lints，以检测和拒绝包含受影响的 codepoints；而 Rust 1.0.0 到 Rust 1.56.0 中则不包括这样的 lints。公告指出，如果你不对这些 <span style="background-color:#ffffff">codepoints </span>的存在进行 out-of-band checks，你的源代码就容易受到这种攻击。</span></p> 
<p><span style="color:#000000">为了评估生态系统的安全性，Rust 团队分析了曾经在 crates.io 上发布的所有 crate 版本（截至 2021-10-17），只有 5 个 crate 的源代码中存在受影响的代码点，而且没有出现任何恶意的情况。</span></p> 
<p><span style="color:#000000">Rust 1.56.1 中有两个新的 deny-by-default lints，可以检测受影响的 codepoints，分别在 string literals 和 comments 中。这些 lints 将阻止包含这些 codepoints 的源代码文件被编译，从而保护用户免受攻击。</span></p> 
<p><span style="color:#000000">如果你的代码对这些 codepoints 有正确的用途，官方建议用相关的转义序列来替换它们。错误信息会建议使用正确的转义。</span></p> 
<p><span style="color:#000000">如果你不能升级你的编译器版本，或者你的代码库还包括非 Rust 源代码文件。官方不择建议定期检查以下 codepoints 是否存在于你的版本库和你的依赖中：<span style="background-color:#ffffff">U+202A、U+202B、U+ 202C、U+202D、U+202E、U+2066、U+2067、U+2068、U+2069。</span></span></p> 
<p>安全研究员 Ross Anderson <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.lightbluetouchpaper.org%2F2021%2F11%2F01%2Ftrojan-source-invisible-vulnerabilities%2F" target="_blank">指出</a>，鉴于<span style="background-color:#ffffff; color:#080e14">该漏洞是 Unicode 问题，所以它不仅会影响 Rust；还会影响 </span><span style="background-color:#ffffff; color:#141412">C、C++、C#、JavaScript、Java、Rust、Go 和 Python 等</span><span style="background-color:#ffffff; color:#080e14">其他顶级语言</span><span style="background-color:#ffffff; color:#141412">，并怀疑它适用于大多数其他现代语言。</span></p> 
<p><span style="color:#000000">此外，其还发现了一个类似的安全问题；即</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-42694" target="_blank">CVE-2021-42694</a><span style="color:#000000">，涉及标识符内的 homoglyphs。不过从 Rust 1.53.0 开始，Rust 已经包含了对该攻击的缓解措施。由于 Rust 1.0.0 到 Rust 1.52.1 版本中缺乏对 non-ASCII 标识符的支持，因此不受影响。</span></p> 
<p><span style="background-color:#ffffff; color:#000000">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rust-lang.org%2F2021%2F11%2F01%2FRust-1.56.1.html" target="_blank">查看官方公告</a>。</span></p>
                                        </div>
                                      
</div>
            