
---
title: 'EasyTrans 1.2.4 发布，Mybatis Plus 多表关联外键翻译组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
author: 开源中国
comments: false
date: Fri, 06 May 2022 04:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg'
---

<div>   
<div class="content">
                                                                                            <p><strong>更新内容：</strong></p> 
<ul> 
 <li>     支持表唯一键字段代替主键翻译(比如excel导入填写用户手机号，插入数据库的时候需要userid)</li> 
 <li>     修复使用 @TransMethodResult 翻译方法返回值的时候，平铺不起作用的问题</li> 
 <li>     修复vo中有循环嵌套  会引发无限循环问题</li> 
</ul> 
<p><strong>插件介绍：</strong></p> 
<p><strong>       </strong>表里我们经常存放字典码，外键 给前端展示的时候要展示字典描述(比如 sex 0 代表男)，外键要显示title/name (如userid1 要翻译为张三)。字典比较简单，很多项目都直接交给前端翻译，但是外键翻译是必须要后台来做的，最常见的就是 表join ，这样又要自己写sql 比较麻烦。使用Easy Trans，只需要一个注解就可以搞定数据翻译。</p> 
<p>    <img alt src="https://oscimg.oschina.net/oscnet/up-acaec21fb4d5f58171162d215babe87e5fb.jpg" referrerpolicy="no-referrer"></p> 
<p><strong>支持的场景：</strong></p> 
<ul> 
 <li>  字典翻译     把sex 0翻译为男</li> 
 <li>  普通外键翻译/唯一键翻译  框架使用mp/jpa能力自动帮你去执行sql根据外键查询name/title 并且set到你的vo字段上</li> 
 <li>  跨微服务翻译   比如order集合user是2个微服务，但是order要展示创建人姓名，表里只有id  可以使用跨微服务翻译</li> 
 <li>  枚举翻译   把枚举中的汉字给到前端</li> 
</ul> 
<p><strong>Trans注解：</strong></p> 
<p> 程序员只需要掌握这一个注解就算熟练使用EasyTrans了，绝对不干让程序员掉更多头发的事情。</p> 
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
<p>项目地址：https://gitee.com/fhs-opensource/easy_trans</p> 
<p>文档地址：https://gitee.com/fhs-opensource/easy_trans/wikis</p>
                                        </div>
                                      
</div>
            