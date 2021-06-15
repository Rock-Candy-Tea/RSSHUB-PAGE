
---
title: 'Agileutil v0.0.21 发布, 增加内置web框架，移除sanic依赖'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1560'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 18:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1560'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:left">内置Web框架</h2> 
<p style="text-align:left">Agileutil也可以作为一个web框架来使用, HttpRpcServer在此基础上构建。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><strong>from</strong> <strong>agileutil.http.server</strong> <strong>import</strong> HttpServer, route
<strong>import</strong> <strong>json</strong>

@route(<span style="color:#dd2200">'/test'</span>)
<strong>async</strong> <strong>def</strong> <strong>test</strong>(request):
    a = request.data.get(<span style="color:#dd2200">'a'</span>)
    b = request.data.get(<span style="color:#dd2200">'b'</span>)
    c = <span style="color:#0086b3">int</span>(a) + <span style="color:#0086b3">int</span>(b)
    <strong>return</strong> json.dumps(&#123;<span style="color:#dd2200">'sum'</span>:c&#125;)

hs = HttpServer()
hs.serve()</pre> 
  <p>详情：<a href="https://gitee.com/lycclsltt/agileutil">https://gitee.com/lycclsltt/agileutil</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            