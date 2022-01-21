
---
title: 'Taichi（太极）0.8.10 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2415'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2415'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">Taichi（太极）0.8.10 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="margin-left:0"><span style="color:#333333">此版本亮点内容如下：</span></p> 
<ul> 
 <li><strong>AOT</strong> 
  <ul> 
   <li>添加一组通用的 AOT 结构 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3973" target="_blank">#3973</a> )</li> 
   <li>切换 vulkan aot 以使用 taichi::aot::ModuleData</li> 
   <li>将 opengl aot 转换为 dump ModuleData ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3991" target="_blank">#3991</a> )</li> 
  </ul> </li> 
 <li><strong>Language and syntax</strong> 
  <ul> 
   <li>使用 FrontendExprStmt 代替 FrontendEvalStmt ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3978" target="_blank">#3978</a> )</li> 
   <li>使用 <strong>globals </strong>获取全局变量( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3949" target="_blank">#3949</a> )</li> 
   <li>支持静态短路 bool 运算 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3958" target="_blank">#3958</a> )</li> 
   <li>实验性自动 mesh_local ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3989" target="_blank">#3989</a> )</li> 
   <li>支持嵌套的 mesh-for ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3990" target="_blank">#3990</a> )</li> 
  </ul> </li> 
 <li><strong>Performance</strong> 
  <ul> 
   <li>加速 whole_kernel_cse pass ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3957" target="_blank">#3957</a> )</li> 
   <li>摆脱线性搜索中的一些 no-ops</li> 
   <li>减少内核启动上下文构建开销 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3947" target="_blank">#3947</a> )</li> 
   <li>重构 func body 以减少 python 开销并提高可读性 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3984" target="_blank">#3984</a> )</li> 
   <li>让 store_to_load_forwarding 与本地张量一起在基本块中工作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3942" target="_blank">#3942</a> )</li> 
  </ul> </li> 
 <li><strong>Documentations</strong> 
  <ul> 
   <li>更新文档预览设置。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4021" target="_blank">#4021</a> )</li> 
   <li>添加编译时递归的 doc ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3994" target="_blank">#3994</a> )</li> 
   <li>添加操作页面（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4004" target="_blank">#4004</a>）</li> 
   <li>改进类型系统文档 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4002" target="_blank">#4002</a> )</li> 
  </ul> </li> 
 <li><strong>Error messages</strong> 
  <ul> 
   <li>添加 TaichiTypeError ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3964" target="_blank">#3964</a> )</li> 
   <li>用户调用外部函数时产生警告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4007" target="_blank">#4007</a> )</li> 
   <li>缩短 TaichiCompilationError 的 traceback 长度 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3965" target="_blank">#3965</a> )</li> 
   <li>遇到未定义名称时引发异常 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3951" target="_blank">#3951</a> )</li> 
  </ul> </li> 
 <li><strong>Bug 修复</strong> 
  <ul> 
   <li>修复在 TI_WITH_LLVM=OFF 下构建会失败的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4043" target="_blank">#4043</a> )</li> 
   <li>将 PtrOffsetStmt 视为随机初始化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F3998" target="_blank">#3998</a> ))</li> 
   <li>GGUI imwrite BGRA 到 RGBA 的转换 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4018" target="_blank">#4018</a> )</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.8.10" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.8.10</a></p>
                                        </div>
                                      
</div>
            