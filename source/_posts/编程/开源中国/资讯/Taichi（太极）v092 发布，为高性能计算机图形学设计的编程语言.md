
---
title: 'Taichi（太极）v0.9.2 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Fri, 25 Mar 2022 07:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Taichi（太极）v0.9.2 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h4><strong><span style="background-color:#ffffff; color:#24292f">Highlights</span></strong></h4> 
<ul> 
 <li><strong>CI/CD workflow</strong> 
  <ul> 
   <li>在发布工作流程中生成 manylinux2014-compatible wheels with CUDA backend ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4550" target="_blank">#4550</a> ) </li> 
  </ul> </li> 
 <li><strong>Command line interface</strong> 
  <ul> 
   <li>修复 taichi gallery 命令中的一些错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4548" target="_blank">#4548</a>）</li> 
  </ul> </li> 
 <li><strong>Documentation</strong> 
  <ul> 
   <li>调整 CPU GUI 文档布局 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4605" target="_blank">#4605</a>)</li> 
   <li>重构类型系统（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4584" target="_blank">#4584</a>）</li> 
   <li>修复了 broken links（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4563" target="_blank">#4563</a>）</li> 
   <li>重构 README.md (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4549" target="_blank">#4549</a>) </li> 
   <li>创建 CODE_OF_CONDUCT (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4564" target="_blank">#4564</a>) </li> 
   <li>更新 syntax.md (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4557" target="_blank">#4557</a>) </li> 
   <li>更新 ndrange 的文档字符串 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4486" target="_blank">#4486</a>) </li> 
   <li>Minor updates：建议输入提示参数和返回值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4510" target="_blank">#4510</a>) </li> 
   <li>重构内核和函数。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4496" target="_blank">#4496</a>）</li> 
   <li>添加初始变量和片段（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4457" target="_blank">#4457</a>）</li> 
  </ul> </li> 
 <li><strong>Language and syntax</strong> 
  <ul> 
   <li>弃用 ext_arr/any_arr 改用 types.ndarray<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4598" target="_blank">#4598</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>添加 taichi gallery 命令供用户选择并在 gui 中运行示例<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4532" target="_blank">#4532</a><span style="background-color:#ffffff; color:#24292f">)<span> </span></span></li> 
   <li>添加 ti.serialize 和 ti.loop_config <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4525" target="_blank">#4525</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>支持简单矩阵切片<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4488" target="_blank">#4488</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>删除构建矩阵的传统方法 <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4521" target="_blank">#4521</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.9.2" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.9.2</a></p>
                                        </div>
                                      
</div>
            