
---
title: 'Easy_Trans 1.1.9 版本发布，一个注解搞定字典_外键翻译'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-365196978ce8acca7dd71f3570677f08b80.bmp'
author: 开源中国
comments: false
date: Wed, 16 Feb 2022 10:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-365196978ce8acca7dd71f3570677f08b80.bmp'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left">1、升级内容</h1> 
<p>        A 新增多数据源支持</p> 
<p>           如果一个系统连接了多个数据库，可能user和order是2个库，order在翻译创建人的时候，就可以指定user数据源</p> 
<pre><code class="language-java"> @Trans(type = TransType.SIMPLE, target = User.class, fields = "userName", dataSource="User")
 private Long userId;</code></pre> 
<p>       B  优化自动查询SQL执行次数  </p> 
<p>      C bug fix  </p> 
<p>           解决跨微服务翻译，使用JPA 时主键数据类型问题</p> 
<p>           解决JPA 根据id查询，id匹配不到数据时候报错。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">2、介绍</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">   在项目开发中，借助JPA和Mybatis Plus我们已经可以做到单表查询不写SQL，但是很多时候我们需要关联字典表，关联其他表来实现字典码和外键的翻译，又要去写sql，使用 EasyTrans 你只需要在被翻译的pojo属性上加一个注解即可完成字典码/外键 翻译。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">先看效果：</p> 
<p>    <img alt height="182" src="https://oscimg.oschina.net/oscnet/up-365196978ce8acca7dd71f3570677f08b80.bmp" width="456" referrerpolicy="no-referrer"></p> 
<p>           </p> 
<p>     <span style="background-color:#ffffff; color:#40485b">easy trans适用于三种场景</span><br> <span style="background-color:#ffffff; color:#40485b">    1 我有一个id，但是我需要给客户展示他的title/name 但是我又不想做表关联查询</span><br> <span style="background-color:#ffffff; color:#40485b">    2 我有一个字典码 sex 和 一个字典值0 我希望能翻译成 男 给客户展示。</span><br> <span style="background-color:#ffffff; color:#40485b">    3 我有一组user id 比如 1，2,3 我希望能展示成 张三,李四,王五 给客户</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">食用步骤</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术经理/架构 需要做的事情</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1 、先把maven 引用加上</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>       <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy-trans-spring-boot-starter<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.1.9<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span>        <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Mybatis plus用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>        <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy_trans_mybatis_plus_extend<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.1.9<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span>        <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">JPA 用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>        <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy_trans_jpa_extend<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.1.9<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span>        <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2、在yaml中添加如下配置</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#008080"><span style="color:#6f42c1">easy-trans</span></span><span><span style="color:#6f42c1">:</span></span></span>
<span>   <span style="color:#008080"><span style="color:#6f42c1">autotrans</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#888888"><span style="color:#6a737d"># 如果没使用到autotrans可以不配置</span></span></span>
<span>       <span style="color:#888888"><span style="color:#6a737d">#您的service/dao所在的包 支持通配符比如com.*.**.service.**，他的默认值是com.*.*.service.impl</span></span></span>
<span>       <span style="color:#008080"><span style="color:#6f42c1">package</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#dd2200"><span style="color:#032f62">com.fhs.test.service.**;com.fhs.test.dao.**</span></span> </span>
<span>   <span style="color:#888888"><span style="color:#6a737d">#启用redis缓存 如果不用redis请设置为false</span></span></span>
<span>   <span style="color:#008080"><span style="color:#6f42c1">is-enable-redis</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#008080"><span style="color:#005cc5">true</span></span> </span>
<span>   <span style="color:#888888"><span style="color:#6a737d">#启用全局翻译(拦截所有responseBody进行自动翻译)，如果对于性能要求很高可关闭此配置</span></span></span>
<span>   <span style="color:#008080"><span style="color:#6f42c1">is-enable-global</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#008080"><span style="color:#005cc5">true</span></span> </span>
<span>   <span style="color:#888888"><span style="color:#6a737d">#启用平铺模式</span></span></span>
<span>   <span style="color:#008080"><span style="color:#6f42c1">is-enable-tile</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#008080"><span style="color:#005cc5">true</span></span></span>
<span><span style="color:#dd2200"><span style="color:#032f62">spring:#如果用到redis配置redis连接</span></span></span>
<span>  <span style="color:#dd2200"><span style="color:#6f42c1">redis</span></span><span><span style="color:#6f42c1">:</span></span></span>
<span>    <span style="color:#008080"><span style="color:#6f42c1">host</span></span><span><span style="color:#6f42c1">:</span></span> <span style="color:#dd2200"><span>192.168</span><span>.0</span><span>.213</span></span></span>
<span>    <span style="color:#008080"><span style="color:#6f42c1">port</span></span><span><span style="color:#6f42c1">:</span></span> <strong style="color:#0000dd"><span>6379</span></strong></span>
<span>    <span style="color:#008080"><span style="color:#6f42c1">password</span></span><span><span style="color:#6f42c1">:</span></span> <strong style="color:#0000dd"><span>123456</span></strong></span>
<span>    <span style="color:#008080"><span style="color:#6f42c1">database</span></span><span><span style="color:#6f42c1">:</span></span> <strong style="color:#0000dd"><span>0</span></strong></span>
<span>    <span style="color:#008080"><span style="color:#6f42c1">timeout</span></span><span><span style="color:#6f42c1">:</span></span> <strong style="color:#0000dd"><span>6000</span></strong></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3、如果不使用redis，请在启动类加禁用掉redis的自动配置类</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span>@<span style="color:#d73a49">SpringBootApplication</span></span><span>(</span><span><span style="color:#d73a49">exclude</span></span> <span>=</span> <span>&#123;</span> <strong style="color:#445588"><span style="color:#d73a49">RedisAutoConfiguration</span></strong><span><span style="color:#6f42c1">.</span></span><span style="color:#008080"><span style="color:#6f42c1">class</span></span> <span>&#125;)</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">4、初始化字典数据(如果你们项目没字典表请忽略)</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>       <span><span style="color:#6a737d">@Autowired</span></span>  <span style="color:#888888"><span style="color:#6a737d">//注入字典翻译服务</span></span></span>
<span>       <strong><span style="color:#d73a49">private</span></strong>  <strong style="color:#445588">DictionaryTransService</strong> <span>dictionaryTransService</span><span>;</span></span>
<span>       <span style="color:#888888"><span style="color:#6a737d">//在某处将字典缓存刷新到翻译服务中，以下是demo</span></span></span>
<span>       <strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588"><span>String</span></strong><span>,</span><strong style="color:#445588"><span>String</span></strong><span>></span> <span>transMap</span> <span>=</span> <strong style="color:#000000"><span style="color:#d73a49">new</span></strong> <strong style="color:#445588">HashMap</strong><span><>();</span></span>
<span>       <span>transMap</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200"><span style="color:#032f62">"0"</span></span><span>,</span><span style="color:#dd2200"><span style="color:#032f62">"男"</span></span><span>);</span></span>
<span>       <span>transMap</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200"><span style="color:#032f62">"1"</span></span><span>,</span><span style="color:#dd2200"><span style="color:#032f62">"女"</span></span><span>);</span></span>
<span>       <span>dictionaryTransService</span><span>.</span><span style="color:#008080">refreshCache</span><span>(</span><span style="color:#dd2200"><span style="color:#032f62">"sex"</span></span><span>,</span><span>transMap</span><span>);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">5、微服务配置(比如订单服务用到了用户服务的user数据来进行翻译，不牵扯微服务的可以不管)<br> A、白名单添加 /easyTrans/proxy/** 保证其不被拦截，RPC trans的时候easytrans会自动调用目标微服务的接口来获取数据。<br> B、应用之间的认证可以通过filter/interceptor实现，然后自定义RestTemplate 保证easytrans在请求用户服务的时候带上需要认证的参数</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">普通程序员需要做的事情</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">pojo 中添加</p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span><span style="color:#6a737d">@Data</span></span></span>
<span><span><span style="color:#6a737d">@Builder</span></span></span>
<span><span><span style="color:#6a737d">@AllArgsConstructor</span></span></span>
<span><span><span style="color:#6a737d">@NoArgsConstructor</span></span></span>
<span><span style="color:#888888"><span style="color:#6a737d">//实现TransPojo  接口，代表这个类需要被翻译或者被当作翻译的数据源</span></span></span>
<span><strong><span style="color:#d73a49">public</span></strong> <strong><span style="color:#d73a49">class</span></strong> <strong style="color:#445588">Student</strong> <strong><span style="color:#d73a49">implements</span></strong> <strong style="color:#445588">TransPojo</strong> <span>&#123;</span></span>
<span>     <span style="color:#888888"><span style="color:#6a737d">// 字典翻译 ref为非必填</span></span></span>
<span>    <span><span style="color:#6a737d">@Trans</span></span><span>(</span><span><span style="color:#d73a49">type</span></span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">DICTIONARY</span><span>,</span><span>key</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"sex"</span></span><span>,</span><span>ref</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"sexName"</span></span><span>)</span></span>
<span>    <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588">Integer</strong> <span>sex</span><span>;</span></span>

<span>    <span style="color:#888888"><span style="color:#6a737d">//这个字段可以不写，实现了TransPojo接口后有一个getTransMap方法，sexName可以让前端去transMap取</span></span></span>
<span>    <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588"><span>String</span></strong> <span>sexName</span><span>;</span></span>
<span>    </span>
<span>    <span style="color:#888888"><span style="color:#6a737d">//SIMPLE 翻译，用于关联其他的表进行翻译    schoolName 为 School 的一个字段</span></span></span>
<span>    <span><span style="color:#6a737d">@Trans</span></span><span>(</span><span><span style="color:#d73a49">type</span></span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">SIMPLE</span><span>,</span><span>target</span> <span>=</span> <strong style="color:#445588">School</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span>fields</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"schoolName"</span></span><span>)</span></span>
<span>    <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588"><span>String</span></strong> <span>schoolId</span><span>;</span></span>
<span></span>
<span><span style="color:#888888"><span style="color:#6a737d">//远程翻译，调用其他微服务的数据源进行翻译</span></span></span>
<span><span><span style="color:#6a737d">@Trans</span></span><span>(</span><span><span style="color:#d73a49">type</span></span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">RPC</span><span>,</span><span>targetClassName</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"com.fhs.test.pojo.School"</span></span><span>,</span><span>fields</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"schoolName"</span></span><span>,</span><span>serviceName</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"easyTrans"</span></span><span>,</span><span>alias</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"middle"</span></span><span>)</span></span>
<span>    <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588"><span>String</span></strong> <span>middleSchoolId</span><span>;</span></span>
<span></span>
<span><span style="color:#888888"><span style="color:#6a737d">// 枚举翻译，返回文科还是理科给前端</span></span></span>
<span><span><span style="color:#6a737d">@Trans</span></span><span>(</span><span><span style="color:#d73a49">type</span></span><span>=</span><strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">ENUM</span><span>,</span><span>key</span> <span>=</span> <span style="color:#dd2200"><span style="color:#032f62">"desc"</span></span><span>)</span></span>
<span>    <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588">StudentType</strong> <span>studentType</span> <span>=</span> <strong style="color:#445588">StudentType</strong><span>.</span><span style="color:#008080">ARTS</span><span>;</span></span>

<span>    <strong><span style="color:#d73a49">public</span></strong> <strong><span style="color:#d73a49">static</span></strong> <strong><span style="color:#d73a49">enum</span></strong> <strong style="color:#445588">StudentType</strong><span>&#123;</span></span>

<span>        <span style="color:#008080">ARTS</span><span>(</span><span style="color:#dd2200"><span style="color:#032f62">"文科"</span></span><span>),</span></span>
<span>        <span style="color:#008080">SCIENCES</span><span>(</span><span style="color:#dd2200"><span style="color:#032f62">"理科"</span></span><span>);</span></span>

<span>        <strong><span style="color:#d73a49">private</span></strong> <strong style="color:#445588"><span>String</span></strong> <span>desc</span><span>;</span></span>
<span>        <strong style="color:#445588">StudentType</strong><span>(</span><strong style="color:#445588"><span>String</span></strong> <span>desc</span><span>)&#123;</span></span>
<span>            <strong style="color:#000000"><span style="color:#d73a49">this</span></strong><span>.</span><span style="color:#008080">desc</span> <span>=</span> <span>desc</span><span>;</span></span>
<span>        <span>&#125;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">然后访问你的controller，看返回结果。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">示例项目</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/fhs-opensource/easy_trans_springboot_demo">https://gitee.com/fhs-opensource/easy_trans_springboot_demo</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">插件文档</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/fhs-opensource/easy_trans/wikis/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B">https://gitee.com/fhs-opensource/easy_trans/wikis/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B</a></p>
                                        </div>
                                      
</div>
            