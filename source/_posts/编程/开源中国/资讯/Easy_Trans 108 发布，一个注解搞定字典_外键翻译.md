
---
title: 'Easy_Trans 1.0.8 发布，一个注解搞定字典_外键翻译'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 16:19:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left">1、升级内容</h1> 
<p>A 字典翻译添加国际化支持</p> 
<p>B 添加simple翻译，通过一个注解即可实现外键翻译 其他表的name/title 的功能。</p> 
<p>C 对所有返回responseBody的controller方法返回结果进行自动翻译</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">2、介绍</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在项目开发中，借助JPA和Mybatis Plus我们已经可以做到单表查询不写SQL，但是很多时候我们需要关联字典表，关联其他表来实现字典码和外键的翻译，又要去写sql，使用 EasyTrans 你只需要在被翻译的pojo属性上加一个注解即可完成字典码/外键 翻译。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">先看效果：</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0923/192412_492187e6_339743.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">easy trans适用于三种场景</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">A 我有一个id，但是我需要给前端展示他的title/name 但是我又不想做表关联查询</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">B  我有一个字典吗 sex 和 一个字典值0 我希望能翻译成 男 给前端展示。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">C 我有一组user id 比如 1，2,3 我希望能展示成 张三,李四,王五 给前端</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">3、食用步骤</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">技术经理/架构 需要做的事情 </h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1 、先把maven 引用加上</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>       <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy-trans-spring-boot-starter<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.0.8<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Mybatis plus用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>        <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy_trans_mybatis_plus_extend<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.0.8<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">JPA 用户另外还需要加以下扩展：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>        <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>com.fhs-opensource<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>easy_trans_jpa_extend<span style="color:#000080"></artifactId></span></span>
<span>            <span style="color:#000080"><version></span>1.0.8<span style="color:#000080"></version></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如果使用Redis请添加redis的引用(如果之前加过了请不要重复添加)</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>        <span style="color:#000080"><dependency></span></span>
<span>            <span style="color:#000080"><groupId></span>org.springframework.boot<span style="color:#000080"></groupId></span></span>
<span>            <span style="color:#000080"><artifactId></span>spring-boot-starter-data-redis<span style="color:#000080"></artifactId></span></span>
<span>        <span style="color:#000080"></dependency></span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2、在yaml中添加如下配置</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#008080">easy-trans</span><span>:</span></span>
<span>   <span style="color:#008080">autotrans</span><span>:</span></span>
<span>       <span style="color:#888888">#您的service/dao所在的包 支持通配符比如com.*.**.service.**，他的默认值是com.*.*.service.impl</span></span>
<span>       <span style="color:#008080">package</span><span>:</span> <span style="color:#dd2200">com.fhs.test.service.**;com.fhs.test.dao.**</span> </span>
<span>   <span style="color:#888888">#启用redis缓存 如果不用redis请设置为false</span></span>
<span>   <span style="color:#008080">is-enable-redis</span><span>:</span> <span style="color:#008080">true</span> </span>
<span>   <span style="color:#888888">#启用全局翻译(拦截所有responseBody进行自动翻译)，如果对于性能要求很高可关闭此配置</span></span>
<span>   <span style="color:#008080">is-enable-global</span><span>:</span> <span style="color:#008080">true</span> </span>
<span>  </span>
<span><span style="color:#dd2200">spring:#如果用到redis配置redis连接</span></span>
<span>  <span style="color:#dd2200">redis</span><span>:</span></span>
<span>    <span style="color:#008080">host</span><span>:</span> <span style="color:#dd2200">192.168.0.213</span></span>
<span>    <span style="color:#008080">port</span><span>:</span> <strong style="color:#0000dd">6379</strong></span>
<span>    <span style="color:#008080">password</span><span>:</span> <strong style="color:#0000dd">123456</strong></span>
<span>    <span style="color:#008080">database</span><span>:</span> <strong style="color:#0000dd">0</strong></span>
<span>    <span style="color:#008080">timeout</span><span>:</span> <strong style="color:#0000dd">6000</strong></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3、如果不使用redis，请在启动类加禁用掉redis的自动配置类</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@SpringBootApplication</span><span>(</span><span>exclude</span> <span>=</span> <span>&#123;</span> <strong style="color:#445588">RedisAutoConfiguration</strong><span>.</span><span style="color:#008080">class</span> <span>&#125;)</span></span></pre> 
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
 </div> 
</div> 
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
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">然后访问你的controller，看返回结果。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">参与贡献和技术支持</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">如果遇到使用问题可以加QQ群:976278956</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">示例项目</h1> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:left"><a href="https://gitee.com/fhs-opensource/easy_trans_springboot_demo">https://gitee.com/fhs-opensource/easy_trans_springboot_demo</a></p>
                                        </div>
                                      
</div>
            