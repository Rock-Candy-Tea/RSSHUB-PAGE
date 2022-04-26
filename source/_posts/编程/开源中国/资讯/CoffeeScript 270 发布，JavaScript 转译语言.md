
---
title: 'CoffeeScript 2.7.0 发布，JavaScript 转译语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9157'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9157'
---

<div>   
<div class="content">
                                                                                            <p>CoffeeScript 2.7.0 发布了。CoffeeScript 是一套 JavaScript 转译语言，它会将类似 Ruby 语法的代码编译成 JavaScript，而且大部分结构都相似。CoffeeScript 拥有更严格的语法。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容包括：</p> 
<ul> 
 <li>现在支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-import-assertions" target="_blank">导入断言语法</a>。这允许像<code>export &#123; version &#125; from './package.json' assert &#123; type: 'json' &#125;</code><span style="background-color:#ffffff; color:#212529"><span> </span></span>这样的语句或像<code>import('./calendar.json', &#123; assert &#123; type: 'json' &#125; &#125;)</code><span style="background-color:#ffffff; color:#212529">这样的表达式。</span></li> 
 <li>CoffeeScript 不再总是修补 Node 的错误堆栈跟踪。这个补丁调整了行号和列号以匹配源 CoffeeScript 而不是生成的 JavaScript，这会导致与其他库的冲突，并且在传递 Node 的新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fdocs%2Flatest%2Fapi%2Fcli.html%23--enable-source-maps" target="_blank"><code>--enable-source-maps</code>flag</a><span style="background-color:#ffffff; color:#212529"><span> </span></span>时是不必要的。现在，只有在未设置<code>--enable-source-maps</code>、没有其他库已经修补堆栈跟踪并且使用 <code>require('coffeescript/register')</code>时才会进行修补。可以通过<code>require('coffeescript').patchStackTrace()</code>或<code>import &#123; patchStackTrace &#125; from 'coffeescript'; patchStackTrace()</code>明确启用补丁。</li> 
 <li>修复了 block (triple-quoted) strings 未正确转换为 JSX expression container wrapping the template literal 的问题（如<code><div a=&#123;`...`&#125; /></code>）。</li> 
 <li>修复了对于显式<code>[</code>array 或<code>&#123;</code>object literal 的非空第一行，续行的行为不符合预期的问题。</li> 
</ul> 
<p>详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcoffeescript.org%2F%23changelog" target="_blank">changelog</a>。</p>
                                        </div>
                                      
</div>
            