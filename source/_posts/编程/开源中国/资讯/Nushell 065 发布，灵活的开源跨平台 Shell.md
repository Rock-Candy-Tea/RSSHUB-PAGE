
---
title: 'Nushell 0.65 发布，灵活的开源跨平台 Shell'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3480'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3480'
---

<div>   
<div class="content">
                                                                                            <p>Nushell，简称 Nu，是一个新的 shell，它对你的命令行采取了一种现代的、结构化的方法。它与你的文件系统、操作系统和越来越多的文件格式的数据无缝衔接。</p> 
<p>近日 Nu 0.65 版本正式发布，这个版本包括对二进制数据的更好支持，检查源文件正确性的新方法，改进的命令统一性等内容。</p> 
<h3>更好地支持二进制数据(hustcer、jt、CBenoit)</h3> 
<p>Nushell 的二进制支持一直在稳步提高，在这个版本中，它得到了更进一步的改善，新的功能包括：</p> 
<ul> 
 <li>新的运算符 <code>bit-and</code>、 <code>bit-or</code>、 <code>bit-xor</code>，以及重新命名的 <code>bit-shl</code> 和 <code>bit-shr</code>。这些对应于位和、或、异或、左移和右移。</li> 
 <li>一个新的 <code>encode</code> 命令，以及对 <code>hash</code> 的二进制支持</li> 
 <li>改进了对 <code>skip</code> 和 <code>take</code> 的二进制支持</li> 
</ul> 
<h3>Nu-check</h3> 
<p>从这个版本开始，Nushell 现在提供了一个 <code>nu-check</code> 命令，可以对源文件进行检查，以发现潜在的解析和类型检查错误。这将使脚本作者可以在不运行的情况下检查他们的脚本。</p> 
<h3>统一性</h3> 
<p>在 0.65 版本中，还继续进行了统一不同数据类型的命令的工作。在这个版本中， <code>db</code> 和 mysql 的支持已经简化，使其更接近于已经存在的数据框架支持。</p> 
<p>之前：</p> 
<pre><code class="language-cpp">open myfile.db
| db select a
| db from table_1
| db where ((db col a) > 1 | db and ((db col a) < 10))
</code></pre> 
<p>现在：</p> 
<pre><code class="language-cpp">open myfile.db
| select a
| from table_1
| where ((field a) > 1 | and ((field a) < 10))
</code></pre> 
<p>就像对数据框架的支持一样，这也是建立在对基于输入类型的重载命令的新支持上。这将使 Nushell 在未来有一个很好的、统一的语法，可以适用于各种数据类型。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nushell.sh%2Fblog%2F2022-07-05-nushell-0_65.html" target="_blank">https://www.nushell.sh/blog/2022-07-05-nushell-0_65.html</a></p>
                                        </div>
                                      
</div>
            