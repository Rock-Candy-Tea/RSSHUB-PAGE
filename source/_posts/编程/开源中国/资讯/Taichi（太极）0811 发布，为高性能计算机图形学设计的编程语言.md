
---
title: 'Taichi（太极）0.8.11 发布，为高性能计算机图形学设计的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
author: 开源中国
comments: false
date: Sun, 30 Jan 2022 07:43:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Taichi（太极）0.8.11 已经发布，这是专为高性能计算机图形学设计的编程语言。</span></p> 
<p style="margin-left:0; margin-right:0"><img height="287" src="https://static.oschina.net/uploads/space/2022/0105/070330_1REO_4937141.gif" width="512" referrerpolicy="no-referrer"></p> 
<div> 
 <div> 
  <div> 
   <p style="margin-left:0; margin-right:0"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这是 v0.8.10 的错误修复版本。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果你在 Windows 上看到如下过多警告，建议升级到此版本。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
   <ul> 
    <li><strong>Bug 修复</strong> 
     <ul> 
      <li>[bug] 修复 windows 上外部函数的警告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4079" target="_blank">#4079</a> )</li> 
     </ul> </li> 
   </ul> 
   <div> 
    <pre><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><span><span><span><span style="background-color:var(--color-canvas-subtle)"><code>a.py:11: UserWarning: Calling non-taichi function "ti.random". Scope inside the function is not processed by the Taichi AST transformer. The function may not work as expected. Proceed with caution! Maybe you can consider turning it into a @ti.func? a[i] = ti.pow(ti.random(), 2) a.py:11: UserWarning: Calling non-taichi function "ti.pow". Scope inside the function is not processed by the Taichi AST transformer. The function may not work as expected. Proceed with caution! Maybe you can consider turning it into a @ti.func? a[i] = ti.pow(ti.random(), 2) </code></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></pre> 
   </div> 
   <p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>完整的变更日志：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
   <ul> 
    <li>[bug] 修复 windows 上外部函数的警告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4079" target="_blank">#4079</a> )</li> 
    <li>[misc] 版本升级：v0.8.10 -> v0.8.11（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4053" target="_blank">#4053</a>）</li> 
    <li>[test] [example] 为 cornell box 添加测试和视频生成。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fpull%2F4045" target="_blank">#4045</a>）</li> 
   </ul> 
   <p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv0.8.11" target="_blank">https://github.com/taichi-dev/taichi/releases/tag/v0.8.11</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            