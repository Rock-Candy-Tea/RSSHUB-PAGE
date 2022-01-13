
---
title: '最快的 Logstash 替代方案 go-stash v1.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/kevwan/go-stash/raw/master/doc/flow.png'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 14:41:00 GMT
thumbnail: 'https://gitee.com/kevwan/go-stash/raw/master/doc/flow.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">go-stash v1.0.1 现已发布。go-stash是一个高效的从Kafka获取，根据配置的规则进行处理，然后发送到ElasticSearch集群的工具。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">go-stash有大概logstash 5倍的吞吐性能，并且部署简单，一个可执行文件即可。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="go-stash" src="https://gitee.com/kevwan/go-stash/raw/master/doc/flow.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">安装</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#0086b3">cd </span>stash <span>&&</span> go build stash.go</span>
</pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Quick Start</h3> 
<ul> 
 <li>可执行文件方式</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span>./stash <span style="color:#000080">-f</span> etc/config.yaml</span>
</pre> 
 </div> 
</div> 
<ul> 
 <li>docker 方式，确保配置文件路径正确</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span>docker run <span style="color:#000080">-d</span> <span style="color:#000080">-v</span> <span style="background-color:#fff0f0; color:#dd2200">`</span><span style="color:#0086b3">pwd</span><span style="background-color:#fff0f0; color:#dd2200">`</span>/etc:/app/etc kevinwan/go-stash</span>
</pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">config.yaml示例如下:</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">Clusters</span><span>:</span></span>
<span><span>-</span> <span style="color:#008080">Input</span><span>:</span></span>
<span>    <span style="color:#008080">Kafka</span><span>:</span></span>
<span>      <span style="color:#008080">Name</span><span>:</span> <span style="color:#dd2200">go-stash</span></span>
<span>      <span style="color:#008080">Log</span><span>:</span></span>
<span>        <span style="color:#008080">Mode</span><span>:</span> <span style="color:#dd2200">file</span></span>
<span>      <span style="color:#008080">Brokers</span><span>:</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">172.16.48.41:9092"</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">172.16.48.42:9092"</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">172.16.48.43:9092"</span></span>
<span>      <span style="color:#008080">Topic</span><span>:</span> <span style="color:#dd2200">ngapplog</span></span>
<span>      <span style="color:#008080">Group</span><span>:</span> <span style="color:#dd2200">stash</span></span>
<span>      <span style="color:#008080">Conns</span><span>:</span> <strong style="color:#0000dd">3</strong></span>
<span>      <span style="color:#008080">Consumers</span><span>:</span> <strong style="color:#0000dd">10</strong></span>
<span>      <span style="color:#008080">Processors</span><span>:</span> <strong style="color:#0000dd">60</strong></span>
<span>      <span style="color:#008080">MinBytes</span><span>:</span> <strong style="color:#0000dd">1048576</strong></span>
<span>      <span style="color:#008080">MaxBytes</span><span>:</span> <strong style="color:#0000dd">10485760</strong></span>
<span>      <span style="color:#008080">Offset</span><span>:</span> <span style="color:#dd2200">first</span></span>
<span>  <span style="color:#008080">Filters</span><span>:</span></span>
<span>  <span>-</span> <span style="color:#008080">Action</span><span>:</span> <span style="color:#dd2200">drop</span></span>
<span>    <span style="color:#008080">Conditions</span><span>:</span></span>
<span>      <span>-</span> <span style="color:#008080">Key</span><span>:</span> <span style="color:#dd2200">status</span></span>
<span>        <span style="color:#008080">Value</span><span>:</span> <strong style="color:#0000dd">503</strong></span>
<span>        <span style="color:#008080">Type</span><span>:</span> <span style="color:#dd2200">contains</span></span>
<span>      <span>-</span> <span style="color:#008080">Key</span><span>:</span> <span style="color:#dd2200">type</span></span>
<span>        <span style="color:#008080">Value</span><span>:</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">app"</span></span>
<span>        <span style="color:#008080">Type</span><span>:</span> <span style="color:#dd2200">match</span></span>
<span>        <span style="color:#008080">Op</span><span>:</span> <span style="color:#dd2200">and</span></span>
<span>  <span>-</span> <span style="color:#008080">Action</span><span>:</span> <span style="color:#dd2200">remove_field</span></span>
<span>    <span style="color:#008080">Fields</span><span>:</span></span>
<span>    <span>-</span> <span style="color:#dd2200">message</span></span>
<span>    <span>-</span> <span style="color:#dd2200">source</span></span>
<span>    <span>-</span> <span style="color:#dd2200">beat</span></span>
<span>    <span>-</span> <span style="color:#dd2200">fields</span></span>
<span>    <span>-</span> <span style="color:#dd2200">input_type</span></span>
<span>    <span>-</span> <span style="color:#dd2200">offset</span></span>
<span>    <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">@version"</span></span>
<span>    <span>-</span> <span style="color:#dd2200">_score</span></span>
<span>    <span>-</span> <span style="color:#dd2200">_type</span></span>
<span>    <span>-</span> <span style="color:#dd2200">clientip</span></span>
<span>    <span>-</span> <span style="color:#dd2200">http_host</span></span>
<span>    <span>-</span> <span style="color:#dd2200">request_time</span></span>
<span>  <span style="color:#008080">Output</span><span>:</span></span>
<span>    <span style="color:#008080">ElasticSearch</span><span>:</span></span>
<span>      <span style="color:#008080">Hosts</span><span>:</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">http://172.16.188.73:9200"</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">http://172.16.188.74:9200"</span></span>
<span>      <span>-</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">http://172.16.188.75:9200"</span></span>
<span>      <span style="color:#008080">Index</span><span>:</span> <span style="color:#dd1144">"</span><span style="color:#dd2200">go-stash-&#123;&#123;yyyy.MM.dd&#125;&#125;"</span></span>
<span>      <span style="color:#008080">MaxChunkBytes</span><span>:</span> <strong style="color:#0000dd">5242880</strong></span>
<span>      <span style="color:#008080">GracePeriod</span><span>:</span> <span style="color:#dd2200">10s</span></span>
<span>      <span style="color:#008080">Compress</span><span>:</span> <span style="color:#008080">false</span></span>
<span>      <span style="color:#008080">TimeZone</span><span>:</span> <span style="color:#dd2200">UTC</span></span>
</pre> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">详细说明</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">input</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>Conns: 3</span>
<span>Consumers: 10</span>
<span>Processors: 60</span>
<span>MinBytes: 1048576</span>
<span>MaxBytes: 10485760</span>
<span>Offset: first</span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Conns</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">链接kafka的链接数，链接数依据cpu的核数，一般<= CPU的核数；</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Consumers</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">每个连接数打开的线程数，计算规则为Conns * Consumers，不建议超过分片总数，比如topic分片为30，Conns *Consumers <= 30</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Processors</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">处理数据的线程数量，依据CPU的核数，可以适当增加，建议配置：Conns * Consumers * 2 或 Conns * Consumers * 3，例如：60 或 90</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">MinBytes MaxBytes</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">每次从kafka获取数据块的区间大小，默认为1M~10M，网络和IO较好的情况下，可以适当调高</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Offset</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可选last和false，默认为last，表示从头从kafka开始读取数据</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Filters</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>- Action: drop</span>
<span>  Conditions:</span>
<span>    - Key: k8s_container_name</span>
<span>      Value: <span style="color:#dd1144">"-rpc"</span></span>
<span>      Type: contains</span>
<span>    - Key: level</span>
<span>      Value: info</span>
<span>      Type: match</span>
<span>      Op: and</span>
<span>- Action: remove_field</span>
<span>  Fields:</span>
<span>    - message</span>
<span>    - _source</span>
<span>    - _type</span>
<span>    - _score</span>
<span>    - _id</span>
<span>    - <span style="color:#dd1144">"@version"</span></span>
<span>    - topic</span>
<span>    - index</span>
<span>    - beat</span>
<span>    - docker_container</span>
<span>    - offset</span>
<span>    - prospector</span>
<span>    - <span style="color:#0086b3">source</span></span>
<span>    - stream</span>
<span>- Action: transfer</span>
<span>  Field: message</span>
<span>  Target: data</span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">- Action: drop</h4> 
<ul> 
 <li>删除标识：满足此条件的数据，在处理时将被移除，不进入es</li> 
 <li>按照删除条件，指定key字段及Value的值，Type字段可选contains(包含)或match(匹配)</li> 
 <li>拼接条件Op: and，也可写or</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">- Action: remove_field</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">移除字段标识：需要移除的字段，在下面列出即可</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">- Action: transfer</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">转移字段标识：例如可以将message字段，重新定义为data字段</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">Output</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Index</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">索引名称，indexname-&#123;&#123;yyyy.MM.dd&#125;&#125;表示年.月.日，也可以用&#123;&#123;yyyy-MM-dd&#125;&#125;，格式自己定义</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">MaxChunkBytes</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">每次往ES提交的bulk大小，默认是5M，可依据ES的io情况，适当的调整</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">GracePeriod</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">默认为10s，在程序关闭后，在10s内用于处理余下的消费和数据，优雅退出</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Compress</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">数据压缩，压缩会减少传输的数据量，但会增加一定的处理性能，可选值true/false，默认为false</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">TimeZone</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">默认值为UTC，世界标准时间</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">ES性能写入测试</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">测试环境</h3> 
