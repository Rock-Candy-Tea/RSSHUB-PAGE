
---
title: 'Bee V1.17.0.7 支持 Harmony 和 Android 直接访问数据库，使用同一套 ORM 代码就够了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-db49be73b2bd43bec9f9437e6d7329006f8.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 11:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-db49be73b2bd43bec9f9437e6d7329006f8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong style="color:#333333">ORM Bee</strong><span style="background-color:#ffffff; color:#40485b"><span> </span><strong>简单易用，文件小，性能好</strong>；同时支持</span><strong style="color:#333333"><span> </span>Android 和 Harmony，还支持 JDBC (可在 JavaWeb 等开发中使用)。</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">在</span><strong style="color:#333333"><span> </span>Harmony 和 Android 两个环境</strong><span style="background-color:#ffffff; color:#40485b"><span> </span>, 可以用</span><strong style="color:#333333">同一套 Bee 代码访问 DB</strong><span style="background-color:#ffffff; color:#40485b">, 提高代码重用，节省人力物。</span></p> 
<p><strong style="color:#3498db">Bee，互联网新时代的 Java ORM 工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p><strong style="color:#333333">V1.17.0.7 (有为)</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">1)</span><strong style="color:#40485b">支持HarmonyOS(鸿蒙)直接使用Bee访问SQLite数据库;</strong><br> <span style="background-color:#ffffff; color:#40485b">2)在</span><strong style="color:#40485b">Harmony和Android两个环境</strong><span style="background-color:#ffffff; color:#40485b">,可以用</span><strong style="color:#40485b">同一套Bee代码访问DB</strong><span style="background-color:#ffffff; color:#40485b">,提高代码重用,节省人力物力!</span></p> 
<p> </p> 
<p><strong>使用实例：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>一、将相关配置等信息注册到 Bee</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在启动的 Ability ，添加相应的配置和注册信息。 若有自定义的配置在 bee.properties 则需要；则需要使用：BeeConfigInit.init (); </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">将上下文注册到 Bee；将创建表和更新表的回调类，注册到 Bee；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以后就可以直接使用 Bee 了。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#d73a49">public</span> <span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">UserDataAbility</span> <span style="color:#d73a49">extends</span> <span style="color:#6f42c1">Ability</span> </span>&#123;
    <span style="color:#d73a49">private</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">final</span> String TAG = UserDataAbility<span>.<span style="color:#d73a49">class</span>.<span style="color:#6f42c1">getSimpleName</span>()</span>;
    <span style="color:#d73a49">private</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">final</span> HiLogLabel LABEL_LOG = <span style="color:#d73a49">new</span> HiLogLabel(<span>3</span>, <span>0xD000F00</span>, TAG);
    <span style="color:#6a737d">@Override</span>
    <span><span style="color:#d73a49">public</span> <span style="color:#d73a49">void</span> <span style="color:#6f42c1">onStart</span><span>(Intent intent)</span> </span>&#123;
        <span style="color:#d73a49">super</span>.onStart(intent);
        BeeConfigInit.init(); <span style="color:#6a737d">//若有自定义的配置在bee.properties则需要</span>
        ContextRegistry.register(<span style="color:#d73a49">this</span>.getApplicationContext()); <span style="color:#6a737d">//将上下文注册到Bee</span>
        RdbOpenCallbackRegistry.register(<span style="color:#d73a49">new</span> MyRdbOpenCallback()); <span style="color:#6a737d">//将创建表和更新表的回调类,注册到Bee</span>
<span style="color:#6a737d">//      BeeRdbStoreRegistry.register(rdbStore);  //直接注册rdbStore对象也可以.  但需要自己去生成,配置信息也不好管理</span>
    &#125;
&#125;</code></pre> 
<p>二、 其它配置 </p> 
<p><strong style="color:#333333">添加 jar 包；定义创建表和更新表的类 与一般工程用法一样。</strong></p> 
<p><strong style="color:#333333">三、使用Bee操作数据库</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以下是<span> </span><strong>select,update,insert,delete</strong><span> </span>操作的例子。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>主要语句如下：</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java">Suid suid = BF.getSuid();  //简单的<span style="color:#d73a49">select</span>,<span style="color:#d73a49">update</span>,<span style="color:#d73a49">insert</span>,<span style="color:#d73a49">delete</span>操作
suid.insert(p);
suid.delete(<span style="color:#d73a49">new</span> Person(), condition);
suid.update(p); //根据id修改对象
list = suid.select(<span style="color:#d73a49">new</span> Person());</code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><em><span style="color:#6a737d">//BF</span></em><em><span style="color:#6a737d">是</span></em><em><span style="color:#6a737d">BeeFactoryHelper</span></em><em><span style="color:#6a737d">的简称</span></em><em><span style="color:#6a737d">,</span></em><em><span style="color:#6a737d">也可以如下用法</span></em><em><span style="color:#6a737d">:</span>
</em><em><span style="color:#6a737d">//Suid suid=BeeFactoryHelper.getSuid();  </span></em>
</pre> 
<p>详细实例，请参照：</p> 
<p><a href="https://my.oschina.net/u/4111850/blog/5542608">https://my.oschina.net/u/4111850/blog/5542608</a></p> 
<p><strong>操作一万条数据性能（单位：毫秒）：</strong></p> 
<p><img height="811" src="https://oscimg.oschina.net/oscnet/up-db49be73b2bd43bec9f9437e6d7329006f8.png" width="386" referrerpolicy="no-referrer"></p> 
<p>其它情况对比:</p> 
<p><img height="258" src="https://oscimg.oschina.net/oscnet/up-8db0c3128345ecbae507932950adb3dc07e.png" width="1514" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由 Bee 框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与 DB 交互的编码工作量，是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的 Java 框架！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">(技术交流 扣群：992650213 ; 更多设计思想，请关注微信公众号：软件设计活跃区)</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee 简单易用：单表操作、多表关联操作，可以不用写 sql, 极少语句就可以完成 SQL 操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333"><span> </span>,10 分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee 功能强大：<strong>复杂查询也支持向对象方式，分页查询性能更高</strong>，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="background-color:#ffffff">高级要求，还可以方便自定义 SQL 语句</span></strong><span style="background-color:#ffffff">。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#c0392b"><strong>你还想添加什么功能，请到评论区告诉我们！</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p>
                                        </div>
                                      
</div>
            