
---
title: 'bboss-elasticsearch v6.7.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8580'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 09:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8580'
---

<div>   
<div class="content">
                                                                                            <p>Elasticsearch Rest Client bboss v6.7.3 发布，版本变更记录：</p> 
<ol> 
 <li>处理flushsync方法在Elasticsearch8的兼容性问题 ，增加获取elasticsearch版本号方法</li> 
 <li>jdk 17兼容性改进</li> 
 <li>Elasticsearch客户端改进：增加ESMatchedQueries注解，用于绑定返回<em>name指定的命名匹配条件数组String[]，参考文档：</em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fclient-annotation%3Fid%3D_2%25e5%2585%2583%25e6%2595%25b0%25e6%258d%25ae%25e6%25b3%25a8%25e8%25a7%25a3" target="_blank">元数据注解</a></li> 
</ol> 
<p>bboss elasticsearch 是一套基于 query dsl 语法操作和访问分布式搜索引擎 elasticsearch 的 o/r mapping 高性能java开发库，底层基于 es restful api。基于 bboss elasticsearch，可以快速编写出访问和操作 elasticsearch 的程序代码，简单、高效、可靠、安全。</p> 
<p><strong><span style="color:#34495e">主要特点：代码简洁，性能高效，客户端负载容灾，兼容性好，易于集成</span></strong></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">快速开始 bboss</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2Fquickstart" target="_blank">https://esdoc.bbossgroups.com/#/quickstart</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fesdoc.bbossgroups.com%2F%23%2F%3Fid%3Dbboss%25e5%2585%25bc%25e5%25ae%25b9%25e6%2580%25a7" target="_blank"><span style="color:#34495e">bboss 兼容性</span></a></h1> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">兼容性：<strong>bboss 兼容所有版本 Elasticsearch、Spring boot</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:1320px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>bboss</th> 
   <th>Elasticsearch</th> 
   <th>spring boot</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">2.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">3.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">5.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">6.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">all</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">7.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">1.x,2.x</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">jdk 兼容性：jdk 1.7+</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start"><strong>代码简洁</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一行代码插入 / 修改</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#8e908c">// 添加 / 修改文档，如果文档 id 存在则修改，不存在则插入</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#d73a49">clientUtil</span><span style="color:#6f42c1">.addDocument</span>(<span style="color:#032f62">"agentinfo"</span>,<span style="color:#6a737d">//索引名称</span>
agentInfo);<span style="color:#6a737d">//需添加/修改的索引数据对象</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一行代码分页 / 高亮检索</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">ESDatas<TAgentInfo> <span style="color:#d73a49">data</span> <span style="color:#6a737d">//ESDatas为查询结果集对象，封装了返回的当前查询的List<TAgentInfo>结果集和符合条件的总记录数totalSize</span>
            = clientUtil.searchList(<span style="color:#032f62">"trace-*/_search"</span>,<span style="color:#6a737d">//查询操作，查询indices trace-*中符合条件的数据</span>
                                <span style="color:#032f62">"queryServiceByCondition"</span>,<span style="color:#6a737d">//通过名称引用配置文件中的query dsl语句</span>
                                traceExtraCriteria,<span style="color:#6a737d">//查询条件封装对象</span>
                                TAgentInfo<span>.<span style="color:#d73a49">class</span>);//指定返回的<span style="color:#6f42c1">po</span>对象类型，<span style="color:#6f42c1">po</span>对象中的属性与<span style="color:#6f42c1">indices</span>表中的文档<span style="color:#6f42c1">filed</span>名称保持一致</span>
