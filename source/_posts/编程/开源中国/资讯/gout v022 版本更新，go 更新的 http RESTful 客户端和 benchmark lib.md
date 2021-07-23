
---
title: 'gout v0.2.2 版本更新，go 更新的 http RESTful 客户端和 benchmark lib'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7325'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 13:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7325'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">项目地址</p> 
<p style="text-align:start"><a href="https://gitee.com/guonaihong/gout">https://gitee.com/guonaihong/gout</a></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout" target="_blank">https://github.com/guonaihong/gout</a></p> 
<p style="text-align:start">本次更新</p> 
<pre style="text-align:start"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
header <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Header</span>)
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// 设置POST方法和url</span>
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/req/body"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 获取所有的响应http header</span>
<span style="color:var(--color-prettylights-syntax-entity)">BindHeader</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>header).
<span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

&#125;</pre> 
<p style="text-align:start">gout 是go写的http 客户端，为提高工作效率而开发</p> 
<p style="text-align:start"><span style="color:#333333">构架</span></p> 
<p style="text-align:start"><span style="color:#333333">feature</span></p> 
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
<h2 style="text-align:start">演示</h2> 
<h2 style="text-align:start">内容</h2> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Installation" target="_blank">Installation</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23example" target="_blank">example</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23quick-start" target="_blank">quick start</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23api-examples" target="_blank">API Examples</a></p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23get-post-put-delete-path-head-options" target="_blank">GET POST PUT DELETE PATH HEAD OPTIONS</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Query-Parameters" target="_blank">Query Parameters</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23http-header" target="_blank">http header</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Set-request-header" target="_blank">Set request header</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Parsing-the-response-header" target="_blank">Parsing the response header</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23get-all-header" target="_blank">get all header</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23http-body" target="_blank">http body</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23body" target="_blank">body</a> 
      <ul> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Set-the-data-to-the-http-request-body" target="_blank">Set the data to the http request body</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Parse-the-response-body-into-a-variable" target="_blank">Parse the response body into a variable</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23json" target="_blank">json</a> 
      <ul> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Serialize-json-to-request-body" target="_blank">Serialize json to request body</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Parsed-http-response-body-in-json-format" target="_blank">Parsed http response body in json format</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23yaml" target="_blank">yaml</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23xml" target="_blank">xml</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23form-data" target="_blank">form-data</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23x-www-form-urlencoded" target="_blank">x-www-form-urlencoded</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23protobuf" target="_blank">protobuf</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23callback" target="_blank">callback</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Set-request-timeout" target="_blank">Set request timeout</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23proxy" target="_blank">proxy</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23socks5" target="_blank">socks5</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23cookie" target="_blank">cookie</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23basic-auth" target="_blank">basic auth</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23context" target="_blank">context</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Cancel-a-sending-request" target="_blank">Cancel a sending request</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23unix-socket" target="_blank">unix socket</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23http2-doc" target="_blank">http2 doc</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23debug-mode" target="_blank">debug mode</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Turn-on-debug-mode" target="_blank">Turn on debug mode</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Turn-off-color-highlighting-in-debug-mode" target="_blank">Turn off color highlighting in debug mode</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Custom-debug-mode" target="_blank">Custom debug mode</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23trace-info" target="_blank">trace info</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23benchmark" target="_blank">benchmark</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23benchmarking-a-certain-number-of-times" target="_blank">benchmarking a certain number of times</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23benchmark-duration" target="_blank">benchmarking for a certain time</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23benchmark-rate" target="_blank">benchmarking at a fixed frequency</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Custom-benchmark-functions" target="_blank">Custom benchmark functions</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23retry-backoff" target="_blank">retry backoff</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23retry-conditions-httpcode" target="_blank">Specify the retry conditions, when equal to a certain http code</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23retry-conditions-backupurl" target="_blank">Specify retry conditions. The default URL cannot be accessed. Use the backup URL</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23import" target="_blank">import</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23send-raw-http-request" target="_blank">send raw http request</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23export" target="_blank">export</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23generate-curl-command" target="_blank">generate curl command</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Incoming-custom-*http.Client" target="_blank">Incoming custom * http.Client</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Using-chunked-data-format" target="_blank">Using chunked data format</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23NewWithOpt" target="_blank">NewWithOpt</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23insecure-skip-verify" target="_blank">Insecure skip verify</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Turn-off-3xx-status-code-automatic-jump" target="_blank">Turn off 3xx status code automatic jump</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23NewWithOpt-set-timeout" target="_blank">NewWithOpt set timeout</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Global-configuration" target="_blank">Global configuration</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23set-timeout" target="_blank">set timeout</a></li> 
    </ul> </li> 
  </ul> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23Unique-features" target="_blank">Unique features</a></p> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23forward-gin-data" target="_blank">forward gin data</a></li> 
  </ul> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%23FAQ" target="_blank">FAQ</a></p> </li> 
</ul> 
<h2 style="text-align:start">Installation</h2> 
<div style="text-align:start"> 
 <pre><code>go get github.com/guonaihong/gout
</code></pre> 
</div> 
<h1 style="text-align:start">example</h1> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%2Fblob%2Fmaster%2F_example" target="_blank">examples</a> 目录下面的例子，都是可以直接跑的。如果觉得运行例子还是不明白用法，可以把你迷惑的地方写出来，然后提<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%2Fissues%2Fnew" target="_blank">issue</a></p> 
<h3 style="text-align:start">运行命令如下</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">cd</span> _example
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> GOPROXY 是打开go module代理，可以更快下载模块</span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:var(--color-prettylights-syntax-comment)">#</span> 第一次运行需要加GOPROXY下载模块，模块已安装的直接 go run 01-color-json.go 即可</span>
env GOPROXY=https://goproxy.cn go run 01-color-json.go</pre> 
</div> 
<h1 style="text-align:start">quick start</h1> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
   <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
   <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
   <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-comment)">// 用于解析 服务端 返回的http body</span>
<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">RspBody</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
   <span style="color:var(--color-prettylights-syntax-constant)">ErrMsg</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"errmsg"`</span>
   <span style="color:var(--color-prettylights-syntax-constant)">ErrCode</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`json:"errcode"`</span>
   <span style="color:var(--color-prettylights-syntax-constant)">Data</span>    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"data"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// 用于解析 服务端 返回的http header</span>
<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">RspHeader</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
   <span style="color:var(--color-prettylights-syntax-constant)">Sid</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`header:"sid"`</span>
   <span style="color:var(--color-prettylights-syntax-constant)">Time</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`header:"time"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
   rsp <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">RspBody</span>&#123;&#125;
   header <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">RspHeader</span>&#123;&#125;

   <span style="color:var(--color-prettylights-syntax-comment)">//code := 0</span>
   err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.

   <span style="color:var(--color-prettylights-syntax-comment)">// POST请求</span>
   <span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:8080"</span>).

   <span style="color:var(--color-prettylights-syntax-comment)">// 打开debug模式</span>
   <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).

   <span style="color:var(--color-prettylights-syntax-comment)">// 设置查询字符串</span>
   <span style="color:var(--color-prettylights-syntax-entity)">SetQuery</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"page"</span>: <span style="color:var(--color-prettylights-syntax-constant)">10</span>, <span style="color:var(--color-prettylights-syntax-string)">"size"</span>: <span style="color:var(--color-prettylights-syntax-constant)">10</span>&#125;).

   <span style="color:var(--color-prettylights-syntax-comment)">// 设置http header</span>
   <span style="color:var(--color-prettylights-syntax-entity)">SetHeader</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"X-IP"</span>: <span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1"</span>, <span style="color:var(--color-prettylights-syntax-string)">"sid"</span>: fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%x"</span>, time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">UnixNano</span>())&#125;).

   <span style="color:var(--color-prettylights-syntax-comment)">// SetJSON设置http body为json</span>
   <span style="color:var(--color-prettylights-syntax-comment)">// 同类函数有SetBody, SetYAML, SetXML, SetForm, SetWWWForm</span>
   <span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"text"</span>: <span style="color:var(--color-prettylights-syntax-string)">"gout"</span>&#125;).

   <span style="color:var(--color-prettylights-syntax-comment)">// BindJSON解析返回的body内容</span>
   <span style="color:var(--color-prettylights-syntax-comment)">// 同类函数有BindBody, BindYAML, BindXML</span>
   <span style="color:var(--color-prettylights-syntax-entity)">BindJSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>rsp).

   <span style="color:var(--color-prettylights-syntax-comment)">// 解析返回的http header</span>
   <span style="color:var(--color-prettylights-syntax-entity)">BindHeader</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>header).
   <span style="color:var(--color-prettylights-syntax-comment)">// http code</span>
   <span style="color:var(--color-prettylights-syntax-comment)">// Code(&code).</span>

   <span style="color:var(--color-prettylights-syntax-comment)">// 结束函数</span>
   <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

   <span style="color:var(--color-prettylights-syntax-comment)">// 判断错误</span>
   <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
   fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"send fail:%s\n"</span>, err)
   &#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> POST /?page=10&size=10 HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> Sid: 15d9b742ef32c130</span>
