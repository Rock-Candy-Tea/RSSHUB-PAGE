
---
title: 'EasyTrans 2.0.1 发布，您的业务代码还可以更少一些'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 14:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
---

<div>   
<div class="content">
                                                                                            <h1><strong style="color:#333333">更新内容：</strong></h1> 
<ul> 
 <li>修复AUTO 类型refs  多个字段问题</li> 
 <li>添加翻译缓存，减少DB查询次数</li> 
</ul> 
<p>很开心的告诉大家，EasyTrans各种翻译都支持缓存啦，下面介绍具体用法，在贴代码之前先搞清楚几个全局概念：</p> 
<p>1、<span style="background-color:#ffffff; color:#40485b">isAccess  true 按照最后一次访问时间计算过期时间  false按照缓存新建时间计算过期时间</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">2、cacheSeconds 缓存过期时间，单位：秒</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">3、maxCache 最大缓存的数量，超过这个值会删除老缓存(根据缓存新建时间)，然后添加新缓存</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">SIMPLE和RPC 配置缓存</h2> 
<p><span style="background-color:#ffffff; color:#40485b">把2个翻译类注入进来，然后根据不同的数据类型配置不同的缓存配置。</span></p> 
<pre><code class="language-java">@Configuration
public class EasyTransCacheConfig implements InitializingBean &#123;
    @Autowired
    private SimpleTransService simpleTransService;
    @Autowired
    private RpcTransService rpcTransService;

    @Override
    public void afterPropertiesSet() throws Exception &#123;
        SimpleTransService.TransCacheSett cacheSett = new SimpleTransService.TransCacheSett();
        cacheSett.setCacheSeconds(10);
        cacheSett.setMaxCache(1000);
        cacheSett.setAccess(false);
        simpleTransService.setTransCache(School.class,cacheSett);
        simpleTransService.setTransCache(UserMp.class,cacheSett);
        rpcTransService.setTransCache(School.class.getName(),cacheSett);
        rpcTransService.setTransCache(UserMp.class.getName(),cacheSett);
    &#125;
&#125;</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start">AUTO 配置缓存</h2> 
<p><span style="background-color:#ffffff; color:#40485b">主要配置globalCache 设置为true</span></p> 
<pre><code class="language-java">@Service
@AutoTrans(namespace = "teacher",fields = &#123;"name","age"&#125;,
        defaultAlias = "teacher",globalCache = true,cacheSeconds = 10,maxCache = 100)
public class TeacherService implements AutoTransAble &#123;
   //其他代码
&#125;</code></pre> 
<h1><strong style="color:#333333">组件介绍：</strong></h1> 
<p><span style="background-color:#ffffff; color:#333333">表里我们经常存放字典码，外键 。给前端展示的时候要展示字典描述 (比如 sex 0 代表男)，外键要显示 title/name (如 userid 1 要翻译为张三)。字典比较简单，很多项目都直接交给前端翻译，但是外键翻译是必须要后台来做的，最常见的做法就是 表 join ，这样又要自己写 sql 比较麻烦。使用 Easy Trans，只需要一个注解就可以搞定数据翻译。</span></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>支持的场景：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>  字典翻译     把 sex 0 翻译为男</li> 
 <li>  普通外键翻译 / 唯一键翻译  框架使用 mp/jpa 能力自动帮你去执行 sql 根据外键查询 name/title 并且 set 到你的 vo 字段上</li> 
 <li>  跨微服务翻译   比如 order (订单服务)     user (用户服务) 是 2 个微服务，但是 order 要展示创建人姓名，表里只有 user id  可以使用跨微服务翻译</li> 
 <li>  枚举翻译   把枚举中的汉字给到前端</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Trans 注解：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> 程序员只需要掌握这一个注解就算熟练使用 EasyTrans 了，绝对不干让程序员掉更多头发的事情。</p> 
<pre><code class="language-java">@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
//实现TransPojo  接口，代表这个类需要被翻译或者被当作翻译的数据源
public class Student implements TransPojo &#123;
     // 字典翻译 ref为非必填
    @Trans(type = TransType.DICTIONARY,key = "sex",ref = "sexName")
    private Integer sex;

    //这个字段可以不写，实现了TransPojo接口后有一个getTransMap方法，sexName可以让前端去transMap取
    private String sexName;
    
    //SIMPLE 翻译，用于关联其他的表进行翻译    schoolName 为 School 的一个字段
    @Trans(type = TransType.SIMPLE,target = School.class,fields = "schoolName")
    private String schoolId;

//远程翻译，调用其他微服务的数据源进行翻译
@Trans(type = TransType.RPC,targetClassName = "com.fhs.test.pojo.School",fields = "schoolName",serviceName = "easyTrans",alias = "middle")
    private String middleSchoolId;

// 枚举翻译，返回文科还是理科给前端
@Trans(type=TransType.ENUM,key = "desc")
    private StudentType studentType = StudentType.ARTS;

    public static enum StudentType&#123;

        ARTS("文科"),
        SCIENCES("理科");

        private String desc;
        StudentType(String desc)&#123;
            this.desc = desc;
        &#125;
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：https://gitee.com/fhs-opensource/easy_trans</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">文档地址：https://gitee.com/fhs-opensource/easy_trans/wikis</p>
                                        </div>
                                      
</div>
            