
---
title: 'Taichi（太极）0.8.4 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif'
author: 开源中国
comments: false
date: Wed, 03 Nov 2021 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taichi（太极）0.8.4 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img src="https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本具体更新内容如下：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>[bug] 将默认值添加到 print_preprocessed_ir ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3292" target="_blank">#3292</a> )</li> 
 <li>[Doc] 更正关于 dev 安装的说明 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3289" target="_blank">#3289</a> ) </li> 
 <li>[refactor] [misc] 重构性能监控基准代码（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3269" target="_blank">#3269</a>）</li> 
 <li>[Lang] 为 LLVM 后端支持更多 SNode trees（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3279" target="_blank">#3279</a>）</li> 
 <li>[Refactor] Taichi 前端 AST 构建器，无需生成代码 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3037" target="_blank">#3037</a> ) </li> 
 <li>[ci] 将 artifacts 保留时间减少到 20 天 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3286" target="_blank">#3286</a> ) </li> 
 <li>[ir] [refactor] 删除 C++ Expr 类中的 ptr_if_global ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3285" target="_blank">#3285</a> ) </li> 
 <li>[doc] 在 dev 安装说明中为子模块添加 using clang++  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3273" target="_blank">#3273</a> )</li> 
 <li>更新 sparse.md ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3266" target="_blank">#3266</a> )</li> 
 <li>[vulkan] 索引加载代码生成器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3259" target="_blank">#3259</a>）</li> 
 <li>[opengl] 移除 listgen 支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3257" target="_blank">#3257</a> ) </li> 
 <li>[llvm] 在 LLVM 后端将 compile_snode_tree_types 与 materialize_snode_tree 分开（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3267" target="_blank">#3267</a>）</li> 
 <li>[Lang] 为 Ndarray 添加元素形状 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3264" target="_blank">#3264</a> ) </li> 
 <li>更新 write_test.md ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3263" target="_blank">#3263</a> ) </li> 
 <li>[ci] 将解压压缩文件移动到 ci_download.py ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3251" target="_blank">#3251</a> )</li> 
 <li>[Lang] 修复字符串格式不支持关键字格式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3256" target="_blank">#3256</a> )</li> 
 <li>[vulkan] 在 Apple 上强制使用 u8 功能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3252" target="_blank">#3252</a>）</li> 
 <li>[vulkan] 从 button_id_to_name/buttom_name_to_id 捕获 std::runtime_error。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3260" target="_blank">#3260</a> ) </li> 
 <li>[cuda] 添加 CUDA 版本检查 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3249" target="_blank">#3249</a> )</li> 
 <li>[<span style="background-color:#ffffff; color:#24292f">refactor</span>] 删除 snode_rw_accessors_bank 中的冗余代码 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3192" target="_blank">#3192</a> ) </li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看发布说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.8.4" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.8.4</a></p>
                                        </div>
                                      
</div>
            