<span style="color:var(--color-prettylights-syntax-comment)">> X-Ip: 127.0.0.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> Content-Type: application/json</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">&#123;</span>
<span style="color:var(--color-prettylights-syntax-comment)">   "text": "gout"</span>
<span style="color:var(--color-prettylights-syntax-comment)">&#125;</span>


<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h1 style="text-align:start">API examples</h1> 
<h2 style="text-align:start">GET POST PUT DELETE PATH HEAD OPTIONS</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
url <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">"https://github.com"</span>
<span style="color:var(--color-prettylights-syntax-comment)">// 发送GET方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送POST方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送PUT方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">PUT</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送DELETE方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">DELETE</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送PATH方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">PATCH</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送HEAD方法</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">HEAD</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 发送OPTIONS</span>
gout.<span style="color:var(--color-prettylights-syntax-entity)">OPTIONS</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
&#125;</pre> 
</div> 
<h2 style="text-align:start">Query Parameters</h2> 
<h3 style="text-align:start">SetQuery</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-comment)">//设置GET请求和url，:8080/test.query是127.0.0.1:8080/test.query的简写</span>
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test.query"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//设置查询字符串</span>
        <span style="color:var(--color-prettylights-syntax-entity)">SetQuery</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;
            <span style="color:var(--color-prettylights-syntax-string)">"q1"</span>: <span style="color:var(--color-prettylights-syntax-string)">"v1"</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"q2"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"q3"</span>: <span style="color:var(--color-prettylights-syntax-entity)">float32</span>(<span style="color:var(--color-prettylights-syntax-constant)">3.14</span>),
            <span style="color:var(--color-prettylights-syntax-string)">"q4"</span>: <span style="color:var(--color-prettylights-syntax-constant)">4.56</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"q5"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">Unix</span>(),
            <span style="color:var(--color-prettylights-syntax-string)">"q6"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">UnixNano</span>(),
            <span style="color:var(--color-prettylights-syntax-string)">"q7"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">Format</span>(<span style="color:var(--color-prettylights-syntax-string)">"2006-01-02"</span>)&#125;).
        <span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span>
    &#125;

&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> GET /test.query?q1=v1&q2=2&q3=3.14&q4=4.56&q5=1574081600&q6=1574081600258009213&q7=2019-11-18 HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 0</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span>
</pre> 
</div> 
<h3 style="text-align:start">SetQuery支持的更多数据类型</h3> 
<h2 style="text-align:start">http header</h2> 
<h4 style="text-align:start">Set request header</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-comment)">//设置GET请求和url，:8080/test.header是127.0.0.1:8080/test.header的简写</span>
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test.header"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//设置debug模式</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//设置请求http header</span>
        <span style="color:var(--color-prettylights-syntax-entity)">SetHeader</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;
            <span style="color:var(--color-prettylights-syntax-string)">"h1"</span>: <span style="color:var(--color-prettylights-syntax-string)">"v1"</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"h2"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"h3"</span>: <span style="color:var(--color-prettylights-syntax-entity)">float32</span>(<span style="color:var(--color-prettylights-syntax-constant)">3.14</span>),
            <span style="color:var(--color-prettylights-syntax-string)">"h4"</span>: <span style="color:var(--color-prettylights-syntax-constant)">4.56</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"h5"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">Unix</span>(),
            <span style="color:var(--color-prettylights-syntax-string)">"h6"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">UnixNano</span>(),
            <span style="color:var(--color-prettylights-syntax-string)">"h7"</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>().<span style="color:var(--color-prettylights-syntax-entity)">Format</span>(<span style="color:var(--color-prettylights-syntax-string)">"2006-01-02"</span>)&#125;).
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span>
    &#125;

&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> GET /test.header HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H2: 2</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H3: 3.14</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H4: 4.56</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H5: 1574081686</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H6: 1574081686471347098</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H7: 2019-11-18</span>
<span style="color:var(--color-prettylights-syntax-comment)">> H1: v1</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>


