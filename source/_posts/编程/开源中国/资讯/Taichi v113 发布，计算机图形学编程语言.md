
---
title: 'Taichi v1.1.3 发布，计算机图形学编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 07:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Taichi <span style="background-color:#ffffff; color:#333333">是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前 Taichi v1.1.3 发布了，此版本带来大量改进，摘录如下：</p> 
<ul> 
 <li><strong>模块</strong> 
  <ul> 
   <li>添加纹理接口到 C-API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5520" target="_blank">#5520</a> ) </li> 
  </ul> </li> 
 <li><strong>Bug修复</strong> 
  <ul> 
   <li>使用 MacOS 禁用 vkCmdWriteTimestamp ，以在 Vulkan 上启用测试 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6020" target="_blank">#6020</a> )</li> 
   <li>修复打印 i8/u8 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5893" target="_blank">#5893</a> )</li> 
   <li>修复存储 quant 浮点数的 codegen 中的错误类型转换 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5818" target="_blank">#5818</a> )</li> 
   <li>移除错误优化：Float x // 1 -> x ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5672" target="_blank">#5672</a> ) </li> 
  </ul> </li> 
 <li><strong>构建系统</strong> 
  <ul> 
   <li>清理 Taichi core cmake ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5595" target="_blank">#5595</a> )</li> 
  </ul> </li> 
 <li><strong>CI/CD 工作流程</strong> 
  <ul> 
   <li>更新 torch 和 cuda 版本 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6054" target="_blank">#6054</a> ) </li> 
  </ul> </li> 
 <li><strong>错误信息</strong> 
  <ul> 
   <li>为内部非静态 if 中断/继续静态时添加错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5755" target="_blank">#5755</a> )</li> 
   <li>离线缓存路径不存在时不显示警告（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5747" target="_blank">#5747</a>）</li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>语言和句法</strong></p> 
<ul> 
 <li>排序 coo ，以在 GPU 上构建正确的 csr 格式稀疏矩阵 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6050" target="_blank">#6050</a> )</li> 
 <li>MatrixNdarray 重构第 6 部分：使用 TensorType 为 LocalLoadStmt 和 GlobalLoadStmt 添加标量化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6024" target="_blank">#6024</a> ) </li> 
 <li>MatrixField refactor 4/n: Disallow invalid matrix field definition ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6074" target="_blank">#6074</a> )</li> 
 <li>修复矩阵向量乘法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6014" target="_blank">#6014</a> ) </li> 
 <li>MatrixNdarray 重构第 5 部分：使用 TensorType 为 LocalStoreStmt 和 GlobalStoreStmt 添加标量化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5946" target="_blank">#5946</a> )</li> 
 <li>弃用 NdarrayMatrix/NdarrayVector 的 SOA 布局 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6030" target="_blank">#6030</a> ) </li> 
 <li>索引新的本地矩阵实现 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5783" target="_blank">#5783</a> ) </li> 
 <li>使标量内核参数不可变（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5990" target="_blank">#5990</a>）</li> 
 <li>用整数指数降级 pow() ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6044" target="_blank">#6044</a> ) </li> 
 <li>支持 abs(i64) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6018" target="_blank">#6018</a> ) </li> 
 <li>MatrixNdarray 重构第 4 部分：将 TensorType 降低到 CHI IR 级别，用于元素索引的 MatrixNdarray ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5936" target="_blank">#5936</a> )</li> 
 <li>MatrixNdarray 重构 part3: Enable TensorType for MatrixNdarray at Frontend IR level ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5900" target="_blank">#5900</a> )</li> 
 <li>使用 cuSolver 在 GPU 上支持线性系统求解 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5860" target="_blank">( #5860</a> )</li> 
 <li>MatrixNdarray 重构第 2 部分：删除 python-scope AnyArray 中的冗余成员（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5885" target="_blank">#5885</a>）</li> 
 <li>MatrixNdarray 重构第 1 部分：重构 Taichi 内核参数以使用 TensorType ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5881" target="_blank">#5881</a> )</li> 
 <li>MatrixNdarray 重构 part0：支持在 Ndarray 中直接构造 TensorType 并使用 element_shape 重构 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5875" target="_blank">#5875</a> )</li> 
 <li>启用局部矩阵/向量的定义（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5782" target="_blank">#5782</a>）</li> 
 <li>使用 coo 格式 ndarray 在 GPU 上构建 csr 稀疏矩阵 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5838" target="_blank">#5838</a> )</li> 
 <li>为选定的 MatrixNdarray/VectorNdarray 方法添加 @python_scope 装饰器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5844" target="_blank">#5844</a>）</li> 
 <li>使 python 范围比较返回 1 而不是 -1 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5840" target="_blank">#5840</a> )</li> 
 <li>允许在 if 条件中隐式转换整数类型 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5763" target="_blank">#5763</a> ）</li> 
 <li>支持 GPU 上的稀疏矩阵 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5185" target="_blank">#5185</a> )</li> 
 <li>改进循环错误消息并删除对真实类型 id 的检查（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5792" target="_blank">#5792</a>）</li> 
 <li>实现矩阵/向量的索引验证 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5605" target="_blank">#5605</a> ) </li> 
 <li><strong>网状太极</strong> 
  <ul> 
   <li>修复的嵌套网格<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F6062" target="_blank"> ( #6062</a> )</li> 
  </ul> </li> 
 <li><strong>Vulkan 后端</strong> 
  <ul> 
   <li>内部跟踪图像布局 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5597" target="_blank">#5597</a> )</li> 
  </ul> </li> 
</ul> 
<p>完整 Changelog 可查看更新公告： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv1.1.3" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v1.1.3</a></p>
                                        </div>
                                      
</div>
            