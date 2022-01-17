
---
title: 'IoTLink 物联网综合业务支撑平台 V0.5.0 首次发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-737b548eb7f61a788113f4f7b4afb11c264.png'
author: 开源中国
comments: false
date: Mon, 17 Jan 2022 08:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-737b548eb7f61a788113f4f7b4afb11c264.png'
---

<div>   
<div class="content">
                                                                                            <p><strong>v0.5.0 更新说明：</strong></p> 
<p>首次提交版本代码，部分功能正在优化中，逐步释放开源</p> 
<p>欢迎大家给点个赞，<span style="background-color:#ffffff; color:#40485b">愿所有的物联网公司、物联网从业者、物联网开发者享受开源的魅力。让物联网在不久的将来更具工具化，为各行各业赋能创造。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">IoTLink基于 SpringBoot、Vue、Mybatis、RabbitMq、Mysql、Redis 等开发,支持物联网卡、物联网模组、卡+模组融合管理。提供状态、资费、客户、进销存、合同、订单、续费、充值、诊断、账单等功能。平台可同时接入中国移动、中国电信、中国联通、第三方物联网卡进行统一管理。逐步完善平台，助您快速接入物联网，让万物互联更简单。</span></p> 
<p style="text-align:center"><img alt height="416" src="https://oscimg.oschina.net/oscnet/up-737b548eb7f61a788113f4f7b4afb11c264.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>特别鸣谢：</strong><a href="https://gitee.com/y_project/RuoYi-Vue"><strong>RuoYi-Vue</strong></a><strong>，</strong><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FElemeFE%2Felement"><strong>element</strong></a><strong>，</strong><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin"><strong>vue-element-admin</strong></a><strong>，</strong><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Felunez%2Feladmin-web"><strong>eladmin-web</strong></a></p> 
<p>源码库地址：<a href="https://gitee.com/sdyunze/iotlink" target="_blank">https://gitee.com/sdyunze/iotlink</a></p> 
<p>演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdemo.5iot.cn%2F">http://demo.5iot.com</a></p> 
<p>演示账号/密码：5iot/123456</p> 
<p><span>后端结构</span></p> 
<blockquote> 
 <p> </p> 
 <pre style="margin-left:0; margin-right:0; text-align:left">com.yunze     
├── common            // 工具类
│       └── annotation                    // 自定义注解
│       └── config                        // 全局配置
│       └── constant                      // 通用常量
│       └── core                          // 核心控制
│       └── enums                         // 通用枚举
│       └── exception                     // 通用异常
│       └── filter                        // 过滤器处理
│       └── mapper                        // 数据持久化
│       └── utils                         // 通用类处理
├── framework         // 框架核心
│       └── aspectj                       // 注解实现
│       └── config                        // 系统配置
│       └── datasource                    // 数据权限
│       └── interceptor                   // 拦截器
│       └── manager                       // 异步处理
│       └── security                      // 权限控制
│       └── web                           // 前端控制
├── cAdmin            // 平台业务分离执行监听
│       └── system                       // 监听yunze-admin业务执行
├── yunze-generator   // 代码生成
├── yunze-quartz      // 定时任务
├── yunze-system      // 系统代码
├── yunze-admin       // 后台服务
├── yunze-ui          // 页面前端代码
</pre> 
</blockquote> 
<p><span style="background-color:#ffffff; color:#40485b">前端结构</span></p> 
<blockquote> 
 <pre style="margin-left:0; margin-right:0; text-align:left">├── build                      // 构建相关  
├── bin                        // 执行脚本
├── public                     // 公共文件
│   ├── favicon.ico            // favicon图标
│   └── index.html             // html模板
├── src                        // 源代码
│   ├── api                    // 所有请求
│   ├── assets                 // 主题 字体等静态资源
│   ├── components             // 全局公用组件
│   ├── directive              // 全局指令
│   ├── layout                 // 布局
│   ├── router                 // 路由
│   ├── store                  // 全局 store管理
│   ├── utils                  // 全局公用方法
│   ├── views                  // view
│   ├── App.vue                // 入口页面
│   ├── main.js                // 入口 加载组件 初始化等
│   ├── permission.js          // 权限管理
│   └── settings.js            // 系统配置
├── .editorconfig              // 编码格式
├── .env.development           // 开发环境配置
├── .env.production            // 生产环境配置
├── .env.staging               // 测试环境配置
├── .eslintignore              // 忽略语法检查
├── .eslintrc.js               // eslint 配置项
├── .gitignore                 // git 忽略项
├── babel.config.js            // babel.config.js
├── package.json               // package.json
└── vue.config.js              // vue.config.js
</pre> 
</blockquote>
                                        </div>
                                      
</div>
            