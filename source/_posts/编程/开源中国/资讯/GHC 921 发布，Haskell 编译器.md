
---
title: 'GHC 9.2.1 发布，Haskell 编译器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=393'
author: 开源中国
comments: false
date: Sun, 31 Oct 2021 18:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=393'
---

<div>   
<div class="content">
                                                                                            <p>GHC（Glasgow Haskell Compiler）是 Haskell 语言的顶级套件。本次大版本更新带来了期待已久的众多新功能。</p> 
<p>新的 Haskell 语言级更新：</p> 
<ul> 
 <li><strong>GHC2021 语言</strong>：在 Haskell2010 标准的基础上，打包了数十个常用语言扩展。</li> 
 <li><strong>ImpredicativeTypes 扩展</strong>：第一类的多态类型支持。</li> 
 <li><strong>UnliftedDataTypes 扩展</strong>：允许定义严格求值的数据类型，在部分场合下可带来性能提升。</li> 
 <li><strong>Record Dot Syntax 系列扩展</strong>： 
  <ul> 
   <li>OverloadedRecordDot 扩展允许使用点访问记录，如 foo.x。</li> 
   <li>OverloadedRecordUpdate 扩展允许使用点更新记录，如 foo&#123;x.y.z = 1&#125;。</li> 
  </ul> </li> 
 <li>还有其他更多更新！</li> 
</ul> 
<p>新的编译器更新：</p> 
<ul> 
 <li><strong>编译速度大大提升</strong>，编译时间可降低 20%。</li> 
 <li><strong>GHC 现原生支持 ARMv8 代码生成，无需依赖于 LLVM。</strong></li> 
 <li>现可更激进地内联 generics，提升性能。</li> 
 <li>还有其他更多更新！</li> 
</ul> 
<p>运行时系统更新：</p> 
<ul> 
 <li><strong>并行垃圾回收器性能显著提升。</strong></li> 
 <li><strong>提供了新的 profile 手段 -hi，便于调试空间泄漏。</strong></li> 
 <li>还有其他更多更新！</li> 
</ul>
                                        </div>
                                      
</div>
            