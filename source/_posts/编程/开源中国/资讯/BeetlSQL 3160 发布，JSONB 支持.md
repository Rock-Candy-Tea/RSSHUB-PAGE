
---
title: 'BeetlSQL 3.16.0 发布，JSONB 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8759'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 09:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8759'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li>调整AttributeConvert，增加新接口，干预内置生成语句方式，参考<a href="https://gitee.com/xiandafu/beetlsql/issues/I5HAK5#note_11768322">Postgress BJSON</a></li> 
 <li>视图支持通过@AssingId指定主键，以支持内置查询，更新操作，参考<a href="https://gitee.com/xiandafu/beetlsql/issues/I5I6OC#note_11803606">视图更新</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Maven</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>beetlsql<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>3.16.0-RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span></code>
</pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span> </span>BeetlSQL 自主研发自 2015 年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑，不亚于 MyBatis。你不想写 SQL 也好，或者想更好地写 SQL 也好，BeetlSQL 都能满足这要求，目前支持的数据库如下</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>传统数据库：MySQL (包括支持 MySQL 协议的各种数据库), MariaDB ,Oralce ,Postgres (包括支持 Postgres 协议的各种数据库), DB2 , SQL Server ，H2 , SQLite , Derby ，神通，达梦，华为高斯，人大金仓，PolarDB，GBase8s，GreatSQL 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL 查询引擎：Drill,Presto，Druid</li> 
 <li>内存数据库：ignite，CouchBase</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide%2F1958115" target="_blank">多库使用</a> <a href="https://gitee.com/xiandafu/dao-benchmark">性能测试</a></p> 
