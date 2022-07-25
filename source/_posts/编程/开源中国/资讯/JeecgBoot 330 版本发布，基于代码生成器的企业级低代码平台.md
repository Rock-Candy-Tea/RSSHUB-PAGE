
---
title: 'JeecgBoot 3.3.0 版本发布，基于代码生成器的企业级低代码平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Mon, 25 Jul 2022 11:11:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">JeecgBoot 是一款企业级的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成！JeecgBoot 引领低代码开发模式 (OnlineCoding-> 代码生成 -> 手工 MERGE)， 帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v3.3.0 | 2022-07-25</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官方网站：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>技术文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
 <li>在线演示：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>新手入门：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fquickstart" target="_blank">http://jeecg.com/doc/quickstart</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">不兼容的升级点：Websocket 安全加强，增加 token 校验、接口签名拦截器的时间戳改造、System 模块重构大。平滑升级有难度，请仔细对比修改日志。</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">重点升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>websocket 安全加强，增加 token 校验</li> 
 <li>【签名改造】 解决 X-TIMESTAMP 时区问题</li> 
 <li>System 模块开展代码 p3c 规范扫描大重构</li> 
 <li>升级代码生成器，支持生成权限注解和菜单的 SQL</li> 
 <li>vue2 弹窗支持任意拖动位置</li> 
 <li>微服务模式下，多租户不支持问题修复</li> 
 <li>模板消息重构，提供全局统一推送接口（支持钉钉、企业微信、邮件、短信、系统消息）</li> 
 <li>提供数据脱敏注解</li> 
 <li>发现的 SQL 漏洞修复</li> 
 <li>Vue3 前端与后台版本号同步，功能也已经全部同步</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">后台问题</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>分表分库的 demo 以及分库分表整合案例的文档<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I52EN1">issues/I52EN1</a></li> 
 <li>签名校验中的时间校验有时区问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3482" target="_blank">issues/3482</a></li> 
 <li>websocket 服务端，存在性能和安全问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3278" target="_blank">issues/3278</a></li> 
 <li>代码生成模板中，前端代码多了一个结尾 </j-modal><a href="https://gitee.com/jeecg/jeecg-boot/issues/I53X5M">issues/I53X5M</a></li> 
 <li>post 请求 X_SIGN 签名拦截校验后报错，request body 为空<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I53J5E">issues/I53J5E</a></li> 
 <li>JwtFilter 中 ThreadLocal 需要及时清除<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2FI53J5E" target="_blank">issues/I53J5E</a></li> 
 <li>Online 表单开发，代码生成时选择 ERP 页面风格，vue2 前端文件错误<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I54TAK">issues/I54TAK</a></li> 
 <li>category/loadOne 接口问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3663" target="_blank">issues/3663</a></li> 
 <li>3.2.0 用 online 表单生成 erp 抛出异常<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I55OSQ">issues/I55OSQ</a></li> 
 <li>获取系统用户列表时，使用 SQL 注入生效<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3676" target="_blank">issues/3676</a></li> 
 <li>这块代码有 SQL 注入的风险<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3538" target="_blank">issues/3538</a></li> 
 <li>online 表单开发 功能测试和生成的代码结果不一致 bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3625" target="_blank">issues/3625</a></li> 
 <li>excel 导出导出转换器接口无法找到<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3708" target="_blank">issues/3708</a></li> 
 <li>seata 测试 product 服务启动失败<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I57ZUG">issues/I57ZUG</a></li> 
 <li>建议升级 fastjson 版本至 1.2.83，低版本爆出漏洞<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I58VD6">issues/I58VD6</a></li> 
 <li>字典接口存在 SQL 注入风险<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3713" target="_blank">issues/3713</a></li> 
 <li>@JRepeat 注解添加之后无法实现重复提交的拦截提示<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I59M95">issues/I59M95</a></li> 
 <li>路由网关无法添加 path 过滤<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I57I6O">issues/I57I6O</a></li> 
 <li>3.0 微服务版存在 Spring Cloud Gateway SpEL 表达式注入问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I55RTF">issues/I55RTF</a></li> 
 <li>生产 prod 的问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5A134">issues/I5A134</a></li> 
 <li>平台维护的路由网关菜单问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3763" target="_blank">issues/3763</a></li> 
 <li>3.2.0 rabbitma 发送延迟消息存在 5 秒中的间隔<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3755" target="_blank">issues/3755</a></li> 
 <li>Autopoi 字段 Type 文档与实际代码控制不一致<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3732" target="_blank">issues/3732</a></li> 
 <li>3.2 版本，跑测试用例代码抛出异常<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I561IU">issues/I561IU</a></li> 
 <li>DictAspect Jackson 序列化报错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3629" target="_blank">issues/3629</a></li> 
 <li>自动生成的后台接口 /exportXls 中直接使用 queryWrapper 过滤<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I58SM9">issues/I58SM9</a></li> 
 <li>拼写错误，JeeccgBaseConfig<a href="https://gitee.com/jeecg/jeecg-boot/issues/I5CMHC">issues/I5CMHC</a></li> 
 <li>SQL 增强 bug<a href="https://gitee.com/jeecg/jeecg-boot/issues/I5ATD8">issues/I5ATD8</a></li> 
 <li>多租户微服务之间调用找不到 tenant-id（自定义页面）<a href="https://gitee.com/jeecg/jeecg-boot/issues/I5AO20">issues/I5AO20</a></li> 
 <li>中转 HTTP 请求，解决跨域问题 bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3826" target="_blank">issues/3826</a></li> 
 <li>SQL 注入及盲注高风险<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5C3VP">issues/I5C3VP</a></li> 
 <li>数据权限规则问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3810" target="_blank">issues/3810</a></li> 
 <li>数据脱敏注解怎么用不了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3852" target="_blank">issues/3852</a></li> 
 <li>根据模板导出 excel，无法导出图片<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I59983">issues/I59983</a></li> 
 <li>指定带过滤条件的字典 table 在生成代码后失效<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5BNY9">issues/I59983</a></li> 
 <li>启动报错，单体应用升级至 V3.2.0 版本<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I55DJD">issues/I55DJD</a></li> 
 <li>启动报错：java.lang.ArrayIndexOutOfBoundsException: -1<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3653" target="_blank">issues/3653</a></li> 
 <li>项目启动后报错，数组下标越界<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I55PDE">issues/I55PDE</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Vue2 前端</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>online 在线生成小问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3420" target="_blank">issues/3420</a></li> 
 <li>通过 Online 表单开发后，数据达到 57 万后，导出的 excel 中提示超时<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4JRE8">issues/I4JRE8</a></li> 
 <li>代码生成 app 页面没有此 js<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4WFGF">issues/I4WFGF</a></li> 
 <li>character '@' that cannot start any token<a href="https://gitee.com/jeecg/jeecg-boot/issues/I4XI00">issues/I4XI00</a></li> 
 <li>vue 有些页面报错，但是在线演示的却没有<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4X63V">issues/I4X63V</a></li> 
 <li>JeecgBoot 一对多示例，表单删除<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4VYOC">issues/I4VYOC</a></li> 
 <li>项目运行起来后前端访问列表页下的角色列表和用户列表报错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3472" target="_blank">issues/3472</a></li> 
 <li>给新建用户赋予角色的逻辑漏洞<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3461" target="_blank">issues/3461</a></li> 
 <li>启动的时候提示信息<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I52HJC">issues/I52HJC</a></li> 
 <li>单标签页模式下，打开外部链接 报错误 “这是最后一页，不能再关闭了啦”<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3546" target="_blank">issues/3546</a></li> 
 <li>用户为上级 负责部门下拉框选项的数据没有数据，需要从普通切换到上级才能有数据<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I52Z8Z">issues/I52Z8Z</a></li> 
 <li>富文本编辑器在服务器图片上传是相对路径<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4BCC3">issues/I4BCC3</a></li> 
 <li>j-vxe-table 点击事件冲突问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I54E2M">issues/I54E2M</a></li> 
 <li>部门用户可以有 admin 权限的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3806" target="_blank">issues/3806</a></li> 
 <li>JTreeSelect 树形下拉框 (异步加载) 自定义查询条件 查询结果问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3709" target="_blank">issues/3709</a></li> 
 <li>下拉搜索框条件过滤<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5DAPN">issues/I5DAPN</a></li> 
 <li>内嵌子表风格 bug<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3800" target="_blank">issues/3800</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Vue3 前端</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>代码编辑器默认样式改成 idea 风格</li> 
 <li>支持企业微信 / 钉钉 oauth2 登录</li> 
 <li>角色支持首页配置</li> 
 <li>我的消息 -- 全部已读等接口报错<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F101" target="_blank">issues/3420</a></li> 
 <li>JTreeSelect 下拉树自定义组件 查询不到数据<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F96" target="_blank">issues/96</a></li> 
 <li>online 配置部门选择后编辑，查看数据应该显示部门名称，不是部门代码<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5F3P4">issues/I5F3P4</a></li> 
 <li>前端升级到 vue3 后，从企业微信和钉钉的工作台免登入失败<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5BG1I">issues/I5BG1I</a></li> 
 <li>Online 对接积木报表后不显示打印按钮<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3843" target="_blank">issues/3843</a></li> 
 <li>JVxeTypes.upload 文件上传的时候，触发不了编辑<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5FTO6">issues/I5FTO6</a></li> 
 <li>是否支持 OAuth2 登录<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5DJZ8">issues/I5DJZ8</a></li> 
 <li>附表问题控件类型问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3854" target="_blank">issues/3854</a></li> 
 <li>列表查看详情，富文本不能下拉<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5ABAO">issues/I5ABAO</a></li> 
 <li>顶部菜单混合模式 分割菜单点击 导航无法显示<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5BIPO">issues/I5BIPO</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Autopoi</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[issues/I4PU45] @excel 里面新增属性 fixedIndex</li> 
 <li>导入字典替换需要将 --- 替换成_，不然数据库会存</li> 
 <li>mybatis-plus 升级 时间字段变成了 jdk8 的 LocalDateTime，导致格式化失败</li> 
 <li>AutoPOI (Excel 工具)==>excel 根据模板导出功能<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3687" target="_blank">issues/3687</a></li> 
 <li>AutoPoi excel 导入 ImportParams 中没有 startSheetIndex 参数<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I57UPC">issues/I57UPC</a></li> 
 <li>autopoi 模板导出 Excel 功能，#fe: 横向遍历不好用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3328" target="_blank">issues/3328</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JeecgBoot?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">开源界 “小普元” 超越传统商业平台。引领低代码开发模式 (OnlineCoding-> 代码生成器 -> 手工 MERGE)，低代码开发同时又支持灵活编码， 可以帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高开发效率，节省成本，同时又不失灵活性。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用最新主流前后分离框架（SpringBoot+Mybatis-plus+Ant-Design+Vue），容易上手；代码生成器依赖性低，灵活的扩展能力，可灵活实现二次开发；</li> 
 <li>开发效率很高，采用代码生成器，单表数据模型和一对多 (父子表)、树列表等数据模型，增删改查功能自动生成，菜单配置直接使用（前端代码和后端代码都一键生成）；</li> 
 <li>代码生成器提供强大模板机制，支持自定义模板风格。目前提供四套风格模板（单表两套、一对多两套）</li> 
 <li>封装完善的用户、角色、菜单、组织机构、数据字典、在线定时任务等基础功能。强大的权限机制，支持访问授权、按钮权限、数据权限、表单权限等</li> 
 <li>零代码在线开发能力，在线配置表单、在线配置报表、在线配置图表、在线设计表单</li> 
 <li>常用共通封装，各种工具类 (定时任务，短信接口，邮件发送，Excel 导入导出等), 基本满足 80% 项目需求</li> 
 <li>简易 Excel 导入导出，支持单表导出和一对多表模式导出，生成的代码自带导入导出功能</li> 
 <li>集成简易报表工具，图像报表和数据导出非常方便，可极其方便的生成图形报表、pdf、excel、word 等报表；</li> 
 <li>采用前后分离技术，页面 UI 精美，针对常用组件做了封装：时间、行表格控件、截取显示控件、报表组件，编辑器等等</li> 
 <li>查询过滤器：查询功能自动生成，后台动态拼 SQL 追加查询条件；支持多种匹配方式（全匹配 / 模糊查询 / 包含查询 / 不匹配查询）；</li> 
 <li>数据权限（精细化数据权限控制，控制到行级，列表级，表单字段级，实现不同人看不同数据，不同人对同一个页面操作不同字段</li> 
 <li>在线配置报表（无需编码，通过在线配置方式，实现曲线图，柱状图，数据等报表）</li> 
 <li>页面校验自动生成 (必须输入、数字校验、金额校验、时间空间等);</li> 
 <li>提供单点登录 CAS 集成方案，项目中已经提供完善的对接代码</li> 
 <li>表单设计器，支持用户自定义表单布局，支持单表，一对多表单、支持 select、radio、checkbox、textarea、date、popup、列表、宏等控件</li> 
 <li>专业接口对接机制，统一采用 restful 接口方式，集成 swagger-ui 在线接口文档，Jwt token 安全验证，方便客户端对接</li> 
 <li>接口安全机制，可细化控制接口授权，非常简便实现不同客户端只看自己数据等控制</li> 
 <li>高级组合查询功能，在线配置支持主子表关联查询，可保存查询历史</li> 
 <li>提供各种系统监控，实时跟踪系统运行情况（监控 Redis、Tomcat、jvm、服务器信息、请求追踪、SQL 监控）</li> 
 <li>消息中心（支持短信、邮件、微信推送等等）</li> 
 <li>集成 Websocket 消息通知机制</li> 
 <li>提供 APP 发布方案：</li> 
 <li>支持多语言，提供国际化方案；</li> 
 <li>数据变更记录日志，可记录数据每次变更内容，通过版本对比功能查看历史变化</li> 
 <li>平台 UI 强大，实现了移动自适应</li> 
 <li>平台首页风格，提供多种组合模式，支持自定义风格</li> 
 <li>提供简单易用的打印插件，支持谷歌、IE 浏览器等各种浏览器</li> 
 <li>示例代码丰富，提供很多学习案例参考</li> 
 <li>采用 maven 分模块开发方式</li> 
 <li>支持菜单动态路由</li> 
 <li>权限控制采用 RBAC（Role-Based Access Control，基于角色的访问控制）</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统功能模块</h3> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─系统管理
