
---
title: 'MineAdmin v0.6.1 已经发布，权限管理后台框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6354'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 15:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6354'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">[新增] 角色验证注解，支持多角色验证和条件验证(OR,AND)<br> [新增] 新增配置文件(config/autoload/mineadmin.php)，添加是否开启数据权限配置项<br> [新增] 代码生成器新增Tab组件，列表可为tab页面切换数据。感谢 kikigoper 贡献的代码<br> [新增] 新增了下载文件接口</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[变更] API接口授权的简易模式策略变更<br> [变更] 删除maResourceSelect资源选择器组件，改为使用scui系列组件<br> [变更] 代码生成器maResourceSelect变更为scui组件<br> [变更] 更换定时规则生成器为SCUI版<br> [变更] 载入common下公共函数库文件方式变更，不再使用composer.json的自动加载方式<br> [变更] 附件管理左侧目录管理变更为类型管理，类型可通过字典维护</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[修复] 定时任务rule字段长度不够导致保存或更新失败问题<br> [修复] 部分页面在移动端显示异常问题<br> [修复] 安装系统命令数据库端口参数丢失问题，感谢Bruce-K 贡献的代码<br> [修复] 前端index.html提示浏览器版本过低乱码问题<br> [修复] 多参数注解在原生注解下不生效的问题<br> [修复] 自增ID模型在新增失败的问题<br> [修复] 编辑器上传图片后回显问题<br> [修复] 彻底修复本地与第三方上传存储路径不一致问题</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[优化] 数据表设计器优化，默认第一个字段是主键ID<br> [优化] 多次打开装载数据表Modal后，勾选数据丢失问题<br> [优化] webscoket.js 开启心跳报错问题<br> [优化] 上传图片和上传文件超时时间改为默认30秒<br> [优化] 设置默认点击菜单数据即可打开子节点<br> [优化] 代码生成器生成目录改为强制模式<br> [优化] 更新到最新版hyperf，同步更新官方获取协程上下文命名空间地址</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">提示：更新到0.6.1版本方法</p> 
<ol> 
 <li>更新后端依赖，执行 composer update 命令</li> 
 <li>后端执行升级SQL命令：php bin/hyperf.php mine:update</li> 
 <li>更新前端依赖，执行 yarn 命令</li> 
</ol>
                                        </div>
                                      
</div>
            