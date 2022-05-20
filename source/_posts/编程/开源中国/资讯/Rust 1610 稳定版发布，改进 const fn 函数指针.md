
---
title: 'Rust 1.61.0 稳定版发布，改进 const fn 函数指针'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4129'
author: 开源中国
comments: false
date: Fri, 20 May 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4129'
---

<div>   
<div class="content">
                                                                                            <p>Rust 1.61.0 已正式发布。此版本包含多项重要的语法变更，以及编辑器和标准库方面的改动。</p> 
<p style="text-align:start"><strong>语言特性</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93827%2F" target="_blank"><code>const fn</code><span> 签名已引入通用 trait 边界</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93827%2F" target="_blank"><code>const fn</code><span> 签名现已支持在参数中使用</span><code>impl Trait</code>并返回位置</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93827%2F" target="_blank">支持在<code>const fn</code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93827%2F" target="_blank">创建、转换和传递函数指针 </a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F94081%2F" target="_blank">递归调用 (Recursive calls) 现在支持设置函数的不透明<code>impl Trait</code><span>返回类型</span></a></li> 
</ul> 
<p style="text-align:start"><strong>编译器</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93901%2F" target="_blank">支持在<code>#[link]</code><span>属性和命令行中链接修饰符语法</span>，特别是<code>whole-archive</code><span>修饰符</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F89887%2F" target="_blank"><code>char</code><span> 类型在 </span>debuginfo</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F89887%2F" target="_blank">中被描述为 UTF-32</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.rust-lang.org%2Freference%2Fattributes%2Fcodegen.html%23the-target_feature-attribute" target="_blank"><code>#[target_feature]</code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F90621%2F" target="_blank">属性支持与 aarch64 功能一起使用</a></li> 
 <li>X86<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93745%2F" target="_blank"><code>#[target_feature = "adx"]</code><span> </span>现已到达稳定状态</a></li> 
</ul> 
<p style="text-align:start"><strong>Libraries</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F88375%2F" target="_blank"><code>ManuallyDrop<T></code>现在被记录为具有相同的布局<code>T</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F92714%2F" target="_blank"><code>#[ignore = "…"]</code><span> </span>运行测试时会打印信息</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F93263%2F" target="_blank">Consistently始终将 Windows 上缺少的 stdio 句柄显示为 NULL 句柄</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Fpull%2F95016%2F" target="_blank"><code>Vec::from_raw_parts</code>现在对其输入的限制较少</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-lang%2Frust%2Freleases%2Ftag%2F1.61.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            