<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 0</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h4 style="text-align:start">Parsing the response header</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-comment)">// 和解析json类似，如要解析http header需设置header tag</span>
<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rspHeader</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Total</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>       <span style="color:var(--color-prettylights-syntax-string)">`header:"total"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Sid</span>   <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>    <span style="color:var(--color-prettylights-syntax-string)">`header:"sid"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Time</span>  time.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Time</span> <span style="color:var(--color-prettylights-syntax-string)">`header:"time" time_format:"2006-01-02"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

    rsp <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rspHeader</span>&#123;&#125;
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-comment)">// :8080/test.header是 http://127.0.0.1:8080/test.header的简写</span>
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test.header"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">//解析请求header至结构体中</span>
        <span style="color:var(--color-prettylights-syntax-entity)">BindHeader</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>rsp). 
        <span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span>
    &#125;

    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"rsp header:\n%#v \nTime:%s\n"</span>, rsp, rsp.<span style="color:var(--color-prettylights-syntax-constant)">Time</span>)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> GET /test.header HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>



<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 0</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Sid: 1234</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Time: 2019-11-18</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Total: 2048</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h3 style="text-align:start">SetHeader和BindHeader支持的更多类型</h3> 
<h2 style="text-align:start">http body</h2> 
<h3 style="text-align:start">body</h3> 
<h4 style="text-align:start">Set the data to the http request body</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-comment)">// SetBody 设置string, []byte等类型数据到http body里面</span>
<span style="color:var(--color-prettylights-syntax-comment)">// SetBody支持的更多数据类型可看下面</span>
<span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// 设置POST方法和url</span>
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/req/body"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 设置非结构化数据到http body里面</span>
<span style="color:var(--color-prettylights-syntax-comment)">// 设置json需使用SetJSON</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetBody</span>(<span style="color:var(--color-prettylights-syntax-string)">"send string"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> POST /req/body HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">send string</span>

<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Type: text/plain; charset=utf-8</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 2</span>

<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h4 style="text-align:start">get all header</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
header <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Header</span>)
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// 设置POST方法和url</span>
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/req/body"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 获取所有的响应http header</span>
<span style="color:var(--color-prettylights-syntax-entity)">BindHeader</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>header).
<span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

&#125;</pre> 
</div> 
<h4 style="text-align:start">Parse the response body into a variable</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-comment)">// BindBody bind body到string, []byte等类型变量里面</span>
<span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// 设置GET 方法及url</span>
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"www.baidu.com"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 绑定返回值</span>
<span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).
<span style="color:var(--color-prettylights-syntax-comment)">// 结束函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"html size = %d\n"</span>, <span style="color:var(--color-prettylights-syntax-entity)">len</span>(s))
&#125;</pre> 
</div> 
<h4 style="text-align:start">支持的类型有</h4> 
<ul> 
 <li>io.Reader(SetBody 支持)</li> 
 <li>io.Writer(BindBody 支持)</li> 
 <li>int, int8, int16, int32, int64</li> 
 <li>uint, uint8, uint16, uint32, uint64</li> 
 <li>string</li> 
 <li>[]byte</li> 
 <li>float32, float64</li> 
</ul> 
<h4 style="text-align:start">明确不支持的类型有</h4> 
<ul> 
 <li>struct</li> 
 <li>array, slice</li> 
</ul> 
<h3 style="text-align:start">json</h3> 
<h4 style="text-align:start">Serialize json to request body</h4> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%2Fblob%2Fmaster%2F_example%2F01-color-json.go" target="_blank">更多支持数据类型及用法</a></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//设置json到请求body</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(
gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;
<span style="color:var(--color-prettylights-syntax-string)">"str"</span>:   <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
<span style="color:var(--color-prettylights-syntax-string)">"num"</span>:   <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
<span style="color:var(--color-prettylights-syntax-string)">"bool"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
<span style="color:var(--color-prettylights-syntax-string)">"null"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">nil</span>,
<span style="color:var(--color-prettylights-syntax-string)">"array"</span>: gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-string)">"baz"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-string)">"obj"</span>:   gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>, <span style="color:var(--color-prettylights-syntax-string)">"b"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>&#125;,
&#125;,
).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> POST /colorjson HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> Content-Type: application/json</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">&#123;</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "array": [</span>
<span style="color:var(--color-prettylights-syntax-comment)">        "foo",</span>
<span style="color:var(--color-prettylights-syntax-comment)">        "bar",</span>
<span style="color:var(--color-prettylights-syntax-comment)">        "baz"</span>
<span style="color:var(--color-prettylights-syntax-comment)">    ],</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "bool": false,</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "null": null,</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "num": 100,</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "obj": &#123;</span>
<span style="color:var(--color-prettylights-syntax-comment)">        "a": 1,</span>
<span style="color:var(--color-prettylights-syntax-comment)">        "b": 2</span>
<span style="color:var(--color-prettylights-syntax-comment)">    &#125;,</span>
<span style="color:var(--color-prettylights-syntax-comment)">    "str": "foo"</span>
<span style="color:var(--color-prettylights-syntax-comment)">&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h4 style="text-align:start">Parsed http response body in json format</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rsp</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">ErrMsg</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"errmsg"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">ErrCode</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`json:"errcode"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
rsp <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rsp</span>&#123;&#125;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//绑定响应json数据到结构体</span>
<span style="color:var(--color-prettylights-syntax-entity)">BindJSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>rsp).
<span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">yaml</h3> 
<ul> 
 <li>SetYAML() 设置请求http body为yaml</li> 
 <li>BindYAML() 解析响应http body里面的yaml到结构体里面</li> 
</ul> 
<p style="text-align:start">发送yaml到服务端，然后把服务端返回的yaml结果解析到结构体里面</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">data</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Id</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`yaml:"id"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Data</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`yaml:"data"`</span>
&#125;


<span style="color:var(--color-prettylights-syntax-keyword)">var</span> d1, d2 <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">data</span>
<span style="color:var(--color-prettylights-syntax-keyword)">var</span> httpCode <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> 


err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test.yaml"</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetYAML</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>d1).<span style="color:var(--color-prettylights-syntax-entity)">BindYAML</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>d2).<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>httpCode).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> httpCode <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span>&#123;
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"send fail:%s\n"</span>, err)
&#125;</pre> 
</div> 
<h3 style="text-align:start">xml</h3> 
<ul> 
 <li>SetXML() 设置请求http body为xml</li> 
 <li>BindXML() 解析响应http body里面的xml到结构体里面</li> 
</ul> 
<p style="text-align:start">发送xml到服务端，然后把服务端返回的xml结果解析到结构体里面</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">data</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Id</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`xml:"id"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Data</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`xml:"data"`</span>
&#125;


<span style="color:var(--color-prettylights-syntax-keyword)">var</span> d1, d2 <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">data</span>
<span style="color:var(--color-prettylights-syntax-keyword)">var</span> httpCode <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> 


err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test.xml"</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetXML</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>d1).<span style="color:var(--color-prettylights-syntax-entity)">BindXML</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>d2).<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>httpCode).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> httpCode <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span>&#123;
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"send fail:%s\n"</span>, err)
&#125;</pre> 
</div> 
<h3 style="text-align:start">form-data</h3> 
<ul> 
 <li>SetForm() 设置http body 为multipart/form-data格式数据</li> 
</ul> 
<p style="text-align:start">客户端发送multipart/form-data到服务端,curl用法等同go代码</p> 
<div style="text-align:start"> 
 <pre>curl -F mode=A -F text=<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>good<span style="color:var(--color-prettylights-syntax-string)">"</span></span> -F voice=@./test.pcm -f voice2=@./test2.pcm url</pre> 
</div> 
<ul> 
 <li>使用gout.H</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

code <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/test"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetForm</span>(
gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;
<span style="color:var(--color-prettylights-syntax-string)">"mode"</span>: <span style="color:var(--color-prettylights-syntax-string)">"A"</span>,
<span style="color:var(--color-prettylights-syntax-string)">"text"</span>: <span style="color:var(--color-prettylights-syntax-string)">"good"</span>,
<span style="color:var(--color-prettylights-syntax-comment)">// 从文件里面打开</span>
<span style="color:var(--color-prettylights-syntax-string)">"voice"</span>:  gout.<span style="color:var(--color-prettylights-syntax-entity)">FormFile</span>(<span style="color:var(--color-prettylights-syntax-string)">"test.pcm"</span>),
<span style="color:var(--color-prettylights-syntax-string)">"voice2"</span>: gout.<span style="color:var(--color-prettylights-syntax-entity)">FormMem</span>(<span style="color:var(--color-prettylights-syntax-string)">"pcm"</span>),
&#125;,
).
<span style="color:var(--color-prettylights-syntax-comment)">//解析http code，如不关心可以不设置</span>
<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>code).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> code <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span> &#123;
&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> POST /test HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> Content-Type: multipart/form-data; boundary=2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">--2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Disposition: form-data; name="mode"</span>

<span style="color:var(--color-prettylights-syntax-comment)">A</span>
<span style="color:var(--color-prettylights-syntax-comment)">--2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Disposition: form-data; name="text"</span>

<span style="color:var(--color-prettylights-syntax-comment)">good</span>
<span style="color:var(--color-prettylights-syntax-comment)">--2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Disposition: form-data; name="voice"; filename="voice"</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Type: application/octet-stream</span>

<span style="color:var(--color-prettylights-syntax-comment)">pcm pcm pcm</span>

