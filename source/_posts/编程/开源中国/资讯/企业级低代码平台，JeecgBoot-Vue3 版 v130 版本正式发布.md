
---
title: '企业级低代码平台，JeecgBoot-Vue3 版 v1.3.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 10:40:00 GMT
thumbnail: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Jeecgboot-Vue3 采用 Vue3.0、Vite、 Ant-Design-Vue、TypeScript 等新技术方案，包括二次封装组件、utils、hooks、动态菜单、权限校验、按钮级别权限控制等功能。JeecgBoot 企业级的低代码平台对应的 vue3 前端版本！</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">强大的代码生成器让前后端代码一键生成！JeecgBoot 引领低代码开发模式 (OnlineCoding-> 代码生成 -> 手工 MERGE)， 帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.3.0 | 2022-06-27</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<p>Github</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3" target="_blank">https://github.com/jeecgboot/jeecgboot-vue3</a></li> 
 <li>后端：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
</ul> 
<p>Gitee</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端：<a href="https://gitee.com/jeecg/jeecgboot-vue3">https://gitee.com/jeecg/jeecgboot-vue3</a></li> 
 <li>后端：<a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue3.jeecg.com" target="_blank">http://vue3.jeecg.com</a></li> 
 <li>官方网站：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>在线演示：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot3.jeecg.com" target="_blank">http://boot3.jeecg.com</a></li> 
 <li>快速入门：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1V34y187Y9" target="_blank">入门视频</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue3.jeecg.com%2F2677352" target="_blank">代码生成</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">重大版本发布，全功能趋于稳定健壮。</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">升级 SQL</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#d73a49">UPDATE</span> sys_permission 
