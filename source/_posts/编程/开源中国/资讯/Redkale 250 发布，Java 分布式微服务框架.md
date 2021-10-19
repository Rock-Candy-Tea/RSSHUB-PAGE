
---
title: 'Redkale 2.5.0 发布，Java 分布式微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4722'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 11:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4722'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redkale 2.5.0 发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Redkale， 一个Java分布式微服务框架，1.4M的jar可以代替传统几十M的第三方。包含TCP/UDP、HTTP、RPC、依赖注入、序列化与反序列化、数据库操作、WebSocket等功能。  一方面模块高度整合，极大的简化业务开发代码，一方面暴露大量底层，方便二次框架开发。  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Java并不臃肿， 臃肿的是你自己的设计思维！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次版本更新内容：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f"> 1、【新增】支持Graalvm的native-image原生打包</span><br> <span style="background-color:#ffffff; color:#24292f"> 2、【新增】apidoc生成OpenAPI 3.0规范json文件</span><br> <span style="background-color:#ffffff; color:#24292f"> 3、【新增】net包支持TLS，且支持最新版TLSv1.3</span><br> <span style="background-color:#ffffff; color:#24292f"> 4、【新增】增加</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbean" target="_blank">@bean</a><span style="background-color:#ffffff; color:#24292f">类，DataSource增加对所有entity参数是否有标记</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fentity" target="_blank">@entity</a><span style="background-color:#ffffff; color:#24292f">的判断</span><br> <span style="background-color:#ffffff; color:#24292f"> 5、【新增】增加PrepareCompiler 需结合redkale-maven-plugin插件使用</span><br> <span style="background-color:#ffffff; color:#24292f"> 6、【新增】RedkaleClassLoader增加putDynXXX系列方法，增加Mpsc相关并发容器类</span><br> <span style="background-color:#ffffff; color:#24292f"> 7、【优化】【不兼容】移除JDK8的支持， 最低版本升级为JDK11</span><br> <span style="background-color:#ffffff; color:#24292f"> 8、【优化】【不兼容】废弃RetResult.attach属性</span><br> <span style="background-color:#ffffff; color:#24292f"> 9、【优化】【不兼容】移除ResourceFactory.root(),增加ResourceFactory.create()</span><br> <span style="background-color:#ffffff; color:#24292f">10、【优化】工程改成maven构建方式</span><br> <span style="background-color:#ffffff; color:#24292f">11、【优化】RestMapping.name默认值不再去掉Service的服务名</span><br> <span style="background-color:#ffffff; color:#24292f">12、【优化】Server.createContext()去掉参数，并从Server.start移至Server.init方法中调用</span><br> <span style="background-color:#ffffff; color:#24292f">13、【优化】增加XmlReader，移除java.xml的依赖</span><br> <span style="background-color:#ffffff; color:#24292f">14、【优化】convert支持java.lang.Record类</span><br> <span style="background-color:#ffffff; color:#24292f">15、【优化】移除AsyncConnection的newInputStream</span><br> <span style="background-color:#ffffff; color:#24292f">16、【修复】修复没mq配置下HttpMessageLocalClient无法正常使用的bug</span><br> <span style="background-color:#ffffff; color:#24292f">17、【修复】修复HttpSimpleRequest复制给HttpRequest.requestURI没有加上path前缀</span><br> <span style="background-color:#ffffff; color:#24292f">18、【修复】修复RESNAME_APP_CONF没有依赖注入的bug</span></p> 
<p><strong>原生打包：</strong></p> 
<p> 需要安装Graalvm，在工程pom.xml 加入： </p> 
<pre><code class="language-xml"><plugin> 
  <groupId>org.redkale.maven.plugins</groupId>  
  <artifactId>redkale-maven-plugin</artifactId>  
  <version>1.0.0</version>  
  <configuration> 
    <nativeimageArgs> 
      <arg>--allow-incomplete-classpath</arg>  
      <arg>--no-fallback</arg> 
    </nativeimageArgs> 
  </configuration>  
  <executions> 
    <execution> 
      <id>redkale-compile</id>  
      <phase>process-classes</phase>  
      <goals> 
        <goal>compile</goal> 
      </goals> 
    </execution> 
  </executions> 
</plugin></code></pre> 
<p>  编译完工程后执行：</p> 
<pre><code class="language-bash">native-image -H:+ReportExceptionStackTraces --report-unsupported-elements-at-runtime -jar redkale-benchmark.jar</code></pre> 
<p>即可得到可运行文件  redkale-benchmark  </p> 
<p>由于redkale的零依赖， 原生打包后的文件大小远小于其他可原生打包的框架， 使用依赖官方plugins进行redis、mysql/postgresql等常规功能，打包后的大小依然不大， 如果SpringBoot工程加入redis、mysql等第三方后使用尚未成熟的Spring Native进行打包， 包体会非常大。</p> 
<p>详情工程可参考： https://github.com/TechEmpower/FrameworkBenchmarks/blob/master/frameworks/Java/redkale/redkale-native.dockerfile</p> 
<p><strong>OpenAPI文档：</strong></p> 
<p>编译完工程并启动后执行 bin/apidoc.sh 会在工程目录下生成符合OpenAPI 3.0.0规范的openapi-doc.json 离线文件。</p> 
<p>将json文件放进<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswagger-api%2Fswagger-ui" target="_blank">swagger-ui</a>即可展现文档。</p>
                                        </div>
                                      
</div>
            