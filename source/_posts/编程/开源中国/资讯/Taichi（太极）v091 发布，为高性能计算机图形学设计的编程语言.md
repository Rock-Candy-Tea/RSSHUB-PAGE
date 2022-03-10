
---
title: 'Taichi（太极）v0.9.1 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 07:02:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Taichi（太极）v0.9.1 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h4><strong><span style="background-color:#ffffff; color:#24292f">Highlights</span></strong></h4> 
<ul> 
 <li><strong>CI/CD workflow</strong> 
  <ul> 
   <li>窗口测试前清理工作区 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4405" target="_blank">#4405</a> )</li> 
  </ul> </li> 
 <li><strong>Documentation</strong> 
  <ul> 
   <li>更新 ops 中函数的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4465" target="_blank">#4465</a> )</li> 
   <li>更新 misc 中函数的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4474" target="_blank">#4474</a> )</li> 
   <li>更新 misc 中的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4446" target="_blank">#4446</a> )</li> 
   <li>更新 operations 中函数的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4427" target="_blank">#4427</a> ) </li> 
   <li>更新 PyTorch 接口文档（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4311" target="_blank">#4311</a>）</li> 
   <li>更新 operations 中函数的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4413" target="_blank">#4413</a> )</li> 
   <li>更新 operations 中函数的文档字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4392" target="_blank">#4392</a> ) </li> 
   <li>修复断开的链接 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4368" target="_blank">#4368</a> ) </li> 
   <li>重新整理文章：Getting-started，gui ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4360" target="_blank">#4360</a> ) </li> 
  </ul> </li> 
 <li><strong>Error messages</strong> 
  <ul> 
   <li>添加当内核参数中的元素数量超过时的错误消息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4444" target="_blank">#4444</a>）</li> 
   <li>添加无效节点大小的错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4460" target="_blank">#4460</a>）</li> 
   <li>为文字的错误类型注释添加错误消息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4462" target="_blank">#4462</a> ) </li> 
   <li>删除错误信息中提到的 ti.pyfunc ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4429" target="_blank">#4429</a> )</li> 
  </ul> </li> 
 <li><strong>Language and syntax</strong> 
  <ul> 
   <li>支持稀疏矩阵生成器数据类型配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4411" target="_blank">#4411</a> )</li> 
   <li>支持文字的类型注解 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4440" target="_blank">#4440</a> ) </li> 
   <li>支持简单矩阵切片 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4420" target="_blank">#4420</a> ) </li> 
   <li>支持内核返回矩阵类型值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4062" target="_blank">#4062</a>）</li> 
  </ul> </li> 
 <li><strong>Vulkan backend</strong> 
  <ul> 
   <li>使用 cuda 时启用 Vulkan 设备选择 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4330" target="_blank">#4330</a> ) </li> 
  </ul> </li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.9.1" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.9.1</a></p>
                                        </div>
                                      
</div>
            