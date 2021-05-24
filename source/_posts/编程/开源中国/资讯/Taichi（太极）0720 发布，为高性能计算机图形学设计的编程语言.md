
---
title: 'Taichi（太极）0.7.20 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif'
author: 开源中国
comments: false
date: Mon, 24 May 2021 07:51:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taichi（太极）0.7.20 已经发布，这是专为高性能计算机图形学设计的编程语言。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>此版本具体更新内容如下：</p> 
<ul> 
 <li>[ir]在 printing ReturnStmt 时删除“kernel”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2353" target="_blank">＃2353</a>）</li> 
 <li>[misc] 支持 Python 3.9（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2274" target="_blank">＃2274</a>）</li> 
 <li>[opt] 简化 modulo POT（Stage 1）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2352" target="_blank">＃2352</a>）</li> 
 <li>[opt] 略微简化代数简化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2337" target="_blank">＃2337</a>）</li> 
 <li>[Refactor] 添加一个可调用的类以统一内核和函数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2338" target="_blank">＃2338</a>）</li> 
 <li>[ir] 将 KernelReturnStmt 重命名为 ReturnStmt（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2349" target="_blank">＃2349</a>）</li> 
 <li>[lang] 在序列化器中支持 std::optional 和 enum 类（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2350" target="_blank">＃2350</a>）</li> 
 <li>[IR] 支持 DiffRange shl（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2346" target="_blank">＃2346</a>）</li> 
 <li>[Docker] 通过在 Dockerfile 中增加 CMake 版本来修复 Docker 构建（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2348" target="_blank">＃2348</a>） </li> 
 <li>[ir] [test] 添加对 make_block_local 的测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2343" target="_blank">＃2343</a>）</li> 
 <li>[ir] 添加 ArithmeticInterpretor 来评估 CHI IR 的子集（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2342" target="_blank">＃2342</a>）</li> 
 <li>[opt] 更好地封装 BLS bounds（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2341" target="_blank">＃2341</a>）</li> 
 <li>[Example] cornell_box: 删除未使用的 sphere（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2334" target="_blank">＃2334</a>）</li> 
 <li>[opt] 简化 replace_statements 并改进 demote_dense_struct_fors（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2335" target="_blank">＃2335</a>）</li> 
 <li>[refactor] [test]  重组测试的文件结构（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2336" target="_blank">＃2336</a>）</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.7.20" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.7.20</a></p>
                                        </div>
                                      
</div>
            