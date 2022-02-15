
---
title: 'JeeSite V4.3.3 发布：新增主题，快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-34f850aa7cc90fa1acb33a24b9a06a0e53e.png'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 10:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-34f850aa7cc90fa1acb33a24b9a06a0e53e.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start">升级内容</h3> 
<ul> 
 <li> <p>升级 spring boot 2.5.9、mybatis 3.5.9、jsqlparser 4.3、layer 3.5、laydate 5.3、支持 jdk17</p> </li> 
 <li> <p>增加 gen.checkTableExists 参数为 false 时候的友好提示</p> </li> 
 <li> <p>新增 yml 环境配置实例，如：application-prod.yml</p> </li> 
 <li> <p>新增系统管理员的默认角色，必选提示信息，增强体验</p> </li> 
 <li> <p>组织机构带用户接口算法优化，提升接口性能 50%</p> </li> 
 <li> <p>文件秒传、分片上传、多线程上传，放到标准版</p> </li> 
 <li> <p><strong>新增两套主题风格</strong>：亮蓝无界、浅蓝无界</p> </li> 
 <li> <p>TabPage 少于1个标签，自动隐藏标签栏</p> </li> 
 <li> <p>DataGrid 固定列锁定列支持鼠标滚动事件</p> </li> 
 <li> <p>DataGrid multiboxonly 选项优化，点击行的时候不进行选中或取消复选框</p> </li> 
 <li> <p>DataGrid 子表编辑 radio、checkbox 支持 class 属性传递</p> </li> 
 <li> <p>DataGrid 修正多级表头拖拽时有点错位的情况</p> </li> 
 <li> <p>DataGrid 增加表头高度调整实例</p> </li> 
 <li> <p>form:select 增加 dictIcon、dictStyle 属性，是否加载字典里设置的图标和样式</p> </li> 
 <li> <p>form:fileupload 文件上传 md5 验证时，可获取biz信息 v4.3.3+</p> </li> 
 <li> <p>laydate 回调函数支持接收参数，例如：data-done="function(value, date, endDate)&#123;&#125;"</p> </li> 
 <li> <p>laydate 新增 data-options 属性，例如：data-options="&#123;range: ['#startDate', '#endDate']&#125;"</p> </li> 
 <li> <p>Weixin 修正 getUserByWxOpenid 出现死循环问题</p> </li> 
 <li> <p>Log 日志差异比较，忽略 avatarBase64 较大的属性比较</p> </li> 
 <li> <p>BPM 增加 PC 表单和手机表单查看地址</p> </li> 
 <li> <p>BPM 流程标题脚本生成，支持获取流程变量</p> </li> 
 <li> <p>BPM 模型保存，防止数据库里 lastUpdatedBy 为空的时候报错</p> </li> 
 <li> <p>Cloud 新增 BpmCloudUtils 微服务环境下的 BPM 调用工具</p> </li> 
 <li> <p>Cloud 升级 sentinel 1.8.1</p> </li> 
 <li> <p>Cloud 多处细节优化</p> </li> 
</ul> 
<p><img height="957" src="https://oscimg.oschina.net/oscnet/up-34f850aa7cc90fa1acb33a24b9a06a0e53e.png" width="1809" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">升级方法</h3> 
<ul> 
 <li>修改<span> </span><code>pom.xml</code><span> </span>文件中的<span> </span><code>jeesite-parent</code><span> </span>版本号为<span> </span><code>4.3.3-SNAPSHOT</code></li> 
 <li>如果你导入了<span> </span><code>jeesite-common</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你导入了<span> </span><code>jeesite-module-core</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</li> 
 <li>升级了 layer 3.5 组件，查找替换 /3.1/layer.js 为 /3.5/layer.js</li> 
 <li>升级了 laydate 5.3 组件，查找替换 /5.0/laydate.js 为 /5.3/laydate.js</li> 
 <li>执行<span> </span><code>root/package.bat(sh)</code><span> </span>打包脚本，强制更新依赖即可。</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>进一步了解</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>JeeSite 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeesite.com" target="_blank">http://jeesite.com</a></li> 
 <li>JeeSite 在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesite.com" target="_blank">http://docs.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jeesite.com" target="_blank">http://demo.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.jeesite.com" target="_blank">http://vue.jeesite.com</a>  (Vue3分离版本)</li> 
 <li>JeeSite 源码下载：<a href="https://gitee.com/thinkgem/jeesite4" target="_blank">https://gitee.com/thinkgem/jeesite4</a></li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            