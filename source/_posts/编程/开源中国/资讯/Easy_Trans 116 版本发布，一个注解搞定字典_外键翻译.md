
---
title: 'Easy_Trans 1.1.6 版本发布，一个注解搞定字典_外键翻译'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 11:12:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left">1、升级内容</h1> 
<p>   A 新增枚举翻译   </p> 
<p>     配置type=TransType.ENUM  并且指定key 为desc 则会把 枚举的desc字段返回给前端</p> 
<pre><code class="language-java">    @Trans(type=TransType.ENUM,key = "desc")
    private StudentType studentType = StudentType.ARTS;

    public static enum StudentType&#123;

        ARTS("文科"),
        SCIENCES("理科");

        private String desc;
        StudentType(String desc)&#123;
            this.desc = desc;
        &#125;
    &#125;</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">2、介绍</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在项目开发中，借助JPA和Mybatis Plus我们已经可以做到单表查询不写SQL，但是很多时候我们需要关联字典表，关联其他表来实现字典码和外键的翻译，又要去写sql，使用 EasyTrans 你只需要在被翻译的pojo属性上加一个注解即可完成字典码/外键 翻译。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">先看效果：</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">easy trans适用于三种场景<br> 1 我有一个id，但是我需要给客户展示他的title/name 但是我又不想做表关联查询<br> 2 我有一个字典码 sex 和 一个字典值0 我希望能翻译成 男 给客户展示。<br> 3 我有一组user id 比如 1，2,3 我希望能展示成 张三,李四,王五 给客户</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">食用步骤</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术经理/架构 需要做的事情</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在项目开发中，借助JPA和Mybatis Plus我们已经可以做到单表查询不写SQL，但是很多时候我们需要关联字典表，关联其他表来实现字典码和外键的翻译，又要去写sql，使用 EasyTrans 你只需要在被翻译的pojo属性上加一个注解即可完成字典码/外键 翻译。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">先看效果：</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">easy trans适用于四种场景<br> 1 我有一个id，但是我需要给客户展示他的title/name 但是我又不想做表关联查询<br> 2 我有一个字典码 sex 和 一个字典值0 我希望能翻译成 男 给客户展示。<br> 3 我有一组user id 比如 1，2,3 我希望能展示成 张三,李四,王五 给客户<br> 4 我有一个枚举，枚举里有一个title字段，我想给前端展示title的值 给客户</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">食用步骤</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术经理/架构 需要做的事情</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1 、先把maven 引用加上</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>       <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy-trans-spring-boot-starter<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.1.6<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Mybatis plus用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>        <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy_trans_mybatis_plus_extend<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.1.6<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">JPA 用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>        <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy_trans_jpa_extend<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.1.6<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">注意：非maven中央仓库更新可能延迟，如果高版本无法引入请尝试切到低一个版本过一天后在切回来。</span></p> 