<span style="color:#d73a49">SET</span> del_flag = <span>1</span> 
<span style="color:#d73a49">WHERE</span> <span style="color:#d73a49">id</span> <span style="color:#d73a49">IN</span> (
<span style="color:#032f62">'1438108182116425729'</span>,
<span style="color:#032f62">'1438108183219527682'</span>,
<span style="color:#032f62">'1438108185660612609'</span>,
<span style="color:#032f62">'1438108185815801858'</span>,
<span style="color:#032f62">'1438108185958408193'</span>,
<span style="color:#032f62">'1438108186289758209'</span>
)
</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:left">重点升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>代码生成器提供 vue3 原生表单模板生成</li> 
 <li>代码生成器支持菜单 sql 生成</li> 
 <li>捕获接口超时异常，跳转到登录界面</li> 
 <li>JSwitch 组件当查询条件时的，query 模式下的重置问题</li> 
 <li>常用示例，报错优化</li> 
 <li>修改部门弹窗初始赋值问题</li> 
 <li>登录后选择租户和部门功能优化</li> 
 <li>单表原生组件示例添加</li> 
 <li>分类树添加的时候，下拉值不实时变更的问题 -</li> 
 <li>BasicTable 新增 alertAfter 插槽</li> 
 <li>JVxeTable “无痕刷新示例” 的 checkbox 无法自动更新</li> 
 <li>第一次加载时，点击第一个输入框，光标会跑到富文本输入框</li> 
 <li>下拉多选 JSelectMultiple，搜索时，查不到数据</li> 
 <li>[issues/54] 树字典，勾选，然后批量删除，系统错误</li> 
 <li>校验唯一方法修改 (必填校验)</li> 
 <li>修复路由添加时 Path 无法添加问题</li> 
 <li>用户选择单选 / 多选特殊处理</li> 
 <li>markdown 无法上传</li> 
 <li>列表配置要缓存</li> 
 <li>合并 vben 最新版代码，解决表格字段排序问题</li> 
 <li>系统编码规则，最后一个输入框不能删除</li> 
 <li>用户编辑负责部门后列表不刷新负责部门信息</li> 
 <li>【issues/69】JVxeTable 即时保存 demo 报错</li> 
 <li>【issues/I57GNY】批量删除后，批量操作按钮还处于显示状态</li> 
 <li>修复列表更多中，当只有一个菜单时显示多余分割线问题</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Issues 处理</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>jeecg-boot V3 的 RangePicker 类型，不能导出 excel<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I54815">#I54815</a></li> 
 <li>RangePicker 时间框<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I554DN">#I554DN</a></li> 
 <li>我的部门 - 添加已有用户 打不开<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F62" target="_blank">#62</a></li> 
 <li>VUE3 一对多情况本地测试可以使用打包之后一对多出现异常<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I55RB0">#I55RB0</a></li> 
 <li>账号头像为空时，默认头像路径加载找不到资源<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I559WB">#I559WB</a></li> 
 <li>登录页面，验证码不刷新问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F41" target="_blank">#41</a></li> 
 <li>[WebSocket] 连接发生错误<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I56UQP">#I56UQP</a></li> 
 <li>用户管理中连续点两次编辑租户配置就丢失了<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I56C5I">#I56C5I</a></li> 
 <li>菜单的排序不支持小数了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F56" target="_blank">#56</a></li> 
 <li>定时任务 tag 颜色反了<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5773O">#I5773O</a></li> 
 <li>jvxeTable demo 即时保存报错<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F69" target="_blank">#69</a></li> 
 <li>批量删除后，表格刷新，当前选中行丢失，但批量操作按钮还处于显示状态<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I57GNY">#I57GNY</a></li> 
 <li>表格列的配置（是否显示、冻结等）关闭页面后，再点击页面进入，配置丢失了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F66" target="_blank">#66</a></li> 
 <li>增加外部页面菜单，存在 #字符时不能跳转外部页面<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I58YS9">#I58YS9</a></li> 
 <li>用户管理，详情按钮<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I58HCG">#I58HCG</a></li> 
 <li>部门选择 JSelectDept 自定义值时，回显问题<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4ZEZA">#I4ZEZA</a></li> 
 <li>我的部门菜单 点击 添加已有用户 弹出用户列表没加载出来，报了错<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I59UHC">#I59UHC</a></li> 
 <li>按钮 Icon 更改不了， submitButtonOptions 按钮都是 显示查询 icon<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3737" target="_blank">#3737</a></li> 
 <li>用户管理处编辑了用户的负责部门后表格没有刷新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3650" target="_blank">#3650</a></li> 
 <li>用户管理处编辑了用户的部门后，表格没刷新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F53" target="_blank">#53</a></li> 
 <li>jvxetable 的 checkbox 自动更新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F84" target="_blank">#84</a></li> 
 <li>Markdown 编辑器在 Edge 浏览器中失效<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F89" target="_blank">#89</a></li> 
 <li>树字典，勾选，然后批量删除，系统错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F54" target="_blank">#54</a></li> 
 <li>树字典，行删除后，刷新并折叠，能否优化下不刷新整个页面<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F55" target="_blank">issues/#55</a></li> 
 <li>JPopup 示例还是不可以使用<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5B1QB">#I5B1QB</a></li> 
 <li>vue3 前端的一些小问题<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I50ODG">#I50ODG</a></li> 
 <li>online 表单开发 - 点击【配置地址】报错 - Uncaught ReferenceError: React is not defined<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5BFJT">#I5BFJT</a></li> 
 <li>用户具备多部门时，每次刷新浏览器，都会弹出【请选择部门】对话框<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I53LB9">#I53LB9</a></li> 
 <li>分步表单 按钮图标问题<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5BQM1">#I5BQM1</a></li> 
 <li><数据字典> 导入 / 导出功能，操作后提示没有传递 export.url/import.url 参数<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5AMDD">#I5AMDD</a></li> 
 <li>oauth2 钉钉无法登录<a href="https://gitee.com/jeecg/jeecg-boot/issues/I5BOUF">#I5BOUF</a></li> 
 <li>用户选择器不可用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F93" target="_blank">#93</a></li> 
 <li>标签页打开显示总是为：“AUTO 在线表单”，而不是为配置的菜单名称<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5C1F7">#I5C1F7</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装与使用</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Get the project code</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#005cc5">git</span> clone https://github.com/jeecgboot/jeecgboot-vue3.git
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Installation dependencies</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">cd</span> <span style="color:#032f62">jeecgboot-vue3</span>
<span style="color:#6f42c1">yarn</span> <span style="color:#032f62">install</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>配置后台接口地址</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">.env</span><span style="color:#6f42c1">.development</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>run</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">yarn</span> <span style="color:#032f62">serve</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>build</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">yarn</span> <span style="color:#032f62">build</span>
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统效果</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">系统后台</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142354.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142339.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142409.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142401.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_11.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Online 表单 & Online 报表 & 代码生成<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-e8862f2c3c14eace9090c20a8fb928234a4.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-e3b3a736236bc66f255a9a32ab3f9b7196b.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-221b8cbdea3c17d31a1365023a73d3d439f.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-14092f6f213b26ab145cf70b2dc6dec5635.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">报表效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201904/14160828_pkFr.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160834_Lo23.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160842_QK7B.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160849_GBm5.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160858_6RAM.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">接口文档</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e6ea09dbaa01b8458c2e23614077ba9507f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">流程设计 & 表单设计</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fe98e9f766e5abb6759f6f13d5f9186f0cf.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160917_9Ftz.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160633_u59G.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201907/05165142_yyQ7.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">报表设计</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-da89eb034b8583d57b3f61493fec313ed28.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-35deca9d020d61ad464accfdeb3bb90ba5c.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-d1695b4a53ebbc9e9651e309e5af1c8bd30.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-4cc634b612e97f08ab702ef34f2ede53f2a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">大屏模板</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201912/25133248_Ag1C.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201912/25133301_k9Kc.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-649cb79c01eb95d5c2217a5dad28515da82.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能模块</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Vue3 版已实现了系统管理、系统监控、报表、各种组件、前端权限、GUI 代码生成、Online 表单、Online 报表等平台功能。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─首页
│  ├─首页（四套首页满足不同场景需求）
│  ├─工作台
├─系统管理
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
│  └─对象存储
│  └─多租户管理
├─系统监控
│  ├─网关路由配置（<span style="color:#d73a49">gateway</span>）
│  ├─定时任务
│  ├─数据源管理
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─<span style="color:#d73a49">SQL</span>监控
│  ├─性能监控
│  │  ├─监控 <span style="color:#d73a49">Redis</span>
│  │  ├─<span style="color:#d73a49">Tomcat</span>
│  │  ├─<span style="color:#d73a49">jvm</span>
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
├─消息中心
│  ├─我的消息
│  ├─消息管理
│  ├─模板管理
├─积木报表设计器
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
├─代码生成器（<span style="color:#d73a49">GUI</span>）
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供<span style="color:#d73a49">4</span>套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带<span style="color:#d73a49">excel</span>导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─<span style="color:#d73a49">Excel</span>导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
│─常用示例
│  ├─自定义组件示例
│  ├─<span style="color:#d73a49">JVxeTable</span>示例(ERP行业复杂排版效果)
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多内嵌示例
│  └─异步树<span style="color:#d73a49">Table</span>
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─<span style="color:#d73a49">PDF</span>预览
│─封装通用组件
│  ├─行编辑表格<span style="color:#d73a49">JVxeTable</span>
│  └─省略显示组件
│  └─时间控件
│  └─高级查询 (未实现)
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
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  └─<span style="color:#d73a49">Mock</span>示例（子菜单很多）
│  └─页面<span style="color:#d73a49">&</span>导航（子菜单很多）
│  └─组件<span style="color:#d73a49">&</span>功能（子菜单很多）
├─高级功能
│  ├─支持微前端
│  ├─提供<span style="color:#d73a49">CAS</span>单点登录
│  ├─集成<span style="color:#d73a49">Websocket</span>消息通知机制
│  ├─支持第三方登录（<span style="color:#d73a49">QQ</span>、钉钉、微信等）
│  ├─系统编码规则
├─<span style="color:#d73a49">Online</span>在线开发
│  ├─<span style="color:#d73a49">Online</span>在线表单 
│  ├─<span style="color:#d73a49">Online</span>代码生成器
│  ├─<span style="color:#d73a49">Online</span>在线报表 
└─更多功能开发中。。
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">入门必备</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本项目需要一定前端基础知识，请确保掌握 Vue 的基础知识，以便能处理一些常见的问题。 建议在开发前先学一下以下内容，提前了解和学习这些知识，会对项目理解非常有帮助:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2F" target="_blank">Vue3 文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank">TypeScript</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnext.router.vuejs.org%2F" target="_blank">Vue-router</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2F2x.antdv.com%2Fdocs%2Fvue%2Fintroduce-cn%2F" target="_blank">Ant-Design-Vue</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvvbin.cn%2Fdoc-next" target="_blank">Vben 文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank">Es6</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitejs.dev%2F" target="_blank">Vitejs</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpinia.esm.dev%2Fintroduction.html" target="_blank">Pinia (vuex 替代方案)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs" target="_blank">Vue-RFCS</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fmigration%2Fintroduction.html" target="_blank">Vue2 迁移到 3</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">浏览器支持</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本地开发</strong>推荐使用<span> </span><code>Chrome 最新版</code>浏览器，<strong>不支持</strong><code>Chrome 80</code><span> </span>以下版本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>生产环境</strong>支持现代浏览器，不支持 IE。</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="IE" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png" referrerpolicy="no-referrer"></a>IE</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt=" Edge" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" referrerpolicy="no-referrer"></a>Edge</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Firefox" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" referrerpolicy="no-referrer"></a>Firefox</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Chrome" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" referrerpolicy="no-referrer"></a>Chrome</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Safari" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" referrerpolicy="no-referrer"></a>Safari</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">not support</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            