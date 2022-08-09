
---
title: 'fhs-framework 3.1 低代码快速开发平台更新，我们只想让普通程序员少写代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bc59122995fbe354e4062753dcd213d5d73.png'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 17:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bc59122995fbe354e4062753dcd213d5d73.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">更新内容：</strong></h1> 
<ul> 
 <li>PostgreSQL 支持(x_postgres分支)</li> 
 <li>pagex 组件集添加一对多插件</li> 
 <li>审计日志功能</li> 
 <li>表单填充(自测和测试神器，不用一个一个输入了)</li> 
</ul> 
<h4> 一对多<strong style="color:#333333">：</strong></h4> 
<p>篇幅有限，我们举一个最简单的例子,一个人，有多个手机号,使用PAGEX 主业务json 这么写：</p> 
<pre><code class="language-json">[
        &#123;
          type: "text",
          name: "name",
          label: "姓名"
        &#125;,
        &#123;
          type: "buttons",
          name: "buttons",
          buttons: [
            &#123;
              name: "加一行",//点击加一行后添加一行手机号输入
              click: function (_v,_model) &#123;
                _v.$refs.mobiles[0].addRow();
              &#125;
            &#125;
           ]
       &#125;,
         &#123;
          type: "one2x",
          name: "mobiles",
          defaultValue:&#123;
            operator,:'chinaMobile',//运营商默认选中移动
          &#125;,
          //当数据发生改变的时候触发
          onDataChange:(_newDatas)=>&#123;
              this.$refs.userForm.setModelProp('total',_newDatas.length);
          &#125;,
           controls: [
            &#123;
              type: 'select',
              name: 'operator',
              label: '运营商',
              rule: [&#123;  required: true, message: '请选择运营商', trigger: 'change' &#125;],
              dictCode: "operator",//运营商的字典码
            &#125;,
            &#123;
              type: 'text',
              name: 'mobile',
              label: '手机号',
              rule: [&#123;pattern: /^0?1(3|4|5|7|8)\d&#123;9&#125;$/, message: '请输入正确得手机号', trigger: 'blur'&#125;],
            &#125;
         ]
]</code></pre> 
<h4> 审计日志<strong style="color:#333333">：</strong></h4> 
<p>我们致力于显示能让用户和运维人员都能看懂的日志，我们使用了swagger属性名来替代字段名，并且对于一些字典/外键做了翻译。</p> 
<p>当然还有优化空间，我们会在后期的版本中继续优化。</p> 
<p><img height="320" src="https://oscimg.oschina.net/oscnet/up-bc59122995fbe354e4062753dcd213d5d73.png" width="1624" referrerpolicy="no-referrer"></p> 
<h4> 表单自动填充<strong style="color:#333333">：</strong></h4> 
<p>  我们很多项目表单有非常多的字段。这些字段有格式校验，重复校验，在造数据的时候非常麻烦，配合表单自动填充功能，可在开发和测试的时候一键填充表单内容，是不是很香。每个人的生命是宝贵的，应该减少无聊的活。</p> 
<p>支持：</p> 
<ol> 
 <li>根据正则来生成符合指定正则的字符串</li> 
 <li>内置了一些通用规则，包含：用户名，邮箱，身份证号码，url，ip，数字，日期，手机号，姓名，你可以自己在js里使用正则来扩展通用规则。</li> 
 <li>支持下拉框，checkbox，radio的自动选中(随机选)</li> 
 <li>支持程序员写死值</li> 
 <li>支持在生产环境能屏蔽掉 填充表单的按钮</li> 
</ol> 
<p>pagex使用表单填充功能的demo:</p> 
<pre><code class="language-json">[
                    &#123;
                        type: "text",
                        name: "userName",
                        label: "姓名",
                        rule: "required",
                        mock:'@name' //使用通用规则name来自动生成姓名
                    &#125;,
                    &#123;
                        type: "textarea",
                        name: "remark",
                        label: "备注",
                        mock:'我是备注' //写死值
                    &#125;,
]
</code></pre> 
<h1><strong style="color:#333333">FHS Framework介绍：</strong></h1> 
<p>fhs 基于大家常用的技术栈,SpringBoot Cloud Mybatis Plus Sa-Token ,Vue ElementUI等等，但是为了能让程序员减少编码(尤其是无任何意义的编码)，我们做了非常多的微创新。</p> 
<p><strong>1、翻译服务</strong></p> 
<p><strong>     </strong> 就一个注解，可以搞定大部分不需要关联过滤和统计的连表查询</p> 
<p>   <img alt="输入图片说明" src="https://gitee.com/fhs-opensource/easy_trans/raw/master/images/jieshao_temp.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<pre><code class="language-java"> // 字典翻译 ref为非必填
    @Trans(type = TransType.DICTIONARY,key = "sex",ref = "sexName")
    private Integer sex;

    //这个字段可以不写，实现了TransPojo接口后有一个getTransMap方法，sexName可以让前端去transMap取
    private String sexName;
    
    //SIMPLE 翻译，用于关联其他的表进行翻译    schoolName 为 School 的一个字段
    @Trans(type = TransType.SIMPLE,target = School.class,fields = "schoolName")
    private String schoolId;

//远程翻译，调用其他微服务的数据源进行翻译
@Trans(type = TransType.RPC,targetClassName = "com.fhs.test.pojo.School",fields = "schoolName",serviceName = "easyTrans",alias = "middle")
    private String middleSchoolId;</code></pre> 
<p>  </p> 
<p>本组件已经单独开源：https://gitee.com/fhs-opensource/easy_trans</p> 
<p>  </p> 
<p><strong>2、每一个业务都可以有一个牛逼的父类</strong></p> 
<p><strong>     </strong> 简单的业务，mapper，service，controller中不需要写业务代码，生成个空类即可，父类已经有所有功能了。</p> 
<p><strong>3、高级查询API</strong></p> 
<p><strong>     </strong>对于单表查询API，后端继承了父类后，前端都可以通过高级查询API自己拼接过滤条件,不需要写代码。</p> 
<pre><code class="language-json">&#123;
   "sorter":[&#123;//排序支持ASC和DESC
       "property":"userId",
       "direction":"DESC"
   &#125;],
   "querys":[&#123;//过滤条件 where sex=男 and (name=张三 or name=李四 )
         "property":"name", // po字段名
         "operator":"=",//操作符 
         "value":"张三",//操作值
         "relation":"OR",//关联关系AND OR
         "group":"nameGroup"//相同的group 外层会加括号
   &#125;,
   &#123;
         "property":"name",
         "operator":"=",
         "value":"李四",
         "relation":"OR",
         "group":"nameGroup"
   &#125;,&#123;
         "property":"sex", //使用了默认的关联关系AND 以及默认操作符 =
         "value":"男"
   &#125;]
&#125;</code></pre> 
<p>   后端也设计了安全字段，部分字段前端传了并不会起作用。</p> 
<p><strong>3、pagex vue组件集</strong></p> 
<p><strong>   </strong>pagex 组件基于elementUI为基础，集封装了常见的表单组件，程序员可以使用JSON来写组件代码，可以把表单和列表代码量减少60%+。</p> 
<p>   虽然pagex看起来很强大，实际他们只是几个vue文件而已，只要有vue组件开发经验的人都可以维护扩展它。</p> 
<p>   以下是一个DEMO，对字典分组进行增删改查，字典分组有名称和编码2个属性。</p> 
<p>  </p> 
<pre><code class="language-html"><template>

    <pagex-crudForm :namespace="namespace" :title="title" :crudSett="crudSett" :formSett="formSett" :idFieldName="idFieldName" >
    </pagex-crudForm>

</template>

<script>

export default &#123;
  name: "Dict",
  data() &#123;
    return &#123;
      namespace:'dictGroup',
      title:'字典分组',
      idFieldName:'groupId',//主键
      crudSett:&#123; // 列表配置
        api: '/basic/ms/dictGroup/pagerAdvance', //列表接口
        sortSett: [&#123;//排序
          "direction": "DESC",
          "property": "updateTime"
        &#125;],
        buttons: [//列表上的按钮
          &#123;
            title: '新增',
            name: 'add',
            code: "add",
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-plus', // 支持写click 自定义点击事件，新增组件会自带事件
          &#125;
        ],
        columns: [
          &#123;label: '分组名称', name: 'groupName'&#125;,//列 分组名称
          &#123;//分组编码列，点击之后跳转到字典项列表
            label: '分组编码', name: 'groupCode', type: 'formart',
            formart: "<label style='cursor:pointer'>$&#123;groupCode&#125;</label>",//格式化显示效果
            click: function (_row) &#123;
              this.$router.push(&#123;path: '/dict/type/data/',query:&#123;groupCode: _row.groupCode&#125;&#125;);
            &#125;
          &#125;,
          &#123;
            label: '操作',//操作列
            name: 'operation',
            type: 'textBtn',
            textBtn: [
              &#123;
                title: "编辑",
                type: "bottom",
                size: 'mini'
              &#125;,
              &#123;
                title: "详情",
                type: "success",
                size: 'mini'
              &#125;,
              &#123;
                title: "删除",
                type: "danger",
                size: 'mini',
                api: '/basic/ms/dictGroup/'
              &#125;
            ],
          &#125;
        ],
        filters: [//过滤条件
          &#123;label: '分组名称:', name: 'groupName', placeholder: "分组名称", type: 'text', operation: 'like'&#125;,//like 是后台过滤规则，模糊匹配 支持> < != between like 等等
          &#123;label: '分组编码:', name: 'groupCode', placeholder: "分组编码", type: 'text', operation: 'like'&#125;
        ],
      &#125;,
      formSett:&#123;// 表单
        addApi: '/basic/ms/dictGroup/',//新增表单的url，默认的post 
        updateApi: '/basic/ms/dictGroup/',//修改表单的url 默认是post
        data:&#123;
           //这里写默认值，比如groupName:'默认编码'
        &#125;,
        controls:[//表单字段
          &#123;
            type: 'text',
            name: 'groupName',
            label: '分组名称',
            rule: 'required',
            placeholder: '请输入分组名称'
          &#125;, &#123;
            type: 'text',
            name: 'groupCode',
            label: '分组编码',
            rule: 'required',
            placeholder: '请输入分组编码'
          &#125;
        ]
      &#125;,
    &#125;
  &#125;,
  methods: &#123;
     //自定义方法
  &#125;
&#125;;
</script></code></pre> 
<p><strong>4、表单初始化</strong></p> 
<p><strong>  </strong> 本次更新里写了，这里不重复说明。</p> 
<p><strong>5、更简单的微服务调用</strong></p> 
<p>  只需要在服务提供者的service接口上<span style="background-color:#ffffff; color:#40485b">加@CloudMethod 即可完成接口暴露。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">  哪个微服务用到直接 Autowired service接口即可(把service接口和一些pojo单独放到模块中给其他模块依赖)。详情：</span><a href="https://gitee.com/fhs-opensource/easy_cloud">https://gitee.com/fhs-opensource/easy_cloud</a></p> 
<p><strong>6、ALL IN ONE 模式开发  微服务模式部署</strong></p> 
<p><strong>    </strong>在本地调试的时候只启动一个java进程debug，在部署测试环境和生产环境的时候使用微服务+网关模式部署。</p> 
<p>    大家都知道，微服务开发大家链接同一个注册中心的时候有很多让人 头疼的事情。fhs的这个小特性就避免了这些头疼的事情。</p>
                                        </div>
                                      
</div>
            