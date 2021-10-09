
---
title: 'JeeSite V4.3.0.2 快速开发平台发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6287'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 21:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6287'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-right:0px"><span style="background-color:#ffffff; color:#333333">JeeSite Cloud v4.3.0.2 发布，具体更新内容如下：</span></p> 
<h1 style="margin-right:0">升级内容</h1> 
<ul> 
 <li>增加 Datagrid 的 options.gridMinMeight 最小高度设置</li> 
 <li>增加 web.securityMode 开关，控制一些风险功能的操作</li> 
 <li>优化 ztree 图标显示，可区分半选中状态</li> 
 <li>优化 oauth2 client 的超时时间，默认 30 秒</li> 
 <li>优化 Cloud 下或引入第三方插件的时候 Validator 可能会有冲突问题</li> 
 <li>优化 扩展 Lang 语言包时，如果没有定义的前端语言包，则不报错</li> 
 <li>优化 自定义登录页时，不在 adminPath 下的时候，地址不对问题</li> 
 <li>优化 uni-app h5 的流程图展示，可以拖拽</li> 
 <li>优化 Swagger Models 的扫描</li> 
 <li>修正 select2 禁用的时候，按空格可弹窗下拉框问题</li> 
 <li>修正 js.log 在 ie11 下报错兼容性问题</li> 
 <li>修正 Cloud 下消息内容可能会丢失问题</li> 
 <li>去掉 树表里的 parent 为空验证，因为无关紧要</li> 
 <li>字典 treeData 接口增加 cssClass 和 cssStyle 返回</li> 
 <li>菜单 获取菜单和权限接口增加 parentCode 参数返回</li> 
 <li>BPM 提交流程，自动完成相同处理人时，之前是读取的是全局表单，优化为如果有定义当前节点的流程选项，则读取当前节点的选项</li> 
 <li>BPM 增加根据流程 ids 和流程 keys 进行查询，支持 in 查询</li> 
 <li>BPM 修正 BpmTask 的 assigneeCode 显示不正确的问题</li> 
 <li>发布基于 Spring Authorization Server 的 OAuth2 服务端</li> 
 <li>升级 Shiro 1.8.0</li> 
 <li>CrudService 新增 updateStatusByIds 和 deleteByIds 批量方法</li> 
 <li>BPM 新增手机端风格的流程跟踪图和流程追踪界面</li> 
 <li>BPM 更正流程表单 URL 前面加<span> </span><code>///</code><span> </span>无效的问题</li> 
 <li>BPM 增加流程接口在线文档</li> 
 <li>对象存储：增加 baseDir 参数</li> 
 <li>字典接口：treeData 包含 status 为空的数据</li> 
 <li>文件管理：点击文件夹树刷新的时候，右侧列表显示根文件夹数据</li> 
 <li>模块管理：优化模块编码的验证，支持带减号，字母开头</li> 
 <li>layer.css 去掉top动画，不影响拖拽动作</li> 
 <li>form:checkbox 当 name 为空的时候不发送 !号开头的参数</li> 
 <li>国际化译文优化，访问日志国际化，感谢 SoleMan 分享</li> 
</ul> 
<h3>升级方法</h3> 
<ul> 
 <li>修改<span> </span><code>pom.xml</code><span> </span>文件中的<span> </span><code>jeesite-parent</code><span> </span>版本号为<span> </span><code>4.3.0-SNAPSHOT</code></li> 
 <li>如果你导入了<span> </span><code>jeesite-common</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你导入了<span> </span><code>jeesite-module-core</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</li> 
 <li>执行<span> </span><code>root/package.bat(sh)</code><span> </span>打包脚本，强制更新依赖即可。</li> 
</ul>
                                        </div>
                                      
</div>
            