<span style="color:var(--color-prettylights-syntax-comment)">--2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Disposition: form-data; name="voice2"; filename="voice2"</span>
<span style="color:var(--color-prettylights-syntax-comment)">Content-Type: application/octet-stream</span>

<span style="color:var(--color-prettylights-syntax-comment)">pcm</span>
<span style="color:var(--color-prettylights-syntax-comment)">--2b0685e5b98e540f80b247d5e7c1283807aa07e62b827543859a6db765a8--</span>


<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Server: gurl-server</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 0</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span>
 </pre> 
</div> 
<ul> 
 <li>使用结构体</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">testForm</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Mode</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`form:"mode"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Text</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`form:"text"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Voice</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`form:"voice" form-file:"true"`</span> <span style="color:var(--color-prettylights-syntax-comment)">//从文件中读取 </span>
    <span style="color:var(--color-prettylights-syntax-constant)">Voice2</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span> <span style="color:var(--color-prettylights-syntax-string)">`form:"voice2" form-file:"mem"`</span>  <span style="color:var(--color-prettylights-syntax-comment)">//从内存中构造</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rsp</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span>&#123;
    <span style="color:var(--color-prettylights-syntax-constant)">ErrMsg</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"errmsg"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">ErrCode</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`json:"errcode"`</span>
&#125;

t <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">testForm</span>&#123;&#125;
r <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">rsp</span>&#123;&#125;
code <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(url).<span style="color:var(--color-prettylights-syntax-entity)">SetForm</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>t).<span style="color:var(--color-prettylights-syntax-entity)">ShoudBindJSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>r).<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>code).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;

&#125;</pre> 
</div> 
<h3 style="text-align:start">x-www-form-urlencoded</h3> 
<ul> 
 <li>使用SetWWWForm函数实现发送x-www-form-urlencoded类型数据</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

code <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/post"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 设置x-www-form-urlencoded数据</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetWWWForm</span>(
gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;
<span style="color:var(--color-prettylights-syntax-string)">"int"</span>:     <span style="color:var(--color-prettylights-syntax-constant)">3</span>,
<span style="color:var(--color-prettylights-syntax-string)">"float64"</span>: <span style="color:var(--color-prettylights-syntax-constant)">3.14</span>,
<span style="color:var(--color-prettylights-syntax-string)">"string"</span>:  <span style="color:var(--color-prettylights-syntax-string)">"test-www-Form"</span>,
&#125;,
).
<span style="color:var(--color-prettylights-syntax-comment)">// 关心http code 返回值设置</span>
<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>code).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> code <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span> &#123;
&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">> POST /post HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-comment)">> Content-Type: application/x-www-form-urlencoded</span>
<span style="color:var(--color-prettylights-syntax-comment)">></span>

<span style="color:var(--color-prettylights-syntax-comment)">float64=3.14&int=3&string=test-www-Form</span>

<span style="color:var(--color-prettylights-syntax-comment)">< HTTP/1.1 200 OK</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Content-Length: 0</span>
<span style="color:var(--color-prettylights-syntax-comment)">< Server: gurl-server</span>

<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h3 style="text-align:start">protobuf</h3> 
<p style="text-align:start">SetProtoBuf支持，protobuf序列化后的[]byte，或者生成的protobuf结构体指针</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
httpCode <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/echo"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetProtoBuf</span>( <span style="color:var(--color-prettylights-syntax-comment)">/* protobuf 生成的结构体，必须传指针类型*/</span> ).
<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>httpCode).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
&#125;</pre> 
</div> 
<h3 style="text-align:start">callback</h3> 
<p style="text-align:start">callback主要用在，服务端会返回多种格式body的场景, 比如404返回的是html, 200返回json。 这时候要用Callback挂载多种处理函数，处理不同的数据结构</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

r, str404 <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Result</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-string)">""</span>
code <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span>

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Callback</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) (err <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span>) &#123;

<span style="color:var(--color-prettylights-syntax-keyword)">switch</span> c.<span style="color:var(--color-prettylights-syntax-constant)">Code</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span>: <span style="color:var(--color-prettylights-syntax-comment)">//http code为200时，服务端返回的是json 结构</span>
c.<span style="color:var(--color-prettylights-syntax-entity)">BindJSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>r)
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> <span style="color:var(--color-prettylights-syntax-constant)">404</span>: <span style="color:var(--color-prettylights-syntax-comment)">//http code为404时，服务端返回是html 字符串</span>
c.<span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>str404)
&#125;
code <span style="color:var(--color-prettylights-syntax-constant)">=</span> c.<span style="color:var(--color-prettylights-syntax-constant)">Code</span>
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span>

&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"http code = %d, str404(%s) or json result(%v)\n"</span>, code, str404, r)

&#125;</pre> 
</div> 
<h2 style="text-align:start">Set request timeout</h2> 
<p style="text-align:start">setimeout是request级别的超时方案。相比http.Client级别，更灵活。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetTimeout</span>(<span style="color:var(--color-prettylights-syntax-constant)">2</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h2 style="text-align:start">proxy</h2> 
<ul> 
 <li>SetProxy 设置代理服务地址</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"log"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Client</span>&#123;&#125;
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">New</span>(c).
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"www.qq.com"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 设置proxy服务地址</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetProxy</span>(<span style="color:var(--color-prettylights-syntax-string)">"http://127.0.0.1:7000"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">// 绑定返回数据到s里面</span>
<span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
log.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(s)
&#125;</pre> 
</div> 
<h2 style="text-align:start">socks5</h2> 
<ul> 
 <li>SetSOCKS5 设置socks5地址</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"log"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Client</span>&#123;&#125;
    s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-entity)">New</span>(c).
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"www.qq.com"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">// 设置proxy服务地址</span>
        <span style="color:var(--color-prettylights-syntax-entity)">SetSOCKS5</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:7000"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">// 绑定返回数据到s里面</span>
        <span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        log.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(err)
        <span style="color:var(--color-prettylights-syntax-keyword)">return</span>
    &#125;   

    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(s)
&#125;</pre> 
</div> 
<h2 style="text-align:start">cookie</h2> 
<ul> 
 <li>SetCookies设置cookie, 可以设置一个或者多个cookie</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

<span style="color:var(--color-prettylights-syntax-comment)">// === 发送多个cookie ====</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// :8080/cookie是http://127.0.0.1:8080/cookie的简写</span>
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/cookie"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//设置debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetCookies</span>(
<span style="color:var(--color-prettylights-syntax-comment)">//设置cookie1</span>
<span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Cookie</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"test1"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Value</span>: <span style="color:var(--color-prettylights-syntax-string)">"test1"</span>,
&#125;,
<span style="color:var(--color-prettylights-syntax-comment)">//设置cookie2</span>
<span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Cookie</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"test2"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Value</span>: <span style="color:var(--color-prettylights-syntax-string)">"test2"</span>,
&#125;,
).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// === 发送一个cookie ===</span>
err <span style="color:var(--color-prettylights-syntax-constant)">=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">// :8080/cookie/one是http://127.0.0.1:8080/cookie/one的简写</span>
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/cookie/one"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//设置debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetCookies</span>(
<span style="color:var(--color-prettylights-syntax-comment)">//设置cookie1</span>
<span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Cookie</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"test3"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Value</span>: <span style="color:var(--color-prettylights-syntax-string)">"test3"</span>,
&#125;,
).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(err)