│  ├─用户管理
│  ├─角色管理
│  ├─菜单管理
│  ├─权限设置（支持按钮权限、数据权限）
│  ├─表单权限（控制字段禁用、隐藏）
│  ├─部门管理
│  ├─我的部门（二级管理员）
│  └─字典管理
│  └─分类字典
│  └─系统公告
│  └─职务管理
│  └─通讯录
│  └─多租户管理
├─<span style="color:#d73a49">Online</span>在线开发(低代码)
│  ├─<span style="color:#d73a49">Online</span>在线表单 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>代码生成器 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>在线报表 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>在线图表(暂不开源)
│  ├─<span style="color:#d73a49">Online</span>图表模板配置(暂不开源)
│  ├─<span style="color:#d73a49">Online</span>布局设计(暂不开源)
│  ├─多数据源管理 <span style="color:#d73a49">-</span> 功能已开放
├─积木报表设计器(低代码)
│  ├─打印设计器 <span style="color:#d73a49">-</span> 功能已开放
│  ├─数据报表设计 <span style="color:#d73a49">-</span> 功能已开放
│  ├─图形报表设计(支持Echart) <span style="color:#d73a49">-</span> 功能已开放
│  ├─大屏设计器(暂不开源)
├─消息中心
│  ├─消息管理
│  ├─模板管理
├─代码生成器(低代码)
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供<span style="color:#d73a49">4</span>套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带<span style="color:#d73a49">excel</span>导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─<span style="color:#d73a49">Excel</span>导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
├─系统监控
│  ├─<span style="color:#d73a49">Gateway</span>路由网关
│  ├─性能扫描监控
│  │  ├─监控 <span style="color:#d73a49">Redis</span>
│  │  ├─<span style="color:#d73a49">Tomcat</span>
│  │  ├─<span style="color:#d73a49">jvm</span>
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
│  ├─定时任务
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─<span style="color:#d73a49">SQL</span>监控
│  ├─<span style="color:#d73a49">swagger-ui</span>(在线接口文档)
│─报表示例
│  ├─曲线图
│  └─饼状图
│  └─柱状图
│  └─折线图
│  └─面积图
│  └─雷达图
│  └─仪表图
│  └─进度条
│  └─排名列表
│  └─等等
│─大屏模板
│  ├─作战指挥中心大屏
│  └─物流服务中心大屏
│─常用示例
│  ├─自定义组件
│  ├─对象存储(对接阿里云)
│  ├─<span style="color:#d73a49">JVXETable</span>示例（各种复杂<span style="color:#d73a49">ERP</span>布局示例）
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多<span style="color:#d73a49">TAB</span>例子
│  └─内嵌<span style="color:#d73a49">table</span>例子
│  └─常用选择组件
│  └─异步树<span style="color:#d73a49">table</span>
│  └─接口模拟测试
│  └─表格合计示例
│  └─异步树列表示例
│  └─一对多<span style="color:#d73a49">JEditable</span>
│  └─<span style="color:#d73a49">JEditable</span>组件示例
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─<span style="color:#d73a49">PDF</span>预览
│  └─分屏功能
│─封装通用组件
│  ├─行编辑表格<span style="color:#d73a49">JEditableTable</span>
│  └─省略显示组件
│  └─时间控件
│  └─高级查询
│  └─用户选择组件
│  └─报表组件封装
│  └─字典组件
│  └─下拉多选组件
│  └─选人组件
│  └─选部门组件
│  └─通过部门选人组件
│  └─封装曲线、柱状图、饼状图、折线图等等报表的组件（经过封装，使用简单）
│  └─在线<span style="color:#d73a49">code</span>编辑器
│  └─上传文件组件
│  └─验证码组件
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  ├─各种高级表单
│  ├─各种列表效果
│  └─结果页面
│  └─异常页面
│  └─个人页面
├─高级功能
│  ├─系统编码规则
│  ├─提供单点登录<span style="color:#d73a49">CAS</span>集成方案
│  ├─提供<span style="color:#d73a49">APP</span>发布方案
│  ├─集成<span style="color:#d73a49">Websocket</span>消息通知机制
│─流程模块功能 (暂不开源)
│  ├─流程设计器
│  ├─在线表单设计
│  └─我的任务
│  └─历史流程
│  └─历史流程
│  └─流程实例管理
│  └─流程监听管理
│  └─流程表达式
│  └─我发起的流程
│  └─我的抄送
│  └─流程委派、抄送、跳转
│  └─。。。
└─其他模块
   └─更多功能开发中。。

