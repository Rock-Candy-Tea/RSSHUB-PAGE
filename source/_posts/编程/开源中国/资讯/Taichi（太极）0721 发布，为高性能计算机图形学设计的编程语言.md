
---
title: 'Taichi（太极）0.7.21 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 07:01:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Taichi（太极）0.7.21 已经发布，这是专为高性能计算机图形学设计的编程语言。</p> 
<p><img alt src="https://static.oschina.net/uploads/space/2021/0611/070135_jaaS_2744687.gif" referrerpolicy="no-referrer"></p> 
<p>此版本具体更新内容如下：</p> 
<ul> 
 <li>[CI] 修改了build.py，使之在所有上传中使用 token （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2408" target="_blank">#2408</a>）</li> 
 <li>[CI] 配置 Jenkinsfile 以支持 nightly test（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2405" target="_blank">#2405</a>）</li> 
 <li>[ir] 在 IR Builder 中添加 random 和 atomic 语句 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2379" target="_blank">#2379</a> )</li> 
 <li>[lang] 修复旧版 GCC 上找不到的 filesystem header ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2401" target="_blank">#2401</a> )</li> 
 <li>[Metal] 使从 aot 转储的文件名可配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2402" target="_blank">#2402</a>）</li> 
 <li>[Misc] 修复了 mass_spring_3d.py 在导入错误时不退出的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2400" target="_blank">#2400</a> )</li> 
 <li>[lang] 为 refine_coordinates 添加测试（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2382" target="_blank">#2382</a>）</li> 
 <li>[CI] 简化的 github CI 程序。（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2399" target="_blank">#2399</a>）</li> 
 <li>[CI] 支持自动取消之前提交的 workflows ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2397" target="_blank">#2397</a> )</li> 
 <li>[CI] 恢复格式检查，添加依赖（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2394" target="_blank">#2394</a>）</li> 
 <li>[Opt] 优化嵌套类型转换 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2390" target="_blank">#2390</a> )</li> 
 <li>[type] [bug] 移除位指针结构的冗余组件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2393" target="_blank">#2393</a> )</li> 
 <li>[CI] 在 pull request 中添加 comment dispatch 以支持自动格式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2392" target="_blank">#2392</a>）</li> 
 <li>[Doc] 添加更多关于 fast_gui 的文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2385" target="_blank">#2385</a> )</li> 
 <li>[metal] 修复 un-materialized runtime 而导致的 Nonetype ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2389" target="_blank">#2389</a> )</li> 
 <li>[Doc] 更新关于 LLVM_DIR 的开发者安装文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2384" target="_blank">#2384</a> )</li> 
 <li>[metal] 为 metal 添加 AOT module builder ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2372" target="_blank">#2372</a> )</li> 
 <li>[ir] 将 nodiscard 添加到 get_loop_guard/get_if_guard ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2377" target="_blank">#2377</a> )</li> 
 <li>[vulkan] 添加 Vulkan API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F2376" target="_blank">#2376</a> )</li> 
 <li>......</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.7.21" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.7.21</a> </p>
                                        </div>
                                      
</div>
            