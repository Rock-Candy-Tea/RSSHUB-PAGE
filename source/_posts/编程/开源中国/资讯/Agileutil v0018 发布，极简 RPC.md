
---
title: 'Agileutil v0.0.18 发布，极简 RPC'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/lycclsltt/agileutil/raw/master/docs/pic1.jpeg'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 17:01:00 GMT
thumbnail: 'https://gitee.com/lycclsltt/agileutil/raw/master/docs/pic1.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:left">简介</h2> 
<p style="text-align:left">Agileutil是一个Python3 RPC框架，client和server既可以直连，也可以通过Consul做服务注册发现。</p> 
<h2 style="text-align:left">特性</h2> 
<ul> 
 <li>像本地函数一样调用</li> 
 <li>使用简单，用户只需要关注业务即可</li> 
 <li>HTTP/UDP/TCP 全协议支持</li> 
 <li>支持异步 async/await</li> 
</ul> 
<h2 style="text-align:left">安装</h2> 
<p style="text-align:left">Python 版本 >= 3.6</p> 
<div style="text-align:left"> 
 <div> 
  <pre>pip install agileutil</pre> 
 </div> 
</div> 
<h2 style="text-align:left">快速开始</h2> 
<p style="text-align:left">创建文件myservice.py</p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.rpc</strong> <strong>import</strong> rpc

@rpc
<strong>def</strong> <strong>hello</strong>(name):
    <strong>return</strong> <span style="color:#dd2200">'hello '</span> + name</pre> 
 </div> 
</div> 
<p style="text-align:left">启动：</p> 
<div style="text-align:left"> 
 <div> 
  <pre>agileutil <span style="color:#000080">--run</span> myservice</pre> 
 </div> 
</div> 
<p style="text-align:left"><img alt="pic1.jpeg" src="https://gitee.com/lycclsltt/agileutil/raw/master/docs/pic1.jpeg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">详细介绍：<a href="https://gitee.com/lycclsltt/agileutil">https://gitee.com/lycclsltt/agileutil</a></p>
                                        </div>
                                      
</div>
            