
---
title: 'Fish Shell 3.5 发布，包含多项脚本方面的改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0621/073525_JIIw_5430600.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 07:35:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0621/073525_JIIw_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#121212">Fish Shell 近日发布了重要版本 3.5.0。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">fish 是适用于 Linux、macOS 的命令行 Shell，其名字取于 "the </span><strong>f</strong><span style="color:#333333">riendly </span><strong>i</strong><span style="color:#333333">nteractive </span><strong>sh</strong><span style="color:#333333">ell" 的简称，最大特点就是方便易用、功能强大、智能并且用户友好。很多其他 Shell 需要配置才有的功能，fish 默认提供，不需要任何配置。</span></p> 
<p><img alt height="264" src="https://static.oschina.net/uploads/space/2022/0621/073525_JIIw_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#121212">值得关注的变化：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进脚本处理 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>math</code>现在可以将下划线 ( <code>_</code>) 处理为数字中的可视分隔符</li> 
   <li><code>read</code>现在作为管道中的最后一个进程提供更快的速度</li> 
   <li>直接跟随变量扩展的带引号的命令替换（如<code>echo "$var$(echo x)"</code>）不会影响变量扩展</li> 
  </ul> </li> 
 <li>改进自动补全命令行</li> 
 <li>增强绑定</li> 
 <li>脚本支持捕捉和处理 SIGINT 以及 SIGTERM 信号</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffishshell.com%2Fdocs%2Fcurrent%2Frelnotes.html%23fish-3-5-0-released-june-16-2022" target="_blank"><span style="color:#121212">详细更新说明查看发布公告</span></a><span style="color:#121212">。</span></p>
                                        </div>
                                      
</div>
            