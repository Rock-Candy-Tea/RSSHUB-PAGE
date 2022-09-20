
---
title: 'EasyTrans 2.0.3 发布 让您少写30%的多表sql'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 17:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">更新内容：</strong></h1> 
<ul> 
 <li>字典翻译支持 集合翻译 比如爱好有篮球，足球  对应的code=[0,1]</li> 
 <li>添加国产orm beetl支持</li> 
</ul> 
<h1><span style="color:#333333">支持的ORM框架</span><strong style="color:#333333">：</strong></h1> 
<p><strong style="color:#333333">1、Mybatis Plus   </strong></p> 
<p><strong style="color:#333333">2、JPA    </strong></p> 
<p><strong style="color:#333333">3、 TK Mybatis </strong></p> 
<p><strong style="color:#333333">4、BeetlSQL</strong></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">组件介绍：</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">表里我们经常存放字典码，外键 。给前端展示的时候要展示字典描述 (比如 sex 0 代表男)，外键要显示 title/name (如 userid 1 要翻译为张三)。字典比较简单，很多项目都直接交给前端翻译，但是外键翻译是必须要后台来做的，最常见的做法就是 表 join ，这样又要自己写 sql 比较麻烦。使用 Easy Trans，只需要一个注解就可以搞定数据翻译。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>支持的场景：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>  字典翻译     把 sex 0 翻译为男</li> 
 <li>  普通外键翻译 / 唯一键翻译  框架使用 mp/jpa 能力自动帮你去执行 sql 根据外键查询 name/title 并且 set 到你的 vo 字段上</li> 
 <li>  跨微服务翻译   比如 order (订单服务)     user (用户服务) 是 2 个微服务，但是 order 要展示创建人姓名，表里只有 user id  可以使用跨微服务翻译</li> 
 <li>  枚举翻译   把枚举中的汉字给到前端</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Trans 注解：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> 程序员只需要掌握这一个注解就算熟练使用 EasyTrans 了，绝对不干让程序员掉更多头发的事情。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">@Data</span>
<span style="color:#6a737d">@Builder</span>
<span style="color:#6a737d">@AllArgsConstructor</span>
<span style="color:#6a737d">@NoArgsConstructor</span>
<span style="color:#6a737d">//实现TransPojo  接口，代表这个类需要被翻译或者被当作翻译的数据源</span>
<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> Student <span style="color:#d73a49">implements</span> TransPojo &#123;
     <span style="color:#6a737d">// 字典翻译 ref为非必填</span>
    <span style="color:#6a737d">@Trans</span>(<span style="color:#d73a49">type</span> = TransType.DICTIONARY,key = <span style="color:#032f62">"sex"</span>,ref = <span style="color:#032f62">"sexName"</span>)
    <span style="color:#d73a49">private</span> Integer sex;

    <span style="color:#6a737d">//这个字段可以不写，实现了TransPojo接口后有一个getTransMap方法，sexName可以让前端去transMap取</span>
    <span style="color:#d73a49">private</span> <span>String</span> sexName;
    
    <span style="color:#6a737d">//SIMPLE 翻译，用于关联其他的表进行翻译    schoolName 为 School 的一个字段</span>
    <span style="color:#6a737d">@Trans</span>(<span style="color:#d73a49">type</span> = TransType.SIMPLE,target = School.class,fields = <span style="color:#032f62">"schoolName"</span>)
    <span style="color:#d73a49">private</span> <span>String</span> schoolId;

<span style="color:#6a737d">//远程翻译，调用其他微服务的数据源进行翻译</span>
<span style="color:#6a737d">@Trans</span>(<span style="color:#d73a49">type</span> = TransType.RPC,targetClassName = <span style="color:#032f62">"com.fhs.test.pojo.School"</span>,fields = <span style="color:#032f62">"schoolName"</span>,serviceName = <span style="color:#032f62">"easyTrans"</span>,alias = <span style="color:#032f62">"middle"</span>)
    <span style="color:#d73a49">private</span> <span>String</span> middleSchoolId;

<span style="color:#6a737d">// 枚举翻译，返回文科还是理科给前端</span>
<span style="color:#6a737d">@Trans</span>(<span style="color:#d73a49">type</span>=TransType.ENUM,key = <span style="color:#032f62">"desc"</span>)
    <span style="color:#d73a49">private</span> StudentType studentType = StudentType.ARTS;

    <span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">enum</span> StudentType&#123;

        ARTS(<span style="color:#032f62">"文科"</span>),
        SCIENCES(<span style="color:#032f62">"理科"</span>);

        <span style="color:#d73a49">private</span> <span>String</span> desc;
        StudentType(<span>String</span> desc)&#123;
            <span style="color:#d73a49">this</span>.desc = desc;
        &#125;
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：https://gitee.com/fhs-opensource/easy_trans</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">文档地址：https://gitee.com/fhs-opensource/easy_trans/wikis</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            