<p> </p> 
<p><strong>关于AttributeConvert类说明</strong></p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">可以自定义一个属性注解，BeetlSQL上遇到此属性注解，将按照属性注解的执行类去执行映射，比如对手机号码的入库加密，出库解密。比如对JSON对象序列化成字符串到数据库，然后从数据库反序列成成对象。同其他BeetlSQL扩展注解机制类似，实现一个扩展注解，需要使用@Builder注解申明其执行类</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>@<span style="color:#dd4a68">Retention</span><span style="color:#999999">(</span>RetentionPolicy<span style="color:#999999">.</span>RUNTIME<span style="color:#999999">)</span>
@<span style="color:#dd4a68">Target</span><span style="color:#999999">(</span>value <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#999999">&#123;</span>ElementType<span style="color:#999999">.</span>METHOD<span style="color:#999999">,</span> ElementType<span style="color:#999999">.</span>FIELD<span style="color:#999999">&#125;</span><span style="color:#999999">)</span>
@<span style="color:#dd4a68">Builder</span><span style="color:#999999">(</span><span style="background-color:#f1c40f">Base64Convert</span><span style="color:#999999"><span style="background-color:#f1c40f">.</span></span><span style="background-color:#f1c40f">class</span><span style="color:#999999">)</span>
public static @interface <span style="color:#dd4a68">Base64</span> <span style="color:#999999">&#123;</span>

<span style="color:#999999">&#125;</span>

</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">如上申明一个@Base，用于字段在入库加密，出库解密。其实现类使用@Builder注解申明，本例其执行类是Base64Convert。</p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">执行类必须是一个AttributeConvert的子类，实现AttributeConvert方法</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>public static class <span style="color:#dd4a68"><span style="background-color:#f1c40f">Base64Convert</span></span><span style="background-color:#f1c40f">  </span>implements <span style="color:#dd4a68">AttributeConvert</span> <span style="color:#999999">&#123;</span>
  Charset utf8  <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> Charset<span style="color:#999999">.</span><span style="color:#dd4a68">forName</span><span style="color:#999999">(</span><span style="color:#669900">"UTF-8"</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
  public  Object <span style="color:#dd4a68">toDb</span><span style="color:#999999">(</span>ExecuteContext ctx<span style="color:#999999">,</span> Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span> String name<span style="color:#999999">,</span> Object pojo<span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
    String value<span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#999999">(</span>String<span style="color:#999999">)</span> BeanKit<span style="color:#999999">.</span><span style="color:#dd4a68">getBeanProperty</span><span style="color:#999999">(</span>dbValue<span style="color:#999999">,</span>name<span style="color:#999999">)</span><span style="color:#999999">;</span>
    byte<span style="color:#999999">[</span><span style="color:#999999">]</span> bs <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> java<span style="color:#999999">.</span>util<span style="color:#999999">.</span>Base64<span style="color:#999999">.</span><span style="color:#dd4a68">getEncoder</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">.</span><span style="color:#dd4a68">encode</span><span style="color:#999999">(</span>value<span style="color:#999999">.</span><span style="color:#dd4a68">getBytes</span><span style="color:#999999">(</span>utf8<span style="color:#999999">)</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
    <span style="color:#0077aa">return</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">String</span><span style="color:#999999">(</span>bs<span style="color:#999999">,</span>utf8<span style="color:#999999">)</span><span style="color:#999999">;</span>
  <span style="color:#999999">&#125;</span>
  
  public  Object <span style="color:#dd4a68">toAttr</span><span style="color:#999999">(</span>ExecuteContext ctx<span style="color:#999999">,</span> Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span> String name<span style="color:#999999">,</span> ResultSet rs<span style="color:#999999">,</span> int index<span style="color:#999999">)</span> throws SQLException <span style="color:#999999">&#123;</span>
    String value  <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> rs<span style="color:#999999">.</span><span style="color:#dd4a68">getString</span><span style="color:#999999">(</span>index<span style="color:#999999">)</span><span style="color:#999999">;</span>
    <span style="color:#0077aa">return</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">String</span><span style="color:#999999">(</span>java<span style="color:#999999">.</span>util<span style="color:#999999">.</span>Base64<span style="color:#999999">.</span><span style="color:#dd4a68">getDecoder</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">.</span><span style="color:#dd4a68">decode</span><span style="color:#999999">(</span>value<span style="color:#999999">)</span><span style="color:#999999">,</span>utf8<span style="color:#999999">)</span><span style="color:#999999">;</span>
  <span style="color:#999999">&#125;</span>
<span style="color:#999999">&#125;</span>

</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">toDb方法用于将属性转化为列，pojo指入库的POJO对象，name是指其属性名称,可以调用BeetlSQL3提供的类BeanKit.getBeanProperty获取对象属性值</p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">toAttr将数据库转化为属性</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>@<span style="color:#dd4a68">Table</span><span style="color:#999999">(</span>name<span style="background-color:rgba(255, 255, 255, 0.5)">=</span><span style="color:#669900">"sys_user"</span><span style="color:#999999">)</span>
@Data
public  class <span style="color:#dd4a68">UserData</span><span style="color:#999999">&#123;</span>
  @AutoID
  Integer id<span style="color:#999999">;</span>
  @Base64
  String name<span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>

</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">另外一个例子，自定义Jackson注解</p> 
<pre><span style="color:#bbb529">@Data
</span><span style="color:#bbb529">@Table</span>(name=<span style="color:#6a8759">"json_test"</span>)
<span style="color:#cc7832">public class </span>JsonDataEntity &#123;
   <span style="color:#bbb529">@AssignID
</span><span style="color:#bbb529">   </span>String <span style="color:#9876aa">id</span><span style="color:#cc7832">;
</span><span style="color:#cc7832">   </span><span style="color:#bbb529">@Jackson
</span><span style="color:#bbb529">   @Column</span>(<span style="color:#6a8759">"json_data"</span>)
   Color <span style="color:#9876aa">jsonData</span><span style="color:#cc7832">;
</span>
&#125;
</pre> 
<p>@Jackson注解负责序列化和反序列化，定义如下，使用JacksonConvert</p> 
<pre>
<span style="color:#bbb529">@Retention</span>(RetentionPolicy.<em>RUNTIME</em>)
<span style="color:#bbb529">@Target</span>(value = &#123;ElementType.<em>METHOD</em><span style="color:#cc7832">, </span>ElementType.<em>FIELD</em>&#125;)
<span style="color:#bbb529">@Builder</span>(<span style="background-color:#f1c40f">JacksonConvert.</span><span style="color:#cc7832"><span style="background-color:#f1c40f">class</span></span>)
<span style="color:#cc7832">public </span>@<span style="color:#cc7832">interface </span><span style="color:#bbb529">Jackson </span>&#123;

&#125;
</pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">以toDb方法为例子</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>public class <span style="color:#dd4a68">JacksonConvert</span> implements <span style="color:#dd4a68">AttributeConvert</span> <span style="color:#999999">&#123;</span>
    ObjectMapper objectMapper <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">ObjectMapper</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">;</span>

    @Override
    public  Object <span style="color:#dd4a68">toDb</span><span style="color:#999999">(</span>ExecuteContext ctx<span style="color:#999999">,</span>  Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>String name<span style="color:#999999">,</span> Object dbValue<span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
        Object obj <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> BeanKit<span style="color:#999999">.</span><span style="color:#dd4a68">getBeanProperty</span><span style="color:#999999">(</span>dbValue<span style="color:#999999">,</span>name<span style="color:#999999">)</span><span style="color:#999999">;</span>
        <span style="color:#0077aa">if</span><span style="color:#999999">(</span>obj<span style="background-color:rgba(255, 255, 255, 0.5)">==</span><span style="color:#0077aa">null</span><span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
            <span style="color:#0077aa">return</span> <span style="color:#0077aa">null</span><span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span>
        <span style="color:#0077aa">try</span> <span style="color:#999999">&#123;</span>
            String str <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> objectMapper<span style="color:#999999">.</span><span style="color:#dd4a68">writeValueAsString</span><span style="color:#999999">(</span>obj<span style="color:#999999">)</span><span style="color:#999999">;</span>
            <span style="color:#0077aa">return</span> str<span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span> <span style="color:#0077aa">catch</span> <span style="color:#999999">(</span><span style="color:#dd4a68">JsonProcessingException</span> e<span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
            <span style="color:#0077aa">throw</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">IllegalArgumentException</span><span style="color:#999999">(</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span>
    <span style="color:#999999">&#125;</span>
    
<span style="color:#999999">&#125;</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"> 本次发布新增功能: AttributeConvert还能影响针对POJO自动生成的内置SQL语句，提供如下方法</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>default  String <span style="color:#dd4a68">toAutoSqlPart</span><span style="color:#999999">(</span>DBStyle dbStyle<span style="color:#999999">,</span>Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>AutoSQLEnum autoSQLEnum<span style="color:#999999">,</span> String name<span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
<span style="color:#0077aa">return</span> <span style="color:#0077aa">null</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">默认情况下，返回nul，不会影响自动生成语句，比如对于内置insert语句，生成的是</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#0077aa">insert</span> <span style="color:#0077aa">into</span> <span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span>  <span style="color:#0077aa">value</span><span style="color:#999999">(</span> <span style="color:#708090">#&#123;id&#125;,#&#123;jsonData&#125; )</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">在postgres数据库，如果json_data列使用了jsonb，那期望内置生成的insert sql语句是</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#0077aa">insert</span> <span style="color:#0077aa">into</span> <span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span>  <span style="color:#0077aa">value</span><span style="color:#999999">(</span> <span style="color:#708090">#&#123;id&#125;,#&#123;jsonData&#125;::JSON )</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">针对这个情况，可以<code>JacksonConvert</code><span> </span>可以重写toAutoSqlPart</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>default  String <span style="color:#dd4a68">toAutoSqlPart</span><span style="color:#999999">(</span>DBStyle dbStyle<span style="color:#999999">,</span>Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>AutoSQLEnum autoSQLEnum<span style="color:#999999">,</span> String name<span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
<span style="color:#0077aa">return</span> <span style="color:#669900">"$$::JSON"</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">这里的$$代表了属性占位符号，BeetlSQL的内置生成sql语句依据此生成合适的sql片段，如替换<code>$$</code>,生成<code>#&#123;jsonData&#125;::JSON</code>.</p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">可以参考源码例子 org.beetl.sql.postgres.JacksonConvert</p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"> </p> 
<p> </p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">JacksonConvert 实现了<span style="background-color:#ffff00">AttributeConvert</span>,以toDb为例子</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>public class <span style="color:#dd4a68">JacksonConvert</span> implements <span style="color:#dd4a68">AttributeConvert</span> <span style="color:#999999">&#123;</span>
    ObjectMapper objectMapper <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">ObjectMapper</span><span style="color:#999999">(</span><span style="color:#999999">)</span><span style="color:#999999">;</span>

    @Override
    public  Object <span style="color:#dd4a68">toDb</span><span style="color:#999999">(</span>ExecuteContext ctx<span style="color:#999999">,</span>  Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>String name<span style="color:#999999">,</span> Object dbValue<span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
        Object obj <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> BeanKit<span style="color:#999999">.</span><span style="color:#dd4a68">getBeanProperty</span><span style="color:#999999">(</span>dbValue<span style="color:#999999">,</span>name<span style="color:#999999">)</span><span style="color:#999999">;</span>
        <span style="color:#0077aa">if</span><span style="color:#999999">(</span>obj<span style="background-color:rgba(255, 255, 255, 0.5)">==</span><span style="color:#0077aa">null</span><span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
            <span style="color:#0077aa">return</span> <span style="color:#0077aa">null</span><span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span>
        <span style="color:#0077aa">try</span> <span style="color:#999999">&#123;</span>
            String str <span style="background-color:rgba(255, 255, 255, 0.5)">=</span> objectMapper<span style="color:#999999">.</span><span style="color:#dd4a68">writeValueAsString</span><span style="color:#999999">(</span>obj<span style="color:#999999">)</span><span style="color:#999999">;</span>
            <span style="color:#0077aa">return</span> str<span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span> <span style="color:#0077aa">catch</span> <span style="color:#999999">(</span><span style="color:#dd4a68">JsonProcessingException</span> e<span style="color:#999999">)</span> <span style="color:#999999">&#123;</span>
            <span style="color:#0077aa">throw</span> <span style="color:#0077aa">new</span> <span style="color:#dd4a68">IllegalArgumentException</span><span style="color:#999999">(</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">)</span><span style="color:#999999">;</span>
        <span style="color:#999999">&#125;</span>
    <span style="color:#999999">&#125;</span>
    
<span style="color:#999999">&#125;</span>
</code></pre> 
<p> </p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffff00">AttributeConvert</span>还能影响针对POJO自动生成的内置SQL语句，提供如下方法</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>default  String <span style="color:#dd4a68">toAutoSqlPart</span><span style="color:#999999">(</span>DBStyle dbStyle<span style="color:#999999">,</span>Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>AutoSQLEnum autoSQLEnum<span style="color:#999999">,</span> String name<span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
<span style="color:#0077aa">return</span> <span style="color:#0077aa">null</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">默认情况下，返回nul，不会影响自动生成语句，比如对于内置insert语句，生成的是</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#0077aa">insert</span> <span style="color:#0077aa">into</span> <span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span>  <span style="color:#0077aa">value</span><span style="color:#999999">(</span> <span style="color:#708090">#&#123;id&#125;,#&#123;jsonData&#125; )</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">在postgres数据库，如果json_data列使用了jsonb，那期望内置生成的insert sql语句是</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#0077aa">insert</span> <span style="color:#0077aa">into</span> <span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span><span style="color:#999999">.</span>  <span style="color:#0077aa">value</span><span style="color:#999999">(</span> <span style="color:#708090">#&#123;id&#125;,#&#123;jsonData&#125;::JSON )</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">针对这个情况，可以<code>JacksonConvert</code><span> </span>可以重写toAutoSqlPart</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>default  String <span style="color:#dd4a68">toAutoSqlPart</span><span style="color:#999999">(</span>DBStyle dbStyle<span style="color:#999999">,</span>Class <span style="color:#dd4a68">cls</span><span style="color:#999999">,</span>AutoSQLEnum autoSQLEnum<span style="color:#999999">,</span> String name<span style="color:#999999">)</span><span style="color:#999999">&#123;</span>
<span style="color:#0077aa">return</span> <span style="color:#669900">"$$::JSON"</span><span style="color:#999999">;</span>
<span style="color:#999999">&#125;</span>
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">这里的$$代表了属性占位符号，BeetlSQL的内置生成sql语句依据此生成合适的sql语句，如替换<code>$$</code>,生成<code>#&#123;jsonData&#125;::JSON</code>.</p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">可以参考源码例子 org.beetl.sql.postgres.JacksonConvert</p>
                                        </div>
                                      
</div>
            