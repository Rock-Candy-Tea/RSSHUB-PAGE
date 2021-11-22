
---
title: 'Lark Parser 1.0 发布，Python 解析工具库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-efa3af8257c6e420e690db0753267fdd1b4.png'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 08:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-efa3af8257c6e420e690db0753267fdd1b4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Lark Parser 1.0 已发布。Lark 是一个现代化的 Python 解析库，可以解析任何无上下文的语法。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Lark 提供：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>高级语法语言，基于EBNF</li> 
 <li>三种解析算法可供选择：Earley，LALR(1) 和 CYK</li> 
 <li>自动树构造，从语法进行推断</li> 
 <li>具有正则表达式支持和自动行计数的快速 unicode 词法分析器</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-efa3af8257c6e420e690db0753267fdd1b4.png" referrerpolicy="no-referrer"></p> 
<p>1.0 版本的发布意味着 API 已稳定，当然也包含部分破坏性变更。</p> 
<p><strong>改进</strong></p> 
<ul> 
 <li>提供更好的类型注解</li> 
 <li>支持动态 Earley 的终端优先级 (terminal priorities)</li> 
 <li>正式支持 Python 3 语法，可通过<code>%import python (...)</code>进行使用</li> 
 <li>引入新的实验性功能：Tree Templates</li> 
 <li>修复多项错误</li> 
</ul> 
<p><strong>破坏性变更</strong></p> 
<ul> 
 <li>放弃对 Python 2 的支持，<span style="background-color:#ffffff; color:#24292f">Lark 现在只支持 Python 3.6 及以上版本</span></li> 
 <li>使用<code>pip install lark</code><span>（</span>不是 lark-parser）安装 lark</li> 
 <li><code>maybe_placeholders</code><span> </span>的值默认为 True</li> 
 <li><span>将</span><code>TraditionalLexer</code>重命名为<code>BasicLexer</code>，将<code>'standard'</code>lexer 选项重命名为<code>'basic'</code></li> 
 <li>对于 terminals 和 rules，默认优先级为 0（此前 terminals 的优先级为 1）</li> 
 <li>丢弃机制现在通过返回丢弃 (Discard) 完成，而不是将其作为一个异常引发</li> 
 <li><code>UnexpectedInput.match_examples()</code><span>中的</span><code>use_accepts</code>默认值现在为 True</li> 
 <li><code>v_args(meta=True)</code><span> 现在将 </span>meta 作为第一个参数，例如<code>(meta, children)</code></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flark-parser%2Flark%2Freleases%2Ftag%2F1.0.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            