&#125;</pre> 
</div> 
<h2 style="text-align:start">basic auth</h2> 
<p style="text-align:start">使用<code>SetBasicAuth</code>接口</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetBasicAuth</span>(<span style="color:var(--color-prettylights-syntax-string)">"userName"</span>, <span style="color:var(--color-prettylights-syntax-string)">"password"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"str"</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
<span style="color:var(--color-prettylights-syntax-string)">"num"</span>:   <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
<span style="color:var(--color-prettylights-syntax-string)">"bool"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
<span style="color:var(--color-prettylights-syntax-string)">"null"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">nil</span>,
<span style="color:var(--color-prettylights-syntax-string)">"array"</span>: gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-string)">"baz"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-string)">"obj"</span>:   gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>, <span style="color:var(--color-prettylights-syntax-string)">"b"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>&#125;,
&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h2 style="text-align:start">context</h2> 
<ul> 
 <li>WithContext设置context，可以取消http请求</li> 
</ul> 
<h3 style="text-align:start">Cancel a sending request</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"context"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">//　声明一个context</span>
    ctx, cancel <span style="color:var(--color-prettylights-syntax-constant)">:=</span> context.<span style="color:var(--color-prettylights-syntax-entity)">WithCancel</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>())

    <span style="color:var(--color-prettylights-syntax-comment)">//调用cancel可取消http请求</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        time.<span style="color:var(--color-prettylights-syntax-entity)">Sleep</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>)
        <span style="color:var(--color-prettylights-syntax-entity)">cancel</span>()
    &#125;() 

    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:8080/cancel"</span>). <span style="color:var(--color-prettylights-syntax-comment)">//设置GET请求以及需要访问的url</span>
        <span style="color:var(--color-prettylights-syntax-entity)">WithContext</span>(ctx).             <span style="color:var(--color-prettylights-syntax-comment)">//设置context, 外层调用cancel函数就可取消这个http请求</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
    &#125;   
&#125;</pre> 
</div> 
<h2 style="text-align:start">unix socket</h2> 
<ul> 
 <li>UnixSocket可以把http底层通信链路由tcp修改为unix domain socket<br> 下面的例子，会通过domain socket发送http GET请求，http body的内容是hello world</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Client</span>&#123;&#125;

    g <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-entity)">New</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>c).
        <span style="color:var(--color-prettylights-syntax-entity)">UnixSocket</span>(<span style="color:var(--color-prettylights-syntax-string)">"/tmp/test.socket"</span>) <span style="color:var(--color-prettylights-syntax-comment)">//设置unixsocket文件位置</span>

    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> g.
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"http://a/test"</span>).   <span style="color:var(--color-prettylights-syntax-comment)">//设置GET请求</span>
        <span style="color:var(--color-prettylights-syntax-entity)">SetBody</span>(<span style="color:var(--color-prettylights-syntax-string)">"hello world"</span>). <span style="color:var(--color-prettylights-syntax-comment)">//设置body内容</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(err)
&#125;</pre> 
</div> 
<h2 style="text-align:start">http2 doc</h2> 
<p style="text-align:start">go 使用https访问http2的服务会自动启用http2协议，这里不需要任何特殊处理</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhttp2.golang.org%2F" target="_blank">https://http2.golang.org/</a> (bradfitz建的http2测试网址,里面大约有十来个测试地址，下面的例子选了一个)</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"https://http2.golang.org/reqinfo"</span>). <span style="color:var(--color-prettylights-syntax-comment)">//设置GET请求和请求url</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).                             <span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式，可以看到请求数据和响应数据</span>
        <span style="color:var(--color-prettylights-syntax-entity)">SetBody</span>(<span style="color:var(--color-prettylights-syntax-string)">"hello, ###########"</span>).           <span style="color:var(--color-prettylights-syntax-comment)">//设置请求body的内容，如果你的请求内容是json格式，需要使用SetJSON函数</span>
        <span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).                            <span style="color:var(--color-prettylights-syntax-comment)">//解析响应body内容</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()                                     <span style="color:var(--color-prettylights-syntax-comment)">//结束函数</span>

    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"send fail:%s\n"</span>, err)
    &#125;   
    _ <span style="color:var(--color-prettylights-syntax-constant)">=</span> s 
&#125;</pre> 
</div> 
<h2 style="text-align:start">debug mode</h2> 
<h3 style="text-align:start">Turn on debug mode</h3> 
<p style="text-align:start">该模式主要方便调试用的，默认开启颜色高亮(如果要关闭颜色高亮，请往下看)</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>). <span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"str"</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
<span style="color:var(--color-prettylights-syntax-string)">"num"</span>:   <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
<span style="color:var(--color-prettylights-syntax-string)">"bool"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
<span style="color:var(--color-prettylights-syntax-string)">"null"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">nil</span>,
<span style="color:var(--color-prettylights-syntax-string)">"array"</span>: gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-string)">"baz"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-string)">"obj"</span>:   gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>, <span style="color:var(--color-prettylights-syntax-string)">"b"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>&#125;,
&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">Turn off color highlighting in debug mode</h3> 
<p style="text-align:start">使用gout.NoColor()传入Debug函数关闭颜色高亮</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(gout.<span style="color:var(--color-prettylights-syntax-entity)">NoColor</span>()).
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"str"</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
<span style="color:var(--color-prettylights-syntax-string)">"num"</span>:   <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
<span style="color:var(--color-prettylights-syntax-string)">"bool"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
<span style="color:var(--color-prettylights-syntax-string)">"null"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">nil</span>,
<span style="color:var(--color-prettylights-syntax-string)">"array"</span>: gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-string)">"baz"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-string)">"obj"</span>:   gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>, <span style="color:var(--color-prettylights-syntax-string)">"b"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>&#125;,
&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">Custom debug mode</h3> 
<p style="text-align:start">debug 自定义模式，可传递函数。下面演示用环境变量开启debug模式(只有传递IOS_DEBUG环境变量才输出日志)</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"os"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">IOSDebug</span>() gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">DebugOpt</span> &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">return</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">DebugFunc</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(o <span style="color:var(--color-prettylights-syntax-constant)">*</span>gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">DebugOption</span>) &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">if</span> <span style="color:var(--color-prettylights-syntax-entity)">len</span>(os.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"IOS_DEBUG"</span>)) <span style="color:var(--color-prettylights-syntax-constant)">></span> <span style="color:var(--color-prettylights-syntax-constant)">0</span> &#123; 
            o.<span style="color:var(--color-prettylights-syntax-constant)">Debug</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">true</span>
        &#125;
    &#125;)  
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

    s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
        <span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:8080"</span>).
        <span style="color:var(--color-prettylights-syntax-comment)">// Debug可以支持自定义方法</span>
        <span style="color:var(--color-prettylights-syntax-comment)">// 可以实现设置某个环境变量才输出debug信息</span>
        <span style="color:var(--color-prettylights-syntax-comment)">// 或者debug信息保存到文件里面，可以看下_example/15-debug-save-file.go</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-entity)">IOSDebug</span>()).
        <span style="color:var(--color-prettylights-syntax-entity)">SetBody</span>(<span style="color:var(--color-prettylights-syntax-string)">"test hello"</span>).
        <span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).
        <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// env IOS_DEBUG=true go run customize.go</span></pre> 
