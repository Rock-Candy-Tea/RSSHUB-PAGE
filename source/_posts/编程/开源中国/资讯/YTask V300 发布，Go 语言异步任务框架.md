
---
title: 'YTask V3.0.0 发布，Go 语言异步任务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3752'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 09:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3752'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <h3>YTask</h3> 
 <p style="margin-left:0; margin-right:0">YTask是一个Go语言异步任务框架，其支持所有能被序列化为json的类型。本次更新增加了诸多功能，修复bug，提升了稳定性。</p> 
 <ul> 
  <li>Gitee：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgojuukaze%2FYTask" target="_blank">https://gitee.com/gojuukaze/YTask</a></li> 
  <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgojuukaze%2FYTask" target="_blank">https://github.com/gojuukaze/YTask</a></li> 
  <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.ikaze.cn%2FYTask" target="_blank">https://doc.ikaze.cn/YTask</a></li> 
 </ul> 
 <h3>更新说明</h3> 
 <p style="margin-left:0; margin-right:0">若从v2升级，请先阅读 （If upgrading from v2, please read this first）-><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.ikaze.cn%2FYTask%2Fupgrade.html%23v2v3" target="_blank">从v2升级到v3</a></p> 
 <ul> 
  <li>Improve English documentation<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgojuukaze%2FYTask%2Fwiki" target="_blank">En Doc</a></li> 
  <li>修改目录结构，把broker, backend移出主包。现在不用安装不必要的driver包了</li> 
  <li>broker, backend全部支持连接池 (#27)</li> 
  <li>支持工作流，文档 -><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.ikaze.cn%2FYTask%2Fworkflow.html" target="_blank">https://doc.ikaze.cn/YTask/workflow.html</a> <pre style="margin-left:.5em; margin-right:.5em; text-align:left"><code class="language-go">client<span style="color:#f8f8f2">.</span><span style="color:#e6db74">Workflow<span style="color:#f8f8f2">(</span></span><span style="color:#f8f8f2">)</span><span style="color:#f8f8f2">.</span>
     <span style="color:#e6db74">Send<span style="color:#f8f8f2">(</span></span><span style="color:#a6e22e">"group1"</span><span style="color:#f8f8f2">,</span> <span style="color:#a6e22e">"add"</span><span style="color:#f8f8f2">,</span> <span style="color:#ae81ff">123</span><span style="color:#f8f8f2">,</span> <span style="color:#ae81ff">44</span><span style="color:#f8f8f2">)</span><span style="color:#f8f8f2">.</span>
     <span style="color:#e6db74">Send<span style="color:#f8f8f2">(</span></span><span style="color:#a6e22e">"group1"</span><span style="color:#f8f8f2">,</span> <span style="color:#a6e22e">"add"</span><span style="color:#f8f8f2">)</span><span style="color:#f8f8f2">.</span>
     <span style="color:#e6db74">Done<span style="color:#f8f8f2">(</span></span><span style="color:#f8f8f2">)</span>
</code></pre> </li> 
  <li>支持中止任务(#22) ，文档 -><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.ikaze.cn%2FYTask%2FabortTask.html" target="_blank">https://doc.ikaze.cn/YTask/abortTask.html</a></li> 
  <li>修复log行号输出bug</li> 
  <li>修改队列名拼写错误，修改msg结构体</li> 
  <li>TaskCtl移动到server包中，结构体内的某些字段移动到msg中 ( 从v2升级时需要注意 )</li> 
  <li>通过TaskCtl获取重试次数时需要通过<span> </span><code>ctl.GetRetryCount()</code></li> 
  <li>不在支持RocketMq ，具体说明见:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgojuukaze%2FYTask%2Ftree%2Fmaster%2Fdrives%2Frocketmq" target="_blank">drives/rocketmq</a></li> 
 </ul> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            