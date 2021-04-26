
---
title: 'Taichi（太极）0.7.17 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 07:50:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taichi（太极）0.7.17 已经发布，这是专为高性能计算机图形学设计的编程语言。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0316/070528_Jp1b_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>此版本具体更新内容如下：</p> 
<ul> 
 <li>[Lang] 添加 ti.randn</li> 
 <li>[ir] [refactor] 将 StackXStmt 重命名为 AdStackXStmt</li> 
 <li>[ir] 将 set_arg_nparray 重命名为 set_arg_external_array</li> 
 <li>[ir] [refactor] 删除 OffloadedStmt::step</li> 
 <li>[test] 增加一个测试，对 indices of reversed loops 进行范围分析</li> 
 <li>[refactor] 删除 legacy C++ frontend macros</li> 
 <li>[IR] 为所有语句添加内联文档</li> 
 <li>[ir] 将 is_np_array 重命名为 is_external_array，但前端除外</li> 
 <li>[opt] 避免为 BLS 递归生成两次索引</li> 
 <li>[refactor] 在 python/taichi/misc、python/taichi/main 和测试中统一 ti_core 的用法为 _ti_core</li> 
 <li>[misc] 更新 README.md</li> 
 <li>[ir] 将 uniquely_accessed_bit_structs 从 compile_to_offloads 移到 AnalysisManager</li> 
 <li>[ir] 移除 clone 中的 type_check</li> 
 <li>[type] [opt] 对具有非共享指数的 CustomFloatType 使用 BitStructStoreStmt</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.7.17" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.7.17</a></p>
                                        </div>
                                      
</div>
            