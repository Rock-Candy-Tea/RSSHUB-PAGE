
---
title: '计算机图形学编程语言 Taichi（太极）v1.0.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Tue, 19 Jul 2022 07:34:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Taichi（太极）v1.0.4 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h4><strong><span style="background-color:#ffffff; color:#24292f">Highlights</span></strong></h4> 
<ul> 
 <li><strong>Documentation</strong> 
  <ul> 
   <li>修正错别字<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5283" target="_blank">#5283</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>更新 dev_install.md <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5266" target="_blank">#5266</a><span style="background-color:#ffffff; color:#24292f">) </span></li> 
   <li>更新了 README 命令行<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5199" target="_blank">#5199</a><span style="background-color:#ffffff; color:#24292f">)<span> </span></span></li> 
   <li>修改编译警告<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5180" target="_blank">#5180</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>更新了 odop.md，删除了过时的信息<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5163" target="_blank">#5163</a><span style="background-color:#ffffff; color:#24292f">)<span> </span></span></li> 
  </ul> </li> 
 <li><strong>Language and syntax</strong> 
  <ul> 
   <li>Refine SNode with quant 7/n: 支持将 QuantFixedType 置于 quant_array 之下<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5386" target="_blank">#5386</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>为 1d case 添加行列式<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5375" target="_blank">#5375</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>使 floor、ceil 和 round 接受 dtype 可选参数<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5307" target="_blank">#5307</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>重命名 struct_class 为 dataclass<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5365" target="_blank">#5365</a><span style="background-color:#ffffff; color:#24292f">)<span> </span></span></li> 
   <li>改进 ti 示例，以便用户可以通过输入数字来选择运行哪个示例 <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5265" target="_blank">#5265</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>Refine SNode with quant 5/n: 将 bit_array 重命名为 quant_array <span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5344" target="_blank">#5344</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>将 bit_vectorize 设为 ti.loop_config 的参数 <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5334" target="_blank">#5334</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>Refine SNode with quant 3/n: 将 bit_vectorize 转换为一个 on/off switch<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5331" target="_blank">#5331</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>添加缺少 init 调用的错误消息 <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5280" target="_blank">#5280</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>修复 fractal gui 关闭警告 <span style="background-color:#ffffff; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5281" target="_blank">#5281</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>Refine SNode with quant 2/n: 在 bit_vectorize 关闭的情况下，为 bit_array 启用 struct<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5253" target="_blank">#5253</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
   <li>在 AST 中重构索引表达式并强制执行整数索引<span style="background-color:#ffffff; color:#24292f"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F5138" target="_blank">#5138</a><span style="background-color:#ffffff; color:#24292f">)</span></li> 
  </ul> </li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv1.0.4" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v1.0.4</a></p>
                                        </div>
                                      
</div>
            