<ul> 
 <li>stash服务器：3台 4核 8G</li> 
 <li>es服务器： 15台 16核 64G</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">关键配置</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>- Input:</span>
<span>      Conns: 3</span>
<span>      Consumers: 10</span>
<span>      Processors: 60</span>
<span>      MinBytes: 1048576</span>
<span>      MaxBytes: 10485760</span>
<span>  Filters:</span>
<span>  - Action: remove_field</span>
<span>    Fields:</span>
<span>    - message</span>
<span>    - <span style="color:#0086b3">source</span></span>
<span>    - beat</span>
<span>    - fields</span>
<span>    - input_type</span>
<span>    - offset</span>
<span>    - request_time</span>
<span>  Output:</span>
<span>      Index: <span style="color:#dd1144">"nginx_pro-&#123;&#123;yyyy.MM.d&#125;&#125;"</span></span>
<span>      Compress: <span style="color:#0086b3">false</span></span>
<span><span style="color:#0086b3">      </span>MaxChunkBytes: 5242880</span>
<span>      TimeZone: UTC</span>
</pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">写入速度平均在15W/S以上</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="go-stash" src="https://pro-public.xiaoheiban.cn/icon/ee207a1cb094c0b3dcaa91ae75b118b8.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新内容：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1. 升级了go-zero至v1.2.5</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2. 升级了go-queue至v1.1.1</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：</p> 
<ul> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: left;">gitee: <a href="https://gitee.com/kevwan/go-stash">https://gitee.com/kevwan/go-stash</a></li> 
 <li style="color: rgb(51, 51, 51); margin-left: 0px; margin-right: 0px; text-align: left;">github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkevwan%2Fgo-stash" target="_blank">https://github.com/kevwan/go-stash</a></li> 
</ul>
                                        </div>
                                      
</div>
            