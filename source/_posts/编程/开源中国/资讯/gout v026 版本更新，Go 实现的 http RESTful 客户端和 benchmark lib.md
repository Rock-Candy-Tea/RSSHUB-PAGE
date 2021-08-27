
---
title: 'gout v0.2.6 版本更新，Go 实现的 http RESTful 客户端和 benchmark lib'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3975'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 03:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3975'
---

<div>   
<div class="content">
                                                                                            <p>项目地址</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout" target="_blank">https://github.com/guonaihong/gout</a></p> 
<p><a href="https://gitee.com/guonaihong/gout">https://gitee.com/guonaihong/gout</a></p> 
<p>本次更新</p> 
<p>绑定数据支持校验</p> 
<pre><code class="language-go">package main

import (
"fmt"
"time"

"github.com/gin-gonic/gin"
"github.com/guonaihong/gout"
)

type bodyJSON struct &#123;
Code int `valid:"required"`
&#125;

func server() &#123;
r := gin.Default()
r.GET("/have", func(c *gin.Context) &#123;
c.JSON(200, gin.H&#123;"code": 200&#125;)
&#125;)

r.GET("/empty", func(c *gin.Context) &#123;

&#125;)

r.Run()
&#125;

func main() &#123;
go server()

time.Sleep(time.Second / 100)

b := bodyJSON&#123;&#125;

err := gout.GET(":8080/have").BindJSON(&b).Do()
fmt.Println(b, err)

b = bodyJSON&#123;&#125;
// 这里会报错, 因为bodyJSON里面的值为空, 到达数据校验的目的
err = gout.GET(":8080/empty").BindJSON(&b).Do()
fmt.Println(err)
&#125;
</code></pre> 
<h2>feature</h2> 
<ul> 
 <li>支持设置 GET/PUT/DELETE/PATH/HEAD/OPTIONS</li> 
 <li>支持设置请求 http header(可传 struct,map,array,slice 等类型)</li> 
 <li>支持设置 URL query(可传 struct,map,array,slice,string 等类型)</li> 
 <li>支持设置 json 编码到请求 body 里面(可传struct, map, string, []byte 等类型)</li> 
 <li>支持设置 xml 编码到请求 body 里面(可传struct, string, []byte 等类型)</li> 
 <li>支持设置 yaml 编码到请求 body 里面(可传struct, map, string, []byte 等类型)</li> 
 <li>支持设置 protobuf 编码到请求 body里面(可传struct)</li> 
 <li>支持设置 form-data(可传 struct, map, array, slice 等类型)</li> 
 <li>支持设置 x-www-form-urlencoded(可传 struct,map,array,slice 等类型)</li> 
 <li>支持设置 io.Reader，uint/uint8/uint16...int/int8...string...[]byte...float32,float64 至请求 body 里面</li> 
 <li>支持解析响应body里面的json,xml,yaml至结构体里(BindJSON/BindXML/BindYAML)</li> 
 <li>支持解析响应body的内容至io.Writer, uint/uint8...int/int8...string...[]byte...float32,float64</li> 
 <li>支持解析响应header至结构体里</li> 
 <li>支持接口性能benchmark，可控制压测一定次数还是时间，可控制压测频率</li> 
 <li>支持retry-backoff，可以指定重试条件</li> 
 <li>支持发送裸http数据包</li> 
 <li>支持导出curl命令</li> 
 <li>传入自定义*http.Client</li> 
 <li>支持请求中间件(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantlabs%2Fgout-middleware" target="_blank">https://github.com/antlabs/gout-middleware</a>)</li> 
 <li>支持设置chunked数据格式发送</li> 
 <li>支持body, header的数据校验</li> 
 <li>等等更多</li> 
</ul>
                                        </div>
                                      
</div>
            