</div> 
<h3 style="text-align:start">trace info</h3> 
<p style="text-align:start">gout.Trace()可输出http各个阶段的耗时，比如dns lookup时间，tcp连接时间等等。可以很方便的做些性能调优。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">openDebugTrace</span>() &#123;
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/colorjson"</span>).
        <span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(gout.<span style="color:var(--color-prettylights-syntax-entity)">Trace</span>()).
        <span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"str"</span>: <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"num"</span>:   <span style="color:var(--color-prettylights-syntax-constant)">100</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"bool"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">false</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"null"</span>:  <span style="color:var(--color-prettylights-syntax-constant)">nil</span>,
            <span style="color:var(--color-prettylights-syntax-string)">"array"</span>: gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"foo"</span>, <span style="color:var(--color-prettylights-syntax-string)">"bar"</span>, <span style="color:var(--color-prettylights-syntax-string)">"baz"</span>&#125;,
            <span style="color:var(--color-prettylights-syntax-string)">"obj"</span>:   gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1</span>, <span style="color:var(--color-prettylights-syntax-string)">"b"</span>: <span style="color:var(--color-prettylights-syntax-constant)">2</span>&#125;,
        &#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
    &#125;
&#125;</pre> 
</div> 
<ul> 
 <li>output</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-constant)">=================== Trace Info(S): ===================</span>
<span style="color:var(--color-prettylights-syntax-constant)">     DnsDuration           : 0s</span>
<span style="color:var(--color-prettylights-syntax-constant)">     ConnDuration          : 868.623µs</span>
<span style="color:var(--color-prettylights-syntax-constant)">     TLSDuration           : 0s</span>
<span style="color:var(--color-prettylights-syntax-constant)">     RequestDuration       : 376.712µs</span>
<span style="color:var(--color-prettylights-syntax-constant)">     WaitResponeDuration   : 717.008µs</span>
<span style="color:var(--color-prettylights-syntax-constant)">     ResponseDuration      : 76.158µs</span>
<span style="color:var(--color-prettylights-syntax-constant)">     TotalDuration         : 2.13921ms</span>
<span style="color:var(--color-prettylights-syntax-constant)">=================== Trace Info(E): ===================</span></pre> 
</div> 
<h2 style="text-align:start">benchmark</h2> 
<h3 style="text-align:start">benchmarking a certain number of times</h3> 
<p style="text-align:start">下面的例子，起了20并发。对:8080端口的服务，发送3000次请求进行压测，内容为json结构</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">const</span> (
benchNumber     <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">30000</span>
benchConcurrent <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">20</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).                     <span style="color:var(--color-prettylights-syntax-comment)">//压测本地8080端口</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"hello"</span>: <span style="color:var(--color-prettylights-syntax-string)">"world"</span>&#125;). <span style="color:var(--color-prettylights-syntax-comment)">//设置请求body内容</span>
<span style="color:var(--color-prettylights-syntax-entity)">Filter</span>().                          <span style="color:var(--color-prettylights-syntax-comment)">//打开过滤器</span>
<span style="color:var(--color-prettylights-syntax-entity)">Bench</span>().                           <span style="color:var(--color-prettylights-syntax-comment)">//选择bench功能</span>
<span style="color:var(--color-prettylights-syntax-entity)">Concurrent</span>(benchConcurrent).       <span style="color:var(--color-prettylights-syntax-comment)">//并发数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Number</span>(benchNumber).               <span style="color:var(--color-prettylights-syntax-comment)">//压测次数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">benchmark-duration</h3> 
<p style="text-align:start">下面的例子，起了20并发。对:8080端口的服务，压测持续时间为10s，内容为json结构</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">const</span> (
benchTime       <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">10</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>
benchConcurrent <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">30</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).                     <span style="color:var(--color-prettylights-syntax-comment)">//压测本机8080端口</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"hello"</span>: <span style="color:var(--color-prettylights-syntax-string)">"world"</span>&#125;). <span style="color:var(--color-prettylights-syntax-comment)">//设置请求body内容</span>
<span style="color:var(--color-prettylights-syntax-entity)">Filter</span>().                          <span style="color:var(--color-prettylights-syntax-comment)">//打开过滤器</span>
<span style="color:var(--color-prettylights-syntax-entity)">Bench</span>().                           <span style="color:var(--color-prettylights-syntax-comment)">//选择bench功能</span>
<span style="color:var(--color-prettylights-syntax-entity)">Concurrent</span>(benchConcurrent).       <span style="color:var(--color-prettylights-syntax-comment)">//并发数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Durations</span>(benchTime).              <span style="color:var(--color-prettylights-syntax-comment)">//压测时间</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">benchmark-rate</h3> 
<p style="text-align:start">下面的例子，起了20并发。对:8080端口的服务，压测总次数为3000次，其中每秒发送1000次。内容为json结构</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">const</span> (
benchNumber     <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">3000</span>
benchConcurrent <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-constant)">20</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).                     <span style="color:var(--color-prettylights-syntax-comment)">//压测本机8080端口</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"hello"</span>: <span style="color:var(--color-prettylights-syntax-string)">"world"</span>&#125;). <span style="color:var(--color-prettylights-syntax-comment)">//设置请求body内容</span>
<span style="color:var(--color-prettylights-syntax-entity)">Filter</span>().                          <span style="color:var(--color-prettylights-syntax-comment)">//打开过滤器</span>
<span style="color:var(--color-prettylights-syntax-entity)">Bench</span>().                           <span style="color:var(--color-prettylights-syntax-comment)">//选择bench功能</span>
<span style="color:var(--color-prettylights-syntax-entity)">Rate</span>(<span style="color:var(--color-prettylights-syntax-constant)">1000</span>).                        <span style="color:var(--color-prettylights-syntax-comment)">//每秒发1000请求</span>
<span style="color:var(--color-prettylights-syntax-entity)">Concurrent</span>(benchConcurrent).       <span style="color:var(--color-prettylights-syntax-comment)">//并发数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Number</span>(benchNumber).               <span style="color:var(--color-prettylights-syntax-comment)">//压测次数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">Custom benchmark functions</h3> 
<p style="text-align:start">自定义压测函数，构造每次不一样的http request数据</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/google/uuid"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout/filter"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"sync/atomic"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">int32</span>(<span style="color:var(--color-prettylights-syntax-constant)">0</span>)

    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> filter.<span style="color:var(--color-prettylights-syntax-entity)">NewBench</span>().
        <span style="color:var(--color-prettylights-syntax-entity)">Concurrent</span>(<span style="color:var(--color-prettylights-syntax-constant)">30</span>). <span style="color:var(--color-prettylights-syntax-comment)">//开30个go程</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Number</span>(<span style="color:var(--color-prettylights-syntax-constant)">30000</span>).  <span style="color:var(--color-prettylights-syntax-comment)">//压测30000次</span>
        <span style="color:var(--color-prettylights-syntax-entity)">Loop</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span> &#123;

<span style="color:var(--color-prettylights-syntax-comment)">// 下面的代码，每次生成不一样的http body 用于压测</span>
            uid <span style="color:var(--color-prettylights-syntax-constant)">:=</span> uuid.<span style="color:var(--color-prettylights-syntax-entity)">New</span>()  <span style="color:var(--color-prettylights-syntax-comment)">//生成uuid</span>
            id <span style="color:var(--color-prettylights-syntax-constant)">:=</span> atomic.<span style="color:var(--color-prettylights-syntax-entity)">AddInt32</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>i, <span style="color:var(--color-prettylights-syntax-constant)">1</span>) <span style="color:var(--color-prettylights-syntax-comment)">//生成id, 可以理解为++i，线程安全版本</span>

            c.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"sid"</span>: uid.<span style="color:var(--color-prettylights-syntax-entity)">String</span>(),
                <span style="color:var(--color-prettylights-syntax-string)">"appkey"</span>: fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"ak:%d"</span>, id),
                <span style="color:var(--color-prettylights-syntax-string)">"text"</span>:   fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"test text :%d"</span>, id)&#125;)
            <span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span>

        &#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
    &#125;