<p> </p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2、在yaml中添加如下配置</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">easy-trans</span><span>:</span></span>
<span>   <span style="color:#008080">autotrans</span><span>:</span> <span style="color:#888888"># 如果没使用到autotrans可以不配置</span></span>
<span>       <span style="color:#888888">#您的service/dao所在的包 支持通配符比如com.*.**.service.**，他的默认值是com.*.*.service.impl</span></span>
<span>       <span style="color:#008080">package</span><span>:</span> <span style="color:#dd2200">com.fhs.test.service.**;com.fhs.test.dao.**</span> </span>
<span>   <span style="color:#888888">#启用redis缓存 如果不用redis请设置为false</span></span>
<span>   <span style="color:#008080">is-enable-redis</span><span>:</span> <span style="color:#008080">true</span> </span>
<span>   <span style="color:#888888">#启用全局翻译(拦截所有responseBody进行自动翻译)，如果对于性能要求很高可关闭此配置</span></span>
<span>   <span style="color:#008080">is-enable-global</span><span>:</span> <span style="color:#008080">true</span> </span>
<span>   <span style="color:#888888">#启用平铺模式</span></span>
<span>   <span style="color:#008080">is-enable-tile</span><span>:</span> <span style="color:#008080">true</span></span>
<span><span style="color:#dd2200">spring:#如果用到redis配置redis连接</span></span>
<span>  <span style="color:#dd2200">redis</span><span>:</span></span>
<span>    <span style="color:#008080">host</span><span>:</span> <span style="color:#dd2200">192.168.0.213</span></span>
<span>    <span style="color:#008080">port</span><span>:</span> <strong style="color:#0000dd">6379</strong></span>
<span>    <span style="color:#008080">password</span><span>:</span> <strong style="color:#0000dd">123456</strong></span>
<span>    <span style="color:#008080">database</span><span>:</span> <strong style="color:#0000dd">0</strong></span>
<span>    <span style="color:#008080">timeout</span><span>:</span> <strong style="color:#0000dd">6000</strong></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3、如果不使用redis，请在启动类加禁用掉redis的自动配置类</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@SpringBootApplication</span><span>(</span><span>exclude</span> <span>=</span> <span>&#123;</span> <strong style="color:#445588">RedisAutoConfiguration</strong><span>.</span><span style="color:#008080">class</span> <span>&#125;)</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">4、初始化字典数据(如果你们项目没字典表请忽略)</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>       <span>@Autowired</span>  <span style="color:#888888">//注入字典翻译服务</span></span>
<span>       <strong>private</strong>  <strong style="color:#445588">DictionaryTransService</strong> <span>dictionaryTransService</span><span>;</span></span>
<span>       <span style="color:#888888">//在某处将字典缓存刷新到翻译服务中，以下是demo</span></span>
<span>       <strong style="color:#445588">Map</strong><span><</span><strong style="color:#445588">String</strong><span>,</span><strong style="color:#445588">String</strong><span>></span> <span>transMap</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">HashMap</strong><span><>();</span></span>
<span>       <span>transMap</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"0"</span><span>,</span><span style="color:#dd2200">"男"</span><span>);</span></span>
<span>       <span>transMap</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"1"</span><span>,</span><span style="color:#dd2200">"女"</span><span>);</span></span>
<span>       <span>dictionaryTransService</span><span>.</span><span style="color:#008080">refreshCache</span><span>(</span><span style="color:#dd2200">"sex"</span><span>,</span><span>transMap</span><span>);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">5、微服务配置(比如订单服务用到了用户服务的user数据来进行翻译，不牵扯微服务的可以不管)<br> A、白名单添加 /easyTrans/proxy/** 保证其不被拦截，RPC trans的时候easytrans会自动调用目标微服务的接口来获取数据。<br> B、应用之间的认证可以通过filter/interceptor实现，然后自定义RestTemplate 保证easytrans在请求用户服务的时候带上需要认证的参数</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">普通程序员需要做的事情</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">pojo 中添加</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@Data</span></span>
<span><span>@Builder</span></span>
<span><span>@AllArgsConstructor</span></span>
<span><span>@NoArgsConstructor</span></span>
<span><span style="color:#888888">//实现TransPojo  接口，代表这个类需要被翻译或者被当作翻译的数据源</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">Student</strong> <strong>implements</strong> <strong style="color:#445588">TransPojo</strong> <span>&#123;</span></span>
<span>     <span style="color:#888888">// 字典翻译 ref为非必填</span></span>
<span>    <span>@Trans</span><span>(</span><span>type</span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">DICTIONARY</span><span>,</span><span>key</span> <span>=</span> <span style="color:#dd2200">"sex"</span><span>,</span><span>ref</span> <span>=</span> <span style="color:#dd2200">"sexName"</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>sex</span><span>;</span></span>

<span>    <span style="color:#888888">//这个字段可以不写，实现了TransPojo接口后有一个getTransMap方法，sexName可以让前端去transMap取</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>sexName</span><span>;</span></span>
<span>    </span>
<span>    <span style="color:#888888">//SIMPLE 翻译，用于关联其他的表进行翻译    schoolName 为 School 的一个字段</span></span>
<span>    <span>@Trans</span><span>(</span><span>type</span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">SIMPLE</span><span>,</span><span>target</span> <span>=</span> <strong style="color:#445588">School</strong><span>.</span><span style="color:#008080">class</span><span>,</span><span>fields</span> <span>=</span> <span style="color:#dd2200">"schoolName"</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>schoolId</span><span>;</span></span>
<span></span>
<span><span style="color:#888888">//远程翻译，调用其他微服务的数据源进行翻译</span></span>
<span><span>@Trans</span><span>(</span><span>type</span> <span>=</span> <strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">RPC</span><span>,</span><span>targetClassName</span> <span>=</span> <span style="color:#dd2200">"com.fhs.test.pojo.School"</span><span>,</span><span>fields</span> <span>=</span> <span style="color:#dd2200">"schoolName"</span><span>,</span><span>serviceName</span> <span>=</span> <span style="color:#dd2200">"easyTrans"</span><span>,</span><span>alias</span> <span>=</span> <span style="color:#dd2200">"middle"</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>middleSchoolId</span><span>;</span></span>
<span></span>
<span><span style="color:#888888">// 枚举翻译，返回文科还是理科给前端</span></span>
<span><span>@Trans</span><span>(</span><span>type</span><span>=</span><strong style="color:#445588">TransType</strong><span>.</span><span style="color:#008080">ENUM</span><span>,</span><span>key</span> <span>=</span> <span style="color:#dd2200">"desc"</span><span>)</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">StudentType</strong> <span>studentType</span> <span>=</span> <strong style="color:#445588">StudentType</strong><span>.</span><span style="color:#008080">ARTS</span><span>;</span></span>

<span>    <strong>public</strong> <strong>static</strong> <strong>enum</strong> <strong style="color:#445588">StudentType</strong><span>&#123;</span></span>

<span>        <span style="color:#008080">ARTS</span><span>(</span><span style="color:#dd2200">"文科"</span><span>),</span></span>
<span>        <span style="color:#008080">SCIENCES</span><span>(</span><span style="color:#dd2200">"理科"</span><span>);</span></span>

<span>        <strong>private</strong> <strong style="color:#445588">String</strong> <span>desc</span><span>;</span></span>
<span>        <strong style="color:#445588">StudentType</strong><span>(</span><strong style="color:#445588">String</strong> <span>desc</span><span>)&#123;</span></span>
<span>            <strong style="color:#000000">this</strong><span>.</span><span style="color:#008080">desc</span> <span>=</span> <span>desc</span><span>;</span></span>
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
            