</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统截图</h3> 
<p>PC 端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5a396adc1ff8f074082fa002b88b5915.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/69de4ca50e51c70b6e2f48a530be6eb3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/df82289dcc7326cdf7adc073d4feab3a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/b91d1ae6ff0177c728434150bc82a72a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5091f504924e235ca0d49196a686c643.png" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/320e78580453295b47c97f1c31d0c050.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/0f607ab82712c1f240aa14827091e94e.png" referrerpolicy="no-referrer"></p> 
<p>PAD 端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/0eba9d8fa3a4847599cfe940ff6a80d3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/7debc83021006b8fdae7f65378fd6492.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/2cc9e7b01a99248033bd5da69802842f.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/62f5720f2fd20b43bdccfaeb469d4460.png" referrerpolicy="no-referrer"></p> 
<p>报表效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/55d6dc8d7baef718d3032d6b6d1265ab.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/366b4070ca053dcbd267e0eaa2971950.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/f343d6821db09a2448baef238948a6ca.gif" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/4f5ffd3b8357185a0226b9c317bc2c55.png" referrerpolicy="no-referrer"></p> 
<p>大屏效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/60ae64fe29fd6ec26d75a225389b53dd.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎吐槽，欢迎 star~</p>
                                        </div>
                                      
</div>
            