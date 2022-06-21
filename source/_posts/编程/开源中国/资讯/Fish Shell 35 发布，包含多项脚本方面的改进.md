
---
title: 'Fish Shell 3.5 发布，包含多项脚本方面的改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8ac37b9a595ea6b4d16839034fa3b00e68f.png'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 07:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8ac37b9a595ea6b4d16839034fa3b00e68f.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#121212">Fish Shell 近日发布了重要版本 3.5.0。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">fish 是适用于 Linux、macOS 的命令行 Shell，其名字取于 "the<span> </span></span><strong style="color:#333333">f</strong><span style="background-color:#ffffff; color:#333333">riendly<span> </span></span><strong style="color:#333333">i</strong><span style="background-color:#ffffff; color:#333333">nteractive<span> </span></span><strong style="color:#333333">sh</strong><span style="background-color:#ffffff; color:#333333">ell" 的简称，最大特点就是方便易用、功能强大、智能并且用户友好。很多其他 Shell 需要配置才有的功能，fish 默认提供，不需要任何配置。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8ac37b9a595ea6b4d16839034fa3b00e68f.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#121212">值得关注的变化：</span></p> 
<ul> 
 <li>改进脚本处理 
  <ul> 
   <li><code><span><span>math</span></span></code>现在可以将下划线 ( <code><span><span>_</span></span></code>) 处理为数字中的可视分隔符</li> 
   <li><code><span><span>read</span></span></code>现在作为管道中的最后一个进程提供更快的速度</li> 
   <li>直接跟随变量扩展的带引号的命令替换（如<code><span>echo</span><span> </span><span>"$var$(echo</span><span> </span><span>x)"</span></code>）不会影响变量扩展</li> 
  </ul> </li> 
 <li>改进自动补全命令行</li> 
 <li>增强绑定</li> 
 <li>脚本支持捕捉和处理 SIGINT 以及 SIGTERM 信号</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#121212"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffishshell.com%2Fdocs%2Fcurrent%2Frelnotes.html%23fish-3-5-0-released-june-16-2022" target="_blank">详细更新说明查看发布公告</a>。</span></p>
                                        </div>
                                      
</div>
            