<span style="color:#6a737d">//获取当前页结果对象列表</span>
        List<TAgentInfo> demos = <span style="color:#d73a49">data</span>.getDatas();
        <span style="color:#6a737d">//获取总记录数</span>
        long totalSize = <span style="color:#d73a49">data</span>.getTotalSize();</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">根据文档 id 获取文档</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">Demo demo = clientUtil.getDocument(<span style="color:#032f62">"demo"</span>,<span style="color:#6a737d">//索引表</span>
      <span style="color:#032f62">"2"</span>,<span style="color:#6a737d">//文档id</span>
      Demo<span>.<span style="color:#d73a49">class</span>)</span>;<span style="color:#6a737d">//指定返回对象类型</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span> </span>根据字段直接获取文档</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span>String</span> <span>document</span> = clientInterface.getDocumentByField(<span style="color:#032f62">"demo"</span>,<span style="color:#6a737d">//索引名称</span>
                  <span style="color:#032f62">"applicationName.keyword"</span>,<span style="color:#6a737d">//字段名称</span>
                  <span style="color:#032f62">"blackcatdemo2"</span>);<span style="color:#6a737d">//字段值</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一行代码根据字段值进行分页查找</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">ESDatas<Map> documents = clientInterface.searchListByField(<span style="color:#032f62">"demo"</span>,<span style="color:#6a737d">//索引名名称</span>
                                          <span style="color:#032f62">"applicationName.keyword"</span>, <span style="color:#6a737d">//检索字段名称</span>
                                          <span style="color:#032f62">"blackcatdemo2"</span>,<span style="color:#6a737d">//检索值</span>
                                           Map<span>.<span style="color:#d73a49">class</span>,  <span style="color:#d73a49">//返回结果类型，可以是po对象类型也可以是map类型</span></span>
                                           <span>0</span>,  <span style="color:#6a737d">//分页起始位置</span>
                                           <span>10</span>); <span style="color:#6a737d">//分页每页记录数</span>
<span style="color:#6a737d">//获取当前页结果对象列表</span>
        List<Map> demos = <span style="color:#d73a49">data</span>.getDatas();
        <span style="color:#6a737d">//获取匹配的总记录数</span>
        long totalSize = <span style="color:#d73a49">data</span>.getTotalSize();</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一行代码删除文档</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#d73a49">clientUtil</span><span style="color:#6f42c1">.deleteDocument</span>(<span style="color:#032f62">"demo"</span>,<span style="color:#6a737d">//索引表</span>
          <span style="color:#032f62">"2"</span>);<span style="color:#6a737d">//文档id</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一行代码批量删除文档</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">//批量删除文档</span>
        clientUtil.deleteDocuments(<span style="color:#032f62">"demo"</span>,<span style="color:#6a737d">//索引表</span>
                <span style="color:#d73a49">new</span> <span>String</span>[]&#123;<span style="color:#032f62">"2"</span>,<span style="color:#032f62">"3"</span>&#125;);<span style="color:#6a737d">//批量删除文档ids</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">所有 api 可以直接指定 Elasticsearch 集群数据源操作，指哪打哪：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">ESDatas<Demo> esDatas = 
            clientUtil.searchListWithCluster(datasourceName,<span style="color:#6a737d">//指定操作的Elasticsearch集群数据源名称</span>
                  <span style="color:#032f62">"demo/_search"</span>,<span style="color:#6a737d">//demo为索引表，_search为检索操作action</span>
            <span style="color:#032f62">"searchDatas"</span>,<span style="color:#6a737d">//esmapper/demo7.xml中定义的dsl语句</span>
            params,<span style="color:#6a737d">//变量参数</span>
            Demo<span>.<span style="color:#d73a49">class</span>)</span>;<span style="color:#6a737d">//返回的文档封装对象类型</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>易于集成</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">快速集成，导入 BBoss maven 坐标:</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>bboss-elasticsearch-rest-jdbc<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>6.7.3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">如果是 spring boot 项目，还需导入以下 maven 坐标:</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>com.bbossgroups.plugins<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>bboss-elasticsearch-spring-boot-starter<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
        <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"><</span></span><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>6.7.3<span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span>
    <span style="color:#2973b7"><span style="color:#2973b7"><span style="color:#525252"><span style="color:#333333"></</span></span><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#525252"><span style="color:#333333">></span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">快速配置，在 application.properties 文件中增加 Elasticsearch 服务器地址和认证（可选）配置即可</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6a737d">#elasticsearch.rest.hostNames=10.180.211.27:9200,10.180.211.28:9200,10.180.211.29:9200 
elasticsearch.rest.hostNames=10.21.20.168:9200</span>

<span style="color:#6a737d">#x-pack or searchguard security authentication and password configuration</span>

elasticUser=elastic
elasticPassword=changeme</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#42b983">spring boot 配置</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">spring.elasticsearch.bboss.elasticsearch.rest.hostNames</span>=<span>127.0</span>.<span>0.1</span>:<span>9200</span>
<span style="color:#6a737d">#spring.elasticsearch.bboss.elasticsearch.rest.hostNames=10.180.211.27:9200,10.180.211.28:9200,10.180.211.29:9200 </span>

<span style="color:#6a737d">##support x-pack and searchguard</span>

<span style="color:#6f42c1">spring.elasticsearch.bboss.elasticUser</span>=elastic

<span style="color:#6f42c1">spring.elasticsearch.bboss.elasticPassword</span>=changeme</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            