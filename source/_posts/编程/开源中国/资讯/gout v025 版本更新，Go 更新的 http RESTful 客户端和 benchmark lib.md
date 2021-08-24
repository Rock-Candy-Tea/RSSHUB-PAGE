
---
title: 'gout v0.2.5 版本更新，Go 更新的 http RESTful 客户端和 benchmark lib'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3989'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 13:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3989'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">项目</h2> 
<p><a href="https://gitee.com/guonaihong/gout">https://gitee.com/guonaihong/gout</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout" target="_blank">https://github.com/guonaihong/gout</a></p> 
<h2 style="text-align:start">feature</h2> 
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
 <li>等等更多</li> 
</ul> 
<p>更新更新内容</p> 
<p>1. 通过静态分析工具, 扫描代码, 减少报警</p> 
<p>2.</p> 
<p style="text-align:start">本次功能优化在使用query string时，可以使用更丰富的数据结构。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">query</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">A</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`query:"a"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/"</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetQuery</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">query</span>&#123;<span style="color:var(--color-prettylights-syntax-constant)">A</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"1"</span>, <span style="color:var(--color-prettylights-syntax-string)">"2"</span>, <span style="color:var(--color-prettylights-syntax-string)">"3"</span>&#125;&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
&#125;</pre> 
</div> 
<p style="text-align:start">客户端请求的包如下:</p> 
<div style="text-align:start"> 
 <pre><code>GET /?a=1&a=2&a=3 HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: Go-http-client/1.1
Accept-Encoding: gzip</code></pre> 
</div>
                                        </div>
                                      
</div>
            