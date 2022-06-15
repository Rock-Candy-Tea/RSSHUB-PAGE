
---
title: '计算机图形学编程语言 Taichi（太极）发布 1.0.3 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9499'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9499'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">专为高性能计算机图形学设计的编程语言 Taichi（太极）已经发布 1.0.3 版本，这是一个维护版本，带来模块更新和一些 Bug 修复。主要内容如下：</p> 
<p><strong>模块</strong></p> 
<ul> 
 <li>支持导入外部 Vulkan 缓冲区 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5020" target="_blank">#5020</a> )</li> 
 <li>支持将 taichi 作为 AOT 模块的子目录 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5007" target="_blank">#5007</a> )</li> 
</ul> 
<p><strong>Bug修复</strong></p> 
<ul> 
 <li>修复读取整个 bit_struct 的前端类型检查 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5027" target="_blank">#5027</a> )</li> 
 <li>降低 FrontendWhileStmt 时删除多余的 AllocStmt ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4870" target="_blank">#4870</a> )</li> 
</ul> 
<p style="margin-left:0px"><strong>构建系统</strong></p> 
<ul> 
 <li>改进 Windows 构建脚本 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4955" target="_blank">#4955</a> )</li> 
 <li>改进了 Windows 上的构建 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4925" target="_blank">#4925</a> )</li> 
 <li>定义 Cmake OpenGL 运行时目标 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4887" target="_blank">#4887</a> )</li> 
 <li>使用关键字而不是普通的 target_link_libraries CMake ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4864" target="_blank">#4864</a> )</li> 
 <li>定义运行时构建目标 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4838" target="_blank">#4838</a> )</li> 
 <li>切换到 scikit-build 作为构建后端 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4624" target="_blank">#4624</a> )</li> 
</ul> 
<p><strong>用例</strong></p> 
<ul> 
 <li>修复 ggui 中的 block_dim 警告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5128" target="_blank">#5128</a> )</li> 
 <li>更新mass_spring_3d_ggui.py的视觉效果（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5081" target="_blank">#5081</a>）</li> 
 <li>将 mass_spring_3d_ggui.py 更新到 v2 <span style="color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3879" target="_blank">#3879</a><span style="color:#24292f">)</span></li> 
</ul> 
<p><strong>语言和句法</strong></p> 
<ul> 
 <li>为 glsl 矩阵类型添加更多初始化例程 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5069" target="_blank">#5069</a> )</li> 
 <li>支持从 ti.ndarray() 构造向量和矩阵 ndarray</li> 
 <li>禁止读取整个 bit_struct ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5061" target="_blank">#5061</a> )</li> 
 <li>结构类实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4989" target="_blank">#4989</a>)</li> 
 <li>添加短路 if-then-else 运算符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5022" target="_blank">#5022</a>）</li> 
 <li>从 ndarray 构建稀疏矩阵 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4841" target="_blank">(#4841</a>)</li> 
 <li>修复使用数学向量和矩阵类型时潜在的精度错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5032" target="_blank">#5032</a> )</li> 
 <li>重构 quant 类型定义 API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5036" target="_blank">#5036</a> )</li> 
</ul> 
<p> </p> 
<p>其他内容可查更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv1.0.3" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v1.0.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            