
---
title: 'Crystal 1.3.0 发布，语法类似 Ruby 的编译型编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5212'
author: 开源中国
comments: false
date: Sat, 08 Jan 2022 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5212'
---

<div>   
<div class="content">
                                                                                            <p>Crystal 是一种通用的、面向对象的编程语言，由 Ary Borenszweig、Juan Wajnerman、Brian Cardiff 和 300 多名贡献者设计开发。Crystal 的语法受到 Ruby 语言的启发，属于编译语言，具有静态类型检查功能，但一般不需要指定变量或方法参数的类型，可实现接近 C/C++ 的性能。它的类型由一个先进的全局类型推理算法来解决。</p> 
<p>最新发布的版本包含错误修复和功能改进，涉及到编译器、代码生成、调试器、解析器、语义、语法、标准库、加密、网络、运行时和语法宏等方面，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Freleases%2Ftag%2F1.3.0" target="_blank">详情查看 release note</a>。</p> 
<p><strong>部分亮点</strong></p> 
<p><strong>系统调用(</strong><strong>SYSCALLS)</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了一个实验性 API 来创建原生系统调用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F10777" target="_blank">#10777</a>)。目前仅支持 Linux。这是支持 Linux<code class="language-plaintext">io_uring</code>接口以提高 IO 性能的第一步。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如需定义系统调用，请打开一个模块并使用</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2Fapi%2F1.3.0%2FSyscall.html%23def_syscall%2528name%252Creturn_type%252C%252Aargs%2529-macro" target="_blank"><code class="language-plaintext">Syscall.def_syscall</code></a><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>宏。如以下示例所示，需要传入系统调用名称、返回类型及其参数。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>require "syscall"

module MySyscalls
  Syscall.def_syscall write, Int32, fd : Int32, buf : UInt8*, count : LibC::SizeT
end

data = "Hello!\n"
MySyscalls.write(1, data.to_unsafe, LibC::SizeT.new(data.size))</code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong>支持 128 位字面量</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start">通过改进解析器，现在可以理解完整范围内的数字文字或 128 位整数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F11571" target="_blank">#11571</a>)。到目前为止，仅在 64 位值的范围内支持 128 位文字。</p> 
<pre><code>1_i128                                       # Works in 1.2.2 and 1.3.0
170141183460469231731687303715884105727_i128 # Fails in 1.2.2, works in 1.3.0</code></pre> 
<pre><code>1_.1   # Error: unexpected '_' in number
-0u64  # Error: Invalid negative value -0 for UInt64
-0_u64 # Error: Invalid negative value -0 for UInt64
1__2   # Error: consecutive underscores in numbers aren't allowed
0x_2   # Error: unexpected '_' in number
0_12   # Error: octal constants should be prefixed with 0o
0e40   # => 0.0
0x     # Error: numeric literal without digits</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrystal-lang.org%2F2022%2F01%2F06%2F1.3.0-released.html" target="_blank">详细更新说明点此查看</a>。</p>
                                        </div>
                                      
</div>
            