&#125;</pre> 
</div> 
<h2 style="text-align:start">retry-backoff</h2> 
<p style="text-align:start">retry 功能使用带抖动功能和指数回退的算法实现<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.awsarchitectureblog.com%2F2015%2F03%2Fbackoff.html" target="_blank">backoff</a></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">HEAD</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:8080"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).                      <span style="color:var(--color-prettylights-syntax-comment)">//打开debug模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Filter</span>().                         <span style="color:var(--color-prettylights-syntax-comment)">//打开过滤器</span>
<span style="color:var(--color-prettylights-syntax-entity)">Retry</span>().                          <span style="color:var(--color-prettylights-syntax-comment)">//打开重试模式</span>
<span style="color:var(--color-prettylights-syntax-entity)">Attempt</span>(<span style="color:var(--color-prettylights-syntax-constant)">5</span>).                       <span style="color:var(--color-prettylights-syntax-comment)">//最多重试5次</span>
<span style="color:var(--color-prettylights-syntax-entity)">WaitTime</span>(<span style="color:var(--color-prettylights-syntax-constant)">500</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span>). <span style="color:var(--color-prettylights-syntax-comment)">//基本等待时间</span>
<span style="color:var(--color-prettylights-syntax-entity)">MaxWaitTime</span>(<span style="color:var(--color-prettylights-syntax-constant)">3</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>).     <span style="color:var(--color-prettylights-syntax-comment)">//最长等待时间</span>
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;
&#125;</pre> 
</div> 
<h3 style="text-align:start">retry conditions httpcode</h3> 
<p style="text-align:start">指定重试条件，这里面的例子是服务端返回的状态码是209进行重试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%2Fblob%2Fmaster%2F_example%2F19c-retry-httpcode.go" target="_blank">完整代码</a></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout/filter"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">useRetryFuncCode</span>() &#123;
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080/code"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).<span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).<span style="color:var(--color-prettylights-syntax-entity)">F</span>().
<span style="color:var(--color-prettylights-syntax-entity)">Retry</span>().<span style="color:var(--color-prettylights-syntax-entity)">Attempt</span>(<span style="color:var(--color-prettylights-syntax-constant)">3</span>).<span style="color:var(--color-prettylights-syntax-entity)">WaitTime</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> <span style="color:var(--color-prettylights-syntax-constant)">10</span>).<span style="color:var(--color-prettylights-syntax-entity)">MaxWaitTime</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> <span style="color:var(--color-prettylights-syntax-constant)">50</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Func</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> c.<span style="color:var(--color-prettylights-syntax-constant)">Error</span> <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> c.<span style="color:var(--color-prettylights-syntax-constant)">Code</span> <span style="color:var(--color-prettylights-syntax-constant)">==</span> <span style="color:var(--color-prettylights-syntax-constant)">209</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> filter.<span style="color:var(--color-prettylights-syntax-constant)">ErrRetry</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span>

&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;</pre> 
</div> 
<h3 style="text-align:start">retry conditions backupurl</h3> 
<p style="text-align:start">指定条件进行重试，这里的例子是默认url不能访问，使用backup url进行访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fgout%2Fblob%2Fmaster%2F_example%2F19b-retry-customize-backup.go" target="_blank">完整代码</a></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout/core"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout/filter"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)
<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">useRetryFunc</span>() &#123;
<span style="color:var(--color-prettylights-syntax-comment)">// 获取一个没有服务绑定的端口</span>
port <span style="color:var(--color-prettylights-syntax-constant)">:=</span> core.<span style="color:var(--color-prettylights-syntax-entity)">GetNoPortExists</span>()
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">""</span>

err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":"</span> <span style="color:var(--color-prettylights-syntax-constant)">+</span> port).<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).<span style="color:var(--color-prettylights-syntax-entity)">BindBody</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>s).<span style="color:var(--color-prettylights-syntax-entity)">F</span>().
<span style="color:var(--color-prettylights-syntax-entity)">Retry</span>().<span style="color:var(--color-prettylights-syntax-entity)">Attempt</span>(<span style="color:var(--color-prettylights-syntax-constant)">3</span>).<span style="color:var(--color-prettylights-syntax-entity)">WaitTime</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> <span style="color:var(--color-prettylights-syntax-constant)">10</span>).<span style="color:var(--color-prettylights-syntax-entity)">MaxWaitTime</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Millisecond</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> <span style="color:var(--color-prettylights-syntax-constant)">50</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Func</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> c.<span style="color:var(--color-prettylights-syntax-constant)">Error</span> <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
c.<span style="color:var(--color-prettylights-syntax-entity)">SetHost</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>) <span style="color:var(--color-prettylights-syntax-comment)">//必须是存在的端口</span>
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> filter.<span style="color:var(--color-prettylights-syntax-constant)">ErrRetry</span>
&#125;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span>

&#125;).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span>, err)
&#125;</pre> 
</div> 
<h1 style="text-align:start">import</h1> 
<h2 style="text-align:start">send raw http request</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-string)">`POST /colorjson HTTP/1.1</span>
<span style="color:var(--color-prettylights-syntax-string)">Host: 127.0.0.1:8080</span>
<span style="color:var(--color-prettylights-syntax-string)">User-Agent: Go-http-client/1.1</span>
<span style="color:var(--color-prettylights-syntax-string)">Content-Length: 97</span>
<span style="color:var(--color-prettylights-syntax-string)">Content-Type: application/json</span>
<span style="color:var(--color-prettylights-syntax-string)">Accept-Encoding: gzip</span>

