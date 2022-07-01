
---
title: 'PHP 8.2 最新进展，已发布 Alhpa2，即将进行新特性冻结'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4486'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 10:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4486'
---

<div>   
<div class="content">
                                                                                            <p>PHP基金会每月都会在博客上发表当月的PHP核心的最新进展。本文介绍的是6月的进展情况。</p> 
<h2>PHP8.2 的 QA 版本 和 特性冻结</h2> 
<p>PHP8.2计划于<strong>11 月 24 日 </strong>发布，PHP的版本发行管理员们已经发布了PHP8.2的Alpha 1和Alpha 2的版本。</p> 
<p>这些Alpha 版本不适合用于生产环境，而是用作测试环境和本地开发的版本节点。</p> 
<p>已经编译的windows版本可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwindows.php.net%2Fqa%2F" target="_blank">https://windows.php.net/qa/ </a>上找到，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2F_%2Fphp%3Ftab%3Dtags%26page%3D1%26name%3D8.2.0" target="_blank">Docker 镜像 </a>可以在Docker Hub 上找到，源代码在Github 上的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp%2Fphp-src" target="_blank">php/php-src</a>中，可以自行编译，在 Homebrew 上，PHP 8.2-dev 软件包可从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fshivammathur%2Fhomebrew-php" target="_blank">shivammathur/php</a> 查看相关指令。 </p> 
<p><strong>7 月 19 日 </strong>是 PHP 8.2 特性冻结日期，在此之后PHP8.2不在接收新的特性建议。PHP的新特性都有2周的讨论期和2周的投票期。在特性冻结之前必须对所有的RFC（提案）进行投票。</p> 
<h2>RFC的更新</h2> 
<p>上次PHP武器库小编在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpreturn.com%2Findex%2Fa626a74a300dc5.html" target="_blank">PHP8.2将会有哪些新东西？</a>中介绍了一部分的已经通过的新特性，如今又有一些新特性被投票通过，还有一些正在进行中。</p> 
<h3>已实现：允许false和null作为独立类型</h3> 
<p>在之前的文章中已经介绍过，有些开发者并不看好这件事，认为false作为独立类型并没有什么用。在这之前false只能和其他类型一起联合声明。</p> 
<p>你可以在PHP的播客中了解到对开发者George Peter Banyard的访谈。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpinternals.news%2F99" target="_blank">https://phpinternals.news/99</a> ，他提到大量的传统函数会在内部返回false和抛出异常。并不会返回有实际意义的东西，返回false也许是为了中断当前函数代码的执行。所以使用false作为独立的返回值也是有意义的。</p> 
<h3>已实现:允许true作为独立类型</h3> 
<p>早在之前的文章中，小编就提到过，false可以作为独立的类型（并且进行声明），但是true却不可以。此提案建议添加true作为独立类型，使PHP的类型系统根据表现力。</p> 
<h3>已通过：随机扩展5.x</h3> 
<p>是 Go Kudo 提出的 RFC 的第五次迭代，改进PHP的随机数生成器，并且将一些列的改动移动到单独的扩展中。</p> 
<h3>已通过：为is_callable添加弃用通知，并添加callable类型</h3> 
<p>PHP以后将弃用is_callable函数的部分表现，但在PHP8.2中只会产生弃用通知。这样做的原因，简单来讲，is_callable使用起来语法混乱。但注意，is_callable只是放弃了判断字符串的用法，比如is_callable(‘myFunction’)，对于其他类型仍然是可用的，比如一个变量代表的是一个回调函数。</p> 
<h3>已通过：析取范式类型</h3> 
<p>该提案提议PHP支持更多的类型声明组合，比如：</p> 
<pre><code class="language-php"><span>(</span><span>A</span><span>&</span><span>B</span><span>&</span><span>D</span><span>)</span><span>|</span><span>int</span><span>|</span><span>null</span></code></pre> 
<p>就是说该值有可能是null，有可能是整型，也有可能是实现了A接口、B接口、D接口的对象。</p> 
<p>对此可以查看提案详情： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fdnf_types" target="_blank">https://wiki.php.net/rfc/dnf_types</a> </p> 
<h2>更多的RFC</h2> 
<p>还有更多讨论中的提案，下面做一个简单地接受和链接。</p> 
<p>讨论中：新的CURL RUL API（增加curl类和url类）</p> 
<p>讨论中：const声明时使用枚举属性值</p> 
<p>讨论中：PDO程序中特性的子类（能够提高对sqlite、pgsql的支持）</p> 
<p>讨论中：使 iterator_*() 系列接受所有可迭代对象（目前只接受Traversables，但不接受array）</p> 
<p>讨论中：在枚举中实现自动Stringable（但仍然不能自定义覆盖）</p> 
<p>讨论中：短闭包（匿名函数想要使用外部变量必须使用use声明，短闭包可以解决这样的问题（，跟js的箭头函数效果一样））</p> 
<h2>其他</h2> 
<p>文章由PHP武器库小编根据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fthephp.foundation%2Fblog%2F2022%2F06%2F30%2Fphp-core-roundup-3%2F" target="_blank">https://thephp.foundation/blog/2022/06/30/php-core-roundup-3/</a> 翻译整理而成，有问题请联系。</p> 
<p>提到的文章链接：</p> 
<ul> 
 <li>PHP8.2的windows版本（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwindows.php.net%2Fqa%2F" target="_blank">https://windows.php.net/qa/</a> ）</li> 
 <li>PHP8.2的docker 镜像（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2F_%2Fphp%3Ftab%3Dtags%26page%3D1%26name%3D8.2.0" target="_blank">https://hub.docker.com/_/php?tab=tags&page=1&name=8.2.0</a> ）</li> 
 <li>PHP8.2的源码托管地址（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp%2Fphp-src" target="_blank">https://github.com/php/php-src</a> ）</li> 
 <li>PHP8.2的Mac工具Homebrew  安装（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fshivammathur%2Fhomebrew-php" target="_blank">https://github.com/shivammathur/homebrew-php</a> ）</li> 
 <li>PHP8.2将有哪些新东西？（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpreturn.com%2Findex%2Fa626a74a300dc5.html" target="_blank">https://phpreturn.com/index/a626a74a300dc5.html</a> ）</li> 
 <li>提案：将false和null作为独立类型（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fnull-false-standalone-types" target="_blank">https://wiki.php.net/rfc/null-false-standalone-types</a> ）</li> 
 <li>对于（将false和null作为独立类型）提案的开发者访谈（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpinternals.news%2F99" target="_blank">https://phpinternals.news/99</a> ）</li> 
 <li>提案：将true作为独立类型（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Ftrue-type" target="_blank">https://wiki.php.net/rfc/true-type</a> ）</li> 
 <li>提案：对is_callable的弃用通知（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fpartially-supported-callables-expand-deprecation-notices" target="_blank">https://wiki.php.net/rfc/partially-supported-callables-expand-deprecation-notices</a> ）</li> 
 <li>提案：析取范式类型（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fdnf_types" target="_blank">https://wiki.php.net/rfc/dnf_types</a> ）</li> 
 <li>提案：新的CURL URL API （ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fcurl-url-api" target="_blank">https://wiki.php.net/rfc/curl-url-api</a> ）</li> 
 <li>提案：const声明使用枚举属性值（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Ffetch_property_in_const_expressions" target="_blank">https://wiki.php.net/rfc/fetch_property_in_const_expressions</a> ）</li> 
 <li>提案：PDO的特定子类（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fpdo_driver_specific_subclasses" target="_blank">https://wiki.php.net/rfc/pdo_driver_specific_subclasses</a> ）</li> 
 <li>提案：扩大iterator的可迭代多项（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fiterator_xyz_accept_array" target="_blank">https://wiki.php.net/rfc/iterator_xyz_accept_array</a> ）</li> 
 <li>提案：在没居中实现自动Stringable（  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fauto-implement_stringable_for_string_backed_enums" target="_blank">https://wiki.php.net/rfc/auto-implement_stringable_for_string_backed_enums</a> ）</li> 
 <li>提案：短闭包（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.php.net%2Frfc%2Fauto-capture-closure" target="_blank">https://wiki.php.net/rfc/auto-capture-closure</a> ）</li> 
</ul> 
<p>关于PHP更多合并说明可以查看：  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fthephp.foundation%2Fblog%2F2022%2F06%2F30%2Fphp-core-roundup-3%2F%23merged-prs-and-commits" target="_blank">https://thephp.foundation/blog/2022/06/30/php-core-roundup-3/#merged-prs-and-commits</a> </p> 
<blockquote> 
 <p><span>原文标题：</span>PHP8.2最新进展，已发布Alhpa2，即将进行新特性冻结</p> 
 <p><span>原文地址：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fphpreturn.com%2Findex%2Fa62be479ae1e02.html" target="_blank">https://phpreturn.com/index/a62be479ae1e02.html</a></p> 
 <p><span>原文平台：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fphpreturn.com" target="_blank">PHP武器库</a></p> 
 <p><span>版权声明：</span>本文由<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fphpreturn.com" target="_blank">phpreturn.com</a>（PHP武器库官网）原创和首发，所有权利归phpreturn（PHP武器库）所有，本站允许任何形式的转载/引用文章，但必须同时注明出处。</p> 
</blockquote>
                                        </div>
                                      
</div>
            