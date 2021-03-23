
---
title: 'Crystal 编程语言正式迈入 1.0 版本'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Tue, 23 Mar 2021 07:32:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p>Crystal 是一种通用的、面向对象的编程语言，由 Ary Borenszweig、Juan Wajnerman、Brian Cardiff 和300多名贡献者设计开发。它的语法受到 Ruby 语言的启发，它是一种编译语言，具有静态类型检查功能，但一般不需要指定变量或方法参数的类型，可实现接近 c/c++ 的性能。它的类型由一个先进的全局类型推理算法来解决。</p> 
<p>Crystal 1.0.0 版本正式发布，该版本是 Crystal 的第一个主要版本，也是它的一个重要里程碑。此版本更新内容如下：</p> 
<h3>语言变化</h3> 
<ul> 
 <li>支持 <code>Tuple#[](Range)</code> 编译时范围资源. (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F10379" target="_blank">#10379</a>)</li> 
</ul> 
<h3>宏</h3> 
<ul> 
 <li>不要使用命名的参数键名作为 <code>method_missing</code> 调用的参数</li> 
</ul> 
<h3>标准库</h3> 
<ul> 
 <li>(break-change) 删除已废弃的定义</li> 
 <li>修正多处的示例代码</li> 
</ul> 
<h3>宏</h3> 
<ul> 
 <li>(break-change) 总是在 getter/property 宏中添加显式返回类型。</li> 
</ul> 
<h3>数值</h3> 
<ul> 
 <li>(break-change) 将默认的四舍五入模式改为 <code>TIES_EVEN</code></li> 
 <li>修复降频浮动无穷大</li> 
 <li>修正 <code>String#to_f</code> 超出范围的行为</li> 
 <li>实现 <code>Number#round</code> 的四舍五入模式。</li> 
 <li>Add missing unicode whitespace support to <code>String</code> methods. (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Fpull%2F10367" target="_blank">#10367</a>, thanks <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstraight-shoota" target="_blank">@straight-shoota</a></strong>)</li> 
</ul> 
<h3>文本</h3> 
<ul> 
 <li>为 <code>String</code> 方法添加缺失的 unicode 空白支持</li> 
</ul> 
<h3>集合</h3> 
<ul> 
 <li>修正 <code>Range#==</code> 忽略通用类型参数</li> 
 <li>让 <code>Enumerable#flat_map</code>、 <code>Iterator#flat_map</code> 可以和混合元素类型一起使用</li> 
 <li>删除重复的 <code>sort</code> 相关规格</li> 
 <li>修正关于 <code>Set#each</code> 返回类型的文档</li> 
 <li>修正文档中关于 <code>Set#*set_of?</code> 的例子</li> 
 <li>修正对设定规格的期望</li> 
</ul> 
<h3>序列化</h3> 
<ul> 
 <li>(break-change) 默认将 <code>Enum</code> 序列化为下划线的 <code>String</code></li> 
 <li>(break-change)在 XML 模块中使用类代替结构体</li> 
 <li>增加 <code>YAML::Nodes::Node#kind</code></li> 
</ul> 
<h3>文件</h3> 
<ul> 
 <li>让 <code>IO::Memory</code> 不能用只读的 <code>Slice</code> 写入</li> 
 <li>允许在 <code>IO#read_at</code> 中使用 <code>Int64</code> 值</li> 
 <li>增加 <code>IO::Sized#remaining=(value)</code> 来重用一个现有的实例</li> 
</ul> 
<h3>联网</h3> 
<ul> 
 <li>(security) 删除 Cookie 名称解码</li> 
 <li>(break-change) 删除 cookie 值的隐式编。(#10485, thanks @straight-shoota)</li> 
 <li>(break-change) 将 <code>HTTP::Cookies.from_headers</code> 拆分成服务器/客户端的独立方法</li> 
 <li>(性能) 对 <code>HTTP::Cookies</code> 进行了小幅性能改进</li> 
 <li>从类方法构造 <code>HTTP::Client</code> 时，遵循子类</li> 
 <li>让 <code>content-length</code> 标头更符合 RFC 标准</li> 
 <li>修正 <code>#respond_with_status</code>，当标头文件写入或关闭时</li> 
 <li>修正 <code>Cookie#==</code>，把所有的 ivars 都考虑进去</li> 
 <li>删除 <code>HTTP::Cookie</code> 中隐含的 <code>path=/</code></li> 
 <li>添加 <code>HTTP::Request#local_address</code></li> 
</ul> 
<h3><strong>日志</strong></h3> 
<ul> 
 <li>在 <code>#finalize</code> 时关闭 <code>AsyncDispatcher</code></li> 
</ul> 
<h3>系统</h3> 
<ul> 
 <li>修正 <code>Process.parse_argument</code> 的行为</li> 
 <li>为 macOS/darwin 目标添加 aarch64 支持</li> 
 <li>在 x86_64-darwin 中加入 <code>LibC::MAP_ANONYMOUS</code> 以匹配其他平台</li> 
</ul> 
<h3>运行时</h3> 
<ul> 
 <li>改进 ELF 阅读器在未初始化运行时的错误信息。</li> 
</ul> 
<h3>编译器</h3> 
<ul> 
 <li>(break-change) 不允许在字符串和字符文字的转义序列中代入一半， <code>\\x</code> 用于任意二进制值。</li> 
 <li>修正当在详尽的段内调用伪方法时的 ICE</li> 
 <li>修复解析 <code>foo.%</code> 调用时的 ICE</li> 
 <li>修正符号引用规则的边缘情况</li> 
 <li>在 Const 初始化器中支持封闭的变量</li> 
 <li>文档语法修正</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrystal-lang%2Fcrystal%2Freleases%2Ftag%2F1.0.0" target="_blank">https://github.com/crystal-lang/crystal/releases/tag/1.0.0</a></p>
                                        </div>
                                      
</div>
            