<span style="color:var(--color-prettylights-syntax-string)">&#123;"array":["foo","bar","baz"],"bool":false,"null":null,"num":100,"obj":&#123;"a":1,"b":2&#125;,"str":"foo"&#125;</span>
<span style="color:var(--color-prettylights-syntax-string)">    `</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">NewImport</span>().<span style="color:var(--color-prettylights-syntax-entity)">RawText</span>(s).<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetHost</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;</pre> 
</div> 
<h1 style="text-align:start">export</h1> 
<h2 style="text-align:start">generate curl command</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 1.formdata</span>
    err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>).
        <span style="color:var(--color-prettylights-syntax-entity)">SetForm</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">A</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"text"</span>, <span style="color:var(--color-prettylights-syntax-string)">"good"</span>, <span style="color:var(--color-prettylights-syntax-string)">"mode"</span>, <span style="color:var(--color-prettylights-syntax-string)">"A"</span>, <span style="color:var(--color-prettylights-syntax-string)">"voice"</span>, gout.<span style="color:var(--color-prettylights-syntax-entity)">FormFile</span>(<span style="color:var(--color-prettylights-syntax-string)">"./t8.go"</span>)&#125;).
        <span style="color:var(--color-prettylights-syntax-entity)">Export</span>().<span style="color:var(--color-prettylights-syntax-entity)">Curl</span>().<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    <span style="color:var(--color-prettylights-syntax-comment)">// output:</span>
    <span style="color:var(--color-prettylights-syntax-comment)">// curl -X GET -F "text=good" -F "mode=A" -F "voice=@./voice" "http://127.0.0.1:1234"</span>

    <span style="color:var(--color-prettylights-syntax-comment)">// 2.json body</span>
    err <span style="color:var(--color-prettylights-syntax-constant)">=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>).
        <span style="color:var(--color-prettylights-syntax-entity)">SetJSON</span>(gout.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">H</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"key1"</span>: <span style="color:var(--color-prettylights-syntax-string)">"val1"</span>, <span style="color:var(--color-prettylights-syntax-string)">"key2"</span>: <span style="color:var(--color-prettylights-syntax-string)">"val2"</span>&#125;).
        <span style="color:var(--color-prettylights-syntax-entity)">Export</span>().<span style="color:var(--color-prettylights-syntax-entity)">Curl</span>().<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
    <span style="color:var(--color-prettylights-syntax-comment)">// output:</span>
    <span style="color:var(--color-prettylights-syntax-comment)">// curl -X GET -H "Content-Type:application/json" -d "&#123;\"key1\":\"val1\",\"key2\":\"val2\"&#125;" "http://127.0.0.1:1234"</span>

    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%v\n"</span>, err)
&#125;</pre> 
</div> 
<h1 style="text-align:start">Incoming custom *http.Client</h1> 
<p style="text-align:start">使用New接口即可使用自己的http.Client对象</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>

<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Client</span>&#123;&#125; <span style="color:var(--color-prettylights-syntax-comment)">//http.Client里面有fd连接池，如果对这块优化不是太了解，只使用一个实例就行</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">New</span>(c). <span style="color:var(--color-prettylights-syntax-comment)">// New接口可传入http.Client对象</span>
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"www.qq.com"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Debug</span>(<span style="color:var(--color-prettylights-syntax-constant)">true</span>).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %s\n"</span>, err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;</pre> 
</div> 
<h1 style="text-align:start">Using chunked data format</h1> 
<p style="text-align:start">使用Chunked接口, 设置为"Transfer-Encoding: chunked"的数据编码方式</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>).
                <span style="color:var(--color-prettylights-syntax-entity)">Chunked</span>().
                <span style="color:var(--color-prettylights-syntax-entity)">SetBody</span>(<span style="color:var(--color-prettylights-syntax-string)">"11111111111"</span>).
                <span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
        <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
                fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err :%v\n"</span>, err)
        &#125;   
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// 使用nc 起一个tcp服务, 使用上面的代码发起数据观察下结果</span>
<span style="color:var(--color-prettylights-syntax-comment)">// nc -l 8080</span></pre> 
</div> 
<h1 style="text-align:start">NewWithOpt</h1> 
<p style="text-align:start">这里记录全局配置的方法, 后面所有的全局配置都推荐使用<code>gout.NewWithOpt</code>接口的实现</p> 
<h2 style="text-align:start">insecure skip verify</h2> 
<p style="text-align:start">忽略ssl验证, 使用<code>gout.WithInsecureSkipVerify()</code>接口配置该功能, 传入<code>gout.NewWithOpt</code>接口即可生效.</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-comment)">// globalWithOpt里面包含连接池, 这是一个全局可复用的对象</span>
globalWithOpt <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">NewWithOpt</span>(gout.<span style="color:var(--color-prettylights-syntax-entity)">WithInsecureSkipVerify</span>())
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> globalWithOpt.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"url"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span> ,err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;</pre> 
</div> 
<h2 style="text-align:start">Turn off 3xx status code automatic jump</h2> 
<p style="text-align:start">golang client库默认遇到301的状态码会自动跳转重新发起新请求, 你希望关闭这种默认形为, 那就使用下面的功能</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-comment)">// globalWithOpt里面包含连接池, 这是一个全局可复用的对象, 一个进程里面可能只需创建1个</span>
globalWithOpt <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">NewWithOpt</span>(gout.<span style="color:var(--color-prettylights-syntax-entity)">WithClose3xxJump</span>())
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> globalWithOpt.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"url"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span> ,err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;</pre> 
</div> 
<h2 style="text-align:start">NewWithOpt set timeout</h2> 
<p style="text-align:start"><code>gout.WithTimeout</code> 为了让大家少用<code>gout.SetTimeout</code>而设计</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-comment)">// globalWithOpt里面包含连接池, 这是一个全局可复用的对象, 一个进程里面可能只需创建1个</span>
globalWithOpt <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">NewWithOpt</span>(gout.<span style="color:var(--color-prettylights-syntax-entity)">WithTimeout</span>())
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> globalWithOpt.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"url"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err = %v\n"</span> ,err)
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;</pre> 
</div> 
<h1 style="text-align:start">Global configuration</h1> 
<h2 style="text-align:start">set timeout</h2> 
<p style="text-align:start">设置全局超时时间。可以简化一些代码。在使用全局配置默认你已经了解它会带来的一些弊端.</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
gout.<span style="color:var(--color-prettylights-syntax-entity)">SetTimeout</span>(time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span> <span style="color:var(--color-prettylights-syntax-constant)">1</span>)
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"www.baidu.com"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"err is:%v\n"</span>)
&#125;
&#125;</pre> 
</div> 
<h1 style="text-align:start">Unique features</h1> 
<h2 style="text-align:start">forward gin data</h2> 
<p style="text-align:start">gout 设计之初就考虑到要和gin协同工作的可能性，下面展示如何方便地使用gout转发gin绑定的数据。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/gout"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">testQuery</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Size</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`query:"size" form:"size"`</span> <span style="color:var(--color-prettylights-syntax-comment)">// query tag是gout设置查询字符串需要的</span>
<span style="color:var(--color-prettylights-syntax-constant)">Page</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`query:"page" form:"page"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Ak</span>   <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`query:"ak" form:"ak"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">//下一个服务节点</span>
<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">nextSever</span>() &#123;
r <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">Default</span>()

r.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"/query"</span>, <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
q <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">testQuery</span>&#123;&#125;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> c.<span style="color:var(--color-prettylights-syntax-entity)">ShouldBindQuery</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>q)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
c.<span style="color:var(--color-prettylights-syntax-entity)">JSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, q)
&#125;)
r.<span style="color:var(--color-prettylights-syntax-entity)">Run</span>(<span style="color:var(--color-prettylights-syntax-string)">":1234"</span>)
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-entity)">nextSever</span>()
r <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">Default</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// 演示把gin绑定到的查询字符串转发到nextServer节点</span>
r.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"/query"</span>, <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
q <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">testQuery</span>&#123;&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// 绑定查询字符串</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> c.<span style="color:var(--color-prettylights-syntax-entity)">ShouldBindQuery</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>q)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// 开发转发, 复用gin所用结构体变量q</span>
code <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">0</span> <span style="color:var(--color-prettylights-syntax-comment)">// http code</span>
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gout.
<span style="color:var(--color-prettylights-syntax-comment)">//发起GET请求</span>
<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"127.0.0.1:1234/query"</span>).
<span style="color:var(--color-prettylights-syntax-comment)">//设置查询字符串</span>
<span style="color:var(--color-prettylights-syntax-entity)">SetQuery</span>(q).
<span style="color:var(--color-prettylights-syntax-comment)">//关心http server返回的状态码 设置该函数</span>
<span style="color:var(--color-prettylights-syntax-entity)">Code</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>code).
<span style="color:var(--color-prettylights-syntax-entity)">Do</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">||</span> code <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">200</span> &#123; <span style="color:var(--color-prettylights-syntax-comment)">/* todo Need to handle errors here */</span>
&#125;
c.<span style="color:var(--color-prettylights-syntax-entity)">JSON</span>(<span style="color:var(--color-prettylights-syntax-constant)">200</span>, q)
&#125;)

r.<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// http client</span>
<span style="color:var(--color-prettylights-syntax-comment)">// curl '127.0.0.1:8080/query?size=10&page=20&ak=test'</span></pre> 
</div>
                                        </div>
                                      
</div>
            